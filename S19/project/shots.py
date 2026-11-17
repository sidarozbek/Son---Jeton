"""Son Jeton, scene 19. Sidar on the deck of ship A, Vehbi on the quay. D7; invoices rain out of the containers.
The last number of push is the horizontal field of view in degrees. Only toonkit.camera here: Blender loads it."""
from toonkit.camera import Shots, push
import config

SHOTS = Shots(config.END)

# A. Wide from along the quay: Sidar on the deck, Vehbi below. The stamp comes down: D7.
SHOTS.add(0, 5.6, push((-3.4, -3.6, 2.7), (-3.6, -3.4, 2.75), (-7.0, 3.6, 1.0), f0=60, f1=58), 'wide, D7')
# B. Two-shot along the quay: Vehbi counting; the lids swing open; the invoices burst out and rain; the catch.
SHOTS.add(5.6, 10.65, push((-2.0, 4.3, 2.9), (-2.2, 4.25, 3.0), (-7.2, 4.6, 1.4), (-7.2, 4.6, 1.6), f0=60, f1=66), 'two-shot, the invoices')
# C. Sidar on the deck, the invoice up high: "Told you!"
SHOTS.add(10.65, 11.5, push((-5.3, 1.35, 1.75), (-5.35, 1.45, 1.75), (-6.45, 5.0, 2.0), f0=46, f1=44), 'Sidar, told you')
# D. Vehbi, invoices still falling: "You said the ships were full."
SHOTS.add(11.5, 13.55, push((-5.0, 3.85, 1.6), (-5.1, 3.8, 1.6), (-6.6, 2.6, 1.3), f0=46, f1=42), 'Vehbi, full')
# E. Sidar: "Of invoices!"
SHOTS.add(13.55, config.END, push((-5.3, 1.35, 1.75), (-5.4, 1.6, 1.8), (-6.45, 5.0, 2.0), f0=48, f1=46), 'Sidar, of invoices')
