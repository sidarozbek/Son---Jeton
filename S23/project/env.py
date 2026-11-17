"""Scene 23: the exam hall. Even, cool morning light; brighter towards the windows on the left.
Drawn here: the exam sheets on the desks and the pen in Vehbi's hand; the question INSERT (Vehbi's exam sheet, full
frame, the current question marked, his earlier answers already written); and the stamp FLASHES (D1, D5, D6, D8,
each the clipping as first shown, slammed in fast)."""
import math

import cv2
import numpy as np
import skia
from PIL import Image, ImageDraw, ImageFont

import room as R
import stamp

AIR = np.array((1.02, 1.02, 1.04), np.float32)
INK = (30, 30, 36)
PEN_BLUE = (34, 52, 150)
SANS_B = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
SANS = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
SERIF = '/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf'
HAND = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Oblique.ttf'


def _f(p, s):
    return ImageFont.truetype(p, int(s))


def _ease(u):
    u = min(max(u, 0.0), 1.0)
    return u * u * (3 - 2 * u)


class Env:
    def __init__(self, cfg, cast):
        self._grid = None
        self.cast = cast
        self._sheet = {}

    def step(self, t, dt, n):
        pass

    # ---------------- the sheets on the desks
    def behind(self, c, ctx):
        cam = ctx.cam
        for x, y in R.ALL_DESKS:
            p = [np.array([x + dx, y + dy, R.DESK_H + .002]) for dx, dy in ((-.15, -.2), (.15, -.2), (.15, .2), (-.15, .2))]
            if min(cam.depth(q) for q in p) < .3:
                continue
            q = [cam.pt(v) for v in p]
            path = skia.Path()
            path.addPoly([skia.Point(float(a), float(b)) for a, b in q], True)
            c.drawPath(path, skia.Paint(AntiAlias=True, Color=skia.Color(246, 244, 236)))
            c.drawPath(path, skia.Paint(AntiAlias=True, Style=skia.Paint.kStroke_Style, StrokeWidth=1.0, Color=skia.Color(*INK, 120)))
            for k in range(5):
                yy = y + .14 - k * .07
                a, b = cam.pt(np.array([x - .11, yy, R.DESK_H + .003])), cam.pt(np.array([x + .1, yy, R.DESK_H + .003]))
                c.drawLine(a[0], a[1], b[0], b[1], skia.Paint(AntiAlias=True, StrokeWidth=.8, Color=skia.Color(120, 120, 130, 160)))

    def on_actor(self, c, ink, ctx, pup):
        if pup is self.cast['vehbi'] and ctx.t < R.PEN_DOWN:
            cam = ctx.cam
            h = pup.q['hand'][1]
            if cam.depth(h) > .3:
                a, b = cam.pt(h + np.array([-.02, .03, -.04])), cam.pt(h + np.array([.03, -.04, .1]))
                c.drawLine(a[0], a[1], b[0], b[1], skia.Paint(AntiAlias=True, StrokeWidth=max(.012 * cam.scale(h), 1.5),
                                                              StrokeCap=skia.Paint.kRound_Cap, Color=skia.Color(30, 50, 140)))
        d = ctx.cam.depth(pup.root + np.array([0, 0, 1.0]))          # Desks nearer than a character hide it.
        keep = ctx.zb.astype(np.float32) > d - .14
        al = np.where(keep, 255, 0).astype(np.uint8)
        img = skia.Image.fromarray(np.dstack([al, al, al, al]), colorType=skia.ColorType.kRGBA_8888_ColorType)
        c.drawImage(img, 0, 0, skia.SamplingOptions(), skia.Paint(BlendMode=skia.BlendMode.kDstIn))

    # ---------------- the exam sheet insert
    def sheet(self, W, H, k, t):
        """Vehbi's exam sheet: the header, four questions; answers before k written; question k marked."""
        done = tuple(j for j in range(4) if t >= R.L[j] + 1.6)
        key = (W, H, k, done)
        if key not in self._sheet:
            im = Image.new('RGB', (W, H), (70, 56, 44))
            d = ImageDraw.Draw(im)
            x0, x1 = int(W * .06), int(W * .94)
            d.rectangle((x0, int(H * .03), x1, H), fill=(248, 246, 238))
            d.text((W / 2, H * .1), 'TÜRKİYE EKONOMİSİ · SINAV', font=_f(SANS_B, H * .045), fill=INK, anchor='mm')
            d.text((x0 + W * .04, H * .19), 'Ad Soyad:', font=_f(SANS, H * .03), fill=INK, anchor='lm')
            d.text((x0 + W * .17, H * .19), 'Vehbi', font=_f(HAND, H * .036), fill=PEN_BLUE, anchor='lm')
            d.line((x0 + W * .03, H * .23, x1 - W * .03, H * .23), fill=(180, 176, 166), width=2)
            for j, a in enumerate(R.ANSWERS):
                y = H * (.31 + j * .17)
                if j == k:
                    d.rectangle((x0 + W * .02, y - H * .04, x1 - W * .02, y + H * .1), fill=(250, 238, 170))
                d.text((x0 + W * .04, y), a['q'], font=_f(SERIF, H * .036), fill=INK, anchor='lm')
                d.line((x0 + W * .07, y + H * .075, x1 - W * .1, y + H * .075), fill=(170, 170, 180), width=2)
                if j in done:
                    d.text((x0 + W * .08, y + H * .05), a['a'], font=_f(HAND, H * .042), fill=PEN_BLUE, anchor='lm')
            self._sheet[key] = np.array(im).astype(np.float32)
        img = self._sheet[key]
        a, b = R.Q[k]
        u = _ease((t - a) / (b - a))
        s = 1.0 + .25 * u                                                # Push in on the question.
        cx, cy = W * .45, H * (.31 + k * .17)
        M = np.float32([[s, 0, (1 - s) * cx], [0, s, (1 - s) * cy]])
        return cv2.warpAffine(img, M, (W, H), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)

    # ---------------- the stamp flashes
    def flash(self, pic, k, t):
        H, W = pic.shape[:2]
        a, b = R.FLASH[k]
        u = (t - a) / (b - a)
        A = R.ANSWERS[k]
        out = pic.astype(np.float32)
        hit = .13 / (b - a)                                              # The drop takes 0.13 s, however long the hold.
        if u < hit:                                                      # The stamp comes down.
            cx, cy = W * .66, H * .3
            yb = -H * .1 + (cy + H * .09 + H * .1) * _ease(u / hit)
            stamp.stamp_tool(out, cx, yb, 1)
            return np.clip(out, 0, 255).astype(np.uint8)
        cl = stamp.clipping(pic, A['head'], A['body'], A['date'])        # The clipping slams in.
        v = _ease((u - hit) * (b - a) / .09)
        sc = 1.12 - .12 * v
        M = cv2.getRotationMatrix2D((W / 2, H / 2), 3 * (1 - v), sc)
        cl = cv2.warpAffine(cl.astype(np.float32), M, (W, H), borderMode=cv2.BORDER_REPLICATE)
        out = out * (1 - v) + cl * v
        if abs(u - hit) * (b - a) < .035:
            out = np.roll(out, 4, axis=0)
        return np.clip(out, 0, 255).astype(np.uint8)

    def grid(self, ctx):
        H, W = ctx.H, ctx.W
        if self._grid is None or self._grid[0].shape != (H, W):
            u, v = np.meshgrid(np.arange(W, dtype=np.float32), np.arange(H, dtype=np.float32))
            self._grid = (u, v)
        return self._grid

    def post(self, pic, ctx):
        t, H, W = ctx.t, ctx.H, ctx.W
        for k, (a, b) in enumerate(R.Q):
            if a <= t < b:
                return np.clip(self.sheet(W, H, k, t), 0, 255).astype(np.uint8)
        u, v = self.grid(ctx)
        vg = 1 - .2 * (((u - W / 2) / (W / 2)) ** 2 + ((v - H / 2) / (H / 2)) ** 2)[..., None]
        out = np.clip(pic.astype(np.float32) * AIR * vg, 0, 255).astype(np.uint8)
        for k, (a, b) in enumerate(R.FLASH):
            if a <= t < b:
                return self.flash(out, k, t)
        return out
