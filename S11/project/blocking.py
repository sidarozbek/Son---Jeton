"""Scene 11 blocking, as pure functions of t. No drawing imports. Kuş Bankerlik, as Scene 10 left it.

Beats:
  0.00  The office; the queue; the board at %90. Coins on the window's counter.
  0.80  The coins turn into birds, one by one, and fly up under the ceiling. The board: %120 (2.6), %150 (6.5);
        the flock grows with it.
  3.00  A bird takes a coin from the newest customer's hand and carries it up the queue to the oldest one.
  3.20  Vehbi, following it with his finger: "Look. New money pays the old customers."  (to 5.76)
  6.20  Sidar, lecturing: "That's called profit."  (to 7.79)   Another bird carries another coin (7.0-8.8).
  8.20  Vehbi: "That's called a chain."  (to 9.27)
  9.90  The stamp: D4. The clipping holds to the end.   End 15.00."""
import math

import room as R

END = R.END
L1, L2, L3 = 3.20, 6.20, 8.20

V_POS = (3.95, 2.35)
S_POS = (4.7, 2.6)
S_TH0 = math.atan2(5.5 - 2.6, 5.2 - 4.7)          # At the board.
V_TH0 = math.atan2(2.6 - 2.35, 4.7 - 3.95) - .3
S_WALK = (99.0, 100.0)
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
