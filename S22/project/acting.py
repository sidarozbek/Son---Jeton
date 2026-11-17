"""Son Jeton, scene 22: "August 1989. Money can cross the border freely now." D8. "If money flows... a token flows
too." The sixth token hops out of the river into Vehbi's hand. "I taught you where to look." Eyes, face, head, body."""
import math

from toonkit.camera import smooth
import blocking as B
import room as R

V_BOOK = dict(ax=6, ay=250, az=30)
V_BOOK_UP = dict(ax=-10, ay=70, az=180)
ARMS_DOWN = dict(ax=10, ay=330, az=0, bx=10, by=330, bz=0)


def root(name, t):
    return B.where(name, t)


def direct(cast, cfg):
    s, v = cast['sidar'], cast['vehbi']
    s.face(0, .01, 'rest', lid=.5, brow=.6, ba=.6, smile=-.15)      # Where Scene 21 left him.
    v.face(0, .01, 'rest', lid=.3, brow=.4)
    s.to(0, .01, hp=-.12, squash=.02)
    s.look(0, .1, -.5)

    # ---------------- The book. "August 1989. Money can cross the border freely now."
    v.to(R.BOOK_OPEN, .4, ease=smooth, **V_BOOK_UP, hp=-.18, th=B.heading(B.V_POS, B.S_POS) - .7)
    v.look(R.BOOK_OPEN, 0, -.6, dur=.15)
    v.face(R.BOOK_OPEN + .2, .3, 'realizing')
    v.line(R.L1, 'voices/v1.tsv', 'August 1989. Money can cross the border freely now')
    v.face(R.L1 + .6, .3, 'correcting', lid=.25)
    v.hands(R.L1 + .3, 1, 'point')
    v.to(R.L1 + .3, .35, ease=smooth, bx=-50, by=80, bz=200)
    v.look(R.L1 + 2.9, .5, .1, dur=.12)                                               # Up, to Sidar.
    v.to(R.L1 + 2.9, .3, ease=smooth, hp=0)
    s.look(R.L1 + 1.5, -.5, 0, dur=.2)
    s.to(R.L1 + 1.5, .5, ease=smooth, hp=0, squash=0)

    # ---------------- The stamp: D8.
    for p in (s, v):
        p.look(R.STAMP[1], 0, .5, dur=.2)
        p.look(R.CLIP[3] + .1, 0, 0, dur=.3)
    v.to(R.STAMP[0], .5, ease=smooth, **V_BOOK, bx=10, by=330, bz=0)
    v.hands(R.STAMP[0] + .3, 1, 'relaxed')

    # ---------------- The glint. To the kerb. "If money flows... a token flows too."
    v.look(R.GLINT + .1, -.6, -.5, dur=.1)
    v.face(R.GLINT + .1, .2, 'curious', lid=0, brow=.6)
    v.to(B.V_STEP[0] - .1, .2, loco=1, th=-math.pi / 2 - .3)
    v.to(B.V_STEP[1] - .2, .3, ease=smooth, loco=0, th=-math.pi + .45, hp=-.3, lean=.06)     # Facing upstream.
    v.line(R.L2, 'voices/v2.tsv', 'If money flows, a token flows too')
    s.look(R.GLINT + .5, -.4, -.5, dur=.15)
    s.to(R.GLINT + .5, .5, ease=smooth, hp=-.2)
    s.face(R.GLINT + .6, .3, 'curious', lid=.1, brow=.6)
    v.hands(R.REACH, 1, 'open')
    v.to(R.REACH, .4, ease=smooth, bx=-10, by=190, bz=170, lean=.1)                   # Hand out, palm up, low.
    v.hands(R.HOP[1], 1, 'pinch')
    v.to(R.HOP[1] + .05, .4, ease=smooth, bx=-10, by=40, bz=170, lean=0, hp=0)        # Caught; up to his eyes.
    v.face(R.HOP[1] + .1, .3, 'almost_smile')
    v.look(R.HOP[1] + .1, .1, .3, dur=.1)

    # ---------------- Sidar, himself again: "I taught you where to look."
    s.face(R.HOP[1] + .4, .4, 'smug', lid=.15, brow=.6)
    s.to(R.HOP[1] + .4, .5, ease=smooth, hp=.1, lean=-.05, squash=0)
    s.line(R.L3, 'voices/s3.tsv', 'I taught you where to look')
    s.look(R.L3 - .2, -.4, 0, dur=.1)
    s.hands(R.L3 + .2, 1, 'point')
    s.to(R.L3 + .2, .3, ease=smooth, bx=20, by=90, bz=190)                            # A finger at his own eye.
    s.to(R.L3 + 1.4, .4, ease=smooth, **ARMS_DOWN)
    s.hands(R.L3 + 1.5, 1, 'relaxed')
    v.look(R.L3 + .5, .5, .1, dur=.1)
    v.face(R.L3 + .9, .4, 'unimpressed', lid=.45)

    for k, pup in enumerate((s, v)):
        pup.auto_blink(160 + k, cfg.END, every=(3.0, 5.5))
