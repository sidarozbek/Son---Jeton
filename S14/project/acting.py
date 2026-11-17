"""Son Jeton, scene 14: D5; "I told you so"; the phone rings over Vehbi; the fourth token.
The joke is on Sidar alone: nothing here makes light of the people who lost their savings. Eyes, face, head, body."""
import math

from toonkit.camera import smooth
import blocking as B
import room as R

S_ARM_DOWN = dict(bx=20, by=200, bz=30)


def root(name, t):
    return B.where(name, t)


def direct(cast, cfg):
    s, v = cast['sidar'], cast['vehbi']
    qs = [cast[f'q{i}'] for i in range(len(R.QUEUE_SPOTS))]
    for i, q in enumerate(qs):                                    # The queue, still and quiet, as Scene 13 left them.
        q.face(0, .01, 'rest', lid=.5, brow=.2)
        q.to(0, .01, hp=.12)
        q.look(0, 0, -.2)
    s.face(0, .01, 'rest', lid=.45)
    s.to(0, .01, th=-2.2)                                         # Facing the room and Vehbi, not the board.
    v.face(0, .01, 'rest', lid=.45, brow=.2)

    # ---------------- The stamp. They look up; no flinch this time either.
    for p in (s, v):
        p.look(R.STAMP[1], 0, .5, dur=.2)
        p.look(R.CLIP[3] + .1, 0, 0, dur=.3)

    # ---------------- "I told you so."  Quiet at first; he talks himself into it.
    s.line(B.L1, 'voices/s1.tsv', 'I told you so')
    s.face(B.L1 - .1, .3, 'rest', lid=.4, brow=-.1)
    s.face(B.L1 + .5, .3, 'determined', lid=.25, brow=.2)
    s.to(B.L1 + .5, .3, ease=smooth, hp=-.04, lean=-.02)
    s.look(B.L1 + .2, -.3, 0, dur=.15)

    # ---------------- "You said you built—"  Cut off by the ring.
    v.look(B.L2 - .3, .3, 0, dur=.12)
    v.line(B.L2, 'voices/v2.tsv', 'You said you built')
    v.face(B.L2, .15, 'correcting', lid=.4)
    v.hands(B.L2 + .1, 1, 'point')
    v.to(B.L2 + .1, .2, bx=20, by=130, bz=140)
    v.look(R.RING + .05, -.7, 0, dur=.08)                          # His eyes go to the phone.
    v.to(R.RING + .1, .3, bx=10, by=270, bz=20)
    v.hands(R.RING + .3, 1, 'relaxed')
    s.look(R.RING, -.8, .05, dur=.06)                              # Saved.
    s.face(R.RING + .1, .2, 'smug', lid=.25, brow=.1)

    # ---------------- "Phone's ringing. Come."  Fast, relieved; off to the phone.
    s.line(B.L3, 'voices/s3.tsv', "Phone's ringing. Come")
    s.to(B.S_WALK[0] - .1, .2, loco=1, lean=.05)
    for k in range(13):
        u = k / 12
        s.to(B.S_WALK[0] + (B.S_WALK[1] - B.S_WALK[0]) * u - .05, .12, th=B.path_heading(B.S_PATH, min(max(u, .02), .98)))
    s.to(B.S_WALK[1] - .1, .3, ease=smooth, th=math.pi, loco=0, lean=0)
    v.to(B.V_WALK[0] - .1, .2, loco=1)
    for k in range(13):
        u = k / 12
        v.to(B.V_WALK[0] + (B.V_WALK[1] - B.V_WALK[0]) * u - .05, .12, th=B.path_heading(B.V_PATH, min(max(u, .02), .98)))
    v.to(B.V_WALK[1] - .1, .3, ease=smooth, th=B.heading(B.V_END, B.S_PHONE), loco=0)
    s.hands(R.COIN_IN - .9, 1, 'pinch')
    s.to(R.COIN_IN - .9, .3, bx=-6, by=40, bz=150)
    s.to(R.COIN_IN - .45, .3, bx=-24, by=20, bz=220)
    s.to(R.COIN_IN + .3, .3, **S_ARM_DOWN)
    s.hands(R.COIN_IN + .4, 1, 'relaxed')
    v.face(R.COIN_IN, .3, 'unimpressed', lid=.5)

    for k, pup in enumerate([s, v] + qs):
        pup.auto_blink(70 + k, cfg.END)
