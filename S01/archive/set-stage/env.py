"""What else lives in the room. The lamp light is applied to the whole finished picture in 3D, from the depth buffer,
so the set and the characters share one pool of warm light; the corridor stays cold until the door opens."""
import numpy as np
import skia

from toonkit.fx import Precip
import room as R

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

    def step(self, t, dt, n):
        pass

    def top(self, c, ctx):
        self.dust.draw(c, ctx)

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

    def post(self, pic, ctx):
        cam, H, W = ctx.cam, ctx.H, ctx.W
        wx, wy, wz = self.world(ctx)
        u, v = self._grid
        d2 = (wx - LAMP[0]) ** 2 + (wy - LAMP[1]) ** 2 + ((wz - LAMP[2]) * 1.25) ** 2
        pool = np.exp(-d2 / REACH ** 2)
        # Under the shade is brightest; above it the cone throws less.
        pool *= np.where(wz > LAMP[2] + .1, .55, 1.0)
        room = AMB + (1 - AMB) * pool[..., None] * WARM[None, None, :] / WARM.max()
        room = room * (WARM ** pool[..., None])
        # Corridor: cold and dim, with warm spill through the door in proportion to how open it is.
        op = R.door_open(ctx.t)
        dd = (wx - DOOR_C[0]) ** 2 + (wy - DOOR_C[1]) ** 2 * .6 + (wz - DOOR_C[2]) ** 2 * .5
        spill = op * np.exp(-dd / 1.6)[..., None] * .7
        corr = COLD * (.62 + spill * .4) * (1 - spill) + WARM * .72 * spill
        inside = (wy < R.D + .03)[..., None]
        gain = np.where(inside, room, corr)
        # A soft vignette pulls the eye to the light.
        vg = 1 - .28 * (((u - W / 2) / (W / 2)) ** 2 + ((v - H / 2) / (H / 2)) ** 2)[..., None]
        out = pic.astype(np.float32) * gain * vg
        return np.clip(out, 0, 255).astype(np.uint8)
