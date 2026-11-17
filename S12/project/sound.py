"""Scene 12 sound. Placeholder effects from synthesis, tied to the same numbers as the picture; recorded voices."""
import numpy as np

import blocking as B
import room as R

SR = 48000


def score(m, cfg):
    m.bed(wind=.004, hum=.008, hum_f=(60, 120), duck=[])
    for t in np.arange(0, cfg.END, .3):                     # The flock, still circling up there.
        m.add(m.whoosh(.12, .55, .95), float(t), .006)
    m.add(m.thud(500, .02, .9), R.TAP, .05)                 # Chalk-tap on the board.
    m.add(m.tick(5000, .02), R.TAP + .01, .02)
    m.steps(B.V_WALK[0], B.V_WALK[1], .4, f=140, g=.03)
    m.steps(B.S_WALK[0], B.S_WALK[1], .4, f=110, g=.04)
    t = R.GRAB_V + .2
    while t < R.POP:                                        # Metal scraping in the slot as they tug.
        m.add(m.tick(2200, .04), float(t), .02)
        t += .48
    m.add(m.thud(220, .05, .8), R.POP, .1)                  # POP.
    m.add(m.tick(4200, .05), R.POP, .06)
    m.add(m.tick(3600, .04), R.CATCH, .04)
    m.voice('voices/v1.wav', B.L1, 1.0)
    m.voice('voices/s2.wav', B.L2, 1.0)
    m.voice('voices/v3.wav', B.L3, 1.0)
    m.voice('voices/s4.wav', B.L4, 1.0)
