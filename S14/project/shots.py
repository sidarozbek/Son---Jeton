"""Son Jeton, scene 14. Kuş Bankerlik after the fall. The stamp and the clipping are drawn over the picture in stamp.py.
The last number of push is the horizontal field of view in degrees. Only toonkit.camera here: Blender loads it."""
from toonkit.camera import Shots, push
import config

SHOTS = Shots(config.END)

# A. Wide and still: the shut window, the dark board, the sign on the floor, the queue. The stamp comes down: D5.
SHOTS.add(0, 5.9, push((3.2, .25, 1.8), (3.2, .28, 1.8), (3.0, 4.8, 1.55), f0=64), 'wide, D5')
# B. Sidar: "I told you so."
SHOTS.add(5.9, 7.45, push((3.35, .7, 1.45), (3.4, .82, 1.45), (4.75, 2.6, 1.4), f0=44, f1=42), 'Sidar, told you')
# C. Vehbi: "You said you built—"  The phone rings over him.
SHOTS.add(7.45, 9.0, push((5.3, .9, 1.38), (5.25, 1.0, 1.38), (3.6, 2.6, 1.3), f0=44, f1=42), 'Vehbi, cut off')
# D. Sidar to the phone on the left wall: "Phone's ringing. Come."  The fourth token.
SHOTS.add(9.0, config.END, push((2.6, .25, 1.7), (2.2, .35, 1.65), (4.0, 2.2, 1.25), (.8, 3.9, 1.3), f0=60, f1=58), 'to the phone, token four')
