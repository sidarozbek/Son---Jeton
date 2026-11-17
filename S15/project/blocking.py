"""Scene 15 blocking, as pure functions of t. No drawing imports. The harbour; see-through ships drift past in silence.

Beats:
  0.00  The harbour. Three pale, see-through ships glide by without a sound. Sidar and Vehbi on the quay.
  2.70  Sidar turns to us, arms wide, grand: "Ships. Full of goods."  (to 4.10)
  4.30  Vehbi walks to the quay edge and stands side-on to the passing ship.
  5.55  He puts his right hand out sideways to touch the hull; it goes straight in (6.05). The hull slides on through it.
  7.10  Vehbi, hand still inside, to Sidar: "Full of what?"  (to 7.75)
  8.60  Sidar, defensive: "Goods! Paper goods."  (to 10.13)
 10.40  Vehbi takes his hand back out and looks at it: nothing on it.   End 13.00."""
import math

import room as R

END = R.END
S_POS = (-1.0, 2.7)
V_WALK = R.V_WALK
V_START = (.35, 2.85)
V_EDGE = (.62, 3.78)
S_TH0 = math.pi / 2 - .15                      # Both looking out to sea at first.
V_TH0 = math.pi / 2 + .1
S_TO_CAM = math.atan2(-.4 - 2.7, -.7 + 1.0)    # Sidar turns to the camera for his line.
V_SIDE = math.pi                               # Side-on at the edge: his right side to the ship.


def _ease(u):
    u = min(max(u, 0.0), 1.0)
    return u * u * (3 - 2 * u)


def _lerp(a, b, u):
    return (a[0] + (b[0] - a[0]) * u, a[1] + (b[1] - a[1]) * u)


def heading(a, b):
    return math.atan2(b[1] - a[1], b[0] - a[0])


def sidar(t):
    return S_POS


def vehbi(t):
    return _lerp(V_START, V_EDGE, _ease((t - V_WALK[0]) / (V_WALK[1] - V_WALK[0])))


def where(name, t):
    return sidar(t) if name == 'sidar' else vehbi(t)


def pos(name, t, z=0.0):
    x, y = where(name, t)
    return (x, y, z)
