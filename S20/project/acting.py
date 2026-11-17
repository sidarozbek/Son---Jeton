"""Son Jeton, scene 20: "Last one. Token five." The token goes see-through. "It's... see-through." "It's a perfectly
good tok—" The line crackles; the picture folds away. Eyes, face, head, body."""
import math

from toonkit.camera import smooth
import blocking as B
import room as R

ARMS_DOWN = dict(ax=10, ay=330, az=0, bx=10, by=330, bz=0)
TOKEN_UP = dict(bx=-20, by=-10, bz=150)


def root(name, t):
    return B.where(name, t)


def direct(cast, cfg):
    s, v, o = cast['sidar'], cast['vehbi'], cast['officer']
    s.face(0, .01, 'rest', lid=.3, brow=.3)
    v.face(0, .01, 'rest', lid=.35, brow=.1)
    o.face(0, .01, 'rest', lid=.6, brow=-.2)
    o.to(0, .01, hp=-.4, lean=.12, ax=60, ay=260, az=120, bx=40, by=230, bz=150)
    o.hands(0, 1, 'pinch')

    # ---------------- "Last one. Token five."  Solemn: the token held up between them.
    s.hands(R.TOKEN_UP - .2, 1, 'pinch')
    s.to(R.TOKEN_UP - .2, .45, ease=smooth, **TOKEN_UP)
    s.look(R.TOKEN_UP, .2, .3, dur=.15)                                              # At the token.
    s.line(R.L1, 'voices/s1.tsv', 'Last one. Token five')
    s.face(R.L1 - .1, .4, 'rest', lid=.45, brow=.5)
    s.to(R.L1, .5, ease=smooth, hp=.05)
    v.look(R.TOKEN_UP + .1, -.2, .3, dur=.15)
    v.face(R.L1 + .5, .4, 'rest', lid=.3, brow=.3)

    # ---------------- It goes see-through. Both stare at it.
    v.look(R.SEE[0] + .3, -.1, .35, dur=.1)
    v.face(R.SEE[0] + .4, .3, 'curious', lid=.15)
    s.face(R.SEE[0] + .6, .3, 'blank')
    s.to(R.SEE[0] + .5, .5, ease=smooth, hp=.15, bz=130, by=-20)                       # Brings it closer to his eyes.

    # ---------------- "It's... see-through."
    v.line(R.L2, 'voices/v2.tsv', "It's see-through")
    v.look(R.L2 + .7, .1, .1, dur=.12)                                                 # Up at Sidar on "see-through".
    v.face(R.L2 + .6, .3, 'one_brow')

    # ---------------- "It's a perfectly good tok—"  Defensive, then into the slot anyway.
    s.line(R.L3, 'voices/s3.tsv', "It's a perfectly good tok")
    s.face(R.L3 - .1, .2, 'bluff')
    s.to(R.L3, .3, ease=smooth, hp=0, bz=150, by=-10)
    s.look(R.COIN_IN - .5, -.8, 0, dur=.1)
    s.to(R.COIN_IN - .45, .35, ease=smooth, th=B.S_PHONE)                              # To the phone...
    s.pin(1, R.SLOT20)
    s.to(R.COIN_IN - .15, .3, ease=smooth, bhold=1)                                   # ...and in it goes.
    s.to(R.COIN_IN + .35, .3, ease=smooth, bhold=0, **ARMS_DOWN)
    s.hands(R.COIN_IN + .4, 1, 'relaxed')

    # ---------------- The crackle: both jolt.
    for p, k in ((s, 0), (v, 1)):
        p.to(R.CRACKLE + .05 * k, .1, squash=.04)
        p.to(R.CRACKLE + .25, .3, squash=0)
        p.face(R.CRACKLE + .05, .15, 'panic')
        p.on_ones(R.CRACKLE, R.FOLD[0] + .5)
    s.look(R.CRACKLE + .1, .3, .4, dur=.08)
    v.look(R.CRACKLE + .1, -.3, .4, dur=.08)

    for k, pup in enumerate((s, v, o)):
        pup.auto_blink(140 + k, cfg.END)
