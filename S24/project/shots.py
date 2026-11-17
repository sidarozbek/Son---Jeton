"""Son Jeton, scene 24. The corridor after the exam. Black from room.BLACK (env.post).
The last number of push is the horizontal field of view in degrees. Only toonkit.camera here: Blender loads it."""
from toonkit.camera import Shots, push
import config

SHOTS = Shots(config.END)

# A. Down the corridor: the door, Vehbi coming out and towards us; the friend falls in beside him.
SHOTS.add(0, 2.9, push((1.6, .8, 1.7), (1.55, 1.3, 1.65), (1.2, 8.5, 1.1), (1.3, 7.5, 1.1), f0=50, f1=46), 'the corridor')
# B. The two of them, walking up to us: "Where were you last night?"
SHOTS.add(2.9, 4.4, push((1.6, 2.6, 1.5), (1.6, 2.9, 1.5), (1.5, 5.8, 1.3), f0=46, f1=44), 'the question')
# C. Vehbi, close and slow: he stops; he thinks; "...I don't know."  Then black.
SHOTS.add(4.4, config.END, push((.85, 3.4, 1.45), (.92, 3.75, 1.45), (1.1, 5.4, 1.3), f0=40, f1=36), 'I don\'t know')
