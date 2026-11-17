#!/usr/bin/env python3
"""Scene 10 on: the office of the imaginary "Kuş Bankerlik", 1982, painted with code (BGR). An original design: the
name is the story plan's invention, the bird mark is drawn here, nothing copies a real banker's office.
- bk_wall.jpg: cream walls over dark wood panelling.  - bk_floor.jpg: beige terrazzo.
- bk_back.jpg: the back wall: the wooden partition with the barred teller window (gişe), the sign with the bird mark.
- rate_<n>.jpg: the interest board's number cards (%30 to %90); the board flips between them."""
import os

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

import room as R

r = np.random.default_rng(71)
os.makedirs('tex', exist_ok=True)
BOLD = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
SERIF_B = '/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf'


def noise(h, w, s):
    n = cv2.GaussianBlur(r.normal(0, 1, (h, w)).astype(np.float32), (0, 0), s)
    return n / (n.std() + 1e-6)


def save(name, a):
    cv2.imwrite('tex/' + name, np.clip(a, 0, 255).astype(np.uint8), [cv2.IMWRITE_JPEG_QUALITY, 92])


def text(a, xy, s, font, px, rgb, anchor='mm'):
    im = Image.fromarray(cv2.cvtColor(np.clip(a, 0, 255).astype(np.uint8), cv2.COLOR_BGR2RGB))
    ImageDraw.Draw(im).text(xy, s, font=ImageFont.truetype(font, px), fill=rgb, anchor=anchor)
    a[:] = cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR)


def bird(a, cx, cy, s, col):
    """The bank's mark: a simple flying bird, two curved wings and a body. Original."""
    pts = [(-1.0, -.1), (-.55, -.45), (-.15, -.1), (0, -.05), (.15, -.1), (.55, -.45), (1.0, -.1), (.5, -.25), (.1, .15), (0, .3), (-.1, .15), (-.5, -.25)]
    poly = np.array([(cx + x * s, cy + y * s) for x, y in pts], np.int32)
    cv2.fillPoly(a, [poly], col, cv2.LINE_AA)


PX = 200
# ---- walls: cream plaster over a dark wood dado with a rail.
h, w = int(R.H * PX), int(3 * PX)
wl = np.dstack([np.full((h, w), v, np.float32) for v in (190, 214, 226)])
wl *= (1 + noise(h, w, 30) * .04 + noise(h, w, 1.5) * .02)[..., None]
d = int(1.0 * PX)
wl[h - d:] = (50, 70, 96)
for x in range(0, w, int(.4 * PX)):
    cv2.line(wl, (x, h - d), (x, h), (36, 50, 70), 3)
wl[h - d:] *= (1 + noise(d, w, 1.2) * .05)[..., None]
cv2.rectangle(wl, (0, h - d - 10), (w, h - d + 4), (40, 58, 80), -1)
save('bk_wall.jpg', wl)

# ---- floor: beige terrazzo.
N = 512
f = np.dstack([np.full((N, N), v, np.float32) for v in (168, 186, 196)])
f *= (1 + noise(N, N, 30) * .04)[..., None]
for _ in range(2500):
    x, y = r.integers(0, N, 2)
    cv2.circle(f, (int(x), int(y)), int(r.integers(1, 4)), tuple(float(c) for c in r.choice([(120, 130, 140), (210, 220, 226), (90, 110, 140)])), -1)
for i in range(0, N, N // 2):
    cv2.line(f, (i, 0), (i, N), (130, 140, 146), 2)
    cv2.line(f, (0, i), (N, i), (130, 140, 146), 2)
save('bk_floor.jpg', f)

# ---- the back wall (6 m x 3 m): the wooden partition, the barred window, the sign with the bird mark.
h, w = int(R.H * PX), int(R.W * PX)
b = np.dstack([np.full((h, w), v, np.float32) for v in (190, 214, 226)])
b *= (1 + noise(h, w, 30) * .04)[..., None]
def X(m):
    return int(m * PX)
def Y(m):
    return h - int(m * PX)
# Partition: dark polished wood from the floor to 2.0 m, with panels.
cv2.rectangle(b, (X(1.2), Y(2.0)), (X(4.8), h), (40, 62, 92), -1)
for x0 in (1.3, 2.0, 3.7, 4.2):
    cv2.rectangle(b, (X(x0), Y(.9)), (X(x0 + .45), Y(.15)), (54, 80, 112), 4)
# The teller window: x 2.6-3.4, 1.0-1.75 m; dark inside, brass bars, a slot at the sill.
x0, x1 = R.WINDOW
cv2.rectangle(b, (X(x0), Y(1.75)), (X(x1), Y(1.0)), (30, 36, 40), -1)
cv2.rectangle(b, (X(x0), Y(1.75)), (X(x1), Y(1.0)), (60, 150, 190), 6)
for x in np.linspace(x0 + .08, x1 - .08, 7):
    cv2.line(b, (X(x), Y(1.75)), (X(x), Y(1.12)), (70, 160, 200), 5)
cv2.rectangle(b, (X(x0 + .25), Y(1.06)), (X(x1 - .25), Y(1.0)), (14, 14, 16), -1)
# The sign over the partition.
cv2.rectangle(b, (X(1.4), Y(2.65)), (X(4.6), Y(2.12)), (40, 40, 140), -1)          # Deep red board (BGR).
cv2.rectangle(b, (X(1.4), Y(2.65)), (X(4.6), Y(2.12)), (60, 160, 210), 6)
bird(b, X(1.72), Y(2.39), 44, (80, 200, 236))
text(b, (X(3.2), Y(2.385)), 'KUŞ BANKERLİK', SERIF_B, int(.25 * PX), (240, 210, 120))
# The interest board's frame on the right: FAİZ over an empty slot (the number cards sit in front of it).
bx0, bx1, bz0, bz1 = R.BOARD
cv2.rectangle(b, (X(bx0), Y(bz1)), (X(bx1), Y(bz0)), (24, 26, 30), -1)
cv2.rectangle(b, (X(bx0), Y(bz1)), (X(bx1), Y(bz0)), (60, 160, 210), 5)
text(b, ((X(bx0) + X(bx1)) // 2, Y(bz1 - .12)), 'FAİZ', BOLD, int(.16 * PX), (240, 220, 140))
save('bk_back.jpg', b)

# ---- the interest number cards: white-on-black flip numerals.
for n in R.RATES:
    c = np.full((260, 420, 3), (22, 24, 28), np.float32)
    cv2.line(c, (0, 130), (420, 130), (60, 60, 64), 3)
    text(c, (210, 136), f'%{n}', BOLD, 140, (250, 246, 236))
    save(f'rate_{n}.jpg', c)
# ---- Scene 12: the chalkboard. Months along the bottom; new customers needed up the side, doubling each month;
# a dashed line for everyone there is to recruit; where the bars cross it, an X and "burada biter". Chalk on green.
cb = np.dstack([np.full((540, 720), v, np.float32) for v in (52, 74, 44)])
cb *= (1 + noise(540, 720, 20) * .06 + noise(540, 720, 1.2) * .04)[..., None]
CH = (226, 232, 232)
cv2.line(cb, (70, 470), (680, 470), CH, 4)
cv2.line(cb, (70, 470), (70, 40), CH, 4)
for i in range(8):
    x = 100 + i * 72
    hgt = 6 * 2 ** i
    top = max(470 - hgt, 30)
    cv2.rectangle(cb, (x, top), (x + 40, 470), CH, 3)
    text(cb, (x + 20, 495), str(i + 1), BOLD, 24, (232, 232, 226))
for x in range(70, 680, 30):
    cv2.line(cb, (x, 150), (x + 16, 150), CH, 3)
text(cb, (180, 128), 'herkes', BOLD, 30, (232, 232, 226))
cv2.line(cb, (527, 125), (577, 175), (90, 120, 230), 6)
cv2.line(cb, (577, 125), (527, 175), (90, 120, 230), 6)
text(cb, (430, 60), 'burada biter', BOLD, 28, (220, 230, 240))
cv2.arrowedLine(cb, (470, 75), (535, 125), (220, 230, 240), 3, tipLength=.2)
text(cb, (150, 30), 'yeni müşteri', BOLD, 26, (232, 232, 226))
text(cb, (690, 455), 'ay', BOLD, 24, (232, 232, 226))
cb[:12] = cb[-12:] = (60, 90, 120)
cb[:, :12] = cb[:, -12:] = (60, 90, 120)
save('chalkboard.jpg', cb)
print('banker textures done')
