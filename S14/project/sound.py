"""Scene 14 sound. Placeholder effects from synthesis; recorded voices."""
import numpy as np

import blocking as B
import room as R

SR = 48000


def ring(d=.9):
    """An old telephone bell: two fast-struck bells at 440/660 Hz, trembling."""
    t = np.arange(int(d * SR)) / SR
    trem = (np.sin(2 * np.pi * 20 * t) > 0).astype(float) * .8 + .2
    return (np.sin(2 * np.pi * 440 * t) + .7 * np.sin(2 * np.pi * 660 * t)) * trem * np.minimum(1, t / .01) * np.minimum(1, (d - t) / .05)


def hiss(m, d, g=1.0):
    n = m.rng.normal(0, 1, int(d * SR))
    n = n - m.lowpass(n, .2)
    t = np.arange(len(n)) / SR
    gate = (np.sin(t * 47) * np.sin(t * 13.3) > -.2).astype(float) * .7 + .3
    return n / (np.abs(n).max() + 1e-9) * gate * g


def score(m, cfg):
    m.bed(wind=.004, hum=.006, hum_f=(60, 120), duck=[(R.STAMP[1], R.CLIP[3], .5)])
    m.add(m.whoosh(.35, .3, .9), R.STAMP[0], .05)
    m.add(m.thud(70, .18, .6), R.STAMP[1], .25)
    m.add(m.whoosh(.5, .4, .95), R.CLIP[0], .04)
    m.add(m.whoosh(.45, .4, .95), R.CLIP[2], .03)
    for k in range(3):                                           # The payphone rings, three times.
        m.add(ring(), R.RING + k * 1.3, .05)
    m.add(hiss(m, .6, .03), R.RING - .1, 1.0)
    m.steps(B.S_WALK[0], B.S_WALK[1], .35, f=110, g=.04)
    m.steps(B.V_WALK[0], B.V_WALK[1], .4, f=140, g=.03)
    m.add(m.tick(3800, .05), R.COIN_IN + .15, .07)
    for i, dt in enumerate((.09, .16, .21)):
        m.add(m.tick(2600 - i * 300, .025), R.COIN_IN + .15 + dt, .035 - i * .007)
    m.voice('voices/s1.wav', B.L1, 1.0)
    m.voice('voices/v2.wav', B.L2, 1.0)
    m.voice('voices/s3.wav', B.L3, 1.0)
