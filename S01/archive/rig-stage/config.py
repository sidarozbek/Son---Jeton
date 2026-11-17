"""Everything not listed here keeps its default from engine/toonkit/settings.py."""
from toonkit.camera import Plane, sun_dir

END = 14.0
GROUND = Plane()              # Flat floor. A street on a hill: Plane(sy=.05).
SKY0, SKY1 = (.30, .28, .25), (.34, .31, .27)
CLOUDS = 0                    # Interior: no sky.
HAZE_COL = (.42, .38, .32)
HAZE_DIST = 300
HAZE_MAX = .25
TO_LIGHT = sun_dir(35, 30)    # Same numbers as S.sun in setdef.py.
RIM_COL = (.95, .86, .70)
RIM = .22
SHADOW = .5
SAT, TINT = .92, (1.0, .985, .95)
CHAR_SAT, CHAR_TINT, CHAR_GAIN = .96, (1.0, .985, .96), .98
LINE_OF_ACTION = ('sidar', 'vehbi')   # The lint warns when a cut crosses the line between these two.
