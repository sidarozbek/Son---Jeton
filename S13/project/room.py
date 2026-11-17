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
QUEUE_SPOTS = ((3.0, 4.75), (2.95, 4.15), (2.85, 3.55), (2.7, 2.95), (2.5, 2.4), (2.25, 1.9))   # Back in line at the window.
DOOR = (-.4, 2.6)

# ---- Scene 12: the blackboard on its easel, and the slot where the tokens are stuck.
BOARD_C = (4.2, 5.4, 3.9, .8, 1.7)                           # Chalkboard: x0, x1, y, z0, z1 (faces the front).
SLOT = (3.0, D - .02, 1.03)                                  # The teller window's slot.

# ---- Scene 13: the sign as its own board, hung from two hooks over the partition.
SIGN = (1.4, 4.6, 2.12, 2.65)                                # x0, x1, z0, z1.

# ---- timing (Scene 13). No one speaks. No joke.
RATE_TIMES = (-9, -8, -7, -6, -5, -4, -3, -2, -1, -.5)       # %150, until the board goes dark.
BOARD_DARK = 5.6
ARRIVALS = (-1.0,) * 6
WALK_IN = 2.2
FLOCK_C = (3.1, 3.4, 2.5)
LIFT = 2.8                                                    # The whole flock lifts at once...
EXIT = (3.2, 5.4)                                             # ...and streams out of the street door, bird after bird.
DOOR_OUT = (-2.5, 2.6, 1.6)
SHUTTER = 5.6                                                 # The teller window's shutter comes down.
SIGN_HOOK = 10.0                                              # One hook of the sign gives; it swings...
SIGN_FALL = 10.9                                              # ...and drops to the floor.
SIGN_LAND = 11.35
TAP, GRAB_V, GRAB_S, POP, CATCH = 99, 99, 99, 99, 99
STAMP = (99.0, 99.5, 99.8)
CLIP = (99.0, 99.5, 99.8, 99.9)
PAGE = (99.0, 99.5)
STAMP_HEAD, STAMP_BODY, STAMP_DATE = '', (), ''
CARRIES = ()
HATCH = (-5.0, -4.0)
PILE = (3.0, D - .25, 1.04)
END = 14.6


def rate_index(t):
    return len(RATE_TIMES) - 1


def flock_size(t):
    return 34


def exit_time(i):
    return EXIT[0] + (EXIT[1] - EXIT[0]) * ((i * 7) % 34) / 34


def clip(t):
    return 0.0


def tug(t):
    return 0.0


def shutter(t):
    """0 open, 1 down."""
    u = min(max((t - SHUTTER) / .35, 0.0), 1.0)
    return u * u


def sign_pose(t):
    """(angle about its left hook in radians, drop in metres). It swings down on its left hook, then falls."""
    import math
    if t < SIGN_HOOK:
        return 0.0, 0.0
    if t < SIGN_FALL:
        u = (t - SIGN_HOOK) / (SIGN_FALL - SIGN_HOOK)
        a = .5 * (1 - math.exp(-u * 4)) + .08 * math.sin(u * 14) * math.exp(-u * 3)
        return a, 0.0
    u = min((t - SIGN_FALL) / (SIGN_LAND - SIGN_FALL), 1.0)
    return .5 + .9 * u, 2.1 * u * u
