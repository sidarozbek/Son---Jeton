"""Son Jeton, scene 18: "All aboard!"; the officer writes Sidar in his ledger as export goods; "Germany! Finally,
someone appreciates me."; nothing moves; "...Are we moving?" / "On paper, you've arrived." Eyes, face, head, body."""
import math

from toonkit.camera import smooth
import blocking as B
import room as R

ARMS_DOWN = dict(ax=10, ay=330, az=0, bx=10, by=330, bz=0)
V_BOOK = dict(ax=6, ay=250, az=30)


def root(name, t):
    return B.where(name, t)


def walk(p, path, a, b):
    p.to(a - .1, .2, loco=1)
    for k in range(13):
        u = k / 12
        p.to(a + (b - a) * u - .05, .12, th=B.path_heading(path, min(max(u, .02), .98)))
    p.to(b - .1, .3, ease=smooth, loco=0)


def direct(cast, cfg):
    s, v, o = cast['sidar'], cast['vehbi'], cast['officer']
    s.face(0, .01, 'determined', lid=.2, brow=.3)
    v.face(0, .01, 'unimpressed', lid=.4)
    o.face(0, .01, 'rest', lid=.6, brow=-.2)
    o.to(0, .01, hp=-.4, lean=.12, ax=60, ay=260, az=120, bx=40, by=230, bz=150)
    o.hands(0, 1, 'pinch')

    # ---------------- "All aboard!"  Off to the gangway, an arm up, and up the plank.
    walk(s, B.S_PATH, R.S_WALK[0], R.S_WALK[1])
    s.line(R.L1, 'voices/s1.tsv', 'All aboard')
    s.hands(R.L1 - .2, 1, 'point')
    s.to(R.L1 - .2, .25, bx=30, by=-60, bz=120)                                      # An arm up, pointing at the sky.
    s.look(R.L1 - .3, .5, .1, dur=.1)
    s.to(R.L1 + .9, .4, ease=smooth, bx=10, by=330, bz=0)
    s.hands(R.L1 + 1.0, 1, 'relaxed')
    s.to(R.S_WALK[1] + .1, .5, ease=smooth, th=-math.pi / 2 + .25)                  # On deck: he turns to face the quay.
    s.face(R.S_WALK[1] + .2, .3, 'smug', lid=.2, brow=.4)
    s.to(R.S_WALK[1] + .3, .4, ease=smooth, lean=-.05, hp=.1)                        # Chin up: cargo of quality.

    # ---------------- The officer writes, then stamps the entry. He never looks up.
    o.pin(1, (R.LEDGER[0] - .05, R.LEDGER[1] - .15, R.LEDGER[2] + .06))
    o.to(R.WRITE[0] - .3, .3, ease=smooth, bhold=.95)
    for k in range(int((R.WRITE[1] - R.WRITE[0]) / .25)):                            # Scribbling.
        o.to(R.WRITE[0] + k * .25, .12, bhold=.9 if k % 2 else 1.0)
    o.to(R.STAMP_L - .5, .25, ease=smooth, bhold=0, bx=40, by=120, bz=170)
    o.pin(1, (R.LEDGER[0] - .1, R.LEDGER[1] - .12, R.LEDGER[2] + .09))
    o.to(R.STAMP_L - .08, .08, bhold=1)
    o.on_ones(R.STAMP_L - .1, R.STAMP_L + .15)
    o.to(R.STAMP_L + .3, .3, ease=smooth, bhold=0, bx=40, by=230, bz=150)

    # ---------------- Vehbi round the counter to the ledger; he reads it out.
    walk(v, B.V_PATH, R.V_WALK[0], R.V_WALK[1])
    v.to(R.V_WALK[1], .4, ease=smooth, th=B.heading(B.V_READ, R.LEDGER[:2]), hp=-.35)
    v.look(R.V_WALK[1], 0, -.7, dur=.15)
    v.face(R.V_WALK[1], .3, 'correcting', lid=.4)
    v.line(R.L2, 'voices/v2.tsv', 'One landlord. Export goods. Destination: Germany')
    v.to(R.L2 + .2, .5, ease=smooth, lean=.06)
    v.look(R.L2 + 1.6, -.2, -.75, dur=.3)                                              # His eyes run along the line.
    v.look(R.L2 + 3.4, .2, -.75, dur=.3)
    v.look(R.L2 + 4.9, -.1, -.7, dur=.3)
    s.look(R.L2 + .4, -.4, -.1, dur=.1)
    s.face(R.L2 + 2.8, .3, 'curious', lid=.1, brow=.6)                                 # "Destination..."

    # ---------------- "Germany! Finally, someone appreciates me."  Arms wide on the deck.
    s.line(R.L3, 'voices/s3.tsv', 'Germany! Finally, someone appreciates me')
    s.face(R.L3 - .05, .2, 'try_smile')
    s.to(R.L3, .3, ease=smooth, ax=260, ay=90, az=80, bx=260, by=90, bz=80, lean=-.08, hp=.15)
    s.hands(R.L3, 1, 'open')
    s.hands(R.L3, -1, 'open')
    s.face(R.L3 + 1.0, .3, 'smug', lid=.1, brow=.6)
    s.to(R.L3 + 2.4, .5, ease=smooth, ax=-20, ay=200, az=60, bx=-20, by=200, bz=60, lean=0, hp=.08)   # Hands to his chest.
    v.to(R.L3 + .3, .4, ease=smooth, hp=0, lean=0, th=B.heading(B.V_READ, B.S_DECK))
    v.look(R.L3 + .3, .2, .15, dur=.1)
    v.face(R.L3 + .5, .3, 'unimpressed', lid=.45)

    # ---------------- Nothing moves. He waits for the ship to leave. It doesn't.
    s.to(14.7, .5, ease=smooth, **ARMS_DOWN)
    s.hands(14.8, 1, 'relaxed')
    s.hands(14.8, -1, 'relaxed')
    s.face(14.8, .4, 'rest', lid=.2, brow=.4)
    s.look(14.9, -.7, 0, dur=.1)
    s.to(14.9, .4, ease=smooth, hy=-.5, hp=0)
    s.look(15.3, .7, 0, dur=.1)
    s.to(15.3, .4, ease=smooth, hy=.5)
    s.to(15.65, .3, ease=smooth, hy=0, hp=-.1)                                          # Down at the deck.
    s.line(R.L4, 'voices/s4.tsv', 'Are we moving')
    s.face(R.L4 - .05, .3, 'doubt')
    s.look(R.L4 + .4, .2, .2, dur=.1)
    s.to(R.L4 + .4, .4, ease=smooth, hp=.08, hy=.15)                                     # To Vehbi.

    # ---------------- "On paper, you've arrived."
    v.line(R.L5, 'voices/v5.tsv', "On paper, you've arrived")
    v.face(R.L5 - .1, .3, 'slow_lid')
    v.to(R.L5 + .3, .3, ease=smooth, hp=-.05)
    s.face(R.L5 + 1.2, .4, 'bluff')

    for k, pup in enumerate((s, v, o)):
        pup.auto_blink(120 + k, cfg.END)
