"""Scene 21 sound. The unfold; then the river: a steady rush of water with paper in it, and nothing else. Far-off
evening traffic, very low. No music: the moment is quiet."""
import numpy as np

import blocking as B
import room as R

SR = 48000


def river(m, d):
    """Running water and paper: a band of filtered noise with a soft crackle riding on it."""
    n = int(d * SR)
    x = m.lowpass(m.rng.normal(0, 1, n), .08) - m.lowpass(m.rng.normal(0, 1, n), .01)
    x = x / (np.abs(x).max() + 1e-9)
    t = np.arange(n) / SR
    crackle = m.rng.normal(0, 1, n) * ((m.rng.random(n) < .004).astype(float))
    crackle = crackle - m.lowpass(crackle, .3)
    return (x * (1 + .2 * np.sin(t * 1.3)) + crackle * .4) * np.minimum(1, t / 1.0)


def score(m, cfg):
    m.bed(wind=.02, hum=.004, hum_f=(48, 72))
    a, b = R.UNFOLD
    m.add(m.whoosh(.6, .3, .9), a + .1, .06)                     # The unfold: the fold's sounds, backwards.
    m.add(m.whoosh(.45, .25, .85), a + .9, .07)
    m.add(m.whoosh(.5, .2, .8), a + 1.7, .07)
    m.add(river(m, R.END - 1.6), 1.6, .05)
    m.voice('voices/v1.wav', R.L1, 1.0)
    m.voice('voices/s2.wav', R.L2, 1.0)
