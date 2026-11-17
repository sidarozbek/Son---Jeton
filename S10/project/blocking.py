"""Scene 10 blocking, as pure functions of t. No drawing imports.

Beats:
  0.00  1982, the office of "Kuş Bankerlik". Three people queue at the teller window. The interest board reads %30.
  1.00  The board flips on its own: %35, %40 (1.90), %45, %50 (2.85)...
  2.00  Sidar, carried away, counting along: "Forty percent! Fifty! Vehbi, look!"  (to 4.70)
  3.00  More people come in at the door and join the queue: 3.00, 4.30, 5.60.
  5.20  Vehbi, quiet, certain: "Nobody can pay that."  (to 6.23)   The board: %60 (5.0), %75 (6.6).
  7.10  Sidar walks straight past the queue to the window and slaps his two tokens on the counter (8.35):
  8.50  "Invest them."  (to 9.37)   The queue turns to look. The board: %90 (9.4).   End 10.80."""
import math

import room as R

END = R.END
L1, L2, L3 = 2.00, 5.20, 8.50

V_POS = (3.95, 2.35)
S_POS = (4.7, 2.6)
S_TH0 = math.atan2(5.5 - 2.6, 5.2 - 4.7)          # At the board.
V_TH0 = math.atan2(2.6 - 2.35, 4.7 - 3.95) - .3
S_WALK = (7.1, 8.2)
S_PATH = [S_POS, (3.85, 4.3), (3.5, 4.95)]
WIN_C = ((R.WINDOW[0] + R.WINDOW[1]) / 2, R.D)
Q_TH0 = [math.atan2(WIN_C[1] - y, WIN_C[0] - x) for x, y in R.QUEUE_SPOTS]


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


def sidar(t):
    return _path(S_PATH, (t - S_WALK[0]) / (S_WALK[1] - S_WALK[0]))


def vehbi(t):
    return V_POS


def queue(i, t):
    spot = R.QUEUE_SPOTS[i]
    t0 = R.ARRIVALS[i]
    if t0 < 0:
        return spot
    return _path([R.DOOR, (spot[0] - .6, spot[1] - .3), spot], (t - t0) / R.WALK_IN)


def heading(a, b):
    return math.atan2(b[1] - a[1], b[0] - a[0])


def where(name, t):
    if name == 'sidar':
        return sidar(t)
    if name == 'vehbi':
        return vehbi(t)
    return queue(int(name[1:]), t)


def pos(name, t, z=0.0):
    x, y = where(name, t)
    return (x, y, z)
