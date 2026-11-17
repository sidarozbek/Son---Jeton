"""Turnaround: a quiet room bed only."""


def score(m, cfg):
    m.bed(wind=.0, hum=.012, hum_f=(60, 120))
