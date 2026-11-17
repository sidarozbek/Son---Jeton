"""Scene 19: the harbour, mid-1980s, a clear day, at the customs post. Bright, slightly hazy sea air. The light itself is in env.post."""
from toonkit.camera import Plane

import blocking

END = blocking.END
GROUND = Plane()
SKY0, SKY1 = (.58, .72, .86), (.86, .89, .88)
CLOUDS = .08
HAZE_COL = (.80, .84, .86)
HAZE_DIST = 140
HAZE_MAX = .5
TO_LIGHT = (-.35, -.45, .82)
RIM_COL = (.9, .92, .95)
RIM = .25
SHADOW = .45
SHADOW_TINT = (.95, .97, 1.02)
SAT, TINT = .9, (1.0, 1.0, .99)
CHAR_SAT, CHAR_TINT, CHAR_GAIN = .92, (1.0, 1.0, .99), 1.0
LINE_OF_ACTION = ('vehbi', 'sidar')
