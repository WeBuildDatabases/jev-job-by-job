# Official cookbook notes (read 2026-10-28)

Source: docs.typesafe.ai cookbooks, fetched 2026-10-28. Numbers are copied from the pages; "(derived)" marks our arithmetic.
The site lists 21 cookbooks. The two self-consistency pages are one job here, so the article covers 20 jobs plus images.
Cross-cutting: most cookbook runs used `jev-1.12` (Twitch, memory, intelliprompter, self-consistency used `jev-1.13.0`); our tests use `jev-1.14.0`.
Almost every cookbook is a single replayed run on authored or hand-picked inputs; only re-ranking (n=40), classification-with-confidence (n=60, curated), skill suggestion (n=488) and feature discovery (800 held out) report measured results against labels. Every threshold lives in application code and is described as illustrative.

| # | Cookbook | Headline result on the page | Stated or implied limits |
|---|---|---|---|
| 1 | Function calling | 10 trading functions, 28 fillable args, 54 questions in one request per command; per-command confidence 0.53–1.00 on 14 hand-written commands; no accuracy reported | Only closed-set args are filled; integers/free text/dates keep defaults; Choice always picks, so optional args need a "stated" Noul |
| 2 | Skill suggestion | 182 skills, 488 requests; wrong loads 16.8% → 7.3%, needless loads 9.8% → 4.0% (agent alone → with suggestion); 37 fixed, 7 broken | Covered requests were written from the skills' own text ("easier than the ones users send"); second pass can only reject what the first pass ranked |
| 3 | Guardrails for LLMs | 15 illustrative messages; 4 Nouls + severity Score; code policy pass/review/block/support | Thresholds should come from your own labelled traffic; jailbreak 0.74 near the cut flips with policy; no attack on Jev itself tested |
| 4 | Citation check | 8 citations on RFC 7519 (4 planted failures); code exact-match first, then one Choice supports/contradicts/says_nothing; AUTO_ACCEPT 0.8 | Two of the four "caught" failures were caught by low-confidence review (0.27, 0.56), not confident verdicts; reworded quotes look fabricated to exact match |
| 5 | Classifying RAG passages | 72 passages scored with 4 Nouls; planted injection ranked 1st by embeddings, scored 0.99 injection by Jev and excluded | Thresholds picked for this corpus; "Nothing here is a security boundary."; an ordinary answerable query admitted nothing |
| 6 | Simple memory | Expected routes 2/6 without memory, 6/6 with memory (6 authored cases) | Memory only grows: no expiry, no replacement of outdated facts |
| 7 | Hierarchical classification | Beam search 4/4 expected leaves vs greedy 2/4 (one document per hierarchy) | n=4; sibling order "is part of the question" |
| 8 | Classification using confidence | 60 10-K filings: forced 39/60; confident half 27/30; unsure half 12/30; with division fallback 48/60 useful | Filings filtered to ones whose text supports their code; 0.9 cutoff chosen on the same 60; 3 confident errors |
| 9 | Twitch chat filter | 29 authored messages; median ~0.4 s per request; rules changed in code: "14 messages changed, 0 new requests" | No gold labels; mainly English; near-tie category (0.57 vs 0.42) decided a blur vs hide |
| 10 | SDE cascade | One staged example: hallucinated 0.95 fires, overall judge 0.56 would not; 100-prompt chart only, no numbers in text | Mini-model failure was hard-coded; "the cascade is only as good as its verifier" |
| 11 | Date extraction | 6/6 rows OK on 4 authored documents; 5 auto-accepted, 1 sent to review | Supports today/tomorrow/day-after/weekday only; the review case was rescued by code, not by `mode`; no US/EU numeric formats or "N days after X" |
| 12 | Pre-parsed value extraction | Three demos, confidences 0.90–1.00 | Candidate finding is the hard part; Jev can still pick the wrong candidate; regex miss → correct answer is "none" |
| 13 | Structure recovery | 28 lines → 17 blocks, 2 requests, 10,211 tokens, 0.8 s; prints $0.0003 (prose says $0.0015) | n=1 memo, thresholds fitted to it; lowest block confidence 0.43 |
| 14 | Re-ranking | CLERC legal, 40 queries, BM25 top-30: top-1 5% → 18%, top-5 15% → 35%, top-10 38% → 62%; 1,200 calls, $0.0645 | Cannot add a passage the first search missed; only baseline is BM25 |
| 15 | Line-by-line search | 4 queries on GitHub ToS (218 lines); exists 0.98/0.97/0.14/0.46 | ≤255 options per Choice; some line always ranks first, hence the "exists" Noul; one line per answer |
| 16 | Entity alignment | 450 beer pairs: 40 merged, 50 curator, 360 unlinked | Labels were available but precision/recall not computed |
| 17 | Intelliprompter | 5 criteria all ticked by tick 6; threshold 2.5 on a 1–5 scale | One-way ticks can't be undone; a direct mention already scores above the threshold; no negated speech tested |
| 18 | Self-consistency (Choice + Noul pages) | Noul: mean SD 0.0102 over 15 runs, 111 ms, $0.000043/call. Choice: raw agreement 90.8%; with 0.60 abstain rule 99.2% agreement, 25.8% abstained | "None of this shows accuracy or superiority"; Haiku at temperature 0 was more stable on the Choice page |
| 19 | Parallel questions | 13 questions on the GDPR article: one call $0.000497 / 0.27 s vs 13 calls $0.006090 / 2.71 s ("12.2x cheaper, 10.0x faster"); 11/13 SD exactly 0 | Speed compares sequential calls; savings shrink for short documents |
| 20 | Autoresearch feature discovery | Wine scores, 800 held out: mean 3.088 RMSE; word counts 2.466; direct Jev score 2.145; 18 questions 1.869; 38 questions after 5 rounds 1.772 | One dataset, one loop run; Score max 10 levels; most gain from the first proposal |
| + | Images and Box | "Dreamer-ready", not production; header `TypeSafe-Danger-Zone-Images: true`; Box always returns a box, so pair it with a Noul | 280–1568 px per side; EXIF rotation not applied; no recommended Box threshold yet |

Model weaknesses listed on the official jaggedness page (jev-1.13): literal reading, maths and counting, date comparison, indirection, large irrelevant state, adversarial content, contradictory instructions/criteria, Choice option order, generation.
