"""Scene 18 sound. Placeholder effects from synthesis; recorded voices. The harbour bed; steps on the quay and hollow
steps up the plank; the officer's pen and his stamp; then, for the wait, nothing but the water. The ship never moves,
so there is no engine, no horn."""
import numpy as np

import blocking as B
import room as R

SR = 48000


def slap(m, d=.35):
    n = int(d * SR)
    t = np.arange(n) / SR
    x = m.lowpass(m.rng.normal(0, 1, n), .06) * np.exp(-t / (d * .3)) * np.minimum(1, t / .03)
    return x / (np.abs(x).max() + 1e-9)


def gull(d=.45, f0=1500):
    t = np.arange(int(d * SR)) / SR
    f = f0 * (1 - .35 * t / d) * (1 + .03 * np.sin(2 * np.pi * 9 * t))
    ph = 2 * np.pi * np.cumsum(f) / SR
    return (np.sin(ph) + .3 * np.sin(2 * ph)) * np.sin(np.pi * t / d) ** 1.5


def scratch(m, d=.2):
    n = int(d * SR)
    x = m.rng.normal(0, 1, n)
    x = x - m.lowpass(x, .3)
    return x * np.sin(np.linspace(0, np.pi, n)) / (np.abs(x).max() + 1e-9)


def score(m, cfg):
    m.bed(wind=.035, hum=0.0, duck=[(R.STAMP[1], R.CLIP[3], .5)])
    for k, tt in enumerate(np.arange(.6, R.END, 1.8)):
        m.add(slap(m), tt + .3 * np.sin(k * 2.3), .04)
    m.add(gull(), 5.9, .015)
    m.add(m.whoosh(.35, .3, .9), R.STAMP[0], .05)                     # D7.
    m.add(m.thud(70, .18, .6), R.STAMP[1], .25)
    m.add(m.whoosh(.5, .4, .95), R.CLIP[0], .04)
    m.add(m.whoosh(.45, .4, .95), R.CLIP[2], .03)
    for tt in R.LIDS:                                                 # The lids: a hollow clank each, nothing inside.
        m.add(m.thud(180, .12, .4), tt + .2, .07)
        m.add(m.tick(900, .06), tt + .22, .03)
    m.add(m.whoosh(.6, .1, .7), R.BURST - .05, .09)                   # The burst...
    for k in range(40):                                               # ...and paper, paper, paper.
        m.add(scratch(m, .25), R.BURST + .1 + k * .14 + .05 * np.sin(k * 3.1), .03 * (1 - k / 50))
    m.add(scratch(m, .2), R.CATCH[1], .06)                            # The catch.
    for k in range(6):                                                # Waved.
        m.add(scratch(m, .12), R.CATCH[1] + .3 + k * .35, .03)
    m.voice('voices/v1.wav', R.L1, 1.0)
    m.voice('voices/s2.wav', R.L2, 1.0)
    m.voice('voices/v3.wav', R.L3, 1.0)
    m.voice('voices/s4.wav', R.L4, 1.0)
