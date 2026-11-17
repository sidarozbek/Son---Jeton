"""Scene 24 blocking, as pure functions of t. No drawing imports. The corridor after the exam.

Beats:
  0.00  The corridor. Two students walk off towards the window. The exam hall's door.
  0.50  Vehbi comes out of the door, the book back in his hand, and walks towards us down the corridor.
  1.20  His friend, waiting by the wall, falls in beside him.
  3.00  The friend, easy: "Where were you last night?"  (to 4.18)
  4.30  Vehbi stops. He thinks. He looks away, at nothing.
  5.90  "...I don't know."  (to 6.48)  For the first time.
  8.40  Black.   End 11.00."""
import math

import room as R

END = R.END
V_PATH = [(.35, 9.2), (1.05, 8.6), (1.1, 5.4)]
V_WALK = (.5, 4.3)
F_PATH = [(2.4, 8.2), (1.95, 7.6), (1.95, 5.6)]
F_WALK = (1.2, 4.1)
OTHERS = [((1.0, 7.2), (1.2, 13.0)), ((1.9, 7.8), (2.0, 13.4))]
O_WALK = (0.0, 5.5)
V_TH0 = math.atan2(8.6 - 9.2, 1.05 - .35)
F_TH0 = -math.pi / 2 - .4


def _ease(u):
    u = min(max(u, 0.0), 1.0)
    return u * u * (3 - 2 * u)


def _path(pts, u):
    segs = [math.hypot(b[0] - a[0], b[1] - a[1]) for a, b in zip(pts, pts[1:])]
    d = _ease(u) * sum(segs)
    for (a, b), L in zip(zip(pts, pts[1:]), segs):
        if d <= L:
            k = d / L if L else 0
            return (a[0] + (b[0] - a[0]) * k, a[1] + (b[1] - a[1]) * k)
        d -= L
    return pts[-1]


def path_heading(pts, u, du=.01):
    a, b = _path(pts, max(u - du, 0)), _path(pts, min(u + du, 1))
    return math.atan2(b[1] - a[1], b[0] - a[0])


def heading(a, b):
    return math.atan2(b[1] - a[1], b[0] - a[0])


def where(name, t):
    if name == 'vehbi':
        return _path(V_PATH, (t - V_WALK[0]) / (V_WALK[1] - V_WALK[0]))
    if name == 'friend':
        return _path(F_PATH, (t - F_WALK[0]) / (F_WALK[1] - F_WALK[0]))
    a, b = OTHERS[int(name[1:])]
    u = min(max((t - O_WALK[0]) / (O_WALK[1] - O_WALK[0]), 0.0), 1.0)
    return (a[0] + (b[0] - a[0]) * u, a[1] + (b[1] - a[1]) * u)


def pos(name, t, z=0.0):
    x, y = where(name, t)
    return (x, y, z)
