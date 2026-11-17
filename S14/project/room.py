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

# ---- Scene 14: a wall payphone on the left wall, beyond the street door (Scene 03's design), facing into the room.
PHONE = (.06, 4.25, 1.05)
SLOT14 = (.09, 4.34, 1.49)

# ---- timing (Scene 14)
RATE_TIMES = (-9, -8, -7, -6, -5, -4, -3, -2, -1, -.5)
BOARD_DARK = -1.0                                              # Dark, as Scene 13 left it.
ARRIVALS = (-1.0,) * 6
WALK_IN = 2.2
FLOCK_C = (3.1, 3.4, 2.5)
LIFT, EXIT, DOOR_OUT = -9.0, (-9.0, -8.0), (-2.5, 2.6, 1.6)
SHUTTER = -5.0                                                 # Down.
SIGN_HOOK, SIGN_FALL, SIGN_LAND = -3.0, -2.0, -1.5             # On the floor.
STAMP = (.5, .87, 1.15)                                        # D5.
CLIP = (1.0, 1.35, 5.2, 5.55)
RING = 8.45                                                    # The payphone rings and cuts Vehbi off; the line crackles.
COIN_IN = 12.9                                                 # The fourth token.
TAP, GRAB_V, GRAB_S, POP, CATCH = 99, 99, 99, 99, 99
PAGE = (99.0, 99.5)
CARRIES = ()
HATCH = (-5.0, -4.0)
PILE = (3.0, D - .25, 1.04)
END = 14.2

STAMP_HEAD = 'BANKERLER BATTI'
STAMP_BODY = ('1981–1982\'de banker sistemi çöktü.', 'Bankerlerin çoğu battı;', 'yüz binlerce kişi birikimini kaybetti.')
STAMP_DATE = '1982'
# Sources checked 2026-11-08: Sözcü ("Geçmişten günümüze banker piyasası": the market "yüzlerce gecekondu bankerle
# dolmuştu"; after 1981 "Çoğu bankerler zaten batmış"); Milli Gazete (Banker Kastelli: after the 1982 collapse "150 bin
# kişi tasfiyeye başvurdu", the chain reached 250,000 people; "Binlerce aile birikimini kaybederek mağdur oldu").
# The plan gives 100,000 families to 300,000 people depending on the source, so the stamp says "yüz binlerce".
# No banker is named.


def rate_index(t):
    return len(RATE_TIMES) - 1


def flock_size(t):
    return 0


def exit_time(i):
    return -9.0


def clip(t):
    a, b, c, d = CLIP
    if t <= a or t >= d:
        return 0.0
    if t < b:
        u = (t - a) / (b - a)
    elif t > c:
        u = 1 - (t - c) / (d - c)
    else:
        return 1.0
    return u * u * (3 - 2 * u)


def tug(t):
    return 0.0


def shutter(t):
    return 1.0


def sign_pose(t):
    return 1.4, 2.1
