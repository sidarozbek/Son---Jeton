"""Scene 05: inside the grocer's, the evening of 24 January 1980, as pure functions of t. No drawing imports.
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

# ---- timing
BELL = 0.0                                # The door bell, still ringing from their coming in.
TURN = 3.9                                # The grocer turns his back to them.
SWAPS = (5.1, 6.6, 8.1)                   # Each card flips over to its new price.
FLIP = .3                                 # Seconds for one card to flip.
TURN_BACK = 9.55                          # He turns round again, all innocence.
END = 13.8


def card_turn(i, t):
    """For card i: (scale of the old card, scale of the new card) across its flip; each goes 1 -> 0 or 0 -> 1."""
    t0 = SWAPS[i]
    u = (t - t0) / FLIP
    if u <= 0:
        return 1.0, 0.0
    if u >= 1:
        return 0.0, 1.0
    return (max(1 - 2 * u, 0.0), max(2 * u - 1, 0.0))
