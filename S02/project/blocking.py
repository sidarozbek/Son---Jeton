"""Scene 02 blocking, as pure functions of t. No drawing imports: shots.py, acting.py, env.py and sound.py all read it.

Beats:
  0.00  Where Scene 01 ended: Sidar inside, smug; Vehbi facing him, book in hand.
  0.40  Sidar, chest out: "January 1980. I was in that room." He points up at "that room", eyes narrowed, seeing it.
  4.30  Vehbi pushes his glasses up, opens the book, turns it to him.
  5.00  Vehbi: "That's not what it says."
  6.25  Sidar reads. Slowly. Anger arrives.
  7.00  Sidar: "Then the book is wrong!"  He lunges and seizes the book at 8.20.
  8.20  Tug of war. Vehbi never lets go. They turn half a circle around the book, swapping places; five yanks.
 12.15  The contract slips out of the book and drifts to the floor (lands 13.15).
 13.40  Sidar lets go all at once, straightens his tie as if nothing happened. Never embarrassed.
 15.40  Vehbi looks down at the contract, then slowly back up at him.
 17.40  Sidar, not looking at Vehbi, surveys the room; his eyes go to the open door.  End 19.0."""
import math

import room as R

END = 19.0
L1, L2, L3 = 0.40, 5.0, 7.0

S_START = (2.98, 3.52)     # Scene 01's end.
V_START = (2.20, 3.72)
C = ((S_START[0] + V_START[0]) / 2, (S_START[1] + V_START[1]) / 2)
RAD = math.hypot(S_START[0] - C[0], S_START[1] - C[1])
PHI0 = math.atan2(S_START[1] - C[1], S_START[0] - C[0])
TURN = (8.6, 11.9)         # Half a circle around the book.
BOOK_Z = 1.02


def _ease(u):
    u = min(max(u, 0.0), 1.0)
    return u * u * (3 - 2 * u)


def turn(t):
    """Angle travelled around the book, 0 to pi, with a stagger at each yank."""
    u = _ease((t - TURN[0]) / (TURN[1] - TURN[0]))
    return math.pi * u


def sidar(t):
    a = PHI0 + turn(t)
    return (C[0] + RAD * math.cos(a), C[1] + RAD * math.sin(a))


def vehbi(t):
    a = PHI0 + math.pi + turn(t)
    return (C[0] + RAD * math.cos(a), C[1] + RAD * math.sin(a))


def yank(t):
    """0 to 1: how hard the book is pulled toward Sidar at this moment."""
    v = 0.0
    for k in R.YANKS:
        d = t - k
        if -.06 < d < .45:
            v = max(v, math.exp(-max(d, 0) * 7) if d >= 0 else (d + .06) / .06)
    return v


def book(t):
    """The book's centre in the world: between them, pulled toward Sidar on each yank."""
    s, v = sidar(t), vehbi(t)
    k = .5 + .13 * yank(t)
    return (v[0] + (s[0] - v[0]) * k, v[1] + (s[1] - v[1]) * k, BOOK_Z + .03 * math.sin(t * 9) * (R.GRAB < t < R.RELEASE))


def heading(a, b):
    return math.atan2(b[1] - a[1], b[0] - a[0])


def pos(name, t, z=0.0):
    x, y = vehbi(t) if name == 'vehbi' else sidar(t)
    return (x, y, z)


# The contract's fall: from the book to the floor in front of them, drifting side to side.
FLOOR_SPOT = (C[0] + .05, C[1] - .32)


def contract(t):
    """(x, y, z, flutter angle, lying flat 0..1) or None before it slips."""
    if t < R.SLIP:
        return None
    b = book(R.SLIP)
    u = min((t - R.SLIP) / (R.LAND - R.SLIP), 1.0)
    e = 1 - (1 - u) ** 1.6
    x = b[0] + (FLOOR_SPOT[0] - b[0]) * e + .12 * math.sin(u * 7.5) * (1 - u)
    y = b[1] + (FLOOR_SPOT[1] - b[1]) * e
    z = b[2] * (1 - e) + .004
    ang = .9 * math.sin(u * 7.5) * (1 - u)
    return (x, y, z, ang, u)
