"""Shared test bookkeeping. Each case records what we expected (written before any call) and what came back."""
import jev


class Test:
    def __init__(self, tid, job, cookbook):
        self.tid, self.job, self.cookbook = tid, job, cookbook
        self.cases, self.notes, self.tokens, self.seconds, self.requests = [], [], 0, 0.0, 0

    def ask(self, state, questions, assets=None):
        r = jev.ask(state, questions, assets, tag=self.tid)
        self.tokens += r['usage']['input_tokens']
        self.seconds += r['seconds']
        self.requests += 1
        return r['answers']

    def case(self, cid, kind, expected, got, passed, detail=''):
        """kind: 'core' = what the cookbook says Jev does; 'edge' = probes a documented limit;
        'code' = outcome decided by ordinary code, not Jev; 'measure' = a cost/speed measurement. Only core/edge are tallied."""
        self.cases.append({'id': cid, 'kind': kind, 'expected': expected, 'got': got,
                           'pass': bool(passed), 'detail': detail})

    def summary(self):
        def tally(kind):
            cs = [c for c in self.cases if c['kind'] == kind]
            return f"{sum(c['pass'] for c in cs)}/{len(cs)}"
        return {'id': self.tid, 'job': self.job, 'cookbook': self.cookbook, 'core': tally('core'),
                'edge': tally('edge'), 'requests': self.requests, 'input_tokens': self.tokens,
                'cost_usd': round(self.tokens * jev.PRICE, 6), 'api_seconds': round(self.seconds, 2),
                'notes': self.notes, 'cases': self.cases}


def top(answer):
    return answer['choice']


def p(answer, option):
    return answer['probabilities'][option]
