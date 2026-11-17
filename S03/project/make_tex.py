#!/usr/bin/env python3
"""Paints every surface of the rented room with code: flat, gouache-like, no light baked in (the lamp light comes from
env.post). All colours BGR. Cultural layer from the bible: net curtain, patterned vinyl floor, panel radiator,
tulip tea glass, printed contract form, photocopied notes."""
import os
import subprocess
import sys

import cv2
import numpy as np

os.makedirs('tex', exist_ok=True)
r = np.random.default_rng(11)
TOOL = os.environ.get('TOON_TOOLS', os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), '..', '..', 'tools'))
PX = 400   # Pixels per metre on stretched walls.


def noise(h, w, s, sy=None):
    n = cv2.GaussianBlur(r.normal(0, 1, (h, w)).astype(np.float32), (0, 0), sigmaX=s, sigmaY=sy or s)
    return n / (n.std() + 1e-6)


def save(name, a, q=92):
    cv2.imwrite('tex/' + name, np.clip(a, 0, 255).astype(np.uint8), [cv2.IMWRITE_JPEG_QUALITY, q])


def plain(h, w, col):
    return np.dstack([np.full((h, w), v, np.float32) for v in col])


def plaster(w_m, h_m=2.7, top=(176, 200, 196), low=(112, 134, 118), dado=1.1, seed=0):
    """Old rented-room wall: pale distemper above, oil-painted dado below, a dark line between, scuffs and patches."""
    h, w = int(h_m * PX), int(w_m * PX)
    a = plain(h, w, top)
    a *= (1 + noise(h, w, 60) * .035 + noise(h, w, 3) * .012)[..., None]
    for _ in range(int(w_m * 3)):          # Old patched spots, a shade off.
        x, y = int(r.integers(0, w)), int(r.integers(0, int(h * .55)))
        cv2.ellipse(a, (x, y), (int(r.integers(30, 110)), int(r.integers(20, 60))), 0, 0, 360,
                    tuple(float(v * r.uniform(.94, 1.03)) for v in top), -1)
    y0 = int(h * (1 - dado / h_m))
    a[y0:] = plain(h - y0, w, low) * (1 + noise(h - y0, w, 40) * .03)[..., None]
    cv2.line(a, (0, y0), (w, y0), tuple(v * .55 for v in low), 7)
    a[int(h * .965):] = np.array((44, 56, 70), np.float32)          # Skirting board, dark brown.
    a[:int(h * .02)] *= .8
    for _ in range(int(w_m * 6)):          # Chair and shoe scuffs on the dado.
        x, y = int(r.integers(0, w)), int(r.integers(y0 + 40, int(h * .95)))
        cv2.line(a, (x, y), (x + int(r.integers(20, 70)), y + int(r.integers(-6, 6))), tuple(v * .8 for v in low), 3)
    return a


# ---- walls
save('wall.jpg', plaster(2.2))
w = plaster(4.4, seed=1)
# Window above the desk on the left wall: y 1.25 to 2.45, z 1.05 to 2.2. Night: dark blue glass behind a net curtain.
x0, x1 = int(1.25 * PX), int(2.45 * PX)
z0, z1 = int((2.7 - 2.2) * PX), int((2.7 - 1.05) * PX)
cv2.rectangle(w, (x0 - 26, z0 - 26), (x1 + 26, z1 + 30), (210, 222, 224), -1)   # Painted frame.
glass = plain(z1 - z0, x1 - x0, (70, 44, 30)) * (1 + noise(z1 - z0, x1 - x0, 30) * .06)[..., None]
for _ in range(5):                                     # A few far lit windows across the street, small and dim.
    gx, gy = int(r.integers(20, x1 - x0 - 40)), int(r.integers(int((z1 - z0) * .35), z1 - z0 - 40))
    cv2.rectangle(glass, (gx, gy), (gx + 12, gy + 16), (70, 120, 160), -1)
w[z0:z1, x0:x1] = glass
cv2.line(w, ((x0 + x1) // 2, z0), ((x0 + x1) // 2, z1), (200, 212, 214), 14)
cv2.line(w, (x0, int(z0 + (z1 - z0) * .3)), (x1, int(z0 + (z1 - z0) * .3)), (200, 212, 214), 12)
# Net curtain: off-white lace, mostly see-through, gathered in vertical folds, hanging from a rod.
lace = np.zeros((z1 - z0 + 60, x1 - x0 + 120), np.float32)
lh, lw = lace.shape
for x in range(0, lw, 6):
    lace[:, x:x + 2] = .55
for y in range(0, lh, 6):
    lace[y:y + 2] = np.maximum(lace[y:y + 2], .45)
for cx in range(30, lw, 90):                          # Flower motifs.
    for cy in range(60, lh, 120):
        cv2.circle(lace, (cx + (cy // 120 % 2) * 45, cy), 16, .9, 3)
folds = (np.sin(np.linspace(0, 26 * np.pi, lw)) * .5 + .5) ** 1.5
lace = np.clip(lace * .6 + folds[None, :] * .35, 0, 1)
lace[int(lh * .86):] *= .2                            # Hem sits above the sill.
ys, xs = slice(z0 - 40, z0 - 40 + lh), slice(x0 - 60, x0 - 60 + lw)
reg = w[ys, xs]
k = (lace * .62)[..., None]
w[ys, xs] = reg * (1 - k) + np.array((214, 228, 232), np.float32) * k
cv2.line(w, (x0 - 80, z0 - 44), (x1 + 80, z0 - 44), (60, 70, 90), 10)     # Curtain rod.
cv2.rectangle(w, (x0 - 40, z1 + 24), (x1 + 40, z1 + 44), (196, 208, 210), -1)  # Sill.
save('wall_window.jpg', w)

# Corridor: cold blue-grey distemper, darker dado, a light switch and a meter box.
c = plaster(9.0, top=(140, 128, 116), low=(96, 86, 78), dado=1.0)
cv2.rectangle(c, (int(1.4 * PX), int(1.3 * PX)), (int(1.4 * PX) + 34, int(1.3 * PX) + 52), (200, 206, 210), -1)
cv2.rectangle(c, (int(6.2 * PX), int(.5 * PX)), (int(6.2 * PX) + 160, int(.5 * PX) + 220), (110, 116, 120), -1)
cv2.rectangle(c, (int(6.2 * PX), int(.5 * PX)), (int(6.2 * PX) + 160, int(.5 * PX) + 220), (50, 54, 58), 6)
save('corridor.jpg', c)

# ---- patterned vinyl floor (muşamba): beige ground, brown octagons, cream squares. One repeat = 0.6 m.
N = 1024
f = plain(N, N, (112, 150, 178))
cell = N // 4
for i in range(4):
    for j in range(4):
        cx, cy = i * cell + cell // 2, j * cell + cell // 2
        o = int(cell * .42)
        oc = np.array([[cx - o // 2, cy - o], [cx + o // 2, cy - o], [cx + o, cy - o // 2], [cx + o, cy + o // 2],
                       [cx + o // 2, cy + o], [cx - o // 2, cy + o], [cx - o, cy + o // 2], [cx - o, cy - o // 2]], np.int32)
        cv2.fillConvexPoly(f, oc, (62, 92, 132))
        cv2.polylines(f, [oc], True, (40, 60, 90), 4)
        cv2.circle(f, (cx, cy), int(o * .35), (150, 186, 206), -1)
for i in range(5):
    for j in range(5):
        cx, cy = i * cell, j * cell
        s = int(cell * .13)
        cv2.rectangle(f, (cx - s, cy - s), (cx + s, cy + s), (168, 200, 214), -1)
f *= (1 + noise(N, N, 80) * .05 + noise(N, N, 2) * .02)[..., None]
wear = np.clip(noise(N, N, 140) - .6, 0, 1)[..., None]          # Worn paths.
f = f * (1 - wear * .25) + np.array((100, 128, 150), np.float32) * wear * .25
save('vinyl.jpg', f)

# Corridor floor: grey terrazzo tiles.
t_ = plain(N, N, (118, 120, 122))
spk = r.random((N, N)) > .985
t_[spk] = (60, 62, 66)
t_ *= (1 + noise(N, N, 30) * .05)[..., None]
for i in range(0, N, N // 3):
    cv2.line(t_, (i, 0), (i, N), (80, 82, 86), 5)
    cv2.line(t_, (0, i), (N, i), (80, 82, 86), 5)
save('terrazzo.jpg', t_)

# Ceiling: flat cream, a few water stains.
ce = plain(512, 512, (150, 172, 176)) * (1 + noise(512, 512, 40) * .05)[..., None]
save('ceiling.jpg', ce)


# ---- side sheets on flat grey, cut into real shapes by cut_sheet.py.
def sheet(w_, h_):
    return np.full((h_, w_, 3), 128, np.uint8)


def cut(name, *args):
    subprocess.run([sys.executable, os.path.join(TOOL, 'cut_sheet.py'), f'tex/{name}.jpg', f'tex/{name}.json', *args], check=True)


# Door: four-panel painted door, 0.9 x 2.02 m, sheet 450 x 1010 (2 px per cm + margin).
d = sheet(500, 1060)
cv2.rectangle(d, (25, 25), (475, 1035), (176, 196, 206), -1)
for (px0, py0, px1, py1) in ((70, 80, 230, 470), (270, 80, 430, 470), (70, 560, 230, 980), (270, 560, 430, 980)):
    cv2.rectangle(d, (px0, py0), (px1, py1), (156, 178, 190), -1)
    cv2.rectangle(d, (px0, py0), (px1, py1), (110, 130, 140), 5)
cv2.circle(d, (62, 540), 16, (50, 120, 170), -1)          # Brass knob, on the latch side.
cv2.rectangle(d, (50, 570), (74, 610), (40, 60, 80), -1)  # Keyhole plate.
d[25:1035, 25:475] = np.clip(d[25:1035, 25:475].astype(np.float32) * (1 + noise(1010, 450, 30) * .03)[..., None], 0, 255)
cv2.imwrite('tex/door.jpg', d, [cv2.IMWRITE_JPEG_QUALITY, 94])
cut('door', '--eps', '2', '--rim', '0,500,0,1060,150,170,180')

# Desk lamp, side view: round base, two-part arm, cone shade tipped down toward the desk. Sheet 600 x 700.
l = sheet(600, 700)
cv2.ellipse(l, (190, 660), (130, 26), 0, 0, 360, (46, 72, 50), -1)
cv2.line(l, (190, 640), (230, 380), (46, 72, 50), 22)
cv2.line(l, (230, 380), (380, 220), (46, 72, 50), 20)
cv2.circle(l, (230, 380), 18, (36, 56, 40), -1)
shade = np.array([[330, 160], [440, 150], [560, 330], [380, 400]], np.int32)
cv2.fillConvexPoly(l, shade, (70, 168, 226))
cv2.line(l, (380, 400), (560, 330), (150, 226, 250), 18)   # The lit rim of the shade.
cv2.imwrite('tex/lamp.jpg', l, [cv2.IMWRITE_JPEG_QUALITY, 94])
cut('lamp', '--eps', '2', '--rim', '0,600,0,700,50,80,60')

# A stack of books, side view: spines of varied colour and thickness, slightly uneven. Sheet 400 x 640.
b = sheet(420, 660)
y = 640
cols = [(40, 50, 140), (110, 70, 40), (50, 110, 60), (60, 140, 190), (120, 110, 100), (40, 40, 90), (150, 130, 60), (60, 80, 120)]
k = 0
while y > 60:
    th = int(r.integers(38, 78))
    sx = int(r.integers(30, 70))
    ln = int(r.integers(290, 350))
    col = cols[k % len(cols)]
    cv2.rectangle(b, (sx, y - th), (sx + ln, y), col, -1)
    cv2.rectangle(b, (sx, y - th), (sx + ln, y), tuple(v * .55 for v in col), 4)
    cv2.line(b, (sx + 30, y - th // 2), (sx + ln - 30, y - th // 2), (200, 216, 220), 3)   # Title band.
    y -= th
    k += 1
cv2.imwrite('tex/stack.jpg', b, [cv2.IMWRITE_JPEG_QUALITY, 94])
cut('stack', '--eps', '2')

# Tulip tea glass on a saucer: dark red tea, a thin gold rim. Sheet 240 x 320.
g = sheet(240, 320)
cv2.ellipse(g, (120, 296), (100, 14), 0, 0, 360, (220, 230, 236), -1)
glass_pts = np.array([[86, 284], [154, 284], [160, 250], [146, 190], [150, 130], [164, 80], [76, 80], [90, 130], [94, 190], [80, 250]], np.int32)
cv2.fillPoly(g, [glass_pts], (24, 46, 150))
cv2.line(g, (76, 80), (164, 80), (60, 170, 210), 6)
cv2.line(g, (98, 120), (96, 240), (120, 150, 220), 6)    # Highlight.
cv2.imwrite('tex/teaglass.jpg', g, [cv2.IMWRITE_JPEG_QUALITY, 94])
cut('teaglass', '--eps', '1.5')

# Panel radiator, front view: off-white with vertical channels. Sheet 800 x 400 for 1.0 x 0.5 m.
p = sheet(840, 440)
cv2.rectangle(p, (20, 20), (820, 420), (206, 216, 218), -1)
for x in range(40, 820, 24):
    cv2.line(p, (x, 30), (x, 410), (170, 180, 184), 6)
cv2.rectangle(p, (20, 20), (820, 420), (140, 150, 154), 5)
cv2.imwrite('tex/radiator.jpg', p, [cv2.IMWRITE_JPEG_QUALITY, 94])
cut('radiator', '--eps', '2')
print('textures done')
