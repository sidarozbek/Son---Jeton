"""Son Jeton, scene 17: stamp D6; "Tax refunds and export credits. It's in the book."; "I put these ships on paper.";
"That's the problem." The officer never speaks and never looks up. Eyes, face, head, body."""
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
    s.face(0, .01, 'smug', lid=.3, brow=.2)
    v.face(0, .01, 'unimpressed', lid=.4)
    o.face(0, .01, 'rest', lid=.6, brow=-.2)
    o.to(0, .01, hp=-.38, lean=.08, ax=60, ay=260, az=120, bx=40, by=230, bz=150)   # Head down over his forms.
    o.hands(0, 1, 'pinch')
    s.look(0, .3, 0)
    v.look(0, -.2, 0)

    # ---------------- The stamp: D6. They look up; no one flinches. The officer doesn't even look up.
    for p in (s, v):
        p.look(R.STAMP[1], 0, .5, dur=.2)
        p.look(R.CLIP[3] + .1, 0, 0, dur=.3)

    # ---------------- Vehbi: the book. "Tax refunds and export credits. It's in the book."
    v.to(R.BOOK_OPEN, .4, ease=smooth, ax=-10, ay=70, az=180, hp=-.18)              # The book up in front of him.
    v.look(R.BOOK_OPEN, 0, -.6, dur=.15)
    v.face(R.BOOK_OPEN, .3, 'correcting', lid=.35)
    v.line(R.L1, 'voices/v1.tsv', "Tax refunds and export credits. It's in the book")
    v.hands(R.L1 + .1, 1, 'point')
    v.to(R.L1 + .1, .35, ease=smooth, bx=-50, by=80, bz=200)                        # Finger on the page.
    for k, tt in enumerate((8.6, 9.2)):                                               # "It's in the book": two taps.
        v.to(tt, .08, bz=185)
        v.to(tt + .1, .1, bz=200)
    v.look(8.45, .2, 0, dur=.12)
    v.to(8.45, .3, ease=smooth, hp=0)                                                 # Eyes up to Sidar for the end.
    v.to(R.L1 + 3.9, .4, ease=smooth, **V_BOOK, bx=10, by=330, bz=0)
    v.hands(R.L1 + 4.0, 1, 'relaxed')

    # ---------------- Sidar, proud: "I put these ships on paper."
    s.line(R.L2, 'voices/s2.tsv', 'I put these ships on paper')
    s.face(R.L2 - .1, .25, 'smug', lid=.15, brow=.5)
    s.to(R.L2 - .1, .35, ease=smooth, lean=-.06, hp=.1)                               # Chest out.
    s.hands(R.L2 + .7, 1, 'open')
    s.to(R.L2 + .7, .4, ease=smooth, bx=-40, by=80, bz=260)                           # A hand out to his ships.
    s.to(R.L2 + 2.1, .5, ease=smooth, **ARMS_DOWN, lean=0, hp=.05)
    s.hands(R.L2 + 2.2, 1, 'relaxed')

    # ---------------- Vehbi, flat: "That's the problem."
    v.line(R.L3, 'voices/v3.tsv', "That's the problem")
    v.face(R.L3 - .1, .2, 'slow_lid')
    v.to(R.L3 + .9, .4, ease=smooth, hp=-.05)
    s.face(R.L3 + .5, .35, 'bluff')                                                   # He doesn't hear it.
    s.look(R.L3 + .6, -.5, .1, dur=.1)

    for k, pup in enumerate((s, v, o)):
        pup.auto_blink(110 + k, cfg.END)
