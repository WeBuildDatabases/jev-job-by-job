"""Make wordpress-package/post-content.html: the article body with the live image URLs and the stylesheet inlined.
Run after build_wordpress.py. The result is what the WordPress post's Code tab holds."""
import json, re, pathlib

pkg = pathlib.Path(__file__).parent / "wordpress-package"
body = (pkg / "article-body.html").read_text(encoding="utf-8")
url = {x["local"]: x["url"] for x in json.load(open(pkg / "upload-map.json", encoding="utf-8"))
       if x["local"].endswith(".png") and "/" not in x["local"] and " " not in x["local"]}
n = 0
for local, u in url.items():
    n += body.count(f'src="images/{local}"')
    body = body.replace(f'src="images/{local}"', f'src="{u}"')
assert n == 23 and 'src="images/' not in body, n
# wpautop turns a newline inside a paragraph into <br>, so wrapped lines inside p/li are joined
body = re.sub(r'(<(p|li)[ >][^<]*?)\n(?=[^<]*</\2>)', lambda m: m.group(1) + ' ', body)
css = re.sub(r'/\*.*?\*/\n', '', (pkg / "styles.css").read_text(encoding="utf-8"), flags=re.S)
out = f'<style>\n{css}</style>\n<div class="jev-article">\n{body}\n</div>'
(pkg / "post-content.html").write_text(out, encoding="utf-8")
print("post-content.html:", len(out), "chars,", out.count("<details"), "details,", out.count("<img "), "images")
