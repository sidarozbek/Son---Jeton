"""Scene 06 blocking, as pure functions of t. No drawing imports. Same shop and spots as Scene 05.

Beats:
  0.00  INSERT: the wall clock. The minute hand ticks onto twelve (0.60); it strikes.
  1.90  The shop at midnight, one bulb. Everyone where Scene 05 left them.
  2.30  The price cards on the shelves start to swell, all of them, slowly, to more than double their size.
  2.50  Vehbi takes a banknote out of his pocket; from 3.10 it shrinks in his fingers to a stamp.
  4.60  Sidar, triumphant, arms up: "See? SEE?!"  (to 5.53)
  6.20  Vehbi holds the tiny note up between two fingers: "Money doesn't shrink. Prices rise."  (to 8.34)
  8.60  Sidar, at once: "Same thing!"  (to 9.37)   End 10.80."""
import math

import room as R

END = R.END
L1, L2, L3 = 4.60, 6.20, 8.60

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
