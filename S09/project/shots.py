"""Son Jeton, scene 09. The street on 12 September 1980. Long, still shots; no cutting for comedy.
The last number of push is the horizontal field of view in degrees. Only toonkit.camera here: Blender loads it."""
from toonkit.camera import Shots, push
import config

SHOTS = Shots(config.END)

# A. Very wide and still: the empty street, shutters down; the two of them small on the sidewalk.
SHOTS.add(0, 4.6, push((6.5, -4.5, 2.3), (6.5, -4.35, 2.28), (6.2, 5.0, 1.6), f0=58), 'wide, the empty street')
# B. Vehbi, looking along the empty street.
SHOTS.add(4.6, 6.6, push((5.3, 2.3, 1.36), (5.28, 2.4, 1.36), (4.6, 4.75, 1.22), f0=34), 'Vehbi, the street')
# C. Sidar walks to the payphone on the wall; Vehbi a few steps behind.
SHOTS.add(6.6, 8.6, push((6.6, .8, 1.55), (6.8, .9, 1.55), (7.4, 5.0, 1.2), (8.0, 5.3, 1.2), f0=52), 'the walk to the phone')
# D. Sidar at the phone with the third token. Not a word.
SHOTS.add(8.6, 10.75, push((10.7, 5.15, 1.45), (10.62, 5.17, 1.45), (8.0, 5.55, 1.25), f0=50, f1=48), 'Sidar, the third token')
# E. Wide; the stamp comes down quietly: D3. The clipping holds to the end.
SHOTS.add(10.75, config.END, push((7.0, .9, 1.6), (7.0, .95, 1.6), (7.7, 5.2, 1.3), f0=56), 'wide, D3')
