"""Scene 16: Scene 15's harbour plus the customs post: a standing counter and a filing cabinet whose top drawer slides.
Scene 15: an imaginary harbour, mid-1980s. Layout in room.py. The ships are not here: they are drawn in env.py.
The quay along x, the sea beyond y 4.0 one metre down, a far shore; behind, a warehouse and the harbour office."""
import room as R

QY, WZ = R.QUAY_Y, R.WATER_Z


def build(S):
    S.floor(S.tex_mat('quay.jpg'), R.X0, R.X1, -8.0, QY, tile=2.0)
    S.quad(S.tex_mat('sea.jpg', emit=.8), [(R.X0 - 80, QY, WZ), (R.X1 + 80, QY, WZ), (R.X1 + 80, R.SHORE_Y, WZ), (R.X0 - 80, R.SHORE_Y, WZ)],
           [(-20, QY / 6), (20, QY / 6), (20, R.SHORE_Y / 6), (-20, R.SHORE_Y / 6)])
    S.wall(S.tex_mat('quayface.jpg'), (R.X1, QY), (R.X0, QY), WZ - .2, 1.2 + .0, repeat=4.0)       # Faces the sea.
    S.wall(S.tex_mat('shore.jpg', emit=.85), (R.X0 - 120, R.SHORE_Y), (R.X1 + 120, R.SHORE_Y), WZ, 15.5)
    # The warehouse along the back of the quay, facing the sea, with its roof; the harbour office's side wall.
    S.wall(S.tex_mat('warehouse.jpg'), (R.OFFICE_X, R.WAREHOUSE_Y), (R.OFFICE_X + 32, R.WAREHOUSE_Y), 0, 6.0)
    S.box((96, 102, 108), R.OFFICE_X + 16, R.WAREHOUSE_Y - 6, 6.2, 32.4, 12, .4)
    S.wall(S.tex_mat('office.jpg'), (R.OFFICE_X, -14.0), (R.OFFICE_X, -5.0), 0, 4.0)
    S.wall(S.tex_mat('office.jpg'), (R.OFFICE_X, -5.0), (R.OFFICE_X, 1.5), 0, 4.0)
    S.box((150, 120, 100), R.OFFICE_X - 4.5, -4.5, 4.1, 9.2, 13, .25)
    # Bollards along the edge, a stack of crates, a lamp post, a harbour crane (an original, plain frame).
    for bx in R.BOLLARDS:
        S.box((54, 58, 62), bx, QY - .28, .22, .3, .3, .44)
        S.lump((54, 58, 62), bx, QY - .28, .46, .22, .22, .08)
    for (cx, cy, cz, c) in ((5.6, .4, .45, (150, 110, 70)), (6.5, .5, .45, (126, 92, 60)), (6.0, .45, 1.35, (160, 120, 78))):
        S.box(c, cx, cy, cz, .9, .9, .9)
    S.box((60, 64, 66), 3.0, 1.0, 2.0, .1, .1, 4.0)
    S.box((60, 64, 66), 3.0, 1.3, 3.95, .08, .6, .08)
    S.lump((230, 228, 210), 3.0, 1.55, 3.88, .14, .1, .06)
    cx = R.CRANE_X
    for lx, ly in ((cx - 1.2, .6), (cx + 1.2, .6), (cx - 1.2, 3.4), (cx + 1.2, 3.4)):
        S.box((206, 140, 40), lx, ly, 3.0, .25, .25, 6.0)
    S.box((206, 140, 40), cx, 2.0, 6.1, 2.8, 3.2, .4)
    S.box((206, 140, 40), cx, 2.0, 7.0, 1.6, 1.6, 1.6)
    S.box((206, 140, 40), cx, 7.0, 7.3, .35, 11.0, .35)              # The jib, out over the water.
    S.box((50, 50, 50), cx, 11.0, 5.0, .03, .03, 4.4)                # Its cable.
    # The customs post: a standing counter, a filing cabinet; the top drawer is its own object and slides out.
    dx, dy, dh, sx, sy = R.DESK
    S.box((120, 92, 64), dx, dy, dh - .025, sx, sy, .05)
    S.box((96, 72, 50), dx - sx / 2 + .06, dy, dh / 2, .06, sy - .1, dh - .05)              # Front panel (towards the office).
    for lx in (dx + sx / 2 - .06,):
        for ly in (dy - sy / 2 + .06, dy + sy / 2 - .06):
            S.box((96, 72, 50), lx, ly, dh / 2, .06, .06, dh - .05)
    cx, cy, cd, cw, ch = R.CAB
    S.box((122, 132, 128), cx, cy, ch / 2, cd, cw, ch)
    fx = cx + cd / 2
    for z0, z1 in ((.06, .46), (.5, .88)):
        S.box((140, 150, 146), fx + .01, cy, (z0 + z1) / 2, .02, cw - .04, z1 - z0 - .02)
        S.box((60, 60, 60), fx + .03, cy, z1 - .1, .02, .12, .025)                           # Handles.
    S.box((26, 26, 28), fx + .005, cy, sum(R.DRAWER_Z) / 2, .01, cw - .06, R.DRAWER_Z[1] - R.DRAWER_Z[0] - .02)   # The slot.
    z0, z1 = R.DRAWER_Z
    w = cw - .04
    front = S.flat_mat((150, 160, 156))
    side = S.flat_mat((110, 118, 114))
    parts = [S.wall(front, (0, -w / 2), (0, w / 2), z0, z1 - z0),
             S.wall(side, (-.4, -w / 2 + .02), (0, -w / 2 + .02), z0 + .02, z1 - z0 - .08),
             S.wall(side, (0, w / 2 - .02), (-.4, w / 2 - .02), z0 + .02, z1 - z0 - .08),
             S.quad(S.flat_mat((70, 74, 72)), [(-.4, -w / 2, z0 + .03), (0, -w / 2, z0 + .03), (0, w / 2, z0 + .03), (-.4, w / 2, z0 + .03)],
                    [(0, 0), (1, 0), (1, 1), (0, 1)])]
    for k, p in enumerate(parts):
        p.location = (fx + .012, cy, 0)
        S.movers[f'drawer{k}'] = p
    # Scene 18: a gangway plank from the quay up to ship A's (see-through) deck, with a rope rail on one side.
    gx, gw, y0, y1 = R.GANGWAY
    S.quad(S.flat_mat((150, 112, 72)), [(gx - gw / 2, y0, .02), (gx + gw / 2, y0, .02), (gx + gw / 2, y1, R.DECK_Z + .02), (gx - gw / 2, y1, R.DECK_Z + .02)],
           [(0, 0), (1, 0), (1, 1), (0, 1)])
    for k in range(6):                                                         # Cleats across the plank.
        u = (k + .5) / 6
        S.box((110, 80, 50), gx, y0 + (y1 - y0) * u, .04 + R.DECK_Z * u, gw, .04, .03)
    for py, pz in ((y0 + .05, .0), (y1 - .05, R.DECK_Z)):
        S.box((80, 64, 48), gx + gw / 2 + .03, py, pz + .45, .04, .04, .9)
    S.sun(.55, tilt=48, heading=-35)


def animate(S, t):
    out = R.drawer(t) * R.DRAWER_OUT
    for k in range(4):
        S.movers[f'drawer{k}'].location.x = R.CAB[0] + R.CAB[2] / 2 + .012 + out
