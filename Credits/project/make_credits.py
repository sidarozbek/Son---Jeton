"""Son Jeton · end credits. Renders frames with PIL, a quiet sound bed with numpy, then encodes with ffmpeg.

usage: python3 make_credits.py <out_dir>
Every credit reads "Sidar", except Vehbi's voice, which reads "Vehbi" (the person's instruction).
"""
import math, os, subprocess, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H, FPS, SR = 1280, 720, 24, 48000
END = 20.0
SS = 2                                                     # Supersampling for the token.
SANS = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
SANS_B = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
SERIF_B = '/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf'
BG = np.array((18, 15, 13), np.float32)                    # Warm near-black, out of Scene 24's black.
CREAM = (240, 228, 204)                                    # The exam sheet's paper.
GOLD = (226, 184, 80)                                      # The token's brass.
GOLD_DIM = (176, 146, 84)

# The cards: (in, out, rows). A row is (role, name) or ('#', heading).
CARDS = [
    (3.90, 7.10, [('Yazan', 'Sidar'), ('Yöneten', 'Sidar'), ('Yapımcı', 'Sidar')]),
    (7.10, 10.30, [('#', 'SESLER'), ('Sidar’ın sesi', 'Sidar'), ('Vehbi’nin sesi', 'Vehbi'), ('Diğer sesler', 'Sidar')]),
    (10.30, 13.50, [('Karakter tasarımı', 'Sidar'), ('Dekorlar', 'Sidar'), ('Animasyon', 'Sidar'), ('Kurgu', 'Sidar')]),
    (13.50, 16.70, [('Ses tasarımı', 'Sidar'), ('Tarih araştırması', 'Sidar'), ('Hikâye', 'Sidar')]),
]
TITLE = (0.60, 3.90)
LAST = (16.70, END)                                        # "Bir Sidar yapımı" and the token.
FADE = .45


def font(p, s):
    return ImageFont.truetype(p, int(s))


def env(t, a, b, f=FADE):
    """0 → 1 → 0 over [a, b] with fades of f."""
    return float(np.clip(min((t - a) / f, (b - t) / f), 0, 1))


def ease(u):
    u = min(max(u, 0.0), 1.0)
    return u * u * (3 - 2 * u)


def spaced(d, xy, text, f, fill, track, anchor='mm'):
    """Letter-spaced text, centred on xy."""
    widths = [d.textlength(ch, font=f) for ch in text]
    total = sum(widths) + track * (len(text) - 1)
    x = xy[0] - total / 2 if anchor == 'mm' else xy[0]
    for ch, w in zip(text, widths):
        d.text((x, xy[1]), ch, font=f, fill=fill, anchor='lm')
        x += w + track


def token(img, cx, cy, r, t, glint):
    """The sixth token, turning, with Scene 22's four-point glint. Drawn supersampled."""
    S = int(r * 6)
    lay = Image.new('RGBA', (S * SS, S * SS), (255, 250, 220, 0))   # Transparent but light, so the glint's edges stay bright when scaled down.
    d = ImageDraw.Draw(lay)
    c = S * SS / 2
    R = r * SS
    sq = .62 + .38 * abs(math.cos(t * 1.3))                # Turning slowly.
    d.ellipse((c - R * sq, c - R, c + R * sq, c + R), fill=GOLD + (255,), outline=(80, 56, 20, 255), width=max(int(R * .1), 1))
    d.ellipse((c - R * .62 * sq, c - R * .62, c + R * .62 * sq, c + R * .62), outline=(196, 150, 60, 255), width=max(int(R * .05), 1))
    d.ellipse((c - R * .24 * sq, c - R * .24, c + R * .24 * sq, c + R * .24), fill=(18, 15, 13, 255))
    lay = lay.resize((S, S), Image.LANCZOS)
    if glint > 0:                                          # The glint: an opaque four-point star with a soft glow.
        k = glint * (.75 + .25 * math.sin(t * 7))
        st = Image.new('RGBA', (S * SS, S * SS), (255, 250, 225, 0))
        ds = ImageDraw.Draw(st)
        L = R * (1.2 + .6 * k)
        a = t * 1.2
        gx, gy = c - R * .35 * sq, c - R * .35
        pts = []
        for i in range(8):
            rr = L if i % 2 == 0 else R * .16
            ang = a + i * math.pi / 4
            pts.append((gx + rr * math.cos(ang), gy + rr * math.sin(ang)))
        ds.polygon(pts, fill=(255, 250, 225, 255))
        st = st.resize((S, S), Image.LANCZOS)
        glow = st.filter(ImageFilter.GaussianBlur(r * .35))
        for layer, g in ((glow, .9 * k), (st, k)):
            arr = np.array(layer)
            arr[..., 3] = (arr[..., 3] * min(g, 1)).astype(np.uint8)
            lay.alpha_composite(Image.fromarray(arr))
    img.alpha_composite(lay, (int(cx - S / 2), int(cy - S / 2)))


def frame(t):
    base = np.empty((H, W, 3), np.float32)
    base[:] = BG
    yy = np.linspace(-1, 1, H)[:, None]
    xx = np.linspace(-1, 1, W)[None, :]
    vign = 1.0 + .10 * np.exp(-(xx ** 2 * .9 + yy ** 2 * 1.6) * 1.4)   # A soft pool of light.
    base *= vign[..., None]
    base += np.random.default_rng(int(t * FPS)).normal(0, 1.2, (H, W, 1)).astype(np.float32)   # Grain, so the light doesn't band.
    img = Image.fromarray(np.clip(base, 0, 255).astype(np.uint8)).convert('RGBA')
    txt = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(txt)

    # The title: SON JETON, the token as the O of JETON.
    a = env(t, *TITLE, f=.7)
    if a > 0:
        rise = (1 - ease((t - TITLE[0]) / 1.2)) * 14
        f = font(SERIF_B, 104)
        parts = ['SON JET', 'N']
        w0 = d.textlength('SON JET', font=f)
        gap = 78
        w1 = d.textlength('N', font=f)
        x0 = W / 2 - (w0 + gap + w1) / 2
        y = H / 2 - 18 + rise
        al = int(255 * a)
        d.text((x0, y), parts[0], font=f, fill=CREAM + (al,), anchor='lm')
        d.text((x0 + w0 + gap, y), parts[1], font=f, fill=CREAM + (al,), anchor='lm')
        spaced(d, (W / 2, y + 92), 'BİR SINAV HİKÂYESİ', font(SANS, 19), GOLD_DIM + (al,), 6)
        tok = Image.new('RGBA', (W, H), (0, 0, 0, 0))
        token(tok, x0 + w0 + gap / 2 + 2, y + 2, 32, t, ease((t - 1.6) / .5) * env(t, 1.6, TITLE[1], .6))
        arr = np.array(tok)
        arr[..., 3] = (arr[..., 3] * a).astype(np.uint8)
        txt.alpha_composite(Image.fromarray(arr))

    # The cards.
    for a0, b0, rows in CARDS:
        a = env(t, a0, b0)
        if a <= 0:
            continue
        drift = (t - a0) / (b0 - a0) * -10                 # A slow drift up.
        n = len(rows)
        step = 104
        top = H / 2 - (n - 1) * step / 2 + drift
        al = int(255 * a)
        for i, (role, name) in enumerate(rows):
            y = top + i * step
            if role == '#':
                spaced(d, (W / 2, y + 8), name, font(SANS_B, 22), GOLD + (al,), 9)
                d.line((W / 2 - 40, y + 32, W / 2 + 40, y + 32), fill=GOLD_DIM + (al,), width=1)
                continue
            spaced(d, (W / 2, y - 20), role.upper(), font(SANS, 20), (198, 166, 98) + (al,), 4)
            d.text((W / 2, y + 20), name, font=font(SERIF_B, 46), fill=CREAM + (al,), anchor='mm')

    # The last card: "Bir Sidar yapımı", then the token alone.
    a = env(t, LAST[0], LAST[1] + 1, f=.6)
    if a > 0:
        al = int(255 * a)
        k = 1 - ease((t - 18.4) / .9)                       # The words go; the token stays.
        if k > 0:
            spaced(d, (W / 2, H / 2 + 86), 'BİR', font(SANS, 17), GOLD_DIM + (int(al * k),), 4)
            d.text((W / 2, H / 2 + 124), 'Sidar yapımı', font=font(SERIF_B, 40), fill=CREAM + (int(al * k),), anchor='mm')
        tok = Image.new('RGBA', (W, H), (0, 0, 0, 0))
        token(tok, W / 2, H / 2 - 30, 44, t, ease((t - 17.6) / .5))
        arr = np.array(tok)
        arr[..., 3] = (arr[..., 3] * a).astype(np.uint8)
        txt.alpha_composite(Image.fromarray(arr))

    img.alpha_composite(txt)
    out = np.array(img.convert('RGB')).astype(np.float32)
    if t > END - .9:                                       # Out to black.
        out *= 1 - ease((t - (END - .9)) / .9)
    if t < .6:                                             # In from Scene 24's black.
        out *= t / .6
    return np.clip(out, 0, 255).astype(np.uint8)


def chime(sr, t0, n, gain):
    t = np.arange(int(sr * 2.4)) / sr
    x = np.zeros_like(t)
    for f, g, dcy in ((1568, 1.0, 2.2), (2349, .5, 3.0), (3136, .35, 3.8), (4699, .15, 5.0)):
        x += g * np.sin(2 * np.pi * f * t) * np.exp(-t * dcy)
    x *= np.minimum(t / .004, 1)
    out = np.zeros(n)
    i = int(t0 * sr)
    m = min(len(x), n - i)
    out[i:i + m] += x[:m] * gain
    return out


def sound():
    n = int(END * SR)
    t = np.arange(n) / SR
    rng = np.random.default_rng(7)
    # A low, warm room tone: filtered noise and a faint hum, in and out softly.
    noise = rng.standard_normal(n)
    k = np.exp(-np.arange(400) / 80.0)
    noise = np.convolve(noise, k / k.sum(), 'same')
    bed = .010 * noise + .0035 * np.sin(2 * np.pi * 110 * t) + .002 * np.sin(2 * np.pi * 165 * t)
    fade = np.clip(t / 1.5, 0, 1) * np.clip((END - t) / 1.5, 0, 1)
    x = bed * fade
    x += chime(SR, 1.62, n, .06)                            # The title's glint.
    x += chime(SR, 17.62, n, .07)                           # The last glint.
    return np.clip(x, -1, 1)


def main(out):
    os.makedirs(out, exist_ok=True)
    from scipy.io import wavfile
    wav = os.path.join(out, 'credits.wav')
    wavfile.write(wav, SR, (sound() * 32767).astype(np.int16))
    mp4 = os.path.join(out, 'Credits_v01.mp4')
    p = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS),
                          '-i', '-', '-i', wav, '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p',
                          '-c:a', 'aac', '-b:a', '160k', '-ar', str(SR), '-ac', '1', mp4], stdin=subprocess.PIPE)
    for i in range(int(END * FPS)):
        p.stdin.write(frame(i / FPS).tobytes())
    p.stdin.close()
    p.wait()
    print(mp4)


if __name__ == '__main__':
    if len(sys.argv) > 2 and sys.argv[2] == 'stills':
        ims = [Image.fromarray(frame(float(s))) for s in sys.argv[3].split(',')]
        sheet = Image.new('RGB', (W, H // 2 * ((len(ims) + 1) // 2)))
        for i, im in enumerate(ims):
            sheet.paste(im.resize((W // 2, H // 2)), ((i % 2) * W // 2, (i // 2) * H // 2))
        sheet.save(os.path.join(sys.argv[1], 'stills.jpg'))
    else:
        main(sys.argv[1])
