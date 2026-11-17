"""Son Jeton, scene 16: the customs officer stamps; ships come out of a filing cabinet.
"See? One stamp, one ship." / "It came out of a filing cabinet." / "Where else do ships come from?"
The officer never speaks and never looks up from his forms. Eyes, face, head, body."""
import math

from toonkit.camera import smooth
import blocking as B
import room as R

ARMS_DOWN = dict(ax=10, ay=330, az=0, bx=10, by=330, bz=0)


def root(name, t):
    return B.where(name, t)


def direct(cast, cfg):
    s, v, o = cast['sidar'], cast['vehbi'], cast['officer']
    s.face(0, .01, 'smug', lid=.3, brow=.2)
    v.face(0, .01, 'rest', lid=.35, brow=.15)
    o.face(0, .01, 'rest', lid=.55, brow=-.2)
    o.to(0, .01, hp=-.35, lean=.08, ax=60, ay=260, az=120)       # Head down over his forms; left hand on the desk.
    s.look(0, -.3, 0)

    # ---------------- The officer's stamps: up, down hard on the form, up. He never looks at anyone.
    o.pin(1, (R.PAPER[0] - .02, R.PAPER[1] - .05, R.PAPER[2] + .09))
    for ts in R.STAMPS:
        o.to(ts - .55, .3, ease=smooth, bx=40, by=120, bz=170, bhold=0)
        o.to(ts - .08, .08, bhold=1)
        o.on_ones(ts - .1, ts + .15)
        o.to(ts + .12, .05, squash=.03)
        o.to(ts + .2, .15, squash=0)
        o.to(ts + .3, .3, ease=smooth, bhold=0, bx=30, by=200, bz=140)
    o.hands(0, 1, 'pinch')

    # ---------------- They watch the first ship come out of the drawer and hop into the sea.
    DRAWER = R.DRAWER_MOUTH[:2]
    v.look(R.STAMPS[0] + .6, -.6, -.1, dur=.1)
    v.to(R.STAMPS[0] + .65, .3, ease=smooth, hy=.8)
    v.to(R.STAMPS[0] + 1.6, 1.6, ease=smooth, hy=0, hp=.1)
    s.look(R.STAMPS[0] + .3, .4, 0, dur=.1)                                       # Sidar watches Vehbi's face, not the ship.
    s.face(R.STAMPS[0] + .9, .4, 'smug', lid=.15, brow=.5)
    s.to(R.STAMPS[0] + 1.0, .5, ease=smooth, hp=.12, hr=.08)
    v.face(R.STAMPS[0] + 1.0, .3, 'curious', lid=.2)

    # ---------------- "See? One stamp, one ship."  Proud: a hand from the desk to the sea.
    s.to(R.L1 - .3, .3, ease=smooth, th=B.S_TH0, hy=0, hp=.05)
    s.look(R.L1 - .3, 0, 0, dur=.1)
    s.line(R.L1, 'voices/s1.tsv', 'See? One stamp, one ship')
    s.face(R.L1 - .1, .25, 'smug', lid=.2, brow=.4)
    s.hands(R.L1 + .5, 1, 'open')
    s.to(R.L1 + .5, .3, ease=smooth, bx=200, by=150, bz=120, lean=-.04)          # "One stamp," at the desk...
    s.to(R.L1 + 1.2, .4, ease=smooth, bx=-60, by=60, bz=260)             # "...one ship," out to sea.
    s.to(R.L1 + 2.3, .5, ease=smooth, **ARMS_DOWN, lean=0)
    s.hands(R.L1 + 2.3, 1, 'relaxed')
    v.face(R.L1 + .6, .3, 'unimpressed', lid=.45)

    # ---------------- "It came out of a filing cabinet."  Deadpan, a finger at the cabinet.
    v.look(R.L2 - .3, -.5, 0, dur=.1)
    v.line(R.L2, 'voices/v2.tsv', 'It came out of a filing cabinet')
    v.face(R.L2 - .1, .2, 'correcting', lid=.4)
    v.hands(R.L2 + .3, 1, 'point')
    v.to(R.L2 + .3, .3, ease=smooth, bx=-40, by=110, bz=250, hy=.35)
    v.to(R.L2 + 2.0, .4, ease=smooth, bx=10, by=330, bz=0, hy=0)
    v.hands(R.L2 + 2.1, 1, 'relaxed')
    s.to(R.STAMPS[1] + .6, .5, ease=smooth, hp=0, hr=0)
    s.face(R.L2 + .4, .3, 'curious', lid=.25)

    # ---------------- "Where else do ships come from?"  He really wants to know. Palms up.
    s.line(R.L3, 'voices/s3.tsv', 'Where else do ships come from')
    s.face(R.L3 - .1, .3, 'asking')
    s.hands(R.L3 + .1, 1, 'open')
    s.hands(R.L3 + .1, -1, 'open')
    s.to(R.L3 + .1, .35, ease=smooth, ax=120, ay=170, az=150, bx=120, by=170, bz=150, lean=-.03)
    s.to(R.L3 + 1.9, .5, ease=smooth, **ARMS_DOWN, lean=0)
    v.face(R.L3 + 1.2, .4, 'slow_lid')

    # ---------------- Third stamp: both look at the drawer. A tiny ship peeks out.
    v.look(R.STAMPS[2] + .55, -.6, -.2, dur=.1)
    v.to(R.STAMPS[2] + .6, .35, ease=smooth, hy=.8)
    s.look(R.STAMPS[2] + .45, -.9, -.1, dur=.1)                                   # A glance back at the drawer.
    s.to(R.STAMPS[2] + .5, .45, ease=smooth, hy=1.2)

    for k, pup in enumerate((s, v, o)):
        pup.auto_blink(90 + k, cfg.END)
