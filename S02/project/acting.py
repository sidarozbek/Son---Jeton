"""Son Jeton, scene 02: the tug of war over the book. Blocking from blocking.py, mechanics from room.py.
Eyes first, then face, then head, then body."""
import math

import numpy as np

from toonkit.camera import smooth
import blocking as B
import room as R

SIDAR_REST = dict(lid=.28, brow=-.25)
V_LID = dict(lid=.48)


def root(name, t):
    return B.vehbi(t) if name == 'vehbi' else B.sidar(t)


def glasses_push(v, t):
    v.hands(t, 1, 'point')
    v.to(t, .14, bx=-34, by=-118, bz=120)
    v.to(t + .3, .22, bx=10, by=270, bz=20)
    v.hands(t + .42, 1, 'relaxed')


def live_pin(pup, side, fn):
    """A hand that follows a moving point: re-plant the pin every frame before the pose is solved."""
    orig = pup.update

    def update(t, dt, root_xy):
        pup.pins[side] = np.array(fn(t), float)
        return orig(t, dt, root_xy)
    pup.update = update


def facing(pup, who, other, t0, t1, step=.25):
    """Keep facing the other person while the pair turns."""
    t = t0
    while t <= t1 + 1e-6:
        a, b = (B.sidar(t), B.vehbi(t)) if who == 'sidar' else (B.vehbi(t), B.sidar(t))
        pup.to(t, step, ease=smooth, th=B.heading(a, b))
        t += step


def direct(cast, cfg):
    s, v = cast['sidar'], cast['vehbi']
    th_s = B.heading(B.S_START, B.V_START)
    th_v = B.heading(B.V_START, B.S_START)

    # ---------------- Where Scene 01 left them.
    s.face(0, .01, 'smug', **SIDAR_REST)
    s.to(0, .01, th=th_s)
    v.face(0, .01, 'unimpressed')
    v.to(0, .01, th=th_v, ax=26, ay=120, az=190)

    # ---------------- "January 1980. I was in that room."
    s.line(B.L1, 'voices/s1.tsv', 'January 1980')
    s.to(B.L1 - .1, .2, hp=.12, squash=-.05)                           # Chin up, chest out.
    s.look(B.L1 + .5, .1, .5, dur=.3)                                  # Eyes up and away: he is there.
    s.face(B.L1 + .4, .4, 'determined', lid=.35, brow=.1)              # Lids narrow: seeing it.
    s.hands(B.L1 + 2.2, 1, 'point')
    s.to(B.L1 + 2.3, .25, bx=30, by=-150, bz=120, hy=.12)              # Points up at "that room".
    s.to(B.L1 + 3.4, .3, bx=20, by=200, bz=30, hy=0)
    s.hands(B.L1 + 3.6, 1, 'relaxed')
    s.look(B.L1 + 3.3, 0, 0, dur=.15)
    s.face(B.L1 + 3.3, .2, 'smug', **SIDAR_REST)
    v.look(B.L1 + 2.4, .05, .45, dur=.12)                              # Vehbi's eyes follow the finger, a hair late...
    v.look(B.L1 + 3.0, 0, 0, dur=.12)                                  # ...and come back, unimpressed.

    # ---------------- The book: "That's not what it says."
    glasses_push(v, 4.3)
    v.to(4.6, .25, ax=36, ay=95, az=230, hp=-.05)                      # Opens it, turns it to him at arm's length.
    v.line(B.L2, 'voices/v2.tsv', "That's not what it says")
    v.face(B.L2, .12, 'correcting', **V_LID)
    v.face(B.L2 + 1.3, .3, 'unimpressed')
    s.look(B.L2 + .3, -.1, -.45, dur=.2)                               # Sidar reads. Slowly.
    s.to(B.L2 + .3, .4, ease=smooth, hp=-.12, lean=.1)
    s.face(B.L2 + 1.2, .5, 'angry', lid=.2)                            # Anger arrives late.

    # ---------------- "Then the book is wrong!"  The lunge.
    s.line(B.L3, 'voices/s3.tsv', 'Then the book is wrong')
    s.look(B.L3 - .1, 0, 0)
    s.to(B.L3 - .1, .12, hp=.1, lean=-.08, squash=.05)                 # Wind up.
    s.to(R.GRAB - .12, .12, lean=.32, sway=.2, hr=.05, squash=-.05)    # Shoulder first, at the book.
    s.on_ones(R.GRAB - .3, R.GRAB + .3)

    # ---------------- The tug of war. Both of Sidar's hands and Vehbi's left hand ride the book.
    def book_at(dx=0.0):
        def f(t):
            x, y, z = B.book(t)
            a = B.heading(B.sidar(t), B.vehbi(t)) + math.pi / 2
            return (x + dx * math.cos(a), y + dx * math.sin(a), z)
        return f
    live_pin(s, -1, book_at(-.07))
    live_pin(s, 1, book_at(.07))
    live_pin(v, -1, book_at(0))
    s.pin(-1, B.book(R.GRAB)); s.pin(1, B.book(R.GRAB)); v.pin(-1, B.book(R.GRAB))
    s.hands(R.GRAB - .1, -1, 'grip'); s.hands(R.GRAB - .1, 1, 'grip')
    s.to(R.GRAB - .15, .15, ahold=1, bhold=1)
    v.to(R.GRAB - .3, .2, ahold=1)
    s.face(R.GRAB, .1, 'grimace', lid=.15)
    v.face(R.GRAB, .1, 'unimpressed')
    s.to(B.TURN[0], .3, loco=1)
    v.to(B.TURN[0], .3, loco=1)
    facing(s, 'sidar', 'vehbi', B.TURN[0], B.TURN[1] + .2)
    facing(v, 'vehbi', 'sidar', B.TURN[0], B.TURN[1] + .2)
    for k in R.YANKS:                                                  # Each yank: Sidar throws his weight back; Vehbi barely sways.
        s.to(k - .06, .06, lean=-.26, sway=-.12, squash=.04)
        s.to(k + .12, .25, lean=.1, sway=.06, squash=0)
        v.to(k, .08, lean=.07)
        v.to(k + .15, .3, lean=0)
    s.on_ones(B.TURN[0], B.TURN[1])
    s.to(B.TURN[1], .3, loco=0)
    v.to(B.TURN[1], .3, loco=0)
    v.look(R.SLIP + .05, .05, -.5, dur=.15)                            # Vehbi's eyes catch the contract going.
    v.look(R.SLIP + .5, 0, 0, dur=.2)

    # ---------------- He lets go at once, and fixes his tie. Never embarrassed.
    s.to(R.RELEASE, .06, ahold=0, bhold=0, lean=-.04, sway=0)
    s.hands(R.RELEASE, -1, 'relaxed'); s.hands(R.RELEASE + .1, 1, 'pinch')
    s.face(R.RELEASE + .05, .15, 'determined', **SIDAR_REST)
    s.to(R.RELEASE + .1, .2, bx=-46, by=120, bz=80, hp=.12)            # Fingers to the knot.
    s.to(R.RELEASE + .55, .12, bx=-40, by=110, bz=82, hr=.04)          # A tug at the knot...
    s.to(R.RELEASE + .75, .12, bx=-44, by=118, bz=80, hr=-.02)         # ...and back.
    s.to(R.RELEASE + 1.2, .3, bx=20, by=200, bz=30, hr=0)
    s.hands(R.RELEASE + 1.3, 1, 'relaxed')
    s.face(R.RELEASE + 1.2, .3, 'smug', **SIDAR_REST)
    v.to(R.RELEASE, .08, ahold=0, lean=-.1)                            # The pull goes; he rocks back a touch.
    v.to(R.RELEASE + .2, .3, lean=0, ax=6, ay=250, az=30)            # Book down to his side. Still in hand.
    v.face(R.RELEASE + .2, .2, 'unimpressed', eye_s=1.04)

    # ---------------- Vehbi: down at the contract, then slowly up at him.
    v.look(15.5, -.05, -.65, dur=.25)
    v.to(15.5, .5, ease=smooth, hp=-.14)
    v.look(16.5, .05, .05, dur=.7)
    v.to(16.4, .9, ease=smooth, hp=.02)
    v.face(16.6, .5, 'slow_lid')
    v.blink(17.5)
    v.face(17.7, .3, 'unimpressed')

    # ---------------- Sidar surveys the room, not looking at him. His eyes go to the door.
    s.look(17.5, .6, .1, dur=.2)
    s.to(17.55, .5, ease=smooth, hy=.35, th=B.heading(B.sidar(19), (3.05, 4.4)) - .3)
    s.look(18.3, .45, .05, dur=.2)
    s.face(18.2, .3, 'determined', **SIDAR_REST)

    for pup, seed in ((s, 3), (v, 4)):
        pup.auto_blink(seed, cfg.END)
