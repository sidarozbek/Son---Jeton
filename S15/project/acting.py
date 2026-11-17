"""Son Jeton, scene 15: the harbour. "Ships. Full of goods." Vehbi's hand goes through a hull. "Goods! Paper goods."
Eyes, face, head, body. The ship slides on through his hand: the hand is pinned to a point in the world, not to the ship."""
import math

from toonkit.camera import smooth
import blocking as B
import room as R

V_BOOK = dict(ax=6, ay=250, az=30)
S_ARMS_DOWN = dict(ax=10, ay=330, az=0, bx=10, by=330, bz=0)


def root(name, t):
    return B.where(name, t)


def direct(cast, cfg):
    s, v = cast['sidar'], cast['vehbi']
    s.face(0, .01, 'smug', lid=.3, brow=.1)
    v.face(0, .01, 'rest', lid=.35, brow=.15)
    s.look(0, .2, .2)
    v.look(0, -.1, 0)

    # ---------------- They watch the ships go by. Vehbi's eyes follow the near one.
    v.look(1.2, .4, -.05, dur=.4)
    v.to(1.0, .8, ease=smooth, hy=-.25)
    s.to(1.6, .4, ease=smooth, hp=.08)

    # ---------------- "Ships. Full of goods."  He turns to us, arms wide, grand.
    s.to(2.2, .4, ease=smooth, th=B.S_TO_CAM, hy=0, hp=.05)
    s.look(2.2, 0, 0, dur=.1)
    s.line(R.L1, 'voices/s1.tsv', 'Ships. Full of goods')
    s.face(R.L1 - .15, .25, 'determined', lid=.2, brow=.35)
    s.to(R.L1 - .1, .35, ease=smooth, ax=250, ay=110, az=90, bx=250, by=110, bz=90, lean=-.06)
    s.to(R.L1 + .7, .3, ease=smooth, ax=290, ay=60, az=60, bx=290, by=60, bz=60, hp=.12)       # "Full of goods!"
    s.face(R.L1 + .7, .25, 'smug', lid=.25, brow=.3)
    s.to(R.L1 + 1.7, .5, ease=smooth, **S_ARMS_DOWN, lean=0, hp=.04)

    # ---------------- Vehbi goes to the edge, side-on to the passing ship.
    v.look(B.V_WALK[0] - .2, .3, 0, dur=.1)
    v.to(B.V_WALK[0] - .1, .2, loco=1, th=B.heading(B.V_START, B.V_EDGE))
    v.to(B.V_WALK[1] - .35, .4, ease=smooth, loco=0, th=B.V_SIDE, hy=-1.0)     # Body side-on, head to the ship.
    v.face(B.V_WALK[1], .3, 'curious', lid=.2, brow=.3)
    s.to(B.V_WALK[0], .5, ease=smooth, th=B.heading(B.S_POS, B.V_EDGE), hy=.1)
    s.look(B.V_WALK[0], .2, -.1, dur=.15)

    # ---------------- The touch. The right hand goes sideways into the hull; the hull keeps sliding past it.
    v.pin(1, R.V_HAND)
    v.to(R.REACH[0], .35, ease=smooth, bx=70, by=150, bz=40)
    v.to(R.REACH[0] + .2, R.REACH[1] - R.REACH[0] - .2, ease=smooth, bhold=1, lean=.05)
    v.hands(R.REACH[0], 1, 'relaxed')
    v.look(R.TOUCH - .1, -.9, -.25, dur=.08)
    v.face(R.TOUCH + .05, .15, 'blank')                         # Eyes wide: nothing there.
    v.to(R.TOUCH + .05, .3, hp=-.12)
    v.on_ones(R.TOUCH - .2, R.TOUCH + .4)

    # ---------------- "Full of what?"  Hand still inside, head round to Sidar.
    v.look(R.L2 - .35, .7, 0, dur=.1)
    v.to(R.L2 - .3, .3, ease=smooth, hy=.55, hp=0)
    v.line(R.L2, 'voices/v2.tsv', 'Full of what')
    v.face(R.L2 - .1, .2, 'one_brow', lid=.3)

    # ---------------- "Goods! Paper goods."  Defensive. A finger at the ship on "Paper goods".
    s.line(R.L3, 'voices/s3.tsv', 'Goods! Paper goods')
    s.face(R.L3 - .1, .2, 'determined', lid=.1, brow=-.35)
    s.to(R.L3 - .05, .2, bx=40, by=150, bz=190, lean=.05)                          # Both hands up: "Goods!"
    s.to(R.L3 - .05, .2, ax=40, ay=150, az=190)
    s.hands(R.L3 + .55, 1, 'point')
    s.to(R.L3 + .6, .25, ease=smooth, bx=10, by=70, bz=300, ax=10, ay=330, az=0, th=B.heading(B.S_POS, (1.5, 5.6)), lean=0)
    s.to(R.L3 + .6, .25, hy=.0)
    s.face(R.L3 + .7, .25, 'bluff')
    s.to(R.L3 + 1.7, .4, ease=smooth, **S_ARMS_DOWN, th=B.heading(B.S_POS, B.V_EDGE))
    s.hands(R.L3 + 1.8, 1, 'relaxed')

    # ---------------- The hand comes out. He looks at it. Nothing.
    v.to(R.PULL[0], R.PULL[1] - R.PULL[0], ease=smooth, bhold=0, lean=0)
    v.to(R.PULL[0] + .1, .4, ease=smooth, bx=-60, by=170, bz=200)                  # Palm up in front of him.
    v.hands(R.PULL[0] + .2, 1, 'open')
    v.look(R.PULL[0] + .2, .1, -.6, dur=.1)
    v.to(R.PULL[0] + .2, .35, ease=smooth, hy=.15, hp=-.3)
    v.face(R.PULL[1], .3, 'unimpressed', lid=.45)
    v.look(R.PULL[1] + .9, .8, 0, dur=.08)                                          # Then at Sidar.
    v.to(R.PULL[1] + .9, .3, ease=smooth, hy=.55, hp=0)
    s.look(R.PULL[1] + .7, .5, .2, dur=.1)
    s.to(R.PULL[1] + .8, .4, ease=smooth, hy=-.4, hp=.1)                            # Sidar looks off at his ships.

    for k, pup in enumerate((s, v)):
        pup.auto_blink(80 + k, cfg.END)
