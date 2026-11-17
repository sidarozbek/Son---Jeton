# Son Jeton · End credits

| Field | Value |
|---|---|
| Series | Son Jeton |
| Scene | Credits (after Scene 24) |
| Status | In review: first render delivered, awaiting the person's notes |
| Current version | v01 (`final/Credits_v01.mp4`) |
| Runtime | 20.00 s (480 frames at 24 fps) |
| Format | 1280 × 720, 24 fps, H.264, AAC 48 kHz mono |
| On-screen language | Turkish |
| Previous scene | `../S24/S24_SCENE.md` |
| Last updated | 2026-11-10 |

---

## 1. The rule (the person's instruction)

Every credit reads **Sidar**. Only Vehbi's voice reads **Vehbi**.

## 2. Cards

| Time (s) | Card | Content |
|---|---|---|
| 0.00–0.60 | — | Black (from Scene 24's black), the room tone fading in |
| 0.60–3.90 | Title | SON JETON, the sixth token standing in for the O of JETON; it glints at 1.60. Under it: BİR SINAV HİKÂYESİ |
| 3.90–7.10 | 1 | Yazan: Sidar · Yöneten: Sidar · Yapımcı: Sidar |
| 7.10–10.30 | 2 | SESLER · Sidar’ın sesi: Sidar · Vehbi’nin sesi: **Vehbi** · Diğer sesler: Sidar |
| 10.30–13.50 | 3 | Karakter tasarımı: Sidar · Dekorlar: Sidar · Animasyon: Sidar · Kurgu: Sidar |
| 13.50–16.70 | 4 | Ses tasarımı: Sidar · Tarih araştırması: Sidar · Hikâye: Sidar |
| 16.70–20.00 | Last | The token, glinting at 17.60, over "Bir Sidar yapımı"; the words go at 18.40, the token stays, out to black by 20.00 |

## 3. Look

- **Ground:** A warm near-black (18, 15, 13) with a soft pool of light and a fine grain, so it reads as Scene 24's black lifting.
- **Type:** DejaVu Serif Bold for the names and the title, in the exam sheet's cream; DejaVu Sans, letter-spaced capitals, in a dim brass for the roles. These are the same fonts as the stamps and the clippings.
- **The token:** Scene 22's sixth token (a brass oval with a hole, turning) with its four-point glint, now opaque with a soft glow.
- **Motion:** Each card fades in and out over 0.45 s and drifts up 10 px.
- **Not used:** The "Sınavda çıkar" stamp is not used here: by the series' canon, stamps carry only the documented facts D1–D8.

## 4. Sound

| Layer | What | When |
|---|---|---|
| Room tone | Low filtered noise with a faint 110/165 Hz hum, very quiet | Fading in over 1.5 s and out over the last 1.5 s |
| Chime | A bright four-partial chime, like Scene 22's glint | 1.62 and 17.62 |

There is no music, as in the rest of the series. The effects are synthesized.

## 5. Known weak points

| # | Weak point | Next step |
|---|---|---|
| 1 | The roles are the person's wording choice, "Sidar" everywhere; the tools used (the animation engine, the voice cloning) are not credited. | Add a "Yapım araçları" line if wanted. |
| 2 | The sources behind the stamps D1–D8 are in each scene's `SCENE.md`, not on screen. | A "Kaynaklar" card if the film is shown publicly. |
| 3 | At 20 s the cards hold 3.2 s each: enough to read, but not slow. | Longer cards if wanted. |
| 4 | The sound is synthesized. | The person checks the balance. |

## 6. Decisions log

| Date | Decision | By |
|---|---|---|
| 2026-11-10 | All credits "Sidar", only Vehbi's voice "Vehbi" | The person |
| 2026-11-10 | Cards rather than a roll, so every line is readable in 20 s | Claude |
| 2026-11-10 | The sixth token as the title's O and as the last image: the film's object, glinting | Claude |
| 2026-11-10 | "Bir sınav hikâyesi" under the title, and the extra roles (Hikâye, Tarih araştırması and so on), so the cards read as a full credit list | Claude |

## 7. Files

| Path | What |
|---|---|
| `CREDITS_SCENE.md` | This document |
| `final/Credits_v01.mp4`, `final/Credits_v01_contact-sheet.jpg` | First render and its contact sheet (one frame a second) |
| `project/make_credits.py` | Renders the frames (PIL), the sound (numpy) and encodes (ffmpeg) |

## 8. How to re-render

```
python3 project/make_credits.py final                  # about 30 s
python3 project/make_credits.py . stills 2.4,8.7,18.0  # a still sheet
```
Change the names in `CARDS` at the top of the script.
