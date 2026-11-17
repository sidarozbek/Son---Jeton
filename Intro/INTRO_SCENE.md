# Son Jeton · Opening titles

| Field | Value |
|---|---|
| Series | Son Jeton |
| Scene | Intro (before Scene 01) |
| Status | In review: first render delivered, awaiting the person's notes |
| Current version | v01 (`final/Intro_v01.mp4`) |
| Runtime | 12.00 s (288 frames at 24 fps) |
| Format | 1280 × 720, 24 fps, H.264, AAC 48 kHz mono |
| On-screen language | Turkish (the years and the title) |
| Next scene | `../S01/S01_SCENE.md` |
| Last updated | 2026-11-10 |

---

## 1. Idea

The film's whole stretch and its object in twelve seconds: the years 1980 → 1989 count behind, Sidar's five tokens drop in one by one, gather into one, and that one becomes the O of SON JETON, which glints. It shares its look with the end credits (`../Credits/CREDITS_SCENE.md`), so the film opens and closes the same way.

## 2. Beat sheet

| Time (s) | Beat |
|---|---|
| 0.00–0.50 | Up from black |
| 0.55–5.70 | The year counter, large and faint behind: 1980, then each year sliding up into place to 1989, with a soft tick |
| 0.90, 1.68, 2.46, 3.24, 4.02 | A token drops, spinning, clinks on the floor, bounces twice, settles face-on; five in a row |
| 5.55–6.55 | The five slide together into the place of the O; four fade into the fifth, with small clinks |
| 6.55–7.45 | SON JET and N slide in around it |
| 7.65 | The glint (Scene 22's four-point star), with a chime |
| 8.20 | BİR SINAV HİKÂYESİ |
| 11.10–12.00 | Out to black; Scene 01 follows |

## 3. Look and sound

- **Look:** As in the end credits: a warm near-black with a soft pool of light and grain; DejaVu Serif Bold for the title in the exam sheet's cream; the brass token with a hole (Scene 22's sixth token).
- **Years:** Shown as plain years only, not as facts; no stamp is used (by the canon, stamps carry only D1–D8).
- **Sound:** A quiet room tone; a synthesized brass clink for each landing and bounce; a soft tick for each year; the chime at the glint. No music, as in the rest of the series.

## 4. Known weak points

| # | Weak point | Next step |
|---|---|---|
| 1 | The tokens are flat 2D shapes; spinning is a squash of the oval, not a true 3D coin. | Fine at this size. |
| 2 | The year counter is faint by design; on a dim screen it may hardly show. | Raise its opacity (`26` in `frame`) if wanted. |
| 3 | Five tokens drop, though in the film the fifth is lost and the sixth found; the intro doesn't tell that. | Intended: the intro only sets up the five. |
| 4 | The sound is synthesized. | The person checks the balance. |

## 5. Decisions log

| Date | Decision | By |
|---|---|---|
| 2026-11-10 | The intro: five tokens and the years 1980 → 1989 becoming the title; same look as the credits | Claude |

## 6. Files and re-render

| Path | What |
|---|---|
| `final/Intro_v01.mp4`, `final/Intro_v01_contact-sheet.jpg` | First render and its contact sheet (two frames a second) |
| `project/make_intro.py` | Frames (PIL), sound (numpy), encode (ffmpeg); timings at the top |

```
python3 project/make_intro.py final                 # about 20 s
python3 project/make_intro.py . stills 1.2,5.2,8.6  # a still sheet
```
