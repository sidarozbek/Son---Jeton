"""Inside the grocer's, evening. One warm pendant bulb over the counter; cold blue dusk at the front window.
The light pools themselves are in env.post."""
from toonkit.camera import Plane

import blocking

END = blocking.END
GROUND = Plane()
SKY0, SKY1 = (.16, .20, .34), (.30, .32, .44)
CLOUDS = 0
HAZE_COL = (.30, .26, .20)
HAZE_DIST = 300
HAZE_MAX = .1
TO_LIGHT = (-.2, -.3, .93)     # The bulb overhead: short shadows.
RIM_COL = (.62, .72, .95)      # Cold edge from the front window.
RIM = .22
SHADOW = .35
SHADOW_TINT = (1, .96, .9)
SAT, TINT = .92, (1.03, 1.0, .93)
CHAR_SAT, CHAR_TINT, CHAR_GAIN = .95, (1.02, .99, .95), 1.0
LINE_OF_ACTION = ('vehbi', 'sidar')
