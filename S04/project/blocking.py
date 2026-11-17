"""Scene 04 blocking, as pure functions of t. No drawing imports.

Beats:
  0.00  The small folded sheet Scene 03 ended on opens out into a street at dusk, light snow: 24 January 1980.
        They stand where the fold left them: Vehbi left, Sidar right, as at the payphone. Vehbi's hand is still at his ear.
  2.75  Vehbi lowers the hand: there is no receiver. He takes in the street.
  3.00  Sidar holds up four brass tokens and shakes them like dice.
  3.30  Sidar: "Four tokens left. Don't make me waste them."  (to 5.61)
  5.55  Vehbi checks his watch.  6.05  "My exam starts at nine."  (to 8.16)
  8.50  Sidar, enjoying it: "Nine o'clock. Which year?"  (to 10.46)
 10.60  Vehbi's eyes go to the grocer's window: a tear-off calendar. INSERT: OCAK 24 1980 PERŞEMBE.
 11.85  Vehbi, flat, instant: "January twenty-fourth, nineteen eighty."  (to 14.24)
 14.75  Sidar, put out: "…Lucky guess."  He turns to the street.  End 16.80."""
import math

import room as R

END = R.END
L1, L2, L3, L4, L5 = 3.30, 6.05, 8.50, 11.85, 14.75

V_START = (5.45, 4.95)
S_START = (6.45, 4.85)
S_TH0 = math.pi + .38          # Facing Vehbi, opened a little to the road (the cameras).
V_TH0 = -.38
S_AWAY = (6.75, 4.5)           # Where he turns to at the end: the street.


def sidar(t):
    return S_START


def vehbi(t):
    return V_START


def heading(a, b):
    return math.atan2(b[1] - a[1], b[0] - a[0])


def pos(name, t, z=0.0):
    x, y = vehbi(t) if name == 'vehbi' else sidar(t)
    return (x, y, z)
