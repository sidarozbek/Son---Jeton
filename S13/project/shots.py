"""Son Jeton, scene 13. Kuş Bankerlik. Long, still shots; no cutting for comedy.
The last number of push is the horizontal field of view in degrees. Only toonkit.camera here: Blender loads it."""
from toonkit.camera import Shots, push
import config

SHOTS = Shots(config.END)

# A. Wide, a little high: the flock lifts and streams out of the street door on the left.
SHOTS.add(0, 5.6, push((3.6, .3, 2.2), (3.6, .35, 2.2), (2.6, 4.2, 1.9), f0=72), 'wide, the flock leaves')
# B. Slow move along the queue, from beside the shut window: their faces; they stand there.
SHOTS.add(5.6, 9.7, push((4.05, 5.15, 1.5), (4.0, 5.1, 1.48), (2.75, 3.4, 1.3), (2.6, 2.8, 1.25), f0=56, f1=54), 'the queue, still')
# C. Wide and still: the sign swings on one hook and falls. Then nothing.
SHOTS.add(9.7, config.END, push((3.2, .25, 1.8), (3.2, .28, 1.8), (3.0, 4.8, 1.6), f0=64), 'wide, the sign')
