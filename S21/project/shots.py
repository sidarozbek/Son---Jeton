"""Son Jeton, scene 21. August 1989: the street, the river of money (env.py), the unfold (fold.py).
The last number of push is the horizontal field of view in degrees. Only toonkit.camera here: Blender loads it."""
from toonkit.camera import Shots, push
import config

SHOTS = Shots(config.END)

# A. High, down the street: the river of money flowing towards us; the two of them small at its edge.
SHOTS.add(0, 4.9, push((-2.4, 1.0, 4.4), (-1.6, 1.2, 4.0), (8.0, 3.6, .4), (8.0, 3.8, .6), f0=62, f1=58), 'wide, the river')
# B. Vehbi, low from the river's edge, the notes going by in front: "No tokens. The exam's in ten hours."
SHOTS.add(4.9, 8.3, push((4.35, 2.4, 1.55), (4.4, 2.55, 1.55), (5.0, 4.6, .95), f0=54, f1=52), 'Vehbi, ten hours')
# C. Sidar, low and slow, the notes going by: "They won't believe me here either."
SHOTS.add(8.3, 11.9, push((6.95, 2.25, 1.6), (6.85, 2.45, 1.55), (6.1, 4.5, 1.0), f0=52, f1=46), 'Sidar, here either')
# D. Crane up and back: two small figures at the edge of a river of money.
SHOTS.add(11.9, config.END, push((5.4, .4, 3.4), (4.6, -2.6, 6.8), (5.6, 4.4, .8), (5.8, 3.0, .2), f0=56, f1=66), 'wide, alone')
