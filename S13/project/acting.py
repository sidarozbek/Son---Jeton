"""Son Jeton, scene 13: the flock leaves; the window shuts; the queue stands still; the sign falls.
No one speaks. No joke, no comic business: small, slow movements only. Eyes first, then face, then head."""
import math

from toonkit.camera import smooth
import blocking as B
import room as R


def root(name, t):
    return B.where(name, t)


def direct(cast, cfg):
    s, v = cast['sidar'], cast['vehbi']
    qs = [cast[f'q{i}'] for i in range(len(R.QUEUE_SPOTS))]
    for i, q in enumerate(qs):
        q.face(0, .01, 'rest', lid=.35)
        q.look(0, 0, .25)
        q.look(R.LIFT + .1 * i, -.2, .6, dur=.3)                  # They watch the flock go.
        q.to(R.LIFT + .1 * i, .6, ease=smooth, hy=-.3)
        q.look(R.EXIT[1] + .2 * i, 0, .1, dur=.5)
        q.to(R.EXIT[1] + .2 * i, 1.0, ease=smooth, hy=0)
        q.face(R.SHUTTER + .3 + .15 * i, .8, 'rest', lid=.5, brow=.2)
        q.to(R.SHUTTER + 1.5 + .4 * i, 2.0, ease=smooth, hp=.12)   # Heads lower, slowly, one after another.
    s.face(0, .01, 'rest', lid=.3)
    v.face(0, .01, 'rest', lid=.35)
    s.look(0, 0, .4)
    v.look(0, -.2, .3)
    s.look(R.LIFT + .1, -.4, .6, dur=.4)
    v.look(R.LIFT + .2, -.5, .5, dur=.4)
    s.face(R.EXIT[1], .8, 'rest', lid=.45, brow=-.05)
    v.look(R.SHUTTER + 1.0, -.6, 0, dur=.6)                       # Vehbi looks at the people in the queue.
    v.face(R.SHUTTER + 1.0, .8, 'rest', lid=.45, brow=.2)
    s.look(R.SHUTTER + 2.0, 0, -.2, dur=.6)
    for p in [s, v] + qs:                                         # The sign: they look up at it, and that is all.
        p.look(R.SIGN_HOOK + .1, 0, .5, dur=.3)
    for k, pup in enumerate([s, v] + qs):
        pup.auto_blink(60 + k, cfg.END)
