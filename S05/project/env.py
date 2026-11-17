"""What else lives in the grocer's: the light, applied to the whole finished picture in 3D from the depth buffer.
A warm pool under the pendant bulb over the counter, the shop dimmer towards the walls, cold blue dusk at the front window.
Characters are lit as one body at their own position. The grocer stands behind the counter: the engine places a character
at one depth, so the counter would not hide his legs; on_actor cuts him wherever the set is nearer than he is."""
import math

import numpy as np
import skia

import room as R
import blocking as B

LAMP = np.array(R.LAMP, np.float32)
WARM = np.array((1.2, 1.02, .76), np.float32)
COLD = np.array((.55, .63, .86), np.float32)
AMB = .42
REACH = 2.6


class Env:
    def __init__(self, cfg, cast):
        self._grid = None
        self._chars = []
        self.cast = cast

    def step(self, t, dt, n):
        pass

    def top(self, c, ctx):
        pass

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
        if pup is self.cast['grocer']:
            self._behind_counter(c, ctx, pup)
        self._record(c, ctx, pup)

    def _behind_counter(self, c, ctx, pup):
        """Hide the grocer wherever the set in front of him (the counter, its goods) is nearer to the camera than he is."""
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
        """The bulb's warm pool over the counter; cooler and dimmer towards the walls; cold dusk near the front window."""
        d2 = (wx - LAMP[0]) ** 2 + (wy - LAMP[1]) ** 2 + ((wz - LAMP[2]) * .8) ** 2
        pool = np.exp(-d2 / REACH ** 2) * np.where(wz > LAMP[2] + .1, .6, 1.0)
        room = AMB + (1 - AMB) * pool[..., None] * WARM / WARM.max()
        room = room * (WARM ** pool[..., None])
        front = np.clip(1 - wy / 1.2, 0, 1)[..., None] * .5
        return room * (1 - front) + COLD * front

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
        return np.clip(pic.astype(np.float32) * gain * vg, 0, 255).astype(np.uint8)
