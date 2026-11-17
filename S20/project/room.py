"""Scene 20: the same harbour, at a payphone on the harbour office's wall. Token five turns see-through; the line
crackles; the picture folds away like paper.
Scene 19: as Scene 18, Sidar still on the deck. Stamp D7. The containers open; invoices rain out of them.
Scene 18: the customs post again. A gangway up to ship A; Sidar goes aboard; the officer writes him in the ledger.
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

# ---- Scene 20: a payphone on the harbour office's side wall (Scene 03's design), facing the quay.
PHONE = (OFFICE_X + .06, .2, 1.05)
SLOT20 = (OFFICE_X + .09, .29, 1.49)

# ---- timing
L1, L2, L3 = .80, 4.30, 6.10                    # Sidar, Vehbi, Sidar.
TOKEN_UP = .55                                  # Token five, held up between them.
SEE = (2.90, 4.00)                              # It turns see-through: only on paper.
COIN_IN = 7.25                                  # He pushes it into the slot anyway; it is gone by 7.6.
CRACKLE = 7.95                                  # "tok—": the line crackles...
FOLD = (8.90, 12.40)                            # ...and the harbour folds away like paper, with them in it.
END = 13.00
LIDS = (-9.0, -8.8, -8.6)                       # Scene 19's containers: open.
BURST = -40.0                                   # Scene 19's invoices: all landed long ago.
N_SHEETS = 72
CATCH = (-99.0, -98.0)
WRITE = (-9.0, -8.0)
STAMP_L = -5.0


def see(t):
    """How see-through token five is: 0 solid, 1 almost gone."""
    u = min(max((t - SEE[0]) / (SEE[1] - SEE[0]), 0.0), 1.0)
    return u * u * (3 - 2 * u)


def fold(t):
    return min(max((t - FOLD[0]) / (FOLD[1] - FOLD[0]), 0.0), 1.0)


def crackle(t):
    """0-1: how hard the line is crackling the picture."""
    if t < CRACKLE:
        return 0.0
    return min((t - CRACKLE) / (FOLD[0] - CRACKLE), 1.0)


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


def lid(k, t):
    """How far container k's lid has swung open, in radians."""
    u = min(max((t - LIDS[k]) / .25, 0.0), 1.0)
    return 1.95 * (u * u * (3 - 2 * u)) + (.12 * math.sin((t - LIDS[k]) * 14) * math.exp(-(t - LIDS[k]) * 4) if t > LIDS[k] + .25 else 0)


def clip(t):
    return 0.0


# ---- the invoices: each one shot up out of a container, then fluttering down; they stay where they land (in the water
# they sink). Pure functions of t, seeded, so every frame agrees.
SHIP_A = (-7.0, 6.0)
BOX_X = (-8.8, -7.35, -5.9)                     # Container centres along ship A (world x), on its deck; tops at z 1.75.
BOX_TOP = 1.75
_rng = __import__('random').Random(19)
SHEETS = []
for _j in range(N_SHEETS):
    _c = _j % 3
    SHEETS.append(dict(c=_c, x=BOX_X[_c] + _rng.uniform(-.5, .5), y=SHIP_A[1] + _rng.uniform(-.5, .5),
                       t0=BURST + _c * .12 + _rng.uniform(0, 1.0), vx=_rng.uniform(-1.3, 1.3), vy=_rng.uniform(-1.9, .5),
                       vz=_rng.uniform(3.0, 5.5), ph=_rng.uniform(0, 6.28), w=_rng.uniform(4, 7)))
SHEETS[0].update(c=2, x=BOX_X[2], y=SHIP_A[1] - .3, t0=BURST + .3, vx=-.1, vy=-.9, vz=3.4)   # The one Sidar catches.
FALL = .7


def surface(x, y):
    if y < QUAY_Y:
        return .005
    if -12.5 <= x <= -1.5 and 4.62 <= y <= 7.38:
        return DECK_Z + .005
    return WATER_Z


def sheet(j, t):
    """(position, yaw, tilt, landed) of invoice j at time t, or None before it bursts out or once it has sunk."""
    s = SHEETS[j]
    a = t - s['t0']
    if a < 0:
        return None
    g = 9.8
    tb = (s['vz'] + FALL) / g                                   # Ballistic until it is falling at FALL m/s...
    if a <= tb:
        x, y = s['x'] + s['vx'] * a, s['y'] + s['vy'] * a
        z = BOX_TOP + s['vz'] * a - g * a * a / 2
    else:                                                       # ...then it flutters down, drifting and swaying.
        xb, yb = s['x'] + s['vx'] * tb, s['y'] + s['vy'] * tb
        zb = BOX_TOP + s['vz'] * tb - g * tb * tb / 2
        d = a - tb
        k = 1 - math.exp(-d * 1.5)
        x = xb + s['vx'] * .6 * k + .35 * math.sin(d * s['w'] * .5 + s['ph'])
        y = yb + s['vy'] * .6 * k
        z = zb - FALL * d
        floor = surface(x, y)
        if z <= floor:                                          # Landed: work out when, and hold there.
            t_land = (zb - floor) / FALL
            if floor <= WATER_Z + .01:
                if d - t_land > .5:
                    return None
                return (x, y, floor - (d - t_land) * .1), s['ph'], 0.0, True
            dl = t_land
            kl = 1 - math.exp(-dl * 1.5)
            x = xb + s['vx'] * .6 * kl + .35 * math.sin(dl * s['w'] * .5 + s['ph'])
            y = yb + s['vy'] * .6 * kl
            return (x, y, floor), s['ph'] + dl * 1.5, 0.0, True
    return (x, y, z), s['ph'] + a * 1.5, .9 * math.sin(a * s['w'] + s['ph']), False
