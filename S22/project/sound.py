"""Scene 22 sound. The river under everything; a page; the "Sınavda çıkar" stamp (D8); a bright chime for the glint;
a splash of paper and a small metal click as the token lands in his palm."""
import numpy as np

import blocking as B
import room as R

SR = 48000


def river(m, d):
    n = int(d * SR)
    x = m.lowpass(m.rng.normal(0, 1, n), .08) - m.lowpass(m.rng.normal(0, 1, n), .01)
    x = x / (np.abs(x).max() + 1e-9)
    t = np.arange(n) / SR
    crackle = m.rng.normal(0, 1, n) * ((m.rng.random(n) < .004).astype(float))
    crackle = crackle - m.lowpass(crackle, .3)
    return (x * (1 + .2 * np.sin(t * 1.3)) + crackle * .4)


def chime(d=.9, f=1760):
    t = np.arange(int(d * SR)) / SR
    return (np.sin(2 * np.pi * f * t) + .5 * np.sin(2 * np.pi * f * 2.01 * t)) * np.exp(-t / .25) * np.minimum(1, t / .005)


def score(m, cfg):
    m.bed(wind=.02, hum=.004, hum_f=(48, 72), duck=[(R.STAMP[1], R.CLIP[3], .5)])
    m.add(river(m, R.END), 0, .045)
    m.add(m.whoosh(.3, .2, .6), R.BOOK_OPEN, .05)                    # The page.
    m.add(m.whoosh(.35, .3, .9), R.STAMP[0], .05)                    # D8.
    m.add(m.thud(70, .18, .6), R.STAMP[1], .25)
    m.add(m.whoosh(.5, .4, .95), R.CLIP[0], .04)
    m.add(m.whoosh(.45, .4, .95), R.CLIP[2], .03)
    m.add(chime(), R.GLINT, .05)                                     # The glint.
    m.steps(B.V_STEP[0], B.V_STEP[1], .35, f=140, g=.03)
    m.add(m.whoosh(.5, .1, .5), R.HOP[0], .05)                       # The hop...
    m.add(m.tick(3600, .05), R.HOP[1], .08)                          # ...into his palm.
    m.add(chime(.6, 2350), R.HOP[1] + .02, .03)
    m.voice('voices/v1.wav', R.L1, 1.0)
    m.voice('voices/v2.wav', R.L2, 1.0)
    m.voice('voices/s3.wav', R.L3, 1.0)
