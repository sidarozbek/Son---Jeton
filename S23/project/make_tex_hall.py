#!/usr/bin/env python3
"""Scene 23's exam hall, painted with code (BGR). An original, generic hall.
- hall_wall.jpg, hall_floor.jpg: cream plaster over a pale green dado; honey-coloured floorboards.
- hall_front.jpg: the front wall with a blackboard (SINAV chalked on it) and a round clock.
- hall_windows.jpg: the left wall with three tall windows full of morning light."""
import os

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

r = np.random.default_rng(23)
os.makedirs('tex', exist_ok=True)


def noise(h, w, s):
    n = cv2.GaussianBlur(r.normal(0, 1, (h, w)).astype(np.float32), (0, 0), s)
    return n / (n.std() + 1e-6)


def save(name, a):
    cv2.imwrite('tex/' + name, np.clip(a, 0, 255).astype(np.uint8), [cv2.IMWRITE_JPEG_QUALITY, 92])


def text(a, xy, s, px, rgb, anchor='mm'):
    im = Image.fromarray(cv2.cvtColor(np.clip(a, 0, 255).astype(np.uint8), cv2.COLOR_BGR2RGB))
    f = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', px)
    ImageDraw.Draw(im).text(xy, s, font=f, fill=rgb, anchor=anchor)
    a[:] = cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR)


def flat(h, w, bgr):
    return np.dstack([np.full((h, w), v, np.float32) for v in bgr])


P = 100
# ---- wall: 3 m bay, 3.2 m tall.
h, w = int(3.2 * P), int(3 * P)
a = flat(h, w, (196, 222, 232))
a *= (1 + noise(h, w, 12) * .03)[..., None]
a[h - int(1.0 * P):] = (170, 196, 178)
cv2.line(a, (0, h - int(1.0 * P)), (w, h - int(1.0 * P)), (120, 140, 130), 4)
save('hall_wall.jpg', a)

# ---- floor: 1.6 m tile of boards.
h = w = int(1.6 * P)
f = flat(h, w, (110, 160, 196))
for k in range(0, w, 16):
    f[:, k:k + 16] *= r.uniform(.9, 1.08)
    cv2.line(f, (k, 0), (k, h), (80, 110, 140), 1)
f *= (1 + noise(h, w, 2) * .03)[..., None]
save('hall_floor.jpg', f)

# ---- front wall: 9 m x 3.2 m, the blackboard at x 2.5-6.5, z 1.0-2.3, the clock at x 7.4, z 2.45.
h, w = int(3.2 * P), int(9 * P)
a = flat(h, w, (196, 222, 232))
a *= (1 + noise(h, w, 12) * .03)[..., None]
a[h - int(1.0 * P):] = (170, 196, 178)
x0, x1, z0, z1 = int(2.5 * P), int(6.5 * P), int(1.0 * P), int(2.3 * P)
cv2.rectangle(a, (x0 - 8, h - z1 - 8), (x1 + 8, h - z0 + 8), (60, 90, 120), -1)
board = flat(z1 - z0, x1 - x0, (60, 74, 52))
board *= (1 + noise(z1 - z0, x1 - x0, 20) * .05)[..., None]
a[h - z1:h - z0, x0:x1] = board
text(a, ((x0 + x1) // 2, h - z1 + int(.45 * P)), 'SINAV', int(.36 * P), (232, 232, 222))
text(a, ((x0 + x1) // 2, h - z1 + int(.9 * P)), 'Süre: 60 dakika', int(.14 * P), (220, 220, 210))
cx, cy = int(7.4 * P), h - int(2.45 * P)
cv2.circle(a, (cx, cy), int(.24 * P), (240, 242, 244), -1)
cv2.circle(a, (cx, cy), int(.24 * P), (40, 40, 40), 4)
for k in range(12):
    ang = k * np.pi / 6
    p0 = (int(cx + .19 * P * np.sin(ang)), int(cy - .19 * P * np.cos(ang)))
    p1 = (int(cx + .22 * P * np.sin(ang)), int(cy - .22 * P * np.cos(ang)))
    cv2.line(a, p0, p1, (40, 40, 40), 2)
cv2.line(a, (cx, cy), (cx + int(.1 * P), cy - int(.06 * P)), (30, 30, 30), 4)    # Hour hand.
cv2.line(a, (cx, cy), (cx, cy - int(.18 * P)), (30, 30, 30), 3)                 # Minute hand: on the hour.
save('hall_front.jpg', a)

# ---- left wall: 10 m x 3.2 m with three tall windows (seen from inside; morning light).
h, w = int(3.2 * P), int(10 * P)
a = flat(h, w, (196, 222, 232))
a *= (1 + noise(h, w, 12) * .03)[..., None]
a[h - int(1.0 * P):] = (170, 196, 178)
for cx in (2.0, 5.0, 8.0):
    wx0, wx1 = int((cx - .6) * P), int((cx + .6) * P)
    wz0, wz1 = int(1.0 * P), int(2.8 * P)
    cv2.rectangle(a, (wx0 - 8, h - wz1 - 8), (wx1 + 8, h - wz0 + 8), (230, 236, 240), -1)
    sky = np.linspace(255, 225, wz1 - wz0)[:, None]
    a[h - wz1:h - wz0, wx0:wx1] = np.dstack([sky * .98, sky * .96, sky * .86] * np.ones((1, wx1 - wx0, 1)))[..., :3] if False else np.stack([np.repeat(sky * 1.0, wx1 - wx0, 1), np.repeat(sky * .97, wx1 - wx0, 1), np.repeat(sky * .9, wx1 - wx0, 1)], -1)
    cv2.line(a, ((wx0 + wx1) // 2, h - wz1), ((wx0 + wx1) // 2, h - wz0), (210, 216, 220), 6)
    cv2.line(a, (wx0, h - (wz0 + wz1) // 2), (wx1, h - (wz0 + wz1) // 2), (210, 216, 220), 6)
save('hall_windows.jpg', a)
print('ok')
