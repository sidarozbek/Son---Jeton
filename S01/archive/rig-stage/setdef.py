"""Turnaround stand-in: an empty room, so nothing blocks the orbit. The real rented room comes in toon-set."""


def build(S):
    wall = S.tex_mat('wall.jpg')
    floor = S.tex_mat('floor.jpg')
    S.room(-5, 5, -3, 7, 3.4, floor, wall, ceiling_mat=S.flat_mat((58, 50, 42)), repeat=6.0, tile=3.0)
    S.sun(.6, tilt=35, heading=30)


def animate(S, t):
    pass
