"""Scene 07 blocking, as pure functions of t. No drawing imports. Same shop and spots as Scenes 05-06, just after midnight.

Beats:
  0.00  The shop as Scene 06 left it: the swollen price cards, the three of them.
  0.25  A rubber stamp comes down out of the top of the frame: THUNK at 0.62. SINAVDA ÇIKAR, in red.
  0.75  The picture turns into a newspaper clipping: the stamped fact as its headline. Holds to 4.70, back by 5.05.
  5.00  Vehbi opens his book and holds it up. INSERT, the page: 1 ABD doları = 70 TL, underlined.
  5.50  Vehbi: "Seventy lira to the dollar. Same as the book."  (to 9.16)
  9.50  Sidar, hand on heart, moved: "Thirty years at the bank, and finally someone stamps my work."  (to 13.28)
 13.60  Vehbi, flat: "It's not your stamp."  (to 14.58)
 14.90  Sidar, sincerely puzzled: "Whose else would it be?"  (to 16.39)   End 17.60."""
import math

import room as R

END = R.END
L1, L2, L3, L4 = 5.50, 9.50, 13.60, 14.90

V_POS = (1.6, 2.3)
S_POS = (3.4, 2.35)
G_POS = (1.95, 4.4)
S_TH0 = math.pi + .3            # Facing Vehbi, opened a little to the front.
V_TH0 = -.3
G_TH0 = -math.pi / 2 + .25      # Facing his customers.
G_BACK = math.pi / 2            # Facing the shelves.


def sidar(t):
    return S_POS


def vehbi(t):
    return V_POS


def grocer(t):
    return G_POS


def heading(a, b):
    return math.atan2(b[1] - a[1], b[0] - a[0])


def pos(name, t, z=0.0):
    x, y = {'vehbi': vehbi, 'sidar': sidar, 'grocer': grocer}[name](t)
    return (x, y, z)
