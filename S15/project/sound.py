"""Scene 15 sound. Placeholder effects from synthesis; recorded voices. The ships make no sound at all: no engine,
no wake. Only the harbour: wind, water slapping the quay wall, a gull far off. The hull, touched, rustles like paper."""
import numpy as np

import blocking as B
import room as R

SR = 48000


def slap(m, d=.35):
    """Water against the quay wall: a soft low splash."""
    n = int(d * SR)
    t = np.arange(n) / SR
    x = m.lowpass(m.rng.normal(0, 1, n), .06) * np.exp(-t / (d * .3)) * np.minimum(1, t / .03)
    return x / (np.abs(x).max() + 1e-9)


def gull(d=.45, f0=1500):
    """A distant gull: a falling, wavering cry."""
    t = np.arange(int(d * SR)) / SR
    f = f0 * (1 - .35 * t / d) * (1 + .03 * np.sin(2 * np.pi * 9 * t))
    ph = 2 * np.pi * np.cumsum(f) / SR
    return (np.sin(ph) + .3 * np.sin(2 * ph)) * np.sin(np.pi * t / d) ** 1.5


def rustle(m, d=.5):
    """Paper: bright, crackling noise in short bursts."""
    n = int(d * SR)
    x = m.rng.normal(0, 1, n)
    x = x - m.lowpass(x, .25)
    t = np.arange(n) / SR
    gate = (m.rng.random(n) < .02).astype(float)
    env = m.lowpass(gate, .004) * 40
    return x * np.clip(env, 0, 1) * np.sin(np.pi * t / d) / (np.abs(x).max() + 1e-9)


def score(m, cfg):
    m.bed(wind=.03, hum=0.0)
    for k, tt in enumerate(np.arange(.4, R.END, 1.7)):
        m.add(slap(m), tt + .3 * np.sin(k * 2.3), .05)
    m.add(gull(), 1.1, .02)
    m.add(gull(.38, 1700), 1.6, .015)
    m.add(gull(.5, 1400), 11.6, .015)
    m.steps(B.V_WALK[0] + .1, B.V_WALK[1], .38, f=150, g=.035)
    m.add(rustle(m, .6), R.TOUCH - .05, .12)                    # The hand goes in: paper.
    m.add(rustle(m, .9), R.TOUCH + 1.4, .035)                    # The hull slides on through the fingers.
    m.add(rustle(m, .45), R.PULL[0], .09)                        # Out.
    m.voice('voices/s1.wav', R.L1, 1.0)
    m.voice('voices/v2.wav', R.L2, 1.0)
    m.voice('voices/s3.wav', R.L3, 1.0)
