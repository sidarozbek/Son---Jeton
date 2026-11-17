"""Son Jeton, scene 04: the street, the tokens, the watch, the calendar. Blocking from blocking.py, timing from room.py.
Eyes first, then face, then head, then body."""
import math

from toonkit.camera import smooth
import blocking as B
import room as R

SIDAR_REST = dict(lid=.28, brow=-.25)
V_LID = dict(lid=.48)
V_ARM_DOWN = dict(bx=10, by=270, bz=20)
S_ARM_DOWN = dict(bx=20, by=200, bz=30)


def root(name, t):
    return B.vehbi(t) if name == 'vehbi' else B.sidar(t)


def glasses_push(v, t):
    v.hands(t, 1, 'point')
    v.to(t, .14, bx=-34, by=-118, bz=120)
    v.to(t + .3, .22, **V_ARM_DOWN)
    v.hands(t + .42, 1, 'relaxed')


def direct(cast, cfg):
    s, v = cast['sidar'], cast['vehbi']

    # ---------------- Where the fold left them: Vehbi's hand at his ear, Sidar smug.
    s.face(0, .01, 'smug', **SIDAR_REST)
    s.look(0, -.1, 0)
    v.face(0, .01, 'unimpressed', lid=.3, eye_s=1.04)
    v.hands(0, 1, 'grip')
    v.look(0, .1, .3)

    # ---------------- He notices there is no receiver. Looks at the hand; lowers it. Takes in the street, the snow.
    v.look(R.HAND_DOWN - .35, .35, .15, dur=.12)
    v.to(R.HAND_DOWN - .3, .2, hr=.1)
    v.to(R.HAND_DOWN, .35, ease=smooth, **V_ARM_DOWN, hr=0)
    v.hands(R.HAND_DOWN + .1, 1, 'relaxed')
    v.face(R.HAND_DOWN + .05, .3, 'one_brow', **V_LID)
    v.look(R.HAND_DOWN + .45, -.4, .35, dur=.25)        # The facades, the snow.
    v.to(R.HAND_DOWN + .45, .45, ease=smooth, hy=-.25, hp=-.05)
    v.look(R.HAND_DOWN + 1.0, .3, .15, dur=.25)
    v.to(R.HAND_DOWN + 1.0, .4, ease=smooth, hy=.1, hp=0)
    v.face(R.HAND_DOWN + 1.0, .3, 'unimpressed')

    # ---------------- "Four tokens left. Don't make me waste them."  Shaking them like dice.
    s.hands(R.SHAKE[0] - .1, 1, 'grip')
    s.to(R.SHAKE[0] - .15, .25, bx=-10, by=30, bz=210, hp=-.04)
    s.look(R.SHAKE[0], .3, .25, dur=.12)                 # At his own fist first.
    k, t = 0, R.SHAKE[0] + .25
    while t < R.SHAKE[1] - .2:                          # The shake: small fast up-downs of the forearm.
        if not (B.L1 + 1.0 < t < B.L1 + 1.25):          # A beat between the two sentences.
            s.to(t, .09, bx=-10 + (8 if k % 2 else -4), by=30, bz=210 + (14 if k % 2 else -12))
            k += 1
        t += .13
    s.look(B.L1 - .1, -.05, 0, dur=.12)                 # Then at Vehbi.
    s.line(B.L1, 'voices/s1.tsv', "Four tokens left. Don't make me waste them")
    s.face(B.L1, .2, 'determined', **SIDAR_REST)
    s.face(B.L1 + 1.25, .2, 'smug', lid=.24, brow=.0)
    s.to(B.L1 + 1.25, .3, hp=.05, lean=-.02)
    s.to(R.SHAKE[1] - .15, .3, ease=smooth, **S_ARM_DOWN, hp=0, lean=0)   # Pockets them.
    s.hands(R.SHAKE[1], 1, 'relaxed')
    v.look(R.SHAKE[0] + .1, .55, .1, dur=.15)            # Vehbi watches the tokens.

    # ---------------- The watch. "My exam starts at nine."  Anxious; he won't show it.
    v.hands(R.WATCH[0], 1, 'relaxed')
    v.to(R.WATCH[0], .3, ease=smooth, bx=40, by=40, bz=120, hp=.12)       # The wrist up in front of him.
    v.look(R.WATCH[0] + .2, .15, -.45, dur=.15)
    v.face(R.WATCH[0] + .25, .2, 'doubt', lid=.3)
    v.line(B.L2, 'voices/v2.tsv', 'My exam starts at nine')
    v.look(B.L2 + 1.1, 0, 0, dur=.15)                    # Up to Sidar on "at nine".
    v.to(B.L2 + 1.0, .3, hp=0)
    v.face(B.L2 + 1.1, .25, 'unimpressed', lid=.4)
    v.to(R.WATCH[1], .35, ease=smooth, **V_ARM_DOWN)

    # ---------------- "Nine o'clock. Which year?"  Enjoying it.
    s.look(B.L3 - .2, 0, 0, dur=.1)
    s.line(B.L3, 'voices/s3.tsv', "Nine o'clock. Which year?")
    s.face(B.L3, .25, 'smug', lid=.22, brow=.25)
    s.to(B.L3 + .9, .35, ease=smooth, lean=.05, hp=-.05, hy=.12)          # Leans in for "Which year?".
    s.hands(B.L3 + .9, 1, 'open')
    s.to(B.L3 + .9, .3, bx=10, by=150, bz=110)
    s.to(B.L3 + 2.0, .4, ease=smooth, lean=0, hp=0, hy=0, **S_ARM_DOWN)
    s.hands(B.L3 + 2.2, 1, 'relaxed')

    # ---------------- His eyes snap to the window. The calendar. Then the date, flat and instant.
    v.look(R.GLANCE, -.75, -.1, dur=.06)
    v.to(R.GLANCE + .05, .15, hy=-.35)
    v.look(B.L4 - .1, 0, 0, dur=.06)
    v.to(B.L4 - .1, .12, hy=0)
    glasses_push(v, B.L4 - .35)
    v.line(B.L4, 'voices/v4.tsv', 'January twenty-fourth, nineteen eighty')
    v.face(B.L4, .12, 'correcting', **V_LID)
    v.face(B.L4 + 2.3, .3, 'unimpressed')
    s.look(R.GLANCE + .1, -.6, -.1, dur=.1)              # Sidar follows his look to the window, too late.
    s.look(B.L4 + .3, 0, 0, dur=.1)
    s.face(B.L4 + .4, .3, 'doubt', lid=.2)

    # ---------------- "…Lucky guess."  Muttered. He turns to the street.
    s.line(B.L5, 'voices/s5.tsv', 'Lucky guess')
    s.face(B.L5 - .2, .25, 'determined', lid=.35, brow=-.35)
    s.look(B.L5 - .2, .3, .2, dur=.12)                  # Not at Vehbi.
    s.to(B.L5 + .5, .6, ease=smooth, th=B.heading(B.S_START, B.S_AWAY))
    v.face(B.L5 + .3, .3, 'almost_smile', lid=.45)
    v.look(B.L5 + .3, .2, 0, dur=.15)

    for pup, seed in ((s, 7), (v, 8)):
        pup.auto_blink(seed, cfg.END)
