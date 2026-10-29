"""Jobs 10-13: pulling values and structure out of messy text. Expected answers are fixed here before any call."""
import datetime as dt
import re
from common import Test, top
from jev import noul, choice

# ---------------------------------------------------------------- J10 extraction cascade (verify a cheap extractor)
SPEC = {'founded_year': 'The year the company was founded.',
        'employee_count': 'How many people the company employs.',
        'hq_city': 'The city where the company has its headquarters today.',
        'ceo_name': 'The name of the current chief executive.'}
J10_CASES = [  # (id, kind, page, cheap extraction, fields that are wrong)
    ('all_correct', 'core', 'Northwind Ledger was founded in 2011 in Bristol, where it is still headquartered. Today our 140 employees serve 2,300 customers. CEO: Amara Okafor.',
     {'founded_year': '2011', 'employee_count': '140', 'hq_city': 'Bristol', 'ceo_name': 'Amara Okafor'}, set()),
    ('invented_year', 'core', 'Pellucid Health builds scheduling software for clinics. Our Boston team of 85 is led by CEO Daniel Reyes.',
     {'founded_year': '2015', 'employee_count': '85', 'hq_city': 'Boston', 'ceo_name': 'Daniel Reyes'}, {'founded_year'}),
    ('customers_as_staff', 'core', 'Serving 10,000 customers worldwide from our Austin headquarters. Founded 2009. Chief executive: Lou Brandt.',
     {'founded_year': '2009', 'employee_count': '10000', 'hq_city': 'Austin', 'ceo_name': 'Lou Brandt'}, {'employee_count'}),
    ('missed_ceo', 'core', 'Corvid Analytics (Cambridge, founded 2017) employs 42 people. Our chief executive, Hana Sato, previously ran data at a bank.',
     {'founded_year': '2017', 'employee_count': '42', 'hq_city': 'Cambridge', 'ceo_name': ''}, {'ceo_name'}),
    ('truly_absent', 'core', 'Bluefin Analytics, headquartered in Leeds, was started in 2019 by CEO Ruth Adeyemi. We help retailers forecast demand.',
     {'founded_year': '2019', 'employee_count': '', 'hq_city': 'Leeds', 'ceo_name': 'Ruth Adeyemi'}, set()),
    ('wrong_executive', 'core', 'Halvorsen Data Supply, Leeds, is led by co-founders Priya Raman (CEO) and Tom Ellis (CTO). Founded 2004; 60 staff.',
     {'founded_year': '2004', 'employee_count': '60', 'hq_city': 'Leeds', 'ceo_name': 'Tom Ellis'}, {'ceo_name'}),
    ('inferred_year', 'edge', 'In 2024 Snowline Analytics celebrated its 10th anniversary. The Munich company has 230 employees and is run by CEO Jonas Weber.',
     {'founded_year': '2014', 'employee_count': '230', 'hq_city': 'Munich', 'ceo_name': 'Jonas Weber'}, set()),
    ('stale_city', 'edge', 'Founded in Dublin in 2012, Mercer Data moved its headquarters to Lisbon in 2020. 75 employees. CEO: Ana Costa.',
     {'founded_year': '2012', 'employee_count': '75', 'hq_city': 'Dublin', 'ceo_name': 'Ana Costa'}, {'hq_city'}),
]
FIRE = 0.7


def j10():
    t = Test('J10', 'Check a cheap extractor and escalate only the doubtful records', 'SDE cascade')
    wrong_accepts = 0
    for cid, kind, page, ext, bad in J10_CASES:
        qs = {}
        for f, v in ext.items():
            st = f'`extraction.{f}` (the field described by `field_specs.{f}`)'
            if v:
                qs[f + '::hallucinated'] = noul(f'Is the value of {st} not supported by `source_text`, either directly or by simple arithmetic from what it says?')
                qs[f + '::off_target'] = noul(f'Was the value of {st} taken from text in `source_text` that reports something other than what the field describes?')
            else:
                qs[f + '::absence_wrong'] = noul(f'Is {st} empty even though `source_text` contains that information?')
        a = t.ask({'source_text': page, 'field_specs': SPEC, 'extraction': ext}, qs)
        fired = sorted({k.split('::')[0] for k, v in a.items() if v['noul'] > FIRE})
        decision = 'escalate' if fired else 'accept'
        want = 'escalate' if bad else 'accept'
        wrong_accepts += bool(bad) and decision == 'accept'
        t.case(cid, kind, {'decision': want, 'wrong_fields': sorted(bad)},
               {'decision': decision, 'flagged_fields': fired,
                'max': {k: round(v['noul'], 2) for k, v in a.items() if v['noul'] > 0.3}}, decision == want)
    t.notes.append(f'Per-field Noul battery (2 checks per filled field, 1 per empty field), escalate if any > {FIRE}. Wrong records accepted: {wrong_accepts}.')
    return t

# ---------------------------------------------------------------- J11 date extraction
TODAY = dt.date(2026, 10, 28)  # a Wednesday, pinned so results replay
MONTHS = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october',
          'november', 'december']
DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']


def date_questions(role):
    r = f'the {role}'
    return {
        'mode': choice(f'How does `document` state {r}?', {
            'absolute': 'As a calendar date, possibly without the year.',
            'relative': 'Relative to today, such as today, tomorrow or next Tuesday.',
            'none': 'The document does not state this date.'}),
        'month': choice(f'In which month is {r} in `document`? Pick none if no month is stated.',
                        {**{m: m.title() for m in MONTHS}, 'none': 'No month stated.'}),
        'day': choice(f'On which day of the month is {r} in `document`? Pick none if no day number is stated.',
                      {**{f'd{i}': str(i) for i in range(1, 32)}, 'none': 'No day number stated.'}),
        'year': choice(f'In which year is {r} in `document`? Pick none if no year is stated, or out_of_range if a year is stated but not listed.',
                       {**{f'y{y}': str(y) for y in range(2000, 2041)}, 'out_of_range': 'A year outside the list.', 'none': 'No year stated.'}),
        'anchor': choice(f'If `document` states {r} relative to today, what is it relative to?', {
            'today': 'Today.', 'tomorrow': 'Tomorrow.', 'day_after': 'The day after tomorrow.',
            'weekday': 'A named day of the week.', 'none': 'Not stated relative to today.'}),
        'weekday': choice(f'Which day of the week names {r} in `document`, if any?',
                          {**{d: d.title() for d in DAYS}, 'none': 'No weekday named.'}),
        'week': choice(f'If {r} in `document` is a weekday, which week is meant?', {
            'current': 'This week, or a bare weekday such as "on Friday".', 'next': 'Next week, as in "next Thursday".',
            'none': 'No weekday named.'}),
    }


REVIEW_BELOW = 0.60


def resolve(a):
    """Code owns the calendar maths. Returns (date or None, confidence, reason)."""
    used = ['mode']
    mode = top(a['mode'])
    d = None
    if mode == 'absolute':
        used += ['month', 'day', 'year']
        m, day, y = top(a['month']), top(a['day']), top(a['year'])
        if m == 'none' or day == 'none' or y == 'out_of_range':
            return None, min(a[k]['confidence'] for k in used), 'incomplete'
        year = int(y[1:]) if y != 'none' else TODAY.year
        try:
            d = dt.date(year, MONTHS.index(m) + 1, int(day[1:]))
        except ValueError:
            return None, 0, 'impossible date'
        if y == 'none' and (TODAY - d).days > 31:
            d = d.replace(year=year + 1)
    elif mode == 'relative':
        used.append('anchor')
        anc = top(a['anchor'])
        if anc in ('today', 'tomorrow', 'day_after'):
            d = TODAY + dt.timedelta(days=['today', 'tomorrow', 'day_after'].index(anc))
        elif anc == 'weekday':
            used += ['weekday', 'week']
            wd, wk = top(a['weekday']), top(a['week'])
            if wd == 'none':
                return None, min(a[k]['confidence'] for k in used), 'incomplete'
            target = DAYS.index(wd)
            if wk == 'next':  # convention: the named day in the following Monday-to-Sunday week
                d = TODAY - dt.timedelta(days=TODAY.weekday()) + dt.timedelta(days=7 + target)
            else:
                d = TODAY + dt.timedelta(days=(target - TODAY.weekday()) % 7)
        else:
            return None, a['anchor']['confidence'], 'incomplete'
    return d, min(a[k]['confidence'] for k in used), mode


J11_CASES = [  # (id, kind, document, role, acceptable outcomes: ISO date, 'none' or 'review')
    ('explicit', 'core', 'This Order Form renews automatically on March 1, 2027.', 'date the order form renews', {'2027-03-01'}),
    ('no_year', 'core', 'Please return the signed DPA by 14 November.', 'deadline for returning the signed DPA', {'2026-11-14'}),
    ('next_tuesday', 'core', 'The migration window is next Tuesday from 22:00.', 'date of the migration window', {'2026-11-03'}),
    ('not_stated', 'core', 'Kick-off call: date to be confirmed.', 'date of the kick-off call', {'none', 'review'}),
    ('today', 'core', 'The survey closes today at 5pm.', 'date the survey closes', {'2026-10-28'}),
    ('twelve_months_later', 'edge', 'The Initial Term begins on the Effective Date, January 15, 2026, and renews automatically twelve months later.',
     'date the term renews', {'2027-01-15', 'review'}),
    ('ambiguous_numeric', 'edge', 'Renewal: 03/04/2027', 'renewal date', {'review'}),
    ('days_after_invoice', 'edge', 'Invoice dated 3 March 2026. Payment is due 30 days after the invoice date.', 'payment due date',
     {'2026-04-02', 'review'}),
]
COMPARE = [('14 March 2027', '2 April 2026'), ('2026-04-02', 'March 3rd, 2026'), ('1 Feb 2026', '31 January 2026'),
           ('30 Dec 2025', '2 Jan 2026'), ('2026-11-03', '3 Nov 2026'), ('29 Feb 2028', '1 Mar 2028')]
TRUTH = [False, False, False, True, False, True]


def j11():
    t = Test('J11', 'Read a date from text and let code do the calendar maths', 'Date extraction')
    for cid, kind, doc, role, ok in J11_CASES:
        a = t.ask({'document': doc}, date_questions(role))
        d, conf, why = resolve(a)
        if d is None and why == 'none':
            out = 'none'
        elif d is None or conf < REVIEW_BELOW:
            out = 'review'
        else:
            out = d.isoformat()
        t.case(cid, kind, sorted(ok), {'outcome': out, 'proposed': d.isoformat() if d else None,
               'confidence': round(conf, 2), 'mode': why}, out in ok)
    qs = {f'cmp{i}': noul('Is the date in `a` earlier than the date in `b`?') for i in range(len(COMPARE))}
    right = []
    for i, (x, y) in enumerate(COMPARE):
        v = t.ask({'a': x, 'b': y}, {'cmp': qs[f'cmp{i}']})['cmp']['noul']
        right.append((v > 0.5) == TRUTH[i])
    t.case('direct_date_comparison', 'edge', f'{len(COMPARE)}/{len(COMPARE)} comparisons right',
           f'{sum(right)}/{len(COMPARE)} right', all(right),
           'Asking the model to compare dates directly, which the docs advise against.')
    t.notes.append(f'Seven Choice questions per document; code assembles the date, infers missing years and resolves weekdays; review below confidence {REVIEW_BELOW}. Today pinned to {TODAY}.')
    return t

# ---------------------------------------------------------------- J12 pre-parsed value extraction
EMAIL = """From: Lena Fischer <lena.fischer@corvid-analytics.example>
Hi team, please send the signed contract to legal@corvid-analytics.example, not to me. For billing questions call our accounts payable line on +44 20 7946 0321; my direct line is +44 20 7946 0999.
Our PO number is PO-88213 (the quote reference was Q-55102, and invoice INV-20931 is already paid). The quote total was $12,400.00; after the $1,400.00 discount the amount we will pay is $11,000.00. The $500.00 setup fee was waived.

> Earlier message, 2 May: please send contracts to lena.fischer@corvid-analytics.example."""
EMAIL2 = 'Please put our PO # 88213 on the invoice. Quote Q-55102; the prior invoice INV-20931 is paid.'
PATTERNS = {'email': r'[\w.+-]+@[\w-]+(?:\.[\w-]+)+', 'phone': r'\+\d[\d ]{8,}\d', 'money': r'\$[\d,]+\.\d\d',
            'id': r'\b[A-Z]{1,4}-\d{4,6}\b'}
J12_CASES = [  # (id, kind, document, candidate kind, question, expected span or 'none')
    ('contract_email', 'core', EMAIL, 'email', 'Which email address should the signed contract be sent to now?', 'legal@corvid-analytics.example'),
    ('ap_phone', 'core', EMAIL, 'phone', 'Which phone number is for billing questions?', '+44 20 7946 0321'),
    ('direct_line', 'core', EMAIL, 'phone', "Which phone number is the sender's own direct line?", '+44 20 7946 0999'),
    ('po_number', 'core', EMAIL, 'id', "Which identifier is the customer's purchase order number?", 'PO-88213'),
    ('amount_to_pay', 'core', EMAIL, 'money', 'Which amount will the customer actually pay?', '$11,000.00'),
    ('waived_fee', 'edge', EMAIL, 'money', 'Which amount is a charge the customer will not have to pay?', '$500.00'),
    ('fax_absent', 'edge', EMAIL, 'phone', 'Which phone number is a fax number?', 'none'),
    ('regex_missed_po', 'edge', EMAIL2, 'id', "Which identifier is the customer's purchase order number?", 'none'),
]


def j12():
    t = Test('J12', 'Pick the right value from candidates that code found', 'Pre-parsed value extraction')
    for cid, kind, doc, kindc, q, want in J12_CASES:
        cands = list(dict.fromkeys(re.findall(PATTERNS[kindc], doc)))
        opts = {f'c{i}': c for i, c in enumerate(cands)}
        opts['none'] = 'None of these is the requested value.'
        a = t.ask({'document': doc}, {'pick': choice(q.replace('?', ' in `document`?'), opts)})['pick']
        got = opts[top(a)] if top(a) != 'none' else 'none'
        t.case(cid, kind, want, {'picked': got, 'confidence': round(a['confidence'], 2), 'candidates': cands}, got == want)
    t.notes.append('Regular expressions find every candidate; one Choice picks among them plus "none"; code copies the exact text.')
    return t

# ---------------------------------------------------------------- J13 structure recovery
LINES = [
    ('Restoring the orders database', 'heading'),
    ('This runbook explains how to restore the orders database from', 'paragraph'),
    ('the nightly snapshot when a bad migration has corrupted data.', '+'),
    ('Before you start', 'heading'),
    ('Warning: restoring overwrites every change made since the snapshot.', 'callout'),
    ('SELECT the snapshot with the latest timestamp before the incident,', 'paragraph|list_item'),
    ('not the most recent one, because that one already contains the bad data.', '+'),
    ('Stop the application workers.', 'list_item'),
    ('Take a final backup of the current state.', 'list_item'),
    ('Run the restore:', 'list_item'),
    ('pg_restore --clean --dbname=orders /backups/orders-2026-10-27.dump', 'code'),
    ('Check that the row counts match the snapshot report:', 'list_item'),
    ("SELECT count(*) FROM orders WHERE created_at < '2026-10-27';", 'code'),
    ('Restart the workers and watch the error rate for 15 minutes.', 'list_item'),
    ('Note: if the restore fails halfway, do not retry immediately;', 'callout'),
    ('page the database on-call engineer first.', '+'),
    ('Rollback', 'heading'),
    ("If the restored data is also wrong, restore the previous night's", 'paragraph'),
    ('snapshot instead and repeat the checks above.', '+'),
]
EDGE_BLOCKS = {5, 9, 11, 12, 14}  # prose that starts with SELECT, steps ending in a colon, one-line SQL, a "Note:" callout


def j13():
    t = Test('J13', 'Rebuild headings, lists and code from flattened text', 'Structure recovery')
    text = '\n'.join(f'L{i:03d}| {s}' for i, (s, _) in enumerate(LINES))
    qs = {f'j{i}': noul(f'Does line L{i:03d} pick up mid-sentence, continuing a sentence left unfinished at the end of line L{i-1:03d}?')
          for i in range(1, len(LINES))}
    a = t.ask({'document': text}, qs)
    wrong = []
    for i in range(1, len(LINES)):
        prev, cur = LINES[i - 1][0].rstrip(), LINES[i][0]
        # Code heuristic: a long line ending mid-sentence followed by a lowercase start gets the low bar.
        dangling = len(prev) > 40 and (prev[-1] in ',;' or prev[-1].islower()) and cur[0].islower()
        bar = 0.2 if dangling else 0.5
        if (a[f'j{i}']['noul'] > bar) != (LINES[i][1] == '+'):
            wrong.append(f'L{i:03d} ({a[f"j{i}"]["noul"]:.2f})')
    n = len(LINES) - 1
    t.case('line_joins', 'core', f'{n} of {n} join decisions right', {'right': f'{n - len(wrong)} of {n}', 'wrong': wrong}, not wrong)
    blocks = []  # build blocks from the true joins so block typing is judged on its own
    for i, (s, typ) in enumerate(LINES):
        if typ == '+':
            blocks[-1][1] += ' ' + s
        else:
            blocks.append([i, s, typ])
    btext = '\n'.join(f'B{n:03d}| {s}' for n, (_, s, _) in enumerate(blocks))
    types = {'heading': 'A section title.', 'paragraph': 'Ordinary running prose.',
             'list_item': 'One step or item in a list.', 'quote': 'Quoted words from someone else.',
             'code': 'Computer code, a shell command, terminal output, or a config snippet meant to be read verbatim.',
             'callout': 'A warning, note or tip set apart from the main text.'}
    b = t.ask({'document': btext}, {f'b{n}': choice(f'What kind of block is B{n:03d}?', types) for n in range(len(blocks))})
    for n, (first, s, typ) in enumerate(blocks):
        got = top(b[f'b{n}'])
        t.case(f'B{n:03d} {s[:28]}', 'edge' if first in EDGE_BLOCKS else 'core', typ,
               {'type': got, 'confidence': round(b[f'b{n}']['confidence'], 2)}, got in typ.split('|'))
    t.notes.append('Pass 1: one Noul per adjacent line pair (join bar 0.2 after an unfinished line, 0.5 after end punctuation). Pass 2: one Choice per block. Two requests in total.')
    return t


TESTS = [j10, j11, j12, j13]
