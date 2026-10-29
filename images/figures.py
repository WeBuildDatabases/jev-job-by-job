"""Draws the article figures. Usage: python figures.py [00 menu 01 ...]   (no arguments = all)
Writes images/job-NN.svg and renders images/job-NN.png with headless Microsoft Edge.
Every example and score is taken from tests/results (round-1 J cases, round-2 S cases, round-3 R cases)."""
import subprocess, sys, time
from pathlib import Path
from kit import *
from figs_jobs import JOBS

OUT = Path(__file__).parent
EDGE = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
A, B, C = 70, 640, 1160  # column x positions
AW, BW, CW = 480, 440, 370
FIGS = {}


def fig(key):
    def reg(fn):
        FIGS[key] = fn
        return fn
    return reg


# ======================================================================= overview figures
@fig('00')
def hero():
    s = ''
    s += doc(A, 270, 300, 380, lines=11)
    s += text(A + 150, 690, 'a ticket, a record,', 22, MUTED, anchor='middle')
    s += text(A + 150, 718, 'a contract, a scan', 22, MUTED, anchor='middle')
    s += arrow(400, 460, 470, 460)
    blue, cyan = FAMILY['agents'][1], FAMILY['classify'][1]
    x0, y0, w, h = 490, 262, 300, 200
    for lab, cx, cy in [('Yes or no', 0, 0), ('Which one', 1, 0), ('How much', 0, 1), ('Where', 1, 1)]:
        x, y = x0 + cx * (w + 24), y0 + cy * (h + 24)
        s += card(x, y, w, h) + text(x + 22, y + 38, lab, 21, MUTED)
        if lab == 'Yes or no':  # S09: a password spelled out in words
            s += text(x + 22, y + 80, 'Exposes a password?', 21) + bar(x + 22, y + 110, w - 44, '', 0.97, blue, show=False, threshold=0.7)
            s += text(x + 22, y + 176, '0.97 yes', 26, blue, True, display=True)
        elif lab == 'Which one':  # J18: "Production cluster down…"
            s += text(x + 22, y + 80, 'Which queue?', 21)
            c1, w1 = chip(x + 22, y + 100, 'Billing', size=19, h=36)
            c2, w2 = chip(x + 22 + w1 + 8, y + 100, 'Outage', True, cyan, 19, 36)
            s += c1 + c2 + text(x + 22, y + 176, 'confidence 1.00', 26, cyan, True, display=True)
        elif lab == 'How much':  # J17: database named, 4.83 on a 1-5 scale
            s += text(x + 22, y + 80, 'How fully covered?', 21)
            tx, tw_ = x + 22, w - 44
            s += rect(tx, y + 108, tw_, 12, 6, '#ECE8DE')
            s += f'<circle cx="{tx + tw_ * (4.83 - 1) / 4:.1f}" cy="{y + 114}" r="11" fill="{FAMILY["search"][1]}"/>'
            s += text(tx, y + 160, 'not at all', 20, MUTED) + text(tx + tw_, y + 160, 'fully', 20, MUTED, anchor='end')
        else:  # J21: the total due on a scan
            s += doc(x + 22, y + 58, 120, 120, lines=4)
            s += rect(x + 36, y + 118, 82, 36, 3, 'none', BOXC, 3)
            s += text(x + 162, y + 100, 'Where is', 21) + text(x + 162, y + 128, 'the total?', 21)
    s += arrow(1150, 460, 1215, 460)
    s += text(1240, 292, 'What your rules do', 24, INK, True)
    s += outcome(1240, 345, tick, 'Act', 'sure enough')
    s += outcome(1240, 425, person, 'Ask a person', 'not sure')
    s += outcome(1240, 505, cross, 'Stop', 'block, or don\u2019t act')
    s += outcome(1240, 585, gear, 'Software runs it', 'a neutral step')
    s += outcome(1240, 665, question, 'Caveat', 'read the note')
    s += f'<line x1="1266" y1="728" x2="1266" y2="756" stroke="{INK}" stroke-width="2.5"/>' + text(1306, 750, 'your threshold on a bar', 20, MUTED)
    return frame('Overview', 'overview', 'Jev gives an answer and your software acts on it',
                 'You list the possible answers, Jev picks one and says how sure it is.', s,
                 ('THE MATERIAL', "JEV'S ANSWER, IN ONE OF FOUR SHAPES", ''), (A, 490, 1240))


@fig('menu')
def menu():
    s = ''
    for x, title, exit_ in [(A, 'Without an exit', False), (820, 'With an exit', True)]:
        s += text(x, 290, title, 30, INK, True)
        s += bubble(x, 315, 440, '\u201cback up the CRM every 15 minutes\u201d', 23)[0]
        s += text(x, 470, 'How often?', 21, MUTED)
        cx = x
        for opt in ['hourly', 'daily', 'weekly'] + (['not on the list'] if exit_ else []):
            on = (opt == 'hourly' and not exit_) or (opt == 'not on the list' and exit_)
            c, w = chip(cx, 490, opt, on, BAD if not exit_ else WARN, 21)
            s += c
            cx += w + 10
        if not exit_:
            s += outcome(x, 600, gear, 'Runs it hourly', 'confidence 0.98, wrong answer', color=BAD)
        else:
            s += outcome(x, 600, person, 'Asks the user instead', 'nothing is run')
    s += f'<line x1="780" y1="270" x2="780" y2="700" stroke="{LINE}" stroke-width="2"/>'
    s += text(70, 740, 'The same request from our tests: left from round 2 (S01), right from the round-3 replay.', 20, MUTED)
    return frame('The main weakness', 'overview', 'When the answer isn\u2019t on the menu',
                 'Jev always picks one of your options, so include a none-of-these option.', s, None)


@fig('01')
def f01():
    ac = FAMILY['agents'][1]
    s = ''
    s += bubble(A, 280, AW, '\u201cdump contacts to parquet for the last week\u201d', 22)[0]
    s += card(B, 262, BW, 236)
    for i, (lab, val) in enumerate([('action', 'export table'), ('table', 'contacts'), ('format', 'parquet'), ('since', 'last week')]):
        s += text(B + 26, 306 + i * 52, lab, 21, MUTED)
        s += chip(B + 140, 279 + i * 52, val, True, ac, 21, 38)[0]
    s += arrow(A + AW + 10, 330, B - 12, 330) + arrow(B + BW + 12, 380, C - 12, 380)
    s += outcome(C, 380, tick, 'Runs the export', 'lowest confidence 0.99')
    s += bubble(A, 560, AW, '\u201cexport the leads table as xlsx\u201d', 22)[0]
    s += card(B, 545, BW, 132, WARN)
    for i, (lab, val) in enumerate([('table', 'not on the list'), ('format', 'not on the list')]):
        s += text(B + 26, 590 + i * 54, lab, 21, MUTED)
        s += chip(B + 140, 563 + i * 54, val, True, WARN, 21, 38)[0]
    s += arrow(A + AW + 10, 605, B - 12, 605) + arrow(B + BW + 12, 620, C - 12, 620)
    s += outcome(C, 620, person, 'Asks the user', 'nothing is run')
    s += text(B, 718, 'Before the fix it exported contacts as CSV, at 0.89.', 20, BAD)
    s += text(B, 746, 'With the fix, 13 of 14 right in a replay run after the locked round.', 20, MUTED)
    return frame(1, 'agents', 'Turn a request into the right action',
                 'Each list of options needs a not-on-the-list choice.', s, score=(11, 14))


FIGS.update(JOBS)

if __name__ == '__main__':
    keys = sys.argv[1:] or list(FIGS)
    for k in keys:
        name = f'job-{k}' if k.isdigit() else f'fig-{k}'
        svg = OUT / f'{name}.svg'
        svg.write_text(FIGS[k](), encoding='utf-8')
        png = OUT / (name + '.png')
        for attempt in range(4):  # ponytail: Edge occasionally hands off to a closing instance and writes nothing; check and retry
            subprocess.run([EDGE, '--headless=new', f'--user-data-dir={OUT / ".edge-profile"}', '--no-first-run',
                            '--disable-gpu', '--hide-scrollbars', '--force-device-scale-factor=1',
                            f'--screenshot={png}', f'--window-size={W},{H}', svg.as_uri()],
                           check=True, capture_output=True)
            time.sleep(0.5)
            if png.exists() and png.stat().st_mtime >= svg.stat().st_mtime:
                break
        else:
            raise SystemExit(f'{name}: PNG did not refresh')
        print('drew', name, f'(try {attempt + 1})' if attempt else '')
