"""Scene 24: the corridor outside the exam hall. Layout in room.py. Scene 23's cream walls; a terrazzo floor; the exam
hall's door standing open on the left; a tall window at the far end; a bench; ceiling lights."""
import room as R


def build(S):
    W, D, H = R.W, R.D, R.H
    wall = S.tex_mat('hall_wall.jpg')
    S.floor(S.tex_mat('corr_floor.jpg'), 0, W, -2, D, tile=1.2)
    S.quad(S.flat_mat((230, 228, 220)), [(0, D, H), (W, D, H), (W, -2, H), (0, -2, H)], [(0, 1), (1, 1), (1, 0), (0, 0)])
    S.wall(S.tex_mat('corr_end.jpg'), (0, D), (W, D), 0, H)
    S.wall(wall, (W, D), (W, -2), 0, H, repeat=3.0)
    dy, dw = R.DOOR
    S.wall(wall, (0, -2), (0, dy - dw / 2), 0, H, repeat=3.0)
    S.wall(wall, (0, dy + dw / 2), (0, D), 0, H, repeat=3.0)
    S.wall(wall, (0, dy - dw / 2), (0, dy + dw / 2), 2.2, H - 2.2, repeat=3.0)
    S.box((40, 36, 34), -.3, dy, 1.1, .02, dw, 2.2)                         # The hall beyond: dim.
    S.box((150, 110, 70), -.05, dy - dw / 2 - .02, 1.1, .1, .06, 2.24)      # Door frame.
    S.box((150, 110, 70), -.05, dy + dw / 2 + .02, 1.1, .1, .06, 2.24)
    S.box((150, 110, 70), -.05, dy, 2.22, .1, dw + .1, .06)
    S.box((128, 92, 58), .45, dy + dw / 2 - .02, 1.08, .9, .04, 2.12)      # The door leaf, standing open.
    S.box((140, 104, 66), 2.8, 4.0, .23, .36, 1.6, .06)                     # A bench against the right wall.
    for by in (3.35, 4.65):
        S.box((60, 60, 64), 2.8, by, .11, .32, .05, .22)
    for ly in (2.5, 6.5, 10.5):                                             # Ceiling lights.
        S.box((250, 250, 244), 1.5, ly, H - .04, .3, 1.2, .05)
    S.sun(.4, tilt=40, heading=90)


def animate(S, t):
    pass
