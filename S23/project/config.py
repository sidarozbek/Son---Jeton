"""The exam hall, the present day, morning: even, cool daylight from the windows on the left. Light in env.post."""
from toonkit.camera import Plane

import blocking

END = blocking.END
GROUND = Plane()
SKY0, SKY1 = (.70, .78, .86), (.86, .88, .90)
CLOUDS = 0
HAZE_COL = (.8, .8, .8)
HAZE_DIST = 400
HAZE_MAX = .05
TO_LIGHT = (-.8, -.2, .55)
RIM_COL = (.95, .95, .98)
RIM = .25
SHADOW = .35
SHADOW_TINT = (.97, .98, 1.02)
SAT, TINT = .9, (1.0, 1.0, 1.01)
CHAR_SAT, CHAR_TINT, CHAR_GAIN = .92, (1.0, 1.0, 1.0), 1.0
LINE_OF_ACTION = None
