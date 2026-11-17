"""Scene 16 blocking, as pure functions of t. No drawing imports. The customs post on the quay.

Beats:
  0.00  The customs officer at his desk on the quay, the filing cabinet beside him. Sidar beside the desk, proud.
  0.70  The officer stamps a form. The cabinet's top drawer slides open; a tiny paper ship rises out of it (1.25),
        then hops over the quay edge, growing, and lands in the water full size (3.70). See-through.
  4.00  Sidar, proud: "See? One stamp, one ship."  (to 5.99)
  6.30  The officer stamps again; another ship comes out of the drawer and lands further out (9.30).
  7.20  Vehbi, deadpan, pointing at the cabinet: "It came out of a filing cabinet."  (to 9.44)
 10.10  Sidar, genuinely asking: "Where else do ships come from?"  (to 11.64)
 12.15  The officer stamps a third time. The drawer opens; a tiny ship peeks out.   End 13.60.
The officer never speaks; his stamp is a sound."""
import math

import room as R

END = R.END
S_POS = (-7.6, 1.5)
V_POS = (-6.1, .7)
O_POS = (-9.95, 1.2)
S_TH0 = math.atan2(V_POS[1] - S_POS[1], V_POS[0] - S_POS[0])     # Sidar faces Vehbi; he watches Vehbi, not the ships.
V_TH0 = math.atan2(S_POS[1] - V_POS[1], S_POS[0] - V_POS[0])     # Vehbi faces Sidar.


def heading(a, b):
    return math.atan2(b[1] - a[1], b[0] - a[0])


def where(name, t):
    return {'sidar': S_POS, 'vehbi': V_POS, 'officer': O_POS}[name]


def pos(name, t, z=0.0):
    x, y = where(name, t)
    return (x, y, z)
