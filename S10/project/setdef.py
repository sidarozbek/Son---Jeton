"""Scenes 10-14: the office of the imaginary "Kuş Bankerlik", 1982. Layout and timing in room.py.
Back wall: the wooden partition, the barred teller window, the sign, the interest board (its number cards flip)."""
import room as R

WOOD, WOOD_D = (120, 82, 52), (84, 56, 36)


def build(S):
    W, D, H = R.W, R.D, R.H
    wall = S.tex_mat('bk_wall.jpg')
    S.floor(S.tex_mat('bk_floor.jpg'), -1, W, 0, D, tile=1.4)
    S.quad(S.flat_mat((214, 210, 196)), [(-1, D, H), (W, D, H), (W, 0, H), (-1, 0, H)], [(0, 1), (1, 1), (1, 0), (0, 0)])
    S.wall(S.tex_mat('bk_back.jpg'), (0, D), (W, D), 0, H)
    S.wall(wall, (W, D), (W, 0), 0, H, repeat=3.0)
    S.wall(wall, (0, 0), (0, 1.9), 0, H, repeat=3.0)                 # Left wall, with the street door (1.9-3.3).
    S.wall(wall, (0, 3.3), (0, D), 0, H, repeat=3.0)
    S.wall(wall, (0, 1.9), (0, 3.3), 2.2, H - 2.2, repeat=3.0)
    S.box((150, 190, 214), -.5, 2.6, 1.1, .02, 1.4, 2.2)               # Daylight beyond the door.
    S.wall(wall, (W, 0), (-1, 0), 0, H, repeat=3.0)                    # Front wall (behind the cameras in most shots)...
    S.box((176, 204, 222), 3.2, .02, 1.75, 3.2, .02, 1.5)              # ...with the big front window onto the street.
    S.box((84, 56, 36), 3.2, .03, 1.75, .06, .03, 1.5)
    S.box((84, 56, 36), 3.2, .03, 1.0, 3.3, .03, .06)
    S.box((84, 56, 36), 3.2, .03, 2.5, 3.3, .03, .06)
    # The counter shelf at the window and a brass rail for the queue.
    x0, x1, y0, y1, ch = R.COUNTER
    S.box(WOOD_D, (x0 + x1) / 2, (y0 + y1) / 2, ch / 2, x1 - x0, y1 - y0, ch)
    S.box((200, 196, 186), (x0 + x1) / 2, (y0 + y1) / 2, ch + .015, x1 - x0 + .04, y1 - y0 + .04, .03)
    for py in (2.2, 3.4, 4.6):
        S.box((200, 160, 70), 3.55, py, .5, .05, .05, 1.0)
    S.box((200, 160, 70), 3.55, 3.4, .98, .04, 2.4, .04)
    # A potted plant, a bench, a wall clock (stopped), a calendar showing 1982.
    S.box(WOOD, 5.6, 1.2, .23, .5, 1.6, .06)
    for ly in (.55, 1.85):
        S.box(WOOD_D, 5.6, ly, .11, .4, .05, .22)
    S.box((120, 70, 50), .5, 4.9, .22, .36, .36, .44)
    for k in range(5):
        S.lump((60, 120, 60), .5 + .12 * (k % 3 - 1), 4.9 + .1 * (k // 3), .62 + .12 * k / 5, .18, .14, .2)
    # The interest board's number cards, each a quad centred on the board; only the current one is full size.
    bx0, bx1, bz0, bz1 = R.BOARD
    cx, cz = (bx0 + bx1) / 2, bz0 + .32
    for n in R.RATES:
        q = S.wall(S.tex_mat(f'rate_{n}.jpg', emit=.95), (-.38, 0), (.38, 0), -.235, .47)
        q.location = (cx, D - .012, cz)
        q.scale.z = .001
        S.movers[f'rate{n}'] = q
    S.sun(.25, tilt=60, heading=-120)


def animate(S, t):
    k = R.rate_index(t)
    for i, n in enumerate(R.RATES):
        if i == k:
            u = min(max((t - R.RATE_TIMES[i]) / .12, 0.0), 1.0)      # Flips in from a line.
            S.movers[f'rate{n}'].scale.z = max(u, .001)
        else:
            S.movers[f'rate{n}'].scale.z = .001
