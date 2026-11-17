"""Son Jeton, scene 15. The harbour; the ships are drawn in env.py.
The last number of push is the horizontal field of view in degrees. Only toonkit.camera here: Blender loads it."""
from toonkit.camera import Shots, push
import config

SHOTS = Shots(config.END)

# A. Wide from the land: the quay, the sea, three see-through ships drifting by in silence.
SHOTS.add(0, 2.6, push((-6.5, -3.2, 3.2), (-6.1, -3.0, 3.1), (2.0, 9.0, .4), f0=66, f1=64), 'wide, the harbour')
# B. Sidar to us, the ships behind him: "Ships. Full of goods."
SHOTS.add(2.6, 4.3, push((-.6, -1.3, 1.45), (-.62, -1.0, 1.45), (-.9, 2.7, 1.35), (-.9, 2.7, 1.4), f0=60, f1=57), 'Sidar, full of goods')
# C. Vehbi to the edge; his hand goes into the hull; "Full of what?"
SHOTS.add(4.3, 8.45, push((-.35, .3, 2.05), (-.25, .55, 1.9), (.45, 4.0, 1.0), (.6, 4.2, 1.15), f0=50, f1=34), 'Vehbi, the hand in the hull')
# D. Over Vehbi's shoulder to Sidar: "Goods! Paper goods."
SHOTS.add(8.45, 10.35, push((2.3, 3.5, 1.5), (2.2, 3.45, 1.5), (-1.0, 2.75, 1.2), f0=52, f1=50), 'Sidar, paper goods')
# E. The hand comes out; the ship slides on.
SHOTS.add(10.35, config.END, push((-.4, 1.4, 1.75), (-.55, 1.2, 1.8), (.62, 4.0, 1.1), (.7, 4.2, 1.15), f0=44, f1=48), 'the empty hand')
