"""Scene 13 sound: the flock's wings leaving, then quiet. The shutter. The sign's creak and fall. No music."""
import numpy as np

import blocking as B
import room as R


def score(m, cfg):
    m.bed(wind=.004, hum=.006, hum_f=(60, 120), duck=[])
    for t in np.arange(0, R.LIFT, .3):
        m.add(m.whoosh(.12, .55, .95), float(t), .006)
    for t in np.arange(R.LIFT, R.EXIT[1] + .6, .07):           # The lift: a rush of wings, fading out of the door.
        k = 1 - (t - R.LIFT) / (R.EXIT[1] + .6 - R.LIFT)
        m.add(m.whoosh(.15, .5, .95), float(t), .02 * k + .002)
    m.add(m.thud(160, .12, .5), R.SHUTTER + .35, .12)            # The shutter, down.
    m.add(m.whoosh(.35, .2, .6), R.SHUTTER, .03)
    m.add(m.tick(900, .2), R.SIGN_HOOK, .02)                     # A hook gives; the creak of the swing.
    m.add(m.whoosh(.8, .05, .2), R.SIGN_HOOK + .05, .02)
    m.add(m.thud(90, .2, .6), R.SIGN_LAND, .22)                  # The sign on the floor.
    m.add(m.tick(1400, .06), R.SIGN_LAND + .02, .04)
