"""Son Jeton, scene 09: 12 September 1980. No one speaks. No joke. Small, quiet movements only.
Blocking from blocking.py, timing from room.py. Eyes first, then face, then head, then body."""
import math

from toonkit.camera import smooth
import blocking as B
import room as R

S_ARM_DOWN = dict(bx=20, by=200, bz=30)


def root(name, t):
    return B.vehbi(t) if name == 'vehbi' else B.sidar(t)


def direct(cast, cfg):
    s, v = cast['sidar'], cast['vehbi']

    # ---------------- They stand on the empty street. Sidar is not smug today.
    s.face(0, .01, 'rest', lid=.38, brow=-.1)
    v.face(0, .01, 'rest', lid=.35)
    s.look(0, .3, 0)
    v.look(0, .5, 0)

    # ---------------- Vehbi looks along the street, one way and the other. Slowly.
    v.look(3.0, .6, .05, dur=.4)
    v.to(3.0, 1.2, ease=smooth, hy=.35)
    v.look(4.8, -.5, .05, dur=.5)
    v.to(4.8, 1.4, ease=smooth, hy=-.3)
    v.look(6.3, 0, 0, dur=.3)
    v.to(6.3, .8, ease=smooth, hy=0)
    v.face(5.0, .8, 'rest', lid=.42, brow=.15)
    s.look(4.2, -.2, -.1, dur=.4)

    # ---------------- Sidar walks to the payphone. Vehbi follows, a few steps behind.
    s.to(B.S_WALK[0] - .1, .4, ease=smooth, th=B.heading(B.S_START, B.S_PHONE), loco=1)
    s.to(B.S_WALK[1] - .4, .4, ease=smooth, th=math.pi / 2, loco=0)        # Faces the wall and the phone.
    v.to(B.V_WALK[0] - .1, .4, ease=smooth, th=B.heading(B.V_START, B.V_END), loco=1)
    v.to(B.V_WALK[1] - .4, .4, ease=smooth, th=B.heading(B.V_END, B.S_PHONE), loco=0)

    # ---------------- The third token. He looks at it a moment; then into the slot.
    s.hands(R.TOKEN_OUT - .2, 1, 'pinch')
    s.to(R.TOKEN_OUT - .3, .5, ease=smooth, bx=-6, by=40, bz=150, hp=.06)
    s.look(R.TOKEN_OUT, .1, -.35, dur=.3)
    s.to(R.COIN_IN - .45, .5, ease=smooth, bx=-24, by=20, bz=220, hp=0)
    s.look(R.COIN_IN - .3, 0, .1, dur=.3)
    s.to(R.COIN_IN + .5, .6, ease=smooth, **S_ARM_DOWN)
    s.hands(R.COIN_IN + .6, 1, 'relaxed')
    v.look(R.TOKEN_OUT + .2, .2, -.2, dur=.3)

    # ---------------- The stamp: they look up, slowly; no flinch.
    for p in (s, v):
        p.look(R.STAMP[1] + .2, 0, .4, dur=.4)

    for pup, seed in ((s, 21), (v, 22)):
        pup.auto_blink(seed, cfg.END)
