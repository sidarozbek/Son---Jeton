"""Set check: four fixed views of the room before any directing. Replaced in toon-direct."""
from toonkit.camera import Shots, push
import config

SHOTS = Shots(config.END)
SHOTS.add(0, 4, push((2.9, .3, 1.6), (2.9, .3, 1.6), (1.0, 3.4, 1.0), f0=72), 'wide from the front')
SHOTS.add(4, 8, push((3.1, 4.05, 1.45), (3.1, 4.05, 1.45), (.3, 1.7, .95), f0=60), 'from the door to the desk')
SHOTS.add(8, 12, push((-1.9, 5.4, 1.5), (-1.9, 5.4, 1.5), (3.05, 4.4, 1.05), f0=50), 'corridor to the door')
SHOTS.add(12, 20, push((1.4, .3, 1.3), (1.4, .3, 1.3), (3.0, 4.2, .9), f0=64), 'door wide open, books shoved')
