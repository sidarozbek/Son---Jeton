"""Son Jeton, scene 07. The same shop and line as Scenes 05-06: Vehbi left, Sidar right, the grocer behind the counter.
The stamp, the clipping and the textbook page are drawn over the picture in stamp.py; the cameras just hold under them.
The last number of push is the horizontal field of view in degrees. Only toonkit.camera here: Blender loads it."""
from toonkit.camera import Shots, push
import config

SHOTS = Shots(config.END)

# A. Wide three-shot; the stamp comes down on it and it turns into a newspaper clipping.
SHOTS.add(0, 5.05, push((2.5, .15, 1.72), (2.5, .2, 1.72), (2.5, 3.4, 1.25), f0=62), 'wide, the stamp')
# B. INSERT: the textbook page (drawn in stamp.py). The camera underneath sits on Vehbi.
SHOTS.add(5.05, 7.4, push((2.25, .7, 1.3), (2.22, .8, 1.3), (1.7, 2.6, 1.15), f0=46), 'insert, the page')
# C. Vehbi holds the open book up to Sidar: "...Same as the book."
SHOTS.add(7.4, 9.4, push((2.25, .55, 1.32), (2.22, .68, 1.32), (1.75, 2.6, 1.15), f0=50, f1=48), 'Vehbi, the book')
# D. Sidar, hand on heart: "Thirty years at the bank..."
SHOTS.add(9.4, 13.4, push((2.85, .3, 1.4), (2.9, .5, 1.4), (3.25, 2.6, 1.25), f0=46, f1=40), 'Sidar, thirty years')
# E. Vehbi: "It's not your stamp."
SHOTS.add(13.4, 14.8, push((2.3, .5, 1.42), (2.28, .6, 1.42), (1.7, 2.6, 1.32), f0=40), 'Vehbi, not your stamp')
# F. Sidar, wider, the grocer and the cards behind: "Whose else would it be?"
SHOTS.add(14.8, config.END, push((2.95, .35, 1.5), (2.95, .42, 1.5), (3.0, 3.0, 1.32), f0=56), 'Sidar, whose else')
