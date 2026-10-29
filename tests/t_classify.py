"""Jobs 7-9: putting things in categories. Expected answers are fixed here before any call."""
import math
from common import Test, top
from jev import noul, choice

# ---------------------------------------------------------------- J07 hierarchical classification
TREE = {
    'Manufacturing': {
        'Computer and Electronic Products': {'Semiconductors': {}, 'Medical Devices and Instruments': {},
                                             'Networking Hardware': {}, 'All Other Electronics': {}},
        'Food and Beverage': {'Breweries': {}, 'Bakeries': {}, 'All Other Food': {}},
        'All Other Manufacturing': {}},
    'Information': {
        'Software Publishers': {'Database Software': {}, 'Security Software': {}, 'Business Applications': {}},
        'Data Processing and Hosting': {'Cloud Hosting': {}, 'Data Brokers and Enrichment': {}},
        'Telecommunications': {}},
    'Professional Services': {
        'Computer Services': {'Custom Software Development': {}, 'IT Consulting': {}, 'Managed IT Services': {}},
        'Legal and Accounting': {'Law Firms': {}, 'Accounting Firms': {}},
        'Marketing': {'Advertising Agencies': {}, 'Market Research': {}}},
    'Retail and Wholesale': {'Online Retail': {}, 'Wholesale Electronics': {}},
    'Health Care': {'Hospitals': {}, 'Medical Laboratories': {}, 'Clinics': {}},
}
J07_CASES = [
    ('custom_db_dev', 'core', 'The firm writes custom database software for logistics companies under contract.',
     'Professional Services/Computer Services/Custom Software Development'),
    ('db_vendor', 'core', 'Sells a licensed relational database engine to large enterprises.',
     'Information/Software Publishers/Database Software'),
    ('brewery', 'core', 'Brews craft lagers in Leeds and sells them to pubs.', 'Manufacturing/Food and Beverage/Breweries'),
    ('urgent_care', 'core', 'Runs a chain of urgent-care walk-in centres.', 'Health Care/Clinics'),
    ('data_broker', 'core', 'Buys and resells contact data about B2B companies to sales teams.',
     'Information/Data Processing and Hosting/Data Brokers and Enrichment'),
    ('infusion_pumps', 'edge', 'Designs and manufactures the firmware-controlled infusion pumps used in hospitals.',
     'Manufacturing/Computer and Electronic Products/Medical Devices and Instruments'),
    ('hospital_security', 'edge', 'Advises hospitals on cybersecurity and installs firewalls for them.',
     {'Professional Services/Computer Services/IT Consulting', 'Professional Services/Computer Services/Managed IT Services'}),
    ('refurb_switches', 'edge', 'Operates an online shop selling refurbished network switches.', 'Retail and Wholesale/Online Retail'),
]
Q_NODE = 'Which category best matches the business described in `document`?'


def node(path):
    n = TREE
    for part in path:
        n = n[part]
    return n


def beam(t, doc, k, reverse=False):
    """Beam search over the tree; path score is the geometric mean of the choices taken (cookbook)."""
    paths = [((), [])]
    while any(node(p) for p, _ in paths):
        nxt = []
        for p, probs in paths:
            kids = list(node(p))
            if not kids:
                nxt.append((p, probs))
                continue
            if len(kids) == 1:
                nxt.append((p + (kids[0],), probs))
                continue
            order = kids[::-1] if reverse else kids
            a = t.ask({'document': doc}, {'c': choice(Q_NODE, {f'c{i}': kid for i, kid in enumerate(order)})})['c']
            for i, kid in enumerate(order):
                nxt.append((p + (kid,), probs + [a['probabilities'][f'c{i}']]))
        gm = lambda pr: math.exp(sum(math.log(max(x, 1e-9)) for x in pr) / len(pr)) if pr else 1
        paths = sorted(nxt, key=lambda x: -gm(x[1]))[:k]
    best = paths[0]
    return '/'.join(best[0]), round(math.exp(sum(math.log(max(x, 1e-9)) for x in best[1]) / len(best[1])), 3)


def j07():
    t = Test('J07', 'File a record into a deep category tree', 'Hierarchical classification')
    flips = 0
    for cid, kind, doc, want in J07_CASES:
        b, bs = beam(t, doc, 3)
        g, _ = beam(t, doc, 1)
        r, _ = beam(t, doc, 3, reverse=True)
        flips += r != b
        wants = want if isinstance(want, set) else {want}
        t.case(cid, kind, sorted(wants), {'beam3': b, 'greedy': g, 'beam3_reversed_options': r, 'path_score': bs}, b in wants)
    t.notes.append(f'Beam width 3 vs greedy, one Choice request per tree node. Reversing sibling order changed the beam answer for {flips} of {len(J07_CASES)} records.')
    return t

# ---------------------------------------------------------------- J08 classification using confidence
SUBS = {  # subcategory: (parent, examples)
    'cloud_data_warehouse': ('Data Infrastructure', 'Cloud data warehouses, lakehouses, columnar analytics databases.'),
    'relational_dbms': ('Data Infrastructure', 'Relational database engines and licensed SQL servers.'),
    'etl_elt': ('Data Infrastructure', 'Pipelines that copy data from apps into a warehouse; ingestion connectors.'),
    'reverse_etl': ('Data Infrastructure', 'Tools that push warehouse data back into business apps such as CRMs.'),
    'crm': ('Sales and Marketing', 'Customer relationship management, pipeline and opportunity tracking.'),
    'marketing_automation': ('Sales and Marketing', 'Email campaigns, lead nurturing, landing pages.'),
    'sales_intelligence': ('Sales and Marketing', 'B2B contact and company databases, data enrichment for prospecting.'),
    'identity_access': ('Security', 'Single sign-on, multi-factor authentication, identity management.'),
    'endpoint_security': ('Security', 'Antivirus, endpoint detection and response.'),
    'data_loss_prevention': ('Security', 'Tools that stop sensitive data leaving the company.'),
    'accounting_software': ('Finance', 'General ledger, bookkeeping, financial close.'),
    'billing_subscriptions': ('Finance', 'Subscription billing, invoicing, revenue recognition.'),
    'expense_management': ('Finance', 'Employee expenses, corporate cards, receipts.'),
    'database_consulting': ('IT Services', 'Consultancies that design, migrate or tune databases for clients.'),
    'managed_hosting': ('IT Services', 'Running servers and databases for clients as a managed service.'),
    'systems_integration': ('IT Services', 'Connecting enterprise systems for clients as a project.'),
}
CONFIDENT = 0.9
J08_CASES = [  # (id, kind, description, true subcategory or None when the text cannot tell)
    ('warehouse', 'core', 'Point your BI tool at us and query petabytes in seconds. Storage and compute scale separately, and you pay only while queries run.', 'cloud_data_warehouse'),
    ('sso', 'core', 'Staff log in once to reach every work app, and a code is pushed to their phone at sign-in. Leavers lose access everywhere with one click.', 'identity_access'),
    ('subs_billing', 'core', 'Charge customers monthly or yearly, handle upgrades mid-cycle, send the paperwork automatically, and keep your auditors happy with ASC 606 schedules.', 'billing_subscriptions'),
    ('pipelines', 'core', 'Connect Salesforce, Stripe, Zendesk and 300 other apps once; fresh copies of their data land in Snowflake or BigQuery every hour, no code required.', 'etl_elt'),
    ('contact_data', 'core', "Find the right buyer at any company: 200 million verified business emails and mobile numbers, ready to drop into your reps' outreach lists.", 'sales_intelligence'),
    ('pipeline_crm', 'core', 'See every deal your reps are working, which stage it is at, and what the quarter will close at, all in one place.', 'crm'),
    ('vague', 'edge', 'We help companies get more from their data.', None),
    ('consultancy_trap', 'edge', 'We are a consultancy and do not sell software. We migrate customers from Oracle databases to PostgreSQL.', 'database_consulting'),
    ('reverse_etl', 'edge', 'Syncs warehouse tables back into Salesforce and HubSpot so sales reps see product usage.', 'reverse_etl'),
    ('crm_with_warehouse', 'edge', 'A CRM for small businesses with a built-in data warehouse.', 'crm'),
]


def j08():
    t = Test('J08', 'Classify, and fall back to a broader label when unsure', 'Classification using confidence')
    q = choice('Which software category best describes what the vendor in `description` sells or does today?',
               {k: v[1] for k, v in SUBS.items()})
    for cid, kind, desc, want in J08_CASES:
        a = t.ask({'description': desc}, {'c': q})['c']
        sub, conf = top(a), a['confidence']
        reported = sub if conf >= CONFIDENT else SUBS[sub][0]
        if want is None:
            ok = conf < CONFIDENT  # the text cannot support a specific answer
        else:
            ok = reported == want if conf >= CONFIDENT else reported == SUBS[want][0]
        t.case(cid, kind, want or 'not a confident specific label', {'reported': reported, 'top': sub,
               'confidence': round(conf, 2), 'top_p': round(a['probabilities'][sub], 2)}, ok)
    t.notes.append(f'One Choice over {len(SUBS)} subcategories; below confidence {CONFIDENT} code reports the parent category instead (cookbook cutoff).')
    return t

# ---------------------------------------------------------------- J09 live channel filter
CATS = {'question': 'A genuine request for information.',
        'incident': 'Reports that something is broken right now.',
        'unsolicited_fix': 'Tells the people debugging what to do, including instructions phrased as a question; not a request for information.',
        'chatter': 'Thanks, jokes, greetings or general conversation.',
        'spam': 'Vendor pitches, promotions or unrelated links.'}
RULES = {'question': 'highlight', 'incident': 'page_oncall', 'unsolicited_fix': 'collapse', 'chatter': 'show', 'spam': 'hide'}
HOSTILE_AT, SECRET_AT = 0.7, 0.7
J09_CASES = [
    ('doc_question', 'core', 'Is there a doc for rotating the read-replica password?', {'highlight'}),
    ('outage', 'core', 'Prod primary is refusing connections since 09:14 UTC, all writes failing', {'page_oncall'}),
    ('vendor_pitch', 'core', 'Cut your cloud bill 40%! DM me for a free audit of your Postgres fleet', {'hide'}),
    ('thanks', 'core', 'nice, thanks for the quick fix yesterday!', {'show'}),
    ('insult', 'core', 'whoever wrote this migration is an idiot, absolute garbage work', {'hide'}),
    ('pasted_secret', 'core', "here's the conn string if anyone wants to check: postgres://admin:not-a-real-password@10.2.3.4/prod", {'blur'}),
    ('fix_as_question', 'edge', "why don't you just add an index on orders.customer_id??", {'collapse'}),
    ('banter', 'edge', 'you absolute legend, you saved prod again lol', {'show'}),
    ('pt_question', 'edge', 'Alguém sabe como rodar o VACUUM sem travar a tabela?', {'highlight'}),
    ('pt_insult', 'edge', 'quem escreveu essa query é um idiota completo', {'hide'}),
    ('customer_data', 'edge', "FYI Acme Corp's contract is $1.2M a year, renewal contact is jane.doe@acme.example, mobile 07700 900123", {'blur'}),
    ('lag_question', 'edge', 'is anyone else seeing replication lag over 10 minutes on replica-3 right now?', {'page_oncall', 'highlight'}),
]


def j09():
    t = Test('J09', 'Sort a live message stream: show, highlight, hide or blur', 'Twitch chat filter')
    qs = {'category': choice('What kind of message is `message.text` in this team channel?', CATS),
          'hostile': noul('Is `message.text` insulting, hateful or harassing towards someone?',
                          'It attacks or demeans a person or group.', 'Friendly, neutral, or light banter with no target.'),
          'secret': noul('Does `message.text` expose a password, credential, or a specific customer\'s private details?')}
    for cid, kind, text, ok in J09_CASES:
        a = t.ask({'channel': {'name': '#db-help', 'purpose': 'Help with the company Postgres fleet'},
                   'message': {'user': 'member', 'text': text}}, qs)
        cat = top(a['category'])
        if a['hostile']['noul'] >= HOSTILE_AT:
            act = 'hide'
        elif a['secret']['noul'] >= SECRET_AT:
            act = 'blur'
        else:
            act = RULES[cat]
        ps = sorted(a['category']['probabilities'].values(), reverse=True)
        t.case(cid, kind, sorted(ok), {'action': act, 'category': cat, 'margin': round(ps[0] - ps[1], 2),
               'hostile': round(a['hostile']['noul'], 2), 'secret': round(a['secret']['noul'], 2)}, act in ok)
    t.notes.append('One request per message with 3 questions; actions decided by rules in code (hostile and secret thresholds 0.7).')
    return t


TESTS = [j07, j08, j09]
