"""Son Jeton, scene 08. The grocer's: Vehbi starts left, Sidar right; both end at the payphone on the right wall.
The stamp and the clipping are drawn over the picture in stamp.py. The last number of push is the horizontal field of
view in degrees. Only toonkit.camera here: Blender loads it."""
from toonkit.camera import Shots, push
import config

SHOTS = Shots(config.END)

# A. Wide: the cards keep swelling, three giant ones shoot up from the floor; the grocer squeezed. "To the phone! Run!"
SHOTS.add(0, 2.6, push((2.5, .15, 1.75), (2.5, .25, 1.72), (2.6, 3.2, 1.3), f0=66), 'wide, the overflow')
# B. Sidar runs for the phone on the right wall.
SHOTS.add(2.6, 3.8, push((2.7, .2, 1.5), (2.75, .25, 1.5), (4.3, 1.9, 1.15), (4.4, 1.3, 1.15), f0=58), 'Sidar, the run')
# C. Vehbi weaves between the giant cards: "Excuse me. Excuse me. Excuse me."
SHOTS.add(3.8, 6.4, push((2.6, .15, 1.55), (2.8, .15, 1.55), (2.0, 1.9, 1.1), (3.4, 1.5, 1.1), f0=60, f1=58), 'Vehbi, excuse me')
# D. At the phone: the card on Sidar's nose, "Token two.", the token into the slot.
SHOTS.add(6.4, 8.35, push((2.9, .15, 1.45), (3.0, .2, 1.45), (4.3, 1.2, 1.2), f0=58, f1=54), 'Sidar, token two')
# E. Wide as the line crosses; the stamp comes down: D2. The clipping holds to the end.
SHOTS.add(8.35, config.END, push((3.2, .2, 1.6), (3.2, .25, 1.6), (3.9, 1.6, 1.25), f0=62), 'wide, D2')
