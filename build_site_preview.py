"""Preview of ARTICLE.md as a post on webuilddatabases.com: python build_site_preview.py
Mirrors the live blog-post template (measured 2026-10-29): header, navy BLOG band,
featured image + date/byline/title, then the body. Gomme Sans is substituted by Inter,
as the brand kit does. ponytail: static mock, not the WordPress theme."""
import pathlib, re, markdown

here = pathlib.Path(__file__).parent
md = (here / "ARTICLE.md").read_text(encoding="utf-8")
md = md.replace("<details open", '<details markdown="1" open')

# Split off the H1 and the italic standfirst; the template renders them in its own hero.
title = re.match(r"# (.+)", md).group(1)
md = md[md.index("\n") + 1:]
stand_md = re.search(r"\A\s*(\*.+?\*)\s*$", md, re.M).group(1)  # first italic paragraph after the title
md = md.replace(stand_md, "", 1).replace("\n---\n", "\n", 1)
stand = re.sub(r"^<p>|</p>$", "", markdown.markdown(stand_md).strip())
body = markdown.markdown(md, extensions=["tables", "toc", "md_in_html"])

HTML = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<title>{title} | We Build Databases</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap">
<style>
:root{{--navy:#082241;--ink:#333;--li:#5e5e5e;--gold:#F2C931;--green:#5CB800;--purple:#8B5FA8;--rule:#E3E6EA}}
*{{box-sizing:border-box}}
body{{margin:0;background:#fff;color:var(--ink);font:300 17px/1.4 Inter,"Gomme Sans",Arial,sans-serif}}
.wrap{{max-width:1300px;margin:0 auto;padding:0 24px}}
.topbar{{background:#F4F5F7;font-size:14px;font-weight:400;color:var(--navy)}}
.topbar .wrap{{display:flex;justify-content:flex-end;gap:32px;padding:8px 24px}}
.topbar span::before{{content:"";display:inline-block;width:14px;height:14px;background:var(--green);border-radius:50%;margin-right:8px;vertical-align:-2px}}
.nav .wrap{{display:flex;align-items:center;gap:28px;padding:14px 24px}}
.nav img{{height:58px;margin-right:auto}}
.nav a{{color:#1b1b1b;text-decoration:none;font-weight:400;font-size:16px}}
.nav .cta{{background:var(--purple);color:#fff;padding:12px 26px;font-weight:500}}
.band{{background:radial-gradient(1200px 300px at 70% 120%,#1F3F73 0%,#0B1F3F 55%,#071733 100%);color:#fff;padding:22px 0 30px}}
.band .crumb{{font-size:12px;letter-spacing:.04em;text-transform:uppercase;font-weight:500}}
.band .crumb b{{color:var(--gold);font-weight:600}}
.band h1{{margin:14px 0 0;font:700 44px/1.1 "Work Sans",Inter,sans-serif}}
.hero{{display:grid;grid-template-columns:554px 1fr;gap:72px;align-items:center;padding:56px 0 40px}}
.hero img{{width:100%;display:block}}
.date{{color:#C9A227;font-weight:700;font-size:13px;letter-spacing:.04em;text-transform:uppercase;margin:0}}
.by{{margin:4px 0 22px;font-size:14px;color:#777}}
.hero h2.title{{margin:0;font:500 45px/1.2 Inter,"Gomme Sans",sans-serif;color:var(--navy)}}
.stand{{font-size:19px;font-weight:300;color:var(--ink);margin:18px 0 0}}
article{{padding:8px 0 80px}}
article h2{{font-size:25px;font-weight:500;color:var(--ink);line-height:1.4;margin:40px 0 10px}}
article h3{{font-size:17px;font-weight:600;color:var(--ink);margin:28px 0 8px}}
article p{{margin:0 0 16px}}
article li{{color:var(--li);font-weight:400;margin:4px 0}}
article strong{{font-weight:600;color:#222}}
article img{{display:block;width:100%;max-width:1000px;height:auto;margin:22px 0;border:1px solid var(--rule)}}

article table{{border-collapse:collapse;width:100%;font-size:15px;font-weight:400;margin:16px 0}}
article th,article td{{padding:8px 10px;border-bottom:1px solid var(--rule);text-align:left;vertical-align:top}}
article th{{font-weight:600;color:var(--navy)}}
article code{{font:14px "IBM Plex Mono",Consolas,monospace;background:#F1F3F5;padding:1px 4px}}
article hr{{border:0;border-top:1px solid var(--rule);margin:48px 0}}
article a{{color:var(--ink);text-decoration:underline}}
.cta-band{{background:var(--navy);color:#fff;padding:56px 0;text-align:center}}
.cta-band h2{{font:700 32px/1.2 "Work Sans",Inter,sans-serif;margin:0 0 10px}}
.cta-band p{{margin:0 0 24px;font-weight:300}}
.cta-band a{{display:inline-block;background:var(--green);color:#fff;text-decoration:none;padding:14px 28px;font-weight:600}}
footer{{background:#061629;color:#B9C3D1;font-size:14px;padding:36px 0}}
@media (max-width:900px){{.hero{{grid-template-columns:1fr;gap:24px}}.nav a:not(.cta){{display:none}}.band h1{{font-size:32px}}.hero h2.title{{font-size:32px}}}}
article details{{margin:18px 0 22px;padding:12px 18px;border:1px solid #D9D4C7;background:#FFFFFF}}article summary{{cursor:pointer;font-size:15px;color:#6B7280;letter-spacing:.02em}}article summary strong{{font-weight:600;color:#1F2A44}}article details blockquote{{margin:12px 0 4px;padding:0 0 0 16px;border-left:3px solid #D9D4C7;font-size:15px;line-height:1.55;color:#3B4252}}article details blockquote p{{margin:0 0 10px}}article details code{{font-size:13px}}article blockquote.pull{{margin:36px 0;padding:0 0 0 28px;max-width:720px;border-left:3px solid #B9C3D1;background:none;font-size:26px;line-height:1.35;font-weight:500;color:var(--navy)}}article blockquote.pull strong{{font-weight:500}}
</style></head><body>
<div class="topbar"><div class="wrap"><span>(586) 992-6472</span><span>info@webuilddatabases.com</span></div></div>
<div class="nav"><div class="wrap"><img src="images/site/logo-colour.png" alt="We Build Databases"><a href="#">About Us</a><a href="#">Services</a><a href="#">Case Studies</a><a href="#">Blog</a><a href="#">Contact</a><a class="cta" href="#">Get Started</a></div></div>
<div class="band"><div class="wrap"><div class="crumb">Home &bull; Blog &bull; <b>{title}</b></div><h1>BLOG</h1></div></div>
<div class="wrap">
<div class="hero">
  <img src="images/site/title-card.png" alt="Title card: {title}">
  <div><p class="date">October 29, 2026</p><p class="by">By Dan</p><h2 class="title">{title}</h2><p class="stand">{stand}</p></div>
</div>
<article>{body}</article>
</div>
<div class="cta-band"><div class="wrap"><h2>Have data that needs judging, not just storing?</h2><p>We build the database, the pipeline and the rules around tools like Jev.</p><a href="#">Talk to an Expert</a></div></div>
<footer><div class="wrap">&copy; 2026 We Build Databases &middot; (586) 992-6472 &middot; info@webuilddatabases.com</div></footer>
</body></html>
"""
(here / "ARTICLE-site-preview.html").write_text(HTML, encoding="utf-8")
print("wrote ARTICLE-site-preview.html")
