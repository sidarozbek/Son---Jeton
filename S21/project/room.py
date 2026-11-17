"""Scene 21: the same street (Scenes 04 and 09), an evening in August 1989. The grocer's is an exchange office now.
A river of money flows down the street where the road was: banknotes, original and generic, drifting like water.
Scene 09: the same street (Scene 04) on the morning of 12 September 1980: empty, silent, shutters down.
Scene 04: a street on the evening of 24 January 1980, as pure functions of t. No drawing imports.
The road runs along x. Cameras stand in the road (low y); the far sidewalk and the facades are at the back (high y).
  y 0.0-4.2   cobbled road
  y 4.2-6.0   sidewalk, kerb at 4.2
  y 6.0       the facades: ground-floor walls, the grocer's front (x 4.4-7.6), upper floors above 3.2 m"""

import math

ROAD_Y1 = 4.2
FACADE_Y = 6.0
X0, X1 = -8.0, 20.0
GROUND_H = 3.2                       # Height of the ground floor; the upper facade starts here.
UPPER_H = 8.8
SHOP_X0, SHOP_X1 = 4.4, 7.6          # The grocer's front.
SHOP_WIN = (4.52, 6.7, .95, 2.45)    # Its lit window: x0, x1, z0, z1.
CAL = (4.66, 5.0, 1.28, 1.72)       # The tear-off calendar hanging inside the glass: x0, x1, z0, z1.
CAL_Y = FACADE_Y - .015
LAMP_POST = (2.3, 4.45)              # A street lamp at the kerb.
LAMP_HEAD = (2.3, 4.05, 4.05)        # Its lamp, on an arm over the road.
WIN_LIGHT = (5.6, FACADE_Y + .3, 1.7)

PHONE_X = 8.4                         # A wall payphone on the facade, right of the grocer (Scene 03's design).
PHONE_Z0 = 1.05
SLOT = (PHONE_X + .09, FACADE_Y - .07, PHONE_Z0 + .44)

# ---- the river of money: notes drifting along +x over the road, faster in mid-stream.
RIVER = (.3, 4.05)                    # y range, kerb to kerb.
RIVER_X = (-6.0, 22.0)
N_NOTES = 1500

# ---- timing
UNFOLD = (0.0, 2.4)                   # Scene 20's fold, run backwards: the paper opens out into 1989.
L1, L2 = 5.00, 9.60                   # Vehbi, Sidar.
END = 15.00


def unfold(t):
    """1 = folded small (where Scene 20 ended), 0 = open."""
    u = min(max((t - UNFOLD[0]) / (UNFOLD[1] - UNFOLD[0]), 0.0), 1.0)
    return 1 - u


_rng = __import__('random').Random(21)
NOTES = []
for _j in range(N_NOTES):
    y = _rng.uniform(*RIVER)
    mid = 1 - abs((y - sum(RIVER) / 2) / ((RIVER[1] - RIVER[0]) / 2))
    NOTES.append(dict(x=_rng.uniform(*RIVER_X), y=y, v=.5 + 1.0 * mid + _rng.uniform(-.1, .1), z=_rng.uniform(.03, .22),
                      yaw=_rng.uniform(-.6, .6), ph=_rng.uniform(0, 6.28), col=_rng.randrange(6)))


def note(j, t):
    """(x, y, z, yaw, tilt) of note j at time t: drifting down the street, turning slowly, riding the ripples."""
    n = NOTES[j]
    span = RIVER_X[1] - RIVER_X[0]
    x = RIVER_X[0] + (n['x'] - RIVER_X[0] + n['v'] * t) % span
    y = n['y'] + .08 * math.sin(t * .9 + n['ph'])
    z = n['z'] + .03 * math.sin(t * 2.2 + n['ph'] * 2)
    return x, y, z, n['yaw'] + .25 * math.sin(t * .5 + n['ph']), .25 * math.sin(t * 1.7 + n['ph'])
