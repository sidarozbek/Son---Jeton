"""The corridor after the exam, late morning: even indoor light, a bright window at the far end. Light in env.post."""
from toonkit.camera import Plane

import blocking

END = blocking.END
GROUND = Plane()
SKY0, SKY1 = (.70, .78, .86), (.86, .88, .90)
CLOUDS = 0
HAZE_COL = (.9, .9, .9)
HAZE_DIST = 400
HAZE_MAX = .05
TO_LIGHT = (-.1, .8, .6)
RIM_COL = (1.0, .98, .94)
RIM = .35
SHADOW = .35
SHADOW_TINT = (.97, .98, 1.02)
SAT, TINT = .9, (1.0, 1.0, 1.0)
CHAR_SAT, CHAR_TINT, CHAR_GAIN = .92, (1.0, 1.0, 1.0), 1.0
LINE_OF_ACTION = None
