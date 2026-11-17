#!/usr/bin/env python3
"""Scene 05: inside the grocer's, painted with code (BGR). An original shop; no brands, no real labels.
- shelves.jpg: the back wall of shelves, 5 m x 2.8 m, packed with jars, tins, packets and bottles as blocks of colour.
- shopwall.jpg: side walls, pale green oil paint over a darker dado.
- shopfloor.jpg: worn red and cream floor tiles.
- shopfront_in.jpg: the front wall from inside: the shop window onto the blue street, the glass door, the bell.
- card_<price>.jpg: the cardboard price cards, hand lettered in black on white. Prices are invented."""
import os

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

import room as R

r = np.random.default_rng(55)
os.makedirs('tex', exist_ok=True)


def noise(h, w, s):
    n = cv2.GaussianBlur(r.normal(0, 1, (h, w)).astype(np.float32), (0, 0), s)
    return n / (n.std() + 1e-6)


def save(name, a):
    cv2.imwrite('tex/' + name, np.clip(a, 0, 255).astype(np.uint8), [cv2.IMWRITE_JPEG_QUALITY, 92])


def text(a, xy, s, px, rgb):
    f = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
    im = Image.fromarray(cv2.cvtColor(np.clip(a, 0, 255).astype(np.uint8), cv2.COLOR_BGR2RGB))
    ImageDraw.Draw(im).text(xy, s, font=ImageFont.truetype(f, px), fill=rgb, anchor='mm')
    a[:] = cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR)


PX = 200
GOODS = [(60, 70, 190), (40, 150, 220), (200, 200, 190), (60, 140, 80), (40, 90, 200), (180, 120, 60), (90, 60, 140), (30, 190, 230)]

# ---- the back wall of shelves
h, w = int(R.H * PX), int(R.W * PX)
a = np.dstack([np.full((h, w), v, np.float32) for v in (60, 84, 112)])          # Dark wood behind the goods.
a *= (1 + noise(h, w, 1.5) * .05)[..., None]
for z in R.SHELF_Z:
    y = h - int(z * PX)
    x = 6
    top = h - int((z + .42) * PX)
    while x < w - 20:
        cw = int(r.integers(16, 46))
        ch = int(r.integers(30, int(.38 * PX)))
        col = GOODS[int(r.integers(0, len(GOODS)))]
        kind = r.random()
        if kind < .3:                                                        # A jar with a lid.
            cv2.rectangle(a, (x, y - ch), (x + cw, y), tuple(c * .9 for c in col), -1)
            cv2.rectangle(a, (x - 2, y - ch - 8), (x + cw + 2, y - ch), (40, 40, 44), -1)
        elif kind < .55:                                                     # A tin with a band.
            cv2.rectangle(a, (x, y - ch), (x + cw, y), (170, 176, 180), -1)
            cv2.rectangle(a, (x, y - ch * 2 // 3), (x + cw, y - ch // 3), col, -1)
        elif kind < .8:                                                      # A packet.
            cv2.rectangle(a, (x, y - ch), (x + cw, y), col, -1)
            cv2.rectangle(a, (x + 4, y - ch + 6), (x + cw - 4, y - ch + 14), (230, 230, 220), -1)
        else:                                                                # A bottle.
            cv2.rectangle(a, (x + cw // 4, y - ch), (x + cw * 3 // 4, y), (40, 90, 40), -1)
            cv2.rectangle(a, (x + cw // 3, y - ch - 14), (x + cw * 2 // 3, y - ch), (40, 90, 40), -1)
        cv2.rectangle(a, (x, y - ch), (x + cw, y), (30, 36, 44), 2)
        x += cw + int(r.integers(3, 9))
    cv2.rectangle(a, (0, y), (w, y + 14), (70, 100, 136), -1)                    # The shelf board.
    cv2.line(a, (0, y + 14), (w, y + 14), (40, 56, 76), 3)
save('shelves.jpg', a)

# ---- side walls
h, w = int(R.H * PX), int(3 * PX)
s = np.dstack([np.full((h, w), v, np.float32) for v in (176, 196, 168)])        # Pale green oil paint.
s *= (1 + noise(h, w, 30) * .04 + noise(h, w, 1.5) * .02)[..., None]
cv2.rectangle(s, (0, h - int(1.1 * PX)), (w, h), (100, 120, 96), -1)
cv2.line(s, (0, h - int(1.1 * PX)), (w, h - int(1.1 * PX)), (60, 76, 60), 6)
save('shopwall.jpg', s)

# ---- floor tiles
N = 512
f = np.zeros((N, N, 3), np.float32)
t = N // 8
for i in range(8):
    for j in range(8):
        col = (60, 70, 150) if (i + j) % 2 == 0 else (190, 206, 214)
        cv2.rectangle(f, (i * t, j * t), (i * t + t, j * t + t), col, -1)
f *= (1 + noise(N, N, 25) * .06 + noise(N, N, 1.2) * .04)[..., None]
wear = np.clip(noise(N, N, 60) - .7, 0, 1)[..., None]
f = f * (1 - wear * .3) + np.array((120, 130, 136), np.float32) * wear * .3
save('shopfloor.jpg', f)

# ---- the front wall from inside: window onto the blue street, the door with its bell
h, w = int(R.H * PX), int(R.W * PX)
fr = np.dstack([np.full((h, w), v, np.float32) for v in (176, 196, 168)])
cv2.rectangle(fr, (0, h - int(1.1 * PX)), (w, h), (100, 120, 96), -1)
x0, x1, z0, z1 = int(.4 * PX), int(3.2 * PX), int(.95 * PX), int(2.45 * PX)
sky = np.linspace(1, 0, z1 - z0)[:, None]
fr[h - z1:h - z0, x0:x1] = (np.array((120, 84, 52)) * sky[..., None] + np.array((150, 110, 80)) * (1 - sky[..., None]))
cv2.rectangle(fr, (x0, h - z1), (x1, h - z0), (40, 56, 30), 12)
cv2.line(fr, ((x0 + x1) // 2, h - z1), ((x0 + x1) // 2, h - z0), (40, 56, 30), 8)
dx0, dx1 = int(3.6 * PX), int(4.5 * PX)
cv2.rectangle(fr, (dx0, h - int(2.3 * PX)), (dx1, h), (52, 74, 38), -1)
cv2.rectangle(fr, (dx0 + 16, h - int(2.2 * PX)), (dx1 - 16, h - int(1.2 * PX)), (130, 92, 60), -1)
cv2.circle(fr, ((dx0 + dx1) // 2, h - int(2.42 * PX)), 12, (60, 170, 210), -1)   # The bell.
save('shopfront_in.jpg', fr)

# ---- the price cards: hand lettered, a little uneven
for x, z, old, new in R.CARDS:
    for p in (old, new):
        c = np.full((130, 200, 3), (232, 240, 244), np.float32)
        c *= (1 + noise(130, 200, 1.5) * .02)[..., None]
        cv2.rectangle(c, (0, 0), (199, 129), (150, 160, 170), 3)
        text(c, (100, 68), p, 84 if len(p) < 3 else 70, (20, 20, 24))
        save(f'card_{p}.jpg', c)
for x, z, p in R.EXTRA:
    c = np.full((130, 200, 3), (232, 240, 244), np.float32)
    c *= (1 + noise(130, 200, 1.5) * .02)[..., None]
    cv2.rectangle(c, (0, 0), (199, 129), (150, 160, 170), 3)
    text(c, (100, 68), p, 84 if len(p) < 3 else 70, (20, 20, 24))
    save(f'card_{p}.jpg', c)

# ---- Scene 06: a plain wall clock face (no brand): white dial, black ticks, a red rim.
k = np.full((400, 400, 3), (236, 242, 244), np.float32)
cv2.circle(k, (200, 200), 196, (40, 40, 160), 10)
for i in range(60):
    a = i / 60 * 2 * np.pi
    r0 = 160 if i % 5 else 140
    cv2.line(k, (int(200 + r0 * np.sin(a)), int(200 - r0 * np.cos(a))), (int(200 + 182 * np.sin(a)), int(200 - 182 * np.cos(a))), (30, 30, 30), 8 if i % 5 == 0 else 3)
mask = np.zeros((400, 400), np.uint8)
cv2.circle(mask, (200, 200), 200, 255, -1)
k[mask == 0] = (176, 196, 168)
k = cv2.GaussianBlur(k, (0, 0), 1.2)
save('clock.jpg', k)
print('shop textures done')
