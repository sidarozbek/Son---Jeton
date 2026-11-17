"""Scene 02 sound. Placeholder effects from synthesis, tied to the same numbers as the picture; recorded voices."""
import blocking as B
import room as R


def score(m, cfg):
    # The room: the same low hum as Scene 01. Pulled back for Vehbi's slow look, so it lands in quiet.
    m.bed(wind=.004, hum=.01, hum_f=(50, 100), duck=[(15.5, 17.3, .65)])
    # The grab: a slap of palms on a hardback.
    m.add(m.thud(180, .05, .9), R.GRAB, .09)
    m.add(m.tick(2600, .02), R.GRAB + .01, .03)
    # Each yank: a short cloth whoosh and a creak of the book's spine.
    for k in R.YANKS:
        m.add(m.whoosh(.16, .1, .4), k - .04, .05)
        m.add(m.tick(900, .04), k + .02, .03)
    # Shuffling feet while they turn: Sidar's slippers, Vehbi's socks.
    m.steps(B.TURN[0] + .1, B.TURN[1], .38, f=110, g=.05)
    m.steps(B.TURN[0] + .25, B.TURN[1], .46, f=150, g=.025)
    # The contract: a paper flutter down, then a soft pat on the vinyl.
    m.add(m.whoosh(R.LAND - R.SLIP, .25, .7), R.SLIP, .06)
    m.add(m.thud(240, .03, 1.0), R.LAND, .04)
    # The release, and the tie.
    m.add(m.whoosh(.1, .15, .5), R.RELEASE, .05)
    m.add(m.whoosh(.25, .3, .8), R.RELEASE + .5, .03)
    # Voices, recorded in Voicebox, trimmed.
    m.voice('voices/s1.wav', B.L1, 1.0)
    m.voice('voices/v2.wav', B.L2, 1.0)
    m.voice('voices/s3.wav', B.L3, 1.0)
