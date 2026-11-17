"""Placeholder sound from synthesis, tied to the same numbers as the picture. Voices go in when they're recorded."""
import blocking as B
import room as R


def score(m, cfg):
    # The room is never silent: a low night hum, the lamp's faint buzz. Pulled away after "I'm here", so the stare lands in quiet.
    m.bed(wind=.004, hum=.01, hum_f=(50, 100), duck=[(17.55, 18.55, .7)])
    # Knocks: heavy knuckles on a wooden door, and the lamp rattles on the desk each time.
    for k in R.KNOCKS:
        m.add(m.thud(82, .16, .9), k, 0.205)
        m.add(m.tick(3400, .02), k + .02, 0.020)
    # The latch, the crack: a click and a short creak.
    m.add(m.tick(1900, .03), R.CRACK[0] - .05, 0.099)
    m.add(m.whoosh(R.CRACK[1] - R.CRACK[0], .02, .09), R.CRACK[0], 0.083)
    # The shove: a creak that becomes the slam against the stop, a rattle of the frame.
    m.add(m.whoosh(R.PUSH[1] - R.PUSH[0], .05, .25), R.PUSH[0], 0.132)
    m.add(m.thud(70, .3, 1.2), R.PUSH[1], 0.264)
    m.add(m.tick(2200, .05), R.PUSH[1] + .03, 0.040)
    # The books: a skid across the vinyl, then the top ones settle.
    hit = R.PUSH[0] + (R.PUSH[1] - R.PUSH[0]) * .55
    m.add(m.whoosh(.35, .1, .35), hit, 0.073)
    m.add(m.thud(160, .06, 1.0), hit + .38, 0.066)
    m.add(m.thud(190, .05, 1.0), hit + .5, 0.040)
    # Feet: Vehbi in socks, nearly silent; Sidar in slippers, a shuffle.
    m.steps(B.V_WALK[0] + .1, B.V_WALK[1], .52, f=150, g=0.028)
    m.steps(B.S_WALK[0], B.S_WALK[1], .4, f=110, g=0.064)
    # His palm on his chest.
    m.add(m.thud(130, .07, .8), B.L5 + .25, 0.040)
    # Voices, recorded in Voicebox, trimmed, at the same starts as acting.py. Recorded near full scale, so gain 1.0:
    # the default 1.5 drives them into the limiter. Sidar's corridor shout sits a touch lower, behind the door.
    m.voice('voices/s1.wav', B.L1, .95)
    m.voice('voices/v2.wav', B.L2, 1.0)
    m.voice('voices/s3.wav', B.L3, 1.0)
    m.voice('voices/v4.wav', B.L4, 1.0)
    m.voice('voices/s5.wav', B.L5, 1.0)
