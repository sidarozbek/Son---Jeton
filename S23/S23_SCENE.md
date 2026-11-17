# Son Jeton · Scene 23 · The Exam

| Field | Value |
|---|---|
| Series | Son Jeton |
| Scene | 23 of 24 |
| Title | The Exam |
| Status | In review: v03 delivered (the exam is Türkiye Ekonomisi), awaiting the person's notes |
| Current version | v03 (`final/S23_v03.mp4`): v02 with the exam sheet's header corrected |
| Runtime | 33.17 s (796 frames at 24 fps); v01 was 18.00 s |
| Format | 1280 × 720, 24 fps, H.264, AAC 48 kHz |
| Location | An exam hall, the present day, morning |
| Period | The present day |
| Characters | Vehbi; twelve students and a proctor (silent) |
| Spoken language | English (whispered); the exam sheet and the stamps are in Turkish |
| Stamp | D1, D5, D6, D8 again, fast |
| Series canon | `../00_Series/BIBLE.md`; story plan in `../00_Series/SCENE-INDEX.md`; lines in `../00_Series/DIALOGUE-DRAFT.md` |
| Previous scene | `../S22/S22_SCENE.md` |
| Next scene | `../S24/S24_SCENE.md` |
| Last updated | 2026-11-10 |

---

## 1. Logline

In the exam hall Vehbi answers question after question in a whisper, and each answer is cut against the stamp that taught it, faster each time.

## 2. Purpose

- **What it shows:** Why the stamps mattered. Each exam question is answered with exactly the fact one "Sınavda çıkar" stamp gave.
- **The stamps:** Exactly as first shown (D1 in Scene 07, D5 in Scene 14, D6 in Scene 17, D8 in Scene 22), word for word. No new facts are introduced.
- **The rhythm:** Each round is shorter: a question, a whispered answer, a stamp, then faster.

## 3. Synopsis

A quiet exam hall: rows of students bent over their sheets, a proctor at the front, SINAV chalked on the blackboard, a clock. Insert: Vehbi's sheet, question 1 marked: "24 Ocak kararları hangi tarihte alındı?" He whispers as he writes: "January 24th, 1980." The stamp comes down: "1 DOLAR 70 LİRA". Question 2: "Bankers' crisis, '81 to '82." The stamp: "BANKERLER BATTI". Question 3, faster: "Export tax refunds." The stamp: "İHRACATA TEŞVİK". Question 4, fastest: "Decision thirty-two, 1989." The stamp: "32 SAYILI KARAR". Pen down. He sits back and almost smiles.

### From the story plan (canon, verbatim)

| Field | Story plan |
|---|---|
| Plan timecode | 7:20 |
| Part | Final |
| What happens | Sınav salonu. Vehbi soruları hızla yanıtlar. Sorular damgaların hızlı tekrarıyla kesilir. |
| Joke or surprise | İzleyici damgaların neden önemli olduğunu burada görür. |
| “Sınavda çıkar” stamp | — (D1, D5, D6, D8 recalled) |

## 4. Beat sheet

v02 timings (v01's are in the decisions log).

| Time (s) | Question insert | Answer | Stamp flash |
|---|---|---|---|
| 0.00–2.20 | — | The hall | — |
| 2.20–5.00 | Q1 | 5.10 "January 24th, 1980." | 7.90–10.25 D1 |
| 10.25–12.90 | Q2 (Q1's answer now written) | 13.00 "Bankers' crisis, '81 to '82." | 15.35–17.65 D5 |
| 17.65–20.20 | Q3 | 20.25 "Export tax refunds." | 21.70–24.00 D6 |
| 24.00–26.48 | Q4 | 26.55 "Decision thirty-two, 1989." | 28.95–31.15 D8 |
| 31.30 | — | Pen down; he sits back, almost smiles | — |
| 33.20 | — | End | — |

## 5. Dialogue

| # | Character | Line (as spoken) | Turkish equivalent | Start (s) | Length (s) | Voice file | Direction |
|---|---|---|---|---|---|---|---|
| 1 | Vehbi | "January 24th, 1980." | "24 Ocak 1980." | 5.10 | 2.67 | `project/voices/v1.wav` | Whispered while writing. |
| 2 | Vehbi | "Bankers' crisis, '81 to '82." | "Banker krizi, 81–82." | 13.00 | 2.26 | `project/voices/v2.wav` | Whispered, faster. |
| 3 | Vehbi | "Export tax refunds." | "İhracatta vergi iadesi." | 20.25 | 1.33 | `project/voices/v3.wav` | Faster. |
| 4 | Vehbi | "Decision thirty-two, 1989." | "32 Sayılı Karar, 1989." | 26.55 | 2.33 | `project/voices/v4.wav` | Fastest. Pen down. |

- **Voices:** Generated in Voicebox from the consenting cloned voices, 48 kHz mono. The files as received are in `project/voices/raw/`.
- **Trimming:** The whispered takes had long quiet stretches before the words (about 2 s in `v1`, 3.7 s in `v3`), so they were trimmed at −35 dB rather than the usual −45 dB.
- **The proctor's "Pens down."** It was optional and not recorded, so the proctor is silent.

## 6. Characters in this scene

| | Vehbi | The students | The proctor |
|---|---|---|---|
| Position | Seated at the middle desk, third row from the back | Twelve, seated at their desks | Standing at the front, by his table |
| Held | His pen (the book stays in his bag) | — | — |
| Faces used | rest, determined, almost_smile | rest, heads down | rest |
| Never (enforced) | He never says "I don't know" (that is Scene 24) | — | — |

- **Seating:** Each sitter's hips drop to the chair seat (`hipdrop`), and the feet go forward under the desk (`fa`, `fb`); the leg IK bends the knees (`acting.sit`).
- **The others:** The students and the proctor are the generic, silent queue people from Scene 10.

## 7. Location and set

- **The exam hall (new):** An original, generic hall (`project/make_tex_hall.py`, `project/setdef.py`, `project/room.py`).
  - **Room:** 9 × 10 m, with cream walls over a pale green dado and a honey-coloured wooden floor.
  - **Light:** Three tall windows of morning light on the left.
  - **Front wall:** A blackboard reading "SINAV · Süre: 60 dakika", and a round clock.
- **Desks and chairs:** Each wooden desk has a front panel towards the blackboard; a chair with legs and a back stands behind it. On each desk is an exam sheet.
- **The question insert:** Vehbi's exam sheet, full frame (`env.sheet`).
  - **Header:** TÜRKİYE EKONOMİSİ · SINAV; Ad Soyad: Vehbi.
  - **Questions:** The four questions, with the current one marked in yellow and a slow push in. Answers already given are written in blue pen.
- **The stamp flashes:** `env.flash` uses `stamp.py`'s tool, mark and clipping, with the clipping now taking its text as arguments. The stamp drops, then the clipping slams in and holds; it is a hard cut back.

## 8. Shot list

| Shot | Code | In (s) | Out (s) | Length (s) | Framing and move | Content | Purpose |
|---|---|---|---|---|---|---|---|
| 01 | A | 0.00 | 2.20 | 2.20 | High from the back corner | The hall | Where we are |
| 02 | B | 2.20 | 31.20 | 29.00 | Vehbi from the front left, a slow push in; the inserts and flashes cut in over it | Lines 1–4 | The answers |
| 03 | C | 31.20 | 33.17 | 1.97 | From the front, rising | Pen down | Done |

## 9. Timed events

| Event | Time (s) | Source |
|---|---|---|
| Question inserts | 2.20, 10.25, 17.65, 24.00 | `room.Q` |
| Answers | 5.10, 13.00, 20.25, 26.55 | `room.L` |
| Stamp flashes | 7.90, 15.35, 21.70, 28.95 (the stamp drops in 0.13 s, then the clipping holds) | `room.FLASH` |
| Pen down | 31.30 | `room.PEN_DOWN` |

## 10. Sound

| Layer | What | When |
|---|---|---|
| Room | A quiet hall tone; pens scratching all around | Whole scene |
| Clock | Ticking, the ticks coming closer together as the cuts speed up | 0.30–31.30 |
| Sheet | A page at each question | Each insert |
| Stamp | A rush and a THUNK at each flash | Each flash |
| His pen | Short strokes, quicker each round | During each answer |
| Pen down | A click, then quiet | 31.60 |
| Voices | Lines 1–4, whispered | See the dialogue table |

The effects are synthesized placeholders. There is no music.

## 11. Production status

| Stage | Status | Output |
|---|---|---|
| Story plan row | From the person's plan | Section 3 |
| Lines | From `DIALOGUE-DRAFT.md`, recorded by the person | Section 5 |
| Set | New: the exam hall | `project/setdef.py`, `project/make_tex_hall.py` |
| Montage | The inserts and the flashes | `project/env.py`, `project/stamp.py` |
| Direction | Done; the seating rebuilt after the person's note | `project/blocking.py`, `project/shots.py`, `project/acting.py` |
| Final render | Done, v02 (re-rendered) | `final/` |
| Review by the person | Waiting | — |

## 12. Known weak points and next steps

| # | Weak point | Next step |
|---|---|---|
| 1 | The exam questions are the show's own wording, written to match the stamps; they are not taken from a real exam. | The person checks them against the course. |
| 2 | The students and the proctor reuse six generic designs, so some faces repeat across the hall. | More variants if they are seen closer. |
| 3 | The seated pose comes from the standing rig (hips down, feet forward); from some angles the knees look stiff. | Fine at this distance. |
| 4 | Effects are synthesized. | The person checks the balance. |

## 13. Decisions log

| Date | Decision | By |
|---|---|---|
| 2026-11-09 | "Sorular damgaların hızlı tekrarıyla kesilir": each whispered answer cuts to the stamp that taught it, word for word as first shown, faster each round | Claude |
| 2026-11-09 | The proctor's optional line was not recorded; he is silent | Claude |
| 2026-11-09 | First seating (characters sunk into the floor behind a panel) looked like people inside the desks, with the desks turned the wrong way; rebuilt with real chairs, panels towards the blackboard, and a true seated pose | The person's note, Claude |
| 2026-11-09 | In the exam, Vehbi's book stays in his bag | Claude |
| 2026-11-09 | v02: the person asked for the decisions and the exam questions to be shown longer. The frame is held at each question insert +2.2 s (at 2.50, 6.70, 10.25, 12.75 s) and each stamp flash +1.6 s (at 6.30, 9.95, 12.50, 15.85 s); the sound under the hold is the second before it, looped. Made from v01 with `../00_Full/hold.py`, no re-render. The project files still describe v01's timing. | The person; Claude |
| 2026-11-10 | v02 re-rendered. The first v02 froze frames and looped the last second of sound 8 times, so word endings and the THUNK repeated (the person: "Sınav kısmı bozulmuş / Sahne tekrarları oluşuyor"). Now `room.py` holds each question 2.2 s and each clipping 1.6 s longer (v01: Q 2.20/6.45/10.05/12.60, L 2.90/7.00/10.45/12.95, FLASH 5.70/9.35/11.90/15.35, PEN_DOWN 16.10, END 18.00); the stamp's drop is a fixed 0.13 s; the students and the proctor get two more looks to fill the longer shot. | The person's note; Claude |
| 2026-11-10 | v03: the exam is Türkiye Ekonomisi, not İktisat Tarihi (the person's note). The sheet's header now reads "TÜRKİYE EKONOMİSİ · SINAV". No re-render: `project/patch_sheet.py` redrew only the 252 sheet frames (the inserts are full-frame, `env.post` returns the sheet alone) into v02 and kept the rest and the sound; checked first by redrawing the old header, which matched v02 to 1.8/255 on average. | The person; Claude |

## 14. Files

| Path | What |
|---|---|
| `S23_SCENE.md` | This document |
| `final/S23_v01.mp4`, `final/S23_v01_contact-sheet.jpg` | First render and its contact sheet |
| `final/S23_v02.mp4`, `final/S23_v02_contact-sheet.jpg` | v02: re-rendered with the longer timings (see the decisions log) |
| `final/S23_v03.mp4`, `final/S23_v03_contact-sheet.jpg` | v03: the header "TÜRKİYE EKONOMİSİ · SINAV" |
| `project/patch_sheet.py` | Redraws the sheet inserts into an existing render |
| `project/` | The renderable engine project |
| `project/make_tex_hall.py` | Paints the hall's walls, floor, front wall and windows into `tex/` |
| `project/voices/` | `v1`–`v4` (`.wav` and `.tsv`); `raw/` holds the files as received |

## 15. How to re-render

```
cd <path>/S23/project && python3 make_tex_hall.py
python3 engine/toon.py <path>/S23/project lint
python3 engine/toon.py <path>/S23/project final        # v02: about 55 min
```
