"""Scene 08 blocking, as pure functions of t. No drawing imports. The grocer's, as Scene 07 left it.

Beats:
  0.00  The hanging cards keep swelling; three giant cards shoot up out of the floor (0.55, 0.95, 1.35). The grocer is squeezed.
  1.60  Sidar: "To the phone! Run!"  (to 3.49)   He runs round the right of the cards to the payphone on the right wall.
  3.40  Vehbi follows, weaving between the giant cards: "Excuse me. Excuse me. Excuse me."  (3.90 to 6.22)
  5.55  A small card flies off the shelf and sticks to Sidar's nose.
  6.60  Sidar, muffled by it: "Token two."  (to 7.63)   The token into the slot at 7.75; the line crosses at 8.05.
  8.40  The stamp comes down: D2. The clipping holds to the end.   End 13.40."""
import math

import room as R

END = R.END
L1, L2, L3 = 1.60, 3.90, 6.60

V_POS = (1.6, 2.3)
S_POS = (3.4, 2.35)
G_POS = (1.95, 4.4)
S_TH0 = math.pi + .3            # Facing Vehbi, opened a little to the front.
V_TH0 = -.3
G_TH0 = -math.pi / 2 + .25      # Facing his customers.
G_BACK = math.pi / 2            # Facing the shelves.


S_PHONE = (4.4, 1.1)
V_PHONE = (3.85, 1.6)
S_RUN = (2.6, 4.4)
V_RUN = (3.4, 6.5)
S_PATH = [S_POS, (4.0, 2.3), (4.4, 1.6), S_PHONE]
V_PATH = [V_POS, (1.7, 1.45), (2.6, 1.65), (3.65, 1.65), V_PHONE]


def _ease(u):
    u = min(max(u, 0.0), 1.0)
    return u * u * (3 - 2 * u)


def _path(pts, u):
    segs = [math.hypot(b[0] - a[0], b[1] - a[1]) for a, b in zip(pts, pts[1:])]
    d = min(max(u, 0.0), 1.0) * sum(segs)
    for (a, b), L in zip(zip(pts, pts[1:]), segs):
        if d <= L:
            k = d / L if L else 0
            return (a[0] + (b[0] - a[0]) * k, a[1] + (b[1] - a[1]) * k)
        d -= L
    return pts[-1]


def path_heading(pts, u, du=.01):
    a, b = _path(pts, max(u - du, 0)), _path(pts, min(u + du, 1))
    return math.atan2(b[1] - a[1], b[0] - a[0])


def s_u(t):
    return (t - S_RUN[0]) / (S_RUN[1] - S_RUN[0])


def v_u(t):
    return (t - V_RUN[0]) / (V_RUN[1] - V_RUN[0])


def sidar(t):
    return _path(S_PATH, s_u(t))


def vehbi(t):
    return _path(V_PATH, v_u(t))


def grocer(t):
    return G_POS


def heading(a, b):
    return math.atan2(b[1] - a[1], b[0] - a[0])


def pos(name, t, z=0.0):
    x, y = {'vehbi': vehbi, 'sidar': sidar, 'grocer': grocer}[name](t)
    return (x, y, z)
