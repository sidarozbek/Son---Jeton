"""Scene 09: the street on a grey September morning, 1980. Flat, cool daylight; nothing warm.
Scene 04: a street at dusk, 24 January 1980, light snow. Cold blue air; warm light from the grocer's window and one street lamp.
The pools themselves are in env.post."""
from toonkit.camera import Plane

import blocking

END = blocking.END
GROUND = Plane()
SKY0, SKY1 = (.62, .66, .70), (.74, .76, .78)   # Dusk: deep blue overhead, a greyer band low down.
CLOUDS = 0
HAZE_COL = (.42, .46, .58)
HAZE_DIST = 60
HAZE_MAX = .35
TO_LIGHT = (-.3, -.5, .81)     # Soft, high: short shadows towards the facades.
RIM_COL = (.85, .88, .92)
RIM = .15
SHADOW = .3
SHADOW_TINT = (.9, .94, 1.05)
SAT, TINT = .7, (.98, .99, 1.01)
CHAR_SAT, CHAR_TINT, CHAR_GAIN = .8, (1.0, 1.0, 1.0), 1.0
LINE_OF_ACTION = ('vehbi', 'sidar')
