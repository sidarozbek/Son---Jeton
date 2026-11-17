"""Son Jeton, scene 23. The exam hall; the question inserts and the stamp flashes are drawn in env.post.
The last number of push is the horizontal field of view in degrees. Only toonkit.camera here: Blender loads it."""
from toonkit.camera import Shots, push
import config

SHOTS = Shots(config.END)

# A. High from the back corner: rows of bent heads; the proctor; the clock.
SHOTS.add(0, 2.2, push((8.4, .6, 2.9), (8.2, .9, 2.8), (3.6, 7.6, .9), f0=62, f1=60), 'wide, the hall')
# B. Vehbi from the front left, bent over his sheet, whispering. (The inserts and flashes cut in over this.)
SHOTS.add(2.2, 31.2, push((3.3, 8.4, 1.25), (3.45, 8.2, 1.25), (4.45, 6.1, .75), (4.45, 6.1, .8), f0=50, f1=40), 'Vehbi, answering')
# C. Pen down: wide again, from the front.
SHOTS.add(31.2, config.END, push((4.4, 9.6, 1.9), (4.4, 9.7, 2.1), (4.45, 5.6, .7), f0=58, f1=64), 'pen down')
