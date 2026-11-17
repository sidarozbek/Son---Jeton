"""Scene 05 sound. Placeholder effects from synthesis, tied to the same numbers as the picture; recorded voices."""
import numpy as np

import blocking as B
import room as R

SR = 48000


def score(m, cfg):
    # A quiet shop: the bulb's hum, the street faint through the glass.
    m.bed(wind=.006, hum=.01, hum_f=(50, 100), duck=[(B.L2, B.L2 + 7.0, .7)])
    # The door bell, still ringing from their coming in: a few bright strikes dying away.
    for k, d in enumerate((0, .16, .34, .55)):
        m.add(m.tick(2900 - 120 * k, .12), R.BELL + d, .07 * (.6 ** k))
        m.add(m.tick(4350 - 160 * k, .08), R.BELL + d + .01, .03 * (.6 ** k))
    # The grocer turns (cloth), and each card flips: a cardboard flick.
    m.add(m.whoosh(.35, .2, .6), R.TURN, .02)
    for ts in R.SWAPS:
        m.add(m.tick(1700, .03), ts + .02, .035)
        m.add(m.tick(1300, .03), ts + R.FLIP * .55, .03)
    m.add(m.whoosh(.35, .2, .6), R.TURN_BACK, .02)
    # Voices.
    m.voice('voices/s1.wav', B.L1, 1.0)
    m.voice('voices/v2.wav', B.L2, 1.0)
    m.voice('voices/s3.wav', B.L3, 1.0)
