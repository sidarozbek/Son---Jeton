"""Scene 14 blocking, as pure functions of t. No drawing imports. Kuş Bankerlik after the fall: shutter down, board dark,
the sign on the floor, the queue still standing.

Beats:
  0.50  The stamp comes down: D5. The clipping holds to 5.20, back by 5.55.
  6.10  Sidar, quiet at first, then talking himself into it: "I told you so."  (to 7.11)
  7.60  Vehbi: "You said you built—"  The payphone on the left wall rings over him (8.45); the line crackles.
  9.10  Sidar, fast, relieved: "Phone's ringing. Come."  (to 11.19)   Round the front of the queue to the phone; Vehbi follows.
 12.90  The fourth token into the slot.   End 14.20."""
import math

import room as R

END = R.END
V_POS = (3.95, 2.35)
S_POS = (4.7, 2.6)
S_TH0 = math.atan2(5.5 - 2.6, 5.2 - 4.7)
V_TH0 = math.atan2(2.6 - 2.35, 4.7 - 3.95) - .3
WIN_C = ((R.WINDOW[0] + R.WINDOW[1]) / 2, R.D)
Q_TH0 = [math.atan2(WIN_C[1] - y, WIN_C[0] - x) for x, y in R.QUEUE_SPOTS]


L1, L2, L3 = 6.10, 7.60, 9.10
S_WALK = (9.6, 12.2)
V_WALK = (10.0, 12.8)
S_PATH = [(4.7, 2.6), (3.3, 1.3), (1.7, 1.35), (.95, 3.0), (.55, 4.25)]     # Round the front of the queue.
V_PATH = [(3.95, 2.35), (3.0, 1.2), (1.75, 1.15), (1.15, 3.75)]
S_PHONE = (.55, 4.25)
V_END = (1.15, 3.75)


def _ease(u):
    u = min(max(u, 0.0), 1.0)
    return u * u * (3 - 2 * u)


def _lerp(a, b, u):
    return (a[0] + (b[0] - a[0]) * u, a[1] + (b[1] - a[1]) * u)


def _path(pts, u):
    segs = [math.hypot(b[0] - a[0], b[1] - a[1]) for a, b in zip(pts, pts[1:])]
    d = _ease(u) * sum(segs)
    for (a, b), L in zip(zip(pts, pts[1:]), segs):
        if d <= L:
            return _lerp(a, b, d / L if L else 0)
        d -= L
    return pts[-1]


def path_heading(pts, u, du=.01):
    a, b = _path(pts, max(u - du, 0)), _path(pts, min(u + du, 1))
    return math.atan2(b[1] - a[1], b[0] - a[0])


def sidar(t):
    return _path(S_PATH, (t - S_WALK[0]) / (S_WALK[1] - S_WALK[0]))


def vehbi(t):
    return _path(V_PATH, (t - V_WALK[0]) / (V_WALK[1] - V_WALK[0]))


def queue(i, t):
    return R.QUEUE_SPOTS[i]


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
