"""Son Jeton · opening titles. Renders frames with PIL, the sound with numpy, encodes with ffmpeg.

usage: python3 make_intro.py <out_dir>            render
       python3 make_intro.py <dir> stills t1,t2   a still sheet

The years 1980 → 1989 count behind; Sidar's five tokens drop in one by one, gather into one,
and the one becomes the O of SON JETON, which glints. Same look as the end credits.
"""
import math, os, subprocess, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H, FPS, SR = 1280, 720, 24, 48000
END = 12.0
SS = 2
SANS = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
SERIF_B = '/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf'
BG = np.array((18, 15, 13), np.float32)
CREAM = (240, 228, 204)
GOLD = (226, 184, 80)
GOLD_DIM = (176, 146, 84)

N = 5
DROP = [0.90 + i * .78 for i in range(N)]      # When each token starts to fall.
FALL = .42                                      # Seconds to the floor.
FLOOR = H / 2 + 150
GAP = 128
YEARS = (0.55, 5.70)                            # The year counter, 1980 → 1989.
GATHER = (5.55, 6.55)                           # The five slide into one.
TITLE_IN = (6.55, 7.45)                         # The letters arrive around it.
GLINT = 7.65
SUB = 8.20
OUT = (11.10, 12.00)
R_TOK = 30                                      # The token's radius in the row.
R_O = 32                                        # As the O of JETON.


def font(p, s):
    return ImageFont.truetype(p, int(s))


def ease(u):
    u = min(max(u, 0.0), 1.0)
    return u * u * (3 - 2 * u)


def spaced(d, xy, text, f, fill, track):
    widths = [d.textlength(ch, font=f) for ch in text]
    x = xy[0] - (sum(widths) + track * (len(text) - 1)) / 2
    for ch, w in zip(text, widths):
        d.text((x, xy[1]), ch, font=f, fill=fill, anchor='lm')
        x += w + track


def title_geometry(d):
    f = font(SERIF_B, 104)
    w0, w1, gap = d.textlength('SON JET', font=f), d.textlength('N', font=f), 78
    x0 = W / 2 - (w0 + gap + w1) / 2
    return f, x0, w0, gap, H / 2 - 18


def token(img, cx, cy, r, sq, glint, t, alpha=1.0):
    """A brass token with a hole; sq is how face-on it is (1 face-on, ~0 edge-on). Scene 22's glint."""
    S = int(r * 7)
    lay = Image.new('RGBA', (S * SS, S * SS), (255, 250, 225, 0))
    d = ImageDraw.Draw(lay)
    c, R = S * SS / 2, r * SS
    sq = max(sq, .07)
    d.ellipse((c - R * sq, c - R, c + R * sq, c + R), fill=GOLD + (255,), outline=(80, 56, 20, 255), width=max(int(R * .1), 1))
    if sq > .25:
        d.ellipse((c - R * .62 * sq, c - R * .62, c + R * .62 * sq, c + R * .62), outline=(196, 150, 60, 255), width=max(int(R * .05), 1))
        d.ellipse((c - R * .24 * sq, c - R * .24, c + R * .24 * sq, c + R * .24), fill=(18, 15, 13, 255))
    lay = lay.resize((S, S), Image.LANCZOS)
    if glint > 0:
        k = glint * (.75 + .25 * math.sin(t * 7))
        st = Image.new('RGBA', (S * SS, S * SS), (255, 250, 225, 0))
        ds = ImageDraw.Draw(st)
        L, a = R * (1.2 + .6 * k), t * 1.2
        gx, gy = c - R * .35 * sq, c - R * .35
        pts = [(gx + (L if i % 2 == 0 else R * .16) * math.cos(a + i * math.pi / 4),
                gy + (L if i % 2 == 0 else R * .16) * math.sin(a + i * math.pi / 4)) for i in range(8)]
        ds.polygon(pts, fill=(255, 250, 225, 255))
        st = st.resize((S, S), Image.LANCZOS)
        glow = st.filter(ImageFilter.GaussianBlur(r * .35))
        for layer, g in ((glow, .9 * k), (st, k)):
            arr = np.array(layer)
            arr[..., 3] = (arr[..., 3] * min(g, 1)).astype(np.uint8)
            lay.alpha_composite(Image.fromarray(arr))
    if alpha < 1:
        arr = np.array(lay)
        arr[..., 3] = (arr[..., 3] * alpha).astype(np.uint8)
        lay = Image.fromarray(arr)
    img.alpha_composite(lay, (int(cx - S / 2), int(cy - S / 2)))


def bounce(u):
    """Height above the floor (px) and spin speed, u seconds after the drop starts."""
    g = 2 * 420 / FALL ** 2                     # Falls 420 px in FALL seconds.
    if u < FALL:
        return 420 - .5 * g * u * u
    u -= FALL
    for h in (34.0, 9.0):                       # Two small bounces.
        T = 2 * math.sqrt(2 * h / g)
        if u < T:
            v = math.sqrt(2 * g * h)
            return v * u - .5 * g * u * u
        u -= T
    return 0.0


def token_state(i, t):
    """(x, y, sq, alpha) of token i at time t, or None."""
    u = t - DROP[i]
    if u < 0:
        return None
    x = W / 2 + (i - (N - 1) / 2) * GAP
    y = FLOOR - bounce(u)
    land = FALL + .55
    spin = 1 - ease((u - FALL) / .9)            # Spinning as it falls, settling face-on.
    sq = abs(math.cos(u * 11 * max(spin, .0) + i)) * spin + (1 - spin)
    _, x0, w0, gap, ty = TITLE_GEO
    g = ease((t - GATHER[0]) / (GATHER[1] - GATHER[0]))
    tx, tyy = x0 + w0 + gap / 2 + 2, ty + 2
    x = x + (tx - x) * g
    y = y + (tyy - y) * g
    alpha = 1.0 if i == N - 1 or g < .85 else max(0.0, 1 - (g - .85) / .15)   # The last one stays.
    return x, y, sq, alpha


def frame(t):
    base = np.empty((H, W, 3), np.float32)
    base[:] = BG
    yy = np.linspace(-1, 1, H)[:, None]
    xx = np.linspace(-1, 1, W)[None, :]
    base *= (1.0 + .10 * np.exp(-(xx ** 2 * .9 + yy ** 2 * 1.6) * 1.4))[..., None]
    base += np.random.default_rng(int(t * FPS) + 99).normal(0, 1.2, (H, W, 1)).astype(np.float32)
    img = Image.fromarray(np.clip(base, 0, 255).astype(np.uint8)).convert('RGBA')
    lay = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(lay)

    # The years, large and faint behind, flipping 1980 → 1989.
    a = min(ease((t - YEARS[0]) / .4), 1 - ease((t - (YEARS[1] - .5)) / .6))
    if a > 0:
        span = (YEARS[1] - .6 - YEARS[0]) / 9
        k = int(min(max((t - YEARS[0]) / span, 0), 9))
        ph = (t - YEARS[0]) / span - k              # Each year slides up into place.
        sl = 1 - ease(ph / .25) if k > 0 else 0
        fy = font(SERIF_B, 300)
        d.text((W / 2, H / 2 - 60 + sl * 26), str(1980 + k), font=fy, fill=(240, 228, 204, int(26 * a * (1 - .6 * sl))), anchor='mm')

    # The title letters, then the subtitle.
    f, x0, w0, gap, ty = TITLE_GEO
    a = ease((t - TITLE_IN[0]) / (TITLE_IN[1] - TITLE_IN[0]))
    if a > 0:
        s = (1 - a) * 40
        al = int(255 * a)
        d.text((x0 - s, ty), 'SON JET', font=f, fill=CREAM + (al,), anchor='lm')
        d.text((x0 + w0 + gap + s, ty), 'N', font=f, fill=CREAM + (al,), anchor='lm')
    a = ease((t - SUB) / .6)
    if a > 0:
        spaced(d, (W / 2, ty + 92), 'BİR SINAV HİKÂYESİ', font(SANS, 19), GOLD_DIM + (int(255 * a),), 6)
    img.alpha_composite(lay)

    # The tokens, the last one on top.
    for i in range(N):
        st = token_state(i, t)
        if st is None or st[3] <= 0:
            continue
        x, y, sq, al = st
        g = ease((t - GATHER[0]) / (GATHER[1] - GATHER[0]))
        r = R_TOK + (R_O - R_TOK) * g
        if g >= 1:                                  # Now the O: turning slowly, as in the credits.
            sq = .62 + .38 * abs(math.cos((t - GATHER[1]) * 1.3))
        gl = ease((t - GLINT) / .5) if i == N - 1 else 0
        token(img, x, y, r, sq, gl, t, al)

    out = np.array(img.convert('RGB')).astype(np.float32)
    if t < .5:
        out *= t / .5
    if t > OUT[0]:
        out *= 1 - ease((t - OUT[0]) / (OUT[1] - OUT[0]))
    return np.clip(out, 0, 255).astype(np.uint8)


# ---------------- Sound
def partials(sr, spec, dur):
    t = np.arange(int(sr * dur)) / sr
    x = sum(g * np.sin(2 * np.pi * f * t) * np.exp(-t * dc) for f, g, dc in spec)
    return x * np.minimum(t / .002, 1)


def place(buf, x, t0, gain):
    i = int(t0 * SR)
    m = min(len(x), len(buf) - i)
    if m > 0:
        buf[i:i + m] += x[:m] * gain


def sound():
    n = int(END * SR)
    t = np.arange(n) / SR
    rng = np.random.default_rng(7)
    noise = rng.standard_normal(n)
    k = np.exp(-np.arange(400) / 80.0)
    noise = np.convolve(noise, k / k.sum(), 'same')
    x = (.010 * noise + .0035 * np.sin(2 * np.pi * 110 * t) + .002 * np.sin(2 * np.pi * 165 * t))
    x *= np.clip(t / 1.0, 0, 1) * np.clip((END - t) / .9, 0, 1)
    # Brass on a hard floor: inharmonic partials, short.
    clink = partials(SR, ((2380, 1, 30), (3910, .6, 38), (5630, .4, 46), (7240, .25, 60)), .35)
    tick = partials(SR, ((1900, 1, 140), (3700, .4, 180)), .06)
    for i, d0 in enumerate(DROP):
        g = 2 * 420 / FALL ** 2
        tl = d0 + FALL
        place(x, clink, tl, .16)
        T1 = 2 * math.sqrt(2 * 34 / g)
        place(x, clink, tl + T1, .07)
        place(x, clink, tl + T1 + 2 * math.sqrt(2 * 9 / g), .03)
    span = (YEARS[1] - .6 - YEARS[0]) / 9
    for k_ in range(1, 10):                         # A soft tick at each year.
        place(x, tick, YEARS[0] + k_ * span, .05)
    for j in range(4):                              # The four gathering into the fifth.
        place(x, clink, GATHER[0] + .55 + j * .09, .06)
    chime = partials(SR, ((1568, 1, 2.2), (2349, .5, 3.0), (3136, .35, 3.8), (4699, .15, 5.0)), 2.4)
    place(x, chime, GLINT + .02, .07)
    return np.clip(x, -1, 1)


def main(out):
    os.makedirs(out, exist_ok=True)
    from scipy.io import wavfile
    wav = os.path.join(out, 'intro.wav')
    wavfile.write(wav, SR, (sound() * 32767).astype(np.int16))
    mp4 = os.path.join(out, 'Intro_v01.mp4')
    p = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS),
                          '-i', '-', '-i', wav, '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p',
                          '-c:a', 'aac', '-b:a', '160k', '-ar', str(SR), '-ac', '1', mp4], stdin=subprocess.PIPE)
    for i in range(int(END * FPS)):
        p.stdin.write(frame(i / FPS).tobytes())
    p.stdin.close()
    p.wait()
    os.remove(wav)
    print(mp4)


TITLE_GEO = title_geometry(ImageDraw.Draw(Image.new('RGB', (8, 8))))

if __name__ == '__main__':
    if len(sys.argv) > 2 and sys.argv[2] == 'stills':
        ims = [Image.fromarray(frame(float(s))) for s in sys.argv[3].split(',')]
        sheet = Image.new('RGB', (W, H // 2 * ((len(ims) + 1) // 2)))
        for i, im in enumerate(ims):
            sheet.paste(im.resize((W // 2, H // 2)), ((i % 2) * W // 2, (i // 2) * H // 2))
        sheet.save(os.path.join(sys.argv[1], 'stills.jpg'))
    else:
        main(sys.argv[1])
