"""Son Jeton, scene 19: stamp D7; "Empty containers. Fake invoices. Refunds for goods that never left."; invoices rain
out of the containers; "Told you!" / "You said the ships were full." / "Of invoices!" Eyes, face, head, body."""
import math

from toonkit.camera import smooth
import blocking as B
import room as R

ARMS_DOWN = dict(ax=10, ay=330, az=0, bx=10, by=330, bz=0)
V_BOOK = dict(ax=6, ay=250, az=30)


def root(name, t):
    return B.where(name, t)


def direct(cast, cfg):
    s, v, o = cast['sidar'], cast['vehbi'], cast['officer']
    s.face(0, .01, 'smug', lid=.2, brow=.4)
    v.face(0, .01, 'unimpressed', lid=.4)
    o.face(0, .01, 'rest', lid=.6, brow=-.2)
    o.to(0, .01, hp=-.4, lean=.12, ax=60, ay=260, az=120, bx=40, by=230, bz=150)
    o.hands(0, 1, 'pinch')
    s.to(0, .01, hp=.08)
    v.to(0, .01, hp=.12)                                                              # Looking up at Sidar on the deck.

    # ---------------- The stamp: D7. They look up; nobody flinches.
    for p in (s, v):
        p.look(R.STAMP[1], 0, .5, dur=.2)
        p.look(R.CLIP[3] + .1, 0, 0, dur=.3)

    # ---------------- "Empty containers. Fake invoices. Refunds for goods that never left."  Counting on his fingers.
    v.line(R.L1, 'voices/v1.tsv', 'Empty containers. Fake invoices. Refunds for goods that never left')
    v.face(R.L1 - .1, .2, 'correcting', lid=.35)
    v.hands(R.L1, 1, 'point')
    for k, tt in enumerate((R.L1, R.L1 + 1.3, R.L1 + 2.5)):                          # One, two, three.
        v.to(tt, .2, ease=smooth, bx=40, by=110 - k * 15, bz=170)
        v.to(tt + .5, .3, ease=smooth, bx=30, by=140, bz=150)
    v.look(R.LIDS[0] - .1, .4, .4, dur=.1)                                          # A glance at the containers.
    v.look(R.BURST + .2, .3, .7, dur=.1)
    v.look(R.L1 + 2.6, 0, .3, dur=.15)
    v.to(R.L1 + 4.4, .4, ease=smooth, bx=10, by=330, bz=0)
    v.hands(R.L1 + 4.5, 1, 'relaxed')
    s.look(R.LIDS[0], .7, -.2, dur=.1)                                               # Sidar turns to the containers...
    s.to(R.LIDS[0], .4, ease=smooth, hy=.9)
    s.face(R.BURST, .2, 'realizing')                                                 # ...invoices everywhere...
    s.to(R.BURST, .3, ease=smooth, hp=.3)
    s.look(R.BURST + 1.0, 0, .9, dur=.2)
    s.to(9.3, .5, ease=smooth, hy=0, hp=.1)
    s.face(9.4, .3, 'smug', lid=.1, brow=.5)                                         # ...and he sees an opportunity.

    # ---------------- He catches one and waves it: "Told you!"
    s.hands(R.CATCH[0], 1, 'open')
    s.to(R.CATCH[0], .35, ease=smooth, bx=30, by=60, bz=200)
    s.hands(R.CATCH[1], 1, 'pinch')
    s.line(R.L2, 'voices/s2.tsv', 'Told you')
    s.to(R.CATCH[1] + .05, .2, ease=smooth, bx=40, by=-40, bz=120, lean=-.04)       # Up high, waving.
    s.face(R.L2 - .05, .15, 'try_smile')
    v.face(R.L2 + .3, .3, 'slow_lid')

    # ---------------- "You said the ships were full."
    v.line(R.L3, 'voices/v3.tsv', 'You said the ships were full')
    v.face(R.L3 - .1, .2, 'one_brow')
    s.face(R.L3 + .6, .3, 'bluff')

    # ---------------- "Of invoices!"  Triumphant.
    s.line(R.L4, 'voices/s4.tsv', 'Of invoices')
    s.face(R.L4 - .05, .2, 'smug', lid=.1, brow=.6)
    s.to(R.L4, .2, ease=smooth, bx=60, by=-70, bz=100, lean=-.06, hp=.15)
    v.face(R.L4 + 1.0, .4, 'unimpressed', lid=.5)

    for k, pup in enumerate((s, v, o)):
        pup.auto_blink(130 + k, cfg.END)
