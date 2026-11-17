"""Scene 11 sound. Placeholder effects from synthesis, tied to the same numbers as the picture; recorded voices."""
import numpy as np

import blocking as B
import room as R

SR = 48000


def score(m, cfg):
    m.bed(wind=.004, hum=.008, hum_f=(60, 120), duck=[(R.STAMP[1], cfg.END, .5)])
    # The coins turn into birds: a clink, then a flutter, one by one; then the flock's wingbeats and the odd chirp.
    for i in range(5):
        t = R.HATCH[0] + i * (R.HATCH[1] - R.HATCH[0]) / 4
        m.add(m.tick(3600, .04), t, .04)
        m.add(m.whoosh(.35, .5, .95), t + .05, .03)
    for t in np.arange(2.5, R.STAMP[0], .21):
        m.add(m.whoosh(.12, .55, .95), float(t), .008 + .0015 * min(t, 9))
    for t in (3.4, 4.9, 6.8, 8.6):
        m.add(m.tick(4200, .05), t, .012)
        m.add(m.tick(4700, .04), t + .07, .01)
    # The board flaps; the coins handed over.
    for t in R.RATE_TIMES:
        if t > 0:
            for k in range(5):
                m.add(m.tick(1900 + 150 * (k % 3), .02), t + k * .025, .03)
    for a, b in R.CARRIES:
        m.add(m.tick(3400, .04), a, .03)
        m.add(m.tick(3400, .04), b, .03)
    # The stamp.
    m.add(m.whoosh(.35, .3, .9), R.STAMP[0], .06)
    m.add(m.thud(70, .18, .6), R.STAMP[1], .3)
    m.add(m.thud(140, .06, .9), R.STAMP[1], .12)
    m.add(m.whoosh(.5, .4, .95), R.CLIP[0], .05)
    # Voices.
    m.voice('voices/v1.wav', B.L1, 1.0)
    m.voice('voices/s2.wav', B.L2, 1.0)
    m.voice('voices/v3.wav', B.L3, 1.0)
