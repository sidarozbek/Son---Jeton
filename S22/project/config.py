"""August 1989, a summer evening: low warm sun down the street, a peach sky. The light itself is in env.post."""
from toonkit.camera import Plane

import blocking

END = blocking.END
GROUND = Plane()
SKY0, SKY1 = (.52, .60, .78), (.98, .80, .60)
CLOUDS = .06
HAZE_COL = (.95, .80, .66)
HAZE_DIST = 60
HAZE_MAX = .3
TO_LIGHT = (.75, -.35, .56)
RIM_COL = (1.0, .82, .6)
RIM = .35
SHADOW = .45
SHADOW_TINT = (.95, .9, 1.02)
SAT, TINT = .95, (1.04, .99, .92)
CHAR_SAT, CHAR_TINT, CHAR_GAIN = .95, (1.04, .99, .93), 1.0
LINE_OF_ACTION = ('vehbi', 'sidar')
