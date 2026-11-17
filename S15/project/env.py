"""Scene 15: the harbour. The see-through ships are drawn here, under the characters, over the set plate.
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
    def box(kind, x0, x1, y0, y1, z0, z1, ink=True):
        P = [(x0, y0, z0), (x1, y0, z0), (x1, y1, z0), (x0, y1, z0), (x0, y0, z1), (x1, y0, z1), (x1, y1, z1), (x0, y1, z1)]
        for q in ((0, 1, 5, 4), (1, 2, 6, 5), (2, 3, 7, 6), (3, 0, 4, 7), (4, 5, 6, 7)):
            faces.append((kind, [P[i] for i in q]))
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
        box('box', x0, x0 + w - .25, -Bm * .3, Bm * .3, D, D + .75, ink='soft')
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
        order = sorted(range(len(R.SHIPS)), key=lambda i: -cam.depth(np.array(R.ship_pose(i, t)[0])))
        for i in order:
            self.draw_ship(c, ctx, i)

    def to_world(self, i, t, pts):
        (x, y, z), yaw, roll = R.ship_pose(i, t)
        M = _rot(yaw, roll)
        P = np.array(pts, float) @ M.T
        return P + np.array([x, y, z])

    def project(self, cam, P):
        if min(cam.depth(p) for p in P) < .3:
            return None
        return [cam.pt(p) for p in P]

    def draw_ship(self, c, ctx, i, clip_path=None, fill_a=None):
        t, cam, W, H = ctx.t, ctx.cam, ctx.W, ctx.H
        faces, edges, rules, soft = GEOM[i]
        polys = []
        for kind, pts in faces:
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
        keep = (ctx.zb.astype(np.float32) > dmap - .35) | (dmap > 1e3)
        a = np.where(keep, 255, 0).astype(np.uint8)
        mask = skia.Image.fromarray(np.dstack([a, a, a, a]), colorType=skia.ColorType.kRGBA_8888_ColorType)
        c.saveLayer()
        if clip_path is not None:
            c.clipPath(clip_path, doAntiAlias=True)
        sc = cam.scale(np.array(R.ship_pose(i, t)[0]))
        lw = max(min(.035 * sc, 3.2), .8)
        for d, kind, q in polys:
            path = skia.Path()
            path.addPoly([skia.Point(float(x), float(y)) for x, y in q], True)
            al = fill_a if fill_a is not None else {'side': 84, 'deck': 50, 'house': 86, 'funnel': 110, 'box': 52}[kind]
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

    # ---------------- over the characters: the hull over Vehbi's fingers; rings where the hand went in
    def top(self, c, ctx):
        t, cam = ctx.t, ctx.cam
        v = self.cast['vehbi']
        hold = v.p.get('bhold', 0)
        if hold < .3:
            return
        h = v.q['hand'][1]
        depth_in = h[1] - (R.HULL_Y)
        if depth_in <= .0:
            return
        # Rings on the hull side, where the wrist crosses it, spreading from the touch, then gentle while it stays.
        sh = v.q['sh'][1]
        u = (R.HULL_Y - sh[1]) / max(h[1] - sh[1], .05)
        wrist = sh + (h - sh) * min(max(u, 0.0), 1.0)
        for k in range(3):
            age = (t - R.TOUCH - k * .35) % 1.4 if t > R.TOUCH else -1
            if age < 0:
                continue
            rr = .05 + age * .22
            al = int(150 * (1 - age / 1.4))
            pts = [wrist + np.array([math.cos(a) * rr, 0, math.sin(a) * rr * .8]) for a in np.linspace(0, 2 * math.pi, 28)]
            self.polyline(c, cam, pts, skia.Paint(AntiAlias=True, Style=skia.Paint.kStroke_Style, StrokeWidth=1.6, Color=skia.Color(*INK, al)))

    # ---------------- light
    def world(self, ctx):
        cam, H, W = ctx.cam, ctx.H, ctx.W
        if self._grid is None or self._grid[0].shape != (H, W):
            u, v = np.meshgrid(np.arange(W, dtype=np.float32), np.arange(H, dtype=np.float32))
            self._grid = (u, v)

    def on_actor(self, c, ink, ctx, pup):
        if pup is self.cast['vehbi']:
            self.hand_in_hull(c, ctx, pup)
        self._behind(c, ctx, pup)

    def hand_in_hull(self, c, ctx, v):
        """Where the hand is past the hull side, lay the hull over it (only on the hand's own pixels), so the fingers
        sit inside the ship: a disc round the hand, cut by a line across the wrist where it crosses the hull."""
        t, cam = ctx.t, ctx.cam
        if v.p.get('bhold', 0) < .3:
            return
        h = v.q['hand'][1]
        sh = v.q['sh'][1]
        yh = R.HULL_Y
        if h[1] <= yh:
            return
        u = (yh - sh[1]) / max(h[1] - sh[1], .05)
        wrist = sh + (h - sh) * min(max(u, 0.0), 1.0)
        qw, qh = np.array(cam.pt(wrist)), np.array(cam.pt(h))
        d = qh - qw
        n = np.linalg.norm(d)
        if n < 1:
            return
        d /= n
        rad = max(.075 * cam.scale(h), 5)
        qt = qh + d * rad * 2.6                                                     # Past the fingertips, on screen.
        clip = skia.Path()
        clip.moveTo(float(qw[0]), float(qw[1]))
        clip.lineTo(float(qt[0]), float(qt[1]))
        clip = skia.Path(clip)
        stroke = skia.Paint(Style=skia.Paint.kStroke_Style, StrokeWidth=float(rad * 2.2), StrokeCap=skia.Paint.kButt_Cap)
        cap = skia.Path()
        stroke.getFillPath(clip, cap)
        head = skia.Path()
        qh_ = cam.pt(v.q['head'])
        head.addCircle(float(qh_[0]), float(qh_[1]), float(.2 * cam.scale(v.q['head'])))
        c.save()
        c.clipPath(cap, doAntiAlias=True)
        c.clipPath(head, skia.ClipOp.kDifference, True)
        c.drawPaint(skia.Paint(Color=skia.Color(0, 0, 0, 105), BlendMode=skia.BlendMode.kDstOut))      # Fingers half gone...
        c.drawPaint(skia.Paint(Color=skia.Color(*PAPER, 95), BlendMode=skia.BlendMode.kSrcATop))       # ...behind the paper.
        rp = skia.Paint(AntiAlias=True, Style=skia.Paint.kStroke_Style, StrokeWidth=1.2, Color=skia.Color(*RULE, 160), BlendMode=skia.BlendMode.kSrcATop)
        zr = .32
        while zr < R.SHIPS[0]['deck']:
            (x, y, z), yaw, roll = R.ship_pose(0, t)
            a, b = np.array([wrist[0] - 1, yh, z + zr]), np.array([wrist[0] + 1, yh, z + zr])
            qa, qb = cam.pt(a), cam.pt(b)
            c.drawLine(qa[0], qa[1], qb[0], qb[1], rp)
            zr += .32
        c.restore()

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
        return np.clip(pic.astype(np.float32) * AIR * vg, 0, 255).astype(np.uint8)
