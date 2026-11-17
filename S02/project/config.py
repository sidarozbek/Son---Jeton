"""A rented room at night. One warm desk lamp; the corridor beyond the door is cold. The lamp pool itself is in env.post."""
from toonkit.camera import Plane

import blocking

END = blocking.END
GROUND = Plane()
SKY0, SKY1 = (.05, .06, .10), (.08, .09, .14)
CLOUDS = 0
HAZE_COL = (.20, .17, .14)
HAZE_DIST = 300
HAZE_MAX = .12
TO_LIGHT = (-.4, -.42, .81)    # Towards the desk lamp, raised: short shadows, so one character's shadow never falls across the other.
RIM_COL = (.62, .72, .95)      # Cold edge from the corridor.
RIM = .24
SHADOW = .4
SHADOW_TINT = (1, .96, .9)
SAT, TINT = .9, (1.02, .98, .92)
CHAR_SAT, CHAR_TINT, CHAR_GAIN = .95, (1.02, .98, .94), 1.0
LINE_OF_ACTION = ('sidar', 'vehbi')
