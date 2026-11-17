"""Son Jeton cast. Sidar: short, very wide landlord, grey hair and long grey beard, thick rectangular glasses,
grey shirt, brown vest, burgundy tie, slippers. Vehbi: short and thin student at the same height, round thin glasses,
goatee joined to a thin jaw beard, petrol green sweater, always holding an ochre textbook. See BIBLE.md.
The grocer (Scene 05 on): an original shopkeeper, bald on top, thick black moustache, beige dust coat; he never speaks."""
import math

import cv2
import numpy as np
import skia

from toonkit.camera import UP
from toonkit.core import blob, poly, union, rgb
from toonkit.presets import STOCKY, AVERAGE, design
from toonkit.camera import norm
from toonkit.puppet import Character, hand2

HEIGHT = 1.55          # Both the same height: the brief says so.


def shade(c, k=.76):
    r, g, b = (c >> 16) & 255, (c >> 8) & 255, c & 255
    return (int(r * k) << 16) | (int(g * k) << 8) | int(b * k)


def argb(c):
    return 0xFF000000 | c


def hull_of(pup, cam, pts, min_vis=-.08):
    out = []
    for lon, lat, o in pts:
        if pup.vis(cam, lon, lat) > min_vis:
            out.append(cam.pt(pup.surf(lon, lat, o)))
    if len(out) < 3:
        return None
    h = cv2.convexHull(np.array(out, np.float32)).reshape(-1, 2)
    return blob([tuple(map(float, a)) for a in h])


def lipsync_mouth(pup, ink, cam, lat, half, arch_k):
    """Redraw the mouth on top of facial hair, still driven by the voice and the jaw channel:
    the same width and height the engine gives the bare face, so speech shapes (wide, round, narrow) survive."""
    if pup.vis(cam, 0, lat) > .05:
        p = pup.p
        m = dict(h=pup.mouth['h'] + p['jaw'] + p['ts'] * .17, teeth=max(pup.mouth['teeth'], p['ts']) * .6)
        w = half * (pup.mouth['w'] * (1 + p['wide']) + .12 * max(p['smile'], 0))
        pup.mouth3d(ink, cam, lat, w, m, -p['smile'] * arch_k)


def open_drop(pup):
    """How far the jaw has dropped, in head-surface degrees: chin hair rides down with it."""
    return (pup.mouth['h'] + pup.p['jaw']) * 16


# ---------------------------------------------------------------- glasses
def glasses(shape, frame, width, rx=1.4, ry=1.55, out=.075):
    """Glasses on the head surface around each eye. shape 'rect' (squarish, superellipse) or 'round'.
    Bold graphic frame; temples run back to the ears and show in profile."""
    def fn(pup, ink, cam, sc, facing):
        if facing < -.15:
            return
        E = pup.spec['eyes']
        lon0, lat0 = E['lon'], E['lat']
        dl, dt = E['dlon'] * rx, E['dlat'] * ry
        w = max(width * sc, 1.2)
        n = 4.0 if shape == 'rect' else 2.0
        inner = {}
        for side in (-1, 1):
            cx = side * lon0
            if pup.vis(cam, cx, lat0) < .02:
                continue
            ring = []
            for a in np.linspace(0, 2 * math.pi, 33):
                ca, sa = math.cos(a), math.sin(a)
                # Superellipse: n=2 round, n=4 rounded rectangle.
                x = math.copysign(abs(ca) ** (2 / n), ca) * dl
                y = math.copysign(abs(sa) ** (2 / n), sa) * dt
                ring.append((cx + x, lat0 + y))
            pts = pup.poly_surf(cam, ring, out)
            ink.stroke(poly(pts), w, argb(frame))
            inner[side] = (cx - side * dl, lat0 + dt * .25)
            # Temple: from the outer edge back towards the ear, only when the side of the head shows.
            if abs(facing) < .85:
                t0, t1, t2 = (cx + side * dl, lat0 + dt * .3), (side * 72, lat0 + 4), (side * 90, lat0 + 1)
                if pup.vis(cam, side * 86, lat0) > .08:
                    a_, m_, b_ = pup.poly_surf(cam, [t0, t1, t2], out * .7)
                    ink.curve(a_, m_, b_, w * .8, argb(frame))
        if len(inner) == 2:
            a_, m_, b_ = pup.poly_surf(cam, [inner[-1], (0, lat0 + 2), inner[1]], out + .02)
            ink.curve(a_, m_, b_, w * .85, argb(frame))
    return fn


# ---------------------------------------------------------------- Sidar
SKIN_S = 0xC49A7A
HAIR_S = 0x8E8E8A
BEARD, MOUST = 0x9C9C98, 0x6E6E6A
SHIRT, VEST, TIE = 0x8A8E92, 0x6A4A32, 0x6E2430
SLIPPER = 0x4A3426


def vest_and_tie(x):
    """A sleeveless brown vest over the grey shirt: the whole torso in brown, a V at the front showing shirt and tie."""
    ink, c, sc = x.ink, x.c, x.sc
    ink.shape(x.pup._torso_path, VEST, shade(VEST), -20 * sc, -8 * sc)
    if x.ca > .1:
        zx = x.sa * 118 * sc
        top = x.ch + x.ax / x.m * 10 * sc
        hw = 46 * sc * x.ca
        tl, tr = top + x.n * hw + x.n * zx * .9, top - x.n * hw + x.n * zx * .9
        bot = x.h2 + x.ax * .56 + x.n * zx
        v = poly([tuple(tl), tuple(tr), tuple(bot)])
        ink.shape(v, SHIRT, None)
        c.save()
        c.clipPath(v, doAntiAlias=True)
        k0 = x.ch + x.ax / x.m * 4 * sc + x.n * zx * .92
        tw0, tw1 = 11 * sc * x.ca, 17 * sc * x.ca
        k1 = x.h2 + x.ax * .5 + x.n * zx
        tie = poly([tuple(k0 + x.n * tw0), tuple(k1 + x.n * tw1), tuple(k1 - x.n * tw1), tuple(k0 - x.n * tw0)])
        ink.shape(tie, TIE, shade(TIE), -3 * sc, -2 * sc)
        knot = k0 - x.ax / x.m * 8 * sc
        c.drawPath(skia.Path.Circle(float(knot[0]), float(knot[1]), float(13 * sc * x.ca)), skia.Paint(AntiAlias=True, Color=rgb(shade(TIE, .85))))
        c.restore()
        for u in (.42, .3, .18):
            b = x.h2 + x.ax * u + x.n * zx
            c.drawPath(skia.Path.Circle(float(b[0]), float(b[1]), float(6.5 * sc)), skia.Paint(AntiAlias=True, Color=rgb(0x3A2616)))
    else:
        b0, b1 = x.h2 + x.ax * .98, x.h2 + x.ax * .12
        ink.seg(tuple(b0), tuple(b1), max(ink.line_w * .7, 1), argb(shade(VEST, .55)))


def shirt_collar(x):
    """Shirt collar points above the vest, visible from the front and side."""
    if x.ca > -.2:
        col = x.ch + x.ax / x.m * 6 * x.sc
        r = (54 * abs(x.ca) + 50 * abs(x.sa)) * x.sc
        x.ink.shape(skia.Path.Oval(skia.Rect(col[0] - r, col[1] - 16 * x.sc, col[0] + r, col[1] + 16 * x.sc)), SHIRT, shade(SHIRT), -4 * x.sc, -3 * x.sc)


def sidar_beard(pup, ink, cam, sc, facing):
    """Long, full grey beard: one solid mass that falls well past the chin, sideburns into the hair,
    a darker moustache over it, and the mouth redrawn on top so lip-sync still reads."""
    q, K = pup.q, pup.K
    if facing < -.3:
        return
    chin = []
    for lon in range(-84, 85, 12):
        for lat in (-24, -42, -60, -78):
            if pup.vis(cam, lon, lat) > -.1:
                chin.append(cam.pt(pup.surf(lon, lat - (open_drop(pup) * .6 if lat < -40 else 0), .08)))
    # The long part: hangs below the chin, narrowing, a little forward.
    for fwd, down, rt in ((.72, 1.04, .58), (.72, 1.04, -.58), (.66, 1.18, .4), (.66, 1.18, -.4),
                          (.6, 1.28, .2), (.6, 1.28, -.2), (.56, 1.33, 0), (.15, 1.12, .5), (.15, 1.12, -.5)):
        chin.append(cam.pt(q['head'] + K * (q['Fh'] * pup.HD * fwd - q['Uh'] * pup.HH * down + q['Rh'] * pup.HW * rt)))
    pieces = []
    if len(chin) >= 3:
        h = cv2.convexHull(np.array(chin, np.float32)).reshape(-1, 2)
        pieces.append(blob([tuple(map(float, a)) for a in h]))
    for sd in (-1, 1):
        burn = hull_of(pup, cam, [(sd * lo, la, .05) for lo, la in ((64, -36), (94, -34), (94, 14), (76, 10))])
        if burn is not None:
            pieces.append(burn)
    if pieces:
        ink.shape(union(pieces), BEARD, shade(BEARD, .82), -10 * sc, -8 * sc)
        # A few strand lines so the mass reads as hair.
        if facing > .2:
            for lo, sw in ((-30, -4), (-8, 2), (14, 5), (34, 3)):
                a, m_, b = cam.pt(pup.surf(lo, -56, .09)), cam.pt(q['head'] + K * (q['Fh'] * pup.HD * .7 - q['Uh'] * pup.HH * 1.08 + q['Rh'] * pup.HW * (lo + sw) / 90)), \
                    cam.pt(q['head'] + K * (q['Fh'] * pup.HD * .58 - q['Uh'] * pup.HH * 1.22 + q['Rh'] * pup.HW * (lo + sw * 2) / 110))
                ink.curve(a, m_, b, max(ink.line_w * .55, 1), argb(shade(BEARD, .7)))
    if pup.vis(cam, 0, -40) > .04:
        lipsync_mouth(pup, ink, cam, -46, 30, 9)
        # Thin, long moustache: a narrow band over the lip that sweeps out past the mouth corners and droops at the ends.
        lift = pup.mouth['h'] * 8
        top_pts = [(2, -27), (20, -26), (40, -29), (58, -36), (70, -46)]
        bot_pts = [(72, -52), (58, -42), (40, -34), (20, -32), (2, -32)]
        for sd in (-1, 1):
            if pup.vis(cam, sd * 30, -30) < -.02:
                continue
            pts = [(sd * lo, la + lift * min(lo / 40, 1)) for lo, la in top_pts + bot_pts]
            band = poly(pup.poly_surf(cam, pts, .1))
            ink.shape(band, MOUST, None, stroke=True)


SIDAR = design(STOCKY, height=HEIGHT,
               colors=dict(skin=(SKIN_S, shade(SKIN_S)), top=(SHIRT, shade(SHIRT)), legs=(0x3A3A3E, 0x2A2A2E), line2=0xFF3A2A20),
               body=dict(SHOULDER=108, STANCE=52),
               head=dict(HW=110, HD=106, HH=124, JAW=.05),
               hair=dict(col=HAIR_S, shade=shade(HAIR_S), ears_on_top=True,
                         regions=[[(-181, 181, 44, 90)], [(70, 150, -6, 50)], [(-150, -70, -6, 50)],
                                  [(124, 181, -56, 90), (-181, -124, -56, 90)]]),
               eyes=dict(lon=27, lat=4, dlon=12, dlat=9, pupil=5.5, lid_col=0xA88262),
               brows=dict(kind='bar', thick=15, lon=(8, 50), lat=21, col=0xFF55544F),
               nose=dict(kind='ball', lat=-8, out=22, rx=24, ry=27),
               mouth=dict(lat=-46, half=22),
               leg=dict(shoe=dict(col=SLIPPER, shade=shade(SLIPPER), toe=(62, 8), rise=6)),
               torso=dict(profile=[(0, 140, 108), (.42, 146, 112), (1, 102, 86)],
                          features=[vest_and_tie, ('back_seam', dict(top=.94, bottom=.12)), ('hem', dict(W=140, D=108))]),
               head_extras=[sidar_beard, glasses('rect', 0x1E1E22, 6.0, rx=1.5, ry=1.7)],
               # Never: never looks embarrassed or sheepish (no worried brow, no shrinking eyes, no forced smile).
               limits=dict(ba=(-1, .25), eye_s=(.92, 1.2), smile=(-1, .3), ts=(0, .4)),
               contact=(.36, .25))


# ---------------------------------------------------------------- Vehbi
SKIN_V = 0xE0BC9E
HAIR_V, BEARD_V = 0x1E1A18, 0x24201C
SWEATER = 0x1F5A5C
BOOK = 0xB8862E


def vehbi_beard(pup, ink, cam, sc, facing):
    """Short dark goatee joined to a thin beard line along the jaw, and a thin moustache high on the lip; cheeks stay clean."""
    if facing < -.35:
        return
    lons = list(range(-84, 85, 6))
    jt = lambda lo: -60 + 30 * (abs(lo) / 84) ** 1.6
    jw = lambda lo: 13 * (1 - .8 * (abs(lo) / 84) ** 1.2)
    runs, cur = [], []
    for lo in lons:
        if pup.vis(cam, lo, jt(lo)) > -.02:
            cur.append(lo)
        elif cur:
            runs.append(cur)
            cur = []
    if cur:
        runs.append(cur)
    for run in runs:
        if len(run) < 2:
            continue
        # Thin at the ears, a touch wider at the chin.
        # Rises from the chin up the jaw to meet the sideburn under the ear.
        top = pup.poly_surf(cam, [(lo, jt(lo)) for lo in run], .03)
        bot = pup.poly_surf(cam, [(lo, jt(lo) - jw(lo)) for lo in run[::-1]], .035)
        ink.shape(poly(top + bot), BEARD_V, None, stroke=False)
    drop = open_drop(pup)
    g = hull_of(pup, cam, [(lo, la - drop, .05) for lo in (-20, -10, 0, 10, 20) for la in (-56, -70, -84)], -.05)
    if g is not None:
        ink.shape(g, BEARD_V, None, stroke=False)
    lipsync_mouth(pup, ink, cam, -40, 40, 24)
    # Thin moustache set high, just under the nose; it rides up with the upper lip on speech and on a smile,
    # and its ends run down the mouth corners to join the goatee.
    lift = pup.mouth['h'] * 7 + max(pup.p['smile'], 0) * 4
    for sd in (-1, 1):
        if pup.vis(cam, sd * 16, -26) < .02:
            continue
        top = [(sd * lo, la + lift * min(lo / 20, 1)) for lo, la in ((1, -23), (12, -22), (24, -24), (32, -30))]
        bot = [(sd * lo, la + lift * min(lo / 20, 1)) for lo, la in ((34, -36), (24, -29), (12, -28), (1, -29))]
        ink.shape(poly(pup.poly_surf(cam, top + bot, .04)), BEARD_V, None, stroke=False)
        a, m_, b = pup.poly_surf(cam, [(sd * 33, -33 + lift), (sd * 36, -46 - drop * .5), (sd * 22, -56 - drop)], .04)
        ink.curve(a, m_, b, max(4.5 * sc, 1.2), argb(BEARD_V))


def vehbi_back_hair(pup, ink, cam, sc, facing):
    """From behind, the hair hangs down over the nape to the shoulders. Only drawn when the back of the head shows,
    so from the front it never covers the neck or the collar."""
    if facing > -.1:
        return
    q, K = pup.q, pup.K
    pts = []
    for rt, up, fw in ((-86, -20, -30), (86, -20, -30), (-86, -150, -30), (86, -150, -30), (0, -40, -84), (0, -150, -64)):
        pts.append(cam.pt(q['head'] + K * (q['Rh'] * rt + q['Uh'] * up + q['Fh'] * fw)))
    h = cv2.convexHull(np.array(pts, np.float32)).reshape(-1, 2)
    # One piece of hair with the mass above it: drop the line where they overlap.
    ink.shape(blob([tuple(map(float, a)) for a in h]), HAIR_V, shade(HAIR_V, .6), -6 * sc, -4 * sc, stroke_clip=pup._hair_blobs(cam))


def sweater_collar(x):
    """A ribbed crew neck, one shade darker than the sweater."""
    col = x.ch - x.ax * .02
    col = col + x.ax / x.m * 10 * x.sc
    r = (46 * abs(x.ca) + 42 * abs(x.sa)) * x.sc
    x.ink.shape(skia.Path.Oval(skia.Rect(col[0] - r, col[1] - 20 * x.sc, col[0] + r, col[1] + 20 * x.sc)), shade(SWEATER, .82), shade(SWEATER, .65), -3 * x.sc, -2 * x.sc)


def textbook(pup, ink, cam, sc):
    """A thick ochre economics textbook in the hand, contract tucked inside. Never leaves this hand."""
    q = pup.q
    side = -1
    F, R = q['F'], q['R']
    h = q['hand'][side] + UP * .05 + F * .02
    hw, hh, ht = .085, .12, .024
    corners = [h + F * fx * hw + UP * uz * hh + R * rx * ht for fx in (-1, 1) for uz in (-1, 1) for rx in (-1, 1)]
    pts = np.array([cam.pt(p) for p in corners], np.float32)
    hull = cv2.convexHull(pts).reshape(-1, 2)
    ink.shape(blob([tuple(map(float, a)) for a in hull]), BOOK, shade(BOOK), -4 * sc, -3 * sc)
    # Page block: the edge opposite the spine, as a cream band.
    a, b = cam.pt(h + F * hw * .98 + UP * hh * .94), cam.pt(h + F * hw * .98 - UP * hh * .94)
    ink.seg(a, b, max(ht * 1.4 / pup.K * sc, 1.5), 0xFFEEE6D0)
    # The contract's corner sticking out of the top.
    c0, c1 = cam.pt(h + F * hw * .3 + UP * hh * 1.0), cam.pt(h + F * hw * .3 + UP * hh * 1.18)
    ink.seg(c0, c1, max(6 * sc, 1.2), 0xFFF4F1E8)


VEHBI = design(AVERAGE, height=HEIGHT,
               body=dict(NECK=30, SHOULDER=76, ARM=146, STANCE=38, STRIDE=300, LIFT=50, BOB=(8, 5), SWING=.3),
               colors=dict(skin=(SKIN_V, shade(SKIN_V)), top=(SWEATER, shade(SWEATER, .7)), legs=(0x2E3138, 0x202228), line2=argb(shade(SWEATER, .55))),
               head=dict(HW=74, HD=80, HH=114, JAW=.3, CHIN=16, neck=(36, 32), neck_base=16, ear=dict(rx=14, ry=21, lon=95, lat=-3)),
               hair=dict(col=HAIR_V, shade=shade(HAIR_V, .6),
                         regions=[[(-181, 181, 50, 90)], [(78, 150, 8, 54)], [(-150, -78, 8, 54)],
                                  [(128, 181, -40, 90), (-181, -128, -40, 90)]],
                         blobs=[(0, 0, 0, 1)]),     # Replaced by straight panels in Vehbi._hair_blobs.
               eyes=dict(lon=26, lat=4, dlon=15, dlat=12, pupil=6, soft_lid=True, lid_col=0xC49C80),
               brows=dict(kind='curve', weight=2.0, max_lat=40),
               nose=dict(kind='wedge', top=6, tip_lat=-14, out=19, bottom=-20),
               mouth=dict(lat=-40, half=40, smile_arch=24, frown_arch=14),
               arm=dict(w=(50, 38), seams=(), cuff=20),
               leg=dict(hip_w=38, w=(48, 34), folds=0xFF1A1C22,
                        shoe=dict(col=0x8C8C90, shade=0x6E6E72, toe=(64, 6), rise=8, w=(36, 28))),
               torso=dict(profile=[(0, 92, 66), (.5, 96, 70), (1, 90, 64)], hip_ext=34,
                          features=[sweater_collar, ('back_seam', dict(bottom=.12)), ('hem', dict(W=94, D=68, u=.08)),
                                    ('bands', dict(us=(.04,), W=92, D=66, bow=4))]),
               head_extras=[vehbi_back_hair, vehbi_beard, glasses('round', 0x2A2A2E, 3.2, rx=1.35, ry=1.6)],
               hand_rest=('grip', 'relaxed'),
               # Never: no panicked face, brows move little.
               limits=dict(brow=(-.4, .6), ba=(-.5, .4), eye_s=(.92, 1.08), jaw=(0, .12), smile=(-.6, .7), pup=(.9, 1.1)),
               contact=(.3, .18))


# Straight, shoulder-length hair as convex panels in the head frame (right, up, forward), so edges stay straight.
HAIR_PANELS = [
    # Back of the head, above the jaw: hidden by the head from the front.
    [(-80, 70, -10), (80, 70, -10), (0, 112, -20), (-86, -40, -30), (86, -40, -30), (0, 30, -96), (-60, -96, -60), (60, -96, -60)],
] + [
    # Side curtains: fall straight past the jaw to the shoulders, beside the neck, with a straight cut at the ends.
    [(sd * 78, 60, 8), (sd * 90, 10, -6), (sd * 90, -150, -26), (sd * 50, -150, -40), (sd * 54, -40, -46), (sd * 66, 60, -20)]
    for sd in (-1, 1)
]


class FourFingers(Character):
    """The person's rule for this show: four fingers and no thumb. The engine's hand library is thumb plus three
    fingers, so the thumb slot becomes a fourth finger fanned in beside the first, curling the same way."""

    def draw_hand(self, ink, cam, side, skin, skin_s, sc, e):
        q = self.q
        a, b = cam.pt(e), cam.pt(q['hand'][side])
        flip = -side if float(np.dot(q['F'], norm(cam.pos - q['hand'][side]))) >= 0 else side
        d = [tuple(x) for x in self.hand_now[side]]
        f1, f2, f3 = d[1], d[2], d[3]
        spread = 13
        fingers = [(max(f1[0] - spread, -29), f1[1] * .9, f1[2]),
                   (f1[0] - spread * .1, f1[1], f1[2]), (f2[0], f2[1], f2[2]), (f3[0] + 4, f3[1] * .95, f3[2])]
        # hand2 draws digit 0 last and treats it as the thumb only by angle; keep every angle above -30 so all curl as fingers.
        hand2(ink, b, math.atan2(b[1] - a[1], b[0] - a[0]), fingers, skin, skin_s, sc * 1.05, flip, ink.line_w * .92)


class Vehbi(FourFingers):
    # The book never leaves the left hand. Drawn just before that hand, so the curled fingers wrap over its edge.
    def draw_hand(self, ink, cam, side, skin, skin_s, sc, e):
        if side == -1:
            textbook(self, ink, cam, sc)
        super().draw_hand(ink, cam, side, skin, skin_s, sc, e)

    def _hair_blobs(self, cam):
        q, K = self.q, self.K
        parts = []
        for panel in HAIR_PANELS:
            pts = np.array([cam.pt(q['head'] + K * (q['Rh'] * r + q['Uh'] * u + q['Fh'] * f)) for r, u, f in panel], np.float32)
            h = cv2.convexHull(pts).reshape(-1, 2)
            parts.append(blob([tuple(map(float, a)) for a in h]))
        return union(parts)


# ---------------------------------------------------------------- The grocer (Scene 05 on; never speaks)
SKIN_G = 0xD2A27E
HAIR_G = 0x3A332C
COAT = 0xBDB49A            # The shopkeeper's beige dust coat.


def grocer_face(pup, ink, cam, sc, facing):
    """Bald on top with a dark fringe (the hair regions), and a thick black moustache that hides the upper lip."""
    if facing < -.2:
        return
    lipsync_mouth(pup, ink, cam, -42, 30, 18)
    g = hull_of(pup, cam, [(lo, la, .06) for lo in (-34, -20, -6, 6, 20, 34) for la in (-24, -34)] + [(-40, -40, .05), (40, -40, .05)], -.05)
    if g is not None:
        ink.shape(g, HAIR_G, None, stroke=False)


def coat_buttons(x):
    """A front opening and three buttons on the dust coat, and a breast pocket with a pencil."""
    if x.ca > .15:
        c, sc = x.c, x.sc
        b0, b1 = x.h2 + x.ax * .96, x.h2 + x.ax * .02
        x.ink.seg(tuple(b0), tuple(b1), max(x.ink.line_w * .6, 1), argb(shade(COAT, .6)))
        for u in (.8, .55, .3):
            b = x.h2 + x.ax * u + x.n * 6 * sc
            c.drawPath(skia.Path.Circle(float(b[0]), float(b[1]), float(6 * sc)), skia.Paint(AntiAlias=True, Color=rgb(0x6A604C)))
        pk = x.h2 + x.ax * .78 - x.n * 46 * sc * x.ca
        r = skia.Rect(float(pk[0] - 18 * sc), float(pk[1] - 4 * sc), float(pk[0] + 18 * sc), float(pk[1] + 26 * sc))
        c.drawRect(r, skia.Paint(AntiAlias=True, Color=rgb(shade(COAT, .85))))
        c.drawRect(skia.Rect(float(pk[0] + 4 * sc), float(pk[1] - 26 * sc), float(pk[0] + 10 * sc), float(pk[1] + 2 * sc)), skia.Paint(AntiAlias=True, Color=rgb(0xC8A030)))


GROCER = design(AVERAGE, height=1.68,
                body=dict(SHOULDER=96, STANCE=46),
                colors=dict(skin=(SKIN_G, shade(SKIN_G)), top=(COAT, shade(COAT, .78)), legs=(0x34302C, 0x24201E), line2=argb(shade(COAT, .5))),
                head=dict(HW=96, HD=96, HH=112, JAW=.15),
                hair=dict(col=HAIR_G, shade=shade(HAIR_G, .6), ears_on_top=True,
                          regions=[[(70, 128, -8, 26)], [(-128, -70, -8, 26)], [(124, 181, -40, -14), (-181, -124, -40, -14)]]),
                eyes=dict(lon=28, lat=6, dlon=11, dlat=9, pupil=5.5, lid_col=0xB08868),
                brows=dict(kind='bar', thick=14, lon=(8, 46), lat=22, col=0xFF2A2420),
                nose=dict(kind='ball', lat=-6, out=20, rx=20, ry=22),
                mouth=dict(lat=-44, half=24),
                torso=dict(profile=[(0, 118, 92), (.5, 120, 94), (1, 100, 80)],
                           features=[coat_buttons, ('back_seam', dict(bottom=.12)), ('hem', dict(W=120, D=94))]),
                head_extras=[grocer_face],
                contact=(.34, .22))


# ---------------------------------------------------------------- Queue people (Scene 10 on; never speak)
def queue_person(coat, hair, skin, height, bald=False):
    """A customer in the banker's queue: the grocer's build with another coat, hair and height. Generic, original."""
    regions = ([[(70, 128, -8, 26)], [(-128, -70, -8, 26)], [(124, 181, -40, -14), (-181, -124, -40, -14)]] if bald else
               [[(-181, 181, 40, 90)], [(70, 150, -6, 50)], [(-150, -70, -6, 50)], [(124, 181, -50, 90), (-181, -124, -50, 90)]])
    return design(GROCER, height=height,
                  colors=dict(skin=(skin, shade(skin)), top=(coat, shade(coat, .75)), legs=(0x2E2C2A, 0x201E1C), line2=argb(shade(coat, .5))),
                  hair=dict(col=hair, shade=shade(hair, .6), regions=regions),
                  torso=dict(features=[('back_seam', dict(bottom=.12)), ('hem', dict(W=120, D=94))]),
                  head_extras=[])


QUEUE = [queue_person(0x2E3A5A, 0x2A2420, 0xD8A884, 1.66),
         queue_person(0x6A4A30, 0x8A8A86, 0xCC9C78, 1.60, bald=True),
         queue_person(0xB0A07A, 0x3A2A1E, 0xE0B496, 1.58),
         queue_person(0x3C4A3A, 0x1E1A18, 0xC89870, 1.70),
         queue_person(0x5A2E30, 0x4A3A2E, 0xDCAE8C, 1.62),
         queue_person(0x4A4A50, 0x6A6A66, 0xD0A080, 1.64, bald=True)]


# ---------------------------------------------------------------- Vehbi's friend (Scene 24; one line)
FRIEND = queue_person(0x9A4A3A, 0x4A3224, 0xD9AB86, 1.60)


def make(cfg):
    # Scene 24: the corridor after the exam. Vehbi (with his book again), his friend, two students walking off.
    import blocking as B
    out = dict(vehbi=Vehbi(VEHBI, cfg.GROUND, th=B.V_TH0, lid=.25, ax=6, ay=250, az=30),
               friend=FourFingers(FRIEND, cfg.GROUND, th=B.F_TH0, lid=.3))
    for i in range(len(B.OTHERS)):
        out[f'o{i}'] = FourFingers(QUEUE[(i * 2 + 1) % len(QUEUE)], cfg.GROUND, th=math.pi / 2, lid=.4)
    return out
