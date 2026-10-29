"""Job 21: reading scanned documents (images and Box). Ground truth comes from how make_images.py drew them."""
from common import Test, top
from jev import noul, choice, box, image_asset
from make_images import build

AMOUNTS = {'a': '$4,820.00', 'b': '$1,000.00', 'c': '$3,820.00', 'd': '$3,200.00', 'none': 'None of these amounts.'}
KINDS = {'invoice': 'An invoice (a bill from a supplier), whatever its payment status.', 'purchase_order': 'A purchase order placing an order.',
         'receipt': 'A receipt confirming payment.', 'other': 'Any other document.'}


def iou(a, b):
    w = min(a['right'], b['right']) - max(a['left'], b['left'])
    h = min(a['bottom'], b['bottom']) - max(a['top'], b['top'])
    inter = max(0, w) * max(0, h)
    area = lambda x: (x['right'] - x['left']) * (x['bottom'] - x['top'])
    return inter / (area(a) + area(b) - inter)


def found(b, truth, pad=0.01):
    """Pass rule for a Box: the centre of the returned box lies inside the target (padded by 1% of the page)."""
    cx, cy = (b['left'] + b['right']) / 2, (b['top'] + b['bottom']) / 2
    return truth['left'] - pad <= cx <= truth['right'] + pad and truth['top'] - pad <= cy <= truth['bottom'] + pad


def j21():
    t = Test('J21', 'Read scanned documents: what is it, is it signed, where is the total', 'Images and Box (not a cookbook)')
    docs, examples = build()
    ex_assets = {k: image_asset(v) for k, v in examples.items()}
    stamp_opts = {k: {'description': f'A "{k}" stamp like this one.', 'example': ref} for k, (ref, _) in ex_assets.items()}
    stamp_opts['none'] = 'No stamp on the document.'
    for name, (img, truth) in docs.items():
        ref, asset = image_asset(img)
        assets = {ref: asset, **{r: a for r, a in ex_assets.values()}}
        qs = {'kind': choice('What kind of document is `scan`?', KINDS),
              'signed': noul('Has someone signed the signature line in `scan`?'),
              'stamp': choice('Which stamp, if any, is on `scan`?', stamp_opts),
              'total_pick': choice('Which amount is the total due on `scan`?', AMOUNTS),
              'over_4000': noul('Is the total due on `scan` more than $4,000?'),
              'total_box': box('the total due amount (the number, not its label) in `scan`'),
              'signature_box': box('the handwritten signature in `scan`')}
        a = t.ask({'scan': ref}, qs, assets)
        rot = truth.get('rotated', False)
        kind_want = 'purchase_order' if truth['kind'] == 'PURCHASE ORDER' else 'invoice'
        t.case(f'{name}:kind', 'edge' if rot else 'core', kind_want, {'kind': top(a['kind']), 'confidence': round(a['kind']['confidence'], 2)},
               top(a['kind']) == kind_want)
        if name in ('inv_signed', 'inv_unsigned', 'inv_void'):
            t.case(f'{name}:signed', 'core', truth['signed'], round(a['signed']['noul'], 2), (a['signed']['noul'] > 0.5) == truth['signed'])
        if name in ('inv_paid', 'inv_void', 'inv_signed'):
            want = truth['stamp'] or 'none'
            t.case(f'{name}:stamp', 'core', want, {'stamp': top(a['stamp']), 'confidence': round(a['stamp']['confidence'], 2)}, top(a['stamp']) == want)
        if name in ('inv_signed', 'inv_tiny_total', 'inv_rotated'):
            got = AMOUNTS[top(a['total_pick'])]
            t.case(f'{name}:total_pick', 'core' if name == 'inv_signed' else 'edge', truth['total'],
                   {'picked': got, 'confidence': round(a['total_pick']['confidence'], 2)}, got == truth['total'])
        if name == 'inv_signed':
            t.case('inv_signed:over_4000', 'edge', False, round(a['over_4000']['noul'], 2), a['over_4000']['noul'] < 0.5,
                   'A number comparison on an image; the subtotal $4,820.00 is a distractor.')
        if truth.get('total_box'):
            bx = a['total_box']['box']
            t.case(f'{name}:total_box', 'edge' if name == 'inv_tiny_total' else 'core', 'box centred on the total',
                   {'found': found(bx, truth['total_box']), 'iou': round(iou(bx, truth['total_box']), 2), 'confidence': a['total_box']['confidence']},
                   found(bx, truth['total_box']))
        if name == 'inv_signed':
            bx = a['signature_box']['box']
            t.case('inv_signed:signature_box', 'core', 'box centred on the signature',
                   {'found': found(bx, truth['signature_box']), 'iou': round(iou(bx, truth['signature_box']), 2),
                    'confidence': a['signature_box']['confidence']}, found(bx, truth['signature_box']))
        if name == 'inv_unsigned':
            # A Box always returns a box; code must ignore it when the presence Noul says there is nothing there.
            t.notes.append(f"Unsigned invoice: the signature Box still returned {a['signature_box']['box']} with confidence {a['signature_box']['confidence']}; only the separate yes/no question tells code to ignore it.")
    t.notes.append('Synthetic invoices drawn in code (exact truth known). One request per document with 7 questions; stamp options are defined by example images. A Box counts as found when its centre falls on the target. Images are "dreamer-ready" per TypeSafe, not production.')
    return t


TESTS = [j21]
