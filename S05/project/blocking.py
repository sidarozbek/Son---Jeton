"""Scene 05 blocking, as pure functions of t. No drawing imports.

Beats:
  0.00  Inside the grocer's. The door bell is still ringing. Sidar and Vehbi at the counter; the grocer behind it looks up.
  1.00  Sidar leans in to Vehbi, ominous: "Tonight, your money shrinks."  (to 2.57)
  2.90  Vehbi pushes up his glasses, shuts his eyes, and recites: "Devaluation. The lira loses value against foreign
        currency, so imports cost more."  (3.30 to 10.27)
  3.90  Behind him the grocer turns his back and flips three price cards on the shelf to double: 5.1, 6.6, 8.1.
  9.55  The grocer turns round again, all innocence.
 10.70  Sidar, with a nod at the grocer: "He's read the same book."  (to 12.13)
 12.30  Vehbi opens his eyes, looks at the grocer. The grocer smiles.  End 13.80."""
import math

import room as R

END = R.END
L1, L2, L3 = 1.00, 3.30, 10.70

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
