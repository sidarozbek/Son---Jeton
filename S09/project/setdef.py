"""Scene 09: the same street, 12 September 1980, morning: no snow, the grocer's shutter down, a payphone on the wall.
Scene 04: a street at dusk, January 1980. Layout and timing in room.py.
The road along x, cameras in the road; the far sidewalk, the grocer's front and the apartment facades at the back."""
import math

import room as R

FY = R.FACADE_Y


def build(S):
    # Ground: the road, the kerb, the sidewalk; a strip of front sidewalk so wide shots have a near edge.
    S.floor(S.tex_mat('cobbles.jpg'), R.X0, R.X1, -2.0, R.ROAD_Y1, tile=1.8)
    S.floor(S.tex_mat('pavement.jpg'), R.X0, R.X1, R.ROAD_Y1, FY, tile=1.8, lift=.004)
    S.box((150, 152, 150), (R.X0 + R.X1) / 2, R.ROAD_Y1, .03, R.X1 - R.X0, .16, .06)       # Kerb stones.
    # The facades: ground-floor walls either side of the grocer, the shop front, the upper floors, a cornice.
    gw = S.tex_mat('groundwall.jpg')
    S.wall(gw, (R.X0, FY), (R.SHOP_X0, FY), 0, R.GROUND_H, repeat=4.0)
    S.wall(gw, (R.SHOP_X1, FY), (R.X1, FY), 0, R.GROUND_H, repeat=4.0)
    S.wall(S.tex_mat('shutter.jpg'), (R.SHOP_X0, FY), (R.SHOP_X1, FY), 0, R.GROUND_H)
    S.wall(S.tex_mat('facade.jpg'), (R.X0, FY), (R.X1, FY), R.GROUND_H, R.UPPER_H, repeat=4.0)
    S.box((170, 176, 172), (R.X0 + R.X1) / 2, FY - .08, R.GROUND_H, R.X1 - R.X0, .18, .14)
    # A striped awning over the shop, rolled half out.
    for i in range(8):
        col = (196, 64, 52) if i % 2 == 0 else (236, 228, 210)
        x = R.SHOP_X0 + .1 + (i + .5) * (R.SHOP_X1 - R.SHOP_X0 - .2) / 8
        S.box(col, x, FY - .32, 2.98, (R.SHOP_X1 - R.SHOP_X0 - .2) / 8, .62, .04)
    # The street lamp: a pole at the kerb, an arm over the road, a lamp head.
    lx, ly = R.LAMP_POST
    S.box((48, 54, 58), lx, ly, 2.1, .1, .1, 4.2)
    S.box((48, 54, 58), lx, (ly + R.LAMP_HEAD[1]) / 2, 4.15, .06, ly - R.LAMP_HEAD[1] + .1, .06)
    hx, hy, hz = R.LAMP_HEAD
    S.box((40, 44, 48), hx, hy, hz + .06, .34, .22, .08)
    S.lump((210, 214, 210), hx, hy, hz - .02, .13, .08, .05)          # Off: it is morning.
    # Further down the street: a second lamp, a parked van shape (an original boxy silhouette, no make), a bare tree.
    S.box((48, 54, 58), 13.5, ly, 2.1, .1, .1, 4.2)
    S.lump((210, 214, 210), 13.5, 4.05, 4.03, .13, .08, .05)
    S.box((96, 120, 140), 11.0, 3.4, .75, 3.2, 1.6, 1.1)
    S.box((96, 120, 140), 10.0, 3.4, 1.55, 1.2, 1.5, .55)
    S.box((150, 186, 204), 9.95, 3.4 - .76, 1.55, 1.0, .02, .4)
    for wx in (9.9, 12.1):
        for wy in (2.62, 4.18):
            S.box((24, 24, 26), wx, wy, .3, .6, .14, .6)
    S.box((70, 56, 46), -1.2, 5.3, 1.6, .16, .16, 3.2)
    for k in range(6):
        a = k * 1.05
        S.box((70, 56, 46), -1.2 + .45 * math.cos(a), 5.3 + .25 * math.sin(a), 3.25 + .25 * (k % 2), .06, .06, .9)
    # The payphone on the wall, right of the grocer.
    ph = S.prop('payphone.json', 'payphone.jpg', R.PHONE_X, FY - .06, rot=-math.pi / 2, width=.12, height=.52, name='payphone')
    ph.location.z = R.PHONE_Z0
    S.sun(.3, tilt=30, heading=-60)


def animate(S, t):
    pass
