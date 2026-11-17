"""Scene 03 sound. Placeholder effects from synthesis, tied to the same numbers as the picture; recorded voices."""
import numpy as np

import blocking as B
import room as R

SR = 48000


def tone(d, f, g=1.0):
    """A plain sine, for the line's hum once the token drops."""
    t = np.arange(int(d * SR)) / SR
    env = np.minimum(1, t / .02) * np.minimum(1, (d - t) / .05)
    return np.sin(2 * np.pi * f * t) * env * g


def hiss(m, d, g=1.0):
    """The crossed line: band noise with a stutter."""
    n = m.rng.normal(0, 1, int(d * SR))
    n = n - m.lowpass(n, .2)
    t = np.arange(len(n)) / SR
    gate = (np.sin(t * 47) * np.sin(t * 13.3) > -.2).astype(float) * .7 + .3
    return n / (np.abs(n).max() + 1e-9) * gate * g


def score(m, cfg):
    # The room's hum until the cut; the basement: lower and boomier, the boiler, a drip. Ducked for "Hello?".
    m.bed(wind=.006, hum=.012, hum_f=(38, 57), duck=[(0, R.CUT, .45), (B.L5 - .1, B.L5 + .6, .5)])
    # Out of the door: Sidar's slippers, Vehbi's socks; then down wooden stairs.
    m.steps(B.S_EXIT[0], R.CUT, .4, f=110, g=.05)
    m.steps(B.V_EXIT[0] + .1, R.CUT, .48, f=150, g=.025)
    m.steps(R.CUT, B.S_WALK[1], .42, f=95, g=.07)
    m.steps(B.V_WALK[0], B.V_WALK[1], .5, f=140, g=.035)
    for k in np.arange(R.CUT + .7, R.FOLD[0], 1.9):          # A slow drip.
        m.add(m.tick(4200, .02), float(k), .015)
    # The receiver off its cradle: a plastic clack.
    m.add(m.thud(260, .04, .7), R.LIFT, .05)
    m.add(m.tick(1800, .03), R.LIFT + .01, .03)
    # The token: a clink at the slot, a rattle down inside the box, the line opening.
    m.add(m.tick(3800, .05), R.COIN_IN + .15, .08)
    for i, dt in enumerate((.09, .16, .21, .25)):
        m.add(m.tick(2600 - i * 300, .025), R.COIN_IN + .15 + dt, .04 - i * .007)
    m.add(tone(B.L5 - (R.COIN_IN + .45), 425, .01), R.COIN_IN + .45, 1.0)
    # The line crosses: hiss rising into the fold, then paper sounds as it folds.
    m.add(hiss(m, R.FOLD[0] - R.CRACKLE + .6, .035), R.CRACKLE, 1.0)
    m.add(m.whoosh(.5, .2, .8), R.FOLD[0] + .2, .08)
    m.add(m.whoosh(.45, .25, .85), R.FOLD[0] + .42 * (R.FOLD[1] - R.FOLD[0]) + .2, .08)
    m.add(m.whoosh(.6, .3, .9), R.FOLD[0] + .82 * (R.FOLD[1] - R.FOLD[0]), .06)
    m.add(m.thud(300, .03, 1.0), R.FOLD[1], .03)
    # Voices.
    m.voice('voices/s1.wav', B.L1, 1.0)
    m.voice('voices/v2.wav', B.L2, 1.1)
    m.voice('voices/s3.wav', B.L3, 1.0)
    m.voice('voices/s4.wav', B.L4, 1.0)
    m.voice('voices/v5.wav', B.L5, 1.0)
