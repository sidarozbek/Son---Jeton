"""Scene 17 blocking, as pure functions of t. No drawing imports. The customs post, a moment after Scene 16.

Beats:
  0.00  The customs post. Two paper ships afloat; a tiny one still peeking out of the open drawer. The officer, head
        down over his forms, says nothing.
  0.60  The "Sınavda çıkar" stamp comes down: D6. The clipping holds to 5.15, back by 5.50.
  5.80  Vehbi opens the book. 6.20: "Tax refunds and export credits. It's in the book."  (to 9.89)
        INSERT 6.75-8.35: the textbook page, the line underlined. Then his finger taps the page.
 10.40  Sidar, proud, a hand out to his ships: "I put these ships on paper."  (to 12.48)
 13.00  Vehbi, flat: "That's the problem."  (to 13.76)   End 14.60."""
import math

import room as R

END = R.END
S_POS = (-7.6, 1.5)
V_POS = (-6.1, .7)
O_POS = (-9.95, 1.2)
S_TH0 = math.atan2(V_POS[1] - S_POS[1], V_POS[0] - S_POS[0])     # Sidar faces Vehbi.
V_TH0 = math.atan2(S_POS[1] - V_POS[1], S_POS[0] - V_POS[0])     # Vehbi faces Sidar.


def heading(a, b):
    return math.atan2(b[1] - a[1], b[0] - a[0])


def where(name, t):
    return {'sidar': S_POS, 'vehbi': V_POS, 'officer': O_POS}[name]


def pos(name, t, z=0.0):
    x, y = where(name, t)
    return (x, y, z)
