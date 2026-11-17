"""Scene 03 blocking, as pure functions of t. No drawing imports: shots.py, acting.py, env.py and sound.py read it.

Beats:
  0.00  Scene 02's end: Sidar (2.20, 3.72) eyeing the open door; Vehbi (2.98, 3.52), book at his side.
  0.30  Sidar turns to him: "Your phone line is broken."  (to 3.59)
  3.85  Vehbi: "I don't have a phone."  (to 4.81)
  5.10  Sidar: "Downstairs. Come."  He is already walking out of the door; Vehbi follows, book in hand.
  6.90  CUT to the basement. The bulb swings. They come off the stairs and cross to the payphone.
  9.05  Sidar lifts the receiver and holds it out: "It's for you."  (9.25 to 10.07)  Vehbi takes it at 10.20.
 10.55  Sidar holds up the token. INSERT: it drops into the slot (11.35 to 11.50).
 11.95  Vehbi, receiver to his ear: "Hello?"
 12.60  The line crosses: hiss, the bulb stutters. Sidar's smile, the first one that means something.
 13.70  The basement folds like paper: in half, in quarters, down to a small folded sheet on white.  End 18.20."""
import math

import room as R

END = 18.2
L1, L2, L3, L4, L5 = 0.30, 3.85, 5.10, 9.25, 11.95

S_START, V_START = (2.20, 3.72), (2.98, 3.52)
S_TH0 = math.atan2(4.4 - 3.72, 3.05 - 2.20) - .3     # Scene 02's last look: at the door.
S_DOOR, S_CORR = (3.05, 4.15), (3.0, 5.0)
V_FOLLOW = (2.92, 4.0)
S_EXIT = (5.7, 6.9)
V_EXIT = (6.15, 6.9)

# Basement spots.
S_STAIR, V_STAIR = (24.35, 3.9), (23.95, 3.55)     # Just off the bottom step.
S_PHONE, V_PHONE = (23.0, 4.22), (22.12, 4.45)
S_WALK = (R.CUT, 8.75)
V_WALK = (R.CUT + .25, 9.0)


def _ease(u):
    u = min(max(u, 0.0), 1.0)
    return u * u * (3 - 2 * u)


def _lerp(a, b, u):
    return (a[0] + (b[0] - a[0]) * u, a[1] + (b[1] - a[1]) * u)


def _path(pts, u):
    """Along a polyline, by length."""
    segs = [math.hypot(b[0] - a[0], b[1] - a[1]) for a, b in zip(pts, pts[1:])]
    d = u * sum(segs)
    for (a, b), L in zip(zip(pts, pts[1:]), segs):
        if d <= L or L == segs[-1]:
            return _lerp(a, b, min(d / L, 1) if L else 0)
        d -= L
    return pts[-1]


def sidar(t):
    if t < S_EXIT[0]:
        return S_START
    if t < R.CUT:
        return _path([S_START, S_DOOR, S_CORR], (t - S_EXIT[0]) / (S_EXIT[1] - S_EXIT[0]))
    if t < S_WALK[1]:
        return _lerp(S_STAIR, S_PHONE, _ease((t - S_WALK[0]) / (S_WALK[1] - S_WALK[0])))
    return S_PHONE


def vehbi(t):
    if t < V_EXIT[0]:
        return V_START
    if t < R.CUT:
        return _lerp(V_START, V_FOLLOW, (t - V_EXIT[0]) / (V_EXIT[1] - V_EXIT[0]))
    if t < V_WALK[0]:
        return V_STAIR
    if t < V_WALK[1]:
        return _lerp(V_STAIR, V_PHONE, _ease((t - V_WALK[0]) / (V_WALK[1] - V_WALK[0])))
    return V_PHONE


def heading(a, b):
    return math.atan2(b[1] - a[1], b[0] - a[0])


def pos(name, t, z=0.0):
    x, y = vehbi(t) if name == 'vehbi' else sidar(t)
    return (x, y, z)
