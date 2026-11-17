#!/usr/bin/env python3
"""Scene 03's basement, painted with code (BGR): rough concrete walls with damp, a stained concrete floor, the boiler,
and an original wall payphone with a rotary dial and a coin slot (no logo, no real brand). Run after make_tex.py."""
import os
import subprocess
import sys

import cv2
import numpy as np

r = np.random.default_rng(31)
TOOL = os.environ.get('TOON_TOOLS', os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), '..', '..', 'tools'))
PX = 300


def noise(h, w, s):
    n = cv2.GaussianBlur(r.normal(0, 1, (h, w)).astype(np.float32), (0, 0), s)
    return n / (n.std() + 1e-6)


def save(name, a):
    cv2.imwrite('tex/' + name, np.clip(a, 0, 255).astype(np.uint8), [cv2.IMWRITE_JPEG_QUALITY, 92])


# Concrete wall: grey-beige, formwork lines, a damp tide-mark near the floor, old whitewash flaking at the top.
h, w = int(2.4 * PX), int(2.4 * PX)
a = np.dstack([np.full((h, w), v, np.float32) for v in (118, 126, 130)])
a *= (1 + noise(h, w, 40) * .06 + noise(h, w, 2) * .04)[..., None]
for y in range(0, h, int(.6 * PX)):
    cv2.line(a, (0, y), (w, y), (96, 102, 106), 3)
damp = np.clip(1 - np.linspace(0, 1, h)[::-1] * 3.2, 0, 1)[:, None] * (0.6 + .4 * noise(1, w, 30))
a = a * (1 - damp[..., None] * .35) + np.array((70, 80, 84), np.float32) * damp[..., None] * .35
ws = np.clip(noise(h, w, 25) - .3, 0, 1)[..., None] * np.linspace(1, 0, h)[:, None, None] ** 2
a = a * (1 - ws * .5) + np.array((200, 206, 208), np.float32) * ws * .5
save('concrete_wall.jpg', a)

# Concrete floor: darker, oil and coal stains, a drain.
N = 768
f = np.dstack([np.full((N, N), v, np.float32) for v in (92, 98, 102)])
f *= (1 + noise(N, N, 50) * .07 + noise(N, N, 2) * .05)[..., None]
st = np.clip(noise(N, N, 70) - .8, 0, 1)[..., None]
f = f * (1 - st * .5) + np.array((40, 44, 48), np.float32) * st * .5
for i in range(0, N, N // 2):
    cv2.line(f, (i, 0), (i, N), (70, 74, 78), 3)
    cv2.line(f, (0, i), (N, i), (70, 74, 78), 3)
save('concrete_floor.jpg', f)

# Wooden stair treads and risers.
t_ = np.dstack([np.full((256, 512), v, np.float32) for v in (54, 82, 112)])
t_ *= (1 + noise(256, 512, 1.5) * .05 + noise(256, 512, 20) * .05)[..., None]
for y in range(0, 256, 32):
    cv2.line(t_, (0, y), (512, y + int(r.integers(-4, 4))), (38, 58, 82), 2)
save('stair_wood.jpg', t_)


def sheet(w_, h_):
    return np.full((h_, w_, 3), 128, np.uint8)


def cut(name, *args):
    subprocess.run([sys.executable, os.path.join(TOOL, 'cut_sheet.py'), f'tex/{name}.jpg', f'tex/{name}.json', *args], check=True)


# The payphone, front view: a dark green metal case with a chrome face, a rotary dial, a coin slot (top right),
# a coin return (bottom right), the receiver cradle on the left side. 0.34 x 0.52 m; sheet at 2 px per mm-ish.
p = sheet(380, 560)
cv2.rectangle(p, (20, 20), (360, 540), (52, 88, 46), -1)                 # Case.
cv2.rectangle(p, (20, 20), (360, 540), (30, 50, 26), 6)
cv2.rectangle(p, (70, 60), (340, 500), (176, 182, 184), -1)              # Chrome face.
cv2.rectangle(p, (70, 60), (340, 500), (110, 116, 118), 4)
cv2.circle(p, (205, 300), 92, (30, 30, 34), -1)                          # Rotary dial.
for k in range(10):
    ang = np.deg2rad(-60 + k * 30)
    cv2.circle(p, (int(205 + 62 * np.cos(ang)), int(300 + 62 * np.sin(ang))), 14, (200, 204, 206), -1)
cv2.circle(p, (205, 300), 30, (220, 224, 226), -1)
cv2.rectangle(p, (262, 92), (316, 104), (20, 20, 22), -1)                # Coin slot.
cv2.rectangle(p, (250, 430), (326, 476), (60, 64, 66), -1)               # Coin return.
cv2.rectangle(p, (100, 100), (220, 150), (230, 236, 238), -1)            # A blank instruction card: no text.
for y in (112, 124, 136):
    cv2.line(p, (110, y), (210, y), (170, 174, 176), 3)
cv2.rectangle(p, (20, 150), (64, 360), (36, 60, 32), -1)                 # Cradle.
cv2.imwrite('tex/payphone.jpg', p, [cv2.IMWRITE_JPEG_QUALITY, 94])
cut('payphone', '--eps', '2')

# The boiler, side view: a squat iron drum with a door and rivets.
b = sheet(520, 700)
cv2.rectangle(b, (40, 120), (480, 680), (48, 52, 58), -1)
cv2.ellipse(b, (260, 120), (220, 60), 0, 180, 360, (48, 52, 58), -1)
cv2.rectangle(b, (180, 440), (340, 600), (30, 32, 36), -1)
cv2.rectangle(b, (180, 440), (340, 600), (90, 120, 160), 4)
for y in range(180, 660, 60):
    for x in (60, 460):
        cv2.circle(b, (x, y), 7, (80, 86, 92), -1)
cv2.rectangle(b, (230, 20), (290, 90), (60, 64, 70), -1)                 # Flue stub.
cv2.imwrite('tex/boiler.jpg', b, [cv2.IMWRITE_JPEG_QUALITY, 94])
cut('boiler', '--eps', '2')

# A cardboard box stack.
c = sheet(420, 420)
for (x0, y0, x1, y1, col) in ((30, 220, 260, 400, (70, 120, 160)), (200, 240, 400, 400, (60, 108, 146)), (90, 60, 300, 230, (78, 130, 170))):
    cv2.rectangle(c, (x0, y0), (x1, y1), col, -1)
    cv2.rectangle(c, (x0, y0), (x1, y1), tuple(v * .6 for v in col), 4)
    cv2.line(c, ((x0 + x1) // 2, y0), ((x0 + x1) // 2, y1), (150, 170, 190), 6)
cv2.imwrite('tex/boxes.jpg', c, [cv2.IMWRITE_JPEG_QUALITY, 94])
cut('boxes', '--eps', '2')
print('basement textures done')
