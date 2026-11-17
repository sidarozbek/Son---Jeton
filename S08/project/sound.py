"""Scene 08 sound. Placeholder effects from synthesis, tied to the same numbers as the picture; recorded voices."""
import numpy as np

import blocking as B
import room as R

SR = 48000


def creak(m, d, g=1.0):
    n = m.rng.normal(0, 1, int(d * SR))
    n = m.lowpass(n, .08) - m.lowpass(n, .01)
    t = np.arange(len(n)) / SR
    return n / (np.abs(n).max() + 1e-9) * (.6 + .4 * np.sin(t * 7)) * np.minimum(1, t / .3) * np.minimum(1, (d - t) / .3) * g


def hiss(m, d, g=1.0):
    n = m.rng.normal(0, 1, int(d * SR))
    n = n - m.lowpass(n, .2)
    t = np.arange(len(n)) / SR
    gate = (np.sin(t * 47) * np.sin(t * 13.3) > -.2).astype(float) * .7 + .3
    return n / (np.abs(n).max() + 1e-9) * gate * g


def score(m, cfg):
    m.bed(wind=.004, hum=.012, hum_f=(50, 100), duck=[(R.STAMP[1], cfg.END, .5)])
    # The overflow: cardboard straining, and a whump as each giant card shoots up.
    m.add(creak(m, R.GROW[1] - R.GROW[0]), R.GROW[0], .05)
    for ts in R.STAND_UP:
        m.add(m.thud(110, .08, .7), ts, .1)
        m.add(m.whoosh(.25, .3, .8), ts - .05, .04)
    # Running: Sidar's slippers, Vehbi's socks.
    m.steps(B.S_RUN[0], B.S_RUN[1], .26, f=110, g=.05)
    m.steps(B.V_RUN[0], B.V_RUN[1], .3, f=150, g=.03)
    # The card flying onto Sidar's nose: a flutter and a slap.
    m.add(m.whoosh(.3, .3, .9), R.NOSE[0], .04)
    m.add(m.thud(400, .03, .9), R.NOSE[1], .06)
    # The token: clink and rattle; the line crosses.
    m.add(m.tick(3800, .05), R.COIN_IN + .15, .08)
    for i, dt in enumerate((.09, .16, .21, .25)):
        m.add(m.tick(2600 - i * 300, .025), R.COIN_IN + .15 + dt, .04 - i * .007)
    m.add(hiss(m, cfg.END - R.CRACKLE, .03), R.CRACKLE, 1.0)
    # The stamp, the clipping.
    m.add(m.whoosh(.35, .3, .9), R.STAMP[0], .06)
    m.add(m.thud(70, .18, .6), R.STAMP[1], .3)
    m.add(m.thud(140, .06, .9), R.STAMP[1], .12)
    m.add(m.whoosh(.5, .4, .95), R.CLIP[0], .05)
    # Voices.
    m.voice('voices/s1.wav', B.L1, 1.0)
    m.voice('voices/v2.wav', B.L2, 1.0)
    m.voice('voices/s3.wav', B.L3, 1.0)
