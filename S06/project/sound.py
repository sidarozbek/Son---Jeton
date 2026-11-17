"""Scene 06 sound. Placeholder effects from synthesis, tied to the same numbers as the picture; recorded voices."""
import numpy as np

import blocking as B
import room as R

SR = 48000


def chime(f, d=2.2):
    """A wall clock's strike: a low bell partial with a slow decay."""
    t = np.arange(int(d * SR)) / SR
    env = np.exp(-t * 2.2) * np.minimum(1, t / .004)
    return (np.sin(2 * np.pi * f * t) + .5 * np.sin(2 * np.pi * f * 2.76 * t) * np.exp(-t * 3) + .3 * np.sin(2 * np.pi * f * 5.4 * t) * np.exp(-t * 6)) * env


def creak(m, d, g=1.0):
    """Cardboard stretching: band noise with a slow wobble."""
    n = m.rng.normal(0, 1, int(d * SR))
    n = m.lowpass(n, .08) - m.lowpass(n, .01)
    t = np.arange(len(n)) / SR
    return n / (np.abs(n).max() + 1e-9) * (.6 + .4 * np.sin(t * 7)) * np.minimum(1, t / .3) * np.minimum(1, (d - t) / .3) * g


def score(m, cfg):
    m.bed(wind=.004, hum=.012, hum_f=(50, 100), duck=[(B.L2 - .1, B.L2 + 2.2, .6)])
    # The clock's last tick, then the strikes.
    m.add(m.tick(2400, .03), R.MIDNIGHT, .05)
    for k, t in enumerate(R.CHIMES):
        m.add(chime(392), t, .06 if k == 0 else .045)
    for t in np.arange(R.CHIMES[-1] + .75, cfg.END, .75):    # The rest of the twelve, under the scene.
        m.add(chime(392), float(t), .02)
    # The cards swell: a long cardboard stretch, and a pop at the overshoot.
    m.add(creak(m, R.GROW[1] - R.GROW[0]), R.GROW[0], .05)
    m.add(m.thud(180, .05, .8), R.GROW[1] - .4, .04)
    # The banknote crinkling as it shrinks.
    for t in np.arange(R.SHRINK[0], R.SHRINK[1], .18):
        m.add(m.tick(5200, .015), float(t), .012)
    # Voices.
    m.voice('voices/s1.wav', B.L1, 1.0)
    m.voice('voices/v2.wav', B.L2, 1.0)
    m.voice('voices/s3.wav', B.L3, 1.0)
