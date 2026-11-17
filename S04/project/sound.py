"""Scene 04 sound. Placeholder effects from synthesis, tied to the same numbers as the picture; recorded voices."""
import numpy as np

import blocking as B
import room as R

SR = 48000


def score(m, cfg):
    # A cold street: wind, a far-off city hum, ducked under the lines. It swells in as the sheet unfolds.
    m.bed(wind=.02, hum=.008, hum_f=(55, 82), duck=[(0, R.UNFOLD[1] - .6, .2)])
    # The sheet unfolds: three paper sounds, the last one as the street opens.
    u0, u1 = R.UNFOLD
    for k, f in enumerate((.12, .45, .85)):
        m.add(m.whoosh(.45, .25, .85), u0 + f * (u1 - u0), .07)
    m.add(m.thud(240, .05, .9), u1 - .05, .03)
    # A distant car passing behind the facades, once.
    m.add(m.whoosh(2.6, .5, .3), 7.2, .025)
    # The tokens: a rattle with each shake of the fist.
    t, k = R.SHAKE[0] + .25, 0
    while t < R.SHAKE[1] - .3:
        if not (B.L1 + 1.0 < t < B.L1 + 1.25):
            for d in (0, .025, .05):
                m.add(m.tick(3000 + 400 * ((k + int(d * 100)) % 3), .02), t + d + .04, .028 - d * .2)
            k += 1
        t += .13
    m.add(m.tick(2200, .03), R.SHAKE[1] - .1, .03)          # Into the pocket.
    # Vehbi's sleeve back for the watch.
    m.add(m.whoosh(.25, .2, .7), R.WATCH[0], .03)
    # Voices.
    m.voice('voices/s1.wav', B.L1, 1.0)
    m.voice('voices/v2.wav', B.L2, 1.05)
    m.voice('voices/s3.wav', B.L3, 1.0)
    m.voice('voices/v4.wav', B.L4, 1.0)
    m.voice('voices/s5.wav', B.L5, .9)
