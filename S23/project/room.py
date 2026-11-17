"""Scene 23: an exam hall (the present day), as pure functions of t. No drawing imports.
The hall: x 0 (left wall, the windows) to 9 (right wall), y 0 (back, the door) to 10 (front: the blackboard), 3.2 m high.
Desks in four rows facing the front (+y). Vehbi's desk is in the second row from the front, middle.
Everyone sits on a chair: the hips drop to the seat (hipdrop) and the feet go forward under the desk (fa, fb).
The montage: each question on the exam sheet (INSERT), Vehbi's whispered answer, then the stamp that taught it,
fast, each round faster."""
import math

W, D, H = 9.0, 10.0, 3.2
DESK_H = .70
V_DESK = (4.45, 6.6)                    # Vehbi's own desk: third row from the back, in the middle.
DESKS = ([(x, y) for y in (3.4, 5.0) for x in (1.6, 3.5, 5.4, 7.3)] + [(1.6, 6.6), (7.3, 6.6), (2.55, 8.2), (6.35, 8.2)])
ALL_DESKS = DESKS + [V_DESK]
SEAT_H = .42                            # Chair seat height.
CHAIR_BACK = .58                        # The chair (and the sitter) this far behind the desk's centre.
BOARD = (2.5, 6.5, 1.0, 2.3)            # The blackboard on the front wall: x0, x1, z0, z1.
CLOCK = (7.4, D - .02, 2.45)

# ---- the montage, (question insert, line, stamp flash) per answer: each round shorter.
# v02: each question held 2.2 s longer and each clipping 1.6 s longer, so they can be read.
Q = [(2.20, 5.00), (10.25, 12.90), (17.65, 20.20), (24.00, 26.48)]
L = [5.10, 13.00, 20.25, 26.55]
FLASH = [(7.90, 10.25), (15.35, 17.65), (21.70, 24.00), (28.95, 31.15)]
PEN_DOWN = 31.30
END = 33.20

ANSWERS = [
    dict(q='1. 24 Ocak kararları hangi tarihte alındı?', a='24 Ocak 1980',
         head='1 DOLAR 70 LİRA', body=('24 Ocak 1980 kararlarıyla', 'Türk lirası devalüe edildi:', '1 ABD doları 70 lira oldu.'), date='25 OCAK 1980'),
    dict(q='2. Bankerler krizi hangi yıllarda yaşandı?', a='1981–1982',
         head='BANKERLER BATTI', body=('1981–1982\'de banker sistemi çöktü.', 'Bankerlerin çoğu battı;', 'yüz binlerce kişi birikimini kaybetti.'), date='1982'),
    dict(q='3. 1980 sonrasında ihracat hangi teşviklerle desteklendi?', a='Vergi iadesi, ihracat kredisi',
         head='İHRACATA TEŞVİK', body=('1980 sonrasında ihracat;', 'vergi iadesi ve ihracat kredisi', 'gibi teşviklerle desteklendi.'), date="1980'LER"),
    dict(q='4. Sermaye hareketlerini serbestleştiren karar?', a='32 Sayılı Karar (1989)',
         head='32 SAYILI KARAR', body=('7 Ağustos 1989 tarihli', '32 Sayılı Kararla sermaye', 'hareketleri serbestleşti.'), date='AĞUSTOS 1989'),
]
# The four stamps are D1, D5, D6 and D8, word for word as they were first shown (Scenes 07, 14, 17, 22).

STAMP = (99.0, 99.2, 99.4)
CLIP = (99.0, 99.2, 99.4, 99.6)
PAGE = (99.0, 99.5)
STAMP_HEAD, STAMP_BODY, STAMP_DATE = '', (), ''


def clip(t):
    return 0.0


def written(k, t):
    """How much of answer k Vehbi has written, 0-1: while he whispers it."""
    a = L[k]
    return min(max((t - a) / 1.6, 0.0), 1.0)
