"""Draws the synthetic scanned documents for the image test. Ground truth is known by construction.

Every document is fictional. Returns {name: (PIL image, truth dict)}; boxes are fractions of width/height.
"""
from PIL import Image, ImageDraw, ImageFont

FONT = 'C:/Windows/Fonts/arial.ttf'
BOLD = 'C:/Windows/Fonts/arialbd.ttf'
W, H = 1100, 1400


def f(size, bold=False):
    return ImageFont.truetype(BOLD if bold else FONT, size)


def frac(b, w=W, h=H):
    l, t, r, bt = b
    return {'left': l / w, 'top': t / h, 'right': r / w, 'bottom': bt / h}


def signature(d, x, y):
    pts = [(x, y + 30), (x + 25, y), (x + 45, y + 40), (x + 70, y + 5), (x + 95, y + 45), (x + 120, y + 10),
           (x + 150, y + 38), (x + 185, y + 15), (x + 215, y + 30)]
    d.line(pts, fill=(20, 30, 120), width=4, joint='curve')
    d.line([(x + 10, y + 52), (x + 205, y + 48)], fill=(20, 30, 120), width=3)
    return (x - 5, y - 5, x + 220, y + 60)


def stamp(d, text, x, y, colour):
    box = d.textbbox((x + 18, y + 10), text, font=f(46, True))
    outer = (x, y, box[2] + 18, box[3] + 14)
    d.rectangle(outer, outline=colour, width=6)
    d.text((x + 18, y + 10), text, font=f(46, True), fill=colour)
    return outer


def document(kind='INVOICE', total='$3,820.00', signed=True, stamp_text=None, total_size=30):
    img = Image.new('RGB', (W, H), 'white')
    d = ImageDraw.Draw(img)
    d.text((80, 70), 'Halvorsen Data Supply Ltd.', font=f(34, True), fill='black')
    d.text((80, 118), '14 Quarry Lane, Leeds LS2 9JT', font=f(22), fill=(60, 60, 60))
    d.text((760, 70), kind, font=f(48, True), fill=(30, 30, 30))
    d.text((760, 135), 'No. HD-20431', font=f(24), fill='black')
    d.text((760, 168), 'Date: 3 March 2026', font=f(24), fill='black')
    po = kind == 'PURCHASE ORDER'
    d.text((80, 230), ('Ordered by' if po else 'Bill to') + ': Corvid Analytics, 88 Mill Road, Cambridge', font=f(24), fill='black')
    y = 320
    d.line([(80, y), (1020, y)], fill='black', width=2)
    d.text((90, y + 12), 'Item', font=f(24, True), fill='black')
    d.text((780, y + 12), 'Amount', font=f(24, True), fill='black')
    rows = [('Database migration workshop (2 days)', '$3,200.00'), ('Schema review, 12 tables', '$1,140.00'),
            ('Travel', '$480.00')]
    for i, (item, amt) in enumerate(rows):
        yy = y + 60 + i * 50
        d.text((90, yy), item, font=f(24), fill='black')
        d.text((780, yy), amt, font=f(24), fill='black')
    yy = y + 60 + len(rows) * 50 + 20
    d.line([(80, yy), (1020, yy)], fill='black', width=2)
    d.text((90, yy + 20), 'Subtotal', font=f(24), fill='black')
    d.text((780, yy + 20), '$4,820.00', font=f(24), fill='black')
    if not po:
        d.text((90, yy + 60), 'Deposit paid', font=f(24), fill='black')
        d.text((780, yy + 60), '-$1,000.00', font=f(24), fill='black')
    label = (90, yy + 115)
    d.text(label, 'ORDER TOTAL' if po else 'TOTAL DUE', font=f(total_size, True), fill='black')
    tb = d.textbbox((780, yy + 115), total, font=f(total_size, True))
    d.text((780, yy + 115), total, font=f(total_size, True), fill='black')
    truth = {'total_box': frac((tb[0] - 4, tb[1] - 4, tb[2] + 4, tb[3] + 4)), 'total': total}
    d.text((80, 1150), 'Authorised signature:', font=f(22), fill='black')
    d.line([(330, 1210), (640, 1210)], fill=(150, 150, 150), width=1)
    if signed:
        truth['signature_box'] = frac(signature(d, 360, 1145))
    if stamp_text:
        truth['stamp_box'] = frac(stamp(d, stamp_text, 700, 1100, (200, 30, 30) if stamp_text != 'PAID' else (20, 140, 40)))
    truth.update(kind=kind, signed=signed, stamp=stamp_text)
    return img, truth


def stamp_example(text, colour):
    img = Image.new('RGB', (420, 300), 'white')
    stamp(ImageDraw.Draw(img), text, 40, 100, colour)
    return img


def build():
    docs = {
        'inv_signed': document(),
        'inv_unsigned': document(signed=False),
        'po_signed': document(kind='PURCHASE ORDER', total='$4,820.00'),
        'inv_paid': document(total='$3,820.00', stamp_text='PAID'),
        'inv_void': document(total='$3,820.00', stamp_text='VOID', signed=False),
        'inv_tiny_total': document(total='$3,820.00', total_size=14),
    }
    img, truth = document(total='$3,820.00')
    rotated = img.rotate(90, expand=True)  # a sideways scan; boxes not scored on this one
    docs['inv_rotated'] = (rotated, {**truth, 'total_box': None, 'signature_box': None, 'rotated': True})
    examples = {'PAID': stamp_example('PAID', (20, 140, 40)), 'VOID': stamp_example('VOID', (200, 30, 30)),
                'DRAFT': stamp_example('DRAFT', (90, 90, 90))}
    return docs, examples


if __name__ == '__main__':
    from pathlib import Path
    out = Path(__file__).parent / 'images'
    out.mkdir(exist_ok=True)
    docs, examples = build()
    for name, (img, _) in {**docs, **{f'stamp_{k}': (v, None) for k, v in examples.items()}}.items():
        img.save(out / f'{name}.png')
    print('wrote', len(docs) + len(examples), 'images to', out)
