"""Room layout and the scene's mechanical timing, as pure functions of t. No drawing imports: setdef.py (inside Blender),
acting.py, env.py and sound.py all read the same numbers, so the door, the lamp and the books agree with the acting.

Axes: x across the room (0 = desk wall, 4 = bed wall), y into the room (0 = front wall, 4.4 = door wall), z up. Metres."""
import math

W, D, H = 4.0, 4.4, 2.7          # Room size.
DOOR_X0, DOOR_X1, DOOR_H = 2.6, 3.5, 2.05
HINGE = (3.5, 4.4)               # The door swings into the room, hinged on the bed side.
DOOR_W = DOOR_X1 - DOOR_X0
CORR_Y1 = 6.0                    # Corridor runs along x behind the door wall, from y 4.4 to 6.0.
LAMP = (0.3, 1.44, 1.16)         # Under the shade: the light's source.
DESK = (0.38, 1.85)              # Desk centre on the floor.
STACK = (2.62, 3.86)             # The floor stack of books the door will hit.

# Timing, in scene seconds. Placeholders until the voices fix the timing in toon-direct.
KNOCKS = (1.0, 1.32, 1.64, 3.7, 3.95)
CRACK = (6.2, 6.7, .5)            # Vehbi opens the door a crack: start, end, angle in radians.
PUSH = (12.4, 12.75, 1.72)        # Sidar shoulders it wide open.


def _ease(u):
    u = min(max(u, 0.0), 1.0)
    return u * u * (3 - 2 * u)


def door_angle(t):
    """0 shut, positive swings into the room. A small overshoot and a bounce off the stop after the push."""
    a = 0.0
    if t >= CRACK[0]:
        a = CRACK[2] * _ease((t - CRACK[0]) / (CRACK[1] - CRACK[0]))
    if t >= PUSH[0]:
        u = (t - PUSH[0]) / (PUSH[1] - PUSH[0])
        a = CRACK[2] + (PUSH[2] - CRACK[2]) * min(u, 1.0) ** 1.6
        if u > 1:
            s = t - PUSH[1]
            a = PUSH[2] - .14 * math.exp(-s * 6) * math.cos(s * 22)
    # Each knock jolts the shut door a touch in its frame.
    for k in KNOCKS:
        if a == 0.0 and 0 <= t - k < .25:
            a = .006 * math.exp(-(t - k) * 18) * math.sin((t - k) * 60)
    return a


def door_open(t):
    """0 to 1: how open, for the light spilling into the corridor."""
    return max(door_angle(t), 0) / PUSH[2]


def lamp_shake(t):
    """Small tilt of the desk lamp, radians: it jumps at each knock and rings down. Bigger when the door slams."""
    s = 0.0
    for k in KNOCKS:
        d = t - k
        if 0 <= d < 1.2:
            s += .05 * math.exp(-d * 5) * math.sin(d * 34)
    d = t - PUSH[1]
    if 0 <= d < 1.6:
        s += .09 * math.exp(-d * 4) * math.sin(d * 30)
    return s


def stack_slide(t):
    """How far the floor stack is shoved, metres along -y, when the swinging door hits it. It skids and stops."""
    hit = PUSH[0] + (PUSH[1] - PUSH[0]) * .55
    if t < hit:
        return 0.0
    return .55 * (1 - math.exp(-(t - hit) * 7))


def stack_tilt(t):
    """The top of the stack lags, tips and settles."""
    hit = PUSH[0] + (PUSH[1] - PUSH[0]) * .55
    d = t - hit
    if d < 0 or d > 2:
        return 0.0
    return .22 * math.exp(-d * 5) * math.sin(d * 16)
