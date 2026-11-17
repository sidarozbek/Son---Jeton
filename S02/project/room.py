"""Room layout (identical to Scene 01) and Scene 02's mechanics, as pure functions of t. No drawing imports.
Scene 02 starts where Scene 01 ends: the door wide open against its stop, the floor stack where the door shoved it."""
import math

W, D, H = 4.0, 4.4, 2.7
DOOR_X0, DOOR_X1, DOOR_H = 2.6, 3.5, 2.05
HINGE = (3.5, 4.4)
DOOR_W = DOOR_X1 - DOOR_X0
CORR_Y1 = 6.0
LAMP = (0.3, 1.44, 1.16)
DESK = (0.38, 1.85)
STACK = (3.29, 3.08)             # Where Scene 01 left it (3.63 - 0.55).
DOOR_OPEN = 1.72                 # Scene 01's final angle.

KNOCKS = ()
GRAB = 8.2                       # Sidar seizes the book.
RELEASE = 13.4                   # He lets go, all at once.
YANKS = (8.9, 9.6, 10.35, 11.1, 11.75)
SLIP = 12.15                     # The contract slides out of the book.
LAND = 13.15                     # ...and lies flat on the floor.


def door_angle(t):
    return DOOR_OPEN


def door_open(t):
    return 1.0


def lamp_shake(t):
    """A small jump when the book is grabbed and when it's let go."""
    s = 0.0
    for k, a in ((GRAB, .02), (RELEASE, .015)):
        d = t - k
        if 0 <= d < 1.0:
            s += a * math.exp(-d * 6) * math.sin(d * 34)
    return s


def stack_slide(t):
    return 0.0


def stack_tilt(t):
    return 0.0
