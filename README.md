# Jev, job by job

A plain-English field guide to TypeSafe's **Jev** model. It covers the 20 jobs taught by the 21 official cookbooks, plus images, and tests each job with our own examples.

- **Read the article:** [ARTICLE.md](ARTICLE.md)
- **Figures (one per job, plus two explainers):** [images/](images/). How they support the article, and their briefs: [IMAGE-BRIEFS.md](IMAGE-BRIEFS.md). Redraw them with `python images/figures.py` (needs Windows with Microsoft Edge).
- **Short video (34 s):** [video/jev-video.mp4](video/jev-video.mp4) (narrated) and [video/jev-video-silent.mp4](video/jev-video-silent.mp4) (captions only); script, voice and pacing notes in [VIDEO-SCRIPT.md](VIDEO-SCRIPT.md)
- **What each official cookbook claims:** [research/COOKBOOK-NOTES.md](research/COOKBOOK-NOTES.md)
- **The prompts, ours beside TypeSafe's, compared job by job:** [PROMPTS.md](PROMPTS.md)
- **Every example and result:** [tests/results/RESULTS.md](tests/results/RESULTS.md)

## Headline findings

- Across 307 examples, Jev got 155 of 163 "core" examples right (what the cookbooks promise). It got 132 of 144 "edge" examples right; these deliberately push documented weaknesses.
- Its main weakness: **when the right answer isn't among your options, it picks the nearest one, often confidently.** Adding a "none of these" option fixed most of it: 13 of 14 requests handled correctly, up from 11 of 14, in a replay run after the locked round. A date-specific exit fixed both date failures (13 of 13, locked).
- Strongest fits for data work: picking values for database fields, checking extracted data, matching duplicate records, finding answers in contracts, and filtering what an AI may read. The weakest job was rebuilding document structure (20 of 27).
- Cost: 1,463 requests, 788,466 input tokens, **$0.0331**. Median response time was 0.31 s.

These are illustrations on small hand-written samples, not benchmarks. The article cites public-benchmark results where we have them.

## Method in one paragraph

We wrote one test per job, using examples different from TypeSafe's: CRM syncs, retention policies, company records, Postgres runbooks and invoices, all fictional. Each example is marked *core* or *edge*. Expected answers were fingerprinted before any paid call, three times:
- Round 1 was reviewed independently before locking.
- Round 2 was harder stress cases, written after round 1 proved too easy.
- Round 3 tested the obvious remedies.

Outcomes decided by ordinary code (exact quote matching, calendar maths) are labelled separately from Jev's judgments. The model was pinned to `jev-1.14.0`.

## Reproduce

Requirements: Python 3.12 with `numpy` and `Pillow`. Arial fonts are used to draw the test images (Windows paths are in `tests/make_images.py`; change them on other systems). Replaying the cached results needs no API key and costs nothing.

```bash
cd tests
python run_all.py
python run_stress.py
python run_remedy.py
```

Each command replays its round from `tests/results/cache.jsonl`. Any changed or new request is a paid call: set `TYPESAFE_API_KEY` in your environment, and optionally a spending cap with `JEV_JOBS_BUDGET_USD` (default `2.00`). The key is never printed or saved.

| File | What it is |
|---|---|
| `tests/jev.py` | Minimal API client: pinned model, response cache, hard budget cap |
| `tests/t_agents.py` … `t_images.py` | Round 1: one function per job (J01–J21) with locked expected answers |
| `tests/t_stress.py` | Round 2 stress cases (S01–S21), reusing the round-1 machinery |
| `tests/t_remedy.py` | Round 3: do the obvious fixes work? (R01, R11) |
| `tests/make_images.py` | Draws the synthetic invoices; ground truth comes from the drawing code |
| `tests/results/` | Results, the response cache, lock fingerprints, and copies of the locked test files |

## Licence and attribution

Cookbook summaries describe TypeSafe's public documentation at docs.typesafe.ai, read on 28 October 2026. Figures quoted from it are TypeSafe's. All companies, people and documents in our tests are invented.
