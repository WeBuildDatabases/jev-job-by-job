"""Minimal Jev client for the jobs tests: pinned model, response cache, hard budget cap.

The key comes from TYPESAFE_API_KEY or ../../.env.local and is never printed or saved.
Every response is cached by request hash, so a rerun replays without paid calls.
"""
import base64, hashlib, io, json, os, time, urllib.error, urllib.request, uuid
from pathlib import Path

HERE = Path(__file__).resolve().parent
CACHE = HERE / 'results' / 'cache.jsonl'
MODEL = 'jev-1.14.0'
PRICE = 0.042 / 1e6  # USD per input token; output tokens are free
CAP = float(os.environ.get('JEV_JOBS_BUDGET_USD', '2.00'))

_cache = {}
if CACHE.exists():
    for line in CACHE.read_text(encoding='utf-8').splitlines():
        r = json.loads(line)
        _cache[r['hash']] = r


def spent():
    return sum(r['response']['usage']['input_tokens'] for r in _cache.values() if 'response' in r) * PRICE


def _key():
    key = os.environ.get('TYPESAFE_API_KEY')
    env = HERE.parents[1] / '.env.local'
    if not key and env.exists():
        for line in env.read_text().splitlines():
            if line.startswith('TYPESAFE_API_KEY='):
                key = line.split('=', 1)[1].strip().strip('"\'')
    assert key, 'Set TYPESAFE_API_KEY (or put it in .env.local at the study root).'
    return key


def image_asset(img):
    """PIL image -> (reference, asset). Reference is derived from the pixels so caching stays stable."""
    buf = io.BytesIO()
    img.convert('RGB').save(buf, 'PNG')
    data = buf.getvalue()
    ref = 'img-' + hashlib.sha256(data).hexdigest()[:16]
    return ref, {'type': 'image', 'format': 'png', 'data_base64': base64.b64encode(data).decode('ascii')}


def ask(state, questions, assets=None, tag=''):
    """One System One request. Returns {'answers', 'usage', 'seconds', 'cached'}."""
    body = {'model': MODEL, 'state': state, 'questions': questions}
    if assets:
        body['assets'] = assets
    raw = json.dumps(body, sort_keys=True, ensure_ascii=False).encode()
    digest = hashlib.sha256(raw).hexdigest()
    if digest in _cache:
        r = _cache[digest]
        return {**r['response'], 'seconds': r['seconds'], 'cached': True}
    # ponytail: worst-case reservation of 64k tokens per request; refine if the cap ever binds
    if spent() + 65536 * PRICE > CAP:
        raise RuntimeError(f'Budget stop: spent ${spent():.4f} of ${CAP:.2f}')
    headers = {'Authorization': 'Bearer ' + _key(), 'Content-Type': 'application/json'}
    if assets:
        headers['TypeSafe-Danger-Zone-Images'] = 'true'
    req = urllib.request.Request('https://api.typesafe.ai/v1/systemone', data=raw, headers=headers)
    t0 = time.perf_counter()
    try:
        with urllib.request.urlopen(req, timeout=180) as f:
            response = json.load(f)
    except urllib.error.HTTPError as e:
        # A failed call is an error, never an answer.
        raise RuntimeError(f'HTTP {e.code}: {e.read().decode("utf-8", "replace")[:500]}') from None
    seconds = time.perf_counter() - t0
    assert response['model'] == MODEL and set(response['answers']) == set(questions), 'Unexpected response shape'
    record = {'hash': digest, 'tag': tag, 'seconds': seconds, 'response': response}
    _cache[digest] = record
    CACHE.parent.mkdir(parents=True, exist_ok=True)
    with CACHE.open('a', encoding='utf-8') as f:
        f.write(json.dumps(record, ensure_ascii=False) + '\n')
    return {**response, 'seconds': seconds, 'cached': False}


def noul(text, true=None, false=None):
    q = {'type': 'noul', 'instructions': text}
    if true or false:
        q['criteria'] = {'true': true, 'false': false}
    return q


def choice(text, options):
    return {'type': 'choice', 'instructions': text, 'criteria': options}


def score(text, levels):
    return {'type': 'score', 'instructions': text, 'criteria': levels}


def box(text):
    return {'type': 'box', 'instructions': text}
