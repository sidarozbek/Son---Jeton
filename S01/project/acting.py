"""Son Jeton, scene 1: blocking from blocking.py, mechanics from room.py. Eyes first, then face, then head, then body."""
import math

from toonkit.camera import smooth
import blocking as B
import room as R

SIDAR_REST = dict(lid=.28, brow=-.25)
V_LID = dict(lid=.48)                    # Vehbi's heavy lids, kept through every face.


def root(name, t):
    return B.vehbi(t) if name == 'vehbi' else B.sidar(t)


def heading(a, b):
    return math.atan2(b[1] - a[1], b[0] - a[0])


def glasses_push(v, t):
    """Vehbi's running gag: one finger pushes the glasses up before every rule he quotes."""
    v.hands(t, 1, 'point')
    v.to(t, .14, bx=-34, by=-118, bz=120)
    v.to(t + .3, .22, bx=10, by=270, bz=20)
    v.hands(t + .42, 1, 'relaxed')


def direct(cast, cfg):
    s, v = cast['sidar'], cast['vehbi']

    # ---------------- Vehbi at the desk: reading, nothing gets through.
    v.face(0, .01, 'unimpressed')
    v.to(0, .01, th=math.pi, hp=-.12, ax=26, ay=120, az=190)          # Book up, open in front of him.
    v.look(0, .1, -.55)
    v.look(1.66, .1, -.2)                                              # Third knock: the eyes lift a hair. That's all.
    v.look(2.1, .1, -.55)
    # ---------------- Sidar in the corridor: pounding, then the shout.
    s.face(0, .01, 'angry', **{k: v_ for k, v_ in SIDAR_REST.items() if k == 'lid'})
    s.to(0, .01, th=-math.pi / 2 + .35, lean=.08)       # Square to the door, a little turned to the lamp-less corridor.
    knock_at = (R.DOOR_X0 + .45, R.D + .045, 1.22)
    s.pin(1, knock_at)
    s.hands(0, 1, 'fist')
    for k in R.KNOCKS:
        s.to(k - .1, .07, bhold=.55, lean=.04)
        s.to(k, .035, bhold=1, lean=.12, sway=.05)
    s.to(R.KNOCKS[-1] + .15, .15, bhold=0, by=200, bz=30)
    s.hands(R.KNOCKS[-1] + .2, 1, 'relaxed')
    s.on_ones(R.KNOCKS[3] - .15, R.KNOCKS[4] + .2)
    s.line(B.L1, 'voices/s1.tsv', 'Vehbi! Rent!')
    s.to(B.L1 - .12, .1, lean=.16, hp=.12, hr=-.04, squash=-.04)       # Chin up at the door, chest out.
    s.to(B.L1 + .55, .2, hp=.02, hr=.02, squash=0)

    # ---------------- Vehbi: sigh, glasses, the walk, the crack.
    v.look(4.05, .1, .2)
    v.face(4.15, .3, 'slow_lid')
    v.to(4.15, .3, hp=0, ax=6, ay=250, az=20)                          # Book down to his side.
    glasses_push(v, 4.25)
    hd = heading(B.V_DESK, B.V_GAP)
    v.to(B.V_WALK[0] - .05, .2, th=hd, loco=1, lean=.05)
    v.face(B.V_WALK[0] + .3, .2, 'unimpressed')
    v.to(B.V_WALK[1] - .25, .25, th=math.pi / 2)
    v.to(B.V_WALK[1], .1, loco=0, lean=-.03, squash=.02)
    v.to(B.V_WALK[1] + .2, .2, lean=0, squash=0)
    v.pin(1, (R.DOOR_X0 + .06, R.D - .04, .98))                        # The knob.
    v.hands(R.CRACK[0] - .25, 1, 'grip')
    v.to(R.CRACK[0] - .2, .15, bhold=1)
    v.to(R.CRACK[1] - .05, .15, bhold=0, bx=10, by=270, bz=20)
    v.hands(R.CRACK[1], 1, 'relaxed')
    # Sidar hears the latch: a step of weight onto the front foot.
    s.look(R.CRACK[0] + .1, -.2, -.1)
    s.to(R.CRACK[0] + .15, .2, lean=.1, hipdrop=6)

    # ---------------- Clause seven, read from the contract in the book.
    glasses_push(v, B.L2 - .75)
    v.to(B.L2 - .3, .22, ax=26, ay=120, az=190, hp=-.08)
    v.look(B.L2 - .25, .05, -.5)
    v.line(B.L2, 'voices/v2.tsv', 'Clause seven')
    v.face(B.L2, .12, 'correcting', **V_LID)
    v.to(B.L2 + .9, .1, hr=.03)                                        # "the landlord"
    v.look(B.L2 + 2.1, .0, .1)                                         # Eyes up for "at night", straight at him.
    v.to(B.L2 + 2.2, .2, hp=.04, hr=-.02)
    v.face(B.L2 + 3.0, .3, 'unimpressed')
    s.face(B.L2 + .4, .2, 'rest', **SIDAR_REST)
    s.look(B.L2 + 1.2, -.15, -.25)                                     # A glance at the book, contempt.
    s.look(B.L2 + 1.6, 0, 0)
    s.face(B.L2 + 2.6, .15, 'angry', lid=.2)                           # Late and small: he heard "at night".

    # ---------------- "I'm giving notice!"
    s.line(B.L3, 'voices/s3.tsv', 'giving notice')
    s.to(B.L3 - .15, .12, lean=.2, sway=.12, hr=.06, hp=.08)           # Shoulder first.
    s.to(B.L3 + .7, .25, sway=0, hr=0)
    v.blink(B.L3 + .5)
    # ---------------- "In writing."
    glasses_push(v, B.L4 - .45)
    v.line(B.L4, 'voices/v4.tsv', 'In writing')
    v.face(B.L4, .1, 'one_brow', **V_LID)

    # ---------------- The push. Anticipation, the shove, the door flies, the books skid.
    p0, p1 = R.PUSH[0], R.PUSH[1]
    s.face(p0 - .5, .12, 'determined', lid=.15)
    s.to(p0 - .32, .14, lean=-.14, sway=-.16, squash=.06, hr=-.05)    # Wind up, weight back.
    s.to(p0, .1, lean=.42, sway=.28, squash=-.06, hr=.06, hp=-.05)     # Shoulder into the door.
    s.to(p1 + .1, .2, lean=.18, sway=.06, squash=0)
    s.on_ones(p0 - .35, p1 + .35)
    s.to(B.S_WALK[0] - .05, .15, loco=1, th=-math.pi / 2 - .05, lean=.12)
    face_v = heading(B.S_IN, B.V_BACK)
    s.to(B.S_WALK[1] - .3, .3, th=face_v)
    s.to(B.S_WALK[1], .1, loco=0, lean=-.06, squash=.05)               # Overshoot...
    s.to(B.S_WALK[1] + .18, .2, lean=.02, squash=0)                    # ...and settle.
    # Vehbi: the door flies past him. He steps back, deadpan, the book never moves from his hand.
    v.look(p0 + .05, .3, 0)
    v.to(p0 + .05, .12, lean=-.1, hp=.05)
    v.face(p0 + .08, .1, 'unimpressed', eye_s=1.06)
    v.to(B.V_STEP[0], .12, loco=1, th=math.pi / 2 + .4)
    v.to(B.V_STEP[1], .12, loco=0, lean=0)
    v.to(B.V_STEP[1] + .1, .35, ease=smooth, th=heading(B.V_BACK, B.S_IN), hp=0)
    v.face(B.V_STEP[1] + .3, .3, 'unimpressed')
    v.look(B.S_WALK[0], .25, .05)

    # ---------------- "I'm here." His arrival is the written notice. Chest out, chin up, a hand flat on the vest.
    s.line(B.L5, 'voices/s5.tsv', "I'm here")
    s.face(B.L5 - .1, .1, 'determined', lid=.2)
    s.to(B.L5 - .1, .12, hp=.12, squash=-.05, lean=-.04)
    s.hands(B.L5 + .1, 1, 'flat')
    s.to(B.L5 + .1, .18, bx=-40, by=130, bz=80)                       # Hand on his own chest: here, in person.
    s.face(B.L5 + .7, .2, 'smug', **SIDAR_REST)
    s.to(B.L5 + 1.1, .25, bx=20, by=200, bz=30, hp=.06)
    s.hands(B.L5 + 1.2, 1, 'relaxed')

    # ---------------- The reaction: a long, slow look. The joke is how little he moves.
    v.look(B.L5 + .2, .2, .05)
    v.face(18.35, .6, 'slow_lid')
    v.to(18.35, 1.0, ease=smooth, hp=.03, hy=.04)
    v.blink(19.55)
    v.face(19.85, .3, 'unimpressed')
    s.to(18.95, .35, lean=.2, sway=.12, hr=.04)                         # Leans into his space, shoulder first.
    s.to(20.85, .5, ease=smooth, lean=.06, sway=0, hr=0)

    for pup, seed in ((s, 1), (v, 2)):
        pup.auto_blink(seed, cfg.END)
