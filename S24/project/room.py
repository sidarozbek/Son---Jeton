"""Scene 24: the corridor outside the exam hall, as pure functions of t. No drawing imports.
The corridor: x 0 (left wall: the exam hall's door at y 9.2) to 3.0 (right wall), y 0 (behind the cameras) to 14
(the end wall: a tall window), 3.0 m high."""
W, D, H = 3.0, 14.0, 3.0
DOOR = (9.2, 1.1)                       # The exam hall's door on the left wall: centre y, width.

L1, L2 = 3.00, 5.90                     # The friend; Vehbi.
STOP = 4.30                             # Vehbi stops.
BLACK = 8.40                            # Cut to black.
END = 11.00

STAMP = (99.0, 99.2, 99.4)
CLIP = (99.0, 99.2, 99.4, 99.6)
PAGE = (99.0, 99.5)
STAMP_HEAD, STAMP_BODY, STAMP_DATE = '', (), ''


def clip(t):
    return 0.0
