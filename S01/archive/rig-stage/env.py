"""Turnaround: only floating dust. The room's life comes in toon-set."""
from toonkit.fx import Precip


class Env:
    def __init__(self, cfg, cast):
        self.dust = Precip('dust', n=80, color=(250, 235, 200, 90), fall=.05, drift=.08, size=.006)

    def step(self, t, dt, n):
        pass

    def top(self, c, ctx):
        self.dust.draw(c, ctx)
