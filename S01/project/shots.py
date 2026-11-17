"""Son Jeton, scene 1. The line of action runs between Sidar and Vehbi; cameras stay on the front (low y, +x) side
until the push, then on the front side of the new line inside the room. Only toonkit.camera here: Blender loads it."""
import math

from toonkit.camera import Shots, follow, push
import blocking as B
import config

SHOTS = Shots(config.END)

# A. The room, the lamp, the student who won't look up. A slow push in while the knocks land.
SHOTS.add(0, 2.3, push((2.95, .35, 1.7), (2.55, .8, 1.55), (.75, 2.4, 1.05), (.8, 2.4, 1.08), f0=60, f1=52), 'room, slow push')
# B. Corridor, low: the landlord pounding. Power, and a little unease.
SHOTS.add(2.3, 4.36, push((5.3, 4.56, .42), (5.15, 4.58, .45), (3.2, 4.8, 1.3), f0=42, roll=2.5), 'corridor low on Sidar, beside the door')


def walk_cam(t, u):
    # Pans with him from one spot by the bed's foot, drifting a little after him; the look arrives late.
    # Standing on the latch side of the swing, so the opening door never comes between the lens and him.
    import numpy as np
    k = u * u * (3 - 2 * u)
    pos = np.array((1.6 + .35 * k, .8 + .45 * k, 1.58))
    s_ = np.array(B.pos('vehbi', max(t - .2, 0), 1.15))
    return pos, s_, 54, 0


# C. He sighs, pushes his glasses up, walks to the door and opens it a crack.
SHOTS.add(4.36, 7.25, walk_cam, 'follow him to the door')
# D. Over Sidar's shoulder, into the crack: Vehbi reads clause seven. A slow push to his face.
SHOTS.add(7.25, 11.75, push((2.72, 5.85, 1.5), (2.7, 5.65, 1.48), (2.62, 3.95, 1.34), (2.6, 3.95, 1.36), f0=34, f1=29), 'over Sidar into the crack')
# E. Reverse from inside, low: Sidar fills the crack. "I'm giving notice!"
SHOTS.add(11.75, 13.4, push((2.72, 2.98, .95), (2.73, 3.04, .95), (3.15, 4.78, 1.25), f0=36, roll=-2), 'low on Sidar through the crack')
# F. Vehbi close, from the corridor side: "In writing." Glasses first.
SHOTS.add(13.4, 14.8, push((2.76, 5.45, 1.4), (2.75, 5.4, 1.4), (2.6, 3.95, 1.36), f0=22), 'Vehbi close')
# G. Wide from the front of the room: the door flies, the books skid, he walks in. Cut on the shove.
SHOTS.add(14.8, 16.65, push((1.1, .45, 1.5), (1.25, .7, 1.45), (2.8, 3.9, 1.0), (2.85, 3.7, 1.0), f0=58, f1=54), 'wide, the push')
# H. Low on Sidar inside: "I'm here." Chest out, the notice delivered in person.
SHOTS.add(16.65, 18.15, push((1.35, 1.95, .55), (1.45, 2.05, .56), (2.75, 3.52, 1.1), f0=44, roll=1.5), "low on Sidar, 'I'm here'")
# J. Vehbi: a long, slow look at him. Push to the eyes.
SHOTS.add(18.15, 20.35, push((3.15, 2.85, 1.38), (2.95, 3.05, 1.38), (2.2, 3.72, 1.36), f0=40, f1=33), 'push in on Vehbi')


def crane(t, u):
    # Up and back to the size of the problem: two small people in a lamp-lit room.
    k = u * u * (3 - 2 * u)
    pos = (1.6 - .4 * k, .6 - .2 * k, 1.6 + 0.95 * k)
    look = (2.55, 3.55, .95 - .25 * k)
    return pos, look, 50 + 8 * k, 0


# K. Crane up.
SHOTS.add(20.35, config.END, crane, 'crane up')
