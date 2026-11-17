"""Scene 16 sound. Placeholder effects from synthesis; recorded voices. The harbour bed from Scene 15; the officer's
stamp (a dry wooden thump, the only voice he has); the drawer; a paper unfolding as each ship comes out; a soft plop
when it lands. The ships themselves make no sound."""
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


def rustle(m, d=.5):
    n = int(d * SR)
    x = m.rng.normal(0, 1, n)
    x = x - m.lowpass(x, .25)
    t = np.arange(n) / SR
    gate = (m.rng.random(n) < .02).astype(float)
    env = m.lowpass(gate, .004) * 40
    return x * np.clip(env, 0, 1) * np.sin(np.pi * t / d) / (np.abs(x).max() + 1e-9)


def drawer(m, d=.25):
    """A metal drawer on runners: a short rolling rumble."""
    n = int(d * SR)
    t = np.arange(n) / SR
    x = m.lowpass(m.rng.normal(0, 1, n), .15) * (1 + .5 * np.sin(2 * np.pi * 38 * t)) * np.sin(np.pi * t / d)
    return x / (np.abs(x).max() + 1e-9)


def score(m, cfg):
    m.bed(wind=.03, hum=0.0)
    for k, tt in enumerate(np.arange(.6, R.END, 1.8)):
        m.add(slap(m), tt + .3 * np.sin(k * 2.3), .045)
    m.add(gull(), 2.2, .018)
    m.add(gull(.5, 1400), 9.8, .014)
    for k, ts in enumerate(R.STAMPS):
        m.add(m.thud(120, .1, .9), ts, .28)                          # The stamp.
        m.add(m.tick(1800, .03), ts + .005, .05)
        m.add(drawer(m), ts + .3, .06)                               # The drawer rolls open...
        m.add(rustle(m, .45), ts + R.RISE[0], .1)                    # ...paper unfolds...
        if k < 2:
            m.add(m.whoosh(1.6, .02, .12), ts + R.FLY[0] + .2, .05)  # ...the hop...
            m.add(slap(m, .25), ts + R.FLY[1], .08)                  # ...a soft plop.
            m.add(drawer(m, .2), ts + 1.45, .05)                     # The drawer shuts.
    m.voice('voices/s1.wav', R.L1, 1.0)
    m.voice('voices/v2.wav', R.L2, 1.0)
    m.voice('voices/s3.wav', R.L3, 1.0)
