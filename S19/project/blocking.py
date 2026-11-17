"""Scene 19 blocking, as pure functions of t. No drawing imports. Sidar still on the deck of ship A; Vehbi on the quay.

Beats:
  0.60  The "Sınavda çıkar" stamp comes down: D7. The clipping holds to 5.15, back by 5.50.
  5.80  Vehbi, clear and quick, counting on his fingers: "Empty containers. Fake invoices. Refunds for goods that never
        left."  (to 10.35)  On "Empty containers" the containers' lids swing open (6.25-6.90): nothing inside. On "Fake
        invoices" invoices burst out of them (7.30) and rain down over the quay, the deck and the water.
 10.20  One flutters into Sidar's hand (10.60). He waves it: "Told you!"  (10.75)
 11.60  Vehbi: "You said the ships were full."  (to 13.33)
 13.70  Sidar, waving it: "Of invoices!"  (to 14.79)   End 15.80."""
import math

import room as R

END = R.END
S_POS = (-6.45, 5.0)                    # On ship A's deck, where Scene 18 left him.
V_POS = (-6.6, 2.6)                     # On the quay below him.
O_POS = (-9.95, 1.2)
S_TH0 = math.atan2(V_POS[1] - S_POS[1], V_POS[0] - S_POS[0])
V_TH0 = math.atan2(S_POS[1] - V_POS[1], S_POS[0] - V_POS[0])


def heading(a, b):
    return math.atan2(b[1] - a[1], b[0] - a[0])


def where(name, t):
    return {'sidar': S_POS, 'vehbi': V_POS, 'officer': O_POS}[name]


def pos(name, t, z=0.0):
    x, y = where(name, t)
    return (x, y, R.deck_ground(x, y) if name == 'sidar' else z)
