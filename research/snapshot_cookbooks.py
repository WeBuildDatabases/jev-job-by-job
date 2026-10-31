"""Re-download TypeSafe's cookbook pages into research/typesafe-pages/ and show what changed since the last snapshot.
Run it the morning the article goes live:  python research/snapshot_cookbooks.py
Each page says "Numbers below came from `jev-X` on DATE", so the diff names which pages were regenerated."""
import pathlib, subprocess, urllib.request

here = pathlib.Path(__file__).parent / "typesafe-pages"
base = "https://docs.typesafe.ai/"
pages = ["llms.txt", "introduction/coding-agents.md", "agent-skill.md"] + [
    f"cookbooks/{s}.md" for s in """function_calling skill_suggestion llm_guardrails citation_check classifying_rag_passages
    basic_memory hierarchical_classification classification_using_confidence twitch_chat_filter sde_cascade
    date_extraction_cookbook pre_parsed_value_extraction_cookbook autoformat cart_from_primitives rerank_typesafe
    semantic_find entity_alignment intelliprompter consistency_choice_cookbook consistency_noul_cookbook
    parallel_questions autoresearch_feature_discovery reading_scanned_documents ocr_confidence_bounding_boxes feeder_watch""".split()]

for p in pages:
    data = urllib.request.urlopen(base + p, timeout=30).read()
    (here / pathlib.Path(p).name).write_bytes(data)
# a cookbook added to the index since last time shows up here as a new line in llms.txt
print(subprocess.run(["git", "diff", "--stat", "--", str(here)], capture_output=True, text=True).stdout or "no changes since the last snapshot")
print("for the detail: git diff -- research/typesafe-pages")
