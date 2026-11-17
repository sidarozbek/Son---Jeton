"""Son Jeton, scene 17. The customs post; stamp D6 and the textbook insert from stamp.py.
The last number of push is the horizontal field of view in degrees. Only toonkit.camera here: Blender loads it."""
from toonkit.camera import Shots, push
import config

SHOTS = Shots(config.END)

# A. Wide: the post, the two paper ships, the tiny one in the drawer. The stamp comes down: D6.
SHOTS.add(0, 5.7, push((-4.2, -3.0, 2.4), (-4.3, -2.9, 2.45), (-7.6, 3.4, .7), f0=62, f1=60), 'wide, D6')
# B. Vehbi with the book: "Tax refunds and export credits. It's in the book."  (The page insert cuts in over it.)
SHOTS.add(5.7, 10.2, push((-8.3, -.35, 1.45), (-8.15, -.25, 1.45), (-6.1, .7, 1.05), f0=56, f1=50), 'Vehbi, the book')
# C. Sidar, proud, the ships behind him: "I put these ships on paper."
SHOTS.add(10.2, 12.75, push((-6.7, -.95, 1.5), (-6.75, -.7, 1.5), (-7.6, 1.5, 1.35), f0=54, f1=50), 'Sidar, on paper')
# D. Vehbi, flat: "That's the problem."
SHOTS.add(12.75, config.END, push((-8.0, -.1, 1.45), (-7.9, -.03, 1.45), (-6.1, .7, 1.2), f0=44, f1=42), 'Vehbi, the problem')
