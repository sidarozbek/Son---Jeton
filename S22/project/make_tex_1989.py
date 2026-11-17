#!/usr/bin/env python3
"""Scene 21's street: the street of Scenes 04 and 09, August 1989, painted with code (BGR). Original; nothing copied.
- doviz.jpg: the grocer's front is now a small exchange office: a pale front, a big window, a sign board reading
  DÖVİZ (the plain Turkish word, no brand), a rate board with blank rows, and a wall calendar reading AĞUSTOS 1989.
- cobbles.jpg, pavement.jpg: the road and the sidewalk, dry and warm in the summer evening.
(facade.jpg and groundwall.jpg are Scene 04's, kept as they are.)"""
import os

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

r = np.random.default_rng(21)
os.makedirs('tex', exist_ok=True)


def noise(h, w, s):
    n = cv2.GaussianBlur(r.normal(0, 1, (h, w)).astype(np.float32), (0, 0), s)
    return n / (n.std() + 1e-6)


def save(name, a):
    cv2.imwrite('tex/' + name, np.clip(a, 0, 255).astype(np.uint8), [cv2.IMWRITE_JPEG_QUALITY, 92])


def font(px, bold=True):
    p = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf' if bold else '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
    return ImageFont.truetype(p, px)


def text(a, xy, s, px, rgb, anchor='mm', bold=True):
    im = Image.fromarray(cv2.cvtColor(np.clip(a, 0, 255).astype(np.uint8), cv2.COLOR_BGR2RGB))
    ImageDraw.Draw(im).text(xy, s, font=font(px, bold), fill=rgb, anchor=anchor)
    a[:] = cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR)


# ---- the exchange office front: 3.2 m x 3.2 m at 220 px/m.
P = 220
h = w = int(3.2 * P)
s = np.dstack([np.full((h, w), v, np.float32) for v in (200, 214, 222)])          # Pale cream panels (BGR).
s *= (1 + noise(h, w, 20) * .03)[..., None]
cv2.rectangle(s, (0, int(.15 * P)), (w, int(.75 * P)), (60, 40, 150), -1)       # The sign board: deep red.
text(s, (w // 2, int(.45 * P)), 'DÖVİZ', int(.42 * P), (250, 238, 200))
x0, x1, y0, y1 = int(.12 * P), int(2.3 * P), int(.95 * P), int(2.55 * P)         # The window.
cv2.rectangle(s, (x0 - 10, y0 - 10), (x1 + 10, y1 + 10), (90, 96, 100), -1)
glass = np.dstack([np.full((y1 - y0, x1 - x0), v, np.float32) for v in (120, 140, 150)])
glass *= (1 + noise(y1 - y0, x1 - x0, 30) * .05)[..., None]
s[y0:y1, x0:x1] = glass
bx0, by0 = x0 + int(.18 * P), y0 + int(.2 * P)                                   # The rate board: blank rows only.
cv2.rectangle(s, (bx0, by0), (bx0 + int(1.1 * P), by0 + int(1.1 * P)), (30, 30, 30), -1)
text(s, (bx0 + int(.32 * P), by0 + int(.12 * P)), 'ALIŞ', int(.09 * P), (230, 230, 230))
text(s, (bx0 + int(.82 * P), by0 + int(.12 * P)), 'SATIŞ', int(.09 * P), (230, 230, 230))
for k in range(5):
    yy = by0 + int((.3 + k * .16) * P)
    cv2.rectangle(s, (bx0 + int(.1 * P), yy), (bx0 + int(.55 * P), yy + int(.09 * P)), (40, 160, 220), -1)
    cv2.rectangle(s, (bx0 + int(.6 * P), yy), (bx0 + int(1.0 * P), yy + int(.09 * P)), (40, 160, 220), -1)
cx0, cy0 = x0 + int(1.55 * P), y0 + int(.25 * P)                                  # The calendar, hanging inside.
cw, ch = int(.42 * P), int(.56 * P)
cv2.rectangle(s, (cx0, cy0), (cx0 + cw, cy0 + ch), (238, 240, 242), -1)
cv2.rectangle(s, (cx0, cy0), (cx0 + cw, cy0 + int(.14 * P)), (50, 50, 190), -1)
text(s, (cx0 + cw // 2, cy0 + int(.07 * P)), 'AĞUSTOS', int(.07 * P), (250, 250, 250))
text(s, (cx0 + cw // 2, cy0 + int(.33 * P)), '1989', int(.13 * P), (30, 30, 30))
dx0, dx1 = int(2.45 * P), int(3.05 * P)                                           # The glass door.
cv2.rectangle(s, (dx0, int(.95 * P)), (dx1, h), (90, 96, 100), -1)
cv2.rectangle(s, (dx0 + 10, int(1.0 * P)), (dx1 - 10, h - 6), (126, 146, 156), -1)
cv2.rectangle(s, (dx1 - 40, int(2.0 * P)), (dx1 - 26, int(2.25 * P)), (180, 180, 180), -1)
cv2.rectangle(s, (0, h - int(.12 * P)), (w, h), (110, 116, 120), -1)
save('doviz.jpg', s)

# ---- cobbles: grey-brown setts, dry, warm.
P2 = 128
h = w = 2 * P2
cb = np.dstack([np.full((h, w), v, np.float32) for v in (92, 104, 112)])
for row in range(0, h, 24):
    off = 12 if (row // 24) % 2 else 0
    for col in range(-off, w, 28):
        tone = r.uniform(.85, 1.15)
        cv2.rectangle(cb, (col + 2, row + 2), (col + 25, row + 21), tuple(float(v * tone) for v in (120, 132, 140)), -1)
cb *= (1 + noise(h, w, 1.5) * .05)[..., None]
save('cobbles.jpg', cb)

# ---- pavement: square concrete slabs, dry.
pv = np.dstack([np.full((h, w), v, np.float32) for v in (172, 184, 192)])
pv *= (1 + noise(h, w, 8) * .04)[..., None]
for k in range(0, w, 64):
    cv2.line(pv, (k, 0), (k, h), (130, 138, 144), 2)
    cv2.line(pv, (0, k), (w, k), (130, 138, 144), 2)
save('pavement.jpg', pv)
print('ok')
