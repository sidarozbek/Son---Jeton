"""Son Jeton, scene 07: the first stamp. Vehbi's book agrees with it; Sidar takes it as his own life's work stamped.
Blocking from blocking.py, timing from room.py. Eyes first, then face, then head, then body."""
import math

from toonkit.camera import smooth
import blocking as B
import room as R

SIDAR_REST = dict(lid=.28, brow=-.25)
V_LID = dict(lid=.48)
V_ARM_DOWN = dict(bx=10, by=270, bz=20)
V_BOOK_REST = dict(ax=6, ay=250, az=30)
V_BOOK_UP = dict(ax=-20, ay=40, az=190)         # The left hand, with the book, held up and out to Sidar.
S_ARM_DOWN = dict(bx=20, by=200, bz=30)
S_LARM_DOWN = dict(ax=-20, ay=200, az=30)


def root(name, t):
    return {'vehbi': B.vehbi, 'sidar': B.sidar, 'grocer': B.grocer}[name](t)


def direct(cast, cfg):
    s, v, g = cast['sidar'], cast['vehbi'], cast['grocer']

    # ---------------- As Scene 06 left them. The stamp comes down: everyone flinches, then looks up.
    s.face(0, .01, 'determined', **SIDAR_REST)
    v.face(0, .01, 'unimpressed', lid=.55)
    g.face(0, .01, 'curious', lid=.2)
    hit = R.STAMP[1]
    for p in (s, v, g):
        p.to(hit, .06, squash=.05)
        p.to(hit + .08, .2, squash=0)
        p.look(hit + .05, .35, .55, dur=.1)
    s.blink(hit)
    v.blink(hit + .02)

    # ---------------- Vehbi opens the book and holds it up: the same figure.
    v.look(R.BOOK_OPEN - .3, -.2, -.3, dur=.12)
    v.to(R.BOOK_OPEN - .2, .4, ease=smooth, **V_BOOK_UP, hp=.06)
    v.line(B.L1, 'voices/v1.tsv', 'Seventy lira to the dollar. Same as the book')
    v.face(B.L1, .2, 'correcting', **V_LID)
    v.look(B.L1 + 2.2, 0, 0, dur=.12)                      # From the page to Sidar on "Same as the book".
    v.to(B.L1 + 2.2, .3, ease=smooth, hp=0)
    v.face(B.L1 + 3.5, .3, 'unimpressed', lid=.45)
    v.to(B.L1 + 3.7, .4, ease=smooth, **V_BOOK_REST)

    # ---------------- "Thirty years at the bank, and finally someone stamps my work."  Moved, proud, hand on heart.
    s.look(B.L2 - .4, .25, .45, dur=.2)                    # Up to where the stamp came from.
    s.face(B.L2 - .3, .4, 'smug', lid=.38, brow=.2)
    s.line(B.L2, 'voices/s2.tsv', 'Thirty years at the bank, and finally someone stamps my work')
    s.hands(B.L2 + .2, 1, 'flat')
    s.to(B.L2 + .2, .4, ease=smooth, bx=-60, by=120, bz=150, hp=-.06)   # Hand on heart.
    s.to(B.L2 + 1.6, .5, ease=smooth, lean=-.05, hp=-.1)
    s.look(B.L2 + 2.6, 0, 0, dur=.2)
    s.face(B.L2 + 2.6, .3, 'smug', lid=.25, brow=.3)
    s.to(B.L2 + 3.6, .4, ease=smooth, **S_ARM_DOWN, lean=0, hp=0)
    s.hands(B.L2 + 3.8, 1, 'relaxed')
    v.face(B.L2 + 1.0, .3, 'slow_lid')
    g.look(B.L2 + .5, .5, 0, dur=.15)
    g.face(B.L2 + .8, .3, 'doubt', lid=.25)

    # ---------------- "It's not your stamp."  Flat.
    v.line(B.L3, 'voices/v3.tsv', "It's not your stamp")
    v.face(B.L3, .15, 'correcting', **V_LID)

    # ---------------- "Whose else would it be?"  Sincerely puzzled.
    s.line(B.L4, 'voices/s4.tsv', 'Whose else would it be?')
    s.face(B.L4 - .1, .3, 'curious', lid=.15, brow=.4)
    s.hands(B.L4 + .3, 1, 'open')
    s.hands(B.L4 + .3, -1, 'open')
    s.to(B.L4 + .3, .3, ease=smooth, bx=40, by=120, bz=110, ax=-40, ay=120, az=110)   # Palms out.
    s.to(B.L4 + 1.8, .4, ease=smooth, **S_ARM_DOWN, **S_LARM_DOWN)
    s.hands(B.L4 + 2.0, 1, 'relaxed')
    s.hands(B.L4 + 2.0, -1, 'relaxed')
    v.face(B.L4 + .8, .3, 'unimpressed', lid=.55)

    for pup, seed in ((s, 15), (v, 16), (g, 17)):
        pup.auto_blink(seed, cfg.END)
