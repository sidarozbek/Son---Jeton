"""Scene 13: the flock lifts and streams out of the street door; nothing else is drawn.
Scene 12: the flock still circling; the two tokens stuck in the teller window's slot, pulled out, caught.
Scene 11: the coins turn into birds; the flock grows; birds carry coins from the newest customer to the oldest; D4.
The birds are drawn here, over the picture, as simple flapping shapes in 3D positions (original design).
What else lives in the banker's office: the light (even and warm, a pool at the teller window, daylight at the door),
Sidar's two tokens, and the cut that lets the set hide characters behind it. Light is applied to the finished picture
from the depth buffer; characters are lit as one body at their own position."""
import math

import numpy as np
import skia

import room as R
import blocking as B
import stamp

AMB = np.array((.92, .88, .80), np.float32)
WARM = np.array((1.12, 1.02, .86), np.float32)
WIN = np.array((3.0, R.D - .5, 1.6), np.float32)


class Env:
    def __init__(self, cfg, cast):
        self._grid = None
        self._chars = []
        self.cast = cast

    def step(self, t, dt, n):
        pass

    def top(self, c, ctx):
        t, cam = ctx.t, ctx.cam
        for i in range(R.flock_size(t)):
            p = self.flock_pos(i, t)
            te = R.exit_time(i)
            if t >= te:                                            # Out through the street door, and gone.
                u = (t - te) / 1.1
                if u >= 1:
                    continue
                e = u * u
                p = p + (np.array(R.DOOR_OUT) - p) * e
            elif t >= R.LIFT:                                      # The lift: everyone climbs at once.
                p = p + np.array([0, 0, .25 * min((t - R.LIFT) / .3, 1.0)])
            self.draw_bird(c, cam, p, t * (1.6 if t >= R.LIFT else 1.0), i)
        for k, (a, b) in enumerate(R.CARRIES):
            if a <= t < b:
                p = self.carry_pos(k, t)
                self.draw_bird(c, cam, p + np.array([0, 0, .08]), t, 100 + k, big=1.15)
                self.draw_coin(c, cam, p, flat=False)

    def draw_stuck(self, c, ctx):
        """Sidar's two tokens: wedged in the slot (wobbling as they tug), flying out at the pop, then in his hand."""
        t, cam = ctx.t, ctx.cam
        slot = np.array(R.SLOT)
        if t < R.POP:
            for k in (0, 1):
                p = slot + np.array([.012 * k - .006, -.012 - R.tug(t), .012 + .004 * k])
                self.draw_coin(c, cam, p, flat=False)
            return
        if t < R.CATCH:
            u = (t - R.POP) / (R.CATCH - R.POP)
            h = self.hand('sidar')
            for k in (0, 1):
                p = slot + (h - slot) * u + np.array([0, 0, .5 * math.sin(math.pi * u) + .03 * k])
                self.draw_coin(c, cam, p, flat=False)
            return
        h = self.hand('sidar')
        for k in (0, 1):
            self.draw_coin(c, cam, h + np.array([0, 0, .015 * k]), flat=False)

    # ---------------- the coins and the birds
    def hatch_time(self, i):
        a, b = R.HATCH
        return a + i * (b - a) / 4

    def flock_pos(self, i, t):
        """Bird i circling under the ceiling; the first five rise out of the coin pile when they hatch."""
        cx, cy, cz = R.FLOCK_C
        ph = i * 2.399
        rad = .7 + .5 * ((i * 37) % 10) / 10
        w = .9 + .25 * math.sin(i * 1.7)
        a = ph + t * w
        orbit = np.array([cx + rad * math.cos(a) * 1.4, cy + rad * math.sin(a), cz + .18 * math.sin(t * 2.1 + ph)])
        if i < 5:
            th = self.hatch_time(i)
            u = min(max((t - th) / .9, 0.0), 1.0)
            u = u * u * (3 - 2 * u)
            start = np.array(R.PILE) + np.array([(i - 2) * .04, 0, .05])
            return start + (orbit - start) * u
        return orbit

    def hand(self, name):
        return self.cast[name].q['hand'][1] + np.array([0, 0, .05])

    def carry_pos(self, k, t):
        a, b = R.CARRIES[k]
        u = (t - a) / (b - a)
        e = u * u * (3 - 2 * u)
        p0, p1 = self.hand('q5'), self.hand('q0')
        return p0 + (p1 - p0) * e + np.array([0, 0, .7 * math.sin(math.pi * u)])

    def draw_pile(self, c, ctx):
        t, cam = ctx.t, ctx.cam
        for i in range(5):
            if t < self.hatch_time(i):
                p = np.array(R.PILE) + np.array([(i - 2) * .04, (i % 2) * .02, .004 * (i % 3)])
                self.draw_coin(c, cam, p, flat=True)

    def draw_coin(self, c, cam, p, flat):
        if cam.depth(p) < .1:
            return
        q = cam.pt(p)
        r = max(.0135 * cam.scale(p), 1.2)
        f = .45 if flat else 1.0
        rect = skia.Rect(float(q[0] - r), float(q[1] - r * f), float(q[0] + r), float(q[1] + r * f))
        c.drawOval(rect, skia.Paint(AntiAlias=True, Color=skia.Color(214, 170, 74)))
        c.drawOval(rect, skia.Paint(AntiAlias=True, Style=skia.Paint.kStroke_Style, StrokeWidth=max(r * .12, .8), Color=skia.Color(70, 50, 20)))

    def draw_bird(self, c, cam, p, t, seed, big=1.0):
        """A small golden-brown bird: an oval body, a head, and two wings that flap."""
        if cam.depth(p) < .15:
            return
        q = cam.pt(p)
        s = max(.11 * big * cam.scale(p), 2.5)
        flap = math.sin(t * 14 + seed * 1.3)
        body = skia.Paint(AntiAlias=True, Color=skia.Color(176, 128, 58))
        dark = skia.Paint(AntiAlias=True, Color=skia.Color(110, 74, 30))
        wing = skia.Paint(AntiAlias=True, Style=skia.Paint.kStroke_Style, StrokeWidth=max(s * .22, 1.0), StrokeCap=skia.Paint.kRound_Cap, Color=skia.Color(140, 98, 40))
        x, y = float(q[0]), float(q[1])
        for sd in (-1, 1):
            path = skia.Path()
            path.moveTo(x, y)
            path.quadTo(x + sd * s * .6, y - s * (.2 + .7 * flap), x + sd * s * 1.15, y - s * .35 * flap)
            c.drawPath(path, wing)
        c.drawOval(skia.Rect(x - s * .42, y - s * .2, x + s * .42, y + s * .22), body)
        c.drawCircle(x + s * .38, y - s * .12, s * .16, dark)
        c.drawCircle(x + s * .42, y - s * .15, max(s * .04, .6), skia.Paint(AntiAlias=True, Color=skia.Color(20, 16, 10)))

    def world(self, ctx):
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
        self._behind(c, ctx, pup)
        self._record(c, ctx, pup)

    def _behind(self, c, ctx, pup):
        """Hide a character wherever the set is nearer to the camera than they are (the brass rail, the counter)."""
        d = ctx.cam.depth(pup.root + np.array([0, 0, .5]))
        keep = ctx.zb.astype(np.float32) > d - .3
        a = np.where(keep, 255, 0).astype(np.uint8)
        img = skia.Image.fromarray(np.dstack([a, a, a, a]), colorType=skia.ColorType.kRGBA_8888_ColorType)
        c.drawImage(img, 0, 0, skia.SamplingOptions(), skia.Paint(BlendMode=skia.BlendMode.kDstIn))

    def _record(self, c, ctx, pup):
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
        d2 = (wx - WIN[0]) ** 2 + (wy - WIN[1]) ** 2 + (wz - WIN[2]) ** 2
        pool = np.exp(-d2 / 2.6 ** 2)[..., None]
        g = AMB + pool * (WARM - AMB)
        door = (np.clip(1 - np.hypot(wx - 0, wy - 2.6) / 1.6, 0, 1) * .25)[..., None]
        return g + door * np.array((.0, .04, .1), np.float32)

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
        vg = 1 - .22 * (((u - W / 2) / (W / 2)) ** 2 + ((v - H / 2) / (H / 2)) ** 2)[..., None]
        out = np.clip(pic.astype(np.float32) * gain * vg, 0, 255).astype(np.uint8)
        return stamp.overlay(out, ctx.t)
