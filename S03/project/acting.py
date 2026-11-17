"""Son Jeton, scene 03: the broken line, the basement, the payphone, the token. Blocking from blocking.py, timing from room.py.
Eyes first, then face, then head, then body."""
import math

from toonkit.camera import smooth
import blocking as B
import room as R

SIDAR_REST = dict(lid=.28, brow=-.25)
V_LID = dict(lid=.48)


def root(name, t):
    return B.vehbi(t) if name == 'vehbi' else B.sidar(t)


def glasses_push(v, t):
    v.hands(t, 1, 'point')
    v.to(t, .14, bx=-34, by=-118, bz=120)
    v.to(t + .3, .22, bx=10, by=270, bz=20)
    v.hands(t + .42, 1, 'relaxed')


def direct(cast, cfg):
    s, v = cast['sidar'], cast['vehbi']
    s_to_v = B.heading(B.S_START, B.V_START)
    v_to_s = B.heading(B.V_START, B.S_START)

    # ---------------- Scene 02's last frame.
    s.face(0, .01, 'determined', **SIDAR_REST)
    s.to(0, .01, th=B.S_TH0, hy=.35)
    s.look(0, .45, .05)
    v.face(0, .01, 'unimpressed')
    v.to(0, .01, th=v_to_s, ax=6, ay=250, az=30)

    # ---------------- "Your phone line is broken."  Grave, official, a repairman's verdict.
    s.look(.15, 0, 0, dur=.15)
    s.to(.2, .35, ease=smooth, th=s_to_v, hy=0)
    s.line(B.L1, 'voices/s1.tsv', 'Your phone line is broken')
    s.face(B.L1 + .1, .25, 'determined', lid=.3, brow=.15)
    s.to(B.L1 + 1.6, .25, hp=.08)                                      # A grave nod on the pause.
    s.to(B.L1 + 2.0, .3, hp=0)
    s.hands(B.L1 + 2.3, 1, 'point')
    s.to(B.L1 + 2.3, .2, bx=10, by=150, bz=150)                        # A finger at him: "is broken".
    s.to(B.L1 + 3.3, .3, bx=20, by=200, bz=30)
    s.hands(B.L1 + 3.4, 1, 'relaxed')

    # ---------------- "I don't have a phone."
    glasses_push(v, B.L2 - .5)
    v.line(B.L2, 'voices/v2.tsv', "I don't have a phone")
    v.face(B.L2, .12, 'correcting', **V_LID)
    v.face(B.L2 + 1.0, .3, 'unimpressed')

    # ---------------- "Downstairs. Come."  As if Vehbi had said nothing. He is walking before the line ends.
    s.line(B.L3, 'voices/s3.tsv', 'Downstairs. Come')
    s.face(B.L3, .1, 'determined', **SIDAR_REST)
    s.hands(B.L3 + .1, 1, 'point')
    s.to(B.L3 + .1, .15, bx=60, by=170, bz=90, hy=-.25)                # A thumb at the door.
    s.to(B.S_EXIT[0] + .5, .2, hy=-.45)                                 # "Come." over his shoulder as he goes.
    s.to(B.S_EXIT[0] - .1, .2, th=B.heading(B.S_START, B.S_DOOR), loco=1, bx=20, by=200, bz=30, hy=0, lean=.08)
    s.hands(B.S_EXIT[0], 1, 'relaxed')
    s.to(B.S_EXIT[0] + .6, .3, th=B.heading(B.S_DOOR, B.S_CORR))
    v.look(B.L3 + .2, .3, 0)
    v.to(B.V_EXIT[0] - .1, .25, th=B.heading(B.V_START, B.V_FOLLOW), loco=1)    # He follows. Book in hand.

    # ---------------- The basement: off the stairs, across to the phone.
    s.to(R.CUT, .01, th=B.heading(B.S_STAIR, B.S_PHONE), loco=1, lean=.06)
    v.to(R.CUT, .01, th=B.heading(B.V_STAIR, B.V_PHONE), loco=0)
    v.to(B.V_WALK[0], .1, loco=1)
    v.look(R.CUT + .3, .2, .4, dur=.3)                                  # The bulb, the pipes: he takes it in. Unimpressed.
    v.look(R.CUT + 1.3, -.2, .1, dur=.3)
    s.to(B.S_WALK[1] - .25, .25, th=B.heading(B.S_PHONE, B.V_PHONE) + .5, loco=0)
    s.to(B.S_WALK[1], .12, lean=-.04, squash=.04)
    s.to(B.S_WALK[1] + .15, .2, lean=0, squash=0)
    v.to(B.V_WALK[1] - .3, .3, th=B.heading(B.V_PHONE, B.S_PHONE), loco=0)
    v.look(B.V_WALK[1], 0, 0, dur=.2)

    # ---------------- He lifts the receiver and holds it out. "It's for you."
    s.look(R.LIFT - .25, -.3, .2, dur=.12)                              # Eyes to the phone first.
    s.hands(R.LIFT - .15, 1, 'grip')
    s.to(R.LIFT - .2, .18, th=B.heading(B.S_PHONE, (R.PHONE_X, R.BY1)), bx=-30, by=60, bz=160)   # Reaches the cradle.
    s.to(R.LIFT + .2, .3, th=B.heading(B.S_PHONE, B.V_PHONE) + .25, bx=-20, by=110, bz=200)  # Holds it out to him.
    s.look(R.LIFT + .25, 0, 0, dur=.1)
    s.line(B.L4, 'voices/s4.tsv', "It's for you")
    s.face(B.L4, .2, 'smug', **SIDAR_REST)
    s.face(B.L4 + .9, .2, 'determined', **SIDAR_REST)
    v.look(B.L4 - .1, .25, -.25, dur=.12)                               # At the receiver. Then at him.
    v.look(B.L4 + .5, 0, 0, dur=.12)
    v.face(B.L4 + .4, .25, 'one_brow', **V_LID)
    v.hands(R.HANDOVER - .1, 1, 'grip')
    v.to(R.HANDOVER - .2, .18, bx=0, by=110, bz=180)                    # Takes it...
    v.to(R.HANDOVER + .15, .35, ease=smooth, bx=46, by=-70, bz=95, hr=.08)   # ...and puts it to his ear, elbow down.
    s.to(R.HANDOVER - .05, .1, bx=20, by=200, bz=30)                    # Lets go.
    s.hands(R.HANDOVER, 1, 'relaxed')

    # ---------------- The token. Shown, and dropped in.
    s.hands(R.COIN_SHOW - .1, 1, 'pinch')
    s.to(R.COIN_SHOW - .1, .2, th=B.heading(B.S_PHONE, (R.PHONE_X + .1, R.BY1)), bx=-6, by=40, bz=150, hp=-.05)
    s.look(R.COIN_SHOW, -.2, .35, dur=.15)
    s.to(R.COIN_IN - .2, .2, bx=-24, by=20, bz=220)                     # Up to the slot.
    s.to(R.COIN_IN + .25, .25, bx=10, by=190, bz=40, hp=0)
    s.hands(R.COIN_IN + .3, 1, 'relaxed')
    s.face(R.COIN_IN + .2, .3, 'smug', **SIDAR_REST)
    v.look(R.COIN_IN - .2, .4, .15, dur=.12)                            # He hears the clink.

    # ---------------- "Hello?"  A first hesitation, no panic.
    v.look(B.L5 - .25, 0, 0, dur=.12)
    v.line(B.L5, 'voices/v5.tsv', 'Hello?')
    v.face(B.L5 - .1, .2, 'unimpressed', lid=.3, eye_s=1.04)
    v.to(B.L5 - .1, .2, hp=.04, hr=.12)

    # ---------------- The line crosses. Sidar's smile is the first one that means something.
    v.look(R.CRACKLE + .05, .1, .3, dur=.1)                             # Eyes to the stuttering bulb.
    v.face(R.CRACKLE + .1, .15, 'unimpressed', lid=.15, eye_s=1.08)
    s.face(R.CRACKLE + .3, .4, 'smug', lid=.18, brow=.1)
    s.to(R.CRACKLE + .3, .4, ease=smooth, hp=.06, lean=-.03)
    v.blink(R.CRACKLE + .9)
    for pup, seed in ((s, 5), (v, 6)):
        pup.auto_blink(seed, cfg.END)
