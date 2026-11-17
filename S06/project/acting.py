"""Son Jeton, scene 06: midnight at the grocer's. The cards swell, the banknote shrinks, Sidar crows.
Blocking from blocking.py, timing from room.py. Eyes first, then face, then head, then body."""
import math

from toonkit.camera import smooth
import blocking as B
import room as R

SIDAR_REST = dict(lid=.28, brow=-.25)
V_LID = dict(lid=.48)
V_ARM_DOWN = dict(bx=10, by=270, bz=20)
S_ARM_DOWN = dict(bx=20, by=200, bz=30)
S_LARM_DOWN = dict(ax=-20, ay=200, az=30)
NOTE_UP = dict(bx=25, by=40, bz=200)          # Vehbi's right hand up in front of him, holding the note.


def root(name, t):
    return {'vehbi': B.vehbi, 'sidar': B.sidar, 'grocer': B.grocer}[name](t)


def direct(cast, cfg):
    s, v, g = cast['sidar'], cast['vehbi'], cast['grocer']

    # ---------------- Where Scene 05 left them. The clock strikes; heads turn to it.
    s.face(0, .01, 'smug', **SIDAR_REST)
    v.face(0, .01, 'unimpressed')
    g.face(0, .01, 'rest', lid=.3)
    for p, x in ((s, -.6), (v, -.5), (g, -.7)):
        p.look(R.CHIMES[0], x, .3, dur=.15)                # Towards the clock on the left wall.

    # ---------------- The cards swell. The grocer backs off from his own shelves.
    g.look(R.GROW[0] + .1, .2, .2, dur=.12)
    g.to(R.GROW[0] + .1, .5, ease=smooth, th=B.G_TH0 + 1.2)  # Half turns to the shelf.
    g.face(R.GROW[0] + .4, .3, 'blank')
    g.to(R.GROW[0] + 1.6, .6, ease=smooth, lean=-.1, th=B.G_TH0 + .6)
    g.face(R.GROW[1] - .5, .3, 'curious', lid=.2)
    s.look(R.GROW[0] + .2, -.4, .3, dur=.15)
    s.face(R.GROW[0] + .6, .4, 'smug', lid=.2, brow=.1)

    # ---------------- Vehbi takes out a banknote; it shrinks in his fingers. He looks at it, unmoved.
    v.hands(R.NOTE_OUT - .1, 1, 'pinch')
    v.to(R.NOTE_OUT - .1, .2, bx=20, by=250, bz=60)        # To his pocket...
    v.to(R.NOTE_OUT + .25, .35, ease=smooth, **NOTE_UP)    # ...and up in front of him.
    v.look(R.NOTE_OUT + .3, .2, -.25, dur=.15)
    v.to(R.SHRINK[0], .4, ease=smooth, hp=.08)
    v.face(R.SHRINK[0] + .5, .4, 'one_brow', lid=.5)
    v.blink(R.SHRINK[1] - .2)

    # ---------------- "See? SEE?!"  Both arms up.
    s.look(B.L1 - .2, -.1, 0, dur=.1)
    s.line(B.L1, 'voices/s1.tsv', 'See? See?')
    s.face(B.L1, .15, 'smug', lid=.05, brow=.5, eye_s=1.15)
    s.hands(B.L1, 1, 'open')
    s.hands(B.L1, -1, 'open')
    s.to(B.L1 - .05, .2, bx=40, by=40, bz=230, ax=-40, ay=40, az=230, lean=-.05, squash=-.05)
    s.to(B.L1 + .45, .15, bz=250, az=250, squash=.04)
    s.to(B.L1 + 1.1, .4, ease=smooth, **S_ARM_DOWN, **S_LARM_DOWN, lean=0, squash=0)
    s.hands(B.L1 + 1.3, 1, 'relaxed')
    s.hands(B.L1 + 1.3, -1, 'relaxed')
    s.face(B.L1 + 1.1, .3, 'smug', **SIDAR_REST)

    # ---------------- "Money doesn't shrink. Prices rise."  The tiny note held up between two fingers.
    v.look(B.L2 - .3, 0, 0, dur=.12)
    v.to(B.L2 - .3, .3, ease=smooth, hp=0, bx=20, by=30, bz=220)
    v.line(B.L2, 'voices/v2.tsv', "Money doesn't shrink. Prices rise")
    v.face(B.L2, .15, 'correcting', **V_LID)
    v.to(B.L2 + 1.2, .3, ease=smooth, hy=-.2)             # A glance at the swollen cards on "Prices rise".
    v.look(B.L2 + 1.2, -.3, .2, dur=.12)
    v.look(B.L2 + 2.0, 0, 0, dur=.12)
    v.to(B.L2 + 2.0, .3, ease=smooth, hy=0)

    # ---------------- "Same thing!"  At once.
    s.line(B.L3, 'voices/s3.tsv', 'Same thing!')
    s.face(B.L3 - .05, .12, 'determined', lid=.2, brow=.3)
    s.hands(B.L3, 1, 'point')
    s.to(B.L3, .15, bx=10, by=150, bz=150, lean=.06)
    s.to(B.L3 + .9, .4, ease=smooth, **S_ARM_DOWN, lean=0)
    s.hands(B.L3 + 1.0, 1, 'relaxed')
    v.face(B.L3 + .5, .3, 'unimpressed', lid=.55)
    v.to(B.L3 + .9, .4, ease=smooth, **V_ARM_DOWN)
    g.look(B.L3 + .2, -.5, 0, dur=.12)

    for pup, seed in ((s, 12), (v, 13), (g, 14)):
        pup.auto_blink(seed, cfg.END)
