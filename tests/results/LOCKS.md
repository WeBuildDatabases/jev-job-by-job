# How the expected answers were locked

Before each round's first paid call, the runner wrote the SHA-256 fingerprint of every `.py` file in `tests/` to a JSON file. It also copied the files into `locked-tests/`.

| Round | Lock file | Locked at (UTC) | Combined fingerprint |
|---|---|---|---|
| 1 | `PREREGISTERED.json` | 2026-10-28 23:02 | `c68753b662680c9a23e9540150a8ac164395ac72c818dc5c4ee332a416773e78` |
| 2 (stress) | `PREREGISTERED-ROUND2.json` | 2026-10-28 23:34 | `dbbb7128b88db28ea38be4503685cf07047d0c05b3beace137357f6cf276df41` |
| 3 (remedy) | `PREREGISTERED-ROUND3.json` | 2026-10-28 23:37 | `a7f69e84e346374f34687e282969101ad05097887bada919088c33b7f1949f6f` |

**How the combined fingerprint is computed.** It is the SHA-256 of the lock file's contents, serialised as JSON with sorted keys and Python's default separators:

```python
import hashlib, json
d = json.load(open('PREREGISTERED.json'))
print(hashlib.sha256(json.dumps(d, sort_keys=True).encode()).hexdigest())
```

**Times** come from the lock files' modification times, which were recorded locally as 19:02, 19:34 and 19:37 US Eastern (UTC−4). They are self-recorded, not an external timestamp. For independent proof, publish this table, for example in a dated commit or post, before anyone else reruns the tests.

**Not locked.** In job 1 we replayed the round-3 answers with only the "not on the list" exit, without the broad "extra" question. That replay used cached responses, made no new calls, and was decided after seeing round 3. The article labels it as indicative.

**Changed after locking: two test messages, for publishing safety.** Two messages contained made-up credentials realistic enough that code-hosting secret scanners would block a public push:
- a database connection string with a password, in job 9 `pasted_secret`
- a payment-provider-style live API key, in stress test S09 `api_key`

On 28 October 2026, after all three rounds, both were replaced with obviously fake values, `postgres://admin:not-a-real-password@10.2.3.4/prod` and `live_key_FAKE_1234_5678_ABCD`. The change was made in `tests/` and in `locked-tests/`, and the two cases were re-run.
- The expected answer ("blur") and the pass/fail result were unchanged for both cases.
- Jev's "exposes a secret" score fell from 0.98 to 0.82 and from 0.93 to 0.81. Both stayed above the 0.7 blur threshold.
- This added 2 paid requests.

As a result, `t_classify.py` and `t_stress.py` no longer match the original lock hashes. Their hashes after the change are:

| File | SHA-256 after the change |
|---|---|
| `t_classify.py` | `df62f7f5c0a05282b8781a117a2ee45c3d4a4c441dd0f30c04e72c8b6bcdab23` |
| `t_stress.py` | `42425fb0bce34337944ba38ba84843416a3ed1bee67948355b194d3e33d14d18` |

Every other file still matches its original lock hash. Nothing else was changed after locking. `run_remedy.py` contains a cosmetic docstring typo (it says `run_stress.py`) and is hashed as it is.
