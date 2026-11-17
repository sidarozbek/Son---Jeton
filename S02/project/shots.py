"""Son Jeton, scene 02. Before the tug the line runs Sidar (right) to Vehbi (left); every camera stays on the front
(low y) side of it. The tug turns them half a circle, so after it Sidar is on the left; the front side stays the front.
Only toonkit.camera here: Blender loads it."""
from toonkit.camera import Shots, push
import config

SHOTS = Shots(config.END)

# A. Low two-shot, slow push toward Sidar as he remembers. He points up at "that room".
SHOTS.add(0, 4.3, push((1.25, 1.35, .75), (1.45, 1.6, .8), (2.62, 3.6, 1.12), (2.75, 3.56, 1.2), f0=48, f1=42, roll=1.5), 'low two-shot, the memory')
# B. Over Sidar's right shoulder onto Vehbi: the book turned to him. "That's not what it says."
SHOTS.add(4.3, 6.4, push((3.25, 1.95, 1.38), (3.2, 2.02, 1.37), (2.38, 3.7, 1.22), f0=38, f1=34), 'Vehbi three-quarter, the book turned to Sidar')
# C. Sidar close, from Vehbi's side: he reads, the anger arrives, "Then the book is wrong!", the lunge.
SHOTS.add(6.4, 8.6, push((1.15, 2.45, 1.15), (1.22, 2.5, 1.15), (2.98, 3.52, 1.15), f0=46, f1=50), 'Sidar close, the lunge')
# D. Wide, high, from the front of the room: the tug of war, half a circle around the book.
SHOTS.add(8.6, 12.05, push((1.5, .55, 1.95), (1.65, .8, 1.85), (2.6, 3.62, .9), f0=52, f1=48), 'wide, the tug of war')
# E. Low by the floor: the contract slips out and drifts down between their feet.
SHOTS.add(12.05, 13.4, push((2.15, 2.1, .38), (2.18, 2.16, .36), (2.6, 3.4, .45), (2.64, 3.3, .2), f0=46), 'low, the contract falls')
# F. Sidar lets go and fixes his tie, as if nothing happened.
SHOTS.add(13.4, 15.4, push((3.25, 1.85, 1.3), (3.2, 1.93, 1.3), (2.2, 3.72, 1.0), f0=50), 'Sidar, the tie')
# G. Vehbi: down at the contract, then slowly back up at him. Push in.
SHOTS.add(15.4, 17.4, push((1.75, 2.35, 1.32), (1.9, 2.55, 1.32), (2.98, 3.52, 1.32), f0=34, f1=28), 'Vehbi, down then up')
# H. Wide from the bed side: Sidar surveys the room, not looking at him; his eyes go to the open door.
SHOTS.add(17.4, config.END, push((3.75, 1.45, 1.75), (3.7, 1.55, 1.72), (2.45, 3.75, 1.0), f0=50, f1=46), 'wide, Sidar eyes the door')
