"""Jobs 18-20: techniques that get more out of any question. Expected outcomes are fixed here before any call."""
import random
import numpy as np
from common import Test, top
from jev import noul, choice, score, PRICE

# ---------------------------------------------------------------- J18 repeat and agree (self-consistency)
QUEUES = {'Billing': 'Charges, invoices, refunds and plan prices.',
          'Outage': 'The service is down or unusable right now.',
          'Performance': 'The service works but is slow.',
          'Security': 'Suspicious access, credentials or data exposure.',
          'FeatureRequest': 'A request for something the product does not do yet.'}
J18_CASES = [  # (id, kind, ticket, correct queue or None for genuinely mixed)
    ('down', 'core', 'Production cluster down, all queries failing since 09:14 UTC.', 'Outage'),
    ('double_charge', 'core', 'We were charged twice for October; please refund one of the payments.', 'Billing'),
    ('pdf_export', 'core', 'Could you add an option to export dashboards to PDF?', 'FeatureRequest'),
    ('foreign_login', 'core', "Someone logged into our admin account from another country and it wasn't us.", 'Security'),
    ('slow_after_rotation', 'edge', 'Queries got slow right after we rotated credentials, and we see auth failures from an unknown IP.', None),
    ('bill_from_slowness', 'edge', 'Our invoice went up because the slow reports forced us onto a bigger plan.', None),
    ('up_but_unusable', 'edge', 'The cluster is up but every query takes 30 seconds; customers think we are down.', None),
    ('geo_block_request', 'edge', 'Please add a setting to block logins from outside the EU.', None),
]
RUNS, ABSTAIN_BELOW = 8, 0.60


def j18():
    t = Test('J18', 'Ask more than once, act only when answers agree', 'Self-consistency: choices and nouls')
    keys = list(QUEUES)
    abst = total = 0
    for cid, kind, ticket, want in J18_CASES:
        labels, tops = [], []
        for r in range(RUNS):
            order = keys if r % 2 == 0 else keys[::-1]  # half the runs reverse the option order
            a = t.ask({'uid': f'run-{r:02d}', 'ticket': ticket},
                      {'queue': choice('Which queue should handle `ticket`?', {k: QUEUES[k] for k in order})})['queue']
            p = a['probabilities'][top(a)]
            labels.append(top(a) if p >= ABSTAIN_BELOW else 'abstain')
            tops.append(round(p, 2))
        abst += labels.count('abstain')
        total += RUNS
        concrete = {x for x in labels if x != 'abstain'}
        ok = labels == [want] * RUNS if want else len(concrete) <= 1
        tally = lambda xs: dict(sorted({x: xs.count(x) for x in xs}.items()))
        t.case(cid, kind, want or 'no two different automatic labels',
               {'original_order': tally(labels[0::2]), 'reversed_order': tally(labels[1::2]),
                'top_p_range': [min(tops), max(tops)]}, ok)
    t.notes.append(f'{RUNS} runs per ticket with a throwaway uid; odd runs reverse the option order. Code abstains below top probability {ABSTAIN_BELOW}. Abstained: {abst}/{total} answers.')
    return t

# ---------------------------------------------------------------- J19 parallel questions
MSA = """Master Services Agreement between Corvid Cloud Ltd ("Provider") and the Customer.
1. Services. Provider will host and operate managed PostgreSQL databases for the Customer as described in each Order Form. Each Order Form states the number of database clusters, their sizes and the region in which they are hosted.
2. Term. This Agreement starts on the Effective Date and continues for an initial term of 24 months. It then renews automatically for successive 12-month terms unless either party gives at least 90 days written notice before the end of the current term.
3. Fees. The Customer pays the fees in each Order Form annually in advance. Invoices are due within 30 days. Late amounts accrue interest at 1% per month. Provider may increase fees at renewal by no more than 5%.
4. Customer Data. The Customer owns all Customer Data. Provider processes Customer Data only to provide the Services and never uses it to train machine-learning models. Customer Data is hosted in the region chosen in the Order Form and is not moved outside that region without the Customer's written consent.
5. Security. Provider maintains ISO 27001 certification, encrypts Customer Data at rest and in transit, and notifies the Customer of any personal data breach within 48 hours of becoming aware of it.
6. Sub-processors. Provider may use sub-processors listed on its website and will give 30 days notice before adding a new one. The Customer may object on reasonable data protection grounds.
7. Service levels. Availability commitments and service credits are set out in the Service Level Agreement, which forms part of this Agreement. Service credits are the Customer's sole remedy for missed availability targets.
8. Liability. Each party's total liability under this Agreement is capped at the fees paid in the 12 months before the claim. The cap does not apply to breaches of confidentiality, data protection obligations or the Customer's payment obligations.
9. Termination. Either party may terminate for material breach not remedied within 30 days of written notice. On termination Provider will make Customer Data available for export for 30 days and then delete it within a further 30 days.
10. Governing law. This Agreement is governed by the laws of England and Wales, and the courts of London have exclusive jurisdiction."""
J19_QS = {
    'auto_renews': noul('Does `contract` renew automatically?'),
    'notice_90': noul('Does `contract` require at least 90 days notice to stop renewal?'),
    'trains_models': noul('Does `contract` allow the provider to use customer data to train machine-learning models?'),
    'breach_48h': noul('Does `contract` require the provider to report a personal data breach within 48 hours?'),
    'cap_excludes_dp': noul('Does the liability cap in `contract` exclude data protection breaches?'),
    'cap_12m': noul('Is liability in `contract` capped at 12 months of fees?'),
    'law': choice('Which law governs `contract`?', {'england_wales': 'England and Wales.', 'delaware': 'Delaware.',
                                                    'ireland': 'Ireland.', 'not_stated': 'Not stated.'}),
    'payment': choice('When are fees paid under `contract`?', {'monthly_arrears': 'Monthly, after use.',
                                                               'annual_advance': 'Yearly, in advance.', 'on_signature': 'Once, at signature.'}),
    'customer_friendliness': score('How favourable is `contract` to the customer on data protection?',
                                   ['Unfavourable.', 'Mixed.', 'Standard.', 'Favourable.', 'Very favourable.']),
    'lock_in': score('How hard does `contract` make it for the customer to leave?',
                     ['Easy to leave.', 'Some friction.', 'Hard to leave.']),
}
SHORT_DOC = 'Order: 2 clusters, EU region, 24-month term, renews yearly.'
J19_TRUTH = {'auto_renews': True, 'notice_90': True, 'trains_models': False, 'breach_48h': True,
             'cap_excludes_dp': True, 'cap_12m': True, 'law': 'england_wales', 'payment': 'annual_advance'}


def value(a):
    return a['noul'] if a['type'] == 'noul' else a['choice'] if a['type'] == 'choice' else round(a['score'], 1)


def j19():
    t = Test('J19', 'Ask many questions in one request', 'Parallel questions')
    res = {}
    for name, doc in (('long', MSA), ('short', SHORT_DOC)):
        t0 = t.tokens
        b = t.ask({'contract': doc}, J19_QS)
        batch_tokens = t.tokens - t0
        singles, secs = {}, []
        for k, q in J19_QS.items():
            before_s, before_t = t.seconds, t.tokens
            singles[k] = t.ask({'contract': doc}, {k: q})[k]
            secs.append(t.seconds - before_s)
        single_tokens = t.tokens - t0 - batch_tokens
        diffs = [k for k in J19_QS if (abs(b[k]['noul'] - singles[k]['noul']) > 0.05 if b[k]['type'] == 'noul'
                                       else abs(b[k]['score'] - singles[k]['score']) > 0.25 if b[k]['type'] == 'score'
                                       else value(b[k]) != value(singles[k]))]
        if name == 'long':
            wrong = [k for k, v in J19_TRUTH.items() if ((b[k]['noul'] > 0.5) if b[k]['type'] == 'noul' else b[k]['choice']) != v]
            t.case('correct_answers_long_doc', 'core', f'{len(J19_TRUTH)} factual answers right', {'wrong': wrong}, not wrong)
        res[name] = {'batch_tokens': batch_tokens, 'single_tokens': single_tokens,
                     'token_ratio': round(single_tokens / batch_tokens, 1), 'answers_that_differ': diffs,
                     'singles_sequential_s': round(sum(secs), 2), 'singles_slowest_s': round(max(secs), 2)}
    lg, sh = res['long'], res['short']
    t.case('same_answers_long_doc', 'core', 'no answer changes', lg['answers_that_differ'], not lg['answers_that_differ'])
    t.case('cheaper_long_doc', 'measure', 'at least 5x fewer tokens batched', {k: lg[k] for k in ('batch_tokens', 'single_tokens', 'token_ratio')},
           lg['token_ratio'] >= 5)
    t.case('same_answers_short_doc', 'edge', 'no answer changes', sh['answers_that_differ'], not sh['answers_that_differ'])
    t.case('saving_shrinks_short_doc', 'measure', 'smaller saving than the long document',
           {k: sh[k] for k in ('batch_tokens', 'single_tokens', 'token_ratio')}, sh['token_ratio'] < lg['token_ratio'])
    t.notes.append(f"Long contract: one request of {len(J19_QS)} questions used {lg['batch_tokens']} tokens vs {lg['single_tokens']} for separate requests (${lg['batch_tokens']*PRICE:.6f} vs ${lg['single_tokens']*PRICE:.6f}). Separate requests took {lg['singles_sequential_s']} s one after another.")
    t.notes.append(f"Two questions overlap on purpose (cap_12m and cap_excludes_dp) to check that answers do not leak between questions.")
    return t

# ---------------------------------------------------------------- J20 feature discovery
FACTORS = {  # hidden factor -> phrasings (positive, and negated forms that keyword counts will confuse)
    'competitor': (["They mentioned they are trialling a rival vendor.", "Their team is evaluating two competitors this quarter.",
                    "Procurement asked us to match a competitor's quote."],
                   ["They said they are not looking at other vendors.", "No interest in competitors, they told us."]),
    'champion_left': (["Our main sponsor there left the company last month.", "The VP who bought us has moved on.",
                       "Our internal champion resigned."],
                      ["Our sponsor was just promoted and is staying.", "The VP who bought us is still very engaged."]),
    'budget_cut': (["They announced a 20% budget cut for tooling.", "Finance froze all software renewals.",
                    "They are under pressure to reduce spend."],
                   ["Budget is not a concern for them this year.", "They just got a bigger tooling budget."]),
    'usage_up': (["Weekly active users doubled since spring.", "They are rolling us out to two more teams.",
                  "Usage is growing every month."],
                 ["Usage has been flat since onboarding.", "Only one analyst still logs in."]),
    'data_quality': (["They complained that enriched phone numbers are often wrong.", "Several bounced emails came from our data.",
                      "They found duplicate companies in our feed."],
                     ["They praised the accuracy of our data.", "No data issues were raised."]),
}
FILLER = ['Call was friendly.', 'They asked about the roadmap.', 'Next check-in in six weeks.', 'Meeting ran short.',
          'They want an invoice copy.', 'They use Snowflake.', 'Discussed SSO setup.', 'Renewal is in Q3.']
WEIGHTS = {'competitor': 1.6, 'champion_left': 1.4, 'budget_cut': 1.0, 'usage_up': -1.6, 'data_quality': 1.6}
ROUND1 = {  # first proposal: the obvious questions, without data quality
    'competitor': noul('Does `note` say the customer is evaluating or considering a competing vendor?'),
    'champion_left': noul('Does `note` say the customer\'s main sponsor or champion has left or moved on?'),
    'budget_cut': noul('Does `note` say the customer is cutting or freezing spend?'),
    'usage_up': noul('Does `note` say the customer\'s usage of our product is growing?'),
    'tone': score('How positive is the overall tone of `note`?', ['Negative.', 'Neutral.', 'Positive.']),
}
ROUND2 = {'data_quality': noul('Does `note` report problems with the accuracy or quality of the data we supply?')}
DIRECT = score('How likely is the customer in `note` to cancel at renewal?',
               ['Very unlikely.', 'Unlikely.', 'Even chance.', 'Likely.', 'Very likely.'])


def make_notes(n=400, seed=7):
    """Returns (note, label, true factor vector). The factors are kept only to report a perfect-feature ceiling."""
    rng = random.Random(seed)
    rows = []
    for _ in range(n):
        f = {k: rng.random() < 0.35 for k in FACTORS}
        parts = []
        for k, on in f.items():
            pos, neg = FACTORS[k]
            if on:
                parts.append(rng.choice(pos))
            elif rng.random() < 0.4:
                parts.append(rng.choice(neg))
        parts += rng.sample(FILLER, 2)
        rng.shuffle(parts)
        logit = -1.0 + sum(WEIGHTS[k] * f[k] for k in f)
        rows.append((' '.join(parts), int(rng.random() < 1 / (1 + np.exp(-logit))), [float(f[k]) for k in FACTORS]))
    return rows


def logreg(X, y, steps=3000, lr=0.1, l2=0.01):
    X = np.hstack([X, np.ones((len(X), 1))])
    w = np.zeros(X.shape[1])
    for _ in range(steps):
        p = 1 / (1 + np.exp(-X @ w))
        w -= lr * (X.T @ (p - y) / len(y) + l2 * w)
    return lambda Z: 1 / (1 + np.exp(-np.hstack([Z, np.ones((len(Z), 1))]) @ w))


def auc(y, s):
    pos, neg = s[y == 1], s[y == 0]
    return float(np.mean([(p > q) + 0.5 * (p == q) for p in pos for q in neg]))


def cv_auc(X, y, folds=5, repeats=10, seed=1):
    """Mean AUC over repeated stratified-free k-fold cross-validation (fixed seeds, so it replays)."""
    rng = np.random.default_rng(seed)
    scores = []
    for _ in range(repeats):
        idx = rng.permutation(len(y))
        for k in range(folds):
            te = idx[k::folds]
            tr = np.setdiff1d(idx, te)
            scores.append(auc(y[te], logreg(X[tr], y[tr])(X[te])))
    return round(float(np.mean(scores)), 3), round(float(np.std(scores) / np.sqrt(len(scores))), 3)


def j20():
    t = Test('J20', 'Turn free text into numbers a prediction model can use', 'Autoresearch feature discovery')
    rows = make_notes()
    y = np.array([r[1] for r in rows])
    oracle = np.array([r[2] for r in rows])
    f1, f2, direct = [], [], []
    for note, _, _ in rows:
        a = t.ask({'note': note}, {**ROUND1, 'direct': DIRECT})
        f1.append([a[k]['noul'] if a[k]['type'] == 'noul' else a[k]['score'] for k in ROUND1])
        direct.append(a['direct']['score'])
        f2.append(t.ask({'note': note}, ROUND2)['data_quality']['noul'])
    f1, f2, direct = np.array(f1), np.array(f2)[:, None], np.array(direct)
    words = lambda s: s.lower().replace('.', ' ').replace(',', ' ').replace("'", ' ').split()
    vocab = sorted({w for note, _, _ in rows for w in words(note)})
    bow = np.array([[words(note).count(w) for w in vocab] for note, _, _ in rows], float)
    res = {name: cv_auc(X, y) for name, X in (('keywords', bow), ('round1', f1), ('round2', np.hstack([f1, f2])),
                                               ('perfect_round1_factors', oracle[:, :4]), ('perfect_all_factors', oracle))}
    res['direct_score'] = (round(auc(y, direct), 3), None)
    t.case('features_beat_keywords', 'core', 'question features score higher than word counts', res, res['round2'][0] > res['keywords'][0])
    t.case('second_round_helps', 'core', 'adding the data-quality question raises accuracy',
           {k: res[k] for k in ('round1', 'round2', 'perfect_round1_factors', 'perfect_all_factors')}, res['round2'][0] > res['round1'][0])
    t.case('features_vs_direct', 'edge', 'combining narrow questions beats asking for the prediction directly',
           {k: res[k] for k in ('round2', 'direct_score')}, res['round2'][0] > res['direct_score'][0])
    t.notes.append(f'{len(rows)} synthetic account notes ({int(y.sum())} churned); labels drawn at random from planted factors, including a data-quality factor that round 1 does not ask about. AUC = mean (standard error) over 10 x 5-fold cross-validation with logistic regression; "perfect" rows use the true planted factors and mark the ceiling.')
    return t


TESTS = [j18, j19, j20]
