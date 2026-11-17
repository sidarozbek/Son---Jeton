"""Scene 03: the room in Scene 02's end state, and the basement, as pure functions of t. No drawing imports.
The basement sits in the same world, beside the house, at x 20-25: a cut between the two is a cut, not a walk."""
import math

# ---- the room (identical to Scenes 01-02; door wide open, the stack where it was shoved)
W, D, H = 4.0, 4.4, 2.7
DOOR_X0, DOOR_X1, DOOR_H = 2.6, 3.5, 2.05
HINGE = (3.5, 4.4)
DOOR_W = DOOR_X1 - DOOR_X0
CORR_Y1 = 6.0
LAMP = (0.3, 1.44, 1.16)
DESK = (0.38, 1.85)
STACK = (3.29, 3.08)
DOOR_OPEN = 1.72
KNOCKS = ()

# ---- the basement
BX0, BX1, BY0, BY1, BH = 20.0, 25.0, 0.0, 5.0, 2.4
PHONE_X = 22.55                     # Centre of the payphone, on the back wall.
PHONE_Z0 = 1.05                     # Its bottom edge.
PHONE_FACE_Y = BY1 - .12            # Its front face.
SLOT = (PHONE_X + .09, PHONE_FACE_Y - .01, PHONE_Z0 + .44)
CRADLE = (PHONE_X - .2, PHONE_FACE_Y - .03, PHONE_Z0 + .3)
CORD_PORT = (PHONE_X - .15, PHONE_FACE_Y - .02, PHONE_Z0 + .05)
BULB = (22.35, 3.4, 2.1)

# ---- timing
CUT = 6.9                           # Room to basement.
LIFT = 9.05                         # Sidar lifts the receiver.
HANDOVER = 10.2                     # Vehbi takes it.
COIN_SHOW = 10.55                   # Sidar holds up the token...
COIN_IN = 11.35                     # ...and drops it in: in the slot at 11.50.
CRACKLE = 12.6                      # The line crosses: hiss, the bulb flickers.
FOLD = (13.7, 17.6)                 # The basement folds like paper.


def door_angle(t):
    return DOOR_OPEN


def door_open(t):
    return 1.0


def lamp_shake(t):
    return 0.0


def stack_slide(t):
    return 0.0


def stack_tilt(t):
    return 0.0


def bulb(t):
    """Where the hanging bulb is: a slow swing (someone brushed it on the stairs), steadier as time goes on."""
    a = .06 * math.exp(-max(t - CUT, 0) * .25) * math.sin((t - CUT) * 2.3)
    return (BULB[0] + a, BULB[1] + a * .4, BULB[2])


def flicker(t):
    """Bulb brightness, 1 is steady. It stutters when the line crosses and keeps stuttering into the fold."""
    if t < CRACKLE:
        return 1.0
    d = t - CRACKLE
    k = (math.sin(d * 47) * math.sin(d * 13.3) + math.sin(d * 71.7) * .5)
    return max(.35, 1.0 - .35 * (k > .25) - .25 * (abs(math.sin(d * 9.1)) > .93))


def fold(t):
    """0 to 1 through the paper fold."""
    return min(max((t - FOLD[0]) / (FOLD[1] - FOLD[0]), 0.0), 1.0)
