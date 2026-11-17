"""Scene 06: inside the grocer's at midnight (Scene 05's shop). Layout and timing in room.py.
Back wall: shelves of goods with the price cards that flip. Counter across the shop. Front wall: window and door."""
import room as R

WOOD, WOOD_D = (120, 82, 52), (84, 56, 36)


def build(S):
    W, D, H = R.W, R.D, R.H
    side = S.tex_mat('shopwall.jpg')
    S.floor(S.tex_mat('shopfloor.jpg'), 0, W, 0, D, tile=1.2)
    S.quad(S.flat_mat((150, 146, 132)), [(0, D, H), (W, D, H), (W, 0, H), (0, 0, H)], [(0, 1), (1, 1), (1, 0), (0, 0)])
    S.wall(S.tex_mat('shelves.jpg'), (0, D), (W, D), 0, H)                       # Back: the shelves.
    S.wall(S.tex_mat('shopfront_in.jpg'), (W, 0), (0, 0), 0, H)                  # Front, seen from inside.
    S.wall(side, (0, 0), (0, D), 0, H, repeat=3.0)
    S.wall(side, (W, D), (W, 0), 0, H, repeat=3.0)
    # The shelf boards stand out from the wall, so the cards have an edge to sit on.
    for z in R.SHELF_Z:
        S.box((96, 70, 46), W / 2, D - .16, z, W - .1, .32, .03)
        S.box((70, 50, 34), W / 2, R.SHELF_Y, z - .03, W - .1, .02, .06)
    # The counter: a wooden front with a glass case of loose goods, a marble top, a scale and a jar of sweets.
    x0, x1, y0, y1, ch = R.COUNTER
    S.box(WOOD_D, (x0 + x1) / 2, (y0 + y1) / 2, ch / 2, x1 - x0, y1 - y0, ch)
    S.box(WOOD, (x0 + x1) / 2, y0 - .005, ch / 2, x1 - x0 - .1, .01, ch - .12)
    S.box((214, 210, 200), (x0 + x1) / 2, (y0 + y1) / 2, ch + .02, x1 - x0 + .06, y1 - y0 + .06, .04)
    S.box((150, 156, 160), 3.6, 3.65, ch + .1, .3, .22, .12)                    # The scale.
    S.box((120, 126, 130), 3.6, 3.65, ch + .32, .03, .03, .34)
    S.box((180, 186, 190), 3.6, 3.65, ch + .5, .4, .03, .03)
    for sx in (3.42, 3.78):
        S.lump((170, 176, 180), sx, 3.65, ch + .46, .09, .09, .03)
    S.lump((210, 220, 226), .95, 3.65, ch + .14, .1, .1, .13)                   # A glass jar...
    for k in range(6):
        S.lump(((220, 60, 60), (240, 200, 40), (60, 160, 70))[k % 3], .92 + (k % 3) * .03, 3.64 + (k // 3) * .03, ch + .06 + (k // 3) * .05, .025, .025, .025)
    # Sacks of rice and beans in front of the counter, a crate of oranges by the door.
    for sx, col in ((.75, (220, 210, 180)), (1.15, (200, 180, 140))):
        S.lump(col, sx, 3.1, .3, .2, .17, .3)
        S.lump(tuple(c - 20 for c in col), sx, 3.1, .58, .14, .12, .04)
    S.box((120, 84, 50), 4.4, .7, .2, .4, .5, .4)
    for k in range(6):
        S.lump((236, 140, 40), 4.3 + (k % 3) * .1, .55 + (k // 3) * .25, .44, .05, .05, .05)
    # The pendant bulb.
    lx, ly, lz = R.LAMP
    S.box((30, 30, 30), lx, ly, (lz + H) / 2 + .05, .012, .012, H - lz - .05)
    S.box((60, 70, 60), lx, ly, lz + .09, .3, .3, .02)
    S.lump((255, 236, 170), lx, ly, lz, .06, .06, .07)
    # The price cards that flip: an old and a new card on the same spot, each scaled across its width in animate.
    for i, (x, z, old, new) in enumerate(R.CARDS):
        for tag, p in (('old', old), ('new', new)):
            q = S.wall(S.tex_mat(f'card_{p}.jpg', emit=.9), (-R.CARD_W / 2, 0), (R.CARD_W / 2, 0), 0, R.CARD_H)
            q.location = (x, R.SHELF_Y - .015 - (.004 if tag == 'new' else 0), z - R.CARD_H - .01)
            q.scale.x = 1.0 if tag == 'old' else .001
            S.movers[f'card{i}{tag}'] = q
    for i, (x, z, p) in enumerate(R.EXTRA):
        q = S.wall(S.tex_mat(f'card_{p}.jpg', emit=.9), (-R.CARD_W / 2, 0), (R.CARD_W / 2, 0), 0, R.CARD_H)
        q.location = (x, R.SHELF_Y - .015, z - R.CARD_H - .01)
        S.movers[f'extra{i}'] = q
    # The wall clock on the left wall: a face and two hands that turn about the wall's normal (x).
    cx, cy, cz = R.CLOCK
    r = .19
    S.wall(S.tex_mat('clock.jpg', emit=.9), (cx, cy - r), (cx, cy + r), cz - r, 2 * r)
    ink = S.flat_mat((24, 24, 24))
    for name, L, w in (('minute', .16, .014), ('hour', .1, .022)):
        q = S.quad(ink, [(0, -w / 2, -.02), (0, w / 2, -.02), (0, w / 2, L), (0, -w / 2, L)], [(0, 0), (1, 0), (1, 1), (0, 1)])
        q.location = (cx + .012 + (.004 if name == 'minute' else 0), cy, cz)
        S.movers[name] = q
    S.sun(.1, tilt=60, heading=-120)


def animate(S, t):
    g = R.grow(t)
    for i, (x, z, *_) in enumerate(R.CARDS):
        a, b = R.card_turn(i, t)
        S.movers[f'card{i}old'].scale.x = max(a, .001)
        n = S.movers[f'card{i}new']
        n.scale.x, n.scale.z = max(b, .001) * g, g
        n.location.z = z - .01 - R.CARD_H * g          # Hangs from the shelf edge; grows downwards and outwards.
        n.location.y = R.SHELF_Y - .02 - .007 * i      # Staggered, so overlapping cards don't flicker.
    for i, (x, z, p) in enumerate(R.EXTRA):
        q = S.movers[f'extra{i}']
        q.scale.x, q.scale.z = g, g
        q.location.z = z - .01 - R.CARD_H * g
        q.location.y = R.SHELF_Y - .02 - .007 * (i + 3)
    S.movers['minute'].rotation_euler.x = -R.minute_angle(t)
    S.movers['hour'].rotation_euler.x = 0.0
