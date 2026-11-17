"""Scene 23 blocking, as pure functions of t. No drawing imports. The exam hall; everyone seated, heads down.

Beats (v02: questions and clippings held longer):
  0.00  The exam hall, quiet. Rows of students bent over their sheets; a proctor at the front; the clock.
  2.20  INSERT: question 1 on Vehbi's sheet.  5.10 he whispers, writing: "January 24th, 1980."  7.90: the stamp (D1).
 10.25  INSERT: question 2. 13.00 "Bankers' crisis, '81 to '82."  15.35: the stamp (D5).
 17.65  INSERT: question 3. 20.25 "Export tax refunds."  21.70: the stamp (D6).
 24.00  INSERT: question 4. 26.55 "Decision thirty-two, 1989."  28.95: the stamp (D8).
 31.30  Pen down. He sits back.   End 33.20."""
import math

import room as R

END = R.END
V_POS = (R.V_DESK[0], R.V_DESK[1] - R.CHAIR_BACK)
PROCTOR = (8.2, 9.2)
STUDENTS = [(x, y - R.CHAIR_BACK) for x, y in R.DESKS]
V_TH0 = math.pi / 2                       # Facing the front.


def where(name, t):
    if name == 'vehbi':
        return V_POS
    if name == 'proctor':
        return PROCTOR
    return STUDENTS[int(name[1:])]


def pos(name, t, z=0.0):
    x, y = where(name, t)
    return (x, y, z)
