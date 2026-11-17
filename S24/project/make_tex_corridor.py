#!/usr/bin/env python3
"""Scene 24's corridor outside the exam hall, painted with code (BGR). Original and generic.
- corr_floor.jpg: pale grey terrazzo tiles.
- corr_end.jpg: the end wall: one tall window full of late-morning light.
(hall_wall.jpg is Scene 23's wall.)"""
import os

import cv2
import numpy as np

r = np.random.default_rng(24)
os.makedirs('tex', exist_ok=True)


def noise(h, w, s):
    n = cv2.GaussianBlur(r.normal(0, 1, (h, w)).astype(np.float32), (0, 0), s)
    return n / (n.std() + 1e-6)


def save(name, a):
    cv2.imwrite('tex/' + name, np.clip(a, 0, 255).astype(np.uint8), [cv2.IMWRITE_JPEG_QUALITY, 92])


def flat(h, w, bgr):
    return np.dstack([np.full((h, w), v, np.float32) for v in bgr])


P = 100
h = w = int(1.2 * P)
f = flat(h, w, (196, 198, 196))
f *= (1 + noise(h, w, 1.2) * .05)[..., None]
for k in range(0, w, 60):
    cv2.line(f, (k, 0), (k, h), (160, 162, 160), 2)
    cv2.line(f, (0, k), (w, k), (160, 162, 160), 2)
save('corr_floor.jpg', f)

h, w = int(3.2 * P), int(3.0 * P)
a = flat(h, w, (196, 222, 232))
a[h - int(1.0 * P):] = (170, 196, 178)
x0, x1, z0, z1 = int(.6 * P), int(2.4 * P), int(.8 * P), int(2.9 * P)
cv2.rectangle(a, (x0 - 10, h - z1 - 10), (x1 + 10, h - z0 + 10), (232, 236, 240), -1)
sky = np.linspace(255, 232, z1 - z0)[:, None]
a[h - z1:h - z0, x0:x1] = np.stack([np.repeat(sky, x1 - x0, 1), np.repeat(sky * .98, x1 - x0, 1), np.repeat(sky * .93, x1 - x0, 1)], -1)
cv2.line(a, ((x0 + x1) // 2, h - z1), ((x0 + x1) // 2, h - z0), (214, 220, 224), 8)
cv2.line(a, (x0, h - (z0 + z1) // 2), (x1, h - (z0 + z1) // 2), (214, 220, 224), 8)
save('corr_end.jpg', a)
print('ok')
