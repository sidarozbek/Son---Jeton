"""Scenes 10-14: the office of the imaginary "Kuş Bankerlik", 1982, as pure functions of t. No drawing imports.
The office: x 0 (left wall, the street door) to 6 (right wall), y 0 (front) to 5.5 (back wall: the teller window,
the sign, the interest board), 3.0 m high. The queue runs from the window towards the front left."""

W, D, H = 6.0, 5.5, 3.0
WINDOW = (2.6, 3.4)                      # The teller window on the back wall: x0, x1 (1.0-1.75 m up).
SILL = (3.0, D - .22, 1.02)              # Where things are put down at the window.
COUNTER = (2.4, 3.6, D - .4, D, 1.0)     # The little counter shelf in front of the window: x0, x1, y0, y1, height.
BOARD = (4.75, 5.65, 1.25, 2.05)         # The interest board on the back wall: x0, x1, z0, z1.
RATES = (30, 35, 40, 45, 50, 60, 75, 90, 120, 150)

# The queue: where each person stands, front of the line first; when they arrive (walking in from the door, left).
QUEUE_SPOTS = ((3.0, 4.75), (2.95, 4.15), (2.85, 3.55), (2.7, 2.95), (2.5, 2.4), (2.25, 1.9))
DOOR = (-.4, 2.6)

# ---- timing (Scene 11)
RATE_TIMES = (-9, -8, -7, -6, -5, -4, -3, -.5, 2.6, 6.5)    # The board starts at %90 and keeps going: %120, %150.
ARRIVALS = (-1.0, -1.0, -1.0, -1.0, -1.0, -1.0)              # The whole queue is already here.
WALK_IN = 2.2
PILE = (3.0, D - .25, 1.04)                                  # The coins on the window's counter.
HATCH = (.8, 2.2)                                            # The coins turn into birds, one after another.
FLOCK_C = (3.1, 3.4, 2.45)                                   # Where the flock circles, under the ceiling.
CARRIES = ((3.0, 5.2), (7.0, 8.8))                           # A bird carries a coin from the newest to the oldest customer.
STAMP = (9.9, 10.27, 10.55)                                  # D4.
CLIP = (10.4, 10.75, 99.0, 99.5)
PAGE = (99.0, 99.5)
END = 15.0

STAMP_HEAD = 'FAİZLER SERBEST'
STAMP_BODY = ('24 Ocak 1980 kararlarıyla faizler', 'serbest bırakıldı. Bankerler yüksek', 'faiz önerdi; sistem ancak yeni', 'müşteriler geldikçe dönebiliyordu.')
STAMP_DATE = '1981'
# Source checked 2026-11-08: Çukurova Üniversitesi İİBF Dergisi (Banker krizi makalesi, özet): "Faiz oranlarının 24 Ocak
# 1980 kararlarıyla serbest bırakılması bankerlere rahat bir çalışma ortamı sağlamıştı." / "yatırımcılara yüksek faiz
# oranları önerdiler." / "Bankerliğin devamı için yeni müşterilerin sisteme girmesi zorunluydu." The plan's "borrowing at
# ever higher rates to pay interest" is not stated in the source, so it is not on the stamp.


def rate_index(t):
    k = 0
    for i, t0 in enumerate(RATE_TIMES):
        if t >= t0:
            k = i
    return k


def flock_size(t):
    """How many birds are flying: five hatch from the coins, then more with every rise of the rate."""
    n = sum(1 for i in range(5) if t >= HATCH[0] + i * (HATCH[1] - HATCH[0]) / 4)
    if t >= RATE_TIMES[8]:
        n += 6
    if t >= RATE_TIMES[9]:
        n += 8
    n += int(max(t - 3.0, 0) * 1.2)
    return min(n, 34)


def clip(t):
    a, b, c, d = CLIP
    if t <= a:
        return 0.0
    if t < b:
        u = (t - a) / (b - a)
        return u * u * (3 - 2 * u)
    return 1.0
