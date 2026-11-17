"""Scene 06: inside the grocer's at midnight, 24-25 January 1980 (the same shop as Scene 05), as pure functions of t. No drawing imports.
The shop: x 0 (left wall) to 5 (right wall), y 0 (front: window and door) to 5.4 (back wall of shelves), 2.8 m high.
The counter runs across the shop at y 3.4-3.9; the grocer works behind it; Sidar and Vehbi stand in front of it."""

W, D, H = 5.0, 5.4, 2.8
COUNTER = (.5, 4.5, 3.4, 3.9, .95)       # x0, x1, y0, y1, height.
SHELF_Y = D - .32                         # Front edge of the wall shelves.
SHELF_Z = (.45, .9, 1.35, 1.8, 2.25)      # Shelf boards.
LAMP = (2.5, 3.2, 2.35)                   # One pendant bulb over the counter.

# The price cards on the shelf edge that the grocer swaps: (x, z, old, new). Prices are invented.
CARDS = ((2.25, 1.35, '45', '90'), (2.6, 1.35, '120', '240'), (2.95, 1.35, '18', '36'))
CARD_W, CARD_H = .2, .13

# More cards that only grow (no flip): (x, z, price). Invented prices.
EXTRA = ((1.0, 1.8, '60'), (1.4, 1.8, '150'), (3.65, .9, '300'), (4.05, .9, '75'))
CLOCK = (.02, 3.0, 2.2)                   # The wall clock on the left wall, facing +x.

# ---- timing
BELL = -10.0                              # No bell tonight.
SWAPS = (-3.0, -2.0, -1.0)                # Scene 05's flips are long done: the cards already show the doubled prices.
FLIP = .3
MIDNIGHT = .6                             # The minute hand reaches twelve.
CHIMES = (.7, 1.45, 2.2, 2.95)            # The clock strikes (we hear four, the rest under the scene).
GROW = (2.3, 5.8)                         # The price cards swell.
NOTE_OUT = 2.5                            # Vehbi takes a banknote out of his pocket...
SHRINK = (3.1, 5.3)                       # ...and it shrinks in his fingers.
END = 10.8


def card_turn(i, t):
    """All flips happened in Scene 05: old card hidden, new card showing."""
    return 0.0, 1.0


def grow(t):
    """Scale of every price card: 1 before midnight, swelling to 2.6, with a little overshoot."""
    u = min(max((t - GROW[0]) / (GROW[1] - GROW[0]), 0.0), 1.0)
    e = u * u * (3 - 2 * u)
    return 1 + 1.6 * e + .12 * __import__('math').sin(u * 3.14159) * (u > .8)


def note_scale(t):
    """The banknote in Vehbi's fingers: 1 down to 0.35."""
    u = min(max((t - SHRINK[0]) / (SHRINK[1] - SHRINK[0]), 0.0), 1.0)
    return 1 - .65 * (u * u * (3 - 2 * u))


def minute_angle(t):
    """Minute hand, radians clockwise from twelve: a last tick onto twelve at MIDNIGHT."""
    return -.105 if t < MIDNIGHT else 0.0
