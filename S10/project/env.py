"""What else lives in the banker's office: the light (even and warm, a pool at the teller window, daylight at the door),
Sidar's two tokens, and the cut that lets the set hide characters behind it. Light is applied to the finished picture
from the depth buffer; characters are lit as one body at their own position."""
import math

import numpy as np
import skia

import room as R
import blocking as B

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
        self.draw_tokens(c, ctx)

    def draw_tokens(self, c, ctx):
        """Sidar's two remaining tokens: in his hand on the walk, then on the counter by the window."""
        t, cam = ctx.t, ctx.cam
        if t < R.TOKENS_DOWN - 1.2:
            return
        if t < R.TOKENS_DOWN:
            base = self.cast['sidar'].q['hand'][1] + np.array([0, 0, .04])
            offs = ((-.015, 0, 0), (.015, 0, .012))
        else:
            base = np.array(R.SILL) + np.array([.12, -.1, 0])
            offs = ((-.03, 0, 0), (.035, .01, 0))
        for o in offs:
            p = base + np.array(o)
            if cam.depth(p) < .1:
                continue
            q = cam.pt(p)
            r = max(.0135 * cam.scale(p), 1.2)
            flat = .45 if t >= R.TOKENS_DOWN else 1.0          # Lying flat on the counter: an ellipse.
            rect = skia.Rect(float(q[0] - r), float(q[1] - r * flat), float(q[0] + r), float(q[1] + r * flat))
            c.drawOval(rect, skia.Paint(AntiAlias=True, Color=skia.Color(214, 170, 74)))
            c.drawOval(rect, skia.Paint(AntiAlias=True, Style=skia.Paint.kStroke_Style, StrokeWidth=max(r * .12, .8), Color=skia.Color(70, 50, 20)))
            c.drawCircle(float(q[0]), float(q[1]), r * .26 * flat, skia.Paint(AntiAlias=True, Color=skia.Color(40, 30, 16)))

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
        return np.clip(pic.astype(np.float32) * gain * vg, 0, 255).astype(np.uint8)
