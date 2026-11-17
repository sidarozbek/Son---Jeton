"""Scene 13 blocking, as pure functions of t. No drawing imports. Kuş Bankerlik. No one speaks; no joke.

Beats:
  0.00  The office as before: the queue at the window, the board at %150, the flock circling under the ceiling.
  2.80  The whole flock lifts at once and streams out of the street door (3.2-5.4). Silence after it.
  5.60  The teller window's shutter comes down. The board goes dark.
  6.00  The queue stands still. Nobody moves for a long moment; heads lower, slowly.
 10.00  One hook of the KUŞ BANKERLİK sign gives; it swings down, hangs, and falls to the floor (10.9-11.35).
        Then nothing. End 14.60."""
import math

import room as R

END = R.END
V_POS = (3.95, 2.35)
S_POS = (4.7, 2.6)
S_TH0 = math.atan2(5.5 - 2.6, 5.2 - 4.7)
V_TH0 = math.atan2(2.6 - 2.35, 4.7 - 3.95) - .3
WIN_C = ((R.WINDOW[0] + R.WINDOW[1]) / 2, R.D)
Q_TH0 = [math.atan2(WIN_C[1] - y, WIN_C[0] - x) for x, y in R.QUEUE_SPOTS]


def sidar(t):
    return S_POS


def vehbi(t):
    return V_POS


def queue(i, t):
    return R.QUEUE_SPOTS[i]


def heading(a, b):
    return math.atan2(b[1] - a[1], b[0] - a[0])


def where(name, t):
    if name == 'sidar':
        return sidar(t)
    if name == 'vehbi':
        return vehbi(t)
    return queue(int(name[1:]), t)


def pos(name, t, z=0.0):
    x, y = where(name, t)
    return (x, y, z)
