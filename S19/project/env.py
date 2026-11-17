"""Scene 19: as Scene 18; ship A's container lids swing open and invoices rain out (draw_sheets); D7 from stamp.py.
Scene 18: as Scene 16, with the officer's ledger on the counter (draw_form) and a pen before the stamp.
Scene 17: as Scene 16; the "Sınavda çıkar" stamp D6 and the textbook insert from stamp.py, last in post.
Scene 16: the harbour, by the customs post. New ships come out of the filing cabinet (room.ship_state).
Scene 15: the harbour. The see-through ships are drawn here, under the characters, over the set plate.
Each ship is an original, plain little cargo ship: a hull with a raked bow, a deckhouse aft with a funnel, a row of
containers. Every face is paper-pale and see-through, with faint ruled lines on the hull like a form, and an ink edge.
They are hidden wherever the set is nearer to the camera (the quay edge, bollards), from a depth map of their faces.
Where Vehbi's hand is inside ship A's hull, the hull side is drawn again over the hand, so the fingers sit inside it;
rings spread on the hull where the hand went in. Light: an even, bright sea-side day, in post."""
import math

import cv2
import numpy as np
import skia

import room as R
import blocking as B
import stamp

AIR = np.array((1.0, 1.0, .98), np.float32)
PAPER = (238, 240, 230)
INK = (44, 56, 72)
RULE = (120, 150, 196)
MARGIN = (200, 80, 70)


def _rot(yaw, roll):
    cy, sy, cr, sr = math.cos(yaw), math.sin(yaw), math.cos(roll), math.sin(roll)
    Rr = np.array([[1, 0, 0], [0, cr, -sr], [0, sr, cr]])
    Ry = np.array([[cy, -sy, 0], [sy, cy, 0], [0, 0, 1]])
    return Ry @ Rr


def ship_geometry(s):
    """Faces in ship space (x forward, y to port, z up from the waterline). Returns (faces, edges, rules).
    faces: list of (kind, [points]); edges: polylines to ink; rules: hull-side line segments (paper ruling)."""
    L, Bm, D = s['L'], s['B'], s['deck']
    bow = Bm * 1.3
    xs = list(np.arange(-L / 2, L / 2 - bow, 1.0)) + [L / 2 - bow + bow * u for u in (0, .35, .62, .84, 1.0)]
    xs = sorted(set(round(x, 3) for x in xs))

    def half(x):
        if x <= L / 2 - bow:
            return Bm / 2
        u = (x - (L / 2 - bow)) / bow
        return Bm / 2 * math.sqrt(max(1 - u * u, 0))

    faces, edges, rules, soft = [], [], [], []
    port = [(x, half(x)) for x in xs]
    stbd = [(x, -half(x)) for x in xs]
    for side in (port, stbd):
        for (x0, y0), (x1, y1) in zip(side, side[1:]):
            # The deck edge rises a little towards the bow (sheer).
            z0, z1 = D + .25 * max(x0 / (L / 2), 0) ** 2, D + .25 * max(x1 / (L / 2), 0) ** 2
            faces.append(('side', [(x0, y0, 0), (x1, y1, 0), (x1, y1, z1), (x0, y0, z0)]))
        edges.append([(x, y, 0) for x, y in side])
        edges.append([(x, y, D + .25 * max(x / (L / 2), 0) ** 2) for x, y in side])
        zr = .32
        while zr < D - .1:
            rules.append([(x, y, zr) for x, y in side])
            zr += .32
    # Stern transom and deck slices.
    faces.append(('side', [(-L / 2, -Bm / 2, 0), (-L / 2, Bm / 2, 0), (-L / 2, Bm / 2, D), (-L / 2, -Bm / 2, D)]))
    edges.append([(-L / 2, -Bm / 2, 0), (-L / 2, -Bm / 2, D)])
    edges.append([(-L / 2, Bm / 2, 0), (-L / 2, Bm / 2, D)])
    for (x0, y0), (x1, y1) in zip(port, port[1:]):
        za, zb = D + .25 * max(x0 / (L / 2), 0) ** 2, D + .25 * max(x1 / (L / 2), 0) ** 2
        faces.append(('deck', [(x0, -y0, za), (x1, -y1, zb), (x1, y1, zb), (x0, y0, za)]))
    # Deckhouse aft, funnel on top; a mast forward.
    def box(kind, x0, x1, y0, y1, z0, z1, ink=True, lid=None):
        P = [(x0, y0, z0), (x1, y0, z0), (x1, y1, z0), (x0, y1, z0), (x0, y0, z1), (x1, y0, z1), (x1, y1, z1), (x0, y1, z1)]
        for q in ((0, 1, 5, 4), (1, 2, 6, 5), (2, 3, 7, 6), (3, 0, 4, 7), (4, 5, 6, 7)):
            top = q == (4, 5, 6, 7) and lid is not None
            faces.append((f'lid{lid}' if top else kind, [P[i] for i in q]))
        if ink:
            for a, b in ((0, 1), (1, 2), (2, 3), (3, 0), (4, 5), (5, 6), (6, 7), (7, 4), (0, 4), (1, 5), (2, 6), (3, 7)):
                (soft if ink == 'soft' else edges).append([P[a], P[b]])
    hx0, hx1 = -L / 2 + .3, -L / 2 + .3 + L * .2
    box('house', hx0, hx1, -Bm * .38, Bm * .38, D, D + 1.9)
    box('funnel', hx0 + .3, hx0 + 1.0, -.3, .3, D + 1.9, D + 2.9)
    for k in range(s['boxes']):                                   # Containers: a row, empty, you can see straight in.
        span = (L / 2 - bow) - (hx1 + .5)
        w = span / s['boxes']
        x0 = hx1 + .5 + k * w + .1
        box('box', x0, x0 + w - .25, -Bm * .3, Bm * .3, D, D + .75, ink='soft', lid=k)
    mx = L / 2 - bow * .8
    edges.append([(mx, 0, D), (mx, 0, D + 3.2)])
    edges.append([(mx, 0, D + 2.4), (hx1, 0, D + 1.9)])
    return faces, edges, rules, soft


GEOM = [ship_geometry(s) for s in R.SHIPS]


class Env:
    def __init__(self, cfg, cast):
        self._grid = None
        self._chars = []
        self.cast = cast
        self.waves = [(r.uniform(-30, 30), r.uniform(4.6, 70), r.uniform(.4, 1.1), r.uniform(0, 6.28))
                      for r in [np.random.default_rng(15)] for _ in range(140)]

    def step(self, t, dt, n):
        pass

    # ---------------- under the characters
    def behind(self, c, ctx):
        t, cam = ctx.t, ctx.cam
        self.draw_waves(c, ctx)
        self.draw_form(c, ctx)
        live = [i for i in range(len(R.SHIPS)) if R.ship_state(i, t) is not None]
        for i in sorted(live, key=lambda i: -cam.depth(np.array(R.ship_state(i, t)[0]))):
            self.draw_ship(c, ctx, i)
        self.draw_sheets(c, ctx, near=False)

    # ---------------- Scene 19: the invoices
    def split_depth(self, ctx):
        return min(ctx.cam.depth(p.root + np.array([0, 0, 1.0])) for p in (self.cast['sidar'], self.cast['vehbi']))

    def draw_sheets(self, c, ctx, near):
        t, cam = ctx.t, ctx.cam
        cut = self.split_depth(ctx)
        for j in range(R.N_SHEETS):
            st = R.sheet(j, t)
            if st is None:
                continue
            p, yaw, tilt, landed = st
            p = np.array(p)
            if j == 0 and t >= R.CATCH[0]:                       # This one goes to Sidar's hand (drawn with him).
                if t >= R.CATCH[1]:
                    continue
                u = (t - R.CATCH[0]) / (R.CATCH[1] - R.CATCH[0])
                p = p + (self.hand('sidar') - p) * (u * u * (3 - 2 * u))
            d = cam.depth(p)
            if d < .3 or (d < cut) != near:
                continue
            self.draw_sheet(c, cam, p, yaw, tilt)

    def draw_sheet(self, c, cam, p, yaw, tilt, size=1.0):
        """An invoice: a ruled form with a red stamp in the corner, .30 x .21 m, turned and tilted."""
        cy_, sy_, ct, st_ = math.cos(yaw), math.sin(yaw), math.cos(tilt), math.sin(tilt)

        def W(x, y):
            yy, zz = y * ct, y * st_
            return p + np.array([x * cy_ - yy * sy_, x * sy_ + yy * cy_, zz]) * size

        corners = [W(-.15, -.105), W(.15, -.105), W(.15, .105), W(-.15, .105)]
        if min(cam.depth(q) for q in corners) < .2:
            return
        q = [cam.pt(v) for v in corners]
        path = skia.Path()
        path.addPoly([skia.Point(float(x), float(y)) for x, y in q], True)
        c.drawPath(path, skia.Paint(AntiAlias=True, Color=skia.Color(246, 242, 228)))
        sc = cam.scale(p)
        lw = max(min(.006 * sc, 1.6), .6)
        for k in range(3):
            yy = .05 - k * .035
            a, b = cam.pt(W(-.11, yy)), cam.pt(W(.06, yy))
            c.drawLine(a[0], a[1], b[0], b[1], skia.Paint(AntiAlias=True, StrokeWidth=lw, Color=skia.Color(*RULE, 200)))
        m = [cam.pt(W(x, y)) for x, y in ((.08, -.08), (.13, -.08), (.13, -.04), (.08, -.04))]
        mp = skia.Path()
        mp.addPoly([skia.Point(float(x), float(y)) for x, y in m], True)
        c.drawPath(mp, skia.Paint(AntiAlias=True, Style=skia.Paint.kStroke_Style, StrokeWidth=lw, Color=skia.Color(196, 40, 40, 230)))
        c.drawPath(path, skia.Paint(AntiAlias=True, Style=skia.Paint.kStroke_Style, StrokeWidth=lw * 1.3, Color=skia.Color(*INK, 210)))

    def hand(self, name):
        return self.cast[name].q['hand'][1] + np.array([0, 0, .05])

    def to_world(self, i, t, pts):
        (x, y, z), yaw, roll, k = R.ship_state(i, t)
        M = _rot(yaw, roll)
        P = (np.array(pts, float) * k) @ M.T
        return P + np.array([x, y, z])

    def project(self, cam, P):
        if min(cam.depth(p) for p in P) < .3:
            return None
        return [cam.pt(p) for p in P]

    def draw_ship(self, c, ctx, i, clip_path=None, fill_a=None):
        t, cam, W, H = ctx.t, ctx.cam, ctx.W, ctx.H
        faces, edges, rules, soft = GEOM[i]
        polys = []
        lids = []
        for kind, pts in faces:
            if kind.startswith('lid'):                              # Scene 19: ship A's container lids swing open.
                a = R.lid(int(kind[3:]), t) if i == 0 and int(kind[3:]) < len(R.LIDS) else 0.0
                y1 = max(p[1] for p in pts)
                pts = [(x, y1 - (y1 - y) * math.cos(a), z + (y1 - y) * math.sin(a)) for x, y, z in pts]
                kind = 'box'
                if a > .01:
                    lids.append(pts)
            P = self.to_world(i, t, pts)
            q = self.project(cam, P)
            if q is None:
                continue
            polys.append((cam.depth(P.mean(0)), kind, q))
        if not polys:
            return
        polys.sort(key=lambda p: -p[0])
        # Depth map of the ship (nearest face wins), so the set can hide it where the set is nearer.
        dmap = np.full((H, W), 1e4, np.float32)
        for d, kind, q in polys:
            cv2.fillPoly(dmap, [np.round(np.array(q)).astype(np.int32)], float(d))
        k = R.ship_state(i, t)[3]
        keep = (ctx.zb.astype(np.float32) > dmap - max(.35 * k, .03)) | (dmap > 1e3)
        a = np.where(keep, 255, 0).astype(np.uint8)
        mask = skia.Image.fromarray(np.dstack([a, a, a, a]), colorType=skia.ColorType.kRGBA_8888_ColorType)
        c.saveLayer()
        if clip_path is not None:
            c.clipPath(clip_path, doAntiAlias=True)
        sc = cam.scale(np.array(R.ship_state(i, t)[0]))
        lw = max(min(.035 * sc * max(k, .3), 3.2), .8)
        solid = 1 + (1 - k) * 1.8                                   # Small, it is still a folded paper ship: opaque.
        for d, kind, q in polys:
            path = skia.Path()
            path.addPoly([skia.Point(float(x), float(y)) for x, y in q], True)
            al = fill_a if fill_a is not None else min(int({'side': 84, 'deck': 50, 'house': 86, 'funnel': 110, 'box': 52}[kind] * solid), 235)
            col = (214, 120, 80) if kind == 'funnel' else PAPER
            c.drawPath(path, skia.Paint(AntiAlias=False, Color=skia.Color(*col, al)))
        rp = skia.Paint(AntiAlias=True, Style=skia.Paint.kStroke_Style, StrokeWidth=max(lw * .45, .6), Color=skia.Color(*RULE, 120))
        for line in rules:
            self.polyline(c, cam, self.to_world(i, t, line), rp)
        L = R.SHIPS[i]['L']
        mx = L / 2 - R.SHIPS[i]['B'] * 1.3 - 1.2                   # A red margin rule near the bow, as on a form.
        for sy in (1, -1):
            self.polyline(c, cam, self.to_world(i, t, [(mx, sy * R.SHIPS[i]['B'] / 2, .1), (mx, sy * R.SHIPS[i]['B'] / 2, R.SHIPS[i]['deck'] - .05)]),
                          skia.Paint(AntiAlias=True, Style=skia.Paint.kStroke_Style, StrokeWidth=max(lw * .6, .7), Color=skia.Color(*MARGIN, 150)))
        ep = skia.Paint(AntiAlias=True, Style=skia.Paint.kStroke_Style, StrokeWidth=lw, StrokeJoin=skia.Paint.kRound_Join,
                        StrokeCap=skia.Paint.kRound_Cap, Color=skia.Color(*INK, 175))
        for line in edges:
            self.polyline(c, cam, self.to_world(i, t, line), ep)
        sp = skia.Paint(AntiAlias=True, Style=skia.Paint.kStroke_Style, StrokeWidth=lw * .7, Color=skia.Color(*INK, 90))
        for line in soft:
            self.polyline(c, cam, self.to_world(i, t, line), sp)
        for pts in lids:
            self.polyline(c, cam, self.to_world(i, t, pts + [pts[0]]), ep)
        c.drawImage(mask, 0, 0, skia.SamplingOptions(), skia.Paint(BlendMode=skia.BlendMode.kDstIn))
        c.restore()

    def polyline(self, c, cam, P, paint):
        q = self.project(cam, P)
        if q is None:
            return
        path = skia.Path()
        path.moveTo(*q[0])
        for p in q[1:]:
            path.lineTo(*p)
        c.drawPath(path, paint)

    def draw_waves(self, c, ctx):
        """Little bright dashes on the water, drifting. Hidden behind the quay."""
        t, cam = ctx.t, ctx.cam
        c.saveLayer()
        for k, (x, y, L, ph) in enumerate(self.waves):
            x = (x + t * .25 + 30) % 60 - 30
            a = .5 + .5 * math.sin(t * 1.3 + ph)
            P = [np.array([x - L / 2, y, R.WATER_Z + .01]), np.array([x + L / 2, y, R.WATER_Z + .01])]
            if min(cam.depth(p) for p in P) < .5:
                continue
            q0, q1 = cam.pt(P[0]), cam.pt(P[1])
            w = max(min(.05 * cam.scale(P[0]), 2.5), .6)
            c.drawLine(q0[0], q0[1], q1[0], q1[1], skia.Paint(AntiAlias=True, StrokeWidth=w, StrokeCap=skia.Paint.kRound_Cap,
                                                              Color=skia.Color(236, 244, 240, int(40 + 60 * a))))
        zb = ctx.zb.astype(np.float32)
        a = np.where(zb > 3.0, 255, 0).astype(np.uint8)          # Only where the plate shows something far: the sea.
        mask = skia.Image.fromarray(np.dstack([a, a, a, a]), colorType=skia.ColorType.kRGBA_8888_ColorType)
        c.drawImage(mask, 0, 0, skia.SamplingOptions(), skia.Paint(BlendMode=skia.BlendMode.kDstIn))
        c.restore()

    # ---------------- over the characters: the form on the desk, its stamp marks, the officer's stamp
    def top(self, c, ctx):
        self.draw_sheets(c, ctx, near=True)

    def draw_form(self, c, ctx):
        """The officer's ledger, open on the counter: ruled pages, the entry being written, then his red stamp."""
        t, cam = ctx.t, ctx.cam
        lx, ly, lz = R.LEDGER

        def P(dx, dy, dz=0.0):
            return np.array([lx + dx, ly + dy, lz + dz])

        def quad(pts, col, stroke=True):
            if min(cam.depth(p) for p in pts) < .3:
                return
            q = [cam.pt(p) for p in pts]
            path = skia.Path()
            path.addPoly([skia.Point(float(x), float(y)) for x, y in q], True)
            c.drawPath(path, skia.Paint(AntiAlias=True, Color=skia.Color(*col)))
            if stroke:
                c.drawPath(path, skia.Paint(AntiAlias=True, Style=skia.Paint.kStroke_Style, StrokeWidth=1.0, Color=skia.Color(*INK, 170)))

        def line(a, b, col, w=.8):
            if min(cam.depth(a), cam.depth(b)) < .3:
                return
            qa, qb = cam.pt(a), cam.pt(b)
            c.drawLine(qa[0], qa[1], qb[0], qb[1], skia.Paint(AntiAlias=True, StrokeWidth=w, Color=skia.Color(*col)))

        quad([P(-.2, -.26, -.002), P(.2, -.26, -.002), P(.2, .26, -.002), P(-.2, .26, -.002)], (92, 40, 36))          # Cover.
        for side in (-1, 1):                                                                                           # Pages.
            y0, y1 = (-.25, -.005) if side < 0 else (.005, .25)
            quad([P(-.19, y0), P(.19, y0), P(.19, y1), P(-.19, y1)], (240, 236, 222))
            for k in range(9):
                x = -.16 + k * .04
                line(P(x, y0 + .02), P(x, y1 - .02), (*RULE, 150))
        # The entry: three lines of scribble on the far page (the officer's side reads it upside down to Vehbi).
        u = min(max((t - R.WRITE[0]) / (R.WRITE[1] - R.WRITE[0]), 0.0), 1.0)
        for k in range(3):
            frac = min(max(u * 3 - k, 0.0), 1.0)
            if frac <= 0:
                continue
            x = .12 - k * .045
            pts = [P(x + .006 * math.sin(j * 2.3 + k), -.22 + j * .02, .001) for j in range(int(1 + 21 * frac))]
            for a_, b_ in zip(pts, pts[1:]):
                line(a_, b_, (30, 40, 90, 230), 1.3)
        if t >= R.STAMP_L:
            m = [P(-.1 + dx, -.12 + dy, .002) for dx, dy in ((-.05, -.07), (.05, -.07), (.05, .07), (-.05, .07))]
            q = [cam.pt(p) for p in m]
            path = skia.Path()
            path.addPoly([skia.Point(float(x), float(y)) for x, y in q], True)
            c.drawPath(path, skia.Paint(AntiAlias=True, Style=skia.Paint.kStroke_Style, StrokeWidth=1.8, Color=skia.Color(196, 40, 40, 230)))

    def draw_stamp_tool(self, c, ctx):
        """A plain wooden rubber stamp in the officer's right hand: a knob, a handle, a block and the rubber.
        Scene 18: a pen while he writes, then the stamp."""
        cam = ctx.cam
        o = self.cast['officer']
        h = o.q['hand'][1]
        if cam.depth(h) < .3:
            return
        if ctx.t < R.STAMP_L - .6:
            a, b = cam.pt(h + np.array([-.02, 0, -.03])), cam.pt(h + np.array([.03, 0, .1]))
            c.drawLine(a[0], a[1], b[0], b[1], skia.Paint(AntiAlias=True, StrokeWidth=max(.012 * cam.scale(h), 1.5), StrokeCap=skia.Paint.kRound_Cap,
                                                          Color=skia.Color(30, 30, 34)))
            return
        up = np.array([0, 0, 1.0])
        parts = [(h + up * .06, .028, (120, 82, 50)), (h + up * .01, .016, (140, 98, 60)), (h - up * .045, .036, (96, 66, 40)),
                 (h - up * .07, .034, (60, 30, 30))]
        for p, r, col in parts:
            q = cam.pt(p)
            rr = max(r * cam.scale(p), 1.5)
            c.drawCircle(q[0], q[1], rr, skia.Paint(AntiAlias=True, Color=skia.Color(*col)))
            c.drawCircle(q[0], q[1], rr, skia.Paint(AntiAlias=True, Style=skia.Paint.kStroke_Style, StrokeWidth=1.2, Color=skia.Color(*INK, 200)))

    # ---------------- light
    def world(self, ctx):
        cam, H, W = ctx.cam, ctx.H, ctx.W
        if self._grid is None or self._grid[0].shape != (H, W):
            u, v = np.meshgrid(np.arange(W, dtype=np.float32), np.arange(H, dtype=np.float32))
            self._grid = (u, v)

    def on_actor(self, c, ink, ctx, pup):
        if pup is self.cast['officer']:
            self.draw_stamp_tool(c, ctx)
        if pup is self.cast['sidar'] and ctx.t >= R.CATCH[1]:        # The invoice in his hand, waved.
            t = ctx.t
            self.draw_sheet(c, ctx.cam, self.hand('sidar') + np.array([0, 0, .1]), -1.2 + .5 * math.sin(t * 9), 1.2 + .3 * math.sin(t * 9 + 1), 1.3)
        self._behind(c, ctx, pup)

    def _behind(self, c, ctx, pup):
        """Hide a character wherever the set is nearer to the camera than they are (bollards, crates)."""
        d = ctx.cam.depth(pup.root + np.array([0, 0, .5]))
        keep = ctx.zb.astype(np.float32) > d - .3
        a = np.where(keep, 255, 0).astype(np.uint8)
        img = skia.Image.fromarray(np.dstack([a, a, a, a]), colorType=skia.ColorType.kRGBA_8888_ColorType)
        c.drawImage(img, 0, 0, skia.SamplingOptions(), skia.Paint(BlendMode=skia.BlendMode.kDstIn))

    def post(self, pic, ctx):
        H, W = ctx.H, ctx.W
        self.world(ctx)
        u, v = self._grid
        vg = 1 - .18 * (((u - W / 2) / (W / 2)) ** 2 + ((v - H / 2) / (H / 2)) ** 2)[..., None]
        out = np.clip(pic.astype(np.float32) * AIR * vg, 0, 255).astype(np.uint8)
        return stamp.overlay(out, ctx.t)
