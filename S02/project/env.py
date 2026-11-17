"""What else lives in the room. The lamp light is applied to the whole finished picture in 3D, from the depth buffer,
so the set and the characters share one pool of warm light; the corridor stays cold until the door opens."""
import numpy as np
import skia

from toonkit.fx import Precip
import room as R
import blocking as B
import math

LAMP = np.array(R.LAMP, np.float32)
WARM = np.array((1.18, 1.0, .76), np.float32)     # RGB gain at the heart of the pool.
COLD = np.array((.62, .70, .86), np.float32)      # The corridor at night.
AMB = .36                                         # The room far from the lamp.
REACH = 2.3                                       # Metres for the pool to fall off.
DOOR_C = np.array(((R.DOOR_X0 + R.DOOR_X1) / 2, R.D, 1.0), np.float32)


class Env:
    def __init__(self, cfg, cast):
        self.dust = Precip('dust', n=70, color=(255, 230, 190, 80), fall=.04, drift=.05, size=.005)
        self._grid = None
        self._chars = []

    def step(self, t, dt, n):
        pass

    def top(self, c, ctx):
        self.dust.draw(c, ctx)
        self.draw_contract(c, ctx)

    def draw_contract(self, c, ctx):
        """The rental contract slipping out of the book: tumbling as it drifts down, then lying flat on the vinyl."""
        st = B.contract(ctx.t)
        if st is None:
            return
        x, y, z, ang, u = st
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
        return np.where((wy < R.D + .03)[..., None], room, corr)

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
        return np.clip(out, 0, 255).astype(np.uint8)
