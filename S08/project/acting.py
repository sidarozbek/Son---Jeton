"""Son Jeton, scene 08: the labels overflow; the run to the phone; the card on Sidar's nose; token two.
Blocking from blocking.py, timing from room.py. Eyes first, then face, then head, then body."""
import math

from toonkit.camera import smooth
import blocking as B
import room as R

SIDAR_REST = dict(lid=.28, brow=-.25)
V_LID = dict(lid=.48)
V_ARM_DOWN = dict(bx=10, by=270, bz=20)
S_ARM_DOWN = dict(bx=20, by=200, bz=30)


def root(name, t):
    return {'vehbi': B.vehbi, 'sidar': B.sidar, 'grocer': B.grocer}[name](t)


def heading_keys(p, pts, t0, t1, n=14):
    """Face along a path while running it."""
    for k in range(n + 1):
        u = k / n
        p.to(t0 + (t1 - t0) * u - .05, .1, th=B.path_heading(pts, min(max(u, .02), .98)))


def direct(cast, cfg):
    s, v, g = cast['sidar'], cast['vehbi'], cast['grocer']

    # ---------------- The overflow. Everyone startled; the grocer squeezed between his swelling shelf and the counter.
    s.face(0, .01, 'determined', **SIDAR_REST)
    v.face(0, .01, 'unimpressed', lid=.4)
    g.face(0, .01, 'blank')
    for i, ts in enumerate(R.STAND_UP):
        for p in (s, v, g):
            p.to(ts, .05, squash=.04)
            p.to(ts + .08, .15, squash=0)
    s.look(.6, -.4, -.2, dur=.1)
    v.look(.6, .4, -.2, dur=.1)
    g.face(.4, .3, 'panic')
    g.to(.4, 1.5, ease=smooth, squash=.18, lean=.12)      # Squeezed flat.
    g.to(2.4, .4, ease=smooth, hp=.15)

    # ---------------- "To the phone! Run!"  Then he runs, round the right of the cards.
    s.line(B.L1, 'voices/s1.tsv', 'To the phone! Run!')
    s.face(B.L1, .12, 'determined', lid=.15, brow=.4)
    s.hands(B.L1 + .2, 1, 'point')
    s.to(B.L1 + .2, .2, bx=60, by=120, bz=170, hy=.3)     # Points at the phone.
    s.to(B.S_RUN[0] - .1, .2, **S_ARM_DOWN, hy=0, loco=1, lean=.1)
    s.hands(B.S_RUN[0], 1, 'relaxed')
    heading_keys(s, B.S_PATH, B.S_RUN[0], B.S_RUN[1])
    s.to(B.S_RUN[1] - .1, .2, loco=0, lean=0, th=0.0)       # At the phone, facing the wall.

    # ---------------- Vehbi weaves: "Excuse me. Excuse me. Excuse me."  Polite to the cardboard.
    v.to(B.V_RUN[0] - .1, .2, loco=1, lean=.05)
    heading_keys(v, B.V_PATH, B.V_RUN[0], B.V_RUN[1], n=18)
    v.line(B.L2, 'voices/v2.tsv', 'Excuse me. Excuse me. Excuse me')
    v.face(B.L2, .2, 'unimpressed', lid=.45)
    for k, dt in enumerate((0, .75, 1.5)):                 # A little bow of the head to each card.
        v.to(B.L2 + dt, .15, hp=.12)
        v.to(B.L2 + dt + .25, .2, hp=0)
    v.to(B.V_RUN[1] - .1, .2, loco=0, lean=0, th=math.atan2(B.S_PHONE[1] - B.V_PHONE[1], B.S_PHONE[0] - B.V_PHONE[0]))

    # ---------------- The card flies onto Sidar's nose. "Token two."  Muffled. The token in.
    s.look(R.NOSE[0] - .1, -.4, .2, dur=.08)
    s.face(R.NOSE[1], .08, 'determined', lid=.0, brow=.6, eye_s=1.15)
    s.to(R.NOSE[1], .08, hp=-.08, squash=.05)
    s.to(R.NOSE[1] + .12, .2, hp=0, squash=0)
    s.to(R.NOSE[1] + .15, .35, ease=smooth, th=-2.35)        # Turns round, card on his nose, to face the shop.
    s.line(B.L3, 'voices/s3.tsv', 'Token two')
    s.face(B.L3, .2, 'determined', **SIDAR_REST)
    s.hands(B.L3 + .2, 1, 'pinch')
    s.to(B.L3 + .2, .3, bx=60, by=20, bz=200)              # Reaches behind him for the slot, blind.
    s.to(R.COIN_IN + .2, .3, **S_ARM_DOWN)
    s.hands(R.COIN_IN + .3, 1, 'relaxed')
    v.look(R.NOSE[1], .3, .05, dur=.1)
    v.face(R.NOSE[1] + .2, .3, 'one_brow', **V_LID)

    # ---------------- The line crosses; the stamp. Both look up.
    for p in (s, v):
        p.look(R.STAMP[1] + .05, 0, .55, dur=.1)
        p.to(R.STAMP[1], .06, squash=.05)
        p.to(R.STAMP[1] + .08, .2, squash=0)

    for pup, seed in ((s, 18), (v, 19), (g, 20)):
        pup.auto_blink(seed, cfg.END)
