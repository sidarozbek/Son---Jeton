# Son Jeton · Scene 06 · Midnight

| Field | Value |
|---|---|
| Series | Son Jeton |
| Scene | 06 of 24 |
| Title | Midnight |
| Status | In review: first render delivered, awaiting the person's notes |
| Current version | v01 (`final/S06_v01.mp4`) |
| Runtime | 10.80 s (259 frames at 24 fps) |
| Format | 1280 × 720, 24 fps, H.264, AAC 48 kHz |
| Location | Inside the corner grocer's (Scene 05's shop), midnight |
| Period | Midnight, 24–25 January 1980 |
| Characters | Sidar (landlord), Vehbi (tenant), the grocer (silent) |
| Spoken language | English |
| Series canon | `../00_Series/BIBLE.md`; story plan in `../00_Series/SCENE-INDEX.md`; lines in `../00_Series/DIALOGUE-DRAFT.md` |
| Previous scene | `../S05/S05_SCENE.md` |
| Next scene | `../S07/S07_SCENE.md` |
| Last updated | 2026-11-08 |

---

## 1. Logline

The clock strikes midnight. Every price card in the shop swells to more than twice its size, and the banknote in Vehbi's fingers shrinks to the size of a stamp. Sidar crows; Vehbi corrects him; Sidar doesn't care.

## 2. Purpose

- **Topic:** Devaluation as the audience will see it: the money buys less, and prices go up. The picture is pure fantasy (Sidar's world). No stamp, and no documented figure.
- **What this scene tests:**
  - A set that grows during the shot (the cards scale in Blender).
  - A prop that shrinks in a character's hand.
  - A clock insert.
- **Comic engine:** Sidar is triumphant about something he describes wrongly. Vehbi's correction is right, and it changes nothing: "Same thing!"

## 3. Synopsis

An insert: the shop's wall clock. The minute hand ticks onto twelve, and the clock strikes. In the shop, lit by one bulb, the price cards on the shelves (the doubled ones from Scene 05, and four more) begin to swell, slowly, past twice their size, crowding one another. The grocer backs away from his own shelves. Vehbi takes a banknote out of his pocket and watches it shrink in his fingers to the size of a stamp. Sidar throws both arms up: "See? SEE?!" Vehbi holds up the tiny note: "Money doesn't shrink. Prices rise." Sidar, at once: "Same thing!"

### From the story plan (canon, verbatim)

| Field | Story plan |
|---|---|
| Plan timecode | 1:40 |
| Part | 24 Ocak |
| What happens | Gece yarısı banknotlar ceplerde küçülür, fiyat etiketleri büyür. |
| Joke or surprise | Sidar zaferle bağırır: “Gördün mü?” |
| “Sınavda çıkar” stamp | — |

Source: the person's doc “Son Jeton: 8 Dakikalık Hikâye Planı”. Where it conflicts with a later decision in the decisions log, the later decision wins.

## 4. Beat sheet

| Time (s) | Beat |
|---|---|
| 0.00 | Insert: the wall clock at one minute to twelve. |
| 0.60 | The minute hand ticks onto twelve. The first strike at 0.70; heads turn to the clock. |
| 1.90 | Wide: the shop at midnight. |
| 2.30–5.80 | The price cards swell to 2.6 times their size, with a small overshoot at the end. The grocer backs away from the shelves. |
| 2.50 | Vehbi takes a banknote out of his pocket. |
| 3.10–5.30 | The note shrinks in his fingers to about a third of its size. |
| 4.60 | Line 1, with both arms up. |
| 6.20 | Line 2, the tiny note held up; a glance at the cards on "Prices rise". |
| 8.60 | Line 3, at once, with a pointing finger. |
| 10.80 | End. |

## 5. Dialogue

| # | Character | Line (as spoken) | Turkish equivalent | Start (s) | Length (s) | Voice file | Direction |
|---|---|---|---|---|---|---|---|
| 1 | Sidar | "See? SEE?!" | "Gördün mü? GÖRDÜN MÜ?!" | 4.60 | 0.93 | `project/voices/s1.wav` | A triumphant shout as the banknotes shrink. |
| 2 | Vehbi | "Money doesn't shrink. Prices rise." | "Para küçülmez. Fiyatlar artar." | 6.20 | 2.14 | `project/voices/v2.wav` | Holding a tiny banknote, dry. |
| 3 | Sidar | "Same thing!" | "Aynı şey!" | 8.60 | 0.77 | `project/voices/s3.wav` | Instantly. |

- **Voices:** Generated in Voicebox from the consenting cloned voices. Silence trimmed from both ends, 48 kHz mono; the files as received are in `project/voices/raw/`.

## 6. Characters in this scene

| | Sidar | Vehbi | The grocer |
|---|---|---|---|
| Position | (3.40, 2.35), right | (1.60, 2.30), left | (1.95, 4.40), behind the counter |
| Held | — | The book (left), the shrinking banknote (right) | — |
| Faces used | smug, determined | unimpressed, one_brow, correcting | rest, blank, curious |
| Never (enforced) | No embarrassed face | Doesn't say "I don't know" | Never speaks |

## 7. Location and set

- **The shop:** Scene 05's shop and textures, at midnight. The bulb over the counter is the only warm light, the ambient light is lower, and the front window shows the street dark blue.
- **The wall clock** (new): On the left wall at y 3.0, 2.2 m up. A plain white dial with black ticks and a red rim, no brand. The two hands are separate quads that turn about the wall's normal; the minute hand ticks onto twelve at 0.60.
- **The cards:**
  - The three doubled cards from Scene 05 (90, 240, 36), and four new ones (60, 150, 300, 75), all with invented prices.
  - From 2.30 to 5.80 every card grows to 2.6 times its size, hanging from the shelf edge, so it grows downwards and outwards.
  - The cards sit a few millimetres apart in depth, so overlapping cards don't flicker.
- **The banknote:** An invented note, plain green paper with "100" and a circle, no real design. It is drawn in `env.draw_note` in Vehbi's right fingers and shrinks from 15 × 7.5 cm to about a third of that.

## 8. Shot list

| Shot | Code | In (s) | Out (s) | Length (s) | Framing and move | Content | Purpose |
|---|---|---|---|---|---|---|---|
| 01 | A | 0.00 | 1.90 | 1.90 | Insert, the wall clock, slow push | Midnight | The hour |
| 02 | B | 1.90 | 4.50 | 2.60 | Wide from the front of the shop | The cards swell; the note comes out | The fantasy happens |
| 03 | C | 4.50 | 6.00 | 1.50 | Sidar, the swollen cards behind | Line 1 | Triumph |
| 04 | D | 6.00 | 8.50 | 2.50 | Vehbi, with the tiny note in frame | Line 2 | The correction |
| 05 | E | 8.50 | 10.80 | 2.30 | Sidar, wider, the grocer and the cards | Line 3 | Unbothered |

## 9. Timed events

| Event | Time (s) | Source |
|---|---|---|
| Minute hand onto twelve | 0.60 | `room.MIDNIGHT`, `room.minute_angle` |
| Clock strikes (heard) | 0.70, 1.45, 2.20, 2.95; then softly under the scene | `room.CHIMES` |
| Cards swell | 2.30–5.80 | `room.GROW`, `room.grow` |
| Banknote out / shrinks | 2.50 / 3.10–5.30 | `room.NOTE_OUT`, `room.SHRINK`, `room.note_scale` |

## 10. Sound

| Layer | What | When |
|---|---|---|
| Bed | The bulb's hum; lowered under line 2 | Whole scene |
| Clock | The last tick, then the strikes: four clear, the rest softer under the scene | 0.60 on |
| Cards | A long cardboard stretch, and a pop at the overshoot | 2.30–5.80 |
| Note | Paper crinkling as it shrinks | 3.10–5.30 |
| Voices | Lines 1–3 | See the dialogue table |

The effects are synthesized placeholders. The voices play at gain 1.0. There is no music.

## 11. Production status

| Stage | Status | Output |
|---|---|---|
| Story plan row | From the person's plan | Section 3 |
| Lines | From `DIALOGUE-DRAFT.md`, recorded by the person | Section 5 |
| Rig | Reused from Scene 05 | `project/cast.py` |
| Set | Scene 05's shop, with the clock and the growing cards added | `project/setdef.py`, `project/room.py`, `project/make_tex_shop.py` |
| Direction | Done | `project/blocking.py`, `project/shots.py`, `project/acting.py` |
| Voices | Done | `project/voices/` |
| Sound | Placeholder | `project/sound.py` |
| Final render | Done, v01 | `final/` |
| Review by the person | Waiting | — |

## 12. Known weak points and next steps

| # | Weak point | Next step |
|---|---|---|
| 1 | The banknote is small even before it shrinks, and in the wide shot it reads only as a green scrap. | A short insert on the note if the person wants the shrink seen up close. |
| 2 | The swollen cards overlap and cut off one another's numbers (the "90 24…" row). It reads as crowding, but the numbers don't all read. | Spread the cards further apart if the person wants every price legible. |
| 3 | Sidar's arms-up "See?" is framed above the elbows, so the gesture is half lost. | Widen shot C. |
| 4 | Only the cards' size changes; the goods on the shelves stay as they were. | Scene 08 takes it further, with labels spilling off the shelves. |
| 5 | Effects are synthesized; nobody here can hear the mix. | The person checks the balance. |

## 13. Decisions log

| Date | Decision | By |
|---|---|---|
| 2026-11-08 | Scene 06 stays in the grocer's (Scene 05's set), now at midnight, so Scene 08's giant labels can grow out of the same shelves | Claude |
| 2026-11-08 | "Banknotlar ceplerde küçülür" is shown with one note taken out of the pocket, shrinking in Vehbi's fingers | Claude |
| 2026-11-08 | A wall clock insert opens the scene at midnight | Claude |

## 14. Files

| Path | What |
|---|---|
| `S06_SCENE.md` | This document |
| `final/S06_v01.mp4` | First render, with voices |
| `final/S06_v01_contact-sheet.jpg` | Contact sheet of v01 |
| `project/` | The renderable engine project |
| `project/room.py` | The shop, the cards, the clock, and all of this scene's timing |
| `project/setdef.py` | The shop in Blender, the clock hands, the growing cards |
| `project/env.py` | Midnight light; the grocer cut behind the counter; the banknote |
| `project/make_tex_shop.py` | Paints the shop textures, the price cards and the clock face into `tex/` |
| `project/voices/` | `s1`, `v2` and `s3` (`.wav` and `.tsv`); `raw/` holds the files as received |

## 15. How to re-render

```
cd <path>/S06/project && python3 make_tex_shop.py
python3 engine/toon.py <path>/S06/project lint
python3 engine/toon.py <path>/S06/project final        # about 25 min on 2 cores
```
