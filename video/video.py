"""The short video for VIDEO-SCRIPT.md, drawn with the same kit as the article figures.

Timing comes from build/timeline.json (written by voice.py): every scene cut and animation is keyed to the
moment its phrase is spoken, so pacing follows the voice rather than fixed seconds.
python video.py frames DIR   writes one SVG per frame (30 fps). Rendering and encoding: see make_video.ps1."""
import json, math, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'images'))
from kit import *

FPS = 30
TL = json.loads((Path(__file__).parent / 'build' / 'timeline.json').read_text())
DUR = TL['duration']
PH = TL['phrases']
SCENES = TL['scenes'] + [DUR]
S = lambda i: PH[i]['start']
E = lambda i: PH[i]['end']
BLUE, CYAN, VIOLET, MAGENTA, SLATE = (FAMILY[k][1] for k in ('agents', 'classify', 'extract', 'search', 'technique'))


def clamp(x):
    return max(0.0, min(1.0, x))


def ease(x):
    x = clamp(x)
    return 1 - (1 - x) ** 3


def prog(t, a, d):
    """0 -> 1 over d seconds starting at a, eased."""
    return ease((t - a) / d)


def window(t, a, b, fade=0.25):
    return clamp((t - a) / fade) * clamp((b - t) / fade)


def g(body, op=1.0, dx=0.0, dy=0.0, scale=1.0, cx=0, cy=0):
    if op <= 0.001:
        return ''
    tf = f'translate({dx:.1f},{dy:.1f})'
    if scale != 1.0:
        tf += f' translate({cx},{cy}) scale({scale:.3f}) translate({-cx},{-cy})'
    return f'<g opacity="{op:.3f}" transform="{tf}">{body}</g>'


def scene_alpha(t, i, fade=0.3):
    a, b = SCENES[i], SCENES[i + 1]
    if i == len(SCENES) - 2:
        return clamp((t - a) / fade)
    return clamp((t - a) / fade) * clamp((b - t) / fade) if i else clamp((b - t) / fade)


# ---------------------------------------------------------------- captions: the phrase being spoken
def caption(t):
    if t >= SCENES[5]:  # the closing words appear on screen as they are spoken
        return ''
    for i, p in enumerate(PH):
        nxt = PH[i + 1]['start'] if i + 1 < len(PH) else DUR
        if p['start'] - 0.05 <= t < nxt - 0.05:
            w = tw(p['text'], 30) + 56
            return rect(800 - w / 2, 808, w, 56, 28, '#FFFFFF', LINE, 1.5) + text(800, 846, p['text'], 30, INK, anchor='middle')
    return ''


# ---------------------------------------------------------------- 1: thousands of small calls
def paper(x, y, kind, accent, rot):
    body = rect(-90, -60, 180, 120, 8, CARD, LINE, 1.5) + rect(-90, -60, 6, 120, 3, accent) + text(-66, -26, kind, 19, MUTED)
    for i in range(3):
        body += rect(-66, -6 + i * 20, 120 - i * 26, 8, 4, LINE)
    return f'<g transform="translate({x},{y}) rotate({rot})">{body}</g>'


PILE = [(-330, 40, 'ticket', BLUE, -8), (-160, -20, 'invoice', VIOLET, 6), (10, 30, 'contract', MAGENTA, -4), (180, -30, 'record', CYAN, 9),
        (340, 30, 'ticket', BLUE, -6), (-250, 120, 'record', CYAN, 4), (-60, 110, 'invoice', VIOLET, -10), (120, 120, 'contract', MAGENTA, 7),
        (290, 115, 'ticket', BLUE, -3), (-390, -60, 'invoice', VIOLET, 11), (400, -70, 'record', CYAN, -9), (-120, -95, 'contract', MAGENTA, 3),
        (60, -110, 'ticket', BLUE, -7), (240, -120, 'invoice', VIOLET, 5)]


def s1(t):
    s = ''.join(g(paper(800 + x, 470 + y, k, ac, r), prog(t, 0.15 + i * 0.2, 0.5), 0, -60 * (1 - prog(t, 0.15 + i * 0.2, 0.5)))
                for i, (x, y, k, ac, r) in enumerate(PILE))
    p = prog(t, S(0) + 1.4, 0.6)
    s += g(text(800, 250, 'Thousands of small calls, every day', 52, INK, True, 'middle', display=True), p, 0, 12 * (1 - p))
    a = t * 360
    clock = (f'<circle cx="1450" cy="160" r="44" fill="{CARD}" stroke="{INK}" stroke-width="3"/>'
             f'<line x1="1450" y1="160" x2="{1450 + 32 * math.sin(math.radians(a)):.1f}" y2="{160 - 32 * math.cos(math.radians(a)):.1f}" '
             f'stroke="{VIOLET}" stroke-width="4" stroke-linecap="round"/><circle cx="1450" cy="160" r="5" fill="{INK}"/>')
    return s + g(clock, prog(t, 0.3, 0.4))


# ---------------------------------------------------------------- 2: three questions, each on its own words
def s2(t):
    s = ''
    oa = window(t, S(1) - 0.35, S(2) - 0.15)
    if oa:
        p = prog(t, S(1), 1.0)
        c1 = rect(0, 0, 520, 90, 10, CARD, LINE, 1.5) + text(28, 56, 'Acme Data Systems Inc., Austin', 28)
        c2 = rect(0, 0, 520, 90, 10, CARD, LINE, 1.5) + text(28, 56, 'ACME Data Sys, Austin', 28)
        s += g(g(c1, 1, 160 + 380 * p, 330) + g(c2, 1, 920 - 380 * p, 450), oa)
    ob = window(t, S(2) - 0.15, S(3) - 0.15)
    if ob:
        inv = rect(0, 0, 760, 330, 8, CARD, LINE, 1.5) + text(36, 58, 'INVOICE  HD-20431', 24, INK, True)
        for i, (lab, amt, b) in enumerate([('Total excl. VAT', '$3,820.00', False), ('VAT 20%', '$764.00', False), ('TOTAL DUE', '$4,584.00', True)]):
            y = 130 + i * 64
            inv += text(36, y, lab, 30 if b else 28, INK, b) + text(724, y, amt, 30 if b else 28, INK, b, 'end')
        p = prog(t, S(2) + 0.5, 0.8)
        L = 2 * (226 + 56)
        inv += (f'<rect x="512" y="218" width="226" height="56" rx="6" fill="none" stroke="{BOXC}" stroke-width="5" '
                f'stroke-dasharray="{L}" stroke-dashoffset="{L * (1 - p):.1f}"/>')
        s += g(inv, ob, 420, 250)
    oc = window(t, S(3) - 0.15, SCENES[2] + 0.3)
    if oc:
        d = rect(0, 0, 820, 380, 8, CARD, LINE, 1.5) + text(40, 56, '4. Backups', 26, INK, True)
        p = prog(t, S(3) + 0.6, 0.7)
        for i, ln in enumerate(['Backups are taken every 24 hours.', 'Backups are retained for 35 days.', 'Backups are stored in a different region.']):
            y = 130 + i * 80
            if i == 1:
                d += rect(24, y - 40, 772 * p, 58, 8, MAGENTA, op=0.9)
            d += text(48, y, ln, 30, '#FFFFFF' if (i == 1 and p > 0.6) else INK, i == 1 and p > 0.6)
        s += g(d, oc, 390, 230)
    return s


# ---------------------------------------------------------------- 3: Jev's answers, then the speed
def answer_card(x, y, q, a, sub, accent):
    s = rect(x, y, 420, 230, 12, CARD, LINE, 1.5) + rect(x, y, 420, 8, 4, accent) + text(x + 32, y + 66, q, 26, MUTED)
    cw = tw(a, 30, True) + 44
    s += rect(x + 32, y + 98, cw, 58, 29, accent) + text(x + 32 + cw / 2, y + 137, a, 30, '#FFFFFF', True, 'middle')
    return s + text(x + 32, y + 200, sub, 26, accent, True, display=True)


def s3(t):
    s = ''
    for i, (x, q, a, sub, ac) in enumerate([(140, 'Same company?', 'Yes', 'sure 0.91', MAGENTA), (590, 'Total due?', '$4,584.00', 'from three amounts', BOXC),
                                            (1040, 'Covers backups?', 'Line 17', 'answered 0.99', MAGENTA)]):
        p = prog(t, S(4) + 0.1 + i * 0.4, 0.45)
        s += g(answer_card(x, 300, q, a, sub, ac), p, 0, 30 * (1 - p))
    p = prog(t, S(4) + 1.6, 0.5)  # lands on "in a third of a second"
    watch = (f'<circle cx="0" cy="0" r="34" fill="{CARD}" stroke="{INK}" stroke-width="3"/><rect x="-8" y="-48" width="16" height="10" rx="3" fill="{INK}"/>'
             f'<line x1="0" y1="0" x2="{24 * math.sin(p * 2.1):.1f}" y2="{-24 * math.cos(p * 2.1):.1f}" stroke="{VIOLET}" stroke-width="4" stroke-linecap="round"/>')
    return s + g(f'<g transform="translate(660,640)">{watch}</g>' + text(716, 652, 'about 0.3 seconds each', 34, INK, True, display=True), p)


# ---------------------------------------------------------------- 4: your rules decide
def s4(t):
    box = rect(110, 380, 220, 140, 12, CARD, LINE, 1.5) + text(220, 460, 'answers', 28, MUTED, anchor='middle')
    s = f'<path d="M330,450 L700,450 C820,450 860,330 980,330 L1180,330" fill="none" stroke="{LINE}" stroke-width="10" stroke-linecap="round"/>'
    s += f'<path d="M700,450 C820,450 860,580 980,580 L1180,580" fill="none" stroke="{LINE}" stroke-width="10" stroke-linecap="round"/>'
    s = g(s, prog(t, SCENES[3], 0.4))
    s += g(tick(1240, 330, 40) + text(1300, 344, 'Act', 40, INK, True, display=True), prog(t, S(5) + 1.9, 0.4))  # on "act"
    s += g(person(1240, 580, 40) + text(1300, 594, 'Ask a person', 40, INK, True, display=True), prog(t, S(5) + 2.5, 0.4))  # on "ask a person"

    def along(u, low):
        if u < 0.45:
            return 330 + (700 - 330) * u / 0.45, 450
        v = (u - 0.45) / 0.55 * 0.9
        return 700 + (1180 - 700) * v, 450 + ((580 if low else 330) - 450) * (3 * v * v - 2 * v ** 3)
    for i, (lab, col, low) in enumerate([('sure 0.97', OK, False), ('sure 0.99', OK, False), ('sure 0.34', WARN, True),
                                         ('sure 0.95', OK, False), ('sure 1.00', OK, False)]):
        u = clamp((t - S(5) - 0.5 - i * 0.5) / 1.3)  # the last pill arrives before the scene changes
        if 0 < u < 1:
            x, y = along(u, low)  # constant speed so pills never bunch up on arrival
            w = tw(lab, 24, True) + 32
            s += g(rect(x - w / 2, y - 24, w, 48, 24, col) + text(x, y + 8, lab, 24, '#FFFFFF', True, 'middle'), clamp((1 - u) / 0.15))
    return s + g(box, prog(t, SCENES[3], 0.4))  # drawn last, so pills emerge from behind it


# ---------------------------------------------------------------- 5: how many, for how little
def s5(t):
    s = ''
    cx, cy = 1000, 430
    for i in range(36):
        u = clamp((t - S(6) - i * 0.06) / 1.2)
        if 0 < u < 1:
            e = ease(u)
            y0 = 250 + (i * 53 % 380)
            s += g(rect(-60, -22, 120, 44, 22, [BLUE, CYAN, VIOLET, MAGENTA, SLATE][i % 5]), 1 - 0.6 * e,
                   560 + (cx - 560) * e, y0 + (cy - y0) * e, 1 - 0.85 * e, 0, 0)
    p = prog(t, S(7) + 0.9, 0.5)  # lands on "three cents"
    coin = (f'<circle cx="{cx}" cy="{cy}" r="120" fill="{INK}"/><circle cx="{cx}" cy="{cy}" r="100" fill="none" stroke="#FFFFFF" stroke-width="4" opacity="0.6"/>'
            + text(cx, cy + 34, '3¢', 96, '#FFFFFF', True, 'middle', display=True))
    s += g(coin, p, 0, 0, 0.6 + 0.4 * p, cx, cy)
    n = int(1463 * prog(t, S(6) + 0.2, E(6) - S(6)))
    s += g(text(170, 420, f'{n:,}', 110, INK, True, display=True) + text(176, 478, 'test decisions', 34, MUTED), prog(t, S(6) - 0.2, 0.4))
    return s + g(text(176, 560, '$0.033 in total', 40, INK, True, display=True), prog(t, S(7) + 1.2, 0.5))


# ---------------------------------------------------------------- 6: the line, said and shown together
def s6(t):
    p1, p2, p3, p4 = prog(t, S(8) - 0.1, 0.5), prog(t, S(9) - 0.1, 0.5), prog(t, S(10) - 0.1, 0.5), prog(t, E(10) + 0.3, 0.6)
    s = g(text(800, 330, 'Jev judges.', 96, INK, True, 'middle', display=True), p1, 0, 16 * (1 - p1))
    s += g(text(800, 450, 'Your software decides.', 96, BLUE, True, 'middle', display=True), p2, 0, 16 * (1 - p2))
    s += g(text(800, 560, 'Keep your people for the calls that matter.', 36, MUTED, anchor='middle'), p3)
    return s + g(rect(640, 640, 320, 4, 2, LINE) + text(800, 700, 'Results and method: Jev, job by job', 26, INK, anchor='middle'), p4)


DRAW = [s1, s2, s3, s4, s5, s6]


def frame(t):
    body = ''.join(g(fn(t), scene_alpha(t, i)) for i, fn in enumerate(DRAW) if SCENES[i] - 0.3 <= t <= SCENES[i + 1] + 0.3)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1920" height="1080" viewBox="0 0 1600 900">
<rect width="1600" height="900" fill="{BG}"/>{body}{caption(t)}</svg>'''


if __name__ == '__main__':
    target = Path(sys.argv[2])
    target.mkdir(parents=True, exist_ok=True)
    for n in range(int(FPS * DUR)):
        (target / f'f{n:04d}.svg').write_text(frame(n / FPS), encoding='utf-8')
    print('frames', int(FPS * DUR), 'duration', DUR)
