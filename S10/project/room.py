"""Scenes 10-14: the office of the imaginary "Kuş Bankerlik", 1982, as pure functions of t. No drawing imports.
The office: x 0 (left wall, the street door) to 6 (right wall), y 0 (front) to 5.5 (back wall: the teller window,
the sign, the interest board), 3.0 m high. The queue runs from the window towards the front left."""

W, D, H = 6.0, 5.5, 3.0
WINDOW = (2.6, 3.4)                      # The teller window on the back wall: x0, x1 (1.0-1.75 m up).
SILL = (3.0, D - .22, 1.02)              # Where things are put down at the window.
COUNTER = (2.4, 3.6, D - .4, D, 1.0)     # The little counter shelf in front of the window: x0, x1, y0, y1, height.
BOARD = (4.75, 5.65, 1.25, 2.05)         # The interest board on the back wall: x0, x1, z0, z1.
RATES = (30, 35, 40, 45, 50, 60, 75, 90)

# The queue: where each person stands, front of the line first; when they arrive (walking in from the door, left).
QUEUE_SPOTS = ((3.0, 4.75), (2.95, 4.15), (2.85, 3.55), (2.7, 2.95), (2.5, 2.4), (2.25, 1.9))
DOOR = (-.4, 2.6)

# ---- timing (Scene 10)
RATE_TIMES = (0.0, 1.0, 1.9, 2.45, 2.85, 5.0, 6.6, 9.4)     # When the board flips to each rate.
ARRIVALS = (-1.0, -1.0, -1.0, 3.0, 4.3, 5.6)                # Queue people 4-6 walk in.
WALK_IN = 2.2
TOKENS_DOWN = 8.35                                          # Sidar slaps his two tokens on the window's counter.
END = 10.8


def rate_index(t):
    k = 0
    for i, t0 in enumerate(RATE_TIMES):
        if t >= t0:
            k = i
    return k
