"""Son Jeton, scene 05: the grocer's. Sidar's warning, Vehbi's textbook definition, the grocer flipping the price cards
behind his back. Blocking from blocking.py, timing from room.py. Eyes first, then face, then head, then body."""
import math

from toonkit.camera import smooth
import blocking as B
import room as R

SIDAR_REST = dict(lid=.28, brow=-.25)
V_LID = dict(lid=.48)
V_ARM_DOWN = dict(bx=10, by=270, bz=20)
S_ARM_DOWN = dict(bx=20, by=200, bz=30)
G_ARM_DOWN = dict(bx=20, by=200, bz=30)


def root(name, t):
    return {'vehbi': B.vehbi, 'sidar': B.sidar, 'grocer': B.grocer}[name](t)


def glasses_push(v, t):
    v.hands(t, 1, 'point')
    v.to(t, .14, bx=-34, by=-118, bz=120)
    v.to(t + .3, .22, **V_ARM_DOWN)
    v.hands(t + .42, 1, 'relaxed')


def direct(cast, cfg):
    s, v, g = cast['sidar'], cast['vehbi'], cast['grocer']

    # ---------------- They have just come in. The bell; the grocer looks up from his counter.
    s.face(0, .01, 'determined', **SIDAR_REST)
    v.face(0, .01, 'unimpressed')
    g.face(0, .01, 'rest', lid=.35)
    g.look(0, 0, -.35)                                     # Down at his counter...
    g.to(0, .01, hp=.1)
    g.look(.45, 0, 0, dur=.15)                             # ...up at his customers.
    g.to(.4, .3, ease=smooth, hp=0)
    g.face(.55, .3, 'almost_smile', lid=.3)
    v.look(.2, -.2, .2, dur=.2)                            # Vehbi takes in the shelves.

    # ---------------- "Tonight, your money shrinks."  Ominous, leaning in.
    s.look(B.L1 - .25, 0, 0, dur=.1)
    s.to(B.L1 - .2, .35, ease=smooth, lean=.08, hp=-.06, hy=.1)
    s.line(B.L1, 'voices/s1.tsv', 'Tonight, your money shrinks')
    s.face(B.L1, .2, 'determined', lid=.35, brow=.2)
    s.hands(B.L1 + .7, 1, 'point')
    s.to(B.L1 + .7, .2, bx=20, by=120, bz=120)            # A finger at his pocket: "your money".
    s.to(B.L1 + 1.9, .35, ease=smooth, lean=0, hp=0, hy=0, **S_ARM_DOWN)
    s.hands(B.L1 + 2.0, 1, 'relaxed')
    v.look(B.L1 + .1, 0, 0, dur=.12)
    v.face(B.L1 + .4, .3, 'one_brow', **V_LID)

    # ---------------- The definition. Glasses up, eyes shut, word-perfect.
    glasses_push(v, B.L2 - .45)
    v.face(B.L2 - .05, .25, 'correcting', lid=.92)        # Eyes shut while he recites.
    v.to(B.L2, .4, ease=smooth, hp=-.06, hr=.04)          # Chin up a little.
    v.line(B.L2, 'voices/v2.tsv', 'Devaluation. The lira loses value against foreign currency, so imports cost more')
    v.to(B.L2 + 3.4, .4, ease=smooth, hr=-.03)
    v.to(B.L2 + 5.6, .4, ease=smooth, hr=.03)
    v.hands(B.L2 + 2.0, 1, 'point')                        # One raised finger on "against foreign currency".
    v.to(B.L2 + 2.0, .25, bx=0, by=150, bz=140)
    v.to(B.L2 + 3.6, .3, ease=smooth, **V_ARM_DOWN)
    v.hands(B.L2 + 3.8, 1, 'relaxed')

    # ---------------- Behind him: the grocer turns his back and flips the cards, one by one, to double.
    g.look(R.TURN - .3, -.5, 0, dur=.15)                   # A glance at Vehbi first.
    g.face(R.TURN - .3, .2, 'rest', lid=.3)
    g.to(R.TURN, .55, ease=smooth, th=B.G_BACK)
    for i, ts in enumerate(R.SWAPS):
        x = R.CARDS[i][0]
        reach = (x - B.G_POS[0])                              # To his right as he faces the shelves.
        g.hands(ts - .45, 1, 'pinch')
        g.to(ts - .5, .3, ease=smooth, bx=-30 + reach * 40, by=50, bz=150 + reach * 20)
        g.to(ts + R.FLIP + .05, .2, bx=-30 + reach * 40, by=70, bz=140 + reach * 20)
        g.to(ts - .5, .4, ease=smooth, th=B.G_BACK - reach * .5)
    g.to(R.SWAPS[-1] + .6, .35, ease=smooth, **G_ARM_DOWN)
    g.hands(R.SWAPS[-1] + .7, 1, 'relaxed')
    g.to(R.TURN_BACK, .55, ease=smooth, th=B.G_TH0)
    g.face(R.TURN_BACK + .3, .3, 'bluff', lid=.25)        # All innocence.
    g.look(R.TURN_BACK + .3, -.3, 0, dur=.15)
    g.to(R.TURN_BACK + .6, .3, ease=smooth, hp=-.04)       # Wipes nothing off the counter: hands behind him.

    # ---------------- Sidar sees all of it; Vehbi, eyes shut, sees none of it.
    s.look(R.TURN + .2, -.5, .1, dur=.2)                   # Past Vehbi to the shelves.
    s.face(R.SWAPS[0] + .2, .3, 'smug', lid=.25, brow=.0)
    s.look(R.SWAPS[1] + .1, -.55, .12, dur=.15)
    s.to(R.SWAPS[1], .4, ease=smooth, hp=.05)              # Slow nods as each card flips.
    s.to(R.SWAPS[1] + .45, .3, ease=smooth, hp=-.02)
    s.to(R.SWAPS[2], .4, ease=smooth, hp=.06)
    s.to(R.SWAPS[2] + .45, .3, ease=smooth, hp=0)

    # ---------------- "He's read the same book."  A nod at the grocer.
    s.look(B.L3 - .3, -.1, 0, dur=.1)
    s.line(B.L3, 'voices/s3.tsv', "He's read the same book")
    s.face(B.L3, .25, 'smug', **SIDAR_REST)
    s.to(B.L3 + .2, .3, hy=-.25, hp=.06)                  # The nod towards the grocer.
    s.to(B.L3 + .7, .3, hy=0, hp=0)
    s.look(B.L3 + .2, -.5, .15, dur=.12)
    s.look(B.L3 + .9, 0, 0, dur=.12)

    # ---------------- Vehbi opens his eyes and looks round. The grocer smiles.
    v.face(B.L3 + 1.5, .2, 'unimpressed', lid=.42)
    v.look(B.L3 + 1.7, .55, .2, dur=.15)
    v.to(B.L3 + 1.7, .35, ease=smooth, hy=.3)
    v.face(B.L3 + 2.2, .25, 'one_brow', **V_LID)
    g.look(B.L3 + 1.9, -.4, -.05, dur=.12)
    g.face(B.L3 + 2.0, .3, 'forced_smile', lid=.2)

    for pup, seed in ((s, 9), (v, 10), (g, 11)):
        pup.auto_blink(seed, cfg.END)
