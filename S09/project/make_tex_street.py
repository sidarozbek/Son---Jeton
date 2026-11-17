#!/usr/bin/env python3
"""Scene 04's street, January 1980, painted with code (BGR). An original street; nothing copied.
- facade.jpg: upper floors of plain post-war apartment blocks (ochre and cream plaster, tall windows, some lit).
- groundwall.jpg: ground-floor plaster with a grey rendered base.
- shopfront.jpg: an original corner grocer: a painted wooden front, a shop window with shelves, a glass door,
  a sign board reading BAKKAL (the plain Turkish word, no brand).
- calendar.jpg: a tear-off wall calendar page: OCAK / 24 / 1980 / PERŞEMBE (24 January 1980 was a Thursday).
- cobbles.jpg, pavement.jpg: the road and the sidewalk, with a little snow in the joints."""
import os
import sys

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

r = np.random.default_rng(41)
os.makedirs('tex', exist_ok=True)


def noise(h, w, s):
    n = cv2.GaussianBlur(r.normal(0, 1, (h, w)).astype(np.float32), (0, 0), s)
    return n / (n.std() + 1e-6)


def save(name, a):
    cv2.imwrite('tex/' + name, np.clip(a, 0, 255).astype(np.uint8), [cv2.IMWRITE_JPEG_QUALITY, 92])


def font(px, bold=True):
    for p in ('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf' if bold else '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
              '/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf'):
        if os.path.exists(p):
            return ImageFont.truetype(p, px)
    return ImageFont.load_default()


def text(a, xy, s, px, rgb, anchor='mm', bold=True):
    """Draw text on a BGR array with PIL (Turkish letters need a real font)."""
    im = Image.fromarray(cv2.cvtColor(np.clip(a, 0, 255).astype(np.uint8), cv2.COLOR_BGR2RGB))
    ImageDraw.Draw(im).text(xy, s, font=font(px, bold), fill=rgb, anchor=anchor)
    a[:] = cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR)


PX = 160   # pixels per metre for the big surfaces

# ---- facade: one 4 m bay of the upper floors, 8.8 m tall (floors at 2.9 m), tiles along the street.
h, w = int(8.8 * PX), int(4 * PX)
a = np.dstack([np.full((h, w), v, np.float32) for v in (126, 168, 196)])       # Ochre plaster (BGR).
a *= (1 + noise(h, w, 30) * .05 + noise(h, w, 1.5) * .03)[..., None]
stain = np.clip(noise(h, w, 60) - .6, 0, 1)[..., None]
a = a * (1 - stain * .25)
fl = int(2.9 * PX)
for k in range(3):
    y0 = h - (k + 1) * fl
    cv2.rectangle(a, (0, y0 + fl - 14), (w, y0 + fl), (110, 140, 160), -1)        # Floor band.
    for wx in (int(.55 * PX), int(2.45 * PX)):
        x0, x1 = wx, wx + int(1.0 * PX)
        wy0, wy1 = y0 + int(.75 * PX), y0 + int(2.25 * PX)
        lit = r.random() < .45
        glass = (96, 160, 214) if lit else (70, 56, 50)                         # Warm lit or dark (BGR).
        cv2.rectangle(a, (x0 - 8, wy0 - 8), (x1 + 8, wy1 + 14), (200, 214, 222), -1)   # Frame and sill.
        cv2.rectangle(a, (x0, wy0), (x1, wy1), glass, -1)
        if lit:                                                                  # A curtain half drawn.
            cv2.rectangle(a, (x0, wy0), (x0 + int(.35 * PX), wy1), (70, 120, 180), -1)
        cv2.line(a, ((x0 + x1) // 2, wy0), ((x0 + x1) // 2, wy1), (180, 190, 196), 5)
        cv2.line(a, (x0, wy0 + int(.45 * PX)), (x1, wy0 + int(.45 * PX)), (180, 190, 196), 5)
cv2.rectangle(a, (0, 0), (w, 18), (96, 110, 120), -1)                              # Roof edge.
save('facade.jpg', a)

# ---- ground-floor wall: plaster over a grey rendered base, a drainpipe at one edge.
h, w = int(3.2 * PX), int(4 * PX)
g = np.dstack([np.full((h, w), v, np.float32) for v in (150, 184, 204)])
g *= (1 + noise(h, w, 25) * .05 + noise(h, w, 1.5) * .03)[..., None]
cv2.rectangle(g, (0, h - int(.7 * PX)), (w, h), (112, 118, 122), -1)
g[h - int(.7 * PX):] *= (1 + noise(int(.7 * PX), w, 2) * .06)[..., None]
cv2.rectangle(g, (w - 30, 0), (w - 12, h), (80, 88, 92), -1)
save('groundwall.jpg', g)

# ---- the grocer's front: 3.2 m wide, 3.2 m tall, at 220 px/m.
SP = 220
h, w = int(3.2 * SP), int(3.2 * SP)
s = np.dstack([np.full((h, w), v, np.float32) for v in (72, 96, 52)])           # Painted dark green wood.
s *= (1 + noise(h, w, 1.2) * .04)[..., None]
# Sign board across the top.
cv2.rectangle(s, (20, 18), (w - 20, int(.62 * SP)), (120, 64, 30), -1)          # Deep blue board.
cv2.rectangle(s, (20, 18), (w - 20, int(.62 * SP)), (40, 30, 20), 6)
text(s, (w // 2, int(.34 * SP)), 'BAKKAL', int(.36 * SP), (246, 238, 214))
# Shop window: x .12..2.3 m, y .95..2.45 m from the floor (image y measured from the top).
def yy(m):
    return h - int(m * SP)
wx0, wx1 = int(.12 * SP), int(2.3 * SP)
cv2.rectangle(s, (wx0, yy(2.45)), (wx1, yy(.95)), (110, 190, 236), -1)            # Warm lit interior (BGR).
glow = np.zeros((h, w), np.float32)
cv2.rectangle(glow, (wx0, yy(2.45)), (wx1, yy(.95)), 1, -1)
glow = cv2.GaussianBlur(glow, (0, 0), 30)
# Shelves with goods: jars, tins, packets, as blocks of colour.
for k, sy in enumerate((2.2, 1.8, 1.45)):
    cv2.rectangle(s, (wx0, yy(sy)), (wx1, yy(sy) + 8), (60, 90, 120), -1)
    x = wx0 + 12
    while x < wx1 - 30:
        cw = int(r.integers(18, 40))
        ch = int(r.integers(28, 70))
        col = [(60, 70, 190), (40, 150, 220), (200, 200, 190), (60, 140, 80), (40, 90, 200), (180, 120, 60)][int(r.integers(0, 6))]
        cv2.rectangle(s, (x, yy(sy) - ch), (x + cw, yy(sy)), col, -1)
        cv2.rectangle(s, (x, yy(sy) - ch), (x + cw, yy(sy)), (40, 50, 60), 2)
        x += cw + int(r.integers(4, 10))
# Sacks and a scale on the counter at the bottom of the window.
cv2.rectangle(s, (wx0, yy(1.2)), (wx1, yy(.95)), (60, 100, 140), -1)
for x in range(wx0 + 30, wx1 - 60, 110):
    cv2.ellipse(s, (x + 40, yy(1.2)), (42, 50), 0, 180, 360, (150, 196, 214), -1)
# Window frame and glazing bars.
cv2.rectangle(s, (wx0, yy(2.45)), (wx1, yy(.95)), (40, 56, 30), 12)
cv2.line(s, ((wx0 + wx1) // 2, yy(2.45)), ((wx0 + wx1) // 2, yy(.95)), (40, 56, 30), 8)
# The door: x 2.45..3.08 m, up to 2.55 m, with a glass upper half.
dx0, dx1 = int(2.45 * SP), int(3.08 * SP)
cv2.rectangle(s, (dx0, yy(2.55)), (dx1, h), (52, 74, 38), -1)
cv2.rectangle(s, (dx0 + 14, yy(2.45)), (dx1 - 14, yy(1.3)), (100, 170, 214), -1)
cv2.rectangle(s, (dx0, yy(2.55)), (dx1, h), (30, 42, 22), 6)
cv2.circle(s, (dx0 + 22, yy(1.1)), 9, (120, 170, 190), -1)
s = s * (1 + glow[..., None] * .0)
save('shopfront.jpg', s)

# ---- the tear-off calendar page, 0.40 x 0.52 m, at 1500 px/m: red header, a big black 24, the year, the weekday.
cw_, ch_ = 600, 780
c = np.full((ch_, cw_, 3), (226, 240, 246), np.float32)
c *= (1 + noise(ch_, cw_, 1.5) * .015)[..., None]
cv2.rectangle(c, (0, 0), (cw_, 150), (40, 40, 196), -1)                          # Red header (BGR).
text(c, (cw_ // 2, 78), 'OCAK', 104, (255, 248, 236))
text(c, (cw_ // 2, 360), '24', 300, (24, 22, 22))
text(c, (cw_ // 2, 575), '1980', 96, (196, 40, 40))
text(c, (cw_ // 2, 690), 'PERŞEMBE', 70, (24, 22, 22))
for x in range(30, cw_ - 20, 44):                                               # The torn stubs of earlier pages.
    cv2.circle(c, (x, 8), 7, (180, 190, 200), -1)
cv2.rectangle(c, (0, 0), (cw_ - 1, ch_ - 1), (120, 130, 140), 4)
save('calendar.jpg', c)

# ---- cobbles: grey-brown setts in rows, a dusting of snow in the joints.
N = 768
cb = np.dstack([np.full((N, N), v, np.float32) for v in (62, 68, 74)])
mortar = np.zeros((N, N), np.float32)
row_h = N // 12
for j in range(12):
    off = (j % 2) * 30
    y0 = j * row_h
    x = -off
    while x < N:
        bw = int(r.integers(52, 72))
        shade = float(r.normal(1, .1))
        cv2.rectangle(cb, (x + 3, y0 + 3), (x + bw - 3, y0 + row_h - 3), tuple(v * shade for v in (70, 78, 86)), -1)
        cv2.rectangle(mortar, (x, y0), (x + bw, y0 + row_h), 1, 4)
        x += bw
cb *= (1 + noise(N, N, 1.2) * .06)[..., None]
snow = np.clip(mortar * (noise(N, N, 12) * .5 + .7), 0, 1)[..., None]
cb = cb * (1 - snow * .35) + np.array((90, 96, 100), np.float32) * snow * .35          # Scene 09: no snow, dust in the joints.
save('cobbles.jpg', cb)

# ---- pavement: square concrete slabs, wet and grey, snow in the cracks and along the edges.
pv = np.dstack([np.full((N, N), v, np.float32) for v in (128, 132, 134)])
pv *= (1 + noise(N, N, 40) * .06 + noise(N, N, 1.5) * .04)[..., None]
m = np.zeros((N, N), np.float32)
for i in range(0, N, N // 3):
    cv2.line(m, (i, 0), (i, N), 1, 5)
    cv2.line(m, (0, i), (N, i), 1, 5)
m = np.clip(m + np.clip(noise(N, N, 18) - 1.3, 0, 1), 0, 1)[..., None]
pv = pv * (1 - m * .5) + np.array((96, 100, 102), np.float32) * m * .5               # Scene 09: no snow.
save('pavement.jpg', pv)
# ---- Scene 09: the grocer's front with its metal shutter rolled down (the sign board stays), 3.2 x 3.2 m.
sh = cv2.imread('tex/shopfront.jpg').astype(np.float32)
H_, W_ = sh.shape[:2]
y0 = int(.64 * SP)
sh[y0:, :] = (150, 150, 146)
for y in range(y0, H_, 16):
    cv2.line(sh, (0, y), (W_, y), (112, 112, 108), 4)
    cv2.line(sh, (0, y + 3), (W_, y + 3), (176, 176, 172), 2)
sh[y0:] *= (1 + noise(H_ - y0, W_, 1.2) * .03)[..., None]
cv2.rectangle(sh, (0, y0), (W_, y0 + 18), (70, 74, 76), -1)
cv2.rectangle(sh, (W_ // 2 - 40, H_ - 40), (W_ // 2 + 40, H_ - 24), (60, 60, 60), -1)   # The padlocked handle.
save('shutter.jpg', sh)
print('street textures done')
