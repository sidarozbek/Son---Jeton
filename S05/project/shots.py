"""Son Jeton, scene 05. The line runs Vehbi (left) to Sidar (right), 1.8 m apart at the counter; the grocer behind the
counter between them, a little to Vehbi's side, the price cards on the shelf to his right. Cameras stay at the front of
the shop. The last number of push is the horizontal field of view in degrees. Only toonkit.camera here: Blender loads it."""
from toonkit.camera import Shots, push
import config

SHOTS = Shots(config.END)

# A. Wide: inside the grocer's, the bell still ringing; the grocer looks up.
SHOTS.add(0, 1.0, push((2.5, .15, 1.75), (2.5, .25, 1.72), (2.5, 3.6, 1.15), f0=66), 'wide, the grocer')
# B. Sidar leans in: "Tonight, your money shrinks."  The grocer behind, to the left.
SHOTS.add(1.0, 2.9, push((2.8, .15, 1.42), (2.82, .3, 1.42), (3.15, 3.0, 1.2), f0=46, f1=44), 'Sidar, tonight')
# C. Vehbi recites, eyes shut; behind him the grocer turns his back and starts on the cards.
SHOTS.add(2.9, 6.85, push((2.25, .15, 1.42), (2.23, .28, 1.42), (1.85, 3.4, 1.22), f0=46, f1=44), 'Vehbi, the definition')
# D. Sidar's eyes go past Vehbi to the grocer.
SHOTS.add(6.85, 7.85, push((2.95, .45, 1.42), (2.97, .55, 1.42), (3.3, 2.6, 1.22), f0=50, f1=48), 'Sidar, watching the grocer')
# E. Closer on Vehbi and the cards: the third one flips; the grocer turns round.
SHOTS.add(7.85, 10.45, push((2.1, .7, 1.42), (2.1, .82, 1.42), (2.05, 3.8, 1.25), f0=44, f1=42), 'Vehbi and the cards')
# F. Wide three-shot: "He's read the same book."
SHOTS.add(10.45, 12.25, push((2.5, .15, 1.7), (2.5, .28, 1.68), (2.5, 3.3, 1.15), f0=60, f1=58), 'three-shot, same book')
# G. Vehbi opens his eyes and looks round at the grocer, who smiles.
SHOTS.add(12.25, config.END, push((2.4, .6, 1.42), (2.38, .7, 1.42), (1.8, 3.4, 1.3), f0=40), 'Vehbi and the grocer')
