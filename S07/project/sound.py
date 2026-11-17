"""Scene 07 sound. Placeholder effects from synthesis, tied to the same numbers as the picture; recorded voices."""
import numpy as np

import blocking as B
import room as R

SR = 48000


def score(m, cfg):
    m.bed(wind=.004, hum=.012, hum_f=(50, 100), duck=[(R.STAMP[1], R.CLIP[3], .5)])
    # The stamp: a quick rush down, a heavy rubber THUNK, a small rattle as it lifts.
    m.add(m.whoosh(.35, .3, .9), R.STAMP[0], .06)
    m.add(m.thud(70, .18, .6), R.STAMP[1], .3)
    m.add(m.thud(140, .06, .9), R.STAMP[1], .12)
    m.add(m.whoosh(.3, .2, .7), R.STAMP[1] + .1, .03)
    # Into the clipping: newsprint rustle; and back.
    m.add(m.whoosh(.5, .4, .95), R.CLIP[0], .05)
    m.add(m.whoosh(.45, .4, .95), R.CLIP[2], .04)
    # The book opening, a page turning.
    m.add(m.whoosh(.25, .3, .9), R.BOOK_OPEN - .1, .04)
    m.add(m.tick(1500, .03), R.BOOK_OPEN + .15, .03)
    # Voices.
    m.voice('voices/v1.wav', B.L1, 1.0)
    m.voice('voices/s2.wav', B.L2, 1.0)
    m.voice('voices/v3.wav', B.L3, 1.0)
    m.voice('voices/s4.wav', B.L4, 1.0)
