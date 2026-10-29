"""Records the voice-over phrase by phrase with Piper (local, open-source TTS) and builds the timeline.

vo_lines.txt: one phrase per line; a blank line starts a new beat (a new scene).
Writes build/vo_NN.wav, build/vo_mix.wav and build/timeline.json (phrase starts and ends, scene starts, duration).
Needs: pip install piper-tts, and a Piper voice (.onnx + .onnx.json). Set PIPER_VOICE to the .onnx path;
set PIPER_DEPS if piper-tts lives in a separate --target folder.
Voice used: en_US-john-medium (public domain, LibriVox recordings), from huggingface.co/rhasspy/piper-voices."""
import json, os, subprocess, sys, wave
from pathlib import Path

HERE = Path(__file__).parent
BUILD = HERE / 'build'
LEAD, IN_BEAT, BETWEEN_BEATS, TAIL = 0.5, 0.4, 0.75, 2.0  # seconds of silence
LENGTH_SCALE = os.environ.get('PIPER_LENGTH_SCALE', '1.0')  # >1 speaks slower


def beats():
    out, cur = [], []
    for line in (HERE / 'vo_lines.txt').read_text(encoding='utf-8').splitlines():
        if line.strip():
            cur.append(line.strip())
        elif cur:
            out.append(cur)
            cur = []
    return out + ([cur] if cur else [])


def say(text, path):
    env = dict(os.environ)
    if os.environ.get('PIPER_DEPS'):
        env['PYTHONPATH'] = os.environ['PIPER_DEPS']
    subprocess.run([sys.executable, '-m', 'piper', '-m', os.environ['PIPER_VOICE'], '-f', str(path),
                    '--length-scale', LENGTH_SCALE], input=text.encode(), env=env, check=True, capture_output=True)
    with wave.open(str(path)) as w:
        rate, data = w.getframerate(), w.readframes(w.getnframes())
    # trim the silence Piper pads around each phrase, keeping 40 ms either side, so pauses are only the ones we choose
    s = memoryview(data).cast('h')
    loud = [i for i in range(0, len(s), 64) if abs(s[i]) > 500]
    keep = int(0.04 * rate)
    a, b = max(0, loud[0] - keep), min(len(s), loud[-1] + keep)
    with wave.open(str(path), 'wb') as w:
        w.setnchannels(1), w.setsampwidth(2), w.setframerate(rate)
        w.writeframes(data[a * 2:b * 2])
    return (b - a) / rate, rate


def main():
    BUILD.mkdir(exist_ok=True)
    t, phrases, scenes, rate = LEAD, [], [], None
    n = 0
    for b, beat in enumerate(beats()):
        if b:
            t += BETWEEN_BEATS - IN_BEAT
        scenes.append(max(0.0, t - 0.4) if b else 0.0)
        for text in beat:
            wav = BUILD / f'vo_{n:02d}.wav'
            dur, rate = say(text, wav)
            phrases.append({'beat': b, 'text': text, 'start': round(t, 3), 'end': round(t + dur, 3), 'wav': wav.name})
            t += dur + IN_BEAT
            n += 1
    total = round(phrases[-1]['end'] + TAIL, 2)
    buf = bytearray(int(total * rate) * 2)
    for p in phrases:
        with wave.open(str(BUILD / p['wav'])) as w:
            data = w.readframes(w.getnframes())
        o = int(p['start'] * rate) * 2
        buf[o:o + len(data)] = data[:len(buf) - o]
    with wave.open(str(BUILD / 'vo_mix.wav'), 'wb') as w:
        w.setnchannels(1), w.setsampwidth(2), w.setframerate(rate)
        w.writeframes(bytes(buf))
    (BUILD / 'timeline.json').write_text(json.dumps({'duration': total, 'scenes': scenes, 'phrases': phrases}, indent=1))
    for p in phrases:
        print(f"{p['start']:6.2f}-{p['end']:6.2f}  {p['text']}")
    print('duration', total)


if __name__ == '__main__':
    main()
