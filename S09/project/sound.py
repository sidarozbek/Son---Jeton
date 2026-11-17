"""Scene 09 sound: almost nothing. Wind, a far-off bird, the token; a softer stamp. No music."""
import numpy as np

import blocking as B
import room as R

SR = 48000


def score(m, cfg):
    m.bed(wind=.03, hum=0.0, hum_f=(55, 82), duck=[])
    for t in (2.4, 7.1):                                  # A single far-off bird, twice.
        m.add(m.tick(3400, .06), t, .008)
        m.add(m.tick(3100, .05), t + .12, .006)
    m.steps(B.S_WALK[0], B.S_WALK[1], .55, f=100, g=.03)
    m.steps(B.V_WALK[0], B.V_WALK[1], .6, f=140, g=.02)
    m.add(m.tick(3800, .05), R.COIN_IN + .15, .05)
    for i, dt in enumerate((.09, .16, .21)):
        m.add(m.tick(2600 - i * 300, .025), R.COIN_IN + .15 + dt, .025 - i * .006)
    # The stamp, quieter than in Scenes 07-08.
    m.add(m.thud(70, .18, .6), R.STAMP[1], .15)
    m.add(m.whoosh(.5, .4, .95), R.CLIP[0], .03)
