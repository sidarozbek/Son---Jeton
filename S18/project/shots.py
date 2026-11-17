"""Son Jeton, scene 18. The customs post; Sidar boards ship A on paper. Ships drawn in env.py.
The last number of push is the horizontal field of view in degrees. Only toonkit.camera here: Blender loads it."""
from toonkit.camera import Shots, push
import config

SHOTS = Shots(config.END)

# A. Wide: Sidar to the gangway and up onto the see-through deck; Vehbi round the counter; the officer writes.
SHOTS.add(0, 4.5, push((-1.2, 2.0, 2.4), (-1.4, 2.2, 2.4), (-7.2, 2.6, .8), (-7.4, 3.0, .9), f0=64, f1=62), 'wide, all aboard')
# B. Vehbi over the ledger, reading it out.
SHOTS.add(4.5, 11.25, push((-8.4, -.5, 1.65), (-8.5, -.25, 1.6), (-8.95, 2.08, 1.15), (-8.95, 2.08, 1.25), f0=50, f1=42), 'Vehbi, the ledger')
# C. Sidar on the deck, the sea and the hills behind: "Germany! Finally..."  The wait. "...Are we moving?"
SHOTS.add(11.25, 16.85, push((-5.3, 1.3, 1.7), (-5.4, 1.6, 1.8), (-6.0, 4.97, 1.9), f0=50, f1=46), 'Sidar aboard')
# D. Vehbi, dry: "On paper, you've arrived."
SHOTS.add(16.85, config.END, push((-6.4, 2.35, 1.55), (-6.55, 2.3, 1.55), (-8.95, 2.08, 1.3), f0=42, f1=40), 'Vehbi, arrived')
