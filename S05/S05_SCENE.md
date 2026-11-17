# Son Jeton · Scene 05 · The Same Book

| Field | Value |
|---|---|
| Series | Son Jeton |
| Scene | 05 of 24 |
| Title | The Same Book |
| Status | In review: first render delivered, awaiting the person's notes |
| Current version | v01 (`final/S05_v01.mp4`) |
| Runtime | 13.80 s (331 frames at 24 fps) |
| Format | 1280 × 720, 24 fps, H.264, AAC 48 kHz |
| Location | Inside the corner grocer's, evening |
| Period | 24 January 1980, evening |
| Characters | Sidar (landlord), Vehbi (tenant), the grocer (new; never speaks) |
| Spoken language | English |
| Series canon | `../00_Series/BIBLE.md`; story plan in `../00_Series/SCENE-INDEX.md`; lines in `../00_Series/DIALOGUE-DRAFT.md` |
| Previous scene | `../S04/S04_SCENE.md` |
| Next scene | `../S06/S06_SCENE.md` |
| Last updated | 2026-11-08 |

---

## 1. Logline

Sidar warns that Vehbi's money will shrink tonight. Vehbi recites the textbook definition of devaluation with his eyes shut, and behind his back the grocer quietly doubles every price card on the shelf.

## 2. Purpose

- **Topic:** Devaluation, in Vehbi's own textbook words; the picture shows what the words mean before the night is over. This is not a stamp: no documented figure is given.
- **What this scene tests:**
  - A third character.
  - A set that changes during the shot (the cards flip in Blender, frame by frame).
  - A character standing behind a counter.
- **Comic engine:** Vehbi is right and can't see; Sidar can see and only smirks. The grocer acts out the definition while it is being said.

## 3. Synopsis

Inside the grocer's, the door bell is still ringing. The grocer looks up from behind his counter. Sidar leans in to Vehbi: "Tonight, your money shrinks." Vehbi pushes up his glasses, shuts his eyes and recites, word-perfect: "Devaluation. The lira loses value against foreign currency, so imports cost more." Behind him, the grocer turns his back and flips three price cards on the shelf, one by one: 45 to 90, 120 to 240, 18 to 36. Sidar watches every card and nods slowly. The grocer turns round again, all innocence. Sidar nods at him: "He's read the same book." Vehbi opens his eyes and looks round; the grocer gives him a small, forced smile.

### From the story plan (canon, verbatim)

| Field | Story plan |
|---|---|
| Plan timecode | 1:20 |
| Part | 24 Ocak |
| What happens | Bakkal. Sidar “Bu gece paran küçülecek” der. Vehbi devalüasyonun kurla ilgili olduğunu anlatır. |
| Joke or surprise | Vehbi tanımı kusursuz okurken bakkal ona arkasını dönüp etiket değiştirir. |
| “Sınavda çıkar” stamp | — |

Source: the person's doc “Son Jeton: 8 Dakikalık Hikâye Planı”. Where it conflicts with a later decision in the decisions log, the later decision wins.

## 4. Beat sheet

| Time (s) | Beat |
|---|---|
| 0.00 | Inside the shop. The door bell dies away; the grocer looks up and gives them a nod of a smile. |
| 1.00 | Line 1. Sidar leans in and points at Vehbi's pocket on "your money". |
| 2.85 | Vehbi pushes up his glasses and shuts his eyes. |
| 3.30 | Line 2 (to 10.27). One raised finger on "against foreign currency". |
| 3.60–4.45 | The grocer glances at Vehbi and turns his back to them. |
| 5.10 / 6.60 / 8.10 | The three price cards flip to double: 45 → 90, 120 → 240, 18 → 36. |
| 6.85–7.85 | Cutaway: Sidar's eyes go past Vehbi to the shelf; slow nods as the cards flip. |
| 9.55 | The grocer turns round again, all innocence. |
| 10.70 | Line 3, with a nod at the grocer. |
| 12.20 | Vehbi opens his eyes and looks round at the grocer: one brow up. The grocer's forced smile. |
| 13.80 | End. |

## 5. Dialogue

| # | Character | Line (as spoken) | Turkish equivalent | Start (s) | Length (s) | Voice file | Direction |
|---|---|---|---|---|---|---|---|
| 1 | Sidar | "Tonight, your money shrinks." | "Bu gece paran küçülecek." | 1.00 | 1.57 | `project/voices/s1.wav` | Ominous, leaning in. |
| 2 | Vehbi | "Devaluation. The lira loses value against foreign currency, so imports cost more." | "Devalüasyon. Lira yabancı paralar karşısında değer kaybeder, ithalat pahalanır." | 3.30 | 6.97 | `project/voices/v2.wav` | Textbook-perfect, eyes closed. |
| 3 | Sidar | "He's read the same book." | "O da aynı kitabı okumuş." | 10.70 | 1.43 | `project/voices/s3.wav` | A nod at the grocer. |

- **Voices:** Generated in Voicebox from the consenting cloned voices. Silence trimmed from both ends, 48 kHz mono; the files as received are in `project/voices/raw/`.
- **The grocer:** He has no lines.

## 6. Characters in this scene

| | Sidar | Vehbi | The grocer |
|---|---|---|---|
| Role here | The warning, then the audience's eyes | Right, and blind to it | Acts out the definition |
| Position | (3.40, 2.35), right | (1.60, 2.30), left | (1.95, 4.40), behind the counter |
| Faces used | determined, smug | one_brow, correcting (eyes shut), unimpressed | rest, almost_smile, bluff, forced_smile |
| Never (enforced) | No embarrassed face | Doesn't say "I don't know"; never lets go of the book | Never speaks |

- **The grocer, new and original:**
  - Middle-aged, 1.68 m (taller than the two leads).
  - Bald on top, with a dark fringe around the sides and back, and a thick black moustache.
  - A beige shopkeeper's dust coat with three buttons and a breast pocket with a pencil.
  - Four fingers and no thumb, like everyone in the show.
  - Defined in `project/cast.py` (`GROCER`).

## 7. Location and set

- **The shop:** x 0–5, y 0–5.4, 2.8 m high.
  - Back wall: shelves packed with jars, tins, packets and bottles, painted as blocks of colour, with no brands and no readable labels.
  - Side walls: pale green oil paint over a darker dado. Floor: red and cream tiles.
  - Front wall (seen from inside): the window onto the blue street, and the door with its bell.
- **Counter:** Wooden, with a marble top, a scale and a jar of sweets. It runs across the shop at y 3.4–3.9, with sacks of rice and beans in front of it.
- **The price cards:** Three hand-lettered cardboard cards hang from the shelf edge at 1.35 m, at x 2.25, 2.60 and 2.95. Each is two cards on the same spot, old and new; the old one narrows to nothing and the new one widens out, over 0.3 s, at 5.10, 6.60 and 8.10. This is done in Blender (`setdef.animate`), so the cards sit at the right depth behind the grocer's arm. The prices are invented.
- **Behind the counter:** The engine places a character at one depth, so the counter would not hide the grocer's legs. `env._behind_counter` cuts him wherever the set is nearer to the camera than he is.
- **Light** (over the finished picture, in `env.py`):
  - One pendant bulb over the counter gives a warm pool.
  - The shop is dimmer towards the walls, and cold blue dusk comes from the front window.
- **Textures:** Painted with code in `project/make_tex_shop.py`.

## 8. Shot list

| Shot | Code | In (s) | Out (s) | Length (s) | Framing and move | Content | Purpose |
|---|---|---|---|---|---|---|---|
| 01 | A | 0.00 | 1.00 | 1.00 | Wide from the front of the shop | The bell, the grocer looks up | Where we are |
| 02 | B | 1.00 | 2.90 | 1.90 | Sidar, the grocer behind on the left | Line 1 | The warning |
| 03 | C | 2.90 | 6.85 | 3.95 | Vehbi, the grocer and the cards behind on the right | Line 2; the turn; the first card | The gag starts |
| 04 | D | 6.85 | 7.85 | 1.00 | Sidar, the shelf behind | His eyes on the cards | Someone sees it |
| 05 | E | 7.85 | 10.45 | 2.60 | Closer on Vehbi and the cards | The third card; the grocer turns back | The gag lands |
| 06 | F | 10.45 | 12.25 | 1.80 | Wide three-shot | Line 3 | The punchline |
| 07 | G | 12.25 | 13.80 | 1.55 | Vehbi and the grocer | Eyes open; the smile | Too late |

- **Line of action:** Vehbi on the left and Sidar on the right, as in Scene 04.

## 9. Timed events

| Event | Time (s) | Source |
|---|---|---|
| Door bell | 0.00–0.60 | `room.BELL` |
| The grocer turns his back | 3.90 | `room.TURN` |
| Card flips | 5.10, 6.60, 8.10 (0.3 s each) | `room.SWAPS`, `room.card_turn` |
| The grocer turns round | 9.55 | `room.TURN_BACK` |

## 10. Sound

| Layer | What | When |
|---|---|---|
| Bed | The bulb's hum, the street faint through the glass; lowered under the definition | Whole scene |
| Bell | The door bell dying away | 0.00–0.60 |
| Cloth | The grocer turning | 3.90, 9.55 |
| Cards | A cardboard flick for each flip | 5.10, 6.60, 8.10 |
| Voices | Lines 1–3 | See the dialogue table |

The effects are synthesized placeholders. The voices play at gain 1.0. There is no music.

## 11. Production status

| Stage | Status | Output |
|---|---|---|
| Story plan row | From the person's plan | Section 3 |
| Lines | From `DIALOGUE-DRAFT.md`, recorded by the person | Section 5 |
| Rig | Sidar and Vehbi reused; the grocer new | `project/cast.py` |
| Set | New: the shop | `project/setdef.py`, `project/room.py`, `project/make_tex_shop.py` |
| Direction | Done | `project/blocking.py`, `project/shots.py`, `project/acting.py` |
| Voices | Done | `project/voices/` |
| Sound | Placeholder | `project/sound.py` |
| Final render | Done, v01 | `final/` |
| Review by the person | Waiting | — |

## 12. Known weak points and next steps

| # | Weak point | Next step |
|---|---|---|
| 1 | The grocer's design hasn't been approved by the person. It is new and original, made to fill the plan's "bakkal". | The person approves it or asks for changes; it then goes into BIBLE.md. |
| 2 | From behind, the grocer's dark fringe reads a little like a band across the back of his head. | Soften it with a lighter colour or a more ragged edge. |
| 3 | The grocer's hand comes near the cards but doesn't hold them; the flip looks like the card turning on its own. | A grip pass, or a card drawn in his hand. |
| 4 | Vehbi recites with his eyes shut for 7 s; his face is in three-quarter profile in most of it. | Fine for the gag; a more frontal angle if the person wants his face. |
| 5 | Effects are synthesized; nobody here can hear the mix. | The person checks the balance. |

## 13. Decisions log

| Date | Decision | By |
|---|---|---|
| 2026-11-08 | The grocer: a new, original, silent character (bald on top, black moustache, beige dust coat) | Claude (proposal) |
| 2026-11-08 | "Etiket değiştirir" is shown as three hand-lettered price cards flipping to double, with invented prices | Claude |
| 2026-11-08 | Vehbi recites with his eyes shut, so he can't see what the audience sees | Claude |

## 14. Files

| Path | What |
|---|---|
| `S05_SCENE.md` | This document |
| `final/S05_v01.mp4` | First render, with voices |
| `final/S05_v01_contact-sheet.jpg` | Contact sheet of v01 |
| `project/` | The renderable engine project |
| `project/cast.py` | Sidar, Vehbi and the grocer |
| `project/room.py` | The shop's layout, the cards and all of this scene's timing |
| `project/setdef.py` | The shop in Blender, with the flipping cards |
| `project/env.py` | Light; the grocer cut behind the counter |
| `project/make_tex_shop.py` | Paints the shop textures and the price cards into `tex/` |
| `project/voices/` | `s1`, `v2` and `s3` (`.wav` and `.tsv`); `raw/` holds the files as received |

## 15. How to re-render

```
cd <path>/S05/project && python3 make_tex_shop.py
python3 engine/toon.py <path>/S05/project lint
python3 engine/toon.py <path>/S05/project final        # about 30 min on 2 cores
```
