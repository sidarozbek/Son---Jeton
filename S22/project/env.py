"""Scene 22: as Scene 21; the sixth token (draw_token) and stamp D8 with the textbook insert (stamp.py).
Scene 21: August 1989, a summer evening on the street. A river of money flows where the road was: hundreds of
banknotes drifting along it like water, under the characters, hidden where the set is nearer (the kerb, the lamp
post). The notes are original and generic: plain coloured paper with a border, an oval and a few lines; no real
currency, no portrait, no emblem. The light: low warm sun, a warm pool at the exchange office window and at the lamps.
The opening unfold is Scene 20's paper fold run backwards (fold.py)."""
import math

import cv2
import numpy as np
import skia

import room as R
import fold
import stamp

AIR = np.array((1.14, 1.05, .94), np.float32)
INK = (44, 40, 52)
NOTE_COLS = [(150, 190, 150), (140, 170, 200), (214, 170, 176), (220, 196, 128), (184, 168, 214), (200, 206, 190)]


class Env:
    def __init__(self, cfg, cast):
        self._grid = None
        self.cast = cast

    def step(self, t, dt, n):
        pass

    def behind(self, c, ctx):
        """The river: a faint green-gold sheen over the road, then the notes, far ones first."""
        t, cam, W, H = ctx.t, ctx.cam, ctx.W, ctx.H
        c.saveLayer()
        y0, y1 = R.RIVER
        sheen = [np.array(p) for p in ((R.X0, y0, .04), (R.X1, y0, .04), (R.X1, y1, .04), (R.X0, y1, .04))]
        if min(cam.depth(p) for p in sheen) > .2:
            q = [cam.pt(p) for p in sheen]
            path = skia.Path()
            path.addPoly([skia.Point(float(x), float(y)) for x, y in q], True)
            c.drawPath(path, skia.Paint(AntiAlias=True, Color=skia.Color(120, 150, 120, 110)))
        items = []
        for j in range(R.N_NOTES):
            x, y, z, yaw, tilt = R.note(j, t)
            p = np.array([x, y, z])
            d = cam.depth(p)
            if d < .4 or d > 45:
                continue
            items.append((d, j, p, yaw, tilt))
        items.sort(key=lambda a: -a[0])
        for d, j, p, yaw, tilt in items:
            self.draw_note(c, cam, p, yaw, tilt, NOTE_COLS[R.NOTES[j]['col']])
        zb = ctx.zb.astype(np.float32)
        # Hide the river where the set is nearer: compare with the depth of the road surface under each pixel.
        u, v = self.grid(ctx)
        ox, oy = (u - W / 2) / cam.F, (H / 2 - v) / cam.F
        dz = cam.f[2] + cam.r[2] * ox + cam.u[2] * oy
        s = np.where(dz < -1e-3, (.08 - cam.pos[2]) / np.minimum(dz, -1e-3), 1e4).astype(np.float32)
        a = np.where(zb > s - .3, 255, 0).astype(np.uint8)
        mask = skia.Image.fromarray(np.dstack([a, a, a, a]), colorType=skia.ColorType.kRGBA_8888_ColorType)
        c.drawImage(mask, 0, 0, skia.SamplingOptions(), skia.Paint(BlendMode=skia.BlendMode.kDstIn))
        c.restore()

    def draw_note(self, c, cam, p, yaw, tilt, col):
        cy_, sy_, ct, st_ = math.cos(yaw), math.sin(yaw), math.cos(tilt), math.sin(tilt)

        def Wp(x, y):
            yy, zz = y * ct, y * st_
            return p + np.array([x * cy_ - yy * sy_, x * sy_ + yy * cy_, zz])

        S = 2.2                                                     # Cartoon-big: a river needs big notes.
        corners = [Wp(-.08 * S, -.035 * S), Wp(.08 * S, -.035 * S), Wp(.08 * S, .035 * S), Wp(-.08 * S, .035 * S)]
        q = [cam.pt(v) for v in corners]
        path = skia.Path()
        path.addPoly([skia.Point(float(x), float(y)) for x, y in q], True)
        c.drawPath(path, skia.Paint(AntiAlias=True, Color=skia.Color(*col)))
        sc = cam.scale(p)
        if sc * .16 * S < 6:                                            # Far away: just the coloured slip.
            return
        lw = max(min(.006 * sc, 1.6), .5)
        dark = tuple(int(v * .6) for v in col)
        inner = [cam.pt(Wp(x * S, y * S)) for x, y in ((-.07, -.027), (.07, -.027), (.07, .027), (-.07, .027))]
        ip = skia.Path()
        ip.addPoly([skia.Point(float(x), float(y)) for x, y in inner], True)
        c.drawPath(ip, skia.Paint(AntiAlias=True, Style=skia.Paint.kStroke_Style, StrokeWidth=lw, Color=skia.Color(*dark)))
        o = cam.pt(Wp(.035 * S, 0))
        r = max(.018 * S * sc, 1.0)
        c.drawOval(skia.Rect(o[0] - r, o[1] - r * .8, o[0] + r, o[1] + r * .8), skia.Paint(AntiAlias=True, Style=skia.Paint.kStroke_Style, StrokeWidth=lw, Color=skia.Color(*dark)))
        for k in range(3):
            a, b = cam.pt(Wp(-.06 * S, (-.015 + k * .015) * S)), cam.pt(Wp(-.005 * S, (-.015 + k * .015) * S))
            c.drawLine(a[0], a[1], b[0], b[1], skia.Paint(AntiAlias=True, StrokeWidth=lw, Color=skia.Color(*dark)))
        c.drawPath(path, skia.Paint(AntiAlias=True, Style=skia.Paint.kStroke_Style, StrokeWidth=lw * 1.2, Color=skia.Color(*INK, 160)))

    def grid(self, ctx):
        H, W = ctx.H, ctx.W
        if self._grid is None or self._grid[0].shape != (H, W):
            u, v = np.meshgrid(np.arange(W, dtype=np.float32), np.arange(H, dtype=np.float32))
            self._grid = (u, v)
        return self._grid

    # ---------------- Scene 22: the sixth token
    def hand(self):
        return self.cast['vehbi'].q['hand'][1] + np.array([0, 0, .04])

    def top(self, c, ctx):
        if ctx.t < R.HOP[1]:
            self.draw_token(c, ctx, np.array(R.token(ctx.t, tuple(self.hand()))))

    def draw_token(self, c, ctx, p):
        t, cam = ctx.t, ctx.cam
        if cam.depth(p) < .2:
            return
        q = cam.pt(p)
        r = max(.032 * cam.scale(p), 2.5)
        sq = .6 + .4 * abs(math.sin(t * 3.1))                         # Turning as it goes.
        rect = skia.Rect(float(q[0] - r), float(q[1] - r * sq), float(q[0] + r), float(q[1] + r * sq))
        c.drawOval(rect, skia.Paint(AntiAlias=True, Color=skia.Color(226, 184, 80)))
        c.drawOval(rect, skia.Paint(AntiAlias=True, Style=skia.Paint.kStroke_Style, StrokeWidth=max(r * .12, 1.0), Color=skia.Color(80, 56, 20)))
        c.drawCircle(q[0], q[1], r * .26 * sq, skia.Paint(AntiAlias=True, Color=skia.Color(50, 36, 14)))
        g = min(max((t - R.GLINT) / .4, 0.0), 1.0)
        if g > 0:                                                     # The glint: a four-point star that turns.
            k = g * (.7 + .3 * math.sin(t * 7))
            L = r * (2.2 + 1.2 * k)
            a = t * 1.5
            path = skia.Path()
            for i in range(8):
                rr = L if i % 2 == 0 else r * .3
                ang = a + i * math.pi / 4
                x, y = q[0] - r * .3 + rr * math.cos(ang), q[1] - r * .3 * sq + rr * math.sin(ang)
                path.moveTo(x, y) if i == 0 else path.lineTo(x, y)
            path.close()
            c.drawPath(path, skia.Paint(AntiAlias=True, Color=skia.Color(255, 250, 220, int(220 * k))))

    def on_actor(self, c, ink, ctx, pup):
        """Hide a character wherever the set is nearer to the camera (the lamp post, the kerb).
        Scene 22: once caught, the token is drawn with Vehbi, in his hand."""
        if pup is self.cast['vehbi'] and ctx.t >= R.HOP[1]:
            self.draw_token(c, ctx, self.hand())
        d = ctx.cam.depth(pup.root + np.array([0, 0, .5]))
        keep = ctx.zb.astype(np.float32) > d - .3
        a = np.where(keep, 255, 0).astype(np.uint8)
        img = skia.Image.fromarray(np.dstack([a, a, a, a]), colorType=skia.ColorType.kRGBA_8888_ColorType)
        c.drawImage(img, 0, 0, skia.SamplingOptions(), skia.Paint(BlendMode=skia.BlendMode.kDstIn))

    def post(self, pic, ctx):
        H, W = ctx.H, ctx.W
        u, v = self.grid(ctx)
        warm = (1 + .1 * np.clip(1 - u / W, 0, 1))[..., None]                                          # Sun from the left.
        vg = 1 - .22 * (((u - W / 2) / (W / 2)) ** 2 + ((v - H / 2) / (H / 2)) ** 2)[..., None]
        out = np.clip(pic.astype(np.float32) * AIR * warm * vg, 0, 255).astype(np.uint8)
        return stamp.overlay(out, ctx.t)
