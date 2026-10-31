"""Assemble the WordPress hand-off package from ARTICLE.md: python build_wordpress.py
Writes wordpress-package/ (body HTML, images, alt text, CSS, metadata, README) and wordpress-package.zip."""
import csv, json, re, shutil, zipfile, pathlib, markdown

here = pathlib.Path(__file__).parent
out = here / "wordpress-package"
(out / "images").mkdir(parents=True, exist_ok=True)  # ponytail: overwrite in place; rmtree trips on OneDrive's folder lock

md = (here / "ARTICLE.md").read_text(encoding="utf-8")
title = re.match(r"# (.+)", md).group(1)
body_md = md[md.index("\n") + 1:]
stand_md = re.search(r"\A\s*(\*.+?\*)\s*$", body_md, re.M).group(1)
excerpt = re.sub(r"\*+", "", stand_md)
body_md = body_md.replace(stand_md, "", 1).replace("\n---\n", "\n", 1)
body_md = body_md.replace("<details id=", '<details markdown="1" id=')
body = markdown.markdown(body_md, extensions=["tables", "toc", "md_in_html"])
body = body.replace(' markdown="1"', "")
# part headings are h1 in the markdown; the post title is the page's h1, so they become h2.part
body = re.sub(r'<h1 id="([^"]+)">(.+?)</h1>', r'<h2 class="part" id="\1">\2</h2>', body)
# external links open in a new tab; in-page (#) links do not
body = re.sub(r'<a href="(https?://[^"]+)"', r'<a href="\1" target="_blank" rel="noopener"', body)
# each job section ends with a link back to the scoreboard
body = "".join(c.rstrip("\n") + '\n<p class="back"><a href="#scoreboard">&uarr; Back to the scoreboard</a></p>\n'
               if re.match(r'<h2 id="\d+-', c) else c for c in re.split(r'(?=<h2 )', body))
# scoreboard: part rows span the table, the total row is marked, numeric cells are tagged
body = body.replace("<table>", '<table class="scoreboard">', 1)
body = re.sub(r'<tr>\n<td></td>\n<td>(<strong>Part \d+:.*?</strong>)</td>\n<td></td>\n<td></td>\n<td></td>\n</tr>',
              r'<tr class="part"><td colspan="5">\1</td></tr>', body)
body = body.replace('<tr>\n<td></td>\n<td><strong>All jobs</strong></td>', '<tr class="total">\n<td></td>\n<td><strong>All jobs</strong></td>')
body = re.sub(r'<th>(Core|Edge)</th>', r'<th class="num">\1</th>', body)
body = re.sub(r'(<tr(?: class="total")?>\n<td>\d*</td>\n<td>.*?</td>\n)<td>(.*?)</td>\n<td>(.*?)</td>', r'\1<td class="num">\2</td>\n<td class="num">\3</td>', body)
stand_html = re.sub(r"^<p>|</p>$", "", markdown.markdown(stand_md).strip())
body = f'<p class="standfirst">{stand_html}</p>\n' + body   # the excerpt is for listings; the post itself opens with the standfirst
(out / "article-body.html").write_text(body + "\n", encoding="utf-8")
shutil.copy(here / "ARTICLE.md", out / "ARTICLE.md")

# images referenced by the body, plus the header art and share card
imgs = re.findall(r'src="images/([^"]+)"', body)
assert len(imgs) == 23, len(imgs)
for name in imgs:
    shutil.copy(here / "images" / name, out / "images" / name)
    svg = (here / "images" / name).with_suffix(".svg")
    if svg.exists():
        shutil.copy(svg, out / "images" / svg.name)
shutil.copy(here / "images/site/header.png", out / "images/header-1200x630.png")
shutil.copy(here / "images/site/title-card.png", out / "images/share-card-1200x630.png")

# alt text per figure, with the section it sits in
rows, section = [], "Intro"
for m in re.finditer(r'^(## .+)$|^!\[([^\]]*)\]\(images/([^)]+)\)', md, flags=re.M):
    if m.group(1):
        section = m.group(1)[3:]
    else:
        rows.append({"file": m.group(3), "section": section, "alt": m.group(2)})
with open(out / "alt-text.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["file", "section", "alt"]); w.writeheader(); w.writerows(rows)

(out / "styles.css").write_text("""/* Jev article. Scoped to .jev-article; the post body is wrapped in that div. */
.jev-article { max-width: 760px; color: #2B2F36; }
.jev-article p, .jev-article li { font-size: 17px; line-height: 1.65; }
.jev-article p { margin: 0 0 18px; }
.jev-article li { margin: 0 0 7px; }
.jev-article ul, .jev-article ol { margin: 0 0 20px; padding-left: 28px; }
.jev-article a { color: #244C79; text-decoration: underline; text-underline-offset: 2px; text-decoration-color: #B9C3D1; }
.jev-article a:hover { color: #082241; text-decoration-color: #082241; }
.jev-article strong { color: #082241; }
.jev-article h2 { font-size: 26px; line-height: 1.25; color: #082241; margin: 44px 0 14px; scroll-margin-top: 110px; }
.jev-article h2.part { font-size: 21px; letter-spacing: .01em; color: #704184; margin: 56px 0 10px; padding-top: 22px; border-top: 1px solid #E3E6EA; }
.jev-article hr { border: 0; height: 0; margin: 0; }
.jev-article .standfirst { font-size: 20px; line-height: 1.55; color: #3B4252; margin: 0 0 30px; }
.jev-article img { display: block; width: 100%; height: auto; margin: 26px 0; border: 1px solid #E3E6EA; }
.jev-article code { font: 14.5px/1.4 "IBM Plex Mono", Consolas, monospace; background: #F1F3F5; padding: 1px 5px; border-radius: 3px; }
.jev-article table.scoreboard { border-collapse: collapse; width: 100%; font-size: 15px; line-height: 1.4; margin: 18px 0 28px; }
.jev-article table.scoreboard th, .jev-article table.scoreboard td { padding: 9px 10px; border-bottom: 1px solid #E3E6EA; text-align: left; vertical-align: top; }
.jev-article table.scoreboard th { font-weight: 600; color: #082241; border-bottom: 2px solid #082241; padding-bottom: 8px; }
.jev-article table.scoreboard td:first-child { color: #758190; width: 2.2em; padding-left: 0; }
.jev-article table.scoreboard th:first-child { padding-left: 0; }
.jev-article table.scoreboard .num { text-align: right; white-space: nowrap; font-variant-numeric: tabular-nums; width: 4.5em; }
.jev-article table.scoreboard td a { text-decoration: none; color: #244C79; }
.jev-article table.scoreboard td a:hover { text-decoration: underline; }
.jev-article table.scoreboard tr.part td { padding: 22px 0 6px; border-bottom: 1px solid #082241; }
.jev-article table.scoreboard tr.part strong { font-size: 13px; letter-spacing: .08em; text-transform: uppercase; color: #704184; }
.jev-article table.scoreboard tr.total td { border-bottom: 0; border-top: 2px solid #082241; padding-top: 12px; }
.jev-article p.back { margin: 6px 0 0; font-size: 14px; }
.jev-article p.back a { display: inline-block; padding: 6px 12px; border: 1px solid #B9C3D1; border-radius: 4px; background: #F7F8FA; color: #244C79; text-decoration: none; }
.jev-article p.back a:hover { border-color: #082241; color: #082241; }
.jev-article details pre { white-space: pre-wrap; overflow-wrap: anywhere; font: 14px/1.55 "IBM Plex Mono", Consolas, monospace; color: #2B2F36; background: #F1F3F5; padding: 14px 16px; border-radius: 4px; margin: 12px 0 8px; }
.jev-article pre code { background: none; padding: 0; font: inherit; }
.jev-article blockquote.pull { margin: 36px 0; padding: 0 0 0 28px; max-width: 720px; border-left: 3px solid #B9C3D1; background: none; font-size: 26px; line-height: 1.35; font-weight: 500; color: #082241; }
.jev-article blockquote.pull strong { font-weight: 500; }
.jev-article details { scroll-margin-top: 110px; margin: 18px 0 24px; padding: 12px 18px; border: 1px solid #E3E6EA; border-radius: 4px; background: #fff; }
.jev-article details[open] { padding-bottom: 6px; }
.jev-article summary { cursor: pointer; font-size: 15px; color: #6B7280; letter-spacing: .02em; list-style-position: inside; }
.jev-article summary:hover strong { text-decoration: underline; }
.jev-article summary strong { font-weight: 600; color: #082241; }
.jev-article details blockquote { margin: 14px 0 6px; padding: 0 0 0 16px; border-left: 3px solid #D9D4C7; font-size: 15px; line-height: 1.55; color: #3B4252; }
.jev-article details blockquote p { font-size: 15px; margin: 0 0 10px; }
""", encoding="utf-8")

words = len(re.sub(r"<[^>]+>", " ", body).split())
meta = {
    "title": title,
    "slug": "jev-job-by-job",
    "excerpt": excerpt,
    "meta_description": "We tested 21 TypeSafe cookbooks for Jev, the model that decides instead of writes. What it does well, where it breaks, and when to reach for it.",
    "featured_image": "images/header-1200x630.png",
    "social_share_image": "images/share-card-1200x630.png",
    "author": "Dan",
    "category": "Blog",
    "tags": ["Jev", "TypeSafe", "AI", "databases", "data enrichment"],
    "word_count": words,
    "reading_time_minutes": round(words / 230),
    "figures": len(imgs),
    "anchors": {"sections": "h2 ids are generated from the heading text; the scoreboard links depend on them",
                "prompts": "details blocks carry ids prompts-1 to prompts-21, closed by default; the intro 'View the prompts' link targets prompts-1"},
}
(out / "meta.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")

(out / "README.md").write_text(f"""# WordPress hand-off: "{title}"

Everything here is generated from `ARTICLE.md` by `build_wordpress.py`. Edit the Markdown, not the HTML.

## Files
- `article-body.html`: the post body only, no `<html>`/`<head>`. Paste into a Custom HTML block, or the Code editor view of the post. Wrap it in `<div class="jev-article">…</div>` so `styles.css` applies.
- `images/`: {len(imgs)} figures as PNG (1600x900) with editable SVG beside each, plus `header-1200x630.png` (featured image) and `share-card-1200x630.png` (Open Graph / social share).
- `alt-text.csv`: alt text for every figure, already present in the HTML too. Use it when uploading to the media library.
- `styles.css`: pull quote, collapsible prompt blocks, tables, figure sizing. Add to the post's Custom CSS or Appearance > Customize > Additional CSS.
- `meta.json`: title, slug, excerpt, meta description, tags, featured image, word count.
- `ARTICLE.md`: the source, for diffing later edits.

## Steps
1. Upload `images/*.png` to the media library. Keep the file names.
2. In `article-body.html`, replace `src="images/` with the upload URL prefix, for example `src="/wp-content/uploads/2026/10/`. One search-and-replace.
3. Create the post with the title, slug and excerpt from `meta.json`. Set `header-1200x630.png` as the featured image and `share-card-1200x630.png` as the social image (Yoast / Rank Math "Social" tab).
4. Paste the body inside `<div class="jev-article">…</div>` and add `styles.css`.
5. Check: the scoreboard links jump to their sections, the "View the prompts" link in the intro lands on the first prompt block, the 21 "What we asked Jev" blocks are closed and open on click, and the pull quote has no background.

## Notes
- The three outbound links in "How we tested" point at the public repo, https://github.com/WeBuildDatabases/jev-job-by-job. No relative links remain.
- The `<details>` and `id` attributes must survive: use a Custom HTML block or the Code editor, not the visual editor, which strips them.
- Headings carry ids generated from their text (for example `#2-pick-the-right-tool-for-an-ai-agent-or-none`). If the theme rewrites heading ids, re-point the scoreboard links or keep the explicit ids.
- The post body on the current theme runs about 1,285px wide; cap `.jev-article` near 760px for an article this long.
- All figures carry real test numbers and verbatim quotes. Do not crop, re-caption or substitute them.
""", encoding="utf-8")

zip_path = here / "wordpress-package.zip"
with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
    for p in sorted(out.rglob("*")):
        if p.is_file():
            z.write(p, p.relative_to(here))
print(f"wrote {out.name}/ and {zip_path.name}: {words} words, {len(imgs)} figures, {sum(1 for _ in out.rglob('*') if _.is_file())} files")
