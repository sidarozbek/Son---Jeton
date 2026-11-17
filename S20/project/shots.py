"""Son Jeton, scene 20. The payphone on the harbour office's wall; the fold is a whole-picture effect in fold.py.
The last number of push is the horizontal field of view in degrees. Only toonkit.camera here: Blender loads it."""
from toonkit.camera import Shots, push
import config

SHOTS = Shots(config.END)

# A. Sidar at the phone, the token held up: "Last one. Token five."  It goes see-through.
SHOTS.add(0, 4.15, push((-11.0, .9, 1.55), (-11.15, .85, 1.55), (-13.35, .2, 1.3), f0=54, f1=48), 'Sidar, token five')
# B. Vehbi: "It's... see-through."
SHOTS.add(4.15, 5.95, push((-12.9, 1.5, 1.5), (-12.88, 1.35, 1.5), (-12.5, -.7, 1.3), f0=44, f1=42), 'Vehbi, see-through')
# C. Sidar, the phone on the wall beside him: "It's a perfectly good tok—"  Into the slot.
SHOTS.add(5.95, 8.2, push((-10.8, -1.0, 1.75), (-10.95, -.9, 1.75), (-13.6, .25, 1.2), f0=60, f1=56), 'Sidar, the slot')
# D. Both at the phone, the officer beyond: the crackle; the fold.
SHOTS.add(8.2, config.END, push((-9.3, -3.1, 3.0), (-9.35, -3.05, 3.0), (-13.1, .1, .9), f0=54, f1=54), 'the crackle, the fold')
