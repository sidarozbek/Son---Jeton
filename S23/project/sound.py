"""Scene 23 sound. The exam hall: a room tone, pens scratching all around, the clock ticking (faster with each
round, as the cuts get faster), a page turn at each question, the "Sınavda çıkar" thump at each flash. Whispered
answers. Pen down: a click, and quiet."""
import numpy as np

import room as R

SR = 48000


def scratch(m, d=.2):
    n = int(d * SR)
    x = m.rng.normal(0, 1, n)
    x = x - m.lowpass(x, .3)
    return x * np.sin(np.linspace(0, np.pi, n)) / (np.abs(x).max() + 1e-9)


def score(m, cfg):
    m.bed(wind=.004, hum=.008, hum_f=(50, 100))
    t = .3
    while t < R.PEN_DOWN:                                             # The clock: ticks closer together as it goes.
        m.add(m.tick(2200, .03), t, .025)
        t += 1.0 - .45 * min(t / R.PEN_DOWN, 1.0)
    for k in range(60):                                               # Pens all around.
        tt = .2 + k * .29 + .1 * np.sin(k * 1.7)
        if tt < R.END - .5:
            m.add(scratch(m, .15), tt, .008)
    for k, (a, b) in enumerate(R.Q):
        m.add(m.whoosh(.25, .2, .6), a, .03)                          # A page.
    for k, (a, b) in enumerate(R.FLASH):
        m.add(m.whoosh(.2, .3, .9), a, .04)
        m.add(m.thud(70, .14, .6), a + .13, .2)             # THUNK.
    for k, a in enumerate(R.L):
        for j in range(4 + k):
            m.add(scratch(m, .12), a + j * (.4 - .05 * k), .03)       # His pen.
    m.add(m.tick(1500, .04), R.PEN_DOWN + .3, .06)                    # Pen down.
    for k, a in enumerate(R.L):
        m.voice(f'voices/v{k + 1}.wav', a, 1.0)
