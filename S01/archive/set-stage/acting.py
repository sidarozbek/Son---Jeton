"""Set check blocking: Vehbi stands at the desk, Sidar waits in the corridor. Replaced in toon-direct."""
import math

SIDAR_REST = dict(lid=.28, brow=-.25)
POS = dict(sidar=(2.4, 5.25), vehbi=(1.05, 2.55))


def root(name, t):
    return POS[name]


def direct(cast, cfg):
    s, v = cast['sidar'], cast['vehbi']
    s.face(0, .01, 'rest', **SIDAR_REST)
    s.to(0, .01, th=-math.pi / 2)
    v.face(0, .01, 'unimpressed')
    v.to(0, .01, th=math.pi)
    for pup, seed in ((s, 1), (v, 2)):
        pup.auto_blink(seed, cfg.END)
