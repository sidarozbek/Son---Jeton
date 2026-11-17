"""Son Jeton, scene 03. Room (0-6.9): the line runs Sidar (left) to Vehbi (right); cameras stay on the front side.
Basement (6.9-18.2): Sidar right, Vehbi left at the phone; cameras on the front (low-y) side.
Only toonkit.camera here: Blender loads it."""
from toonkit.camera import Shots, push
import config

SHOTS = Shots(config.END)

# ---- the room
# A. Sidar turns from the door to him: "Your phone line is broken."
SHOTS.add(0, 3.72, push((3.25, 1.85, 1.3), (3.18, 1.95, 1.3), (2.2, 3.72, 1.05), f0=48, f1=44), 'Sidar, the line is broken')
# B. Vehbi: "I don't have a phone."
SHOTS.add(3.72, 5.0, push((1.85, 2.4, 1.32), (1.92, 2.5, 1.32), (2.98, 3.52, 1.3), f0=36), 'Vehbi, no phone')
# C. Wide: "Downstairs. Come." He is already out of the door; Vehbi follows.
SHOTS.add(5.0, 6.9, push((1.35, .55, 1.75), (1.5, .75, 1.7), (2.75, 3.95, 1.0), (2.9, 4.2, 1.0), f0=56, f1=52), 'wide, out of the door')

# ---- the basement
# D. Establishing: the bare bulb swinging, the boiler, the stairs; they come off the stairs and cross to the phone.
SHOTS.add(6.9, 9.05, push((20.55, .55, 1.15), (20.75, .8, 1.12), (23.2, 4.1, 1.2), (22.8, 4.4, 1.2), f0=64, f1=56), 'basement, establishing')
# E. Sidar lifts the receiver and holds it out: "It's for you."
SHOTS.add(9.05, 10.5, push((21.75, 2.75, 1.3), (21.8, 2.82, 1.3), (23.0, 4.22, 1.15), f0=42), 'Sidar, it is for you')
# F. INSERT: the token into the slot.
SHOTS.add(10.5, 11.75, push((22.98, 4.2, 1.5), (22.94, 4.26, 1.5), (22.66, 4.84, 1.42), f0=44, f1=38), 'insert, the token')
# G. Vehbi, receiver to his ear: "Hello?" The line crosses; the bulb stutters.
SHOTS.add(11.75, 13.7, push((23.05, 3.0, 1.38), (22.95, 3.12, 1.38), (22.12, 4.45, 1.32), f0=40, f1=34), 'Vehbi, hello')
# H. Wide two-shot as the basement folds like paper.
SHOTS.add(13.7, config.END, push((22.55, 1.6, 1.5), (22.55, 1.75, 1.5), (22.55, 4.35, 1.2), f0=54), 'wide, the fold')
