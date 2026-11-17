"""Scene 18: the customs post again. A gangway up to ship A; Sidar goes aboard; the officer writes him in the ledger.
Scene 17: the customs post from Scene 16, a moment later: two paper ships afloat, a tiny one still peeking out of
the drawer. Stamp D6.
Scene 16: the harbour from Scene 15, by the harbour office, as pure functions of t. No drawing imports.
The quay runs along x. Land (and the cameras) at low y; the quay edge at y 4.0; the sea beyond, 1 m below the quay top.
  y -5.0        the warehouse front ("ANTREPO"), facing the sea
  x -14.0       the harbour office's side wall ("GÜMRÜK"), facing +x
  x -9.0        the customs officer's desk, out on the quay; the filing cabinet beside it, drawers facing +x
The ships are see-through and drawn in env.behind. New ones come out of the filing cabinet's top drawer: a tiny folded
paper ship rises out, then grows as it hops over the quay edge into the water, full size."""
import math

QUAY_Y = 4.0
HULL_Y = 4.30
WATER_Z = -1.0
SHORE_Y = 95.0
X0, X1 = -40.0, 40.0
WAREHOUSE_Y = -5.0
OFFICE_X = -14.0
BOLLARDS = (-6.5, -2.6, 3.4, 8.2)
CRANE_X = 12.5

# ---- the customs post
DESK = (-9.0, 1.2, .95, 1.4, .8)              # A standing counter: centre x, y; height; size along x, y.
PAPER = (-9.45, 1.0, .955)                   # The form on the desk, where the stamp comes down.
CAB = (-9.9, 2.4, .6, .5, 1.3)                # Filing cabinet: centre x, y; depth (x), width (y), height. Drawers face +x.
DRAWER_Z = (.92, 1.22)                        # The top drawer's front, bottom and top.
DRAWER_OUT = .38
DRAWER_MOUTH = (CAB[0] + CAB[2] / 2 + DRAWER_OUT - .19, CAB[1], DRAWER_Z[1] - .05)   # Where a ship comes up out of it.

# ---- timing
STAMPS = (-3.0, -2.0, -1.0)                   # Scene 16's stamps, done: the drawer is open, the tiny ship peeking.
LEDGER = (-9.4, 1.15, .955)                   # The officer's ledger, open on the counter.
GANGWAY = (-6.0, .6, 3.55, 4.85)              # A plank from the quay up to ship A's deck: x centre, width, y0, y1.
DECK_Z = 1.0                                  # Ship A's deck: 2.0 m above the water, 1.0 m above the quay.
DECK = (-11.5, -2.5, 4.62, 7.38)              # Where you can stand on it: x0, x1, y0, y1.

# ---- timing
L1, L2, L3, L4, L5 = 1.60, 4.80, 11.40, 15.70, 17.00
S_WALK = (.30, 3.40)                          # Sidar to the gangway and up it.
V_WALK = (1.60, 3.40)                         # Vehbi round the counter to read the ledger.
WRITE = (1.00, 4.10)                          # The officer writes in the ledger...
STAMP_L = 4.40                                # ...and stamps it.
END = 19.80


def drawer(t):
    """How far the top drawer is out, 0-1: it opens after each stamp and shuts once the ship is out."""
    out = 0.0
    for s in STAMPS:
        a, b = s + .3, s + 1.45
        if t < a:
            continue
        if t < a + .2:
            out = max(out, (t - a) / .2)
        elif t < b:
            out = 1.0
        elif t < b + .25:
            out = max(out, 1 - (t - b) / .25)
    if t >= STAMPS[2] + .3:                   # The last one stays open: the ship is still peeking out at the end.
        out = min(max((t - STAMPS[2] - .3) / .2, 0.0), 1.0)
    return out


# ---- the ships. Born from the drawer (born=stamp index) or already at sea (born=None, drifting).
SHIPS = (
    dict(L=11.0, B=2.8, deck=2.0, boxes=3, born=None, to=(-7.0, 6.0), yaw=0.0, v=0.0, bob=0.0),
    dict(L=12.0, B=3.0, deck=2.1, boxes=3, born=None, to=(1.8, 11.2), yaw=.15, v=.35, bob=.04),
    dict(L=11.0, B=2.8, deck=2.0, boxes=3, born=2, to=None, yaw=0.0, v=0.0, bob=0.0),
    dict(L=22.0, B=4.4, deck=3.0, boxes=5, born=None, to=(4.0, 16.0), yaw=math.pi, v=-.45, bob=.05),
    dict(L=26.0, B=5.0, deck=3.3, boxes=6, born=None, to=(-30.0, 30.0), yaw=0.0, v=.32, bob=.06),
)
RISE, FLY = (.55, 1.0), (1.0, 3.0)            # After its stamp: up out of the drawer; then the hop to the water.
TINY = .035


def _ease(u):
    u = min(max(u, 0.0), 1.0)
    return u * u * (3 - 2 * u)


def ship_state(i, t):
    """(centre of the waterline (x, y, z), yaw, roll, scale), or None while it doesn't exist yet."""
    s = SHIPS[i]
    bobz = s['bob'] * math.sin(t * 1.4 + i * 2.1)
    roll = .012 * math.sin(t * 1.1 + i)
    if s['born'] is None:
        x0, y0 = s['to']
        return (x0 + math.cos(s['yaw']) * abs(s['v']) * t, y0, WATER_Z + bobz), s['yaw'], roll, 1.0
    ts = STAMPS[s['born']]
    a = t - ts
    if a < RISE[0]:
        return None
    mouth = DRAWER_MOUTH
    if a < RISE[1]:                                            # Up out of the drawer, unfolding.
        u = _ease((a - RISE[0]) / (RISE[1] - RISE[0]))
        wob = .15 * math.sin(a * 9) * (1 - u)
        return (mouth[0], mouth[1], mouth[2] + .06 * u), s['yaw'] + wob, 0.0, TINY * (.4 + .6 * u)
    if s['to'] is None:                                        # The last one: stays peeking, bobbing on the paper.
        return (mouth[0], mouth[1], mouth[2] + .06 + .01 * math.sin(a * 5)), .2 * math.sin(a * 2), 0.0, TINY
    tx, ty = s['to']
    if a < FLY[1]:                                             # The hop: over the quay edge, growing as it goes.
        u = (a - FLY[0]) / (FLY[1] - FLY[0])
        e = _ease(u)
        x = mouth[0] + (tx - mouth[0]) * e
        y = mouth[1] + (ty - mouth[1]) * e
        z = (mouth[2] + .06) + (WATER_Z - mouth[2] - .06) * e + 1.8 * math.sin(math.pi * u)
        sc = TINY + (1 - TINY) * _ease(u * 1.15) ** 1.6
        return (x, y, z), s['yaw'] + 1.2 * math.sin(math.pi * u) * (1 - u), .1 * math.sin(math.pi * u * 2), min(sc, 1.0)
    drift = s['v'] * (a - FLY[1])                              # Afloat; the second one sails off slowly.
    return (tx + math.cos(s['yaw']) * drift, ty + math.sin(s['yaw']) * drift, WATER_Z + bobz), s['yaw'], roll, 1.0


def landed(i):
    s = SHIPS[i]
    return STAMPS[s['born']] + FLY[1]


STAMP = (99.0, 99.2, 99.4)        # No "Sınavda çıkar" stamp in this scene.
CLIP = (99.0, 99.2, 99.4, 99.6)
PAGE = (99.0, 99.5)
STAMP_HEAD, STAMP_BODY, STAMP_DATE = '', (), ''


def deck_ground(x, y):
    """Where Sidar walks: the quay at 0, up the gangway, then ship A's deck."""
    gx, gw, y0, y1 = GANGWAY
    if abs(x - gx) <= gw / 2 + .15 and y0 <= y <= y1:
        return DECK_Z * (y - y0) / (y1 - y0)
    if DECK[0] <= x <= DECK[1] and y1 < y <= DECK[3]:
        return DECK_Z
    return 0.0


def clip(t):
    a, b, c, d = CLIP
    if t <= a or t >= d:
        return 0.0
    if t < b:
        u = (t - a) / (b - a)
    elif t > c:
        u = 1 - (t - c) / (d - c)
    else:
        return 1.0
    return u * u * (3 - 2 * u)
