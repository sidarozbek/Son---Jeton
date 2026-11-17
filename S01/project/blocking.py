"""Where everyone stands, as pure functions of t, and when each line starts. No drawing imports: shots.py (inside Blender),
acting.py and sound.py all read it. Door, lamp and book timing live in room.py.

Beats:
  0.0  Vehbi studies at the desk. Knocks; the lamp jumps. He doesn't look up.
  2.3  Corridor, low: Sidar pounds and shouts. "Vehbi! Rent!"
  4.2  Vehbi pushes his glasses up, walks to the door, opens it a crack.
  7.3  Through the crack he reads clause seven from the contract in his book.
 11.85 Sidar: "I'm giving notice!"   13.5 Vehbi: "In writing."
 14.9  Sidar shoulders the door wide open; the books skid. He walks in.
 16.7  "I'm here." Chest out: his arrival is the notice.
 18.15 Vehbi looks at him, slowly, for a long time.  20.35 Crane up."""
import math

import room as R

END = 21.95

# Line starts, scene seconds.
L1, L2, L3, L4 = 2.95, 7.3, 11.85, 13.5     # Timed to the recorded voices.
L5 = 16.7

# Spots.
V_DESK = (1.0, 2.5)          # Standing by the chair, facing the desk.
V_GAP = (2.6, 3.95)         # Inside the crack, clear of the door's swing.
V_BACK = (2.2, 3.72)         # Where the swinging door sends him.
S_DOOR = (3.2, 4.78)        # Corridor side, at the door.
S_IN = (2.98, 3.52)          # Inside, after the push.

V_WALK = (4.25, 6.55)        # Desk to the crack.
V_STEP = (14.95, 15.45)      # Back from the door as it flies.
S_WALK = (15.3, 16.5)      # Through the door to his spot.


def _ease(u):
    u = min(max(u, 0.0), 1.0)
    return u * u * (3 - 2 * u)


def _lerp(a, b, u):
    return (a[0] + (b[0] - a[0]) * u, a[1] + (b[1] - a[1]) * u)


def vehbi(t):
    if t < V_WALK[0]:
        return V_DESK
    if t < V_WALK[1]:
        u = (t - V_WALK[0]) / (V_WALK[1] - V_WALK[0])
        # Around the end of the bed corner, not straight through the chair: a slight curve.
        p = _lerp(V_DESK, V_GAP, u)
        bulge = math.sin(u * math.pi) * .22
        return (p[0] + bulge * .5, p[1] - bulge * .5)
    if t < V_STEP[0]:
        return V_GAP
    if t < V_STEP[1]:
        return _lerp(V_GAP, V_BACK, _ease((t - V_STEP[0]) / (V_STEP[1] - V_STEP[0])))
    return V_BACK


def sidar(t):
    if t < S_WALK[0]:
        # The shove: a lurch toward the door, then he follows it through.
        if R.PUSH[0] - .2 < t < S_WALK[0]:
            k = math.sin(min(max((t - (R.PUSH[0] - .2)) / .55, 0), 1) * math.pi * .5)
            return (S_DOOR[0], S_DOOR[1] - .12 * k)
        return S_DOOR
    u = (t - S_WALK[0]) / (S_WALK[1] - S_WALK[0])
    if u < 1:
        return _lerp((S_DOOR[0], S_DOOR[1] - .12), S_IN, u)
    return S_IN


def pos(name, t, z=0.0):
    x, y = vehbi(t) if name == 'vehbi' else sidar(t)
    return (x, y, z)
