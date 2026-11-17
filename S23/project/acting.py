"""Son Jeton, scene 23: the exam. Vehbi answers in a whisper, writing; each answer is cut against the stamp that
taught it, faster each time. Everyone else: heads down, writing. The proctor stands at the front, still."""
import math

from toonkit.camera import smooth
import blocking as B
import room as R

WRITE = dict(bx=-30, by=230, bz=150)


def root(name, t):
    return B.where(name, t)


def sit(p):
    """Seated: the hips down to the chair seat, the feet forward under the desk, the knees bent by the leg IK."""
    drop = (p.HIP * p.K - R.SEAT_H - .05) / p.K
    fwd = .32 / p.K
    p.to(0, .01, hipdrop=drop, fa=fwd, fb=fwd)


def direct(cast, cfg):
    v = cast['vehbi']
    others = [p for k, p in cast.items() if k.startswith('s')]
    for k, p in enumerate(others):                                  # Heads down, writing; a little life.
        sit(p)
        p.face(0, .01, 'rest', lid=.6)
        p.to(0, .01, hp=-.45, lean=.15, bx=-10, by=160, bz=200, ax=30, ay=170, az=190)   # Hands on the desk.
        p.look(0, 0, -.8)
        for j, tt in enumerate((3.0 + k * .37, 9.0 + k * .29, 14.0 + k * .21, 20.0 + k * .33, 26.0 + k * .27)):
            p.to(tt, .4, ease=smooth, hp=-.3 + .1 * math.sin(k + j), hy=.15 * math.sin(k * 2.1 + j))
        p.auto_blink(200 + k, cfg.END, every=(3.0, 6.0))
    pr = cast['proctor']
    pr.face(0, .01, 'rest', lid=.4)
    pr.to(0, .01, ax=-20, ay=200, az=60, bx=-20, by=200, bz=60)          # Hands folded.
    pr.look(0, -.2, -.3)
    pr.look(8.0, .3, -.3, dur=.6)
    pr.look(13.5, -.4, -.3, dur=.6)
    pr.look(19.0, .2, -.3, dur=.6)
    pr.look(25.5, -.3, -.3, dur=.6)
    pr.auto_blink(230, cfg.END, every=(3.5, 6.5))

    # ---------------- Vehbi: head down, writing; each answer whispered as he writes it, faster each time.
    sit(v)
    v.face(0, .01, 'rest', lid=.45, brow=.2)
    v.to(0, .01, hp=-.4, lean=.12, **WRITE)
    v.hands(0, 1, 'pinch')
    v.pin(1, (R.V_DESK[0] + .05, R.V_DESK[1] - .12, R.DESK_H + .05))             # The writing hand on his sheet.
    v.to(0, .01, bhold=1, ax=60, ay=200, az=150)                                  # The other hand on the desk too.
    v.look(0, 0, -.8)
    v.on_ones(R.L[0], R.PEN_DOWN)
    for k, a in enumerate(R.L):
        name = ["January 24th, 1980", "Bankers' crisis, 81 to 82", "Export tax refunds", "Decision thirty-two, 1989"][k]
        v.line(a, f'voices/v{k + 1}.tsv', name)
        v.face(a - .1, .15, 'determined', lid=.3)
        for j in range(4 + k):                                       # The pen moves: little strokes, quicker each round.
            v.to(a + j * (.4 - .05 * k), .12, bhold=.86 if j % 2 else 1.0)
        v.look(R.Q[k][0] - .2, .1, -.85, dur=.08)                    # Eyes to the next question.
    v.face(R.PEN_DOWN, .3, 'rest', lid=.3, brow=.3)
    v.hands(R.PEN_DOWN, 1, 'relaxed')
    v.to(R.PEN_DOWN, .5, ease=smooth, hp=0, lean=-.04, bhold=0, bx=40, by=230, bz=130, ax=40, ay=230, az=130)   # Pen down; he sits back.
    v.look(R.PEN_DOWN + .3, 0, 0, dur=.3)
    v.face(R.PEN_DOWN + .8, .5, 'almost_smile')
    v.auto_blink(240, cfg.END, every=(3.0, 5.0))
