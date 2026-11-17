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
QUEUE_SPOTS = ((1.95, 4.5), (2.1, 3.85), (1.9, 3.25), (1.6, 2.7), (1.35, 2.2), (1.1, 1.7))   # Scene 12: stepped back from the window to watch.
DOOR = (-.4, 2.6)

# ---- Scene 12: the blackboard on its easel, and the slot where the tokens are stuck.
BOARD_C = (4.2, 5.4, 3.9, .8, 1.7)                           # Chalkboard: x0, x1, y, z0, z1 (faces the front).
SLOT = (3.0, D - .02, 1.03)                                  # The teller window's slot.

# ---- timing (Scene 12)
RATE_TIMES = (-9, -8, -7, -6, -5, -4, -3, -2, -1, -.5)       # The board stays at %150.
ARRIVALS = (-1.0, -1.0, -1.0, -1.0, -1.0, -1.0)
WALK_IN = 2.2
FLOCK_C = (3.1, 3.4, 2.5)
TAP = 5.0                                                    # Vehbi taps the end of the curve: "Here".
GRAB_V, GRAB_S = 10.35, 12.0                                 # Vehbi grabs the stuck tokens; Sidar grabs on behind him.
POP = 13.25                                                  # They come out.
CATCH = 13.75                                                # Sidar has them back.
STAMP = (99.0, 99.5, 99.8)
CLIP = (99.0, 99.5, 99.8, 99.9)
PAGE = (99.0, 99.5)
STAMP_HEAD, STAMP_BODY, STAMP_DATE = '', (), ''
END = 15.0


def rate_index(t):
    k = 0
    for i, t0 in enumerate(RATE_TIMES):
        if t >= t0:
            k = i
    return k


def flock_size(t):
    return 34


def clip(t):
    return 0.0


def tug(t):
    """How far the stuck tokens have been pulled out of the slot, in metres, wobbling as they tug."""
    import math
    if t < GRAB_V:
        return 0.0
    if t < POP:
        k = .6 if t < GRAB_S else 1.0
        return .006 * k * (1 + math.sin((t - GRAB_V) * 13))
    return 0.0

CARRIES = ()                                                 # No carries in this scene.
HATCH = (-5.0, -4.0)                                         # The birds hatched long ago (Scene 11).
PILE = (3.0, D - .25, 1.04)
