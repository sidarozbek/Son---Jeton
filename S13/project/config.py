"""The office of "Kuş Bankerlik", 1982, daytime. Even, warm office light; daylight at the street door.
The light itself is in env.post."""
from toonkit.camera import Plane

import blocking

END = blocking.END
GROUND = Plane()
SKY0, SKY1 = (.62, .70, .80), (.78, .82, .86)
CLOUDS = 0
HAZE_COL = (.30, .26, .20)
HAZE_DIST = 300
HAZE_MAX = .08
TO_LIGHT = (-.2, -.35, .91)
RIM_COL = (.95, .9, .8)
RIM = .18
SHADOW = .35
SHADOW_TINT = (1, .97, .92)
SAT, TINT = .92, (1.03, 1.0, .94)
CHAR_SAT, CHAR_TINT, CHAR_GAIN = .95, (1.02, 1.0, .96), 1.0
LINE_OF_ACTION = ('vehbi', 'sidar')
