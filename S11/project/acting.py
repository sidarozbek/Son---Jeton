"""Son Jeton, scene 11: the coins become birds; Vehbi traces one; Sidar calls it profit; Vehbi calls it a chain.
Eyes first, then face, then head, then body."""
import math

from toonkit.camera import smooth
import blocking as B
import room as R

SIDAR_REST = dict(lid=.28, brow=-.25)
V_LID = dict(lid=.48)
S_ARM_DOWN = dict(bx=20, by=200, bz=30)
V_ARM_DOWN = dict(bx=10, by=270, bz=20)


def root(name, t):
    return B.where(name, t)


def direct(cast, cfg):
    s, v = cast['sidar'], cast['vehbi']
    qs = [cast[f'q{i}'] for i in range(len(R.QUEUE_SPOTS))]
    q_new, q_old = qs[5], qs[0]

    s.face(0, .01, 'smug', **SIDAR_REST)
    v.face(0, .01, 'unimpressed')
    s.look(0, -.3, .2)
    v.look(0, -.2, .2)
    for i, q in enumerate(qs):
        q.face(0, .01, 'rest', lid=.35)
        q.look(0, 0, .2)
        q.look(R.HATCH[0] + .2 + .1 * i, 0, .6, dur=.3)          # Everyone looks up as the birds rise.
        q.face(R.HATCH[0] + .4 + .1 * i, .3, 'curious', lid=.2)
    s.look(R.HATCH[0] + .3, -.2, .6, dur=.3)
    v.look(R.HATCH[0] + .4, -.3, .6, dur=.3)
    s.face(R.HATCH[0] + .6, .4, 'smug', lid=.15, brow=.3)

    # ---------------- The carries: the newest customer holds out a coin; the bird takes it; the oldest one catches it.
    for a, b in R.CARRIES:
        q_new.hands(a - .4, 1, 'pinch')
        q_new.to(a - .5, .4, ease=smooth, bx=10, by=60, bz=170)
        q_new.to(a + .4, .4, ease=smooth, **S_ARM_DOWN)
        q_new.hands(a + .6, 1, 'relaxed')
        q_old.hands(b - .5, 1, 'open')
        q_old.to(b - .6, .4, ease=smooth, bx=10, by=60, bz=170, hy=-.4)
        q_old.face(b, .3, 'almost_smile', lid=.3)
        q_old.to(b + .3, .4, ease=smooth, **S_ARM_DOWN, hy=0)
        q_old.hands(b + .5, 1, 'relaxed')

    # ---------------- "Look. New money pays the old customers."  Following the bird with his finger.
    v.hands(B.L1 - .3, 1, 'point')
    v.to(B.L1 - .3, .3, ease=smooth, bx=40, by=60, bz=200)
    v.line(B.L1, 'voices/v1.tsv', 'Look. New money pays the old customers')
    v.face(B.L1, .2, 'correcting', **V_LID)
    v.look(B.L1, -.5, .5, dur=.2)
    v.to(B.L1 + .2, 2.0, ease=smooth, th=B.V_TH0 + .9)          # The finger tracks the bird up the queue.
    v.look(B.L1 + 1.6, -.6, .3, dur=.4)
    v.to(B.L1 + 2.7, .4, ease=smooth, **V_ARM_DOWN, th=B.V_TH0)
    v.hands(B.L1 + 2.9, 1, 'relaxed')
    v.look(B.L1 + 2.7, 0, 0, dur=.15)

    # ---------------- "That's called profit."  Lecturing, a raised finger.
    s.look(B.L2 - .3, 0, 0, dur=.12)
    s.to(B.L2 - .3, .3, ease=smooth, th=B.heading(B.S_POS, B.V_POS))
    s.line(B.L2, 'voices/s2.tsv', "That's called profit")
    s.face(B.L2, .2, 'smug', lid=.3, brow=.2)
    s.hands(B.L2 + .1, 1, 'point')
    s.to(B.L2 + .1, .2, bx=10, by=120, bz=200, hp=-.05)
    s.to(B.L2 + 1.5, .4, ease=smooth, **S_ARM_DOWN, hp=0)
    s.hands(B.L2 + 1.6, 1, 'relaxed')

    # ---------------- "That's called a chain."  Dry.
    v.line(B.L3, 'voices/v3.tsv', "That's called a chain")
    v.face(B.L3, .15, 'correcting', **V_LID)
    v.face(B.L3 + 1.1, .3, 'unimpressed', lid=.5)
    s.face(B.L3 + .6, .3, 'determined', lid=.3, brow=-.1)

    # ---------------- The stamp.
    for p in [s, v] + qs:
        p.look(R.STAMP[1] + .05, 0, .55, dur=.1)
        p.to(R.STAMP[1], .06, squash=.04)
        p.to(R.STAMP[1] + .08, .2, squash=0)

    for k, pup in enumerate([s, v] + qs):
        pup.auto_blink(40 + k, cfg.END)
