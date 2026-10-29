"""Runs all 21 tests, writes results/summary.json and results/RESULTS.md.

Usage: python run_all.py [J05 J11 ...]   (no arguments = all tests)
Reruns replay from results/cache.jsonl at no cost; only new or changed requests are paid.
"""
import hashlib, json, sys, traceback
from pathlib import Path
import jev, t_agents, t_classify, t_extract, t_search, t_technique, t_images

HERE = Path(__file__).parent
OUT = HERE / 'results'
TESTS = t_agents.TESTS + t_classify.TESTS + t_extract.TESTS + t_search.TESTS + t_technique.TESTS + t_images.TESTS


def lock():
    """Record the hash of every test file the first time, so later edits to expected answers are visible."""
    f = OUT / 'PREREGISTERED.json'
    if not f.exists():
        OUT.mkdir(exist_ok=True)
        f.write_text(json.dumps({p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                                 for p in sorted(HERE.glob('*.py'))}, indent=2))


def table(cases):
    rows = ['| Case | Kind | Expected | Got | Pass |', '|---|---|---|---|---|']
    fmt = lambda v: json.dumps(v, ensure_ascii=False).replace('|', '/')[:220]
    for c in cases:
        rows.append(f"| {c['id']} | {c['kind']} | {fmt(c['expected'])} | {fmt(c['got'])} | {'yes' if c['pass'] else '**no**'} |")
    return '\n'.join(rows)


def main(only):
    lock()
    prior = json.loads((OUT / 'summary.json').read_text()) if (OUT / 'summary.json').exists() else {}
    for fn in TESTS:
        tid = fn.__name__.upper()
        if only and tid not in only:
            continue
        try:
            prior[tid] = fn().summary()
        except Exception:
            prior[tid] = {'id': tid, 'error': traceback.format_exc(limit=3)}
        s = prior[tid]
        print(tid, s.get('core'), s.get('edge'), s.get('error', '')[-300:])
    (OUT / 'summary.json').write_text(json.dumps(prior, indent=1, ensure_ascii=False))
    lines = ['# Test results', '', f'Model `{jev.MODEL}`. Total paid so far: ${jev.spent():.4f}. Core = what the cookbook says Jev does; edge = probes a documented limit.', '',
             '| Test | Job | Core passed | Edge passed | Requests | Input tokens | Cost (USD) |', '|---|---|---|---|---|---|---|']
    for s in prior.values():
        if 'error' not in s:
            lines.append(f"| {s['id']} | {s['job']} | {s['core']} | {s['edge']} | {s['requests']} | {s['input_tokens']:,} | {s['cost_usd']:.5f} |")
    for s in prior.values():
        lines += ['', f"## {s['id']} {s.get('job', '')}", f"Cookbook: {s.get('cookbook', '')}", '']
        if 'error' in s:
            lines.append('```\n' + s['error'] + '\n```')
            continue
        lines += [f'- {n}' for n in s['notes']] + ['', table(s['cases'])]
    (OUT / 'RESULTS.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main(set(a.upper() for a in sys.argv[1:]))
