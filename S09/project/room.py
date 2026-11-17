"""Scene 09: the same street (Scene 04) on the morning of 12 September 1980: empty, silent, shutters down.
Scene 04: a street on the evening of 24 January 1980, as pure functions of t. No drawing imports.
The road runs along x. Cameras stand in the road (low y); the far sidewalk and the facades are at the back (high y).
  y 0.0-4.2   cobbled road
  y 4.2-6.0   sidewalk, kerb at 4.2
  y 6.0       the facades: ground-floor walls, the grocer's front (x 4.4-7.6), upper floors above 3.2 m"""

ROAD_Y1 = 4.2
FACADE_Y = 6.0
X0, X1 = -8.0, 20.0
GROUND_H = 3.2                       # Height of the ground floor; the upper facade starts here.
UPPER_H = 8.8
SHOP_X0, SHOP_X1 = 4.4, 7.6          # The grocer's front.
SHOP_WIN = (4.52, 6.7, .95, 2.45)    # Its lit window: x0, x1, z0, z1.
CAL = (4.66, 5.0, 1.28, 1.72)       # The tear-off calendar hanging inside the glass: x0, x1, z0, z1.
CAL_Y = FACADE_Y - .015
LAMP_POST = (2.3, 4.45)              # A street lamp at the kerb.
LAMP_HEAD = (2.3, 4.05, 4.05)        # Its lamp, on an arm over the road.
WIN_LIGHT = (5.6, FACADE_Y + .3, 1.7)

PHONE_X = 8.4                         # A wall payphone on the facade, right of the grocer (Scene 03's design).
PHONE_Z0 = 1.05
SLOT = (PHONE_X + .09, FACADE_Y - .07, PHONE_Z0 + .44)

# ---- timing
TOKEN_OUT = 8.6                       # Sidar takes out the third token and looks at it.
COIN_IN = 10.1                        # Into the slot, without a word.
STAMP = (10.8, 11.2, 11.5)            # D3. Quieter than the others.
CLIP = (11.35, 11.75, 99.0, 99.5)     # Holds to the end.
END = 16.6

STAMP_HEAD = '12 EYLÜL 1980'
STAMP_BODY = ('Askerî darbeden sonra', '24 Ocak kararları', 'uygulanmaya devam etti.')
STAMP_DATE = 'EYLÜL 1980'
# Sources checked 2026-11-08: Milliyet Uzmanpara ("Türkiye ekonomisinde Özallı yıllar": after 12 September Özal became
# Deputy Prime Minister for the economy; "Gelen yönetim 24 Ocak Kararları ile başladığımız işe devam etmemi istedi.");
# Medyascope ("12 Eylül darbesiyle uygulanma imkanı bulan 24 Ocak Kararları").


def clip(t):
    a, b, c, d = CLIP
    if t <= a or t >= d:
        return 0.0
    if t < b:
        u = (t - a) / (b - a)
    else:
        return 1.0
    return u * u * (3 - 2 * u)

PAGE = (99.0, 99.5)                   # No textbook insert in this scene.
