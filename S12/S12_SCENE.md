# Son Jeton · Scene 12 · The Blackboard

| Field | Value |
|---|---|
| Series | Son Jeton |
| Scene | 12 of 24 |
| Title | The Blackboard |
| Status | In review: first render delivered, awaiting the person's notes |
| Current version | v01 (`final/S12_v01.mp4`) |
| Runtime | 15.00 s (360 frames at 24 fps) |
| Format | 1280 × 720, 24 fps, H.264, AAC 48 kHz |
| Location | The office of "Kuş Bankerlik" (Scene 10's set), with a chalkboard |
| Period | 1982 |
| Characters | Sidar, Vehbi, the six people in the queue (silent) |
| Spoken language | English; the chalkboard is in Turkish |
| Series canon | `../00_Series/BIBLE.md`; story plan in `../00_Series/SCENE-INDEX.md`; lines in `../00_Series/DIALOGUE-DRAFT.md` |
| Previous scene | `../S11/S11_SCENE.md` |
| Next scene | `../S13/S13_SCENE.md` |
| Last updated | 2026-11-08 |

---

## 1. Logline

Vehbi chalks up the banker's arithmetic: each month needs more newcomers than the last, until there is nobody left to recruit. Sidar boasts that he built the place, and then the two of them have to wrestle his tokens back out of the teller window.

## 2. Purpose

- **Topic:** Why the scheme has to fail, shown as arithmetic. The board needs no stamp, and its numbers are only an illustration.
- **What it does for the story:** Sidar gets his two tokens back, which he needs for Scenes 14 and 20.
- **Comic engine:**
  - Sidar's boast comes straight after the proof that the place can't last.
  - The tug-of-war undercuts both of them.

## 3. Synopsis

At Kuş Bankerlik, the queue has stepped back from the window to watch. There is a chalkboard on an easel. It shows bars of new customers needed, doubling every month, and a dashed line labelled "herkes". Where the bars cross the line is an X and "burada biter". Vehbi runs his finger up the bars: "Every month needs more new customers than the last." He taps the X: "Here, it runs out." Sidar turns to the room with his arms spread: "I built this place. With my own hands." Vehbi goes to the teller window, where two tokens are wedged in the slot, and starts tugging: "Then help me pull." Sidar grabs on behind him and they tug together. "Hmph." POP: the tokens fly out, both stagger back, and Sidar catches them, pleased with himself.

### From the story plan (canon, verbatim)

| Field | Story plan |
|---|---|
| Plan timecode | 3:40 |
| Part | Banker |
| What happens | Vehbi sistemin matematiğini tahtada gösterir. Sidar “Ben burayı kurdum” diye övünür. |
| Joke or surprise | Tek bir jeton vezne gözüne sıkışır, ikisi çekip çıkarır. |
| “Sınavda çıkar” stamp | — |

## 4. Beat sheet

| Time (s) | Beat |
|---|---|
| 0.00 | Vehbi at the chalkboard; Sidar beside him; the queue stepped back. |
| 0.80 | Line 1. His finger runs up the bars. |
| 5.00 | He taps the X ("Here"). |
| 6.70 | Line 2. Sidar turns to the room, arms spread, then shows his hands. |
| 9.00–10.30 | Vehbi walks to the teller window. |
| 10.35 | He grabs the tokens stuck in the slot. |
| 10.50 | Line 3, tugging. |
| 11.00–12.00 | Sidar walks over; from 12.00 he pulls on Vehbi, and they tug together. |
| 13.00 | Line 4 ("Hmph."). |
| 13.25 | POP: the tokens fly out, and both stagger back 0.35–0.4 m. |
| 13.75 | Sidar catches them and turns round with them, smug. |
| 15.00 | End. |

## 5. Dialogue

| # | Character | Line (as spoken) | Turkish equivalent | Start (s) | Length (s) | Voice file | Direction |
|---|---|---|---|---|---|---|---|
| 1 | Vehbi | "Every month needs more new customers than the last. Here, it runs out." | "Her ay bir öncekinden fazla yeni müşteri gerekir. Burada biter." | 0.80 | 5.47 | `project/voices/v1.wav` | Tapping the end of the curve. |
| 2 | Sidar | "I built this place. With my own hands." | "Burayı ben kurdum. Kendi ellerimle." | 6.70 | 2.95 | `project/voices/s2.wav` | Boasting. |
| 3 | Vehbi | "Then help me pull." | "O zaman çekmeme yardım et." | 10.50 | 1.09 | `project/voices/v3.wav` | Already tugging the stuck token. |
| 4 | Sidar | "Hmph." | "Hıh." | 13.00 | 0.53 | `project/voices/s4.wav` | Effort as the token pops out. |

- **Voices:** Generated in Voicebox from the consenting cloned voices. Silence trimmed from both ends, 48 kHz mono. The files as received are in `project/voices/raw/`.

## 6. Characters in this scene

| | Sidar | Vehbi | The queue |
|---|---|---|---|
| Path | (3.35, 2.75) → behind Vehbi at the window (2.95, 4.62) | At the board (3.85, 3.50) → the window (3.05, 4.98) | Stepped back to x 1.1–2.1, turned to watch |
| Held | His two tokens, caught at 13.75 | The book; then the stuck tokens | — |
| Faces used | smug, determined | correcting, unimpressed, determined, one_brow | rest |

## 7. Location and set

- **The office:** Scene 11's office. The board stays at %150, and the 34 birds still circle under the ceiling.
- **The chalkboard (new):** On a wooden easel at x 4.2–5.4, y 3.9, 0.8–1.7 m up, facing the front, with a chalk ledge and a stick of chalk. The chalk drawing shows:
  - axes, labelled "yeni müşteri" and "ay";
  - eight bars doubling from month 1 to month 8;
  - a dashed line labelled "herkes";
  - a red X where the bars cross it, with "burada biter" and an arrow.
  - The numbers are an illustration, not data. It is painted in `project/make_tex_banker.py`.
- **The stuck tokens:**
  - Two tokens are wedged in the teller window's slot, wobbling as they tug.
  - They fly out at the pop in an arc to Sidar's hand, and stay there.
  - They are drawn in `env.draw_stuck`.

## 8. Shot list

| Shot | Code | In (s) | Out (s) | Length (s) | Framing and move | Content | Purpose |
|---|---|---|---|---|---|---|---|
| 01 | A | 0.00 | 3.60 | 3.60 | Vehbi at the board, from the front | Line 1 begins | The lecture |
| 02 | B | 3.60 | 6.30 | 2.70 | Closer on the board: the X | "Here, it runs out." | The point |
| 03 | C | 6.30 | 9.70 | 3.40 | Sidar from the front, arms spread | Line 2 | The boast |
| 04 | D | 9.70 | 15.00 | 5.30 | Profile along the back wall, at the window | Lines 3–4; the tug; POP | The undercut |

## 9. Timed events

| Event | Time (s) | Source |
|---|---|---|
| Tap on the X | 5.00 | `room.TAP` |
| Vehbi grabs / Sidar grabs | 10.35 / 12.00 | `room.GRAB_V`, `room.GRAB_S` |
| Pop / catch | 13.25 / 13.75 | `room.POP`, `room.CATCH` |

## 10. Sound

| Layer | What | When |
|---|---|---|
| Bed | Office hum; the flock's wingbeats overhead | Whole scene |
| Chalk | A tap on the board | 5.00 |
| Steps | To the window | 9.00–12.00 |
| Slot | Metal scraping with each tug | 10.55–13.25 |
| Pop | A thud and a bright clink; the catch | 13.25, 13.75 |
| Voices | Lines 1–4 | See the dialogue table |

## 11. Production status

| Stage | Status | Output |
|---|---|---|
| Story plan row | From the person's plan | Section 3 |
| Lines | From `DIALOGUE-DRAFT.md`, recorded by the person | Section 5 |
| Set | Scene 11's office, plus the chalkboard | `project/setdef.py`, `project/make_tex_banker.py` |
| Direction | Done | `project/blocking.py`, `project/shots.py`, `project/acting.py` |
| Final render | Done, v01 | `final/` |
| Review by the person | Waiting | — |

## 12. Known weak points and next steps

| # | Weak point | Next step |
|---|---|---|
| 1 | The plan says one token is stuck; here it is his two tokens together, so Sidar has both back for Scenes 14 and 20. | The person decides; the count only matters for continuity. |
| 2 | At the window, Vehbi is seen in profile, and the counter hides his reaching hand, so the tug reads more from the bodies than the hands. | An insert of the slot and the hands. |
| 3 | Vehbi's finger doesn't quite reach the board in the wide shot; the tap reads from the head and arm movement. | A closer insert with the finger on the X. |
| 4 | Effects are synthesized. | The person checks the balance. |

## 13. Decisions log

| Date | Decision | By |
|---|---|---|
| 2026-11-08 | "Tahta" is a chalkboard on an easel in the banker's office, with a doubling bar chart and a "herkes" line | Claude |
| 2026-11-08 | Two tokens are stuck together in the slot (rather than one), so Sidar's count stays at two for the plan's 4th and 5th tokens | Claude |
| 2026-11-08 | The queue stepped back from the window to watch the lecture | Claude |

## 14. Files

| Path | What |
|---|---|
| `S12_SCENE.md` | This document |
| `final/S12_v01.mp4`, `final/S12_v01_contact-sheet.jpg` | First render and its contact sheet |
| `project/` | The renderable engine project |
| `project/voices/` | `v1`, `s2`, `v3`, `s4` (`.wav` and `.tsv`); `raw/` holds the files as received |

## 15. How to re-render

```
cd <path>/S12/project && python3 make_tex_banker.py
python3 engine/toon.py <path>/S12/project lint
python3 engine/toon.py <path>/S12/project final        # about 45 min on 2 cores
```
