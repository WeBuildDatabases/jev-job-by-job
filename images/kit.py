"""Tiny SVG drawing kit for the article figures. Every figure shares one grammar:
the material (left) -> Jev's answer (middle) -> what your software does (right).

Colour rules: green, amber and red mean only act, ask a person and stop. Family accents are chosen
from hues that never collide with those three, and carry no judgement."""
from html import escape
from PIL import ImageFont

W, H = 1600, 900
BG, INK, MUTED, LINE, CARD = '#F7F5F0', '#1F2A44', '#6B7280', '#D9D4C7', '#FFFFFF'
OK, WARN, BAD = '#2B8A3E', '#E8890C', '#C92A2A'  # act, ask a person, stop
BOXC = '#1C7ED6'  # the "where" answer: a box drawn on the material
FAMILY = {  # name, accent, light tint
    'agents': ('Agents and assistants', '#1971C2', '#E3EEFA'),
    'classify': ('Classification', '#0C8599', '#E0F3F5'),
    'extract': ('Extraction', '#6741D9', '#ECE6FB'),
    'search': ('Search and matching', '#AE3EC9', '#F6E6FA'),
    'technique': ('Techniques', '#4C5A73', '#E7EAF0'),
    'images': ('Images', '#343A40', '#E9EAEC'),
    'overview': ('', '#1F2A44', '#E6E8EE'),
}
SANS = "'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
DISPLAY = "Bahnschrift, 'DIN Alternate', 'Segoe UI', sans-serif"
MONO = "Consolas, Menlo, monospace"
_F = 'C:/Windows/Fonts/'


def tw(s, size, bold=False, mono=False, display=False):
    """Exact rendered width of a string, measured with the same font the PNG uses."""
    if display:
        f = ImageFont.truetype(_F + 'bahnschrift.ttf', size)
        f.set_variation_by_name('SemiBold' if bold else 'Regular')
        return f.getlength(s)
    f = _F + ('consola.ttf' if mono else 'segoeuib.ttf' if bold else 'segoeui.ttf')
    return ImageFont.truetype(f, size).getlength(s)


def wrap(s, size, width, bold=False, mono=False):
    lines, cur = [], ''
    for w in s.split():
        t = (cur + ' ' + w).strip()
        if tw(t, size, bold, mono) <= width:
            cur = t
        else:
            lines.append(cur)
            cur = w
    return lines + [cur] if cur else lines


def text(x, y, s, size=24, fill=INK, bold=False, anchor='start', mono=False, italic=False, op=1, display=False):
    fam, wt = (DISPLAY, 600 if bold else 400) if display else (MONO if mono else SANS, 700 if bold else 400)
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-family="{fam}" font-size="{size}" '
            f'font-weight="{wt}" fill="{fill}" text-anchor="{anchor}"'
            f'{" font-style=\"italic\"" if italic else ""}{f" opacity=\"{op}\"" if op != 1 else ""}>{escape(s)}</text>')


def para(x, y, s, size=24, width=400, fill=INK, bold=False, lh=1.3, mono=False, anchor='start'):
    """Wrapped text; returns (svg, height used)."""
    lines = wrap(s, size, width, bold, mono)
    out = ''.join(text(x, y + i * size * lh, ln, size, fill, bold, anchor, mono) for i, ln in enumerate(lines))
    return out, len(lines) * size * lh


def rect(x, y, w, h, r=14, fill=CARD, stroke=None, sw=2, dash=None, shadow=False, op=1):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}"'
            f'{f" stroke=\"{stroke}\" stroke-width=\"{sw}\"" if stroke else ""}'
            f'{f" stroke-dasharray=\"{dash}\"" if dash else ""}'
            f'{f" opacity=\"{op}\"" if op != 1 else ""}/>')


def card(x, y, w, h, stroke=None):
    return rect(x, y, w, h, 10, CARD, stroke or LINE, 1.5)


def chip(x, y, label, on=False, color=INK, size=22, h=40, outline=None, dash=None, mono=False):
    """A pill. Returns (svg, width)."""
    w = tw(label, size, bold=on, mono=mono) + 32
    fill = color if on else CARD
    s = rect(x, y, w, h, h / 2, fill, outline or (color if on else LINE), 2, dash)
    s += text(x + w / 2, y + h / 2 + size * 0.36, label, size, CARD if on else INK, on, 'middle', mono)
    return s, w


def bar(x, y, w, label, value, color, size=21, show=True, h=14, threshold=None):
    """Labelled probability bar, label above; an optional dark tick marks your threshold."""
    s = text(x, y, label, size, INK)
    if show:
        s += text(x + w, y, f'{value:.2f}', size + 2, color, True, 'end', display=True)
    s += rect(x, y + 12, w, h, h / 2, '#ECE8DE')
    s += rect(x, y + 12, max(h, w * value), h, h / 2, color)
    if threshold is not None:
        tx = x + w * threshold
        s += f'<line x1="{tx:.1f}" y1="{y + 6}" x2="{tx:.1f}" y2="{y + 12 + h + 6}" stroke="{INK}" stroke-width="2.5"/>'
    return s


def arrow(x1, y1, x2, y2, color=INK, sw=3, dash=None):
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{sw}" '
            f'marker-end="url(#ah)"{f" stroke-dasharray=\"{dash}\"" if dash else ""} opacity="0.75"/>')


def bubble(x, y, w, s, size=24, fill=CARD, italic=False):
    """Speech bubble sized to its text. Returns (svg, height)."""
    lines = wrap(s, size, w - 44)
    h = len(lines) * size * 1.3 + 30
    out = rect(x, y, w, h, 16, fill, LINE, 1.5)
    out += f'<path d="M{x+36},{y+h-1} l14,22 l10,-22 z" fill="{fill}" stroke="{LINE}" stroke-width="1.5"/>'
    out += f'<rect x="{x+34}" y="{y+h-4}" width="30" height="6" fill="{fill}"/>'
    out += ''.join(text(x + 22, y + 22 + size * 0.95 + i * size * 1.3, ln, size, INK, italic=italic) for i, ln in enumerate(lines))
    return out, h


def doc(x, y, w, h, fill=CARD, lines=0, line_color=LINE):
    """Page with a folded corner and optional placeholder lines."""
    f = 26
    s = (f'<path d="M{x},{y+8} q0,-8 8,-8 h{w-8-f} l{f},{f} v{h-f-8} q0,8 -8,8 h{-(w-8)} q-8,0 -8,-8 z" '
         f'fill="{fill}" stroke="{LINE}" stroke-width="1.5"/>'
         f'<path d="M{x+w-f},{y} v{f} h{f}" fill="#EFEBE2" stroke="{LINE}" stroke-width="1.5"/>')
    for i in range(lines):
        lw = w - 60 - (i * 37 % 90)
        s += rect(x + 24, y + 44 + i * 26, lw, 9, 4.5, line_color)
    return s


# ---- icons (drawn at centre cx, cy). Meanings are fixed across the set; see the legend in job-00.
def tick(cx, cy, r=24, color=OK):  # act automatically
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{color}"/>'
            f'<path d="M{cx-r*.45},{cy+r*.02} l{r*.32},{r*.32} l{r*.6},{-r*.62}" fill="none" stroke="#fff" '
            f'stroke-width="{r*.2:.1f}" stroke-linecap="round" stroke-linejoin="round"/>')


def cross(cx, cy, r=24, color=BAD):  # stop: block or don't act
    d = r * .38
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{color}"/>'
            f'<path d="M{cx-d},{cy-d} L{cx+d},{cy+d} M{cx+d},{cy-d} L{cx-d},{cy+d}" stroke="#fff" '
            f'stroke-width="{r*.2:.1f}" stroke-linecap="round"/>')


def person(cx, cy, r=24, color=WARN):  # ask a person
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{color}"/>'
            f'<circle cx="{cx}" cy="{cy-r*.28}" r="{r*.24}" fill="#fff"/>'
            f'<path d="M{cx-r*.46},{cy+r*.5} q{r*.46},{-r*.62} {r*.92},0" fill="#fff"/>')


def question(cx, cy, r=24, color=WARN):  # caveat: read the note
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{color}"/>'
            + text(cx, cy + r * .42, '?', int(r * 1.2), '#fff', True, 'middle'))


def gear(cx, cy, r=24, color=INK):  # software runs something (neutral)
    teeth = ''.join(f'<rect x="{cx-r*.16}" y="{cy-r*1.02}" width="{r*.32}" height="{r*.4}" rx="2" fill="{color}" '
                    f'transform="rotate({a} {cx} {cy})"/>' for a in range(0, 360, 45))
    return teeth + f'<circle cx="{cx}" cy="{cy}" r="{r*.72}" fill="{color}"/><circle cx="{cx}" cy="{cy}" r="{r*.3}" fill="{CARD}"/>'


def outcome(x, y, icon, label, sub=None, w=360, color=INK):
    """Icon plus label (and optional grey sub-label) for the right-hand column."""
    s = icon(x + 26, y, 26) + text(x + 66, y + 8 if not sub else y - 2, label, 25, color, True)
    if sub:
        s += text(x + 66, y + 28, sub, 20, MUTED)
    return s


def frame(num, family, title, takeaway, body, captions=('THE MATERIAL', "JEV'S ANSWER", 'YOUR SOFTWARE'),
          cols=(70, 640, 1160), score=None):
    """score: (right, total) across both test rounds, printed in the tag row so no figure reads as 100%."""
    name, accent, tint = FAMILY[family]
    tag = f'Job {num}' if isinstance(num, int) else num
    tagw = tw(tag, 24, True, display=True)
    cap = ''
    if captions:
        for x, c in zip(cols, captions):
            if c:
                c = c[0].upper() + c[1:].lower().replace('jev', 'Jev')
                cap += text(x, 229, c, 20, MUTED)
    sc = text(1530, 82, f'{score[0]} of {score[1]} examples right in our tests', 21, MUTED, anchor='end') if score else ''
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<defs>
<marker id="ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{INK}"/></marker>
</defs>
<rect width="{W}" height="{H}" fill="{BG}"/>
{text(70, 82, tag, 24, INK, True, display=True)}{text(70 + tagw + 18, 82, name, 22, MUTED) if name else ''}{sc}
{text(70, 152, title, 54, INK, True, display=True)}
{cap}
{body}
{text(70, 845, takeaway, 26, INK, False, display=True)}
</svg>'''
