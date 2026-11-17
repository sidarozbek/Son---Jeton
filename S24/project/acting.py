"""Son Jeton, scene 24: "Where were you last night?" / "...I don't know." The first time he has said it. Black.
Eyes, face, head, body."""
import math

from toonkit.camera import smooth
import blocking as B
import room as R


def root(name, t):
    return B.where(name, t)


def walk(p, path, a, b):
    p.to(a - .1, .2, loco=1)
    for k in range(13):
        u = k / 12
        p.to(a + (b - a) * u - .05, .12, th=B.path_heading(path, min(max(u, .02), .98)))
    p.to(b - .1, .3, ease=smooth, loco=0)


def direct(cast, cfg):
    v, f = cast['vehbi'], cast['friend']
    for i in range(len(B.OTHERS)):                                  # Two students walking off towards the window.
        o = cast[f'o{i}']
        o.face(0, .01, 'rest', lid=.4)
        o.to(0, .01, loco=1, th=math.pi / 2)
        o.to(B.O_WALK[1] - .2, .3, loco=0)
        o.auto_blink(300 + i, cfg.END)

    # ---------------- Vehbi out of the door, the book back in his hand. Done; light on his feet.
    v.face(0, .01, 'almost_smile')
    walk(v, B.V_PATH, B.V_WALK[0], B.V_WALK[1])
    v.look(1.0, 0, 0)

    # ---------------- The friend falls in beside him. Easy, friendly.
    f.face(0, .01, 'rest', lid=.3, brow=.2)
    walk(f, B.F_PATH, B.F_WALK[0], B.F_WALK[1])
    f.look(R.L1 - .3, -.6, 0, dur=.12)
    f.to(B.F_WALK[1] - .1, .5, ease=smooth, th=B.heading(B.F_PATH[-1], B.V_PATH[-1]))   # Turns back to him.
    f.line(R.L1, 'voices/f1.tsv', 'Where were you last night')
    f.face(R.L1, .3, 'curious', lid=.2)
    v.look(R.L1 + .3, .5, 0, dur=.15)

    # ---------------- He stops. He thinks. He looks away, at nothing.
    v.face(R.STOP, .4, 'rest', lid=.2, brow=.5)
    v.look(R.STOP + .5, -.5, .2, dur=.5)
    v.to(R.STOP + .4, .8, ease=smooth, hy=-.35, hp=.08)
    v.blink(R.STOP + 1.1, dur=.2)
    v.look(R.L2 - .3, .1, 0, dur=.3)
    v.to(R.L2 - .3, .6, ease=smooth, hy=.1, hp=0)

    # ---------------- "...I don't know."
    v.line(R.L2, 'voices/v2.tsv', "I don't know")
    v.face(R.L2 + .2, .8, 'almost_smile', lid=.3, brow=.4)
    f.face(R.L2 + .5, .6, 'one_brow')

    for k, pup in enumerate((v, f)):
        pup.auto_blink(310 + k, cfg.END, every=(3.0, 5.0))
