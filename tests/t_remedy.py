"""Round 3: does the obvious fix for "picks the nearest option" work? Written after round 2, locked before running.

R01 adds a "not on the list" option to every argument and one "asks for something extra?" Noul to function calling.
R11 adds an "other kind of relative date" option and an "could this be read as two dates?" Noul to date extraction.
Each remedy is run on every round-1 and round-2 case for that job, so it must fix failures without breaking passes.
"""
import t_agents, t_extract, t_stress
from common import Test, top
from jev import noul, choice

NOT_LISTED = 'The request asks for a value that is not one of these.'
EXTRA = noul('Does `command` ask for anything beyond picking one action and its listed settings, such as a filter, a second table, a specific time or day, or a condition?')


def r01():
    t = Test('R01', 'Turn a plain-English request into the right action (with remedy)', 'Function calling')
    qs = {'__tool__': choice('What does the user in `command` want the data tool to do?', t_agents.FUNCS), 'extra': EXTRA}
    for k, (q, opts) in t_agents.ARGS.items():
        qs[k] = choice(q.replace('the user', 'the user in `command`', 1), {**opts, 'not_listed': NOT_LISTED})
    for k, q in t_agents.OPTIONAL.items():
        qs[k + '?stated'] = noul(q.replace('the user', 'the user in `command`', 1))
    for cid, kind, cmd, want in t_agents.J01_CASES + t_stress.S01:
        a = t.ask({'command': cmd}, qs)
        tool, confs, args = top(a['__tool__']), [a['__tool__']['confidence']], {}
        if tool != 'none_of_these':
            for k in t_agents.ARGS:
                fn, arg = k.split('.')
                if fn != tool or (k in t_agents.OPTIONAL and a[k + '?stated']['noul'] < 0.5):
                    continue
                args[arg] = top(a[k])
                confs.append(a[k]['confidence'])
        blocked = 'not_listed' in args.values() or a['extra']['noul'] >= 0.5
        runs = tool != 'none_of_these' and min(confs) >= t_agents.GATE and not blocked
        got = {'tool': tool, 'args': args, 'extra': round(a['extra']['noul'], 2), 'auto_runs': runs}
        ok = (not runs) if want is None else (runs and (tool, args) == want)
        t.case(cid, kind, 'do not run' if want is None else {'tool': want[0], 'args': want[1]}, got, ok)
    t.notes.append('Remedy: every argument menu gains "not on the list", plus one Noul asking whether the request wants anything extra; code refuses to run if either fires.')
    return t


def r11():
    t = Test('R11', 'Read a date from text and let code do the calendar maths (with remedy)', 'Date extraction')
    for cid, kind, doc, role, ok in t_extract.J11_CASES + t_stress.S11:
        qs = t_extract.date_questions(role)
        qs['anchor']['criteria'] = {**qs['anchor']['criteria'], 'other': 'Relative to something else, such as another date, an event or the end of a period.'}
        qs['ambiguous'] = noul(f'Could the {role} in `document` be read as two different calendar dates, for example because the day and month order is unclear?')
        a = t.ask({'document': doc}, qs)
        d, conf, why = t_extract.resolve(a)
        if top(a['anchor']) == 'other' and top(a['mode']) == 'relative':
            d, why = None, 'unsupported relative form'
        if a['ambiguous']['noul'] >= 0.5:
            d, why = None, 'ambiguous'
        if d is None and why == 'none':
            out = 'none'
        elif d is None or conf < t_extract.REVIEW_BELOW:
            out = 'review'
        else:
            out = d.isoformat()
        t.case(cid, kind, sorted(ok), {'outcome': out, 'why': why, 'ambiguous': round(a['ambiguous']['noul'], 2),
               'anchor': top(a['anchor'])}, out in ok)
    t.notes.append('Remedy: the "relative to" menu gains "something else", and a Noul flags dates that could be read two ways; code sends both to review.')
    return t


TESTS = [r01, r11]
