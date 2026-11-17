"""Scene 24 sound. The corridor: steps, a door, distant voices of students, a soft hum of lights. After "...I don't
know." the room goes on for a moment; at black, silence. No music."""
import numpy as np

import blocking as B
import room as R

SR = 48000


def score(m, cfg):
    m.bed(wind=.004, hum=.01, hum_f=(50, 100), duck=[(R.BLACK, R.END, 1.0)])
    m.add(m.thud(90, .2, .5), .45, .05)                               # The door.
    m.steps(B.V_WALK[0] + .1, B.V_WALK[1], .45, f=160, g=.03)
    m.steps(B.F_WALK[0] + .1, B.F_WALK[1], .42, f=180, g=.025)
    m.steps(B.O_WALK[0], B.O_WALK[1], .5, f=150, g=.012)
    murmur = m.lowpass(m.rng.normal(0, 1, int(R.BLACK * SR)), .03)
    murmur = murmur / (np.abs(murmur).max() + 1e-9) * (1 + .5 * np.sin(np.arange(len(murmur)) / SR * 2.1))
    m.add(murmur * np.minimum(1, np.arange(len(murmur)) / SR / .5), 0, .012)
    m.voice('voices/f1.wav', R.L1, 1.0)
    m.voice('voices/v2.wav', R.L2, 1.0)
