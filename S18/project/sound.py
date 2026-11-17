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
    m.bed(wind=.03, hum=0.0)
    for k, tt in enumerate(np.arange(.6, R.END, 1.8)):
        m.add(slap(m), tt + .3 * np.sin(k * 2.3), .045)
    m.add(gull(), 7.5, .015)
    m.add(gull(.5, 1400), 15.0, .018)                                 # The one sound in the wait.
    m.steps(R.S_WALK[0] + .1, 2.6, .36, f=110, g=.04)
    m.steps(2.6, R.S_WALK[1], .3, f=210, g=.05)                        # Hollow, on the plank.
    m.steps(R.V_WALK[0] + .1, R.V_WALK[1], .38, f=140, g=.03)
    for k in range(int((R.WRITE[1] - R.WRITE[0]) / .25)):
        m.add(scratch(m, .18), R.WRITE[0] + k * .25, .02)
    m.add(m.thud(120, .1, .9), R.STAMP_L, .26)
    m.add(m.tick(1800, .03), R.STAMP_L + .005, .05)
    m.voice('voices/s1.wav', R.L1, 1.0)
    m.voice('voices/v2.wav', R.L2, 1.0)
    m.voice('voices/s3.wav', R.L3, 1.0)
    m.voice('voices/s4.wav', R.L4, 1.0)
    m.voice('voices/v5.wav', R.L5, 1.0)
