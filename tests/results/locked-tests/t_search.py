"""Jobs 14-17: finding the passage, line or record that matches. Expected answers are fixed here before any call."""
import math
import re
from collections import Counter
from common import Test, top
from jev import noul, choice, score

# ---------------------------------------------------------------- J14 re-ranking
KB = {
    'a01': 'Resolving deadlocks from concurrent batch updates. When two workers update overlapping rows, sort the rows by primary key in every worker so locks are always taken in the same order, and retry on SQLSTATE 40P01.',
    'a02': 'Deadlock detection settings. deadlock_timeout controls how long Postgres waits on a lock before checking for a deadlock. Raising it delays detection but does not prevent deadlocks.',
    'a03': 'Bulk updates are slow. Update in batches of about 5,000 rows, drop triggers you do not need during the batch, and run ANALYZE afterwards.',
    'a04': "pg_upgrade from 12 to 14 fails with 'cannot drop extension'. Drop the old postgis_topology extension in the 12 cluster before running pg_upgrade.",
    'a05': "pg_upgrade from 15 to 16 fails with 'cannot drop extension'. Update pg_stat_statements to version 1.10 in the old 15 cluster, then rerun pg_upgrade.",
    'a06': 'Upgrading between major versions with logical replication instead of pg_upgrade, for near-zero downtime.',
    'a07': 'Connection refused after changing listen_addresses. listen_addresses only takes effect when the server restarts; a configuration reload is not enough.',
    'a08': 'Too many connections. Raise max_connections or put PgBouncer in transaction pooling mode in front of the database.',
    'a09': "Password authentication failed after upgrading to Postgres 14. The default password_encryption changed to scram-sha-256; reset the user's password so a SCRAM hash is stored.",
    'a10': 'Connection refused from clients. Check that the firewall allows port 5432 from the client network and that the server is running.',
    'a11': 'Replication lag on replicas. Long-running queries on a replica can block WAL replay; tune max_standby_streaming_delay.',
    'a12': 'VACUUM is not removing dead rows. An old open transaction holds back the xmin horizon; find it in pg_stat_activity.',
    'a13': 'Disk full on the primary. Old WAL files pile up when a replication slot is inactive; drop or advance the abandoned slot.',
    'a14': 'Table bloat after mass deletes. Plain VACUUM marks space reusable but does not return it to the operating system; use pg_repack to shrink the table online.',
    'a15': 'Slow queries after a large data load. The planner uses stale statistics until ANALYZE runs; run ANALYZE on the loaded tables.',
    'a16': 'Out of shared memory errors. Raise max_locks_per_transaction when one transaction touches thousands of partitions.',
    'a17': 'Sequence values jump after a crash or failover. Sequences pre-allocate values and gaps are expected; do not rely on gap-free IDs.',
    'a18': 'Timestamps shift by an hour. Use timestamptz columns and set the session time zone; plain timestamp stores no zone.',
    'a19': 'Encoding errors when importing CSV files. Set the client_encoding to match the file, for example LATIN1, before running COPY.',
    'a20': 'Query cancelled on a replica due to conflict with recovery. Enable hot_standby_feedback or raise max_standby_streaming_delay.',
    'a21': 'Lock waits during schema changes. ALTER TABLE takes an exclusive lock; set lock_timeout so a migration fails fast instead of queueing behind long queries.',
    'a22': 'Adding an index without downtime. CREATE INDEX CONCURRENTLY builds the index without blocking writes.',
    'a23': 'Foreign key violations during data loads. Load parent tables before child tables, or defer constraint checking until commit.',
    'a24': 'SSL connection errors. Clients must trust the server certificate authority; set sslmode=verify-full with the right root certificate.',
    'a25': 'Idle connections exhausting the pool. Set idle_in_transaction_session_timeout so abandoned sessions are closed.',
    'a26': 'Duplicate key errors after restoring a dump. Reset each sequence to the maximum id with setval so new rows do not collide.',
    'a27': 'Statement timeout errors in reports. Raise statement_timeout for the reporting role only, not globally.',
    'a28': 'Extension not available after upgrade. Install the extension package for the new major version on the server before CREATE EXTENSION.',
    'a29': 'Logical replication stuck. A subscription stops when a row conflicts with an existing key; fix the row or skip the transaction.',
    'a30': 'Checkpoint warnings in the log. Increase max_wal_size so checkpoints are not forced too often under heavy writes.',
}
J14_CASES = [  # tickets in user words, sharing few terms with the right article
    ('deadlock', 'core', 'Our two nightly jobs keep killing each other when they edit the same order records at once.', 'a01'),
    ('scram_login', 'core', "Since the big version upgrade our app can't sign in any more, even though nobody changed its password.", 'a09'),
    ('ids_collide', 'core', 'After we restored last night\'s backup, every new signup fails because the id it gets is already taken.', 'a26'),
    ('disk_filling', 'core', 'The main server is nearly out of space and the growth is all log files, but nothing has changed in our data.', 'a13'),
    ('near_duplicate_version', 'edge', "pg_upgrade from 15 to 16 stops with 'cannot drop extension'.", 'a05'),
    ('keyword_trap', 'edge', 'We changed listen_addresses and reloaded the config, but clients still get connection refused.', 'a07'),
]
SHORTLIST = 10


def bm25(query, docs, k1=1.5, b=0.75):
    tok = lambda s: re.findall(r'[a-z0-9_]+', s.lower())
    toks = {k: tok(v) for k, v in docs.items()}
    avg = sum(map(len, toks.values())) / len(toks)
    df = Counter(w for ts in toks.values() for w in set(ts))
    n = len(docs)
    def s(ts):
        tf = Counter(ts)
        return sum(math.log(1 + (n - df[w] + .5) / (df[w] + .5)) * tf[w] * (k1 + 1) /
                   (tf[w] + k1 * (1 - b + b * len(ts) / avg)) for w in set(tok(query)) if w in tf)
    return sorted(docs, key=lambda k: -s(toks[k]))


def j14():
    t = Test('J14', 'Move the most useful search result to the top', 'Re-ranking')
    q = noul('Does `candidate` give the fix for the specific error and situation described in `ticket`?',
             'It states the resolution for this exact error under the stated conditions.',
             'It is merely about the same feature, error family or a different version.')
    moves = []
    for cid, kind, ticket, gold in J14_CASES:
        full = bm25(ticket, KB)
        short = full[:SHORTLIST]
        kw = full.index(gold) + 1
        if gold not in short:  # re-ranking cannot recover what the first search missed
            t.case(cid, kind, gold, {'keyword_rank_of_answer': kw, 'note': 'answer not in shortlist'}, False)
            moves.append('missed')
            continue
        p = {k: t.ask({'ticket': ticket, 'candidate': KB[k]}, {'q': q})['q']['noul'] for k in short}
        rr = sorted(short, key=lambda k: -p[k])
        jr = rr.index(gold) + 1
        moves.append('better' if jr < kw else 'same' if jr == kw else 'worse')
        t.case(cid, kind, gold, {'keyword_rank_of_answer': kw, 'jev_rank_of_answer': jr,
               'top_scores': {k: round(p[k], 2) for k in rr[:3]}}, jr == 1)
    t.notes.append(f'Keyword (BM25) shortlist of {SHORTLIST} from {len(KB)} articles; one Noul per ticket-article pair; sort by probability. Pass = right article ranked first.')
    t.notes.append(f"Versus keyword rank: {moves.count('better')} better, {moves.count('same')} same, {moves.count('worse')} worse, {moves.count('missed')} not shortlisted.")
    return t

# ---------------------------------------------------------------- J15 line-by-line search
SLA = """Service Level Agreement - Corvid Cloud Database
1. Definitions
"Customer Data" means data the Customer stores in the Service.
"Incident" means an unplanned interruption or reduction in quality of the Service.
2. Availability
We will make the Service available 99.9% of the time in each calendar month.
Scheduled maintenance announced 72 hours in advance does not count as downtime.
If availability falls below 99.9%, the Customer may claim a service credit.
Service credits are 10% of the monthly fee for each full 0.1% below the target.
Credits must be requested within 30 days of the end of the affected month.
3. Support
Support is available by email and through the support portal.
Severity 1 incidents receive a first response within 30 minutes, 24 hours a day.
Severity 2 incidents receive a first response within 4 business hours.
Severity 3 requests receive a first response within 2 business days.
4. Backups
Backups are taken every 24 hours.
Backups are retained for 35 days.
Backups are stored in a different region from the primary database.
5. Recovery
Our recovery point objective is 24 hours of data.
Our recovery time objective is 4 hours from the start of a declared disaster.
6. Data use
We never use Customer Data to train machine-learning models.
We process Customer Data only to provide the Service.
7. Termination
Either party may end this agreement with 90 days written notice.
After termination, Customer Data is deleted within 60 days."""
SLA_LINES = SLA.split('\n')
L = lambda text: next(f'L{i:03d}' for i, s in enumerate(SLA_LINES) if text in s)
FOUND, ABSENT = 0.7, 0.35
J15_CASES = [  # (id, kind, query, acceptable line ids or None when the document does not answer)
    ('retention', 'core', 'How long are backups kept?', {L('retained for 35 days')}),
    ('uptime', 'core', 'What uptime do you commit to?', {L('99.9% of the time')}),
    ('sev1_response', 'core', 'How quickly do you respond to a severity 1 incident?', {L('Severity 1')}),
    ('model_training', 'core', 'Is our data ever used to train AI models?', {L('never use Customer Data')}),
    ('replicas_absent', 'edge', 'Can we add read replicas to spread query load?', None),
    ('price_absent', 'edge', 'What is the price per GB of storage?', None),
    ('split_answer', 'edge', 'What are the RPO and RTO?', {L('recovery point'), L('recovery time')}),
]


def j15():
    t = Test('J15', 'Find the exact line in a long document that answers a question', 'Line-by-line search')
    doc = '\n'.join(f'L{i:03d}| {s}' for i, s in enumerate(SLA_LINES))
    for cid, kind, query, want in J15_CASES:
        a = t.ask({'document': doc}, {
            'where': choice(f'Which line in `document` contains the answer to this question: "{query}"?',
                            {f'L{i:03d}': None for i in range(len(SLA_LINES))}),
            'exists': noul(f'Does any line in `document` address or answer this question: "{query}"?',
                           'At least one line states or directly implies the answer.',
                           'No line addresses the question.')})
        ex, line = a['exists']['noul'], top(a['where'])
        verdict = 'found' if ex >= FOUND else 'absent' if ex <= ABSENT else 'partial'
        if want is None:
            ok = verdict == 'absent'
        else:
            ok = verdict != 'absent' and line in want and (verdict == 'found' or kind == 'edge')
        t.case(cid, kind, 'absent' if want is None else sorted(want),
               {'verdict': verdict, 'exists': round(ex, 2), 'top_line': line, 'line_p': round(a['where']['probabilities'][line], 2),
                'text': SLA_LINES[int(line[1:])]}, ok)
    t.notes.append(f'Whole {len(SLA_LINES)}-line document in one request per query: a Choice over line ids plus an "is it answered" Noul (found >= {FOUND}, absent <= {ABSENT}).')
    return t

# ---------------------------------------------------------------- J16 entity alignment
LEVELS = ['Two different companies.',
          'Closely related but not clearly the same legal entity: a parent, subsidiary, regional office, or an ambiguous match.',
          'One and the same company.']
J16_CASES = [  # (id, kind, a, b, acceptable routes)
    ('typo_same', 'core', 'Acme Data Systems Inc., acmedata.example, Austin, TX', 'ACME Data Sys, acmedata.example, Austin', {'merge'}),
    ('name_clash', 'core', 'Bluefin Analytics Ltd, bluefin.example, Leeds', 'Bluefin Seafoods plc, bluefinseafoods.example, Grimsby', {'separate'}),
    ('former_name', 'core', 'Halvorsen Data Supply Ltd (formerly Halvorsen Records), halvorsen.example, Leeds', 'Halvorsen Records Ltd, halvorsen.example, Leeds', {'merge'}),
    ('misspelt', 'core', 'Corvid Analytics, corvid-analytics.example, Cambridge', 'Corvid Analytcs Ltd, corvid-analytics.example, Cambridge, UK', {'merge'}),
    ('shared_word', 'core', 'Northwind Ledger, northwindledger.example, Bristol', 'Northwind Logistics, northwind-logistics.example, Bristol', {'separate'}),
    ('suffix_only', 'core', 'Pellucid Health Inc, pellucidhealth.example, Boston', 'Pellucid Health, pellucidhealth.example, Boston, MA', {'merge'}),
    ('subsidiary', 'edge', 'Snowline Analytics GmbH, snowline.example.de, Munich', 'Snowline Analytics Inc., snowline.example.com, Denver', {'curator'}),
    ('id_conflict', 'edge', 'Kestrel Ops Ltd, kestrelops.example, Leeds, company number 08812345', 'Kestrel Ops Ltd, kestrelops.example, Leeds, company number 09933411', {'curator', 'separate'}),
    ('acronym', 'edge', 'International Shipping Data Corporation, isdc.example, Rotterdam', 'ISDC, isdc.example, Rotterdam, NL', {'merge'}),
    ('other_office', 'edge', 'Mercer & Lowe LLP, mercerlowe.example, London office', 'Mercer & Lowe LLP, mercerlowe.example, New York office', {'curator', 'merge'}),
]


def j16():
    t = Test('J16', 'Decide whether two records are the same thing', 'Knowledge graph entity alignment')
    qs = {'link': score('How are the companies in `record_a` and `record_b` related?', LEVELS),
          'name': noul('Do `record_a` and `record_b` give the same company name, allowing for abbreviations and spelling slips?'),
          'domain': noul('Do `record_a` and `record_b` give the same website domain?'),
          'place': noul('Do `record_a` and `record_b` give the same location?')}
    for cid, kind, a_, b_, ok in J16_CASES:
        a = t.ask({'record_a': a_, 'record_b': b_}, qs)
        s = a['link']['score']
        route = 'merge' if s >= 1.5 else 'curator' if s >= 0.5 else 'separate'
        t.case(cid, kind, sorted(ok), {'route': route, 'score': round(s, 2), 'confidence': round(a['link']['confidence'], 2),
               **{k: round(a[k]['noul'], 2) for k in ('name', 'domain', 'place')}}, route in ok)
    t.notes.append('One Score (3 levels) plus three field Nouls per pair; code rounds the score: >= 1.5 merge, >= 0.5 curator, else separate. Unlike the cookbook, we score against labels.')
    return t

# ---------------------------------------------------------------- J17 checklist ticking (intelliprompter)
CHECKS = {
    'database': 'The customer stated which database system they use today.',
    'volume': 'The customer gave an approximate size or volume of their data.',
    'decider': 'The customer named who makes the final buying decision.',
    'compliance': 'The customer said whether they have compliance requirements such as GDPR or HIPAA.',
    'budget': 'The customer gave a budget or price range.',
}
CHUNKS = [
    'Sales: Thanks for making time today. Tell me a bit about your setup?',
    "Customer: Sure. We're on SQL Server 2016, on-prem, roughly four terabytes across two instances.",
    "Customer: On budget, I'd rather come back to that later once we've seen a proposal.",
    "Customer: Compliance-wise it honestly isn't relevant for us; we don't store any personal data.",
    "Customer: I'll be recommending it, but the final sign-off sits with our CFO, Maria.",
    "Sales: Great. Anything on timing? Customer: We'd like to be finished by the end of Q2.",
    'Customer: OK, ballpark, we have around forty to fifty thousand a year set aside for this.',
]
EXPECT_TICK = {'database': 2, 'volume': 2, 'decider': 5, 'compliance': 4, 'budget': 7}
COVER_LEVELS = ['Not mentioned at all.', 'Touched on only indirectly.', 'Mentioned directly.',
                'Covered with some detail.', 'Covered well, with useful detail.']
COVERED_AT = 2.5  # on the cookbook's 1-5 scale


def j17():
    t = Test('J17', 'Tick off a checklist as a conversation happens', 'Intelliprompter')
    ticked = {}
    for n in range(1, len(CHUNKS) + 1):
        open_ = [k for k in CHECKS if k not in ticked]
        if not open_:
            break
        a = t.ask({'transcript': '\n'.join(CHUNKS[:n])},
                  {k: score(f'How completely has the conversation in `transcript` covered this point: "{CHECKS[k]}"', COVER_LEVELS) for k in open_})
        for k in open_:
            if a[k]['score'] + 1 >= COVERED_AT:
                ticked[k] = (n, round(a[k]['score'] + 1, 2))
    for k, want in EXPECT_TICK.items():
        got = ticked.get(k, (None, None))
        kind = 'edge' if k in ('budget', 'compliance') else 'core'
        t.case(k, kind, f'ticked at chunk {want}', {'ticked_at_chunk': got[0], 'score': got[1]}, got[0] == want)
    t.notes.append(f'One request per transcript chunk with one Score per unticked item; ticks are one-way; threshold {COVERED_AT} on 1-5. Budget is mentioned-but-deferred at chunk 3; compliance is answered with a "no" at chunk 4.')
    return t


TESTS = [j14, j15, j16, j17]
