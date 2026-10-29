# Short video (34 s): "Jev judges. Your software decides."

**Status: built.** The files are [`video/jev-video.mp4`](video/jev-video.mp4) (34 s, with narration) and [`video/jev-video-silent.mp4`](video/jev-video-silent.mp4) (captions only, for muted autoplay). Both are 1920 × 1080 at 30 fps.
- **Voice:** "John" from Piper, a free open-source speech engine that runs locally, so the script is never sent anywhere. The voice is built from public-domain LibriVox recordings, so it is safe for public use. "Jev" is pronounced /dʒɛv/, to rhyme with "rev". To use a recorded human voice instead, keep the phrase lengths in `video/build/timeline.json` as a guide, or record one file per line of `video/vo_lines.txt`.
- **Pacing:** each phrase is recorded separately at natural speed and the timeline is built from the real lengths: a 0.4 s pause within a beat, 0.75 s between beats, and a 2 s quiet ending. Every cut and animation fires on its own words. The three questions each get their own picture, "Act" and "Ask a person" appear as they are spoken, the coin lands on "three cents", and the closing lines appear as they are said. The length grew from 30 s to 34 s so nothing is rushed.
- **Visuals:** drawn with the same kit as the article figures, in the same colour rules. The numbers on screen come from the test results: sure 0.91 (company match), the $4,584.00 total due, line 17 answered at 0.99, 1,463 decisions and $0.033.
- **Rebuild:** `pip install piper-tts imageio-ffmpeg`, download `en_US-john-medium.onnx` and its `.onnx.json` from huggingface.co/rhasspy/piper-voices (en/en_US/john/medium), set `PIPER_VOICE` to the `.onnx` path, then run `powershell -File video/make_video.ps1`. It also needs Node with Playwright and Microsoft Edge.
- **Captions:** shown throughout, except in the final scene, where the same words are on screen.

**Audience:** business and operations leaders, not engineers.
**Goal:** they understand what Jev is for, why it's cheap enough to use everywhere, and that people stay in control.
**Length:** originally 30 seconds; built at 34 seconds so the 74 words are spoken at a natural pace with pauses.
**Look:** the same flat editorial style as the article images: off-white background, navy line work, one accent colour per scene, and the white "answer card" motif (see [IMAGE-BRIEFS.md](IMAGE-BRIEFS.md)). Motion is simple: cards slide in, bars fill, a box draws itself.
**Sound:** light, steady percussion that drops out at 0:26 for the tagline.

| Time | Voice-over | On screen | On-screen text |
|---|---|---|---|
| 0:00–0:04 | "Every day, your team makes thousands of small calls." | A desk piled with tickets, invoices, contracts and customer records. A clock ticks quickly in the corner. | *Thousands of small calls* |
| 0:04–0:10 | "Is this the same customer? Which amount is the total? Does this contract cover backups?" | Three quick vignettes, two seconds each: two company cards slide together; a red box draws around "$4,584.00" on an invoice; a line in a contract lights up. | Each question appears briefly beside its vignette. |
| 0:10–0:15 | "Jev makes those calls in a third of a second, and tells you how sure it is." | The answer card pops up three times: "Same company? Yes, sure 0.91", "Total due? $4,584.00", "Covers backups? Line 17, answered 0.99". A small stopwatch reads 0.3 s. | *0.3 seconds* |
| 0:15–0:21 | "Your rules decide what happens: act, or ask a person." | A fork in a conveyor belt. Confident cards roll on to a green "done" tick. One low-confidence card ("sure 0.34") is lifted off by a friendly hand icon labelled "review". | *Act — or ask a person* |
| 0:21–0:26 | "We put it through fourteen hundred test decisions. The whole bill: about three cents." | A long strip of answer cards streams past and collapses into a single coin with "3¢" on it. | *1,463 test decisions, $0.033 in total* |
| 0:26–0:30 | "Jev judges. Your software decides. Keep your people for the calls that matter." | The pile of paperwork from the opening is now neatly sorted into trays. One person leans back from the desk. Then logo or end card. | **Jev judges. Your software decides.** Small line: *Results and method: [repo link]* |

## Voice-over, as one block (74 words)

> Every day, your team makes thousands of small calls. Is this the same customer? Which amount is the total? Does this contract cover backups? Jev makes those calls in a third of a second, and tells you how sure it is. Your rules decide what happens: act, or ask a person. We put it through fourteen hundred test decisions. The whole bill: about three cents. Jev judges. Your software decides. Keep your people for the calls that matter.

## Claim check (every claim maps to the article)

| Claim in the video | Source |
|---|---|
| "a third of a second" | Median response time 0.31 s across 1,463 requests (images about 0.7 s). Article: "The thirty-second version". |
| "tells you how sure it is" | Choice and Score answers carry a confidence value; Yes/No answers are probabilities. Article: jobs 8 and 18. |
| "fourteen hundred test decisions … about three cents" | 1,463 paid requests, $0.0331 in total. Article: Appendix. |
| "Same company / Total due / Backups line" vignettes | Jobs 16, 21 and 15 in the article, all passed in our tests. |
| "act, or ask a person" | The pattern running through every cookbook; article: "Jev judges. Your software decides." |

**Do not add** accuracy percentages, "never wrong", or "replaces your team". Our tests are illustrations, not benchmarks, and the article's main warning ("give every menu a 'none of these' option") doesn't fit in 30 seconds. The end card should therefore point to the article.

## Optional 15-second cut

> Thousands of small calls a day: same customer? which total? is this clause here? Jev answers in a third of a second and says how sure it is. Your rules decide. Jev judges. Your software decides.
