"""The paper fold (from Scene 03): the whole picture folds away like a sheet of paper. Also the line's crackle."""
import math

import cv2
import numpy as np


# ---------------- the paper fold
PAPER = np.array((236, 230, 216), np.float32)       # RGB: the void the folded picture lands in.
PAPER_BACK = (226, 220, 204)


def _ease(u):
    u = min(max(u, 0.0), 1.0)
    return u * u * (3 - 2 * u)


def _warp(dst, src, quad):
    """Paint src into dst on a four-corner quad (TL, TR, BR, BL), with an anti-aliased edge."""
    h, w = src.shape[:2]
    S = np.float32([[0, 0], [w, 0], [w, h], [0, h]])
    M = cv2.getPerspectiveTransform(S, np.float32(quad))
    H, W = dst.shape[:2]
    img = cv2.warpPerspective(src, M, (W, H), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT)
    m = cv2.warpPerspective(np.full((h, w), 255, np.uint8), M, (W, H), flags=cv2.INTER_LINEAR)
    a = (m.astype(np.float32) / 255)[..., None]
    dst[:] = dst * (1 - a) + img.astype(np.float32) * a


def _shadow(dst, quad, off, strength=.25):
    H, W = dst.shape[:2]
    m = np.zeros((H, W), np.uint8)
    cv2.fillConvexPoly(m, np.int32(np.array(quad) + off), 255)
    m = cv2.GaussianBlur(m, (0, 0), 9).astype(np.float32) / 255 * strength
    dst[:] = dst * (1 - m[..., None])


def paper_fold(pic, f):
    """The whole picture folds like a sheet of paper: the right half swings back behind the left, then the bottom half
    behind the top, then the folded quarter shrinks to a small sheet on a paper-white void. Folds go away from the
    viewer, so the picture stays face up until the end."""
    H, W = pic.shape[:2]
    src = pic.astype(np.float32)
    out = np.empty_like(src)
    out[:] = PAPER
    if f < .42:                                   # 1. Right half folds back.
        u = _ease(f / .42)
        a = math.pi * u
        sx = W / 4 * u                            # The fold line drifts to the centre.
        L = src[:, :W // 2]
        Rh = src[:, W // 2:]
        Lq = [(sx, 0), (sx + W / 2, 0), (sx + W / 2, H), (sx, H)]
        _shadow(out, Lq, (6, 8), .18 * u)
        _warp(out, L, Lq)
        cw = W / 2 * math.cos(a)
        if cw > 1:
            sq = .1 * math.sin(a) * H
            x0 = sx + W / 2
            q = [(x0, 0), (x0 + cw, sq), (x0 + cw, H - sq), (x0, H)]
            shade = (.62 + .38 * math.cos(a))
            _warp(out, Rh * shade, q)
        cv2.line(out, (int(sx + W / 2), 0), (int(sx + W / 2), H), (40, 34, 30), 2)
        return np.clip(out, 0, 255).astype(np.uint8)
    half = src[:, :W // 2]
    if f < .82:                                   # 2. Bottom half folds back.
        u = _ease((f - .42) / .40)
        a = math.pi * u
        sy = H / 4 * u
        x0 = W / 4
        T = half[:H // 2]
        Bh = half[H // 2:]
        Tq = [(x0, sy), (x0 + W / 2, sy), (x0 + W / 2, sy + H / 2), (x0, sy + H / 2)]
        _shadow(out, [(x0, sy), (x0 + W / 2, sy), (x0 + W / 2, sy + H / 2 + max(H / 2 * math.cos(a), 0)), (x0, sy + H / 2 + max(H / 2 * math.cos(a), 0))], (6, 8), .2)
        _warp(out, T, Tq)
        ch = H / 2 * math.cos(a)
        if ch > 1:
            sq = .1 * math.sin(a) * W / 2
            y0 = sy + H / 2
            q = [(x0, y0), (x0 + W / 2, y0), (x0 + W / 2 - sq, y0 + ch), (x0 + sq, y0 + ch)]
            _warp(out, Bh * (.62 + .38 * math.cos(a)), q)
        cv2.line(out, (int(x0), int(sy + H / 2)), (int(x0 + W / 2), int(sy + H / 2)), (40, 34, 30), 2)
        cv2.rectangle(out, (int(x0), int(sy)), (int(x0 + W / 2), int(sy + H / 2)), (40, 34, 30), 2)
        return np.clip(out, 0, 255).astype(np.uint8)
    # 3. The folded quarter shrinks to a small sheet, turning a little, and its picture fades to the paper's back.
    u = _ease((f - .82) / .18)
    q4 = half[:H // 2]
    s = 1 - .72 * u
    w, h = W / 2 * s, H / 2 * s
    cx, cy = W / 2, H / 2
    ang = -.25 * u
    cs, sn = math.cos(ang), math.sin(ang)
    corners = [(-w / 2, -h / 2), (w / 2, -h / 2), (w / 2, h / 2), (-w / 2, h / 2)]
    quad = [(cx + x * cs - y * sn, cy + x * sn + y * cs) for x, y in corners]
    _shadow(out, quad, (8, 10), .3)
    face = q4 * (1 - u) + np.array(PAPER_BACK, np.float32) * u
    _warp(out, face, quad)
    cv2.polylines(out, [np.int32(quad)], True, (40, 34, 30), 2, cv2.LINE_AA)
    if u > .5:                                    # The creases show on the back.
        m1 = ((quad[0][0] + quad[1][0]) / 2, (quad[0][1] + quad[1][1]) / 2)
        m2 = ((quad[3][0] + quad[2][0]) / 2, (quad[3][1] + quad[2][1]) / 2)
        cv2.line(out, (int(m1[0]), int(m1[1])), (int(m2[0]), int(m2[1])), (170, 160, 140), 2, cv2.LINE_AA)
    return np.clip(out, 0, 255).astype(np.uint8)


def crackle(pic, k, t):
    """The line crossing, seen: bands of the picture slip sideways, the colour plates split, snow."""
    if k <= 0:
        return pic
    H, W = pic.shape[:2]
    out = pic.copy()
    rng = np.random.default_rng(int(t * 24))
    for _ in range(int(3 + 14 * k)):
        y0 = int(rng.uniform(0, H))
        h = int(rng.uniform(4, 10 + 50 * k))
        dx = int(rng.normal(0, 8 + 60 * k))
        out[y0:y0 + h] = np.roll(out[y0:y0 + h], dx, axis=1)
    s = int(2 + 8 * k)
    out[..., 0] = np.roll(out[..., 0], s, axis=1)
    out[..., 2] = np.roll(out[..., 2], -s, axis=1)
    snow = rng.random((H // 2, W // 2)) < .08 * k
    snow = cv2.resize(snow.astype(np.uint8) * 255, (W, H), interpolation=cv2.INTER_NEAREST)
    o = out.astype(np.float32)
    o = o * (1 - .25 * k * (snow[..., None] / 255)) + 235 * .25 * k * (snow[..., None] / 255)
    return np.clip(o, 0, 255).astype(np.uint8)
