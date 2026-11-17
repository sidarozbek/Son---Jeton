"""The "Sınavda çıkar" stamp and what it brings, as whole-frame effects on the finished picture (RGB uint8):
1. A rubber stamp comes down out of the top of the frame and leaves a red SINAVDA ÇIKAR mark.
2. The picture turns into a newspaper clipping: halftone photo, the documented fact as the headline, the date line.
   No masthead and no real paper's name: the clipping is the show's own device.
3. INSERT: Vehbi's textbook page, the same figure underlined.
The text lives in room.py (STAMP_HEAD, STAMP_BODY, STAMP_DATE); this file only draws it. Reusable by later stamp scenes."""
import math

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

import room as R

RED = (196, 36, 40)
INK = (34, 30, 28)
NEWS = (226, 220, 204)
TABLE = (58, 46, 38)
SANS = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
SERIF_B = '/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf'
SERIF = '/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf'
_cache = {}


def _ease(u):
    u = min(max(u, 0.0), 1.0)
    return u * u * (3 - 2 * u)


def _font(p, s):
    return ImageFont.truetype(p, int(s))


def mark(W, H):
    """The red stamp mark, RGBA, a little rotated, with the ink a touch uneven."""
    key = ('mark', W, H)
    if key in _cache:
        return _cache[key]
    w, h = int(W * .34), int(H * .17)
    im = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((4, 4, w - 5, h - 5), radius=int(h * .12), outline=RED + (255,), width=max(int(h * .07), 3))
    d.text((w / 2, h / 2), 'SINAVDA ÇIKAR', font=_font(SANS, h * .36), fill=RED + (255,), anchor='mm')
    im = im.rotate(-8, expand=True, resample=Image.BICUBIC)
    a = np.array(im).astype(np.float32)
    rng = np.random.default_rng(3)
    grain = cv2.GaussianBlur(rng.uniform(.55, 1.0, a.shape[:2]).astype(np.float32), (0, 0), 1.2)
    a[..., 3] *= np.clip(grain * 1.15, 0, 1)
    _cache[key] = a
    return a


def _paste(dst, rgba, x, y, alpha=1.0):
    h, w = rgba.shape[:2]
    H, W = dst.shape[:2]
    x0, y0 = max(x, 0), max(y, 0)
    x1, y1 = min(x + w, W), min(y + h, H)
    if x1 <= x0 or y1 <= y0:
        return
    s = rgba[y0 - y:y1 - y, x0 - x:x1 - x]
    a = s[..., 3:4] / 255 * alpha
    dst[y0:y1, x0:x1] = dst[y0:y1, x0:x1] * (1 - a) + s[..., :3] * a


def stamp_tool(dst, cx, y_bottom, k):
    """The rubber stamp itself: a wooden handle and knob over a dark rubber block, drawn from its bottom edge."""
    H, W = dst.shape[:2]
    bw, bh = int(W * .30), int(H * .07)
    x0 = int(cx - bw / 2)
    yb = int(y_bottom)
    cv2.rectangle(dst, (x0, yb - bh), (x0 + bw, yb), (40, 36, 34), -1)
    cv2.rectangle(dst, (x0 + 6, yb - bh - int(H * .04)), (x0 + bw - 6, yb - bh), (150, 104, 62), -1)
    nw = int(W * .05)
    cv2.rectangle(dst, (int(cx - nw / 2), yb - bh - int(H * .25)), (int(cx + nw / 2), yb - bh - int(H * .04)), (170, 120, 72), -1)
    cv2.ellipse(dst, (int(cx), yb - bh - int(H * .27)), (int(W * .045), int(H * .05)), 0, 0, 360, (186, 134, 82), -1)
    cv2.rectangle(dst, (x0, yb - bh), (x0 + bw, yb), (20, 18, 16), 2)


def clipping(pic):
    """The newspaper clipping, built around the current picture: a halftone photo, the headline, the body, the date."""
    H, W = pic.shape[:2]
    out = np.empty((H, W, 3), np.float32)
    out[:] = TABLE
    key = ('page', W, H)
    if key not in _cache:
        page = Image.new('RGB', (int(W * .86), int(H * .9)), NEWS)
        d = ImageDraw.Draw(page)
        pw, ph = page.size
        d.text((pw / 2, ph * .05), '— ' + R.STAMP_DATE + ' —', font=_font(SERIF, ph * .035), fill=INK, anchor='mm')
        d.line((pw * .04, ph * .085, pw * .96, ph * .085), fill=INK, width=2)
        d.text((pw / 2, ph * .17), R.STAMP_HEAD, font=_font(SERIF_B, ph * .11), fill=INK, anchor='mm')
        for i, line in enumerate(R.STAMP_BODY):
            d.text((pw * .54, ph * (.32 + i * .062)), line, font=_font(SERIF, ph * .042), fill=INK, anchor='lm')
        rng = np.random.default_rng(9)
        for i in range(8):                                      # Body columns as grey lines: nothing else readable.
            y = ph * (.53 + i * .048)
            d.line((pw * .53, y, pw * (.94 - .2 * (i == 7) - rng.uniform(0, .05)), y), fill=(150, 144, 132), width=max(int(ph * .012), 2))
        _cache[key] = np.array(page).astype(np.float32)
    page = _cache[key].copy()
    ph, pw = page.shape[:2]
    # The photo: the current picture in halftone grey, in a box on the left.
    bx0, by0, bx1, by1 = int(pw * .04), int(ph * .26), int(pw * .5), int(ph * .94)
    ph_w, ph_h = bx1 - bx0, by1 - by0
    src = cv2.resize(pic, (ph_w, ph_h), interpolation=cv2.INTER_AREA)
    g = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY).astype(np.float32) / 255
    yy, xx = np.mgrid[0:ph_h, 0:ph_w]
    cell = 5
    dots = (np.sin(xx * math.pi / cell) * np.sin(yy * math.pi / cell) + 1) / 2
    ht = (g * 1.15 > dots * .9).astype(np.float32) * .55 + g * .45
    photo = np.array(NEWS, np.float32) * ht[..., None] + np.array(INK, np.float32) * (1 - ht[..., None])
    page[by0:by1, bx0:bx1] = photo
    cv2.rectangle(page, (bx0, by0), (bx1, by1), INK, 2)
    # Torn-looking edge: nibble the border.
    rng = np.random.default_rng(4)
    m = np.ones((ph, pw), np.float32)
    for x in range(0, pw, 6):
        m[:int(rng.uniform(0, 7)), x:x + 6] = 0
        m[ph - int(rng.uniform(0, 7)):, x:x + 6] = 0
    for y in range(0, ph, 6):
        m[y:y + 6, :int(rng.uniform(0, 7))] = 0
        m[y:y + 6, pw - int(rng.uniform(0, 7)):] = 0
    rgba = np.dstack([page, m * 255])
    # A soft shadow, then the clipping, slightly turned.
    M = cv2.getRotationMatrix2D((pw / 2, ph / 2), 1.5, 1.0)
    rgba = cv2.warpAffine(rgba, M, (pw, ph), flags=cv2.INTER_LINEAR, borderValue=(0, 0, 0, 0))
    ox, oy = (W - pw) // 2, (H - ph) // 2
    sh = np.zeros((H, W), np.float32)
    sh[oy + 8:oy + ph + 8, ox + 10:ox + pw + 10] = rgba[..., 3] / 255
    sh = cv2.GaussianBlur(sh, (0, 0), 10) * .5
    out *= (1 - sh[..., None])
    _paste(out, rgba, ox, oy)
    mk = mark(W, H)
    _paste(out, mk, int(ox + pw * .26), int(oy + ph * .68))
    return out


def textbook_page(W, H, t):
    """INSERT: Vehbi's textbook open at the page, the line underlined in pencil, a slow push in."""
    key = ('book', W, H)
    if key not in _cache:
        im = Image.new('RGB', (W, H), (60, 48, 36))
        d = ImageDraw.Draw(im)
        d.rectangle((int(W * .04), int(H * .04), int(W * .96), int(H * 1.0)), fill=(236, 228, 206))
        d.line((W * .5, H * .04, W * .5, H), fill=(190, 180, 156), width=6)
        d.text((W * .27, H * .1), 'TÜRKİYE EKONOMİSİ', font=_font(SANS, H * .04), fill=(120, 60, 40), anchor='mm')
        d.text((W * .73, H * .1), 'Bölüm 4 · 1980 sonrası', font=_font(SERIF, H * .035), fill=(120, 110, 96), anchor='mm')
        rng = np.random.default_rng(12)
        for col in (0, 1):
            x0 = W * (.08 + col * .46)
            for i in range(12):
                y = H * (.2 + i * .065)
                if col == 1 and i in (4, 5):
                    continue
                d.line((x0, y, x0 + W * (.38 - rng.uniform(0, .06)), y), fill=(150, 142, 126), width=max(int(H * .012), 2))
        x0 = W * .54
        d.text((x0, H * .46), '24 Ocak 1980:', font=_font(SERIF_B, H * .04), fill=(30, 28, 26), anchor='lm')
        d.text((x0, H * .515), '1 ABD doları = 70 TL', font=_font(SERIF_B, H * .04), fill=(30, 28, 26), anchor='lm')
        d.line((x0, H * .545, x0 + W * .3, H * .548), fill=(90, 90, 96), width=4)
        _cache[key] = np.array(im).astype(np.float32)
    img = _cache[key]
    u = _ease((t - R.PAGE[0]) / (R.PAGE[1] - R.PAGE[0]))
    s = 1.0 + .18 * u
    cx, cy = W * (.5 + .16 * u), H * .5                     # Drifts towards the underlined line.
    M = np.float32([[s, 0, (1 - s) * cx], [0, s, (1 - s) * cy]])
    return cv2.warpAffine(img, M, (W, H), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)


def overlay(pic, t):
    H, W = pic.shape[:2]
    out = pic.astype(np.float32)
    # 3. The textbook page, cut in as an insert.
    if R.PAGE[0] <= t < R.PAGE[1]:
        return np.clip(textbook_page(W, H, t), 0, 255).astype(np.uint8)
    # 2. The clipping.
    k = R.clip(t)
    if k > 0:
        cl = clipping(pic)
        out = out * (1 - k) + cl * k
    # 1. The stamp coming down, and the mark it leaves on the picture until the clipping takes over.
    a, hit, b = R.STAMP
    cx, cy = W * .66, H * .3
    if hit <= t < R.CLIP[1]:
        mk = mark(W, H)
        _paste(out, mk, int(cx - mk.shape[1] / 2), int(cy - mk.shape[0] / 2), 1 - k)
    if a <= t < b:
        if t < hit:
            u = _ease((t - a) / (hit - a))
            yb = -H * .1 + (cy + H * .09 + H * .1) * u
        else:
            u = _ease((t - hit) / (b - hit))
            yb = cy + H * .09 - (cy + H * .5) * u
        stamp_tool(out, cx, yb, 1)
        if abs(t - hit) < .06:                                  # A tiny shake on impact.
            out = np.roll(out, 3, axis=0)
    return np.clip(out, 0, 255).astype(np.uint8)
