"""Scene 09: the street on the morning of 12 September 1980. No snow, no warm light, nothing fantastic: flat grey
daylight over everything, a little brighter towards the open sky. The third token is drawn here; the stamp and the
clipping come from stamp.py at the end of post."""
import math

import cv2
import numpy as np
import skia

from toonkit.fx import Precip
import room as R
import blocking as B
import stamp

AIR = np.array((.78, .8, .84), np.float32)       # Grey morning.       # Dusk ambient, RGB gain.
WARM = np.array((1.3, 1.04, .7), np.float32)      # The shop window.
LAMPC = np.array((1.12, .98, .78), np.float32)     # The street lamp.
WIN = np.array(R.WIN_LIGHT, np.float32)
LMP = np.array(R.LAMP_HEAD, np.float32)


class Env:
    def __init__(self, cfg, cast):
        self._grid = None
        self._chars = []
        self.cast = cast

    def step(self, t, dt, n):
        pass

    def top(self, c, ctx):
        self.draw_token(c, ctx)

    def draw_token(self, c, ctx):
        """The third token: held up in Sidar's fingers, then into the slot."""
        t, cam = ctx.t, ctx.cam
        if not (R.TOKEN_OUT <= t < R.COIN_IN + .15):
            return
        h = self.cast['sidar'].q['hand'][1] + np.array([0, 0, .05])
        u = min(max((t - (R.COIN_IN - .45)) / .6, 0.0), 1.0)
        u = u * u * (3 - 2 * u)
        p = h + (np.array(R.SLOT) - h) * u
        if cam.depth(p) < .1:
            return
        q = cam.pt(p)
        r = max(.0135 * cam.scale(p), 1.2)
        c.drawCircle(float(q[0]), float(q[1]), r, skia.Paint(AntiAlias=True, Color=self._col(p, t, (214, 170, 74))))
        c.drawCircle(float(q[0]), float(q[1]), r, skia.Paint(AntiAlias=True, Style=skia.Paint.kStroke_Style, StrokeWidth=max(r * .12, .8), Color=skia.Color(70, 50, 20)))
        c.drawCircle(float(q[0]), float(q[1]), r * .28, skia.Paint(AntiAlias=True, Color=skia.Color(40, 30, 16)))

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
        """Flat grey daylight, a touch brighter higher up; the sky left as painted."""
        lift = np.clip(wz / 9.0, 0, 1)[..., None] * .08
        out = AIR[None, None, :] + lift if np.ndim(wx) == 2 else AIR[None, :] + lift
        far = (np.hypot(wx - 6, wy - 3) > 40)[..., None]
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
        return stamp.overlay(out, ctx.t)


