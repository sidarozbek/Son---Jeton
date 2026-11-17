"""Scene 23: an exam hall. Layout in room.py. Cream walls, a wooden floor, tall windows on the left wall, a blackboard
and a clock on the front wall, rows of wooden desks (a front panel towards the blackboard) and chairs behind them."""
import room as R

WOOD, WOOD_D = (150, 110, 70), (110, 78, 50)


def build(S):
    W, D, H = R.W, R.D, R.H
    wall = S.tex_mat('hall_wall.jpg')
    S.floor(S.tex_mat('hall_floor.jpg'), 0, W, 0, D, tile=1.6)
    S.quad(S.flat_mat((226, 222, 210)), [(0, D, H), (W, D, H), (W, 0, H), (0, 0, H)], [(0, 1), (1, 1), (1, 0), (0, 0)])
    S.wall(S.tex_mat('hall_front.jpg'), (0, D), (W, D), 0, H)
    S.wall(S.tex_mat('hall_windows.jpg'), (0, 0), (0, D), 0, H)
    S.wall(wall, (W, D), (W, 0), 0, H, repeat=3.0)
    S.wall(wall, (W, 0), (0, 0), 0, H, repeat=3.0)
    for x, y in R.ALL_DESKS:                                    # Desk top, front panel (towards the back of the room), legs.
        S.box(WOOD, x, y, R.DESK_H - .02, 1.0, .55, .04)
        S.box(WOOD_D, x, y + .26, R.DESK_H / 2 + .05, 1.0, .03, R.DESK_H - .1)   # Front panel, towards the blackboard.
        cy = y - R.CHAIR_BACK                                                 # The chair behind the desk: seat, legs, back.
        S.box((92, 70, 52), x, cy, R.SEAT_H - .02, .44, .42, .04)
        for lx in (x - .19, x + .19):
            for ly in (cy - .18, cy + .18):
                S.box((60, 60, 64), lx, ly, (R.SEAT_H - .04) / 2, .03, .03, R.SEAT_H - .04)
        S.box((92, 70, 52), x, cy - .21, R.SEAT_H + .25, .44, .03, .32)
        for lx in (x - .47, x + .47):
            S.box((70, 70, 74), lx, y - .22, R.DESK_H / 2, .03, .03, R.DESK_H)
    # The proctor's table at the front.
    S.box(WOOD, 7.6, 9.3, .74, 1.4, .7, .04)
    S.box(WOOD_D, 7.6, 8.96, .40, 1.4, .03, .64)
    S.sun(.45, tilt=40, heading=0)


def animate(S, t):
    pass
