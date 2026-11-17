"""Son Jeton, scene 12. Kuş Bankerlik: the chalkboard on the right, the queue stepped back on the left, the teller window
in the middle of the back wall. The last number of push is the horizontal field of view in degrees.
Only toonkit.camera here: Blender loads it."""
from toonkit.camera import Shots, push
import config

SHOTS = Shots(config.END)

# A. Vehbi at the chalkboard: "Every month needs more new customers than the last..."
SHOTS.add(0, 3.6, push((3.6, 1.0, 1.5), (3.7, 1.15, 1.5), (4.45, 3.7, 1.3), f0=56, f1=52), 'Vehbi at the board')
# B. INSERT: the board; his finger taps the X: "Here, it runs out."
SHOTS.add(3.6, 6.3, push((4.95, 2.7, 1.3), (5.0, 2.85, 1.32), (4.85, 3.9, 1.3), f0=50, f1=46), 'the board, the X')
# C. Sidar, hands spread: "I built this place. With my own hands."  The office behind him.
SHOTS.add(6.3, 9.7, push((2.9, .7, 1.45), (2.95, .85, 1.45), (3.35, 2.75, 1.4), f0=48, f1=46), 'Sidar, I built this')
# D. At the window, from the side: Vehbi tugging, "Then help me pull."; Sidar grabs on; they tug; POP.
SHOTS.add(9.7, config.END, push((5.75, 5.05, 1.4), (5.7, 5.0, 1.4), (2.85, 4.75, 1.2), f0=44, f1=42), 'the tug')
