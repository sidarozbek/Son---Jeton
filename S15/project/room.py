"""Scene 15: an imaginary harbour, mid-1980s, as pure functions of t. No drawing imports.
The quay runs along x. Land (and the cameras) at low y; the quay edge at y 4.0; the sea beyond, 1 m below the quay top.
  y -5.0        the warehouse front ("ANTREPO"), facing the sea
  x -14.0       the harbour office's side wall ("GÜMRÜK"), facing +x
  y -5.0-4.0    the quay, top at z 0
  y  4.0        the quay edge; the sea at z -1.0 out to the far shore at y 95
The ships are see-through: they are not in the Blender set at all. They are drawn over the plate in env.behind, as
translucent paper-pale shapes, and the set hides them where it is nearer (the quay edge, the bollards)."""
import math

QUAY_Y = 4.0
HULL_Y = 4.30                                # Ship A's near side, as it glides along the quay.
WATER_Z = -1.0
SHORE_Y = 95.0
X0, X1 = -40.0, 40.0
WAREHOUSE_Y = -5.0
OFFICE_X = -14.0
BOLLARDS = (-6.5, -2.6, 3.4, 8.2)            # x of each bollard, at y 3.72.
CRANE_X = 12.5

# ---- the ships: length, beam, deck height (above the water), cabin, containers; then where they are at time t.
# A: the one that glides along the quay, right past Vehbi. B and C further out.
SHIPS = (
    dict(L=14.0, B=3.0, deck=2.25, cy=HULL_Y + 1.5, x0=-5.0, v=.9, bob=.025, boxes=3, seed=0),
    dict(L=22.0, B=4.4, deck=3.0, cy=14.0, x0=12.0, v=-.45, bob=.05, boxes=5, seed=1),
    dict(L=26.0, B=5.0, deck=3.3, cy=28.0, x0=-22.0, v=.32, bob=.06, boxes=6, seed=2),
)


def ship_pose(i, t):
    """Centre (x, y, z of the waterline), yaw and roll of ship i at time t. They drift; nothing drives them."""
    s = SHIPS[i]
    x = s['x0'] + s['v'] * t
    z = WATER_Z + s['bob'] * math.sin(t * 1.4 + i * 2.1)
    yaw = 0.0 if s['v'] >= 0 else math.pi
    roll = .012 * math.sin(t * 1.1 + i)
    return (x, s['cy'], z), yaw, roll


# ---- timing
L1, L2, L3 = 2.70, 7.10, 8.60
V_WALK = (4.30, 5.25)             # Vehbi to the quay edge.
REACH = (5.55, 6.15)              # His right hand goes sideways into the hull.
TOUCH = 6.05                      # The moment the fingers meet the hull: ripples.
PULL = (10.40, 10.85)             # The hand comes back out.
END = 13.0

V_HAND = (.62, 4.50, 1.02)        # Where the hand sits, inside the hull of ship A (its near side is at HULL_Y).

STAMP = (99.0, 99.2, 99.4)        # No stamp in this scene.
CLIP = (99.0, 99.2, 99.4, 99.6)
PAGE = (99.0, 99.5)
STAMP_HEAD, STAMP_BODY, STAMP_DATE = '', (), ''


def clip(t):
    return 0.0
