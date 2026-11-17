"""Scene 20 blocking, as pure functions of t. No drawing imports. The payphone on the harbour office's wall.

Beats:
  0.55  Sidar holds up token five between them.
  0.80  Solemn: "Last one. Token five."  (to 2.47)
  2.90  The token turns see-through in his fingers, ruled like a form (to 4.00): it exists only on paper.
  4.30  Vehbi: "It's... see-through."  (to 5.71)
  6.10  Sidar, to Vehbi, then turning to the phone: "It's a perfectly good tok—"  (to 8.03). He pushes it into the
        slot anyway (7.25); it is gone.
  7.95  The line crackles over the end of his word; the picture tears and snows.
  8.90  The harbour folds away like a sheet of paper, with them in it (to 12.40).   End 13.00."""
import math

import room as R

END = R.END
S_POS = (-13.35, .2)                    # At the phone.
V_POS = (-12.5, -.7)
O_POS = (-9.95, 1.2)
S_TH0 = math.atan2(V_POS[1] - S_POS[1], V_POS[0] - S_POS[0])     # Sidar faces Vehbi for his lines.
V_TH0 = math.atan2(S_POS[1] - V_POS[1], S_POS[0] - V_POS[0])
S_PHONE = math.pi                       # Facing the phone on the wall.


def heading(a, b):
    return math.atan2(b[1] - a[1], b[0] - a[0])


def where(name, t):
    return {'sidar': S_POS, 'vehbi': V_POS, 'officer': O_POS}[name]


def pos(name, t, z=0.0):
    x, y = where(name, t)
    return (x, y, z)
