"""Son Jeton, scene 10: Kuş Bankerlik. The board climbs; Sidar is carried away; Vehbi does the arithmetic; Sidar jumps
the queue with his last two tokens. Eyes first, then face, then head, then body."""
import math

from toonkit.camera import smooth
import blocking as B
import room as R

SIDAR_REST = dict(lid=.28, brow=-.25)
V_LID = dict(lid=.48)
S_ARM_DOWN = dict(bx=20, by=200, bz=30)


def root(name, t):
    return B.where(name, t)


def direct(cast, cfg):
    s, v = cast['sidar'], cast['vehbi']
    qs = [cast[f'q{i}'] for i in range(len(R.QUEUE_SPOTS))]

    # ---------------- The queue: patient, facing the window. Late arrivals walk in from the door.
    for i, q in enumerate(qs):
        q.face(0, .01, 'rest', lid=.35)
        t0 = R.ARRIVALS[i]
        if t0 >= 0:
            q.to(t0 - .05, .1, th=B.heading(R.DOOR, R.QUEUE_SPOTS[i]), loco=1)
            q.to(t0 + R.WALK_IN - .3, .3, th=B.Q_TH0[i], loco=0)
        q.look(0, 0, .2)
        q.look(2.0 + i * .4, .3, .35, dur=.3)               # Glances up at the board.
        q.look(3.0 + i * .4, 0, .1, dur=.3)

    # ---------------- Sidar at the board, carried away.
    s.face(0, .01, 'curious', lid=.15, brow=.3)
    s.look(0, 0, .4)
    v.face(0, .01, 'unimpressed')
    v.look(0, .2, .3)
    for t in R.RATE_TIMES[1:5]:
        s.to(t, .08, squash=-.03)
        s.to(t + .1, .2, squash=0)
    s.line(B.L1, 'voices/s1.tsv', 'Forty percent! Fifty! Vehbi, look!')
    s.face(B.L1, .2, 'smug', lid=.05, brow=.5, eye_s=1.15)
    s.hands(B.L1, 1, 'point')
    s.to(B.L1, .2, bx=40, by=60, bz=200, hp=-.1)            # Points up at the board.
    s.to(B.L1 + 1.6, .3, ease=smooth, th=B.heading(B.S_POS, B.V_POS), hp=0)   # "Vehbi, look!"
    s.look(B.L1 + 1.6, 0, 0, dur=.12)
    s.to(B.L1 + 2.4, .3, ease=smooth, **S_ARM_DOWN, th=B.S_TH0)
    s.hands(B.L1 + 2.5, 1, 'relaxed')
    s.look(B.L1 + 2.4, 0, .4, dur=.15)

    # ---------------- "Nobody can pay that."  Quiet, certain. He has done the sum.
    v.look(B.L2 - .4, .3, .35, dur=.12)
    v.look(B.L2 - .1, 0, 0, dur=.12)
    v.line(B.L2, 'voices/v2.tsv', 'Nobody can pay that')
    v.face(B.L2, .2, 'correcting', **V_LID)
    v.face(B.L2 + 1.2, .3, 'unimpressed', lid=.5)

    # ---------------- Sidar jumps the queue with his last two tokens. "Invest them."
    s.hands(B.S_WALK[0] - .3, 1, 'grip')
    s.to(B.S_WALK[0] - .1, .2, th=B.heading(B.S_PATH[0], B.S_PATH[1]), loco=1, lean=.06, bx=10, by=120, bz=120)
    s.to(B.S_WALK[0] + .6, .3, th=B.heading(B.S_PATH[1], B.S_PATH[2]))
    s.to(B.S_WALK[1] - .1, .2, loco=0, lean=0, th=math.pi / 2)
    s.hands(R.TOKENS_DOWN - .2, 1, 'flat')
    s.to(R.TOKENS_DOWN - .15, .15, bx=-20, by=80, bz=150)    # Slaps them down.
    s.to(R.TOKENS_DOWN, .06, squash=.05)
    s.to(R.TOKENS_DOWN + .1, .15, squash=0)
    s.to(R.TOKENS_DOWN + .1, .3, ease=smooth, th=-.2)          # Turns from the window to face the room as he says it.
    s.line(B.L3, 'voices/s3.tsv', 'Invest them')
    s.face(B.L3, .2, 'determined', lid=.2, brow=.2)
    s.to(B.L3 + .9, .4, ease=smooth, **S_ARM_DOWN)
    s.hands(B.L3 + 1.0, 1, 'relaxed')
    v.look(B.S_WALK[0] + .2, .4, .2, dur=.2)
    v.to(B.S_WALK[0] + .4, .5, ease=smooth, th=B.heading(B.V_POS, B.S_PATH[2]))
    v.face(B.L3 + .4, .3, 'one_brow', **V_LID)
    for i, q in enumerate(qs):                                 # The queue turns to look at him.
        q.look(R.TOKENS_DOWN + .1 + .12 * i, .5, .1, dur=.15)
        q.to(R.TOKENS_DOWN + .15 + .12 * i, .3, ease=smooth, hy=.35)
        q.face(R.TOKENS_DOWN + .3 + .12 * i, .3, 'doubt', lid=.25)

    for k, pup in enumerate([s, v] + qs):
        pup.auto_blink(30 + k, cfg.END)
