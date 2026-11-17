"""Son Jeton, scene 16. The customs post on the quay; the ships are drawn in env.py.
The last number of push is the horizontal field of view in degrees. Only toonkit.camera here: Blender loads it."""
from toonkit.camera import Shots, push
import config

SHOTS = Shots(config.END)

# A. Wide: the officer, the cabinet, Sidar and Vehbi; the stamp; the first ship out of the drawer and into the sea.
SHOTS.add(0, 3.85, push((-3.4, -3.6, 2.7), (-3.7, -3.3, 2.8), (-8.0, 2.2, .9), (-7.4, 3.2, .7), f0=64, f1=66), 'wide, the first ship')
# B. Sidar, proud, the new ship behind him: "See? One stamp, one ship."
SHOTS.add(3.85, 6.2, push((-6.7, -.95, 1.5), (-6.75, -.7, 1.5), (-7.6, 1.5, 1.35), f0=54, f1=50), 'Sidar, one stamp one ship')
# C. Vehbi, deadpan: "It came out of a filing cabinet."  Then wide: the second ship comes out of it and lands.
SHOTS.add(6.2, 8.6, push((-8.2, -.27, 1.5), (-8.1, -.2, 1.5), (-6.1, .7, 1.35), f0=48, f1=44), 'Vehbi, filing cabinet')
SHOTS.add(8.6, 9.95, push((-4.2, -3.0, 2.4), (-4.4, -2.8, 2.45), (-7.6, 3.8, .6), f0=62, f1=60), 'wide, the second ship')
# D. Sidar, genuinely asking: "Where else do ships come from?"
SHOTS.add(9.95, 11.95, push((-6.9, -.6, 1.5), (-6.95, -.45, 1.5), (-7.6, 1.5, 1.4), f0=44, f1=40), 'Sidar, where else')
# E. The third stamp; the drawer opens; a tiny ship peeks out.
SHOTS.add(11.95, config.END, push((-8.0, .6, 1.7), (-8.3, .9, 1.6), (-9.6, 2.2, 1.05), (-9.5, 2.35, 1.12), f0=50, f1=40), 'the drawer')
