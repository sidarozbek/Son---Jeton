"""Son Jeton, scene 21: August 1989. "No tokens. The exam's in ten hours." / "They won't believe me here either."
A short, quiet moment of loneliness; the magic is not broken: the river of money keeps flowing. Eyes, face, head, body."""
import math

from toonkit.camera import smooth
import blocking as B
import room as R


def root(name, t):
    return B.where(name, t)


def direct(cast, cfg):
    s, v = cast['sidar'], cast['vehbi']
    s.face(0, .01, 'blank')
    v.face(0, .01, 'blank')
    s.to(0, .01, hp=-.15)
    v.to(0, .01, hp=-.15)                                         # Arriving: both looking down at the flow.
    s.look(0, 0, -.6)
    v.look(0, 0, -.6)

    # ---------------- They take it in. Sidar checks his hands and his pockets: nothing.
    v.look(2.6, .5, -.3, dur=.4)
    v.to(2.6, 1.2, ease=smooth, hy=.4, hp=-.05)                   # Following the notes downstream.
    v.face(2.8, .5, 'curious', lid=.25)
    s.hands(3.0, 1, 'open')
    s.hands(3.0, -1, 'open')
    s.to(3.0, .5, ease=smooth, ax=60, ay=180, az=140, bx=60, by=180, bz=140, hp=-.25)   # Palms up: empty.
    s.look(3.0, 0, -.8, dur=.2)
    s.to(4.0, .5, ease=smooth, ax=10, ay=330, az=0, bx=10, by=330, bz=0, hp=-.05)
    s.hands(4.1, 1, 'relaxed')
    s.hands(4.1, -1, 'relaxed')
    s.face(3.6, .5, 'rest', lid=.45, brow=.3)

    # ---------------- "No tokens. The exam's in ten hours."  Not a reproach: a fact.
    v.look(R.L1 - .3, .6, .1, dur=.15)
    v.to(R.L1 - .3, .4, ease=smooth, hy=.25, hp=0, th=B.heading(B.V_POS, B.S_POS) - .9)
    v.line(R.L1, 'voices/v1.tsv', "No tokens. The exam's in ten hours")
    v.face(R.L1, .3, 'rest', lid=.4, brow=.35)
    s.look(R.L1 + .3, -.5, 0, dur=.15)

    # ---------------- Sidar looks at the river. The anger goes out of him.
    s.look(8.3, .1, -.5, dur=.4)
    s.to(8.3, .8, ease=smooth, hy=0, hp=-.12, lean=.03, squash=.02)
    s.face(8.5, .8, 'rest', lid=.5, brow=.6, ba=.6, smile=-.15)

    # ---------------- "They won't believe me here either."  Quiet.
    s.line(R.L2, 'voices/s2.tsv', "They won't believe me here either")
    s.face(R.L2, .4, 'rest', lid=.45, brow=.55, ba=.65, smile=-.2)
    v.look(R.L2 + .3, .5, 0, dur=.2)
    v.face(R.L2 + .8, .6, 'rest', lid=.3, brow=.5, ba=.4)            # Vehbi has nothing to say to that.

    # ---------------- Nothing. They stand at the edge of it.
    v.look(12.2, 0, -.5, dur=.5)
    v.to(12.0, 1.2, ease=smooth, hy=0, hp=-.1, th=B.V_TH0)
    s.blink(12.8, dur=.25)

    for k, pup in enumerate((s, v)):
        pup.auto_blink(150 + k, cfg.END, every=(3.0, 5.5))
