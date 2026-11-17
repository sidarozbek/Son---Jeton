"""Son Jeton, scene 04. The line runs Vehbi (left) to Sidar (right), as at the payphone; cameras stay in the road (low y).
The last number of push is the horizontal field of view in degrees: bigger is wider.
Only toonkit.camera here: Blender loads it."""
from toonkit.camera import Shots, push
import config

SHOTS = Shots(config.END)

# A. The folded sheet opens into the street; hold wide as they come to.
SHOTS.add(0, 3.25, push((5.95, -2.2, 1.7), (5.95, -1.7, 1.62), (5.95, 5.1, 1.5), f0=52, f1=50), 'wide, the street opens')
# B. Sidar shakes the four tokens: "Four tokens left. Don't make me waste them."
SHOTS.add(3.25, 5.85, push((4.6, .9, 1.42), (4.65, 1.1, 1.42), (6.35, 4.85, 1.12), f0=33, f1=32), 'Sidar, four tokens')
# C. Vehbi checks his watch: "My exam starts at nine."
SHOTS.add(5.85, 8.35, push((7.3, .9, 1.4), (7.25, 1.1, 1.4), (5.5, 4.95, 1.1), f0=33, f1=32), 'Vehbi, the watch')
# D. Sidar: "Nine o'clock. Which year?"
SHOTS.add(8.35, 10.75, push((4.3, 1.45, 1.45), (4.35, 1.65, 1.44), (6.4, 4.85, 1.15), f0=28, f1=27), 'Sidar, which year')
# E. INSERT: the calendar in the grocer's window.
SHOTS.add(10.75, 11.75, push((4.83, 4.95, 1.5), (4.83, 5.08, 1.5), (4.83, 6.0, 1.5), f0=42, f1=40), 'insert, the calendar')
# F. Vehbi: "January twenty-fourth, nineteen eighty."
SHOTS.add(11.75, 14.55, push((7.05, 1.6, 1.38), (7.0, 1.8, 1.38), (5.48, 4.95, 1.16), f0=28, f1=27), 'Vehbi, the date')
# G. Wide two-shot: "…Lucky guess."  Sidar turns to the street.
SHOTS.add(14.55, config.END, push((5.95, -.6, 1.5), (5.95, -.45, 1.5), (5.95, 4.9, 1.1), f0=48), 'wide, lucky guess')
