"""Scene 17 sound. Placeholder effects from synthesis; recorded voices. The harbour bed; the "Sınavda çıkar" stamp
(rush, thunk, newsprint); a page turning; finger taps on the book. The ships make no sound."""
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


def score(m, cfg):
    m.bed(wind=.03, hum=0.0, duck=[(R.STAMP[1], R.CLIP[3], .5)])
    for k, tt in enumerate(np.arange(.6, R.END, 1.8)):
        m.add(slap(m), tt + .3 * np.sin(k * 2.3), .04)
    m.add(gull(), 5.8, .015)
    m.add(gull(.5, 1400), 12.9, .014)
    m.add(m.whoosh(.35, .3, .9), R.STAMP[0], .05)
    m.add(m.thud(70, .18, .6), R.STAMP[1], .25)
    m.add(m.whoosh(.5, .4, .95), R.CLIP[0], .04)
    m.add(m.whoosh(.45, .4, .95), R.CLIP[2], .03)
    m.add(m.whoosh(.3, .2, .6), R.BOOK_OPEN, .05)                  # The page.
    for tt in (8.6, 9.2):
        m.add(m.thud(300, .03, .3), tt, .05)
    m.voice('voices/v1.wav', R.L1, 1.0)
    m.voice('voices/s2.wav', R.L2, 1.0)
    m.voice('voices/v3.wav', R.L3, 1.0)
