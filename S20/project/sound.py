"""Scene 20 sound. Placeholder effects from synthesis; recorded voices. The harbour bed; the token into the slot
(a soft paper whisper, not a clink: it is only paper); the line's crackle; the paper fold."""
import numpy as np

import blocking as B
import room as R

SR = 48000


def slap(m, d=.35):
    n = int(d * SR)
    t = np.arange(n) / SR
    x = m.lowpass(m.rng.normal(0, 1, n), .06) * np.exp(-t / (d * .3)) * np.minimum(1, t / .03)
    return x / (np.abs(x).max() + 1e-9)


def scratch(m, d=.2):
    n = int(d * SR)
    x = m.rng.normal(0, 1, n)
    x = x - m.lowpass(x, .3)
    return x * np.sin(np.linspace(0, np.pi, n)) / (np.abs(x).max() + 1e-9)


def hiss(m, d, g=1.0):
    n = m.rng.normal(0, 1, int(d * SR))
    n = n - m.lowpass(n, .2)
    t = np.arange(len(n)) / SR
    gate = (np.sin(t * 47) * np.sin(t * 13.3) > -.2).astype(float) * .7 + .3
    ramp = np.minimum(1, t / max(d * .6, .01))
    return n / (np.abs(n).max() + 1e-9) * gate * ramp * g


def score(m, cfg):
    m.bed(wind=.03, hum=0.0, duck=[(R.FOLD[0], R.END, .7)])
    for k, tt in enumerate(np.arange(.4, R.FOLD[0], 1.8)):
        m.add(slap(m), tt + .3 * np.sin(k * 2.3), .04)
    m.add(scratch(m, .5), R.SEE[0] + .2, .02)                         # It turns to paper.
    m.add(scratch(m, .25), R.COIN_IN + .2, .05)                       # Into the slot: a whisper of paper, no clink.
    m.add(hiss(m, R.FOLD[0] - R.CRACKLE + .6, .05), R.CRACKLE, 1.0)  # The line.
    f0, f1 = R.FOLD
    m.add(m.whoosh(.5, .2, .8), f0 + .2, .08)
    m.add(m.whoosh(.45, .25, .85), f0 + .42 * (f1 - f0) + .2, .08)
    m.add(m.whoosh(.6, .3, .9), f0 + .82 * (f1 - f0), .06)
    m.add(m.thud(300, .03, 1.0), f1, .03)
    m.voice('voices/s1.wav', R.L1, 1.0)
    m.voice('voices/v2.wav', R.L2, 1.0)
    m.voice('voices/s3.wav', R.L3, 1.0)
