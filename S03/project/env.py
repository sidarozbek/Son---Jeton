"""What else lives in the room. The lamp light is applied to the whole finished picture in 3D, from the depth buffer,
so the set and the characters share one pool of warm light; the corridor stays cold until the door opens."""
import numpy as np
import skia

from toonkit.fx import Precip
import room as R
import blocking as B
import cv2
import math

LAMP = np.array(R.LAMP, np.float32)
WARM = np.array((1.18, 1.0, .76), np.float32)     # RGB gain at the heart of the pool.
COLD = np.array((.62, .70, .86), np.float32)      # The corridor at night.
AMB = .36                                         # The room far from the lamp.
REACH = 2.3                                       # Metres for the pool to fall off.
BWARM = np.array((1.16, 1.02, .8), np.float32)     # The basement bulb.
BAMB = .3
DOOR_C = np.array(((R.DOOR_X0 + R.DOOR_X1) / 2, R.D, 1.0), np.float32)


class Env:
    def __init__(self, cfg, cast):
        self.dust = Precip('dust', n=70, color=(255, 230, 190, 80), fall=.04, drift=.05, size=.005)
        self._grid = None
        self._chars = []
        self.cast = cast

    def step(self, t, dt, n):
        pass

    def top(self, c, ctx):
        self.dust.draw(c, ctx)
        if ctx.t < R.CUT:
            self.draw_contract(c, ctx)          # Still on the floor where it fell in Scene 02.
        else:
            self.draw_phone_props(c, ctx)

    # ---------------- the receiver, its coiled cord, the token
    def receiver(self, t):
        """Centre and long axis of the receiver in the world."""
        up = np.array([0, 0, 1.0])
        if t < R.LIFT:
            return np.array(R.CRADLE), up
        pup = self.cast['sidar'] if t < R.HANDOVER else self.cast['vehbi']
        q = pup.q
        h = q['hand'][1]
        if t < R.HANDOVER:
            d = up + q['F'] * .35
        else:
            d = (q['head'] - h) * 1.0 + up * .1
        d = d / (np.linalg.norm(d) + 1e-9)
        return h + up * .02 + d * .03, d

    def draw_phone_props(self, c, ctx):
        cam, t = ctx.cam, ctx.t
        cen, d = self.receiver(t)
        a, b = cen - d * .1, cen + d * .1
        if cam.depth(a) < .15 or cam.depth(b) < .15:
            return
        k = cam.scale(cen)
        g = self.gain_at(cen, t)
        col = lambda rgb: skia.Color(*[int(min(255, v * gg)) for v, gg in zip(rgb, g)])
        # The coiled cord: from the port under the phone to the receiver's lower end, sagging, in tight loops.
        p0, p1 = np.array(R.CORD_PORT), a
        n = 90
        pts = []
        for i in range(n + 1):
            u = i / n
            p = p0 + (p1 - p0) * u + np.array([0, 0, -.22 * math.sin(math.pi * u)])
            q = cam.pt(p)
            pts.append(q)
        path = skia.Path()
        coil = max(.012 * cam.scale((p0 + p1) / 2), .8)
        for i, q in enumerate(pts):
            if i == 0:
                path.moveTo(float(q[0]), float(q[1]))
                continue
            dx, dy = q[0] - pts[i - 1][0], q[1] - pts[i - 1][1]
            ln = math.hypot(dx, dy) + 1e-6
            off = coil * math.sin(i * 2.1)
            path.lineTo(float(q[0] - dy / ln * off), float(q[1] + dx / ln * off))
        c.drawPath(path, skia.Paint(AntiAlias=True, Style=skia.Paint.kStroke_Style, StrokeWidth=max(.006 * k, 1.0), Color=col((26, 34, 26))))
        # The receiver: a handle with an earpiece and a mouthpiece.
        sa, sb = cam.pt(a), cam.pt(b)
        ink = skia.Paint(AntiAlias=True, Style=skia.Paint.kStroke_Style, StrokeCap=skia.Paint.kRound_Cap, StrokeWidth=max(.05 * k, 2.0), Color=skia.Color(20, 22, 20))
        c.drawLine(float(sa[0]), float(sa[1]), float(sb[0]), float(sb[1]), ink)
        body = skia.Paint(AntiAlias=True, Style=skia.Paint.kStroke_Style, StrokeCap=skia.Paint.kRound_Cap, StrokeWidth=max(.038 * k, 1.5), Color=col((44, 70, 40)))
        c.drawLine(float(sa[0]), float(sa[1]), float(sb[0]), float(sb[1]), body)
        for q in (sa, sb):
            r = max(.036 * k, 1.5)
            c.drawCircle(float(q[0]), float(q[1]), r, skia.Paint(AntiAlias=True, Color=skia.Color(20, 22, 20)))
            c.drawCircle(float(q[0]), float(q[1]), r * .8, skia.Paint(AntiAlias=True, Color=col((52, 82, 48))))
        # The token: shown in Sidar's fingers, then into the slot.
        if R.COIN_SHOW <= t < R.COIN_IN + .15:
            h = self.cast['sidar'].q['hand'][1] + np.array([0, 0, .05])
            if t >= R.COIN_IN - .45:
                u = min((t - (R.COIN_IN - .45)) / .6, 1.0)
                u = u * u * (3 - 2 * u)
                p = h + (np.array(R.SLOT) - h) * u
            else:
                p = h
            if cam.depth(p) > .1:
                q = cam.pt(p)
                r = max(.0135 * cam.scale(p), 1.2)
                c.drawCircle(float(q[0]), float(q[1]), r, skia.Paint(AntiAlias=True, Color=col((214, 170, 74))))
                c.drawCircle(float(q[0]), float(q[1]), r, skia.Paint(AntiAlias=True, Style=skia.Paint.kStroke_Style, StrokeWidth=max(r * .12, .8), Color=skia.Color(70, 50, 20)))
                c.drawCircle(float(q[0]), float(q[1]), r * .28, skia.Paint(AntiAlias=True, Color=skia.Color(40, 30, 16)))

    def draw_contract(self, c, ctx):
        """The rental contract slipping out of the book: tumbling as it drifts down, then lying flat on the vinyl."""
        x, y, z, ang, u = 2.64, 3.30, .004, 0.0, 1.0
        cam = ctx.cam
        hw, hl = .105, .15
        # Tilted while it falls, flat once it lands.
        pitch = (1 - u) * 1.1 + ang
        yaw = .35 + ang * .6
        cu, su, cp, sp = math.cos(yaw), math.sin(yaw), math.cos(pitch), math.sin(pitch)
        ex = np.array([cu, su, 0.0]) * hw
        ey = (np.array([-su, cu, 0.0]) * cp + np.array([0, 0, 1.0]) * sp) * hl
        p0 = np.array([x, y, z])
        corners = [p0 + ex + ey, p0 - ex + ey, p0 - ex - ey, p0 + ex - ey]
        if any(cam.depth(q) < .1 for q in corners):
            return
        pts = [cam.pt(q) for q in corners]
        path = skia.Path()
        path.moveTo(*map(float, pts[0]))
        for q in pts[1:]:
            path.lineTo(*map(float, q))
        path.close()
        g = self.gain_at(p0, ctx.t)
        paper = tuple(int(min(255, v * k)) for v, k in zip((240, 236, 224), g))
        c.drawPath(path, skia.Paint(AntiAlias=True, Color=skia.Color(*paper)))
        k = cam.scale(p0)
        c.drawPath(path, skia.Paint(AntiAlias=True, Style=skia.Paint.kStroke_Style, StrokeWidth=max(.006 * k, 1.0), Color=skia.Color(40, 32, 28)))
        # Printed lines and the stamp, as marks only: nothing readable.
        for i in range(5):
            f = .55 - i * .22
            a = p0 + ey * f + ex * .7
            b = p0 + ey * f - ex * (.7 if i else .2)
            c.drawLine(*map(float, cam.pt(a)), *map(float, cam.pt(b)), skia.Paint(AntiAlias=True, StrokeWidth=max(.004 * k, .7), Color=skia.Color(120, 112, 100)))
        sq = p0 + ey * .75 + ex * .62
        r = max(.018 * k, 1.5)
        q = cam.pt(sq)
        c.drawRect(skia.Rect(float(q[0] - r), float(q[1] - r), float(q[0] + r), float(q[1] + r)), skia.Paint(AntiAlias=True, Color=skia.Color(150, 60, 50)))

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
        self._cut(c, ctx, pup)
        self._record(c, ctx, pup)

    def _cut(self, c, ctx, pup):
        """The door wall hides whoever is on its other side, except through the open doorway. The engine places a character
        at one depth, so someone pressed against the far side of a wall would show through it; this cuts them exactly."""
        if ctx.cam.pos[0] > 15:
            return                               # The basement has no door wall.
        cam_in = ctx.cam.pos[1] < R.D
        py = float(pup.root[1])
        if abs(py - R.D) < .35 or (py < R.D) == cam_in:
            return
        wx, wy, wz = self.world(ctx)
        keep = (wy > R.D + .06) if cam_in else (wy < R.D - .06)
        a = np.where(keep, 255, 0).astype(np.uint8)
        rgba = np.dstack([a, a, a, a])
        img = skia.Image.fromarray(rgba, colorType=skia.ColorType.kRGBA_8888_ColorType)
        c.drawImage(img, 0, 0, skia.SamplingOptions(), skia.Paint(BlendMode=skia.BlendMode.kDstIn))

    def _record(self, c, ctx, pup):
        """Remember where this character covers the frame, and the light at its own position, so post lights the
        character as one body: lit by where it stands, not by whatever wall happens to be behind each pixel."""
        try:
            snap = c.getSurface().makeImageSnapshot().toarray(colorType=skia.ColorType.kRGBA_8888_ColorType)
        except Exception:
            return
        alpha = snap[..., 3].astype(np.float32) / 255
        chest = pup.root + np.array([0, 0, 1.0])
        self._chars.append((alpha, self.gain_at(chest, ctx.t), ctx.cam.depth(chest)))

    def gain_at(self, p, t):
        x, y, z = (np.array([float(v)], np.float32) for v in p)
        g = self.gain(x, y, z, t)
        return g[0]

    def gain(self, wx, wy, wz, t):
        """RGB gain of the lamp pool inside, and of the cold corridor with warm spill from the door, at world points."""
        d2 = (wx - LAMP[0]) ** 2 + (wy - LAMP[1]) ** 2 + ((wz - LAMP[2]) * 1.25) ** 2
        pool = np.exp(-d2 / REACH ** 2) * np.where(wz > LAMP[2] + .1, .55, 1.0)
        room = AMB + (1 - AMB) * pool[..., None] * WARM / WARM.max()
        room = room * (WARM ** pool[..., None])
        op = R.door_open(t)
        dd = (wx - DOOR_C[0]) ** 2 + (wy - DOOR_C[1]) ** 2 * .6 + (wz - DOOR_C[2]) ** 2 * .5
        spill = op * np.exp(-dd / 1.6)[..., None] * .7
        corr = COLD * (.62 + spill * .4) * (1 - spill) + WARM * .72 * spill
        out = np.where((wy < R.D + .03)[..., None], room, corr)
        # The basement: one bare bulb, swinging, stuttering once the line crosses.
        bx, by, bz = R.bulb(t)
        b2 = (wx - bx) ** 2 + (wy - by) ** 2 + ((wz - bz) * 1.1) ** 2
        bp = np.exp(-b2 / 2.5 ** 2) * R.flicker(t)
        base = BAMB * (.75 + .25 * R.flicker(t))
        bas = base + (1 - base) * bp[..., None] * BWARM / BWARM.max()
        bas = bas * (BWARM ** bp[..., None])
        return np.where((wx > 15)[..., None], bas, out)

    def post(self, pic, ctx):
        cam, H, W = ctx.cam, ctx.H, ctx.W
        wx, wy, wz = self.world(ctx)
        u, v = self._grid
        gain = self.gain(wx, wy, wz, ctx.t)
        # Characters, far to near, each lit as one body where the set doesn't hide it.
        zb = ctx.zb
        for alpha, g, dist in self._chars:
            a = (alpha * (zb >= dist - .55))[..., None]
            gain = gain * (1 - a) + g[None, None, :] * a
        self._chars = []
        # A soft vignette pulls the eye to the light.
        vg = 1 - .28 * (((u - W / 2) / (W / 2)) ** 2 + ((v - H / 2) / (H / 2)) ** 2)[..., None]
        out = pic.astype(np.float32) * gain * vg
        out = np.clip(out, 0, 255).astype(np.uint8)
        f = R.fold(ctx.t)
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
