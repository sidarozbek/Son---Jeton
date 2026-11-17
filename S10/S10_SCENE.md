# Son Jeton · Scene 10 · Kuş Bankerlik

| Field | Value |
|---|---|
| Series | Son Jeton |
| Scene | 10 of 24 |
| Title | Kuş Bankerlik |
| Status | In review: first render delivered, awaiting the person's notes |
| Current version | v01 (`final/S10_v01.mp4`) |
| Runtime | 10.80 s (259 frames at 24 fps) |
| Format | 1280 × 720, 24 fps, H.264, AAC 48 kHz |
| Location | The office of the imaginary "Kuş Bankerlik", daytime (the set for Scenes 10–14) |
| Period | 1982 |
| Characters | Sidar, Vehbi, six people in the queue (new, generic, silent) |
| Spoken language | English; the sign and the board are in Turkish |
| Series canon | `../00_Series/BIBLE.md`; story plan in `../00_Series/SCENE-INDEX.md`; lines in `../00_Series/DIALOGUE-DRAFT.md` |
| Previous scene | `../S09/S09_SCENE.md` |
| Next scene | `../S11/S11_SCENE.md` |
| Last updated | 2026-11-08 |

---

## 1. Logline

At the imaginary banker's office "Kuş Bankerlik", the interest board climbs by itself and the queue keeps growing. Sidar is carried away. Vehbi says nobody can pay that, and Sidar walks past the whole queue to hand over his last two tokens.

## 2. Purpose

- **Topic:** It sets up the bankers' crisis (D4 in Scene 11, D5 in Scene 14). The interest rate climbs, newcomers keep arriving, and Vehbi sees that the numbers can't be paid.
- **The figures:** The rates on the board (30% to 90%) are fantasy, not data, and there is no stamp in this scene.
- **Comic engine:** The board flips on cue with Sidar's counting. Vehbi does the sum in one line, and Sidar jumps the queue anyway.

## 3. Synopsis

The office is warm and wood-panelled, with a red sign reading KUŞ BANKERLİK under a bird mark. There is a barred teller window, an interest board reading FAİZ %30, and three people queuing at the window. The board flips by itself: %35, %40, %45, %50. Sidar, looking up at it and counting along: "Forty percent! Fifty! Vehbi, look!" More people come in at the street door and join the queue. Vehbi, quietly: "Nobody can pay that." The board shows %60, then %75. Sidar walks straight past the whole queue to the window, slaps his last two tokens on the counter, and turns to the room: "Invest them." The queue turns to look at him. The board flips to %90.

### From the story plan (canon, verbatim)

| Field | Story plan |
|---|---|
| Plan timecode | 3:00 |
| Part | Banker |
| What happens | 1982, hayali “Kuş Bankerlik” gişesi. Faiz tabelası kendi kendine yükselir, kuyruk uzar. |
| Joke or surprise | Sidar faize kapılır ve jetonlarını yatırmak ister. |
| “Sınavda çıkar” stamp | — |

## 4. Beat sheet

| Time (s) | Beat |
|---|---|
| 0.00 | The office; three people in the queue; the board at %30. |
| 1.00, 1.90, 2.45, 2.85 | The board flips to %35, %40, %45, %50. Sidar jolts a little at each one. |
| 2.00 | Line 1, pointing up at the board; he turns to Vehbi on "Vehbi, look!". |
| 3.00, 4.30, 5.60 | Newcomers walk in at the street door and join the end of the queue. |
| 5.00 | The board shows %60 (seen in the insert). |
| 5.20 | Line 2. |
| 6.60 | The board shows %75. |
| 7.10–8.20 | Sidar walks past the queue to the window. |
| 8.35 | He slaps the tokens on the counter. |
| 8.50 | Line 3, turning to face the room. |
| 8.45 onwards | The queue turns to look at him, one after another. |
| 9.40 | The board shows %90. |
| 10.80 | End. |

## 5. Dialogue

| # | Character | Line (as spoken) | Turkish equivalent | Start (s) | Length (s) | Voice file | Direction |
|---|---|---|---|---|---|---|---|
| 1 | Sidar | "Forty percent! Fifty! Vehbi, look!" | "Yüzde kırk! Elli! Vehbi, bak!" | 2.00 | 2.70 | `project/voices/s1.wav` | Greedy delight, counting along with the board. |
| 2 | Vehbi | "Nobody can pay that." | "Bunu kimse ödeyemez." | 5.20 | 1.03 | `project/voices/v2.wav` | Quiet, certain. |
| 3 | Sidar | "Invest them." | "Yatırın." | 8.50 | 0.87 | `project/voices/s3.wav` | Slapping his last two tokens on the counter. |

- **Line 3:** The recorded take said "Three tokens. Invest them." Sidar has only two tokens left after Scene 09 (5 − 3), so I cut the take to "Invest them." and he puts down two tokens. `DIALOGUE-DRAFT.md` is corrected. A re-recorded "Two tokens. Invest them." can replace it later (this needs a new lip-sync and render).
- **Voices:** Generated in Voicebox from the consenting cloned voices. Trimmed, 48 kHz mono. The files as received are in `project/voices/raw/`.

## 6. Characters in this scene

| | Sidar | Vehbi | The queue (q0–q5) |
|---|---|---|---|
| Position | (4.70, 2.60), by the board, then at the window (3.50, 4.95) | (3.95, 2.35) | At the window and back towards the door; q3–q5 walk in |
| Held | His last two tokens | The book | — |
| Faces used | curious, smug, determined | unimpressed, correcting, one_brow | rest, doubt |

- **The queue people:**
  - **Design:** New, generic and silent. Each is the grocer's build with a different coat, hair, skin and height (1.58–1.70 m).
  - **Hair and faces:** Two are bald with a fringe, and none have facial hair. They have four fingers like everyone else.
  - **Code:** `project/cast.py` (`queue_person`, `QUEUE`).

## 7. Location and set

- **The office:** An original design (`project/make_tex_banker.py`, `project/setdef.py`), and the set for Scenes 10–14.
  - **Room:** x 0–6 m, y 0–5.5 m, 3.0 m high.
  - **Walls and floor:** Cream walls over dark wood panelling, and a beige terrazzo floor.
  - **Front:** A street door on the left wall with daylight beyond, and a big front window.
- **The back wall:**
  - **Partition:** Dark polished wood.
  - **Teller window:** A barred window at x 2.6–3.4, 1.0–1.75 m up, with a slot and a small counter shelf in front.
  - **Sign:** A red board reading KUŞ BANKERLİK under an original bird mark. The name comes from the story plan, and nothing copies a real banker's office.
  - **Interest board:** On the right. "FAİZ" over a black panel with flip-numeral cards from %30 to %90. Each card flips in over 0.12 s in Blender (`setdef.animate`). The rates are fantasy.
- **Furniture:** A brass queue rail, a bench, and a potted plant.
- **Light:** Even, warm office light, with a warmer pool at the teller window and cool daylight at the door.
- **Hiding behind the set:** Characters are cut where the set is nearer to the camera, so the rail and the counter hide them correctly.

## 8. Shot list

| Shot | Code | In (s) | Out (s) | Length (s) | Framing and move | Content | Purpose |
|---|---|---|---|---|---|---|---|
| 01 | A | 0.00 | 2.00 | 2.00 | Wide from the front | The office, the sign, the queue, %30 | Where we are |
| 02 | B | 2.00 | 4.65 | 2.65 | Sidar from beside the board, looking up | Line 1 | Carried away |
| 03 | C | 4.65 | 5.25 | 0.60 | Insert: the board | %50 → %60 | It climbs |
| 04 | D | 5.25 | 7.00 | 1.75 | Vehbi, the queue behind | Line 2 | The sum |
| 05 | E | 7.00 | 8.45 | 1.45 | Wide | Sidar walks past the queue | Queue-jumping |
| 06 | F | 8.45 | 10.80 | 2.35 | From the right: Sidar at the window, the queue | Line 3; heads turn; %90 | The punchline |

## 9. Timed events

| Event | Time (s) | Source |
|---|---|---|
| Board flips | 1.00, 1.90, 2.45, 2.85, 5.00, 6.60, 9.40 | `room.RATE_TIMES`, `room.RATES` |
| Newcomers arrive | 3.00, 4.30, 5.60 (2.2 s walk) | `room.ARRIVALS`, `room.WALK_IN` |
| Tokens on the counter | 8.35 | `room.TOKENS_DOWN` |

## 10. Sound

| Layer | What | When |
|---|---|---|
| Bed | Office hum, lowered under the lines | Whole scene |
| Board | A clatter of flaps at each flip | Each flip |
| Door and steps | Each newcomer coming in | 3.00, 4.30, 5.60 |
| Tokens | A slap and two clinks on the counter | 8.35 |
| Voices | Lines 1–3 | See the dialogue table |

The effects are synthesized placeholders. There is no music.

## 11. Production status

| Stage | Status | Output |
|---|---|---|
| Story plan row | From the person's plan | Section 3 |
| Lines | Recorded by the person; line 3 cut for continuity | Section 5 |
| Rig | Sidar and Vehbi reused; six queue people new | `project/cast.py` |
| Set | New: the banker's office | `project/setdef.py`, `project/room.py`, `project/make_tex_banker.py` |
| Direction | Done | `project/blocking.py`, `project/shots.py`, `project/acting.py` |
| Final render | Done, v01 | `final/` |
| Review by the person | Waiting | — |

## 12. Known weak points and next steps

| # | Weak point | Next step |
|---|---|---|
| 1 | Line 3 was cut to "Invest them."; the count of tokens isn't spoken. | The person can re-record "Two tokens. Invest them." |
| 2 | The queue people have simple faces, seen mostly from the side and back. | Fine for background; give them eyebrows and moustaches if they get closer. |
| 3 | The teller window is dark, and no teller is seen. | Scene 11 goes behind it, to the safe. |
| 4 | Sidar has his back to the camera on "Vehbi, look!" for a moment. | Acceptable; he turns to Vehbi. |
| 5 | Effects are synthesized. | The person checks the balance. |

## 13. Decisions log

| Date | Decision | By |
|---|---|---|
| 2026-11-08 | The banker's office is a new set, designed to serve Scenes 10–14 | Claude |
| 2026-11-08 | The queue: six generic, silent people built on the grocer's body | Claude |
| 2026-11-08 | Token count: Sidar has two left, so line 3 was cut to "Invest them." and the draft was corrected | Claude |
| 2026-11-08 | The rates on the board (30–90%) are fantasy; no "monthly" or other claim is written on the board | Claude |

## 14. Files

| Path | What |
|---|---|
| `S10_SCENE.md` | This document |
| `final/S10_v01.mp4`, `final/S10_v01_contact-sheet.jpg` | First render and its contact sheet |
| `project/` | The renderable engine project |
| `project/make_tex_banker.py` | Paints the office, the sign and the rate cards into `tex/` |
| `project/voices/` | `s1`, `v2`, `s3` (`.wav` and `.tsv`); `raw/` holds the files as received |

## 15. How to re-render

```
cd <path>/S10/project && python3 make_tex_banker.py
python3 engine/toon.py <path>/S10/project lint
python3 engine/toon.py <path>/S10/project final        # about 30 min on 2 cores
```
