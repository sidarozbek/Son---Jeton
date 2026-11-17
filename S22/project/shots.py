"""Son Jeton, scene 22. The 1989 street; the river (env.py); D8 and the textbook insert (stamp.py); the sixth token.
The last number of push is the horizontal field of view in degrees. Only toonkit.camera here: Blender loads it."""
from toonkit.camera import Shots, push
import config

SHOTS = Shots(config.END)

# A. Vehbi with the book, the river in front of him: "August 1989. Money can cross the border freely now."
SHOTS.add(0, 4.8, push((4.2, 2.3, 1.6), (4.3, 2.45, 1.6), (5.0, 4.85, 1.1), f0=54, f1=50), 'Vehbi, the book')
# B. High wide over the river: the stamp comes down: D8.
SHOTS.add(4.8, 9.7, push((-1.6, 1.2, 4.0), (-1.2, 1.3, 3.8), (7.0, 3.8, .5), f0=60, f1=58), 'wide, D8')
# C. Low at the river, looking upstream: the glint coming down; Vehbi at the kerb, his hand out; the hop.
SHOTS.add(9.7, 13.3, push((1.4, 2.7, .8), (1.8, 2.8, .85), (5.0, 4.2, .8), (5.1, 4.3, 1.0), f0=58, f1=50), 'the token comes')
# D. Vehbi with the token up to his eyes.
SHOTS.add(13.3, 14.45, push((4.0, 2.75, 1.45), (4.05, 2.85, 1.45), (5.15, 4.42, 1.15), f0=52, f1=50), 'Vehbi, the sixth token')
# E. Sidar, smug again: "I taught you where to look."
SHOTS.add(14.45, config.END, push((6.85, 2.6, 1.45), (6.8, 2.75, 1.45), (6.1, 4.7, 1.3), f0=46, f1=42), 'Sidar, where to look')
