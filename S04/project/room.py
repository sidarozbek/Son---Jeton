"""Scene 04: a street on the evening of 24 January 1980, as pure functions of t. No drawing imports.
The road runs along x. Cameras stand in the road (low y); the far sidewalk and the facades are at the back (high y).
  y 0.0-4.2   cobbled road
  y 4.2-6.0   sidewalk, kerb at 4.2
  y 6.0       the facades: ground-floor walls, the grocer's front (x 4.4-7.6), upper floors above 3.2 m"""

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

# ---- timing
UNFOLD = (0.0, 2.4)                  # The folded sheet from Scene 03 opens into the street.
HAND_DOWN = 2.75                     # Vehbi notices he is still holding a phone that isn't there.
SHAKE = (3.0, 5.85)                  # Sidar shakes the four tokens.
WATCH = (5.55, 7.45)                 # Vehbi checks his watch.
GLANCE = 10.6                        # Vehbi's eyes snap to the calendar.
END = 16.8


def unfold(t):
    """1 while it is still a folded sheet, 0 once the street is open."""
    u = (t - UNFOLD[0]) / (UNFOLD[1] - UNFOLD[0])
    return 1.0 - min(max(u, 0.0), 1.0)
