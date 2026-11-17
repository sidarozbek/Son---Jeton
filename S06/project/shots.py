"""Son Jeton, scene 06. The same shop and line as Scene 05: Vehbi left, Sidar right, the grocer behind the counter.
The last number of push is the horizontal field of view in degrees. Only toonkit.camera here: Blender loads it."""
from toonkit.camera import Shots, push
import config

SHOTS = Shots(config.END)

# A. INSERT: the wall clock on the left wall; the minute hand ticks onto twelve.
SHOTS.add(0, 1.9, push((1.25, 3.0, 2.15), (1.1, 3.0, 2.15), (0, 3.0, 2.2), f0=36, f1=34), 'insert, midnight')
# B. Wide: the shop at midnight. The cards swell; Vehbi takes out a banknote.
SHOTS.add(1.9, 4.5, push((2.5, .15, 1.75), (2.5, .35, 1.7), (2.5, 3.6, 1.3), f0=64, f1=60), 'wide, the cards swell')
# C. Sidar, triumphant: "See? SEE?!"  The swollen cards behind him.
SHOTS.add(4.5, 6.0, push((2.8, .2, 1.4), (2.85, .32, 1.4), (3.15, 3.0, 1.3), f0=46, f1=44), 'Sidar, see')
# D. Vehbi holds up the tiny note: "Money doesn't shrink. Prices rise."
SHOTS.add(6.0, 8.5, push((2.25, .7, 1.3), (2.22, .82, 1.3), (1.7, 2.6, 1.15), f0=46, f1=44), 'Vehbi, the tiny note')
# E. Sidar, at once: "Same thing!"  Wider, with the grocer and the giant cards.
SHOTS.add(8.5, config.END, push((2.95, .35, 1.5), (2.95, .45, 1.5), (3.0, 3.0, 1.35), f0=56, f1=54), 'Sidar, same thing')
