"""Son Jeton, scene 12: the arithmetic on the board; Sidar's boast; the tug-of-war with the slot.
Eyes first, then face, then head, then body."""
import math

from toonkit.camera import smooth
import blocking as B
import room as R

SIDAR_REST = dict(lid=.28, brow=-.25)
V_LID = dict(lid=.48)
S_ARM_DOWN = dict(bx=20, by=200, bz=30)
S_LARM_DOWN = dict(ax=-20, ay=200, az=30)
V_ARM_DOWN = dict(bx=10, by=270, bz=20)
REACH = dict(bx=-20, by=60, bz=160)            # Right arm out in front, at the slot.


def root(name, t):
    return B.where(name, t)


def direct(cast, cfg):
    s, v = cast['sidar'], cast['vehbi']
    qs = [cast[f'q{i}'] for i in range(len(R.QUEUE_SPOTS))]
    for i, q in enumerate(qs):
        q.face(0, .01, 'rest', lid=.35)
        q.to(0, .01, th=-.4)                                      # Turned to watch the lecture.
        q.look(0, .4, .1)

    # ---------------- The board. Vehbi explains; his finger runs along the bars and taps the X.
    s.face(0, .01, 'smug', **SIDAR_REST)
    v.face(0, .01, 'correcting', **V_LID)
    v.hands(B.L1 - .3, 1, 'point')
    v.to(B.L1 - .3, .4, ease=smooth, bx=30, by=40, bz=150)
    v.line(B.L1, 'voices/v1.tsv', 'Every month needs more new customers than the last. Here, it runs out')
    v.look(B.L1, .6, .1, dur=.2)
    v.to(B.L1 + .5, 3.5, ease=smooth, bx=70, by=40, bz=190)       # Along the bars, rising.
    v.to(R.TAP - .1, .08, hp=.06)                                  # Tap.
    v.to(R.TAP + .1, .15, hp=0)
    v.look(R.TAP + .6, -.2, 0, dur=.15)                            # Back to Sidar.
    v.to(R.TAP + .7, .4, ease=smooth, **V_ARM_DOWN)
    v.hands(R.TAP + .9, 1, 'relaxed')
    v.face(R.TAP + .7, .3, 'unimpressed', lid=.45)
    s.look(B.L1 + .5, .5, .1, dur=.2)

    # ---------------- "I built this place. With my own hands."  Arms spread at the office.
    s.look(B.L2 - .3, 0, .2, dur=.15)
    s.to(B.L2 - .4, .4, ease=smooth, th=-1.9)                     # Turns to the room, to show it off.
    s.line(B.L2, 'voices/s2.tsv', 'I built this place. With my own hands')
    s.face(B.L2, .2, 'smug', lid=.2, brow=.3)
    s.hands(B.L2 + .1, 1, 'open')
    s.hands(B.L2 + .1, -1, 'open')
    s.to(B.L2 + .1, .4, ease=smooth, bx=60, by=120, bz=150, ax=-60, ay=120, az=150, lean=-.05)
    s.hands(B.L2 + 1.7, 1, 'shrug')
    s.hands(B.L2 + 1.7, -1, 'shrug')
    s.to(B.L2 + 1.7, .3, ease=smooth, bx=10, by=80, bz=150, ax=-10, ay=80, az=150)   # "With my own hands": shows them.
    s.look(B.L2 + 1.8, .1, -.3, dur=.15)
    s.to(B.L2 + 2.9, .4, ease=smooth, **S_ARM_DOWN, **S_LARM_DOWN, lean=0)
    s.hands(B.L2 + 3.0, 1, 'relaxed')
    s.hands(B.L2 + 3.0, -1, 'relaxed')

    # ---------------- Vehbi goes to the window and starts pulling.
    v.to(B.V_WALK[0] - .1, .3, ease=smooth, th=B.heading(B.V_PATH[0], B.V_PATH[1]), loco=1)
    v.to(B.V_WALK[1] - .3, .3, ease=smooth, th=math.pi / 2, loco=0)
    v.hands(R.GRAB_V - .1, 1, 'pinch')
    v.to(R.GRAB_V - .2, .25, **REACH)
    v.line(B.L3, 'voices/v3.tsv', 'Then help me pull')
    v.face(B.L3, .2, 'determined', lid=.3)
    t = R.GRAB_V + .2
    while t < R.POP:                                               # Tug, tug.
        v.to(t, .1, lean=-.07, hp=-.03)
        v.to(t + .24, .1, lean=-.02, hp=0)
        t += .48
    s.to(B.S_WALK[0] - .1, .3, ease=smooth, th=B.heading(B.S_PATH[0], B.S_PATH[1]), loco=1)
    s.to(B.S_WALK[1] - .3, .3, ease=smooth, th=math.pi / 2, loco=0)
    s.hands(R.GRAB_S - .1, 1, 'grip')
    s.to(R.GRAB_S - .2, .25, bx=-10, by=60, bz=150)                # Hands on Vehbi's shoulder, pulling.
    s.face(R.GRAB_S, .2, 'determined', lid=.25, brow=.2)
    t = R.GRAB_S + .1
    while t < R.POP:
        s.to(t, .1, lean=-.09)
        s.to(t + .24, .1, lean=-.03)
        t += .48

    # ---------------- "Hmph."  POP. They stagger back; Sidar catches the tokens.
    s.line(B.L4, 'voices/s4.tsv', 'Hmph')
    for p in (s, v):
        p.to(R.POP, .08, lean=-.2, squash=.05)
        p.to(R.POP + .35, .3, ease=smooth, lean=0, squash=0)
    v.face(R.POP, .1, 'one_brow', lid=.3)
    s.hands(R.CATCH - .3, 1, 'open')
    s.to(R.CATCH - .3, .25, bx=10, by=90, bz=150)
    s.hands(R.CATCH, 1, 'grip')
    s.face(R.CATCH + .1, .3, 'smug', lid=.2, brow=.2)
    s.to(R.CATCH + .1, .3, ease=smooth, th=-.6)                     # Turns round with them, pleased.
    v.to(R.POP + .4, .4, ease=smooth, **V_ARM_DOWN, th=-1.2)
    v.hands(R.POP + .5, 1, 'relaxed')
    v.look(R.CATCH + .2, .4, -.1, dur=.15)

    for k, pup in enumerate([s, v] + qs):
        pup.auto_blink(50 + k, cfg.END)
