"""Turnaround check for the two leads: a full orbit, then a low and a high camera. Not the scene yet."""
from toonkit.camera import Shots, orbit, push
import config

C = (0.0, 3.2, 0.0)
SHOTS = Shots(config.END)
SHOTS.add(0, 4, orbit(C, 4.6, 0, 360, 0.95, look_height=0.8, hfov=40), 'turnaround orbit')
SHOTS.add(4, 5, push((3.2, 2.2, 0.3), (3.2, 2.3, 0.3), (0, 3.2, 1.0), f0=46), 'low')
SHOTS.add(5, 6, push((2.8, 4.6, 3.0), (2.8, 4.5, 3.0), (0, 3.2, 0.5), f0=46), 'high')
# Expression test: both faces, front, static. One named face every half second.
SHOTS.add(6, 10, push((2.3, 3.2, 1.28), (2.3, 3.2, 1.28), (0, 3.2, 1.22), f0=34), 'expression test')
# Speech test: both faces, front, static, with placeholder mouth timing.
SHOTS.add(10, 14, push((2.25, 3.2, 1.3), (2.25, 3.2, 1.3), (0, 3.2, 1.24), f0=30), 'speech test')
