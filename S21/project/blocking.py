"""Scene 21 blocking, as pure functions of t. No drawing imports. August 1989; the street; the river of money.

Beats:
  0.00  Scene 20's fold runs backwards: the folded sheet opens out into 1989 (to 2.40).
  2.40  The street on a summer evening. Where the road was, a river of banknotes flows past. They stand on the
        sidewalk at its edge, in front of the exchange office. Sidar's hands are empty.
  5.00  Vehbi: "No tokens. The exam's in ten hours."  (to 8.13)
  8.30  Sidar looks at the river. His anger goes out, for the first time.
  9.60  Quietly: "They won't believe me here either."  (to 11.44)
 11.50  Nothing. They stand at the edge of it. The money keeps flowing.   End 15.00."""
import math

import room as R

END = R.END
S_POS = (6.1, 4.7)
V_POS = (5.0, 4.85)
S_TH0 = -math.pi / 2 + .25               # Both facing the river (the road), a little towards each other.
V_TH0 = -math.pi / 2 - .2


def heading(a, b):
    return math.atan2(b[1] - a[1], b[0] - a[0])


def where(name, t):
    return S_POS if name == 'sidar' else V_POS


def sidar(t):
    return S_POS


def vehbi(t):
    return V_POS


def pos(name, t, z=0.0):
    x, y = where(name, t)
    return (x, y, z)
