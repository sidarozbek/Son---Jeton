"""Scene 12 blocking, as pure functions of t. No drawing imports. Kuş Bankerlik; the queue has stepped back to watch.

Beats:
  0.00  A chalkboard on an easel: bars of new customers needed, doubling every month; a dashed line, "herkes".
  0.80  Vehbi at the board: "Every month needs more new customers than the last. Here, it runs out."  (to 6.27)
        He taps the X where the bars cross the line at 5.0.
  6.70  Sidar, hands spread at the office: "I built this place. With my own hands."  (to 9.65)
  9.00  Vehbi goes to the teller window: two tokens are wedged in the slot. He grabs them (10.35).
 10.50  Tugging already: "Then help me pull."  (to 11.59)   Sidar grabs on behind him (12.0); they tug together.
 13.00  "Hmph."  (to 13.53)   POP at 13.25: the tokens fly out; both stagger back; Sidar catches them (13.75).
        End 15.00."""
import math

import room as R

END = R.END
L1, L2, L3, L4 = 0.80, 6.70, 10.50, 13.00

V_POS = (3.85, 3.5)
S_POS = (3.35, 2.75)
S_TH0 = math.atan2(3.5 - 2.75, 3.85 - 3.35) - .4   # At Vehbi and the board.
V_TH0 = -.6                                        # Half to the board, half to us.
S_WALK = (11.0, 12.0)
S_PATH = [S_POS, (2.95, 4.2), (2.95, 4.62)]
V_WALK = (9.0, 10.3)
V_PATH = [V_POS, (3.2, 4.4), (3.05, 4.98)]
BACK = .35                                          # How far each staggers back at the pop.
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


def _stagger(p, t, k=1.0):
    if t < R.POP:
        return p
    u = min((t - R.POP) / .35, 1.0)
    e = u * (2 - u)
    return (p[0], p[1] - BACK * k * e)


def sidar(t):
    return _stagger(_path(S_PATH, (t - S_WALK[0]) / (S_WALK[1] - S_WALK[0])), t, 1.2)


def vehbi(t):
    return _stagger(_path(V_PATH, (t - V_WALK[0]) / (V_WALK[1] - V_WALK[0])), t)


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
