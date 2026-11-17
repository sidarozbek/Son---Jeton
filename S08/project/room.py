"""Scene 08: inside the grocer's, 25 January 1980, small hours: the labels overflow, the run to the payphone, D2, as pure functions of t. No drawing imports.
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

# The payphone on the right wall, near the front (Scene 03's design), facing into the shop (-x).
PHONE = (4.94, 1.1, 1.05)                 # x (wall face), y, bottom edge.
SLOT = (4.88, 1.19, 1.49)
# Giant standing price cards that rise out of the floor in their way: (x, y, price), facing the front. Invented prices.
STANDING = ((2.35, 1.95, '240'), (3.0, 1.3, '300'), (2.05, .85, '150'))
STAND_W, STAND_H = .7, .9
STAND_UP = (.55, .95, 1.35)               # When each one shoots up.

# ---- timing
BELL = -10.0
SWAPS = (-3.0, -2.0, -1.0)
FLIP = .3
MIDNIGHT = -1.0
CHIMES = ()
GROW = (0.0, 3.0)                         # The hanging cards keep swelling, from 2.6 to 5 times.
NOTE_OUT = 99.0
SHRINK = (99.0, 100.0)
BOOK_OPEN = 99.0
PAGE = (99.0, 99.5)
NOSE = (5.55, 5.85)                       # A small card flies off the shelf and sticks to Sidar's nose.
COIN_IN = 7.75                            # Token two into the slot.
CRACKLE = 8.05                            # The line crosses again.
STAMP = (8.4, 8.77, 9.05)                 # D2.
CLIP = (8.9, 9.25, 99.0, 99.5)            # The clipping holds to the end of the scene.
END = 13.4

STAMP_HEAD = 'İHRACATA DAYALI BÜYÜME'
STAMP_BODY = ('24 Ocak kararlarıyla fiyat kontrolleri', 'kaldırıldı, ekonomi dışa açıldı.', 'Hazırlayan: Başbakanlık Müsteşarı', 'Turgut Özal.')
STAMP_DATE = '25 OCAK 1980'
# Sources checked 2026-11-08: Karar ("Fiyat kontrol ve sınırlamaları kaldırılarak serbest piyasa uygulamasına geçildi";
# "Türk ekonomisinin dışa açılmasını hedefleyen"), Euronews Türkçe ("Başbakanlık müsteşarlığında göreve getirilen Turgut
# Özal"; "ihracata dayalı büyüme modelinin benimsenmesi"), TDV İslâm Ansiklopedisi (planlama ve başbakanlık müsteşarı).


def card_turn(i, t):
    return 0.0, 1.0


def grow(t):
    u = min(max((t - GROW[0]) / (GROW[1] - GROW[0]), 0.0), 1.0)
    return 2.6 + 2.4 * u * u * (3 - 2 * u)


def stand(i, t):
    """Height scale of standing card i: 0 until it shoots up, then 1 with a little bounce."""
    u = (t - STAND_UP[i]) / .3
    if u <= 0:
        return 0.0
    if u >= 1:
        return 1.0 + .06 * __import__('math').exp(-(u - 1) * 3) * __import__('math').sin((u - 1) * 12)
    return u * (2 - u) * 1.05


def note_scale(t):
    return 1.0


def minute_angle(t):
    return 0.0


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
