"""Scene 09 blocking, as pure functions of t. No drawing imports.

Beats (no one speaks; no joke; nothing fantastic happens):
  0.00  12 September 1980, morning. The street from Scene 04, empty, shutters down. Wind. They stand on the sidewalk.
  3.00  Vehbi looks along the empty street. Sidar is not smug.
  5.50  Sidar walks to the payphone on the wall; Vehbi follows a few steps behind.
  8.60  Sidar takes out the third token and looks at it. 10.10: into the slot.
 10.80  The stamp comes down, quietly: D3. The clipping holds to the end.   End 16.60."""
import math

import room as R

END = R.END
V_START, S_START = (4.6, 4.75), (5.45, 4.65)
S_PHONE = (8.25, 5.42)
V_END = (7.35, 5.0)
S_WALK = (5.5, 8.1)
V_WALK = (6.2, 8.7)
S_TH0 = math.pi + .5
V_TH0 = -.3


def _ease(u):
    u = min(max(u, 0.0), 1.0)
    return u * u * (3 - 2 * u)


def _lerp(a, b, u):
    return (a[0] + (b[0] - a[0]) * u, a[1] + (b[1] - a[1]) * u)


def sidar(t):
    return _lerp(S_START, S_PHONE, _ease((t - S_WALK[0]) / (S_WALK[1] - S_WALK[0])))


def vehbi(t):
    return _lerp(V_START, V_END, _ease((t - V_WALK[0]) / (V_WALK[1] - V_WALK[0])))


def heading(a, b):
    return math.atan2(b[1] - a[1], b[0] - a[0])


def pos(name, t, z=0.0):
    x, y = vehbi(t) if name == 'vehbi' else sidar(t)
    return (x, y, z)
