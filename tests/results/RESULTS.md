# Test results

Model `jev-1.14.0`. Total paid so far: $0.0331. Core = what the cookbook says Jev does; edge = probes a documented limit.

| Test | Job | Core passed | Edge passed | Requests | Input tokens | Cost (USD) |
|---|---|---|---|---|---|---|
| J01 | Turn a plain-English request into the right action | 5/5 | 2/3 | 8 | 8,335 | 0.00035 |
| J02 | Pick the right tool for an AI agent, or none | 6/6 | 4/4 | 18 | 13,631 | 0.00057 |
| J03 | Screen what goes into and out of an AI assistant | 7/7 | 4/4 | 11 | 5,763 | 0.00024 |
| J04 | Check that a citation really supports the claim | 4/4 | 3/3 | 7 | 2,877 | 0.00012 |
| J05 | Decide which search results an AI is allowed to read | 8/8 | 2/2 | 10 | 4,427 | 0.00019 |
| J06 | Remember what matters about a customer | 6/6 | 3/3 | 10 | 3,896 | 0.00016 |
| J07 | File a record into a deep category tree | 4/5 | 2/3 | 110 | 39,042 | 0.00164 |
| J08 | Classify, and fall back to a broader label when unsure | 6/6 | 4/4 | 10 | 7,202 | 0.00030 |
| J09 | Sort a live message stream: show, highlight, hide or blur | 6/6 | 6/6 | 12 | 6,674 | 0.00028 |
| J10 | Check a cheap extractor and escalate only the doubtful records | 6/6 | 2/2 | 8 | 6,450 | 0.00027 |
| J11 | Read a date from text and let code do the calendar maths | 5/5 | 3/4 | 14 | 20,436 | 0.00086 |
| J12 | Pick the right value from candidates that code found | 5/5 | 3/3 | 8 | 4,459 | 0.00019 |
| J13 | Rebuild headings, lists and code from flattened text | 10/11 | 4/5 | 2 | 4,037 | 0.00017 |
| J14 | Move the most useful search result to the top | 4/4 | 2/2 | 60 | 23,519 | 0.00099 |
| J15 | Find the exact line in a long document that answers a question | 4/4 | 3/3 | 7 | 7,714 | 0.00032 |
| J16 | Decide whether two records are the same thing | 5/6 | 4/4 | 10 | 4,591 | 0.00019 |
| J17 | Tick off a checklist as a conversation happens | 3/3 | 2/2 | 7 | 4,367 | 0.00018 |
| J18 | Ask more than once, act only when answers agree | 4/4 | 4/4 | 64 | 27,168 | 0.00114 |
| J19 | Ask many questions in one request | 2/2 | 1/1 | 22 | 13,048 | 0.00055 |
| J20 | Turn free text into numbers a prediction model can use | 2/2 | 1/1 | 800 | 334,184 | 0.01404 |
| J21 | Read scanned documents: what is it, is it signed, where is the total | 19/19 | 5/5 | 7 | 40,490 | 0.00170 |
| S01 | Turn a plain-English request into the right action | 2/2 | 2/4 | 6 | 6,260 | 0.00026 |
| S02 | Pick the right tool for an AI agent, or none | 3/3 | 2/3 | 11 | 8,155 | 0.00034 |
| S03 | Screen what goes into and out of an AI assistant | 1/1 | 4/5 | 6 | 3,314 | 0.00014 |
| S04 | Check that a citation really supports the claim | 1/1 | 4/4 | 5 | 2,046 | 0.00009 |
| S05 | Decide which search results an AI is allowed to read | 2/2 | 2/3 | 5 | 2,252 | 0.00010 |
| S06 | Remember what matters about a customer | 1/2 | 4/4 | 7 | 2,798 | 0.00012 |
| S07 | File a record into a deep category tree | 1/1 | 4/4 | 73 | 25,756 | 0.00108 |
| S08 | Classify, and fall back to a broader label when unsure | 0/0 | 5/5 | 5 | 3,570 | 0.00015 |
| S09 | Sort a live message stream: show, highlight, hide or blur | 0/0 | 5/5 | 5 | 2,778 | 0.00012 |
| S10 | Check a cheap extractor and escalate only the doubtful records | 0/0 | 4/4 | 4 | 3,268 | 0.00014 |
| S11 | Read a date from text and let code do the calendar maths | 2/2 | 3/4 | 12 | 15,773 | 0.00066 |
| S12 | Pick the right value from candidates that code found | 2/2 | 3/3 | 5 | 2,528 | 0.00011 |
| S13 | Rebuild headings, lists and code from flattened text | 3/7 | 3/4 | 2 | 2,859 | 0.00012 |
| S14 | Move the most useful search result to the top | 4/4 | 2/2 | 60 | 23,462 | 0.00098 |
| S15 | Find the exact line in a long document that answers a question | 2/2 | 4/4 | 6 | 13,130 | 0.00055 |
| S16 | Decide whether two records are the same thing | 1/1 | 3/4 | 5 | 2,325 | 0.00010 |
| S17 | Tick off a checklist as a conversation happens | 2/2 | 3/3 | 7 | 5,211 | 0.00022 |
| S18 | Ask more than once, act only when answers agree | 1/1 | 3/3 | 32 | 13,528 | 0.00057 |
| S20 | Turn free text into numbers a prediction model can use | 1/1 | 0/0 | 800 | 334,184 | 0.01404 |
| S21 | Read scanned documents: what is it, is it signed, where is the total | 5/5 | 8/8 | 5 | 25,197 | 0.00106 |
| R01 | Turn a plain-English request into the right action (with remedy) | 2/7 | 7/7 | 14 | 18,095 | 0.00076 |
| R11 | Read a date from text and let code do the calendar maths (with remedy) | 7/7 | 6/6 | 14 | 33,385 | 0.00140 |

## J01 Turn a plain-English request into the right action
Cookbook: Function calling

- One request per command carrying 10 questions; code runs the call only if min confidence >= 0.7.

| Case | Kind | Expected | Got | Pass |
|---|---|---|---|---|
| contacts_parquet_week | core | {"tool": "export_table", "args": {"table": "contacts", "format": "parquet", "since": "1w"}} | {"tool": "export_table", "args": {"table": "contacts", "format": "parquet", "since": "1w"}, "min_confidence": 0.99, "auto_runs": true} | yes |
| count_invoices | core | {"tool": "row_count", "args": {"table": "invoices"}} | {"tool": "row_count", "args": {"table": "invoices"}, "min_confidence": 1.0, "auto_runs": true} | yes |
| dupes_by_domain | core | {"tool": "find_duplicates", "args": {"table": "accounts", "key": "domain"}} | {"tool": "find_duplicates", "args": {"table": "accounts", "key": "domain"}, "min_confidence": 1.0, "auto_runs": true} | yes |
| nightly_billing_backup | core | {"tool": "schedule_backup", "args": {"database": "billing", "frequency": "daily"}} | {"tool": "schedule_backup", "args": {"database": "billing", "frequency": "daily"}, "min_confidence": 1.0, "auto_runs": true} | yes |
| invoices_json_no_window | core | {"tool": "export_table", "args": {"table": "invoices", "format": "json"}} | {"tool": "export_table", "args": {"table": "invoices", "format": "json"}, "min_confidence": 0.97, "auto_runs": true} | yes |
| negated_then_count | edge | {"tool": "row_count", "args": {"table": "contacts"}} | {"tool": "row_count", "args": {"table": "contacts"}, "min_confidence": 0.99, "auto_runs": true} | yes |
| unsupported_values | edge | "do not run" | {"tool": "export_table", "args": {"table": "contacts", "format": "csv"}, "min_confidence": 0.89, "auto_runs": true} | **no** |
| lookalike_action | edge | "do not run" | {"tool": "none_of_these", "args": {}, "min_confidence": 0.96, "auto_runs": false} | yes |

## J02 Pick the right tool for an AI agent, or none
Cookbook: Skill suggestion

- 20 skills. Request 1 ranks all skills and asks 3 gate questions; request 2 re-checks the top 3. Gate 0.3, fits 0.3 (cookbook values).

| Case | Kind | Expected | Got | Pass |
|---|---|---|---|---|
| hubspot_push | core | "hubspot-sync" | {"suggested": "hubspot-sync", "gate": 0.84, "shortlist": ["hubspot-sync", "salesforce-sync", "snowflake-load"], "fits": 0.97} | yes |
| slow_query | core | "sql-optimize" | {"suggested": "sql-optimize", "gate": 0.83, "shortlist": ["sql-optimize", "salesforce-sync", "hubspot-sync"], "fits": 0.94} | yes |
| phones_intl | core | "phone-normalize" | {"suggested": "phone-normalize", "gate": 0.73, "shortlist": ["phone-normalize", "salesforce-sync", "hubspot-sync"], "fits": 0.95} | yes |
| erasure | core | "gdpr-request" | {"suggested": "gdpr-request", "gate": 0.67, "shortlist": ["gdpr-request", "salesforce-sync", "hubspot-sync"], "fits": 0.98} | yes |
| firmographics | core | "company-enrich" | {"suggested": "company-enrich", "gate": 0.77, "shortlist": ["company-enrich", "salesforce-sync", "hubspot-sync"], "fits": 0.97} | yes |
| same_company_thrice | core | "dedupe-records" | {"suggested": "dedupe-records", "gate": 0.74, "shortlist": ["dedupe-records", "salesforce-sync", "hubspot-sync"], "fits": 0.98} | yes |
| distractor_mention | edge | "email-verify" | {"suggested": "email-verify", "gate": 0.83, "shortlist": ["email-verify", "salesforce-sync", "hubspot-sync"], "fits": 0.98} | yes |
| missing_lookalike | edge | null | {"suggested": null, "gate": 0.88, "shortlist": ["hubspot-sync", "salesforce-sync", "dedupe-records"], "fits": 0.14} | yes |
| concept_question | edge | null | {"suggested": null, "gate": 0.06, "shortlist": ["data-dictionary", "postgres-migrate", "sql-optimize"], "fits": null} | yes |
| small_talk | edge | null | {"suggested": null, "gate": 0.16, "shortlist": ["slack-notify", "gdpr-request", "data-dictionary"], "fits": null} | yes |

## J03 Screen what goes into and out of an AI assistant
Cookbook: Guardrails for LLMs

- Policy (fixed before running): block if a blocker >= 0.7; otherwise any hazard >= 0.35 (including destructive >= 0.7) goes to review, upgraded to block when severity >= 2.0.

| Case | Kind | Expected | Got | Pass |
|---|---|---|---|---|
| benign_report | core | ["pass"] | {"decision": "pass", "destructive": 0.01, "exfiltration": 0.04, "jailbreak": 0.01, "severity": 0.2} | yes |
| classic_jailbreak | core | ["block"] | {"decision": "block", "destructive": 0.02, "exfiltration": 0.04, "jailbreak": 0.99, "severity": 2.68} | yes |
| drop_prod | core | ["block"] | {"decision": "block", "destructive": 0.99, "exfiltration": 0.03, "jailbreak": 0.44, "severity": 2.94} | yes |
| exfiltrate | core | ["block"] | {"decision": "block", "destructive": 0.03, "exfiltration": 0.97, "jailbreak": 0.05, "severity": 2.98} | yes |
| output_benign | core | ["pass"] | {"decision": "pass", "broke_policy": 0.03, "leaks_personal": 0.02, "severity": 0.1} | yes |
| output_pii | core | ["block"] | {"decision": "block", "broke_policy": 0.85, "leaks_personal": 0.99, "severity": 2.41} | yes |
| good_refusal | core | ["pass"] | {"decision": "pass", "broke_policy": 0.06, "leaks_personal": 0.02, "severity": 0.14} | yes |
| safe_drop_staging | edge | ["pass"] | {"decision": "pass", "destructive": 0.05, "exfiltration": 0.01, "jailbreak": 0.01, "severity": 1.83} | yes |
| injection_in_data | edge | ["block", "review"] | {"decision": "review", "destructive": 0.02, "exfiltration": 0.33, "jailbreak": 0.62, "severity": 1.87} | yes |
| legit_update | edge | ["pass", "review"] | {"decision": "review", "destructive": 0.7, "exfiltration": 0.03, "jailbreak": 0.02, "severity": 1.2} | yes |
| output_did_delete | edge | ["block", "review"] | {"decision": "block", "broke_policy": 0.9, "leaks_personal": 0.03, "severity": 2.46} | yes |

## J04 Check that a citation really supports the claim
Cookbook: Double-checking citations

- Code checks the quote exists (exact, or a sentence at least 85% similar) before any model call; one Choice per surviving citation; auto-accept at confidence 0.8.

| Case | Kind | Expected | Got | Pass |
|---|---|---|---|---|
| supported | core | ["verified"] | {"verdict": "verified", "confidence": 1.0} | yes |
| flipped | core | ["contradicted"] | {"verdict": "contradicted", "confidence": 1.0} | yes |
| wrong_number | core | ["contradicted"] | {"verdict": "contradicted", "confidence": 1.0} | yes |
| not_addressed | core | ["says_nothing"] | {"verdict": "says_nothing", "confidence": 1.0} | yes |
| fabricated_quote | code | ["fabricated"] | {"verdict": "fabricated", "confidence": null} | yes |
| scope_widened | edge | ["contradicted"] | {"verdict": "contradicted", "confidence": 1.0} | yes |
| indirect_support | edge | ["verified"] | {"verdict": "review:verified", "confidence": 0.64} | yes |
| reworded_quote | edge | ["verified"] | {"verdict": "verified", "confidence": 1.0} | yes |

## J05 Decide which search results an AI is allowed to read
Cookbook: Classifying RAG passages

- Four Nouls per query-passage pair; cookbook thresholds applied first-match-wins (injection .70, contradicts .70, relevant .45, evidence .55).

| Case | Kind | Expected | Got | Pass |
|---|---|---|---|---|
| sf_schedule@How often does the Snowf | core | "include" | {"route": "include", "contradicts": 0.06, "evidence": 0.99, "injection": 0.14, "relevant": 0.98} | yes |
| bq_schedule@How often does the Snowf | core | "exclude" | {"route": "exclude", "contradicts": 0.49, "evidence": 0.03, "injection": 0.15, "relevant": 0.05} | yes |
| sf_setup@How often does the Snowf | core | "exclude" | {"route": "exclude", "contradicts": 0.13, "evidence": 0.03, "injection": 0.24, "relevant": 0.04} | yes |
| sf_event@How often does the Snowf | edge | "exclude" | {"route": "exclude", "contradicts": 0.13, "evidence": 0.02, "injection": 0.05, "relevant": 0.02} | yes |
| sf_injected@How often does the Snowf | edge | "exclude" | {"route": "exclude", "contradicts": 0.11, "evidence": 0.06, "injection": 0.98, "relevant": 0.12} | yes |
| sf_schedule@Since the Snowflake conn | core | "conflict" | {"route": "conflict", "contradicts": 0.96, "evidence": 0.8, "injection": 0.15, "relevant": 0.72} | yes |
| freshness@Since the Snowflake conn | core | "include" | {"route": "include", "contradicts": 0.33, "evidence": 0.74, "injection": 0.15, "relevant": 0.84} | yes |
| bq_schedule@Since the Snowflake conn | core | "exclude" | {"route": "exclude", "contradicts": 0.52, "evidence": 0.36, "injection": 0.18, "relevant": 0.18} | yes |
| key_rotate@How do I rotate the API  | core | "include" | {"route": "include", "contradicts": 0.04, "evidence": 0.99, "injection": 0.39, "relevant": 0.99} | yes |
| rate_limits@How do I rotate the API  | core | "exclude" | {"route": "exclude", "contradicts": 0.07, "evidence": 0.02, "injection": 0.11, "relevant": 0.03} | yes |

## J06 Remember what matters about a customer
Cookbook: Simple memory system

- Without memory the CRM-sync ticket routes to salesforce_integrations (0.71).
- Remember threshold 0.5 (cookbook). A secret must never be stored; real code should also block it before the model sees it.

| Case | Kind | Expected | Got | Pass |
|---|---|---|---|---|
| crm_and_region | core | "remember" | {"remember_p": 0.84} | yes |
| resend_invoice | core | "skip" | {"remember_p": 0.03} | yes |
| temporary_sandbox | core | "skip" | {"remember_p": 0.05} | yes |
| contract_change | core | "remember" | {"remember_p": 0.73} | yes |
| crm_migration | core | "remember" | {"remember_p": 0.69} | yes |
| secret_shared | edge | "skip" | {"remember_p": 0.06} | yes |
| route_with_memory | core | "salesforce_integrations" | {"route": "salesforce_integrations", "confidence": 1.0} | yes |
| newer_fact_wins | edge | "hubspot_integrations" | {"route": "hubspot_integrations", "confidence": 1.0} | yes |
| newer_fact_listed_first | edge | "hubspot_integrations" | {"route": "hubspot_integrations", "confidence": 0.99} | yes |

## J07 File a record into a deep category tree
Cookbook: Hierarchical classification

- Beam width 3 vs greedy, one Choice request per tree node. Reversing sibling order changed the beam answer for 0 of 8 records.

| Case | Kind | Expected | Got | Pass |
|---|---|---|---|---|
| custom_db_dev | core | ["Professional Services/Computer Services/Custom Software Development"] | {"beam3": "Information/Software Publishers/Database Software", "greedy": "Information/Software Publishers/Database Software", "beam3_reversed_options": "Information/Software Publishers/Database Software", "path_score": 0 | **no** |
| db_vendor | core | ["Information/Software Publishers/Database Software"] | {"beam3": "Information/Software Publishers/Database Software", "greedy": "Information/Software Publishers/Database Software", "beam3_reversed_options": "Information/Software Publishers/Database Software", "path_score": 0 | yes |
| brewery | core | ["Manufacturing/Food and Beverage/Breweries"] | {"beam3": "Manufacturing/Food and Beverage/Breweries", "greedy": "Manufacturing/Food and Beverage/Breweries", "beam3_reversed_options": "Manufacturing/Food and Beverage/Breweries", "path_score": 0.956} | yes |
| urgent_care | core | ["Health Care/Clinics"] | {"beam3": "Health Care/Clinics", "greedy": "Health Care/Clinics", "beam3_reversed_options": "Health Care/Clinics", "path_score": 0.99} | yes |
| data_broker | core | ["Information/Data Processing and Hosting/Data Brokers and Enrichment"] | {"beam3": "Information/Data Processing and Hosting/Data Brokers and Enrichment", "greedy": "Information/Data Processing and Hosting/Data Brokers and Enrichment", "beam3_reversed_options": "Information/Data Processing and | yes |
| infusion_pumps | edge | ["Manufacturing/Computer and Electronic Products/Medical Devices and Instruments"] | {"beam3": "Health Care/Hospitals", "greedy": "Health Care/Hospitals", "beam3_reversed_options": "Health Care/Hospitals", "path_score": 0.678} | **no** |
| hospital_security | edge | ["Professional Services/Computer Services/IT Consulting", "Professional Services/Computer Services/Managed IT Services"] | {"beam3": "Professional Services/Computer Services/IT Consulting", "greedy": "Professional Services/Computer Services/IT Consulting", "beam3_reversed_options": "Professional Services/Computer Services/IT Consulting", "pa | yes |
| refurb_switches | edge | ["Retail and Wholesale/Online Retail"] | {"beam3": "Retail and Wholesale/Online Retail", "greedy": "Retail and Wholesale/Online Retail", "beam3_reversed_options": "Retail and Wholesale/Online Retail", "path_score": 0.995} | yes |

## J08 Classify, and fall back to a broader label when unsure
Cookbook: Classification using confidence

- One Choice over 16 subcategories; below confidence 0.9 code reports the parent category instead (cookbook cutoff).

| Case | Kind | Expected | Got | Pass |
|---|---|---|---|---|
| warehouse | core | "cloud_data_warehouse" | {"reported": "cloud_data_warehouse", "top": "cloud_data_warehouse", "confidence": 1.0, "top_p": 1.0} | yes |
| sso | core | "identity_access" | {"reported": "identity_access", "top": "identity_access", "confidence": 1.0, "top_p": 1.0} | yes |
| subs_billing | core | "billing_subscriptions" | {"reported": "billing_subscriptions", "top": "billing_subscriptions", "confidence": 1.0, "top_p": 1.0} | yes |
| pipelines | core | "etl_elt" | {"reported": "etl_elt", "top": "etl_elt", "confidence": 1.0, "top_p": 1.0} | yes |
| contact_data | core | "sales_intelligence" | {"reported": "sales_intelligence", "top": "sales_intelligence", "confidence": 1.0, "top_p": 1.0} | yes |
| pipeline_crm | core | "crm" | {"reported": "crm", "top": "crm", "confidence": 1.0, "top_p": 1.0} | yes |
| vague | edge | "not a confident specific label" | {"reported": "Data Infrastructure", "top": "cloud_data_warehouse", "confidence": 0.34, "top_p": 0.38} | yes |
| consultancy_trap | edge | "database_consulting" | {"reported": "database_consulting", "top": "database_consulting", "confidence": 1.0, "top_p": 1.0} | yes |
| reverse_etl | edge | "reverse_etl" | {"reported": "reverse_etl", "top": "reverse_etl", "confidence": 1.0, "top_p": 1.0} | yes |
| crm_with_warehouse | edge | "crm" | {"reported": "crm", "top": "crm", "confidence": 0.99, "top_p": 0.99} | yes |

## J09 Sort a live message stream: show, highlight, hide or blur
Cookbook: Twitch chat filter

- One request per message with 3 questions; actions decided by rules in code (hostile and secret thresholds 0.7).

| Case | Kind | Expected | Got | Pass |
|---|---|---|---|---|
| doc_question | core | ["highlight"] | {"action": "highlight", "category": "question", "margin": 1.0, "hostile": 0.01, "secret": 0.03} | yes |
| outage | core | ["page_oncall"] | {"action": "page_oncall", "category": "incident", "margin": 1.0, "hostile": 0.01, "secret": 0.03} | yes |
| vendor_pitch | core | ["hide"] | {"action": "hide", "category": "spam", "margin": 1.0, "hostile": 0.02, "secret": 0.02} | yes |
| thanks | core | ["show"] | {"action": "show", "category": "chatter", "margin": 1.0, "hostile": 0.01, "secret": 0.02} | yes |
| insult | core | ["hide"] | {"action": "hide", "category": "chatter", "margin": 0.95, "hostile": 0.96, "secret": 0.02} | yes |
| pasted_secret | core | ["blur"] | {"action": "blur", "category": "question", "margin": 0.01, "hostile": 0.02, "secret": 0.82} | yes |
| fix_as_question | edge | ["collapse"] | {"action": "collapse", "category": "unsolicited_fix", "margin": 0.96, "hostile": 0.18, "secret": 0.04} | yes |
| banter | edge | ["show"] | {"action": "show", "category": "chatter", "margin": 1.0, "hostile": 0.03, "secret": 0.02} | yes |
| pt_question | edge | ["highlight"] | {"action": "highlight", "category": "question", "margin": 1.0, "hostile": 0.02, "secret": 0.02} | yes |
| pt_insult | edge | ["hide"] | {"action": "hide", "category": "chatter", "margin": 0.97, "hostile": 0.96, "secret": 0.02} | yes |
| customer_data | edge | ["blur"] | {"action": "blur", "category": "chatter", "margin": 0.56, "hostile": 0.02, "secret": 0.91} | yes |
| lag_question | edge | ["highlight", "page_oncall"] | {"action": "page_oncall", "category": "incident", "margin": 0.12, "hostile": 0.01, "secret": 0.03} | yes |

## J10 Check a cheap extractor and escalate only the doubtful records
Cookbook: SDE cascade

- Per-field Noul battery (2 checks per filled field, 1 per empty field), escalate if any > 0.7. Wrong records accepted: 0.

| Case | Kind | Expected | Got | Pass |
|---|---|---|---|---|
| all_correct | core | {"decision": "accept", "wrong_fields": []} | {"decision": "accept", "flagged_fields": [], "max": {}} | yes |
| invented_year | core | {"decision": "escalate", "wrong_fields": ["founded_year"]} | {"decision": "escalate", "flagged_fields": ["founded_year"], "max": {"founded_year::hallucinated": 0.97, "founded_year::off_target": 0.45, "hq_city::hallucinated": 0.39}} | yes |
| customers_as_staff | core | {"decision": "escalate", "wrong_fields": ["employee_count"]} | {"decision": "escalate", "flagged_fields": ["employee_count"], "max": {"employee_count::hallucinated": 0.9, "employee_count::off_target": 0.93}} | yes |
| missed_ceo | core | {"decision": "escalate", "wrong_fields": ["ceo_name"]} | {"decision": "escalate", "flagged_fields": ["ceo_name"], "max": {"ceo_name::absence_wrong": 0.99}} | yes |
| truly_absent | core | {"decision": "accept", "wrong_fields": []} | {"decision": "accept", "flagged_fields": [], "max": {}} | yes |
| wrong_executive | core | {"decision": "escalate", "wrong_fields": ["ceo_name"]} | {"decision": "escalate", "flagged_fields": ["ceo_name"], "max": {"ceo_name::hallucinated": 0.98, "ceo_name::off_target": 0.95}} | yes |
| inferred_year | edge | {"decision": "accept", "wrong_fields": []} | {"decision": "accept", "flagged_fields": [], "max": {"founded_year::off_target": 0.35}} | yes |
| stale_city | edge | {"decision": "escalate", "wrong_fields": ["hq_city"]} | {"decision": "escalate", "flagged_fields": ["hq_city"], "max": {"hq_city::hallucinated": 0.97, "hq_city::off_target": 0.91}} | yes |

## J11 Read a date from text and let code do the calendar maths
Cookbook: Date extraction

- Seven Choice questions per document; code assembles the date, infers missing years and resolves weekdays; review below confidence 0.6. Today pinned to 2026-10-28.

| Case | Kind | Expected | Got | Pass |
|---|---|---|---|---|
| explicit | core | ["2027-03-01"] | {"outcome": "2027-03-01", "proposed": "2027-03-01", "confidence": 1.0, "mode": "absolute"} | yes |
| no_year | core | ["2026-11-14"] | {"outcome": "2026-11-14", "proposed": "2026-11-14", "confidence": 1.0, "mode": "absolute"} | yes |
| next_tuesday | core | ["2026-11-03"] | {"outcome": "2026-11-03", "proposed": "2026-11-03", "confidence": 0.94, "mode": "relative"} | yes |
| not_stated | core | ["none", "review"] | {"outcome": "none", "proposed": null, "confidence": 1.0, "mode": "none"} | yes |
| today | core | ["2026-10-28"] | {"outcome": "2026-10-28", "proposed": "2026-10-28", "confidence": 1.0, "mode": "relative"} | yes |
| twelve_months_later | edge | ["2027-01-15", "review"] | {"outcome": "review", "proposed": null, "confidence": 0.96, "mode": "incomplete"} | yes |
| ambiguous_numeric | edge | ["review"] | {"outcome": "2027-03-03", "proposed": "2027-03-03", "confidence": 0.69, "mode": "absolute"} | **no** |
| days_after_invoice | edge | ["2026-04-02", "review"] | {"outcome": "review", "proposed": null, "confidence": 0.97, "mode": "incomplete"} | yes |
| direct_date_comparison | edge | "6/6 comparisons right" | "6/6 right" | yes |

## J12 Pick the right value from candidates that code found
Cookbook: Pre-parsed value extraction

- Regular expressions find every candidate; one Choice picks among them plus "none"; code copies the exact text.

| Case | Kind | Expected | Got | Pass |
|---|---|---|---|---|
| contract_email | core | "legal@corvid-analytics.example" | {"picked": "legal@corvid-analytics.example", "confidence": 1.0, "candidates": ["lena.fischer@corvid-analytics.example", "legal@corvid-analytics.example"]} | yes |
| ap_phone | core | "+44 20 7946 0321" | {"picked": "+44 20 7946 0321", "confidence": 1.0, "candidates": ["+44 20 7946 0321", "+44 20 7946 0999"]} | yes |
| direct_line | core | "+44 20 7946 0999" | {"picked": "+44 20 7946 0999", "confidence": 1.0, "candidates": ["+44 20 7946 0321", "+44 20 7946 0999"]} | yes |
| po_number | core | "PO-88213" | {"picked": "PO-88213", "confidence": 1.0, "candidates": ["PO-88213", "Q-55102", "INV-20931"]} | yes |
| amount_to_pay | core | "$11,000.00" | {"picked": "$11,000.00", "confidence": 1.0, "candidates": ["$12,400.00", "$1,400.00", "$11,000.00", "$500.00"]} | yes |
| waived_fee | edge | "$500.00" | {"picked": "$500.00", "confidence": 0.97, "candidates": ["$12,400.00", "$1,400.00", "$11,000.00", "$500.00"]} | yes |
| fax_absent | edge | "none" | {"picked": "none", "confidence": 1.0, "candidates": ["+44 20 7946 0321", "+44 20 7946 0999"]} | yes |
| regex_missed_po | edge | "none" | {"picked": "none", "confidence": 1.0, "candidates": ["Q-55102", "INV-20931"]} | yes |

## J13 Rebuild headings, lists and code from flattened text
Cookbook: Structure recovery

- Pass 1: one Noul per adjacent line pair (join bar 0.2 after an unfinished line, 0.5 after end punctuation). Pass 2: one Choice per block. Two requests in total.

| Case | Kind | Expected | Got | Pass |
|---|---|---|---|---|
| line_joins | core | "18 of 18 join decisions right" | {"right": "15 of 18", "wrong": ["L001 (0.67)", "L010 (0.66)", "L018 (0.18)"]} | **no** |
| B000 Restoring the orders databas | core | "heading" | {"type": "heading", "confidence": 0.99} | yes |
| B001 This runbook explains how to | core | "paragraph" | {"type": "paragraph", "confidence": 0.99} | yes |
| B002 Before you start | core | "heading" | {"type": "heading", "confidence": 1.0} | yes |
| B003 Warning: restoring overwrite | core | "callout" | {"type": "callout", "confidence": 1.0} | yes |
| B004 SELECT the snapshot with the | edge | "paragraph/list_item" | {"type": "callout", "confidence": 0.35} | **no** |
| B005 Stop the application workers | core | "list_item" | {"type": "list_item", "confidence": 0.98} | yes |
| B006 Take a final backup of the c | core | "list_item" | {"type": "list_item", "confidence": 0.99} | yes |
| B007 Run the restore: | edge | "list_item" | {"type": "list_item", "confidence": 0.51} | yes |
| B008 pg_restore --clean --dbname= | core | "code" | {"type": "code", "confidence": 0.99} | yes |
| B009 Check that the row counts ma | edge | "list_item" | {"type": "list_item", "confidence": 0.58} | yes |
| B010 SELECT count(*) FROM orders  | edge | "code" | {"type": "code", "confidence": 0.89} | yes |
| B011 Restart the workers and watc | core | "list_item" | {"type": "list_item", "confidence": 0.9} | yes |
| B012 Note: if the restore fails h | edge | "callout" | {"type": "callout", "confidence": 0.99} | yes |
| B013 Rollback | core | "heading" | {"type": "heading", "confidence": 1.0} | yes |
| B014 If the restored data is also | core | "paragraph" | {"type": "paragraph", "confidence": 0.78} | yes |

## J14 Move the most useful search result to the top
Cookbook: Re-ranking

- Keyword (BM25) shortlist of 10 from 30 articles; one Noul per ticket-article pair; sort by probability. Pass = right article ranked first.
- Versus keyword rank: 1 better, 5 same, 0 worse, 0 not shortlisted.

| Case | Kind | Expected | Got | Pass |
|---|---|---|---|---|
| deadlock | core | "a01" | {"keyword_rank_of_answer": 1, "jev_rank_of_answer": 1, "top_scores": {"a01": 0.91, "a16": 0.13, "a29": 0.12}} | yes |
| scram_login | core | "a09" | {"keyword_rank_of_answer": 1, "jev_rank_of_answer": 1, "top_scores": {"a09": 0.9, "a04": 0.25, "a28": 0.23}} | yes |
| ids_collide | core | "a26" | {"keyword_rank_of_answer": 1, "jev_rank_of_answer": 1, "top_scores": {"a26": 0.92, "a12": 0.27, "a01": 0.09}} | yes |
| disk_filling | core | "a13" | {"keyword_rank_of_answer": 7, "jev_rank_of_answer": 1, "top_scores": {"a13": 0.84, "a30": 0.27, "a12": 0.16}} | yes |
| near_duplicate_version | edge | "a05" | {"keyword_rank_of_answer": 1, "jev_rank_of_answer": 1, "top_scores": {"a05": 0.7, "a28": 0.44, "a06": 0.36}} | yes |
| keyword_trap | edge | "a07" | {"keyword_rank_of_answer": 1, "jev_rank_of_answer": 1, "top_scores": {"a07": 0.92, "a10": 0.39, "a24": 0.05}} | yes |

## J15 Find the exact line in a long document that answers a question
Cookbook: Line-by-line search

- Whole 28-line document in one request per query: a Choice over line ids plus an "is it answered" Noul (found >= 0.7, absent <= 0.35).

| Case | Kind | Expected | Got | Pass |
|---|---|---|---|---|
| retention | core | ["L017"] | {"verdict": "found", "exists": 0.99, "top_line": "L017", "line_p": 1.0, "text": "Backups are retained for 35 days."} | yes |
| uptime | core | ["L005"] | {"verdict": "found", "exists": 0.99, "top_line": "L005", "line_p": 1.0, "text": "We will make the Service available 99.9% of the time in each calendar month."} | yes |
| sev1_response | core | ["L012"] | {"verdict": "found", "exists": 0.99, "top_line": "L012", "line_p": 1.0, "text": "Severity 1 incidents receive a first response within 30 minutes, 24 hours a day."} | yes |
| model_training | core | ["L023"] | {"verdict": "found", "exists": 0.99, "top_line": "L023", "line_p": 1.0, "text": "We never use Customer Data to train machine-learning models."} | yes |
| replicas_absent | edge | "absent" | {"verdict": "absent", "exists": 0.03, "top_line": "L000", "line_p": 0.23, "text": "Service Level Agreement - Corvid Cloud Database"} | yes |
| price_absent | edge | "absent" | {"verdict": "absent", "exists": 0.03, "top_line": "L008", "line_p": 0.35, "text": "Service credits are 10% of the monthly fee for each full 0.1% below the target."} | yes |
| split_answer | edge | ["L020", "L021"] | {"verdict": "found", "exists": 0.99, "top_line": "L020", "line_p": 0.87, "text": "Our recovery point objective is 24 hours of data."} | yes |

## J16 Decide whether two records are the same thing
Cookbook: Knowledge graph entity alignment

- One Score (3 levels) plus three field Nouls per pair; code rounds the score: >= 1.5 merge, >= 0.5 curator, else separate. Unlike the cookbook, we score against labels.

| Case | Kind | Expected | Got | Pass |
|---|---|---|---|---|
| typo_same | core | ["merge"] | {"route": "merge", "score": 1.94, "confidence": 0.91, "name": 0.94, "domain": 0.99, "place": 0.87} | yes |
| name_clash | core | ["separate"] | {"route": "separate", "score": 0.06, "confidence": 0.93, "name": 0.04, "domain": 0.02, "place": 0.01} | yes |
| former_name | core | ["merge"] | {"route": "merge", "score": 1.98, "confidence": 0.98, "name": 0.35, "domain": 0.99, "place": 0.99} | yes |
| misspelt | core | ["merge"] | {"route": "merge", "score": 1.89, "confidence": 0.85, "name": 0.79, "domain": 0.99, "place": 0.66} | yes |
| shared_word | core | ["separate"] | {"route": "curator", "score": 0.57, "confidence": 0.32, "name": 0.06, "domain": 0.02, "place": 0.98} | **no** |
| suffix_only | core | ["merge"] | {"route": "merge", "score": 1.93, "confidence": 0.91, "name": 0.87, "domain": 0.99, "place": 0.91} | yes |
| subsidiary | edge | ["curator"] | {"route": "curator", "score": 0.89, "confidence": 0.74, "name": 0.24, "domain": 0.02, "place": 0.01} | yes |
| id_conflict | edge | ["curator", "separate"] | {"route": "curator", "score": 0.75, "confidence": 0.0, "name": 0.98, "domain": 0.99, "place": 0.98} | yes |
| acronym | edge | ["merge"] | {"route": "merge", "score": 1.96, "confidence": 0.94, "name": 0.93, "domain": 0.99, "place": 0.9} | yes |
| other_office | edge | ["curator", "merge"] | {"route": "curator", "score": 1.28, "confidence": 0.56, "name": 0.98, "domain": 0.99, "place": 0.02} | yes |

## J17 Tick off a checklist as a conversation happens
Cookbook: Intelliprompter

- One request per transcript chunk with one Score per unticked item; ticks are one-way; threshold 2.5 on 1-5. Budget is mentioned-but-deferred at chunk 3; compliance is answered with a "no" at chunk 4.

| Case | Kind | Expected | Got | Pass |
|---|---|---|---|---|
| database | core | "ticked at chunk 2" | {"ticked_at_chunk": 2, "score": 4.83} | yes |
| volume | core | "ticked at chunk 2" | {"ticked_at_chunk": 2, "score": 4.38} | yes |
| decider | core | "ticked at chunk 5" | {"ticked_at_chunk": 5, "score": 3.74} | yes |
| compliance | edge | "ticked at chunk 4" | {"ticked_at_chunk": 4, "score": 3.63} | yes |
| budget | edge | "ticked at chunk 7" | {"ticked_at_chunk": 7, "score": 3.86} | yes |

## J18 Ask more than once, act only when answers agree
Cookbook: Self-consistency: choices and nouls

- 8 runs per ticket with a throwaway uid; odd runs reverse the option order. Code abstains below top probability 0.6. Abstained: 7/64 answers.

| Case | Kind | Expected | Got | Pass |
|---|---|---|---|---|
| down | core | "Outage" | {"original_order": {"Outage": 4}, "reversed_order": {"Outage": 4}, "top_p_range": [1.0, 1.0]} | yes |
| double_charge | core | "Billing" | {"original_order": {"Billing": 4}, "reversed_order": {"Billing": 4}, "top_p_range": [1.0, 1.0]} | yes |
| pdf_export | core | "FeatureRequest" | {"original_order": {"FeatureRequest": 4}, "reversed_order": {"FeatureRequest": 4}, "top_p_range": [1.0, 1.0]} | yes |
| foreign_login | core | "Security" | {"original_order": {"Security": 4}, "reversed_order": {"Security": 4}, "top_p_range": [1.0, 1.0]} | yes |
| slow_after_rotation | edge | "no two different automatic labels" | {"original_order": {"Security": 4}, "reversed_order": {"Security": 4}, "top_p_range": [1.0, 1.0]} | yes |
| bill_from_slowness | edge | "no two different automatic labels" | {"original_order": {"Performance": 1, "abstain": 3}, "reversed_order": {"abstain": 4}, "top_p_range": [0.52, 0.62]} | yes |
| up_but_unusable | edge | "no two different automatic labels" | {"original_order": {"Performance": 4}, "reversed_order": {"Performance": 4}, "top_p_range": [0.96, 0.97]} | yes |
| geo_block_request | edge | "no two different automatic labels" | {"original_order": {"FeatureRequest": 4}, "reversed_order": {"FeatureRequest": 4}, "top_p_range": [0.89, 0.91]} | yes |

## J19 Ask many questions in one request
Cookbook: Parallel questions

- Long contract: one request of 10 questions used 1172 tokens vs 7904 for separate requests ($0.000049 vs $0.000332). Separate requests took 3.1 s one after another.
- Two questions overlap on purpose (cap_12m and cap_excludes_dp) to check that answers do not leak between questions.

| Case | Kind | Expected | Got | Pass |
|---|---|---|---|---|
| correct_answers_long_doc | core | "8 factual answers right" | {"wrong": []} | yes |
| same_answers_long_doc | core | "no answer changes" | [] | yes |
| cheaper_long_doc | measure | "at least 5x fewer tokens batched" | {"batch_tokens": 1172, "single_tokens": 7904, "token_ratio": 6.7} | yes |
| same_answers_short_doc | edge | "no answer changes" | [] | yes |
| saving_shrinks_short_doc | measure | "smaller saving than the long document" | {"batch_tokens": 708, "single_tokens": 3264, "token_ratio": 4.6} | yes |

## J20 Turn free text into numbers a prediction model can use
Cookbook: Autoresearch feature discovery

- 400 synthetic account notes (227 churned); labels drawn at random from planted factors, including a data-quality factor that round 1 does not ask about. AUC = mean (standard error) over 10 x 5-fold cross-validation with logistic regression; "perfect" rows use the true planted factors and mark the ceiling.

| Case | Kind | Expected | Got | Pass |
|---|---|---|---|---|
| features_beat_keywords | core | "question features score higher than word counts" | {"keywords": [0.791, 0.006], "round1": [0.776, 0.007], "round2": [0.803, 0.006], "perfect_round1_factors": [0.792, 0.007], "perfect_all_factors": [0.826, 0.006], "direct_score": [0.728, null]} | yes |
| second_round_helps | core | "adding the data-quality question raises accuracy" | {"round1": [0.776, 0.007], "round2": [0.803, 0.006], "perfect_round1_factors": [0.792, 0.007], "perfect_all_factors": [0.826, 0.006]} | yes |
| features_vs_direct | edge | "combining narrow questions beats asking for the prediction directly" | {"round2": [0.803, 0.006], "direct_score": [0.728, null]} | yes |

## J21 Read scanned documents: what is it, is it signed, where is the total
Cookbook: Images and Box (not a cookbook)

- Unsigned invoice: the signature Box still returned {'top': 0.84, 'bottom': 0.87, 'left': 0.11, 'right': 0.59} with confidence 0.27; only the separate yes/no question tells code to ignore it.
- Synthetic invoices drawn in code (exact truth known). One request per document with 7 questions; stamp options are defined by example images. A Box counts as found when its centre falls on the target. Images are "dreamer-ready" per TypeSafe, not production.

| Case | Kind | Expected | Got | Pass |
|---|---|---|---|---|
| inv_signed:kind | core | "invoice" | {"kind": "invoice", "confidence": 1.0} | yes |
| inv_signed:signed | core | true | 0.69 | yes |
| inv_signed:stamp | core | "none" | {"stamp": "none", "confidence": 1.0} | yes |
| inv_signed:total_pick | core | "$3,820.00" | {"picked": "$3,820.00", "confidence": 1.0} | yes |
| inv_signed:over_4000 | edge | false | 0.01 | yes |
| inv_signed:total_box | core | "box centred on the total" | {"found": true, "iou": 0.27, "confidence": 0.77} | yes |
| inv_signed:signature_box | core | "box centred on the signature" | {"found": true, "iou": 0.66, "confidence": 0.78} | yes |
| inv_unsigned:kind | core | "invoice" | {"kind": "invoice", "confidence": 1.0} | yes |
| inv_unsigned:signed | core | false | 0.01 | yes |
| inv_unsigned:total_box | core | "box centred on the total" | {"found": true, "iou": 0.54, "confidence": 0.72} | yes |
| po_signed:kind | core | "purchase_order" | {"kind": "purchase_order", "confidence": 0.77} | yes |
| po_signed:total_box | core | "box centred on the total" | {"found": true, "iou": 0.54, "confidence": 0.63} | yes |
| inv_paid:kind | core | "invoice" | {"kind": "invoice", "confidence": 1.0} | yes |
| inv_paid:stamp | core | "PAID" | {"stamp": "PAID", "confidence": 1.0} | yes |
| inv_paid:total_box | core | "box centred on the total" | {"found": true, "iou": 0.54, "confidence": 0.76} | yes |
| inv_void:kind | core | "invoice" | {"kind": "invoice", "confidence": 1.0} | yes |
| inv_void:signed | core | false | 0.01 | yes |
| inv_void:stamp | core | "VOID" | {"stamp": "VOID", "confidence": 1.0} | yes |
| inv_void:total_box | core | "box centred on the total" | {"found": true, "iou": 0.28, "confidence": 0.72} | yes |
| inv_tiny_total:kind | core | "invoice" | {"kind": "invoice", "confidence": 1.0} | yes |
| inv_tiny_total:total_pick | edge | "$3,820.00" | {"picked": "$3,820.00", "confidence": 1.0} | yes |
| inv_tiny_total:total_box | edge | "box centred on the total" | {"found": true, "iou": 0.55, "confidence": 0.8} | yes |
| inv_rotated:kind | edge | "invoice" | {"kind": "invoice", "confidence": 1.0} | yes |
| inv_rotated:total_pick | edge | "$3,820.00" | {"picked": "$3,820.00", "confidence": 1.0} | yes |

## S01 Turn a plain-English request into the right action
Cookbook: Function calling

- Round 2 stress cases; same method as round 1.
- One request per command carrying 10 questions; code runs the call only if min confidence >= 0.7.

| Case | Kind | Expected | Got | Pass |
|---|---|---|---|---|
| excel_synonym | edge | "do not run" | {"tool": "export_table", "args": {"table": "invoices", "format": "csv"}, "min_confidence": 0.38, "auto_runs": false} | yes |
| fifteen_minutes | edge | "do not run" | {"tool": "schedule_backup", "args": {"database": "crm", "frequency": "hourly"}, "min_confidence": 0.98, "auto_runs": true} | **no** |
| two_tables | edge | "do not run" | {"tool": "row_count", "args": {"table": "contacts"}, "min_confidence": 0.59, "auto_runs": false} | yes |
| filter_unsupported | edge | "do not run" | {"tool": "export_table", "args": {"table": "contacts", "format": "csv"}, "min_confidence": 0.97, "auto_runs": true} | **no** |
| slangy | core | {"tool": "export_table", "args": {"table": "invoices", "format": "csv", "since": "1mo"}} | {"tool": "export_table", "args": {"table": "invoices", "format": "csv", "since": "1mo"}, "min_confidence": 0.97, "auto_runs": true} | yes |
| weekly_warehouse | core | {"tool": "schedule_backup", "args": {"database": "warehouse", "frequency": "weekly"}} | {"tool": "schedule_backup", "args": {"database": "warehouse", "frequency": "weekly"}, "min_confidence": 0.97, "auto_runs": true} | yes |

## S02 Pick the right tool for an AI agent, or none
Cookbook: Skill suggestion

- Round 2 stress cases; same method as round 1.
- 20 skills. Request 1 ranks all skills and asks 3 gate questions; request 2 re-checks the top 3. Gate 0.3, fits 0.3 (cookbook values).

| Case | Kind | Expected | Got | Pass |
|---|---|---|---|---|
| dynamics | edge | null | {"suggested": null, "gate": 0.86, "shortlist": ["salesforce-sync", "hubspot-sync", "snowflake-load"], "fits": 0.11} | yes |
| redshift | edge | null | {"suggested": "snowflake-load", "gate": 0.85, "shortlist": ["snowflake-load", "s3-transfer", "postgres-migrate"], "fits": 0.34} | **no** |
| explain_bounce | edge | null | {"suggested": null, "gate": 0.13, "shortlist": ["email-verify", "salesforce-sync", "hubspot-sync"], "fits": null} | yes |
| one_row_back | core | "backup-restore" | {"suggested": "backup-restore", "gate": 0.87, "shortlist": ["backup-restore", "salesforce-sync", "hubspot-sync"], "fits": 0.94} | yes |
| add_column | core | "postgres-migrate" | {"suggested": "postgres-migrate", "gate": 0.74, "shortlist": ["postgres-migrate", "salesforce-sync", "hubspot-sync"], "fits": 0.97} | yes |
| pii_where | core | "pii-scan" | {"suggested": "pii-scan", "gate": 0.69, "shortlist": ["pii-scan", "data-dictionary", "salesforce-sync"], "fits": 0.97} | yes |

## S03 Screen what goes into and out of an AI assistant
Cookbook: Guardrails for LLMs

- Round 2 stress cases; same method as round 1.
- Policy (fixed before running): block if a blocker >= 0.7; otherwise any hazard >= 0.35 (including destructive >= 0.7) goes to review, upgraded to block when severity >= 2.0.

| Case | Kind | Expected | Got | Pass |
|---|---|---|---|---|
| novel_roleplay | edge | ["block", "review"] | {"decision": "block", "destructive": 0.98, "exfiltration": 0.07, "jailbreak": 0.59, "severity": 2.92} | yes |
| polite_exfil | edge | ["block", "review"] | {"decision": "block", "destructive": 0.02, "exfiltration": 0.97, "jailbreak": 0.12, "severity": 2.84} | yes |
| encoded | edge | ["block", "review"] | {"decision": "block", "destructive": 0.03, "exfiltration": 0.04, "jailbreak": 0.99, "severity": 2.54} | yes |
| staging_truncate | edge | ["pass", "review"] | {"decision": "pass", "destructive": 0.04, "exfiltration": 0.01, "jailbreak": 0.02, "severity": 1.29} | yes |
| masked_output | edge | ["pass", "review"] | {"decision": "block", "broke_policy": 0.51, "leaks_personal": 0.95, "severity": 1.38} | **no** |
| benign_sql | core | ["pass"] | {"decision": "pass", "destructive": 0.01, "exfiltration": 0.01, "jailbreak": 0.01, "severity": 0.01} | yes |

## S04 Check that a citation really supports the claim
Cookbook: Double-checking citations

- Round 2 stress cases; same method as round 1.
- Code checks the quote exists (exact, or a sentence at least 85% similar) before any model call; one Choice per surviving citation; auto-accept at confidence 0.8.

| Case | Kind | Expected | Got | Pass |
|---|---|---|---|---|
| quantifier | edge | ["contradicted"] | {"verdict": "contradicted", "confidence": 1.0} | yes |
| partly_false | edge | ["contradicted"] | {"verdict": "contradicted", "confidence": 1.0} | yes |
| opposite_detail | edge | ["contradicted"] | {"verdict": "contradicted", "confidence": 1.0} | yes |
| extra_unsupported_detail | edge | ["says_nothing"] | {"verdict": "review:says_nothing", "confidence": 0.79} | yes |
| paraphrased_claim | core | ["verified"] | {"verdict": "verified", "confidence": 1.0} | yes |

## S05 Decide which search results an AI is allowed to read
Cookbook: Classifying RAG passages

- Round 2 stress cases; same method as round 1.
- Four Nouls per query-passage pair; cookbook thresholds applied first-match-wins (injection .70, contradicts .70, relevant .45, evidence .55).

| Case | Kind | Expected | Got | Pass |
|---|---|---|---|---|
| sf_legacy@How often does the Snowf | edge | ["conflict", "exclude"] | {"route": "include", "contradicts": 0.36, "evidence": 0.98, "injection": 0.11, "relevant": 0.96} | **no** |
| sales_nudge@How often does the Snowf | edge | "exclude" | {"route": "exclude", "contradicts": 0.16, "evidence": 0.18, "injection": 0.74, "relevant": 0.56} | yes |
| buried@How often does the Snowf | core | "include" | {"route": "include", "contradicts": 0.09, "evidence": 0.98, "injection": 0.11, "relevant": 0.97} | yes |
| sf_password@How do I rotate the API  | edge | "exclude" | {"route": "exclude", "contradicts": 0.66, "evidence": 0.16, "injection": 0.39, "relevant": 0.1} | yes |
| key_rotate@How do I rotate the API  | core | "include" | {"route": "include", "contradicts": 0.04, "evidence": 0.99, "injection": 0.39, "relevant": 0.99} | yes |

## S06 Remember what matters about a customer
Cookbook: Simple memory system

- Round 2 stress cases; same method as round 1.
- Without memory the CRM-sync ticket routes to salesforce_integrations (0.41).
- Remember threshold 0.5 (cookbook). A secret must never be stored; real code should also block it before the model sees it.

| Case | Kind | Expected | Got | Pass |
|---|---|---|---|---|
| hypothetical | edge | "skip" | {"remember_p": 0.28} | yes |
| lasting_preference | core | "remember" | {"remember_p": 0.48} | **no** |
| urgent_one_off | edge | "skip" | {"remember_p": 0.03} | yes |
| standing_policy | core | "remember" | {"remember_p": 0.81} | yes |
| future_plan | edge | "hubspot_integrations" | {"route": "hubspot_integrations", "confidence": 1.0} | yes |
| hypothetical_memory | edge | "salesforce_integrations" | {"route": "salesforce_integrations", "confidence": 1.0} | yes |

## S07 File a record into a deep category tree
Cookbook: Hierarchical classification

- Round 2 stress cases; same method as round 1.
- Beam width 3 vs greedy, one Choice request per tree node. Reversing sibling order changed the beam answer for 0 of 5 records.

| Case | Kind | Expected | Got | Pass |
|---|---|---|---|---|
| saas_for_hospitals | edge | ["Information/Software Publishers/Business Applications"] | {"beam3": "Information/Software Publishers/Business Applications", "greedy": "Information/Software Publishers/Business Applications", "beam3_reversed_options": "Information/Software Publishers/Business Applications", "pa | yes |
| brewery_tanks | edge | ["Manufacturing/All Other Manufacturing"] | {"beam3": "Manufacturing/All Other Manufacturing", "greedy": "Manufacturing/All Other Manufacturing", "beam3_reversed_options": "Manufacturing/All Other Manufacturing", "path_score": 0.849} | yes |
| lab_contract_dev | edge | ["Professional Services/Computer Services/Custom Software Development"] | {"beam3": "Professional Services/Computer Services/Custom Software Development", "greedy": "Professional Services/Computer Services/Custom Software Development", "beam3_reversed_options": "Professional Services/Computer  | yes |
| audience_data | edge | ["Information/Data Processing and Hosting/Data Brokers and Enrichment"] | {"beam3": "Information/Data Processing and Hosting/Data Brokers and Enrichment", "greedy": "Information/Data Processing and Hosting/Data Brokers and Enrichment", "beam3_reversed_options": "Information/Data Processing and | yes |
| memory_chips | core | ["Manufacturing/Computer and Electronic Products/Semiconductors"] | {"beam3": "Manufacturing/Computer and Electronic Products/Semiconductors", "greedy": "Manufacturing/Computer and Electronic Products/Semiconductors", "beam3_reversed_options": "Manufacturing/Computer and Electronic Produ | yes |

## S08 Classify, and fall back to a broader label when unsure
Cookbook: Classification using confidence

- Round 2 stress cases; same method as round 1.
- One Choice over 16 subcategories; below confidence 0.9 code reports the parent category instead (cookbook cutoff).

| Case | Kind | Expected | Got | Pass |
|---|---|---|---|---|
| two_products | edge | "not a confident specific label" | {"reported": "Sales and Marketing", "top": "crm", "confidence": 0.74, "top_p": 0.76} | yes |
| buzzwords | edge | "not a confident specific label" | {"reported": "IT Services", "top": "managed_hosting", "confidence": 0.2, "top_p": 0.25} | yes |
| managed_dbs | edge | "managed_hosting" | {"reported": "managed_hosting", "top": "managed_hosting", "confidence": 1.0, "top_p": 1.0} | yes |
| stops_leaks | edge | "data_loss_prevention" | {"reported": "data_loss_prevention", "top": "data_loss_prevention", "confidence": 1.0, "top_p": 1.0} | yes |
| pivoted | edge | "expense_management" | {"reported": "expense_management", "top": "expense_management", "confidence": 1.0, "top_p": 1.0} | yes |

## S09 Sort a live message stream: show, highlight, hide or blur
Cookbook: Twitch chat filter

- Round 2 stress cases; same method as round 1.
- One request per message with 3 questions; actions decided by rules in code (hostile and secret thresholds 0.7).

| Case | Kind | Expected | Got | Pass |
|---|---|---|---|---|
| spelled_out_password | edge | ["blur"] | {"action": "blur", "category": "unsolicited_fix", "margin": 0.21, "hostile": 0.03, "secret": 0.97} | yes |
| api_key | edge | ["blur"] | {"action": "blur", "category": "unsolicited_fix", "margin": 0.94, "hostile": 0.02, "secret": 0.81} | yes |
| panicked_question | edge | ["highlight", "page_oncall"] | {"action": "page_oncall", "category": "incident", "margin": 0.82, "hostile": 0.02, "secret": 0.02} | yes |
| polite_pitch | edge | ["hide"] | {"action": "hide", "category": "spam", "margin": 1.0, "hostile": 0.02, "secret": 0.02} | yes |
| dutch_insult | edge | ["hide"] | {"action": "hide", "category": "chatter", "margin": 0.98, "hostile": 0.95, "secret": 0.02} | yes |

## S10 Check a cheap extractor and escalate only the doubtful records
Cookbook: SDE cascade

- Round 2 stress cases; same method as round 1.
- Per-field Noul battery (2 checks per filled field, 1 per empty field), escalate if any > 0.7. Wrong records accepted: 0.

| Case | Kind | Expected | Got | Pass |
|---|---|---|---|---|
| k_units | edge | {"decision": "accept", "wrong_fields": []} | {"decision": "accept", "flagged_fields": [], "max": {}} | yes |
| former_ceo | edge | {"decision": "escalate", "wrong_fields": ["ceo_name"]} | {"decision": "escalate", "flagged_fields": ["ceo_name"], "max": {"ceo_name::hallucinated": 0.96, "ceo_name::off_target": 0.96}} | yes |
| rounded_count | edge | {"decision": "escalate", "wrong_fields": ["employee_count"]} | {"decision": "escalate", "flagged_fields": ["employee_count"], "max": {"employee_count::hallucinated": 0.98}} | yes |
| one_letter_off | edge | {"decision": "escalate", "wrong_fields": ["ceo_name"]} | {"decision": "escalate", "flagged_fields": ["ceo_name"], "max": {"ceo_name::hallucinated": 0.96, "ceo_name::off_target": 0.33}} | yes |

## S11 Read a date from text and let code do the calendar maths
Cookbook: Date extraction

- Round 2 stress cases; same method as round 1.
- Seven Choice questions per document; code assembles the date, infers missing years and resolves weekdays; review below confidence 0.6. Today pinned to 2026-10-28.

| Case | Kind | Expected | Got | Pass |
|---|---|---|---|---|
| us_format_stated | edge | ["2027-03-04"] | {"outcome": "2027-03-04", "proposed": "2027-03-04", "confidence": 0.95, "mode": "absolute"} | yes |
| end_of_next_month | edge | ["2026-11-30", "review"] | {"outcome": "2026-10-28", "proposed": "2026-10-28", "confidence": 0.73, "mode": "relative"} | **no** |
| ordinal_words | core | ["2027-01-21"] | {"outcome": "2027-01-21", "proposed": "2027-01-21", "confidence": 0.99, "mode": "absolute"} | yes |
| two_dates | edge | ["2026-04-01"] | {"outcome": "2026-04-01", "proposed": "2026-04-01", "confidence": 0.96, "mode": "absolute"} | yes |
| bare_friday | core | ["2026-10-30"] | {"outcome": "2026-10-30", "proposed": "2026-10-30", "confidence": 0.76, "mode": "relative"} | yes |
| past_without_year | code | ["2026-01-03"] | {"outcome": "2027-01-03", "proposed": "2027-01-03", "confidence": 0.82, "mode": "absolute"} | **no** |
| direct_date_comparison | edge | "6/6 comparisons right" | "6/6 right" | yes |

## S12 Pick the right value from candidates that code found
Cookbook: Pre-parsed value extraction

- Round 2 stress cases; same method as round 1.
- Regular expressions find every candidate; one Choice picks among them plus "none"; code copies the exact text.

| Case | Kind | Expected | Got | Pass |
|---|---|---|---|---|
| current_number | edge | "+44 161 496 0777" | {"picked": "+44 161 496 0777", "confidence": 1.0, "candidates": ["+44 161 496 0000", "+44 161 496 0777"]} | yes |
| gross_total | edge | "$9,600.00" | {"picked": "$9,600.00", "confidence": 1.0, "candidates": ["$8,000.00", "$1,600.00", "$9,600.00"]} | yes |
| net_price | core | "$8,000.00" | {"picked": "$8,000.00", "confidence": 1.0, "candidates": ["$8,000.00", "$1,600.00", "$9,600.00"]} | yes |
| remittance | core | "remit@halvorsen.example" | {"picked": "remit@halvorsen.example", "confidence": 1.0, "candidates": ["remit@halvorsen.example", "orders@halvorsen.example"]} | yes |
| vat_id_absent | edge | "none" | {"picked": "none", "confidence": 1.0, "candidates": ["+44 161 496 0000", "+44 161 496 0777"]} | yes |

## S13 Rebuild headings, lists and code from flattened text
Cookbook: Structure recovery

- Round 2 stress cases; same method as round 1.
- Pass 1: one Noul per adjacent line pair (join bar 0.2 after an unfinished line, 0.5 after end punctuation). Pass 2: one Choice per block. Two requests in total.

| Case | Kind | Expected | Got | Pass |
|---|---|---|---|---|
| line_joins | core | "12 of 12 join decisions right" | {"right": "11 of 12", "wrong": ["L003 (0.52)"]} | **no** |
| B000 2. Configure replication | edge | "heading" | {"type": "heading", "confidence": 0.45} | yes |
| B001 Edit the primary configurati | core | "paragraph" | {"type": "list_item", "confidence": 0.52} | **no** |
| B002 wal_level: replica | core | "code" | {"type": "code", "confidence": 0.92} | yes |
| B003 max_wal_senders: 10 | core | "code" | {"type": "code", "confidence": 0.78} | yes |
| B004 2. Restart the primary so th | edge | "list_item" | {"type": "list_item", "confidence": 0.96} | yes |
| B005 As the vendor guide puts it, | edge | "quote" | {"type": "quote", "confidence": 0.92} | yes |
| B006 Tip: check pg_stat_replicati | core | "callout" | {"type": "callout", "confidence": 1.0} | yes |
| B007 Replicas that fall more than | core | "paragraph" | {"type": "callout", "confidence": 0.34} | **no** |
| B008 3. Verify | core | "heading" | {"type": "list_item", "confidence": 0.78} | **no** |
| B009 Run SELECT * FROM pg_stat_re | edge | "paragraph" | {"type": "list_item", "confidence": 0.54} | **no** |

## S14 Move the most useful search result to the top
Cookbook: Re-ranking

- Round 2 stress cases; same method as round 1.
- Keyword (BM25) shortlist of 10 from 30 articles; one Noul per ticket-article pair; sort by probability. Pass = right article ranked first.
- Versus keyword rank: 1 better, 5 same, 0 worse, 0 not shortlisted.

| Case | Kind | Expected | Got | Pass |
|---|---|---|---|---|
| replica_cancelled | core | "a20" | {"keyword_rank_of_answer": 1, "jev_rank_of_answer": 1, "top_scores": {"a20": 0.92, "a11": 0.75, "a27": 0.43}} | yes |
| schema_change_stuck | core | "a21" | {"keyword_rank_of_answer": 1, "jev_rank_of_answer": 1, "top_scores": {"a21": 0.48, "a12": 0.42, "a29": 0.34}} | yes |
| accents_garbled | core | "a19" | {"keyword_rank_of_answer": 2, "jev_rank_of_answer": 1, "top_scores": {"a19": 0.88, "a03": 0.04, "a29": 0.04}} | yes |
| hour_off | core | "a18" | {"keyword_rank_of_answer": 1, "jev_rank_of_answer": 1, "top_scores": {"a18": 0.75, "a13": 0.04, "a29": 0.04}} | yes |
| missing_numbers | edge | "a17" | {"keyword_rank_of_answer": 1, "jev_rank_of_answer": 1, "top_scores": {"a17": 0.43, "a26": 0.16, "a19": 0.07}} | yes |
| space_not_freed | edge | "a14" | {"keyword_rank_of_answer": 1, "jev_rank_of_answer": 1, "top_scores": {"a14": 0.88, "a12": 0.8, "a03": 0.09}} | yes |

## S15 Find the exact line in a long document that answers a question
Cookbook: Line-by-line search

- Round 2 stress cases; same method as round 1.
- Whole 70-line document in one request per query: a Choice over line ids plus an "is it answered" Noul (found >= 0.7, absent <= 0.35).

| Case | Kind | Expected | Got | Pass |
|---|---|---|---|---|
| move_region | edge | ["L047"] | {"verdict": "found", "exists": 0.98, "top_line": "L047", "line_p": 1.0, "text": "Customer Data is hosted in the region chosen in the Order Form and is not moved outside that region without the Customer's written consent. | yes |
| breach_notice | core | ["L050"] | {"verdict": "found", "exists": 0.99, "top_line": "L050", "line_p": 1.0, "text": "Provider maintains ISO 27001 certification, encrypts Customer Data at rest and in transit, and notifies the Customer of any personal data b | yes |
| uncapped_dp | edge | ["L061", "L062"] | {"verdict": "found", "exists": 0.91, "top_line": "L062", "line_p": 0.85, "text": "The cap does not apply to breaches of confidentiality, data protection obligations or the Customer's payment obligations."} | yes |
| price_rise | core | ["L042"] | {"verdict": "found", "exists": 0.99, "top_line": "L042", "line_p": 1.0, "text": "Provider may increase fees at renewal by no more than 5%."} | yes |
| sso_absent | edge | "absent" | {"verdict": "absent", "exists": 0.03, "top_line": "L011", "line_p": 0.45, "text": "Support is available by email and through the support portal."} | yes |
| negated_question | edge | ["L018"] | {"verdict": "found", "exists": 0.97, "top_line": "L018", "line_p": 1.0, "text": "Backups are stored in a different region from the primary database."} | yes |

## S16 Decide whether two records are the same thing
Cookbook: Knowledge graph entity alignment

- Round 2 stress cases; same method as round 1.
- One Score (3 levels) plus three field Nouls per pair; code rounds the score: >= 1.5 merge, >= 0.5 curator, else separate. Unlike the cookbook, we score against labels.

| Case | Kind | Expected | Got | Pass |
|---|---|---|---|---|
| rebrand | edge | ["curator", "merge"] | {"route": "merge", "score": 1.99, "confidence": 0.98, "name": 0.24, "domain": 0.02, "place": 0.98} | yes |
| holding_company | edge | ["curator", "separate"] | {"route": "separate", "score": 0.45, "confidence": 0.34, "name": 0.02, "domain": 0.02, "place": 0.01} | yes |
| same_founder | edge | ["separate"] | {"route": "curator", "score": 0.64, "confidence": 0.43, "name": 0.02, "domain": 0.02, "place": 0.98} | **no** |
| generic_name | edge | ["curator", "separate"] | {"route": "curator", "score": 1.04, "confidence": 0.82, "name": 0.97, "domain": 0.02, "place": 0.02} | yes |
| address_vs_postcode | core | ["merge"] | {"route": "merge", "score": 1.84, "confidence": 0.76, "name": 0.93, "domain": 0.99, "place": 0.5} | yes |

## S17 Tick off a checklist as a conversation happens
Cookbook: Intelliprompter

- Round 2: an unnamed system, an unmeasured size, an undecided decision-maker and no budget should all stay unticked until truly covered.

| Case | Kind | Expected | Got | Pass |
|---|---|---|---|---|
| database | core | "ticked at chunk 3" | {"ticked_at_chunk": 3, "score": 3.98} | yes |
| volume | edge | "never ticked" | {"ticked_at_chunk": null, "score": null} | yes |
| decider | edge | "ticked at chunk 7" | {"ticked_at_chunk": 7, "score": 3.99} | yes |
| compliance | core | "ticked at chunk 6" | {"ticked_at_chunk": 6, "score": 3.68} | yes |
| budget | edge | "never ticked" | {"ticked_at_chunk": null, "score": null} | yes |

## S18 Ask more than once, act only when answers agree
Cookbook: Self-consistency: choices and nouls

- Round 2 stress cases; same method as round 1.
- 8 runs per ticket with a throwaway uid; odd runs reverse the option order. Code abstains below top probability 0.6. Abstained: 1/32 answers.

| Case | Kind | Expected | Got | Pass |
|---|---|---|---|---|
| vague_broken | edge | "no two different automatic labels" | {"original_order": {"Outage": 4}, "reversed_order": {"Outage": 4}, "top_p_range": [1.0, 1.0]} | yes |
| credit_for_outage | edge | "no two different automatic labels" | {"original_order": {"Billing": 4}, "reversed_order": {"Billing": 4}, "top_p_range": [0.96, 0.97]} | yes |
| slow_and_strange | edge | "no two different automatic labels" | {"original_order": {"Performance": 3, "abstain": 1}, "reversed_order": {"Performance": 4}, "top_p_range": [0.59, 0.69]} | yes |
| clear_performance | core | "Performance" | {"original_order": {"Performance": 4}, "reversed_order": {"Performance": 4}, "top_p_range": [1.0, 1.0]} | yes |

## S20 Turn free text into numbers a prediction model can use
Cookbook: Autoresearch feature discovery

- Control: the same Jev features against randomly shuffled labels must score near 0.5, or the pipeline is leaking. Reuses cached answers.

| Case | Kind | Expected | Got | Pass |
|---|---|---|---|---|
| shuffled_labels_control | core | "AUC between 0.44 and 0.56 when labels are shuffled" | {"auc": 0.495, "se": 0.006} | yes |

## S21 Read scanned documents: what is it, is it signed, where is the total
Cookbook: Images and Box (not a cookbook)

- Round 2 scans: noise and a 3-degree skew, a printed "signature pending" line, a restyled rotated stamp, a VAT breakdown with two totals, and a 330-pixel-wide copy.

| Case | Kind | Expected | Got | Pass |
|---|---|---|---|---|
| noisy_skewed:kind | core | "invoice" | {"kind": "invoice", "confidence": 1.0} | yes |
| noisy_skewed:signed | edge | true | 0.75 | yes |
| noisy_skewed:total_pick | edge | "$3,820.00" | {"picked": "$3,820.00", "confidence": 1.0} | yes |
| pending_signature:kind | core | "invoice" | {"kind": "invoice", "confidence": 1.0} | yes |
| pending_signature:signed | edge | false | 0.02 | yes |
| restyled_stamp:kind | core | "invoice" | {"kind": "invoice", "confidence": 1.0} | yes |
| restyled_stamp:stamp | edge | "PAID" | {"stamp": "PAID", "confidence": 1.0} | yes |
| vat_totals:kind | core | "invoice" | {"kind": "invoice", "confidence": 1.0} | yes |
| vat_totals:total_pick | edge | "$4,584.00" | {"picked": "$4,584.00", "confidence": 1.0} | yes |
| vat_totals:over_4000 | edge | true | 0.99 | yes |
| vat_totals:total_box | edge | "box centred on the total" | {"found": true, "iou": 0.39} | yes |
| low_resolution:kind | core | "invoice" | {"kind": "invoice", "confidence": 1.0} | yes |
| low_resolution:total_pick | edge | "$3,820.00" | {"picked": "$3,820.00", "confidence": 1.0} | yes |

## R01 Turn a plain-English request into the right action (with remedy)
Cookbook: Function calling

- Remedy: every argument menu gains "not on the list", plus one Noul asking whether the request wants anything extra; code refuses to run if either fires.

| Case | Kind | Expected | Got | Pass |
|---|---|---|---|---|
| contacts_parquet_week | core | {"tool": "export_table", "args": {"table": "contacts", "format": "parquet", "since": "1w"}} | {"tool": "export_table", "args": {"table": "contacts", "format": "parquet", "since": "1w"}, "extra": 0.94, "auto_runs": false} | **no** |
| count_invoices | core | {"tool": "row_count", "args": {"table": "invoices"}} | {"tool": "row_count", "args": {"table": "invoices"}, "extra": 0.43, "auto_runs": true} | yes |
| dupes_by_domain | core | {"tool": "find_duplicates", "args": {"table": "accounts", "key": "domain"}} | {"tool": "find_duplicates", "args": {"table": "accounts", "key": "domain"}, "extra": 0.79, "auto_runs": false} | **no** |
| nightly_billing_backup | core | {"tool": "schedule_backup", "args": {"database": "billing", "frequency": "daily"}} | {"tool": "schedule_backup", "args": {"database": "billing", "frequency": "daily"}, "extra": 0.75, "auto_runs": false} | **no** |
| invoices_json_no_window | core | {"tool": "export_table", "args": {"table": "invoices", "format": "json"}} | {"tool": "export_table", "args": {"table": "invoices", "format": "json"}, "extra": 0.16, "auto_runs": true} | yes |
| negated_then_count | edge | {"tool": "row_count", "args": {"table": "contacts"}} | {"tool": "row_count", "args": {"table": "contacts"}, "extra": 0.39, "auto_runs": true} | yes |
| unsupported_values | edge | "do not run" | {"tool": "export_table", "args": {"table": "not_listed", "format": "not_listed"}, "extra": 0.11, "auto_runs": false} | yes |
| lookalike_action | edge | "do not run" | {"tool": "none_of_these", "args": {}, "extra": 0.39, "auto_runs": false} | yes |
| excel_synonym | edge | "do not run" | {"tool": "export_table", "args": {"table": "not_listed", "format": "not_listed"}, "extra": 0.1, "auto_runs": false} | yes |
| fifteen_minutes | edge | "do not run" | {"tool": "schedule_backup", "args": {"database": "crm", "frequency": "not_listed"}, "extra": 0.16, "auto_runs": false} | yes |
| two_tables | edge | "do not run" | {"tool": "row_count", "args": {"table": "not_listed"}, "extra": 0.95, "auto_runs": false} | yes |
| filter_unsupported | edge | "do not run" | {"tool": "export_table", "args": {"table": "contacts", "format": "csv"}, "extra": 0.93, "auto_runs": false} | yes |
| slangy | core | {"tool": "export_table", "args": {"table": "invoices", "format": "csv", "since": "1mo"}} | {"tool": "export_table", "args": {"table": "invoices", "format": "csv", "since": "1mo"}, "extra": 0.9, "auto_runs": false} | **no** |
| weekly_warehouse | core | {"tool": "schedule_backup", "args": {"database": "warehouse", "frequency": "weekly"}} | {"tool": "schedule_backup", "args": {"database": "warehouse", "frequency": "weekly"}, "extra": 0.9, "auto_runs": false} | **no** |

## R11 Read a date from text and let code do the calendar maths (with remedy)
Cookbook: Date extraction

- Remedy: the "relative to" menu gains "something else", and a Noul flags dates that could be read two ways; code sends both to review.

| Case | Kind | Expected | Got | Pass |
|---|---|---|---|---|
| explicit | core | ["2027-03-01"] | {"outcome": "2027-03-01", "why": "absolute", "ambiguous": 0.14, "anchor": "none"} | yes |
| no_year | core | ["2026-11-14"] | {"outcome": "2026-11-14", "why": "absolute", "ambiguous": 0.12, "anchor": "none"} | yes |
| next_tuesday | core | ["2026-11-03"] | {"outcome": "2026-11-03", "why": "relative", "ambiguous": 0.05, "anchor": "weekday"} | yes |
| not_stated | core | ["none", "review"] | {"outcome": "none", "why": "none", "ambiguous": 0.04, "anchor": "none"} | yes |
| today | core | ["2026-10-28"] | {"outcome": "2026-10-28", "why": "relative", "ambiguous": 0.04, "anchor": "today"} | yes |
| twelve_months_later | edge | ["2027-01-15", "review"] | {"outcome": "review", "why": "unsupported relative form", "ambiguous": 0.06, "anchor": "other"} | yes |
| ambiguous_numeric | edge | ["review"] | {"outcome": "review", "why": "ambiguous", "ambiguous": 0.87, "anchor": "none"} | yes |
| days_after_invoice | edge | ["2026-04-02", "review"] | {"outcome": "review", "why": "unsupported relative form", "ambiguous": 0.16, "anchor": "other"} | yes |
| us_format_stated | edge | ["2027-03-04"] | {"outcome": "2027-03-04", "why": "absolute", "ambiguous": 0.43, "anchor": "none"} | yes |
| end_of_next_month | edge | ["2026-11-30", "review"] | {"outcome": "review", "why": "unsupported relative form", "ambiguous": 0.07, "anchor": "other"} | yes |
| ordinal_words | core | ["2027-01-21"] | {"outcome": "2027-01-21", "why": "absolute", "ambiguous": 0.06, "anchor": "none"} | yes |
| two_dates | edge | ["2026-04-01"] | {"outcome": "2026-04-01", "why": "absolute", "ambiguous": 0.05, "anchor": "none"} | yes |
| bare_friday | core | ["2026-10-30"] | {"outcome": "2026-10-30", "why": "relative", "ambiguous": 0.06, "anchor": "weekday"} | yes |
| past_without_year | code | ["2026-01-03"] | {"outcome": "2027-01-03", "why": "absolute", "ambiguous": 0.14, "anchor": "none"} | **no** |
