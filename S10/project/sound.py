"""Scene 10 sound. Placeholder effects from synthesis, tied to the same numbers as the picture; recorded voices."""
import numpy as np

import blocking as B
import room as R

SR = 48000


def score(m, cfg):
    # An office: a low murmur of the queue (band noise), a ticking wall clock is NOT used (it's stopped).
    m.bed(wind=.004, hum=.008, hum_f=(60, 120), duck=[(B.L1, B.L3 + 1.0, .7)])
    # The board flipping: a fast clatter of flaps each time.
    for t in R.RATE_TIMES[1:]:
        for k in range(5):
            m.add(m.tick(1900 + 150 * (k % 3), .02), t + k * .025, .03)
    # Footsteps at the door as each newcomer walks in; the street door's creak.
    for t0 in R.ARRIVALS:
        if t0 >= 0:
            m.add(m.whoosh(.4, .1, .3), t0, .015)
            m.steps(t0, t0 + R.WALK_IN, .45, f=120, g=.03)
    m.steps(B.S_WALK[0], B.S_WALK[1], .35, f=110, g=.05)
    # The tokens slapped on the counter.
    m.add(m.thud(300, .03, .9), R.TOKENS_DOWN, .08)
    m.add(m.tick(3600, .05), R.TOKENS_DOWN + .01, .06)
    m.add(m.tick(3200, .04), R.TOKENS_DOWN + .05, .04)
    # Voices.
    m.voice('voices/s1.wav', B.L1, 1.0)
    m.voice('voices/v2.wav', B.L2, 1.0)
    m.voice('voices/s3.wav', B.L3, 1.0)
