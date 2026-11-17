"""A street at dusk, 24 January 1980, light snow. Cold blue air; warm light from the grocer's window and one street lamp.
The pools themselves are in env.post."""
from toonkit.camera import Plane

import blocking

END = blocking.END
GROUND = Plane()
SKY0, SKY1 = (.16, .20, .34), (.30, .32, .44)   # Dusk: deep blue overhead, a greyer band low down.
CLOUDS = 0
HAZE_COL = (.42, .46, .58)
HAZE_DIST = 60
HAZE_MAX = .35
TO_LIGHT = (-.3, -.5, .81)     # Soft, high: short shadows towards the facades.
RIM_COL = (.95, .80, .58)      # Warm edge from the shop window behind them.
RIM = .3
SHADOW = .3
SHADOW_TINT = (.9, .94, 1.05)
SAT, TINT = .88, (.97, .99, 1.04)
CHAR_SAT, CHAR_TINT, CHAR_GAIN = .95, (1.0, .99, .98), 1.0
LINE_OF_ACTION = ('vehbi', 'sidar')
