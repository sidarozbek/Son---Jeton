"""Scene 24: the corridor, late morning. Even light, brighter towards the window at the far end. At the end, black."""
import numpy as np
import skia

import room as R

AIR = np.array((1.03, 1.02, 1.0), np.float32)


class Env:
    def __init__(self, cfg, cast):
        self._grid = None
        self.cast = cast

    def step(self, t, dt, n):
        pass

    def on_actor(self, c, ink, ctx, pup):
        """Hide a character wherever the set is nearer (the door frame, the door leaf)."""
        d = ctx.cam.depth(pup.root + np.array([0, 0, .5]))
        keep = ctx.zb.astype(np.float32) > d - .3
        a = np.where(keep, 255, 0).astype(np.uint8)
        img = skia.Image.fromarray(np.dstack([a, a, a, a]), colorType=skia.ColorType.kRGBA_8888_ColorType)
        c.drawImage(img, 0, 0, skia.SamplingOptions(), skia.Paint(BlendMode=skia.BlendMode.kDstIn))

    def post(self, pic, ctx):
        H, W = ctx.H, ctx.W
        if ctx.t >= R.BLACK:                                        # Black. Nothing after it.
            return np.zeros_like(pic)
        if self._grid is None or self._grid[0].shape != (H, W):
            u, v = np.meshgrid(np.arange(W, dtype=np.float32), np.arange(H, dtype=np.float32))
            self._grid = (u, v)
        u, v = self._grid
        vg = 1 - .24 * (((u - W / 2) / (W / 2)) ** 2 + ((v - H / 2) / (H / 2)) ** 2)[..., None]
        return np.clip(pic.astype(np.float32) * AIR * vg, 0, 255).astype(np.uint8)
