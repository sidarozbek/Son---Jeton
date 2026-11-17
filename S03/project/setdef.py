"""Scene 03: the rented room (as Scene 02 left it) and the basement beside it, in one world.
Basement: x 20-25, y 0-5, 2.4 m high. Stairs down the right wall; the payphone on the back wall; the boiler on the left."""
import math

import room as R
import setdef_room

STEP_RISE, STEP_RUN, STEPS = .218, .27, 11


def build(S):
    setdef_room.build(S)
    wall = S.tex_mat('concrete_wall.jpg')
    x0, x1, y0, y1, h = R.BX0, R.BX1, R.BY0, R.BY1, R.BH
    S.floor(S.tex_mat('concrete_floor.jpg'), x0, x1, y0, y1, tile=1.6)
    S.quad(S.flat_mat((52, 50, 48)), [(x0, y1, h), (x1, y1, h), (x1, y0, h), (x0, y0, h)], [(0, 1), (1, 1), (1, 0), (0, 0)])
    S.wall(wall, (x1, y0), (x0, y0), 0, h, repeat=2.4)
    S.wall(wall, (x0, y0), (x0, y1), 0, h, repeat=2.4)
    S.wall(wall, (x0, y1), (x1, y1), 0, h, repeat=2.4)
    S.wall(wall, (x1, y1), (x1, y0), 0, h, repeat=2.4)
    # Pipes under the ceiling and down to the boiler.
    S.box((70, 72, 76), (x0 + x1) / 2, y1 - .18, h - .14, x1 - x0, .09, .09)
    S.box((70, 72, 76), x0 + .3, 2.0, h - .3, .09, 3.6, .09)
    S.box((70, 72, 76), x0 + .75, 3.35, 1.85, .1, .1, 1.1)
    # The boiler, a coal hatch, cardboard boxes, a shelf of jars.
    bo = S.prop('boiler.json', 'boiler.jpg', x0 + .75, 3.35, rot=-math.pi / 2, width=.75, height=1.3)
    S.box((40, 38, 36), x0 + .02, 1.55, .85, .04, .9, .7)
    S.box((110, 100, 90), x0 + .02, 1.55, .85, .05, .96, .04)
    S.prop('boxes.json', 'boxes.jpg', x0 + .5, .9, rot=-math.pi / 2, width=.5, height=.6)
    S.prop('boxes.json', 'boxes.jpg', x0 + 1.25, .45, rot=-math.pi / 2 + .3, width=.45, height=.45, key=('boxes', 2))
    S.box((88, 64, 44), 23.6, y1 - .14, 1.75, .9, .22, .03)
    for i, jx in enumerate((23.25, 23.42, 23.6, 23.78, 23.95)):
        S.box((120 + 20 * (i % 3), 150, 90 + 30 * (i % 2)), jx, y1 - .14, 1.85, .1, .1, .17)
    # The stairs down the right wall, from the front (top) to the back (bottom), and a handrail.
    sx = x1 - .42
    for i in range(STEPS):
        yc = 3.42 - i * STEP_RUN
        top = (i + 1) * STEP_RISE
        S.box((70, 96, 124), sx, yc, top / 2, .76, STEP_RUN, top)
        S.box((96, 128, 160), sx, yc, top - .01, .78, STEP_RUN + .01, .02)
    S.box((60, 44, 30), sx - .4, 2.05, 1.6, .04, 3.1, .04)
    # The payphone on the back wall; a bare bulb on its flex.
    ph = S.prop('payphone.json', 'payphone.jpg', R.PHONE_X, y1 - .06, rot=-math.pi / 2, width=.12, height=.52, name='payphone')
    ph.location.z = R.PHONE_Z0
    bx, by, bz = R.BULB
    S.box((30, 30, 30), bx, by, (bz + h) / 2 + .05, .012, .012, h - bz - .05)
    S.lump((255, 236, 170), bx, by, bz - .03, .05, .05, .07)


def animate(S, t):
    setdef_room.animate(S, t)
