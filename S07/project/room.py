"""Scene 07: inside the grocer's just after midnight, 25 January 1980 (Scene 06 continues): the first stamp, as pure functions of t. No drawing imports.
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
BELL = -10.0
SWAPS = (-3.0, -2.0, -1.0)
FLIP = .3
MIDNIGHT = -1.0
CHIMES = ()
GROW = (-5.0, -4.0)                       # The cards stay swollen from Scene 06.
NOTE_OUT = 99.0                           # The banknote is back in his pocket.
SHRINK = (99.0, 100.0)
STAMP = (.25, .62, .9)                    # The rubber stamp: comes down, hits at .62, lifts away by .9.
CLIP = (.75, 1.1, 4.7, 5.05)              # The picture turns into a newspaper clipping, holds, and comes back.
BOOK_OPEN = 5.0                           # Vehbi opens the book to the page and holds it up.
PAGE = (5.05, 7.4)                        # INSERT: the textbook page.
END = 17.6

# The stamp's text: the only documented fact in the scene. Sources: the plan's D1 row (CNN Türk), checked again on
# 2026-11-08 against ekonomim.com (dolar 47 liradan 70 liraya). Sources disagree on when the daily rate began, so the
# stamp says only what they agree on.
STAMP_HEAD = '1 DOLAR 70 LİRA'
STAMP_BODY = ('24 Ocak 1980 kararlarıyla', 'Türk lirası devalüe edildi:', '1 ABD doları 70 lira oldu.')
STAMP_DATE = '25 OCAK 1980'


def card_turn(i, t):
    return 0.0, 1.0


def grow(t):
    return 2.6


def note_scale(t):
    return 1.0


def minute_angle(t):
    return 0.0


def clip(t):
    """0 = the picture, 1 = the newspaper clipping."""
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
