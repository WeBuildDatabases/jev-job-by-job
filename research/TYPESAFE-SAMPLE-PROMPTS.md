# TypeSafe's own questions, cookbook by cookbook

Pulled from the cookbook code on docs.typesafe.ai (the `.md` pages saved in `research/typesafe-pages/`). Each block is the call or object as written in the cookbook, so the wording is theirs. Where a cookbook builds its questions from data (a spec file, a taxonomy, a menu), the template or the data block is shown.

## Function calling

`cookbooks/function_calling.md` · model named on the page: `jev-1.12` · 0 question block(s)

_No literal question in the page's code._

## Skill suggestion

`cookbooks/skill_suggestion.md` · model named on the page: `jev-1.12` · 4 question block(s)

```python
Choice(
            instructions=CHOICE_INSTRUCTIONS,
            criteria={skill["name"]: skill["description"] for skill in ROSTER},
        )
```

```python
Noul(instructions=text)
```

```python
Choice(
            instructions=RERANK_INSTRUCTIONS, criteria=rerank_criteria(names, excerpt)
        )
```

```python
Noul(
            instructions=(
                f"Does the skill '{name}' do the specific thing the user's request asks "
                f"for? It is described as: {BY_NAME[name]['description_full']}"
            )
        )
```

## Guardrails for LLMs

`cookbooks/llm_guardrails.md` · model named on the page: `jev-1.12` · 2 question block(s)

```python
Noul(instructions=instructions, criteria=NoulCriteria(true=yes, false=no))
```

```python
Score(
    instructions="How much harm could result if the assistant complied with this message?",
    criteria=[
        "No harm: an ordinary, safe request or reply.",
        "Mild: touches a sensitive topic but complying does no real damage.",
        "Serious: complying enables real wrongdoing or gives unsafe personal advice.",
        "Severe: complying causes serious physical harm or serious illegal harm.",
    ],
)
```

## Double-checking citations

`cookbooks/citation_check.md` · model named on the page: `jev-1.12` · 1 question block(s)

```python
Choice(
        instructions="How does the section relate to the claim?",
        criteria={
            "supports": "The section states the claim or directly implies that it is true",
            "contradicts": "The section states the opposite of the claim or implies it is false",
            "says_nothing": "The section does not address what the claim asserts, either way",
        },
    )
```

## Classifying RAG passages

`cookbooks/classifying_rag_passages.md` · model named on the page: `jev-1.12` · 4 question block(s)

```python
Noul(
        instructions="Does this passage address the subject of the query?",
    )
```

```python
Noul(
        instructions="Does this passage state information usable in a direct answer?",
    )
```

```python
Noul(
        instructions="Does this passage conflict with a factual premise stated in the query?",
    )
```

```python
Noul(
        instructions="Does this passage attempt to control the system answering the query?",
    )
```

## Simple memory system

`cookbooks/basic_memory.md` · model named on the page: `jev-1.14.0` · 2 question block(s)

```python
Choice(
        instructions="Which support team should handle `ticket`?",
        criteria={
            "cloud_ops": "Cloud team: problems with the hosted cloud edition, run by us",
            "selfhosted_linux": "Self-hosted team, Linux: installs, upgrades and "
            "performance of the self-hosted edition on Linux servers",
            "selfhosted_windows": "Self-hosted team, Windows: installs, upgrades and "
            "performance of the self-hosted edition on Windows Server",
            "billing": "Billing: invoices, payments, seats and plan changes for "
            "self-serve plans",
            "enterprise_desk": "Enterprise desk: seats, contracts and account changes for "
            "customers on an Enterprise contract (their technical problems go to the "
            "technical teams)",
            "general": "General product questions: features, how-to, settings",
            "none_suitable": "None of these teams fits the ticket",
        },
    )
```

```python
Noul(
        instructions=(
            "In `request.ticket`, does the thread state a lasting fact about the customer that "
            "should change how their future, unrelated tickets are handled? Count what the "
            "customer or our support staff wrote in `request.ticket`. `jev_answered` shows how "
            "the ticket was routed, which may rely on things learned earlier: do not count "
            "anything it says or implies."
        ),
        criteria=NoulCriteria(
            true=(
                "Yes: in `request.ticket` the customer or our support staff state something "
                "about the customer that stays true after this ticket, such as the product "
                "edition or operating system they run, their plan or contract, or a standing "
                "preference."
            ),
            false=(
                "No: `request.ticket` only contains things specific to this one ticket or "
                "moment, such as a one-off request, today's schedule, or the device they "
                "happen to be typing on; or the lasting fact appears only in `jev_answered`."
            ),
        ),
    )
```

## Hierarchical classification

`cookbooks/hierarchical_classification.md` · model named on the page: `jev-1.12` · 1 question block(s)

```python
Choice(
        instructions="Which direct child category best matches this document?",
        criteria=keys,
    )
```

## Classification using confidence

`cookbooks/classification_using_confidence.md` · model named on the page: `jev-1.12` · 1 question block(s)

```python
Choice(
            instructions=QUESTION,
            criteria={group: describe(group) for group in sorted(GROUPS)},
        )
```

## Twitch chat filter

`cookbooks/twitch_chat_filter.md` · model named on the page: `jev-1.14.0` · 4 question block(s)

```python
Choice(
        instructions="Which category best describes the main purpose of `message.text`?",
        criteria={
            "question": "A genuine request for information from the streamer or chat, "
            "not gameplay instructions phrased as a question or a promotional pitch",
            "hype": "Cheering, reactions, or repeated emotes (PogChamp, LUL, GG, W, "
            "lets gooo); repetition alone does not make cheering spam",
            "conversation": "Ordinary chatter, opinions, replies, useful shared links, "
            "or any message whose main purpose does not fit the other categories",
            "backseat": "Unrequested gameplay advice telling the streamer what to do, "
            "including instructions phrased as a question; not a request for information",
            "spam": "Unsolicited advertising, self-promotion, follower selling, or "
            "promotional links; not ordinary cheering, repeated emotes, or a useful link",
        },
    )
```

```python
Noul(
        instructions="Is this message insulting, hateful or harassing towards someone?",
        criteria=NoulCriteria(
            true="Insults, slurs, threats or personal attacks on the streamer or another viewer",
            false="Friendly, neutral, or light banter with no target",
        ),
    )
```

```python
Noul(
        instructions="Does this message reveal a plot point or ending of the game being played?"
    )
```

```python
{
    "question": "highlight",
    "hype": "show",
    "conversation": "show",
    "backseat": "hide",
    "spam": "hide",
}
```

## SDE cascade

`cookbooks/sde_cascade.md` · model named on the page: `jev-1.12` · 3 question block(s)

```python
Noul(
            instructions=OVERALL_JUDGE, criteria=OVERALL_JUDGE_CRITERIA
        )
```

```python
Noul(
                instructions={
                    "field_spec": spec,
                    "extracted_field": value,
                    "main_question": ABSENCE_QUESTION,
                },
                criteria=ABSENCE_CRITERIA,
            )
```

```python
Noul(
                instructions={
                    "field_spec": spec,
                    "extracted_field": value,
                    "main_question": question,
                },
                criteria=criteria,
            )
```

## Date extraction

`cookbooks/date_extraction_cookbook.md` · model named on the page: `jev-1.12` · 7 question block(s)

```python
Choice(
            instructions=(
                f"How is {role} written? 'absolute' = a calendar date naming a month (e.g. "
                "'August 14', 'the 3rd of March'); 'relative' = given relative to today (today, "
                "tomorrow, the day after tomorrow, or a named weekday such as 'next Thursday'); "
                "'none' = the document does not state this date."
            ),
            criteria={"absolute": None, "relative": None, "none": None},
        )
```

```python
Choice(
            instructions=f"If {role} is an absolute calendar date, which month is it in?",
            criteria={m: None for m in MONTHS} | {"none": absent},
        )
```

```python
Choice(
            instructions=f"If {role} is an absolute calendar date, which day of the month (1-31)?",
            criteria={str(d): None for d in range(1, 32)} | {"none": absent},
        )
```

```python
Choice(
            instructions=(
                f"If {role} is an absolute calendar date, which year? Pick 'none' if the document "
                "states no year (code infers it), or 'out_of_range' if a year is stated but not "
                "in the list."
            ),
            criteria={str(y): None for y in YEAR_WINDOW}
            | {
                "out_of_range": "A year is stated for this date but is outside the listed range.",
                "none": "No year is stated for this date.",
            },
        )
```

```python
Choice(
            instructions=(
                f"If {role} is relative to today, which day is it? 'today', 'tomorrow', "
                "'day_after' (the day after tomorrow), or 'weekday' (a named day of the week)."
            ),
            criteria={
                "today": None,
                "tomorrow": None,
                "day_after": None,
                "weekday": None,
                "none": absent,
            },
        )
```

```python
Choice(
            instructions=f"If {role} names a day of the week, which one?",
            criteria={w: None for w in WEEKDAYS} | {"none": absent},
        )
```

```python
Choice(
            instructions=(
                f"If {role} names a weekday, which week is it in? 'next' for 'next Thursday' or "
                "'Thursday next week'; 'current' for 'this Thursday'; 'none' for a bare weekday "
                "with no qualifier (just 'Thursday' / 'on Thursday')."
            ),
            criteria={"current": None, "next": None, "none": absent},
        )
```

## Pre-parsed value extraction

`cookbooks/pre_parsed_value_extraction_cookbook.md` · model named on the page: `jev-1.14.0` · 4 question block(s)

```python
Choice(instructions=question, criteria=criteria)
```

```python
Choice(instructions=question, criteria={o: None for o in options})
```

```python
Noul(instructions=question)
```

```python
Choice(
            instructions="Which email address does the sender want their receipt sent to?",
            criteria=receipt_criteria,
        )
```

## Structure recovery

`cookbooks/autoformat.md` · model named on the page: `jev-1.12` · 6 question block(s)

```python
Noul(
        instructions=f"Does line {line_id(i)} pick up mid-sentence, continuing a sentence left unfinished at the end of line {line_id(i - 1)}?",
        criteria=NoulCriteria(
            true="The line starts in the middle of a sentence that began on the previous line - the line break tore the sentence apart",
            false="The line begins a new sentence, item, heading, or thought of its own",
        ),
    )
```

```python
Choice(
            instructions=f"What kind of content is block {bid}?", criteria=TYPE_CRITERIA
        )
```

```python
Choice(
                instructions=f"As a heading, what level would block {bid} occupy in this document's structure?",
                criteria=HLEVEL_CRITERIA,
            )
```

```python
Noul(
            instructions=f"Is block {bid} an instruction in a sequence where the order of the items matters?",
            criteria=NoulCriteria(
                true="It is one step of a procedure - the items around it must happen in order",
                false="Order is irrelevant - it is a loose collection, or not a list item at all",
            ),
        )
```

```python
Choice(
            instructions=f"What kind of aside is block {bid}?", criteria=CALLOUT_CRITERIA
        )
```

```python
Noul(
        instructions=f"Are lines {line_id(i - 1)} and {line_id(i)} part of the same paragraph?",
        criteria=NoulCriteria(
            true="The two lines belong to the same paragraph of running text",
            false="The two lines belong to different paragraphs or different pieces of content",
        ),
    )
```

## Re-ranking

`cookbooks/rerank_typesafe.md` · model named on the page: `jev-1.12` · 2 question block(s)

```python
Noul(
    instructions="Is this candidate the cited case?",
    criteria=NoulCriteria(
        true="The candidate states the specific rule the query cites.",
        false="The candidate is only on a similar topic.",
    ),
)
```

```python
Noul(
    instructions=(
        "The query excerpt comes from a US federal court opinion and was written "
        "immediately around a citation to a precedent; the citation itself has been "
        "removed. Could the candidate passage be from that cited precedent — does it "
        "establish the specific legal proposition the query excerpt invokes at its "
        "citation point?"
    ),
    criteria=NoulCriteria(
        true=(
            "The candidate passage states or establishes the specific rule, standard, "
            "holding, or fact pattern that the query excerpt attributes to its removed "
            "citation."
        ),
        false=(
            "The candidate passage is merely on a similar topic or doctrine; it does not "
            "supply the specific proposition the query excerpt relies on."
        ),
    ),
)
```

## Line-by-line search

`cookbooks/semantic_find.md` · model named on the page: `jev-1.12` · 2 question block(s)

```python
Choice(
        instructions=f'Which line of the document contains the answer to: "{query}"?',
        criteria={line_id(i): None for i in range(len(LINES))},
    )
```

```python
Noul(
        instructions=f'Does any line of the document address or answer: "{query}"?',
        criteria=NoulCriteria(
            true="At least one line of the document states or directly implies the answer",
            false="No line of the document addresses this",
        ),
    )
```

## Knowledge graph entity alignment

`cookbooks/entity_alignment.md` · model named on the page: `jev-1.12` · 4 question block(s)

```python
Score(
        instructions="How do the two entity descriptions relate as products?",
        criteria=LEVELS,
    )
```

```python
Noul(
        instructions="Do the two entities state the same beer name?",
    )
```

```python
Noul(
        instructions="Are the two entities from the same brewery?",
    )
```

```python
Noul(
        instructions="Do the two entities describe the same beer style?",
    )
```

## Intelliprompter

`cookbooks/intelliprompter.md` · model named on the page: `jev-1.13.0` · 1 question block(s)

```python
Score(
        instructions=(
            "How completely has the speaker covered this criterion in `transcript`: "
            f'"{description}"'
        ),
        criteria=SCORE_LEVELS,
    )
```

## Self-consistency: choices

`cookbooks/consistency_choice_cookbook.md` · model named on the page: `jev-1.13.0` · 1 question block(s)

```python
Choice(instructions=instructions, criteria=choices)
```

## Self-consistency: nouls

`cookbooks/consistency_noul_cookbook.md` · model named on the page: `jev-1.13.0` · 1 question block(s)

```python
Noul(instructions=question)
```

## Parallel questions

`cookbooks/parallel_questions.md` · model named on the page: `jev-1.12` · 13 question block(s)

```python
Noul(
        instructions="Must a personal data breach be reported to the supervisory authority within 72 hours?"
    )
```

```python
Noul(
        instructions="Does the regulation apply to organisations established outside the EU that offer goods or services to people in the EU?"
    )
```

```python
Noul(
        instructions="Must every organisation appoint a Data Protection Officer, regardless of what data it processes?"
    )
```

```python
Noul(
        instructions="Can valid consent be obtained through pre-ticked boxes or inactivity?"
    )
```

```python
Noul(
        instructions="Does the regulation grant individuals a right to erasure of their personal data?"
    )
```

```python
Noul(
        instructions="Does the regulation include a right to data portability?"
    )
```

```python
Noul(instructions="Is the GDPR a United States federal law?")
```

```python
Noul(
        instructions="Does the GDPR itself impose criminal penalties such as imprisonment?"
    )
```

```python
Choice(
        instructions="What kind of EU legal instrument is the GDPR?",
        criteria={
            "Regulation": "Directly binding law in all member states, no national implementation needed.",
            "Directive": "Sets goals that member states implement through national law.",
            "Treaty": "An international treaty between states.",
            "Recommendation": "Non-binding guidance.",
        },
    )
```

```python
Choice(
        instructions="What is the maximum administrative fine for the most serious infringements?",
        criteria={
            "TwentyM_or_4pct": "Up to EUR 20 million or 4% of annual worldwide turnover, whichever is greater.",
            "TenM_or_2pct": "Up to EUR 10 million or 2% of annual worldwide turnover, whichever is greater.",
            "FixedCap": "A fixed amount not tied to turnover.",
            "NoFines": "The GDPR provides no administrative fines.",
        },
    )
```

```python
Score(
        instructions="How strong are the rights the GDPR grants to individuals over their data?",
        criteria=[
            "None: individuals get no rights over their data.",
            "Weak: a right to be informed, but little control.",
            "Moderate: access and correction rights, but limited means to act on them.",
            "Strong: access, erasure, portability, and objection rights, with enforcement behind them.",
        ],
    )
```

```python
Score(
        instructions="How severe are the penalties the GDPR provides for non-compliance?",
        criteria=[
            "None: no penalties of any kind.",
            "Symbolic: small fixed fines unlikely to change behavior.",
            "Substantial: fines large enough to matter to most companies.",
            "Severe: fines scaled to global revenue, material even to the largest companies.",
        ],
    )
```

```python
Score(
        instructions="How heavy is the compliance burden the GDPR places on organisations?",
        criteria=[
            "Negligible: no meaningful obligations.",
            "Light: a few notices and disclosures.",
            "Moderate: documented processes and some dedicated roles for larger processors.",
            "Heavy: records, impact assessments, officers, and breach procedures for many organisations.",
            "Extreme: obligations so demanding that ordinary organisations cannot fully comply.",
        ],
    )
```

## Autoresearch feature discovery

`cookbooks/autoresearch_feature_discovery.md` · model named on the page: `jev-1.12` · 9 question block(s)

```python
{
                    "op": {"type": "string", "enum": ["add", "revise", "drop"]},
                    "target": {"type": "string"},
                    "name": {"type": "string"},
                    "kind": {"type": "string", "enum": ["intensity", "presence"]},
                    "question": {"type": "string"},
                }
```

```python
{"op": "add", "target": "", "name": ..., "kind": ..., "question": ...}
```

```python
{"op": "revise", "target": <name of an existing feature>, "name": ..., "kind": ...,
  "question": ...}
```

```python
{"op": "drop", "target": <name of an existing feature>, "name": "", "kind": "intensity",
  "question": ""}
```

```python
{
                "id": f"{name}@{round_index}",  # unique, so earlier rounds keep their columns
                "name": name,
                "kind": action["kind"],
                "question": action["question"],
                "replaces": action["target"] if action["op"] == "revise" else "",
            }
```

```python
Score(
                instructions=feature["question"], criteria=INTENSITY_LEVELS
            )
```

```python
Noul(
                instructions=feature["question"], criteria=PRESENCE_CRITERIA
            )
```

```python
{"name": f["name"], "kind": f["kind"], "question": f["question"]}
```

```python
Score(
                instructions=(
                    "Judging only by what this tasting note says, how good is the wine?"
                ),
                criteria=SCORE_LEVELS,
            )
```

## Shopping cart

`cookbooks/cart_from_primitives.md` · model named on the page: `jev-1.14.0` · 2 question block(s)

```python
Choice(
        instructions=(
            f"This is a cafe order. Items already accounted for: {already}. "
            "Which remaining menu item does the order mention? If the order mentions more "
            "than one remaining item, choose the one mentioned first."
        ),
        criteria=criteria,
    )
```

```python
Choice(
            instructions=f"Which {field} did the order ask for, for the {item_name}?",
            criteria=criteria,
        )
```

## Reading a scanned vaccination record

`cookbooks/reading_scanned_documents.md` · model named on the page: `jev-1.14.0` · 7 question block(s)

```python
{
        "type": "noul",
        "instructions": {
            "question": "Does the vaccines table in `page` record any vaccine that is not "
                        "in this list?",
            "list": VACCINES,
        },
    }
```

```python
{
            "type": "noul",
            "instructions": f"Is {vaccine} recorded in the vaccines table in `page`, with "
                            "exactly this name?",
        }
```

```python
{
            "type": "box",
            "instructions": f"the whole {vaccine} row of the vaccines table in `page`",
        }
```

```python
{
            "type": "choice", "criteria": YEAR,
            "instructions": "Dates on this record are written day/month/year, so the year "
                            f"is the last part. What year is written in {where}?",
        }
```

```python
{
            "type": "noul",
            "instructions": f"Is the date in {where} fully legible, with nothing covering, "
                            "staining, smudging or blurring any of it?",
        }
```

```python
{
            "type": "noul",
            "instructions": {"question": IN_DATE_QUESTION, "entry": row["id"]},
            "criteria": IN_DATE_CRITERIA,
        }
```

```python
{
        "type": "noul",
        "instructions": {"question": IN_DATE_QUESTION + " The departure date is on `page`.",
                         "entry": f"the {row['vaccine']} row of the vaccines table in "
                                  "`page`"},
        "criteria": IN_DATE_CRITERIA,
    }
```

## OCR confidence and bounding boxes

`cookbooks/ocr_confidence_bounding_boxes.md` · model named on the page: `jev-1.14.0` · 4 question block(s)

```python
Box(
            instructions=f"{FIELDS[field]}, printed as “{value}” in `page`"
        )
```

```python
Noul(
            instructions=f"Is “{value}” {FIELDS[field]} on `page`? {SAME_VALUE}"
        )
```

```python
Box(
            instructions=f"{FIELDS[field]}, printed as “{values[field]}” in this image: {image}"
        )
```

```python
Noul(
            instructions=f"Image: {image}\nDoes this cropped image clearly show {FIELDS[field]}"
            f" as “{values[field]}”? {SAME_VALUE} Answer no if it is cut off, unreadable or"
            " different."
        )
```

## Feeder-cam visit log

`cookbooks/feeder_watch.md` · model named on the page: `jev-1.14.0` · 8 question block(s)

```python
Noul(instructions="Is there at least one bird in `frame`?")
```

```python
Choice(
        instructions="How many birds are in `frame`?",
        criteria={
            "none": "No bird at all.",
            "one": "Exactly one bird.",
            "several": "Two or more birds.",
        },
    )
```

```python
Box(instructions="The most prominent bird in `frame`")
```

```python
Choice(
        instructions="What species is the leftmost bird in `frame`?", criteria=SPECIES
    )
```

```python
Choice(
        instructions="What species is the rightmost bird in `frame`?", criteria=SPECIES
    )
```

```python
Box(instructions="The leftmost bird in `frame`")
```

```python
Box(instructions="The rightmost bird in `frame`")
```

```python
Box(instructions=f"{BOX_TARGETS[sp]} in `frame`")
```
