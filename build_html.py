"""Rebuild ARTICLE.html from ARTICLE.md: python build_html.py"""
import pathlib, markdown

HEAD = """<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Jev, job by job</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body{margin:0;background:#F7F5F0;color:#1F2A44;font:17px/1.6 "Segoe UI",Inter,Arial,sans-serif}
main{max-width:860px;margin:0 auto;padding:48px 24px 96px}
h1{font-size:38px;line-height:1.15;margin:0 0 16px}h2{font-size:26px;margin:48px 0 12px}h3{font-size:20px}
img{display:block;width:100%;height:auto;margin:20px 0;border:1px solid #D9D4C7}
table{border-collapse:collapse;width:100%;font-size:15px;margin:16px 0}th,td{padding:8px 10px;border-bottom:1px solid #D9D4C7;text-align:left;vertical-align:top}
th{font-weight:600}code{font:14px Consolas,monospace;background:#ECE8DE;padding:1px 4px;border-radius:3px}

hr{border:0;border-top:1px solid #D9D4C7;margin:40px 0}a{color:#1971C2}
details{margin:18px 0 22px;padding:12px 18px;border:1px solid #D9D4C7;background:#FFFFFF}summary{cursor:pointer;font-size:15px;color:#6B7280;letter-spacing:.02em}summary strong{font-weight:600;color:#1F2A44}details blockquote{margin:12px 0 4px;padding:0 0 0 16px;border-left:3px solid #D9D4C7;font-size:15px;line-height:1.55;color:#3B4252}details blockquote p{margin:0 0 10px}details code{font-size:13px}blockquote.pull{margin:36px 0;padding:0 0 0 28px;max-width:720px;border-left:3px solid #B9C3D1;background:none;font-size:26px;line-height:1.35;font-weight:500;color:#082241}blockquote.pull strong{font-weight:500}
</style></head><body><main>"""

here = pathlib.Path(__file__).parent
md = (here / "ARTICLE.md").read_text(encoding="utf-8")
md = md.replace("<details open", '<details markdown="1" open')
body = markdown.markdown(md, extensions=["tables", "toc", "md_in_html"])
(here / "ARTICLE.html").write_text(HEAD + body + "\n</main></body></html>\n", encoding="utf-8")
print("wrote ARTICLE.html")
