"""The rented room at night, and the corridor behind its door. Layout and timing live in room.py.
Room: x 0 (desk and window wall) to 4 (bed wall), y 0 (front wall) to 4.4 (door wall). Corridor: y 4.4 to 6.0."""
import math

import room as R

WOOD, WOOD_D = (120, 82, 52), (84, 56, 36)
TRIM = (196, 186, 162)


def place_door(o, a):
    hx, hy = R.HINGE
    half = R.DOOR_W / 2
    o.location.x = hx - half * math.cos(a)
    o.location.y = hy - half * math.sin(a)
    o.rotation_euler.z = -math.pi / 2 + a


def build(S):
    wall = S.tex_mat('wall.jpg')
    win = S.tex_mat('wall_window.jpg')
    corr = S.tex_mat('corridor.jpg', tint=(.9, .92, 1.0))
    ceil = S.tex_mat('ceiling.jpg')
    W, D, H = R.W, R.D, R.H

    # ---- the room
    S.floor(S.tex_mat('vinyl.jpg'), 0, W, 0, D, tile=1.2)
    S.quad(ceil, [(0, D, H), (W, D, H), (W, 0, H), (0, 0, H)], [(0, 1), (1, 1), (1, 0), (0, 0)])
    S.wall(wall, (W, 0), (0, 0), 0, H, repeat=2.2)               # Front.
    S.wall(win, (0, 0), (0, D), 0, H)                            # Desk wall with the window, one picture.
    S.wall(wall, (W, D), (W, 0), 0, H, repeat=2.2)               # Bed wall.
    S.wall(wall, (0, D), (R.DOOR_X0, D), 0, H, repeat=2.2)       # Door wall, with the opening.
    S.wall(wall, (R.DOOR_X1, D), (W, D), 0, H, repeat=2.2)
    S.wall(wall, (R.DOOR_X0, D), (R.DOOR_X1, D), R.DOOR_H, H - R.DOOR_H, repeat=2.2)
    # Door frame: jambs and head, standing proud of the wall on both sides.
    S.box(TRIM, R.DOOR_X0 - .04, D, R.DOOR_H / 2, .08, .18, R.DOOR_H)
    S.box(TRIM, R.DOOR_X1 + .04, D, R.DOOR_H / 2, .08, .18, R.DOOR_H)
    S.box(TRIM, (R.DOOR_X0 + R.DOOR_X1) / 2, D, R.DOOR_H + .05, R.DOOR_W + .16, .18, .1)

    # ---- the corridor behind the door: dim, cold, long enough to stand a camera in.
    S.floor(S.tex_mat('terrazzo.jpg'), -2.5, 7.5, D, R.CORR_Y1, tile=1.5)
    S.quad(S.flat_mat((70, 72, 78)), [(-2.5, R.CORR_Y1, H), (7.5, R.CORR_Y1, H), (7.5, D, H), (-2.5, D, H)], [(0, 1), (1, 1), (1, 0), (0, 0)])
    S.wall(corr, (-2.5, R.CORR_Y1), (7.5, R.CORR_Y1), 0, H, repeat=4.5)          # Far side.
    Dy = D + .012                                                                 # The room's wall, seen from the corridor.
    S.wall(corr, (7.5, Dy), (R.DOOR_X1, Dy), 0, H, repeat=4.5)
    S.wall(corr, (R.DOOR_X0, Dy), (-2.5, Dy), 0, H, repeat=4.5)
    S.wall(corr, (R.DOOR_X1, Dy), (R.DOOR_X0, Dy), R.DOOR_H, H - R.DOOR_H, repeat=4.5)
    S.wall(corr, (-2.5, D), (-2.5, R.CORR_Y1), 0, H, repeat=4.5)
    S.wall(corr, (7.5, R.CORR_Y1), (7.5, D), 0, H, repeat=4.5)
    S.box((180, 176, 160), 1.2, R.CORR_Y1 - .02, H - .05, .5, .04, .06)          # An unlit corridor fixture.
    for x in (5.6, -1.4):                                                         # Neighbours' doors, shut.
        S.box((92, 76, 60), x, R.CORR_Y1 - .02, 1.02, .9, .03, 2.04)

    # ---- the door
    o = S.prop('door.json', 'door.jpg', 0, 0, width=.045, height=2.02, name='door')
    place_door(o, 0)

    # ---- desk, chair, lamp, books, tea, papers
    dx, dy = R.DESK
    S.box(WOOD, dx, dy, .74, .7, 1.3, .04)
    for lx, ly in ((dx - .3, dy - .6), (dx + .3, dy - .6), (dx - .3, dy + .6), (dx + .3, dy + .6)):
        S.box(WOOD_D, lx, ly, .36, .05, .05, .72)
    S.box(WOOD_D, dx, dy + .4, .62, .62, .42, .18)                              # Drawer block.
    S.box((60, 110, 140), dx, dy + .4, .62, .63, .02, .04)                       # Drawer handle line.
    S.box(WOOD, 1.08, dy, .45, .44, .44, .05)                                    # Chair seat.
    for lx, ly in ((.88, dy - .2), (1.28, dy - .2), (.88, dy + .2), (1.28, dy + .2)):
        S.box(WOOD_D, lx, ly, .22, .04, .04, .44)
    S.box(WOOD, 1.29, dy, .78, .04, .42, .5)                                     # Chair back.
    lamp = S.prop('lamp.json', 'lamp.jpg', .3, 1.3, width=.14, height=.55, name='lamp')
    lamp.location.z = .76
    for bx, by, hh, rot in ((.36, 2.32, .26, math.pi / 2), (.22, 2.38, .16, .1)):
        b = S.prop('stack.json', 'stack.jpg', bx, by, rot=rot, width=.22, height=hh, key=('stack', hh))
        b.location.z = .76
    tg = S.prop('teaglass.json', 'teaglass.jpg', .62, 2.05, width=.08, height=.12)
    tg.location.z = .76
    S.box((236, 232, 220), .46, 1.72, .762, .3, .21, .004)                       # The printed contract form, open.
    S.box((120, 60, 50), .54, 1.8, .7645, .025, .03, .002)                       # Its revenue stamp.
    for px, py in ((.32, 1.98), (.5, 1.55), (.62, 2.35)):                        # Photocopied notes.
        S.box((214, 214, 206), px, py, .761, .21, .3, .002)

    # ---- the bed, the radiator, the floor stacks
    S.box(WOOD_D, 3.55, 1.25, .2, .9, 2.0, .4)
    S.box((214, 206, 186), 3.55, 1.25, .46, .86, 1.96, .14)
    S.box((120, 46, 48), 3.55, 1.0, .55, .92, 1.45, .06)                         # Wool blanket.
    S.lump((226, 220, 204), 3.55, 2.0, .6, .3, .18, .08)                          # Pillow.
    rad = S.prop('radiator.json', 'radiator.jpg', W - .06, 3.05, width=.08, length=1.0)
    rad.location.z = .14
    S.prop('stack.json', 'stack.jpg', R.STACK[0], R.STACK[1], rot=math.pi / 2 + .2, width=.24, height=.45, name='stack', key=('stack', 'floor'))
    S.prop('stack.json', 'stack.jpg', 1.6, 4.15, rot=.4, width=.24, height=.32, key=('stack', 'floor2'))
    S.prop('stack.json', 'stack.jpg', 2.0, .35, rot=1.2, width=.22, height=.22, key=('stack', 'floor3'))  # Foreground, near the front.
    S.sun(.22, tilt=40, heading=-135)


def animate(S, t):
    place_door(S.movers['door'], R.door_angle(t))
    S.movers['lamp'].rotation_euler.x = R.lamp_shake(t)
    st = S.movers['stack']
    st.location.y = R.STACK[1] - R.stack_slide(t)
    st.rotation_euler.x = R.stack_tilt(t)
