#!/usr/bin/env python3
"""Scene 15's harbour, mid-1980s, painted with code (BGR). An original, generic harbour; no real port is copied.
- quay.jpg: concrete quay slabs with joints and a few stains (2 m tile).
- quayface.jpg: the quay wall above the water: concrete, a dark wet band, an old tyre fender.
- sea.jpg: deep green-blue water with soft wave marks (6 m tile).
- shore.jpg: the far shore: low hazy hills, small pale houses, nothing recognisable.
- warehouse.jpg: a long warehouse front: corrugated sheeting, sliding doors numbered 3 and 4, the word ANTREPO.
- office.jpg: the harbour office's side wall: plaster, two windows, a small sign reading GÜMRÜK."""
import os

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

r = np.random.default_rng(15)
os.makedirs('tex', exist_ok=True)


def noise(h, w, s):
    n = cv2.GaussianBlur(r.normal(0, 1, (h, w)).astype(np.float32), (0, 0), s)
    return n / (n.std() + 1e-6)


def save(name, a):
    cv2.imwrite('tex/' + name, np.clip(a, 0, 255).astype(np.uint8), [cv2.IMWRITE_JPEG_QUALITY, 92])


def font(px):
    for p in ('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', '/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf'):
        if os.path.exists(p):
            return ImageFont.truetype(p, px)
    return ImageFont.load_default()


def text(a, xy, s, px, rgb, anchor='mm'):
    im = Image.fromarray(cv2.cvtColor(np.clip(a, 0, 255).astype(np.uint8), cv2.COLOR_BGR2RGB))
    ImageDraw.Draw(im).text(xy, s, font=font(px), fill=rgb, anchor=anchor)
    a[:] = cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR)


def flat(h, w, bgr):
    return np.dstack([np.full((h, w), v, np.float32) for v in bgr])


# ---- quay: 2 m of concrete slabs, joints every 1 m.
h = w = 512
a = flat(h, w, (168, 178, 184))
a *= (1 + noise(h, w, 20) * .05 + noise(h, w, 1.2) * .04)[..., None]
a *= (1 - np.clip(noise(h, w, 40) - 1.0, 0, 1) * .2)[..., None]
for k in range(3):
    cv2.line(a, (0, k * 256), (w, k * 256), (120, 128, 132), 3)
    cv2.line(a, (k * 256, 0), (k * 256, h), (120, 128, 132), 3)
save('quay.jpg', a)

# ---- quay wall: 4 m wide, 1.2 m tall (it reaches a little below the water). A yellow edge strip at the top.
h, w = 240, 800
a = flat(h, w, (150, 160, 166))
a *= (1 + noise(h, w, 8) * .06)[..., None]
wet = np.clip((np.arange(h)[:, None] - 120) / 60, 0, 1)
a = a * (1 - wet[..., None] * .55)
a[:14] = (40, 170, 214)
cv2.circle(a, (560, 100), 52, (34, 34, 36), 26)
save('quayface.jpg', a)

# ---- sea: 6 m tile.
h = w = 512
a = flat(h, w, (120, 106, 52))
a *= (1 + noise(h, w, 14) * .06)[..., None]
for _ in range(90):
    x, y = int(r.uniform(0, w)), int(r.uniform(0, h))
    L = int(r.uniform(14, 40))
    cv2.ellipse(a, (x, y), (L, 4), 0, 200, 340, (150, 140, 90), 2, cv2.LINE_AA)
save('sea.jpg', a)

# ---- far shore: 240 m x 20 m panorama.
h, w = 400, 4800
a = flat(h, w, (214, 204, 186))                       # Pale sky-haze behind the hills (mostly covered by sky colour).
xs = np.arange(w)
ridge = 230 - 70 * np.sin(xs / 700 + .4) - 40 * np.sin(xs / 230 + 1.3) - 15 * noise(1, w, 40)[0]
ridge2 = 300 - 30 * np.sin(xs / 400 + 2.0) - 10 * noise(1, w, 25)[0]
yy = np.arange(h)[:, None]
far = yy > ridge[None, :]
near = yy > ridge2[None, :]
a[far] = (176, 172, 150)
a[near] = (136, 146, 124)
for _ in range(260):
    x = int(r.uniform(0, w))
    y = int(ridge2[x] + r.uniform(4, 80))
    if y > h - 30:
        continue
    bw, bh = int(r.uniform(10, 22)), int(r.uniform(8, 16))
    col = (214, 222, 228) if r.random() < .7 else (150, 176, 206)
    cv2.rectangle(a, (x, y - bh), (x + bw, y), col, -1)
    cv2.rectangle(a, (x, y - bh - 4), (x + bw, y - bh), (90, 104, 160), -1)
a[h - 30:] = (120, 106, 60)
a[:] = cv2.GaussianBlur(a, (0, 0), 1.2)
alpha_like = np.where(far | (yy > h - 30), 1, 0)
sky = np.zeros_like(a)
sky[:] = (222, 226, 219)            # Close to the sky colour low down (config.SKY1).
a = np.where(alpha_like[..., None] > 0, a, sky)
save('shore.jpg', a[90:])                             # 310 px tall: 15.5 m.

# ---- warehouse front: 32 m x 6 m.
PX = 64
h, w = 6 * PX, 32 * PX
a = flat(h, w, (150, 156, 148))
for x in range(0, w, 10):                              # Corrugation.
    a[:, x:x + 4] *= .9
a *= (1 + noise(h, w, 12) * .04)[..., None]
a[:int(.5 * PX)] = (86, 92, 96)                        # Roof edge.
a[h - int(.4 * PX):] = (112, 118, 120)                 # Concrete base.
for k, dx in enumerate((6, 14, 22)):
    x0, x1 = dx * PX, (dx + 5) * PX
    cv2.rectangle(a, (x0, int(1.6 * PX)), (x1, h - int(.4 * PX)), (92, 104, 110), -1)
    for x in range(x0, x1, 12):
        cv2.line(a, (x, int(1.6 * PX)), (x, h - int(.4 * PX)), (78, 88, 94), 2)
    cv2.rectangle(a, (x0, int(1.6 * PX)), (x1, h - int(.4 * PX)), (50, 56, 60), 4)
    text(a, ((x0 + x1) // 2, int(1.15 * PX)), str(k + 2), int(.7 * PX), (250, 250, 250))
cv2.rectangle(a, (int(1.0 * PX), int(.75 * PX)), (int(5.0 * PX), int(1.45 * PX)), (60, 60, 150), -1)
text(a, (int(3.0 * PX), int(1.1 * PX)), 'ANTREPO', int(.5 * PX), (250, 245, 235))
save('warehouse.jpg', a)

# ---- harbour office side wall: 9 m x 4 m.
h, w = 4 * PX, 9 * PX
a = flat(h, w, (170, 196, 214))
a *= (1 + noise(h, w, 10) * .04)[..., None]
a[h - int(.5 * PX):] = (130, 140, 150)
for x0 in (int(1.2 * PX), int(5.6 * PX)):
    cv2.rectangle(a, (x0, int(1.0 * PX)), (x0 + int(1.6 * PX), int(2.6 * PX)), (100, 84, 70), -1)
    cv2.rectangle(a, (x0, int(1.0 * PX)), (x0 + int(1.6 * PX), int(2.6 * PX)), (240, 240, 236), 6)
    cv2.line(a, (x0 + int(.8 * PX), int(1.0 * PX)), (x0 + int(.8 * PX), int(2.6 * PX)), (240, 240, 236), 5)
cv2.rectangle(a, (int(3.3 * PX), int(1.3 * PX)), (int(5.1 * PX), int(1.85 * PX)), (240, 240, 240), -1)
cv2.rectangle(a, (int(3.3 * PX), int(1.3 * PX)), (int(5.1 * PX), int(1.85 * PX)), (40, 40, 40), 3)
text(a, (int(4.2 * PX), int(1.575 * PX)), 'GÜMRÜK', int(.36 * PX), (30, 30, 30))
save('office.jpg', a)
print('ok')
