"""What else lives in the street: the snow, Sidar's four tokens, Vehbi's watch, and the light. The light is applied to the
whole finished picture in 3D, from the depth buffer: cold blue dusk everywhere, warm pools from the grocer's window and the
street lamp. Characters are lit as one body at their own position. The scene opens with Scene 03's paper fold, run backwards."""
import math

import cv2
import numpy as np
import skia

from toonkit.fx import Precip
import room as R
import blocking as B

AIR = np.array((.40, .48, .74), np.float32)       # Dusk ambient, RGB gain.
WARM = np.array((1.3, 1.04, .7), np.float32)      # The shop window.
LAMPC = np.array((1.12, .98, .78), np.float32)     # The street lamp.
WIN = np.array(R.WIN_LIGHT, np.float32)
LMP = np.array(R.LAMP_HEAD, np.float32)


class Env:
    def __init__(self, cfg, cast):
        self.snow = Precip('snow', n=320, fall=.55, drift=.35, size=.011, color=(236, 240, 246, 200))
        self._grid = None
        self._chars = []
        self.cast = cast

    def step(self, t, dt, n):
        pass

    def top(self, c, ctx):
        self.snow.draw(c, ctx)
        self.draw_tokens(c, ctx)
        self.draw_watch(c, ctx)

    def _col(self, p, t, rgb):
        g = self.gain_at(p, t)
        return skia.Color(*[int(min(255, v * k)) for v, k in zip(rgb, g)])

    def draw_tokens(self, c, ctx):
        """Four brass tokens with holes, in Sidar's fist, rattling while he shakes them."""
        t, cam = ctx.t, ctx.cam
        if not (R.SHAKE[0] - .05 <= t < R.SHAKE[1] - .1):
            return
        q = self.cast['sidar'].q
        h = q['hand'][1]
        F, Rr = q['F'], q['R']
        up = np.array([0, 0, 1.0])
        offs = ((-.03, .0, .045), (.0, .02, .06), (.03, -.01, .05), (.012, .03, .085))
        for i, (a, b, z) in enumerate(offs):
            j = .012 * math.sin(t * 37 + i * 1.9) if t < R.SHAKE[1] - .4 else 0
            p = h + Rr * a + F * (b + .03) + up * (z + j)
            if cam.depth(p) < .1:
                continue
            s = cam.pt(p)
            r = max(.0135 * cam.scale(p), 1.2)
            sq = .55 + .35 * abs(math.sin(t * 9 + i))           # Tumbling: seen edge-on, then face-on.
            rect = skia.Rect(float(s[0] - r), float(s[1] - r * sq), float(s[0] + r), float(s[1] + r * sq))
            c.drawOval(rect, skia.Paint(AntiAlias=True, Color=self._col(p, t, (218, 176, 80))))
            c.drawOval(rect, skia.Paint(AntiAlias=True, Style=skia.Paint.kStroke_Style, StrokeWidth=max(r * .14, .8), Color=skia.Color(70, 50, 20)))
            c.drawCircle(float(s[0]), float(s[1]), r * .26 * sq, skia.Paint(AntiAlias=True, Color=skia.Color(40, 30, 16)))

    def draw_watch(self, c, ctx):
        """A small round wristwatch on Vehbi's right wrist, while he has it up to read."""
        t, cam = ctx.t, ctx.cam
        if not (R.WATCH[0] + .15 <= t < R.WATCH[1] + .2):
            return
        q = self.cast['vehbi'].q
        h, sh = q['hand'][1], q['sh'][1]
        p = h + (sh - h) * .14
        if cam.depth(p) < .1:
            return
        s = cam.pt(p)
        r = max(.016 * cam.scale(p), 1.5)
        c.drawCircle(float(s[0]), float(s[1]), r * 1.25, skia.Paint(AntiAlias=True, Color=skia.Color(40, 30, 24)))
        c.drawCircle(float(s[0]), float(s[1]), r, skia.Paint(AntiAlias=True, Color=self._col(p, t, (236, 230, 214))))
        ink = skia.Paint(AntiAlias=True, StrokeWidth=max(r * .16, .8), Color=skia.Color(30, 30, 30))
        c.drawLine(float(s[0]), float(s[1]), float(s[0]), float(s[1] - r * .7), ink)
        c.drawLine(float(s[0]), float(s[1]), float(s[0] + r * .5), float(s[1] + r * .2), ink)

    def world(self, ctx):
        """World position of the set behind every pixel, from the depth buffer. Cached per frame."""
        key = (ctx.frame, ctx.t)
        if getattr(self, '_wkey', None) == key:
            return self._w
        cam, H, W = ctx.cam, ctx.H, ctx.W
        if self._grid is None or self._grid[0].shape != (H, W):
            u, v = np.meshgrid(np.arange(W, dtype=np.float32), np.arange(H, dtype=np.float32))
            self._grid = (u, v)
        u, v = self._grid
        z = np.clip(ctx.zb.astype(np.float32), .05, 60)
        ox, oy = (u - W / 2) / cam.F, (H / 2 - v) / cam.F
        P = cam.pos.astype(np.float32)
        f, r, up = cam.f.astype(np.float32), cam.r.astype(np.float32), cam.u.astype(np.float32)
        wx = P[0] + z * (f[0] + r[0] * ox + up[0] * oy)
        wy = P[1] + z * (f[1] + r[1] * ox + up[1] * oy)
        wz = P[2] + z * (f[2] + r[2] * ox + up[2] * oy)
        self._wkey, self._w = key, (wx, wy, wz)
        return self._w

    def on_actor(self, c, ink, ctx, pup):
        """Remember where this character covers the frame, and the light at its own position (see post)."""
        try:
            snap = c.getSurface().makeImageSnapshot().toarray(colorType=skia.ColorType.kRGBA_8888_ColorType)
        except Exception:
            return
        alpha = snap[..., 3].astype(np.float32) / 255
        chest = pup.root + np.array([0, 0, 1.0])
        self._chars.append((alpha, self.gain_at(chest, ctx.t), ctx.cam.depth(chest)))

    def gain_at(self, p, t):
        x, y, z = (np.array([float(v)], np.float32) for v in p)
        return self.gain(x, y, z, t)[0]

    def gain(self, wx, wy, wz, t):
        """Cold dusk air, a warm pool spilling out of the shop window onto the sidewalk, a lamp pool under the street lamp."""
        dw = (wx - WIN[0]) ** 2 * .55 + (wy - WIN[1]) ** 2 + (wz - WIN[2]) ** 2 * .8
        pw = np.exp(-dw / 2.3 ** 2) * np.where(wy > R.FACADE_Y - .02, .35, 1.0)    # The facade itself takes less.
        dl = (wx - LMP[0]) ** 2 + (wy - LMP[1]) ** 2 + ((wz - LMP[2]) * .45) ** 2
        pl = np.exp(-dl / 3.0 ** 2) * .8
        g = AIR[None, None, :] if np.ndim(wx) == 2 else AIR[None, :]
        out = g + pw[..., None] * (WARM - AIR) + pl[..., None] * (LAMPC - AIR) * .7
        far = (np.hypot(wx - 6, wy - 3) > 40)[..., None]                             # Sky: leave it as painted.
        return np.where(far, 1.0, out)

    def post(self, pic, ctx):
        cam, H, W = ctx.cam, ctx.H, ctx.W
        wx, wy, wz = self.world(ctx)
        u, v = self._grid
        gain = self.gain(wx, wy, wz, ctx.t)
        zb = ctx.zb
        for alpha, g, dist in self._chars:
            a = (alpha * (zb >= dist - .55))[..., None]
            gain = gain * (1 - a) + g[None, None, :] * a
        self._chars = []
        vg = 1 - .26 * (((u - W / 2) / (W / 2)) ** 2 + ((v - H / 2) / (H / 2)) ** 2)[..., None]
        out = np.clip(pic.astype(np.float32) * gain * vg, 0, 255).astype(np.uint8)
        f = R.unfold(ctx.t)
        return paper_fold(out, f) if f > 0 else out


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
