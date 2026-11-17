"""Son Jeton, scene 10. The banker's office: the queue in the middle running to the window; Vehbi left of Sidar on the
right. Cameras at the front. The last number of push is the horizontal field of view in degrees.
Only toonkit.camera here: Blender loads it."""
from toonkit.camera import Shots, push
import config

SHOTS = Shots(config.END)

# A. Wide: the office, the sign, the queue, the board at %30 flipping to %35.
SHOTS.add(0, 2.0, push((3.2, .25, 1.9), (3.2, .4, 1.85), (3.3, 4.6, 1.6), f0=66, f1=64), 'wide, Kuş Bankerlik')
# B. Sidar looking up at the board (from beside it), counting along: "Forty percent! Fifty! Vehbi, look!"
SHOTS.add(2.0, 4.65, push((5.35, 4.7, 1.4), (5.3, 4.6, 1.4), (4.55, 2.5, 1.35), f0=50, f1=48), 'Sidar, forty fifty')
# C. INSERT: the board flips to %60.
SHOTS.add(4.65, 5.25, push((5.2, 4.1, 1.62), (5.2, 4.2, 1.62), (5.2, 5.5, 1.62), f0=40), 'insert, the board')
# D. Vehbi: "Nobody can pay that."  The queue growing behind him.
SHOTS.add(5.25, 7.0, push((5.3, .9, 1.38), (5.25, 1.0, 1.38), (3.6, 2.6, 1.3), f0=44, f1=42), 'Vehbi, nobody can pay')
# E. Wide: Sidar walks past the whole queue to the window.
SHOTS.add(7.0, 8.45, push((4.7, .6, 1.75), (4.6, .8, 1.7), (3.6, 4.4, 1.35), (3.4, 4.8, 1.3), f0=58, f1=54), 'wide, past the queue')
# F. From the right, by the board: Sidar at the window, "Invest them."; the queue turns to look at him; %90.
SHOTS.add(8.45, config.END, push((5.35, 3.75, 1.55), (5.3, 3.8, 1.55), (3.0, 4.2, 1.35), f0=62, f1=60), 'Sidar and the queue, %90')
