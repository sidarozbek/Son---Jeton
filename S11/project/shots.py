"""Son Jeton, scene 11. Kuş Bankerlik, as Scene 10: the queue in the middle; Vehbi left of Sidar on the right.
The last number of push is the horizontal field of view in degrees. Only toonkit.camera here: Blender loads it."""
from toonkit.camera import Shots, push
import config

SHOTS = Shots(config.END)

# A. Wide: the coins on the counter turn into birds and fly up.
SHOTS.add(0, 2.6, push((3.4, .35, 2.55), (3.4, .5, 2.5), (3.0, 5.2, 1.3), (3.0, 5.0, 1.7), f0=58, f1=62), 'wide, coins to birds')
# B. From the right: the whole queue, the flock; a bird carries a coin up the queue. "Look. New money pays the old customers."
SHOTS.add(2.6, 6.0, push((5.4, .8, 1.65), (5.35, .9, 1.7), (2.9, 3.5, 1.65), f0=66, f1=64), 'the queue and the birds')
# C. Sidar, lecturing: "That's called profit."  The flock overhead.
SHOTS.add(6.0, 8.0, push((3.35, .7, 1.45), (3.4, .85, 1.45), (4.75, 2.6, 1.4), f0=46, f1=44), 'Sidar, profit')
# D. Vehbi: "That's called a chain."
SHOTS.add(8.0, 9.8, push((5.3, .9, 1.38), (5.25, 1.0, 1.38), (3.6, 2.6, 1.3), f0=44, f1=42), 'Vehbi, a chain')
# E. Wide: the flock; the stamp comes down: D4. The clipping holds to the end.
SHOTS.add(9.8, config.END, push((3.4, .35, 2.4), (3.4, .4, 2.4), (3.0, 4.6, 1.9), f0=62), 'wide, D4')
