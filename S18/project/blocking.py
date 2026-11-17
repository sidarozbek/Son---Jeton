"""Scene 18 blocking, as pure functions of t. No drawing imports. The customs post; a gangway up to ship A.

Beats:
  0.30  Sidar heads for the gangway. 1.60: "All aboard!"  Up the plank (2.60-3.40) onto the see-through deck; he turns
        to face the quay. Vehbi goes round the counter to stand behind the officer's ledger (1.60-3.40).
  1.00  The officer writes in his ledger; 4.40 he stamps it.
  4.80  Vehbi reads it out: "'One landlord. Export goods. Destination: Germany.'"  (to 11.13)
 11.40  Sidar, delighted, arms wide on the deck: "Germany! Finally, someone appreciates me."  (to 14.63)
 14.70  Nothing moves. The ship doesn't move. Sidar looks about.
 15.70  "...Are we moving?"  (to 16.50)
 17.00  Vehbi, dry: "On paper, you've arrived."  (to 18.92)   End 19.80."""
import math

import room as R

END = R.END
S_PATH = [(-7.6, 1.5), (-6.0, 3.1), (-6.0, 4.97)]
V_PATH = [(-6.1, .7), (-7.3, 2.15), (-8.95, 2.08)]
O_POS = (-9.95, 1.2)
S_DECK = S_PATH[-1]
V_READ = V_PATH[-1]
S_TH0 = math.atan2(3.1 - 1.5, -6.0 + 7.6)
V_TH0 = math.atan2(1.5 - .7, -7.6 + 6.1)


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
    if name == 'sidar':
        return _path(S_PATH, (t - R.S_WALK[0]) / (R.S_WALK[1] - R.S_WALK[0]))
    if name == 'vehbi':
        return _path(V_PATH, (t - R.V_WALK[0]) / (R.V_WALK[1] - R.V_WALK[0]))
    return O_POS


def pos(name, t, z=0.0):
    x, y = where(name, t)
    return (x, y, R.deck_ground(x, y) if name == 'sidar' else z)
