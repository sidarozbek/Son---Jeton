"""Scene 22 blocking, as pure functions of t. No drawing imports. The 1989 street; the river of money.

Beats:
  0.55  Vehbi opens the book. 0.90: "August 1989. Money can cross the border freely now."  (to 4.58)
        INSERT 2.40-4.00: the textbook page, the decision underlined.
  4.90  The "Sınavda çıkar" stamp comes down: D8. The clipping holds to 9.25, back by 9.60.
  9.80  Something glints in the river: a token, coming downstream. Vehbi steps to the kerb.
 10.00  "If money flows... a token flows too."  (to 13.75)  12.20 he puts out his hand; 12.45-13.00 the token hops
        out of the river into it. The sixth token.
 14.60  Sidar, himself again: "I taught you where to look."  (to 16.03)   End 17.20."""
import math

import room as R

END = R.END
S_POS = (6.1, 4.7)
V_POS = (5.0, 4.85)
V_KERB = (5.15, 4.42)
V_STEP = (9.9, 10.6)
S_TH0 = -math.pi / 2 + .25
V_TH0 = -math.pi / 2 - .2


def _ease(u):
    u = min(max(u, 0.0), 1.0)
    return u * u * (3 - 2 * u)


def heading(a, b):
    return math.atan2(b[1] - a[1], b[0] - a[0])


def where(name, t):
    if name == 'sidar':
        return S_POS
    u = _ease((t - V_STEP[0]) / (V_STEP[1] - V_STEP[0]))
    return (V_POS[0] + (V_KERB[0] - V_POS[0]) * u, V_POS[1] + (V_KERB[1] - V_POS[1]) * u)


def pos(name, t, z=0.0):
    x, y = where(name, t)
    return (x, y, z)
