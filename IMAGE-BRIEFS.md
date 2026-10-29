# Images: how they support the article, and the briefs behind them

**Status: produced.** All 23 figures are in [`images/`](images/), both as PNG (used by the article) and as SVG (editable, sharp at any size). They are drawn by code, so every label and number matches the test results. To change one, edit `images/figs_jobs.py` (jobs 2 to 21) or `images/figures.py` (hero, weakness and job 1), then run `python images/figures.py 07` to redraw a single figure, or with no argument to redraw them all. Drawing needs Windows with Microsoft Edge and the Segoe UI font.

## How the imagery helps the article

The article is long: 21 sections for non-technical readers. The images do four jobs that the text can't do on its own.

1. **One grammar, repeated 21 times.** Every figure reads left to right: *the material → Jev's answer → what your software does.* That is the article's core idea, "Jev judges, your software decides", made visual. By the third figure a reader can understand any section from its picture alone.
2. **A real example, not a metaphor.** Each figure shows the actual example and score from our tests, such as the ticket, the 0.98 and the "not on the list" chip. There are no robots or glowing brains, and nothing that would need explaining.
3. **The limit, not just the success.** Where a job has a known weakness, the figure shows it beside the success: the menu exit (job 1), the outdated passage that got through (job 5), the "consistent but a guess" row (job 18) and the "prototype" badge (job 21). Readers skim pictures, so the caveat has to be in the picture.
4. **Colour by family, so readers can find their place.** The five job families and the images section each have one accent colour, carried through the tag, the highlights and the takeaway bar. A reader scrolling back can find "the search ones" by colour.

**Placement.** Each figure sits directly under its section heading, before "What it does", so the picture frames the text that follows. The hero figure (`job-00`) opens "The thirty-second version", and the weakness figure (`fig-menu`) opens "The one weakness to remember". Every figure has alt text that states its point in one sentence, for screen readers and for when an image fails to load.

**Text in images.** There are short labels only, mostly under six words, plus one takeaway sentence at the bottom of each figure. The closing sentence restates the section's lesson in plain words so the image still works when it is shared on its own, for example in a slide or a post.

## Series style (applies to every image)

- **Format:** 1600 × 900 px landscape, PNG plus SVG, readable when shrunk to 800 px wide.
- **Look:** flat editorial illustration with no gradients or 3D. Off-white background (#F7F5F0) and navy ink (#1F2A44).
- **Colour rules (after the adversarial review).** Green (#2B8A3E), amber (#E8890C) and red (#C92A2A) mean only *act*, *ask a person* and *stop*, and appear only where that is the meaning. The Box answer is blue (#1C7ED6). Family accents use hues that never collide with those three, and carry no judgement:
  - blue (#1971C2) for agents and assistants
  - cyan (#0C8599) for classification
  - violet (#6741D9) for extraction
  - magenta (#AE3EC9) for search and matching
  - slate (#4C5A73) for techniques
  - charcoal (#343A40) for images
- **Icons (legend in job-00):** tick = act; person = ask a person; cross = stop; gear = software runs it (neutral); "?" = caveat.
- **Honesty rules:**
  - Every figure shows "N of M examples right in our tests" in its tag row.
  - Thresholds are drawn as a dark tick on bars.
  - Quotes are verbatim from the tests, or marked with an ellipsis.
  - Job 21 shows the real test scan with Jev's actual boxes.
  - Fixed cases show the "before the fix" failure.
- **Type:** Bahnschrift (an engineering DIN-style face) for titles, scores and takeaways; Segoe UI for body text; monospace only for real code and column names.
- **Anti-template rules (from a design "AI slop" pass):** no ALL-CAPS eyebrows, pills or "A · B" meta strings; flat cards with hairline borders instead of the same soft shadow on everything; no emoji as icons; no em dashes or arrows inside sentences; sentence case throughout.
- **Fixed layout:**
  - "Job N" in navy with the family name in grey, top left
  - the title, in large bold type
  - three small sentence-case column captions, plain grey text
  - the content
  - one closing sentence in plain type, bottom left
- **Plain-language pass (29 October 2026).** Removed the things that mark a figure as machine-made: colour dots before captions, the coloured "Job N" tag and divider, the coloured bar beside the takeaway, the "Jev, job by job" sign-off, and slogan-style takeaways (two clipped sentences, semicolons, "X: Y" labels). Every takeaway and sub-label is now an ordinary sentence. "sure 1.00" reads "confidence 1.00".
- **Simplification pass (29 October 2026).** Five figures were cut back to the cookbook idea: job 7 shows three branches and no ranking card; job 13 shows six short lines with one label each; job 14 names only the right article and Jev's top three, the other rows are placeholder bars; job 17 tracks three criteria including the postponed budget; job 20 uses three questions. Scores and quotes are unchanged.
- **Recurring motif: the answer card.** Jev's answer always uses one of four shapes, drawn the same way every time:
  - **Yes/No:** a bar filled to the probability, with the number at the right.
  - **Which one:** pill-shaped chips, with the chosen one filled.
  - **How much:** a track with a marker.
  - **Where:** a red rectangle on the material itself.
- **Outcomes:** three round icons. A green tick means act, an amber person means ask a person, and a red cross means don't act or block.
- **Never show:** real logos, real people, code screenshots, or the word "magic".

The briefs below were written before the figures were drawn. They record the **one idea** each image must get across, and the **alt text** used in the article. Where a figure departs from its brief, the figure follows the test results.

Each brief below gives the **one idea** the image must get across, the **scene**, and **alt text** to use in the article.

---

## LLMs and agents (teal)

**job-01 · Turn a request into the right action**
- **One idea:** a plain sentence becomes a precise button press, and every menu needs a "not on the list" exit.
- **Scene:** a speech bubble, "dump contacts to parquet for the last week", flows into a card of chips. The chips "export_table", "contacts", "parquet" and "1 week" are filled. An arrow leads to a gear labelled "runs". Below, a second bubble, "export the leads table as xlsx", hits the card; its chips read "not on the list" and the arrow stops at a hand-raise icon labelled "can't do that, ask".
- **Alt text:** "A typed request is turned into a specific action with chosen settings; an unsupported request is held back."

**job-02 · Pick the right tool for an AI agent, or none**
- **One idea:** a shelf of 20 tools; Jev points at one, or at an empty slot.
- **Scene:** a toolbox wall with 20 labelled drawers, one glowing teal. A second, smaller panel shows the request "Push these contacts into Pipedrive" with every drawer dim and a chip reading "none fits".
- **Alt text:** "From twenty tools the agent is pointed at the one that fits, or told none does."

**job-03 · Screen what goes into and out of an AI assistant**
- **One idea:** a checkpoint on both sides of the chatbot.
- **Scene:** a conveyor belt of message envelopes passes a checkpoint gate on its way into a chat window and again on its way out. Yes/No bars sit above the gate: "manipulation 98%", "deletes data 3%". Three exit chutes are labelled pass, review and block.
- **Alt text:** "Messages are scored for specific risks before they reach the assistant and before replies leave it, then sorted into pass, review or block."

**job-04 · Check that a citation really supports the claim**
- **One idea:** hold the claim next to the source and compare.
- **Scene:** split view. On the left a sticky note reads "Backups are kept forever". On the right a policy page has a highlighted line, "retained for 35 days". Between them a chip row shows supports / contradicts / says nothing, with "contradicts" filled.
- **Alt text:** "A claim is compared with the exact passage it cites and marked as contradicted."

**job-05 · Decide which search results an AI is allowed to read**
- **One idea:** a bouncer for search results.
- **Scene:** five document cards queue at a velvet rope in front of a chat window. Two get a tick and go through. One gets a "conflict" flag and goes in a separate lane. One small card has a hidden "Note to AI…" line and gets a red stop.
- **Alt text:** "Retrieved passages are admitted, flagged as conflicting, or stopped before the AI reads them."

**job-06 · Remember what matters about a customer**
- **One idea:** keep the lasting fact, drop the passing remark.
- **Scene:** a customer card with a small notebook. Ticket bubbles float toward it. "We use Salesforce, EU data only" is pinned into the notebook. "Resend last month's invoice" floats away. A third bubble, "my password is…", is shredded.
- **Alt text:** "Lasting customer facts are saved for later; one-off requests and secrets are not."

## Classification (amber)

**job-07 · File a record into a deep category tree**
- **One idea:** walk down a tree while keeping a few paths open.
- **Scene:** a tree diagram three levels deep. Three highlighted paths descend at once, like three torchlights. Two fade out and one reaches the leaf "Medical Devices". A greyed path into "Health Care" shows the trap the narrow search fell into.
- **Alt text:** "Several candidate paths down a category tree are explored together, and the best one reaches the right leaf."

**job-08 · Classify, and fall back to a broader label when unsure**
- **One idea:** be specific when sure and general when not.
- **Scene:** two company cards. The first lands on a precise shelf labelled "Cloud Data Warehouse" with "sure: 0.97". The second card, "We help companies get more from their data", lands one shelf up on "Data Infrastructure", with a small "not sure, going broader" tag.
- **Alt text:** "A confident answer gets a specific label; an uncertain one is reported at the broader level."

**job-09 · Sort a live message stream**
- **One idea:** every message gets sorted in under a second.
- **Scene:** a team chat column. Messages are tagged in teal, amber and red: a question highlighted, an outage paged with a bell, a vendor pitch struck through, a pasted password blurred, an insult hidden.
- **Alt text:** "Live chat messages are highlighted, paged, hidden or blurred by rules applied to quick judgments."

## Extraction (coral)

**job-10 · Check a cheap extractor and escalate only the doubtful records**
- **One idea:** a cheap first pass, a quick check, and the expensive expert only when needed.
- **Scene:** a stack of company "About us" pages goes through a small fast machine labelled "cheap extractor", then past an inspector with a Yes/No bar ("made up? 91%"). Most records drop into a tray marked "accept". One red-flagged record goes up a ramp to a larger, slower machine labelled "expert model".
- **Alt text:** "Extracted fields are checked for invented or misplaced values, and only flagged records go to a costlier model."

**job-11 · Read a date from text and let code do the calendar maths**
- **One idea:** Jev reads the pieces, and the calculator does the arithmetic.
- **Scene:** the sentence "The migration window is next Tuesday" is split into chips: "relative", "Tuesday", "next week". The chips feed a classic desk calendar that circles 3 November. A small calculator icon is labelled "code".
- **Alt text:** "The parts of a date are read from text and an ordinary calendar function turns them into the exact day."

**job-12 · Pick the right value from candidates code found**
- **One idea:** code finds every candidate, and Jev picks the one you asked for.
- **Scene:** an email with four dollar amounts circled by a dotted highlighter labelled "code finds all". A question card, "Which amount will they actually pay?", fills one chip: "$11,000.00". The chosen value is copied exactly into a database row.
- **Alt text:** "Pattern matching finds every amount in an email; the judgment picks the one that answers the question."

**job-13 · Rebuild headings, lists and code from flattened text**
- **One idea:** a wall of text becomes a tidy document again.
- **Scene:** on the left, a grey block of plain text with ragged line breaks. On the right, the same words laid out with a bold heading, numbered steps, a monospace code strip and a yellow warning box. Small chips between them read heading, step, code and warning.
- **Alt text:** "Plain text that lost its formatting is rebuilt into headings, steps, code and warnings without changing any words."

## Search and matching (violet)

**job-14 · Move the most useful search result to the top**
- **One idea:** keyword search finds the pile, and Jev puts the right page on top.
- **Scene:** a ten-card list from "keyword search" with the right card at position 7. An arrow labelled "Jev re-ranks" shows the same ten cards with that card now at position 1.
- **Alt text:** "A keyword search shortlist is reordered so the article that actually fixes the problem comes first."

**job-15 · Find the exact line in a long document**
- **One idea:** point to the line, and say so when there isn't one.
- **Scene:** a long numbered contract with one line highlighted in violet: "Backups are retained for 35 days." Beside it, a second query, "Price per GB?", gets a Yes/No bar near zero labelled "not in this document".
- **Alt text:** "The line that answers a question is located, and questions the document doesn't answer are reported as absent."

**job-16 · Decide whether two records are the same thing**
- **One idea:** merge, leave apart, or ask a person.
- **Scene:** three pairs of company record cards. Pair 1, "Acme Data Systems Inc" and "ACME Data Sys", is joined by a zip and labelled "merge". Pair 2, Bluefin Analytics and Bluefin Seafoods, has a gap and "separate". Pair 3, Snowline GmbH (Munich) and Snowline Inc (Denver), has a question mark and a person icon labelled "check".
- **Alt text:** "Pairs of records are judged the same, different, or related enough that a person should decide."

**job-17 · Tick off a checklist as a conversation happens**
- **One idea:** a live checklist that only ticks when a point is truly covered.
- **Scene:** a video call window with a live transcript scrolling and a checklist beside it. "Database: ticked", "Data size: ticked", "Decision-maker: ticked". "Budget" has a speech bubble, "let's come back to that later", and stays unticked.
- **Alt text:** "A sales checklist is ticked as each point is actually covered; a postponed topic stays open."

## Techniques (slate green)

**job-18 · Ask more than once, act only when answers agree**
- **One idea:** agreeing answers are worth acting on, but agreement isn't the same as being right.
- **Scene:** three rows of eight identical ticket cards, each with a chip answer.
  - Top row: "Production cluster down" with all eight chips "Outage", a green tick and "act".
  - Middle row: "Our invoice went up because slow reports…" with mostly "not sure" chips, a hand icon and "ask a person".
  - Bottom row: "It is broken again." with all eight chips "Outage · sure 1.00" and a small amber question mark, labelled "consistent, but a guess".
- **Alt text:** "Repeated answers that agree are acted on and unclear ones go to a person, but a vague ticket can get the same confident guess every time."

**job-19 · Ask many questions in one request**
- **One idea:** read the contract once and answer ten questions.
- **Scene:** on the left, one contract with ten question cards fanned around it and a single envelope labelled "1 trip". On the right, the same contract photocopied ten times with ten envelopes labelled "10 trips". A small price tag on each side shows the difference.
- **Alt text:** "Sending all questions with one copy of a document costs a fraction of sending the document separately for each question."

**job-20 · Turn free text into numbers a model can use**
- **One idea:** sentences become spreadsheet columns.
- **Scene:** an account-manager note ("Our sponsor left last month…") turns into a spreadsheet row of Yes/No values: competitor 0.1, sponsor left 0.9, budget cut 0.2. Arrows lead into a small chart labelled "renewal risk".
- **Alt text:** "Each note is turned into yes/no scores that a standard prediction model uses to forecast renewal risk."

## Images (black and white with a red box)

**job-21 · Read scanned documents**
- **One idea:** what is this page, is it signed, and where is the total?
- **Scene:** a scanned invoice in greyscale. A red rectangle sits around "$3,820.00" and a second around the signature. Three answer cards beside it read "Invoice", "Signed: yes" and "Stamp: PAID". A small grey "prototype" badge sits in the corner, since TypeSafe calls image support experimental.
- **Alt text:** "A scanned invoice is identified, checked for a signature and stamp, and its total located with a box."
