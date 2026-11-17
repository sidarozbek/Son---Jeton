# Son Jeton · Scene 18 · Destination: Germany

| Field | Value |
|---|---|
| Series | Son Jeton |
| Scene | 18 of 24 |
| Title | Destination: Germany |
| Status | In review: first render delivered, awaiting the person's notes |
| Current version | v01 (`final/S18_v01.mp4`) |
| Runtime | 19.79 s (475 frames at 24 fps) |
| Format | 1280 × 720, 24 fps, H.264, AAC 48 kHz |
| Location | The customs post on the quay, and the deck of a paper ship |
| Period | Mid-1980s |
| Characters | Sidar, Vehbi, the customs officer (silent) |
| Spoken language | English |
| Stamp | None (the officer's stamp is a sound effect) |
| Series canon | `../00_Series/BIBLE.md`; story plan in `../00_Series/SCENE-INDEX.md`; lines in `../00_Series/DIALOGUE-DRAFT.md` |
| Previous scene | `../S17/S17_SCENE.md` |
| Next scene | `../S19/S19_SCENE.md` |
| Last updated | 2026-11-08 |

---

## 1. Logline

Sidar walks up a gangway onto a see-through ship, and the officer writes him into the ledger as export goods bound for Germany. Sidar is delighted. Nothing moves. On paper, he has already arrived.

## 2. Purpose

- **Topic:** Export on paper. The goods are registered as shipped, and the paperwork is the journey. This sets up D7 (Scene 19).
- **The picture:** Fantasy, in Sidar's world. The ledger holds scribble and a red stamp; no real names and no figures are shown.
- **Comic engine:**
  - Sidar is flattered to be "appreciated" as goods.
  - The silent wait.
  - Vehbi's dry verdict.

## 3. Synopsis

At the customs post, a wooden gangway leads up from the quay to the paper ship from Scene 16. "All aboard!" Sidar strides up the plank onto the see-through deck and turns to face the quay, chin up. Behind the counter, the officer writes an entry in his ledger and stamps it. Vehbi comes round the counter and reads it out, upside down: "'One landlord. Export goods. Destination: Germany.'" Sidar, arms wide on the deck: "Germany! Finally, someone appreciates me." Nothing happens. He waits for the ship to leave, looks left, right, then down at the deck: "…Are we moving?" Vehbi, dry: "On paper, you've arrived."

### From the story plan (canon, verbatim)

| Field | Story plan |
|---|---|
| Plan timecode | 5:40 |
| Part | Hayali ihracat |
| What happens | Sidar saydam gemiye biner. Bir yetkili onu “ihraç malı” diye deftere yazar. |
| Joke or surprise | Sidar kâğıt üzerinde Almanya'ya gönderilir, ama hiç kımıldamaz. |
| “Sınavda çıkar” stamp | — |

## 4. Beat sheet

| Time (s) | Beat |
|---|---|
| 0.30–2.60 | Sidar to the gangway. Line 1 at 1.60. |
| 2.60–3.40 | Up the plank onto the deck; he turns to the quay, chin up. |
| 1.00–4.10 | The officer writes the entry. |
| 1.60–3.40 | Vehbi goes round the counter to the ledger. |
| 4.40 | The officer stamps the entry. |
| 4.80 | Line 2: Vehbi reads it out, his eyes running along the lines. |
| 11.40 | Line 3: arms wide, then hands to his chest. |
| 14.70–15.65 | The wait: arms down, a look left, a look right, then down at the deck. |
| 15.70 | Line 4. |
| 17.00 | Line 5. |
| 19.80 | End. |

## 5. Dialogue

| # | Character | Line (as spoken) | Turkish equivalent | Start (s) | Length (s) | Voice file | Direction |
|---|---|---|---|---|---|---|---|
| 1 | Sidar | "All aboard!" | "Herkes gemiye!" | 1.60 | 0.59 | `project/voices/s1.wav` | On his way up the gangway. |
| 2 | Vehbi | "'One landlord. Export goods. Destination: Germany.'" | "'Bir ev sahibi. İhraç malı. Varış: Almanya.'" | 4.80 | 6.33 | `project/voices/v2.wav` | Reading the officer's ledger aloud. |
| 3 | Sidar | "Germany! Finally, someone appreciates me." | "Almanya! Sonunda kıymetimi bilen biri." | 11.40 | 3.23 | `project/voices/s3.wav` | Delighted. |
| 4 | Sidar | "…Are we moving?" | "…Gidiyor muyuz?" | 15.70 | 0.80 | `project/voices/s4.wav` | After a beat; nothing moves. |
| 5 | Vehbi | "On paper, you've arrived." | "Kâğıt üstünde vardın bile." | 17.00 | 1.92 | `project/voices/v5.wav` | Dry. |

- **Voices:** Generated in Voicebox from the consenting cloned voices. Silence trimmed from both ends, 48 kHz mono. The files as received are in `project/voices/raw/`.

## 6. Characters in this scene

| | Sidar | Vehbi | The customs officer |
|---|---|---|---|
| Path | (−7.6, 1.5) → (−6.0, 3.1) → up the gangway → the deck (−6.0, 4.97), 1.0 m up | (−6.1, 0.7) → round the counter → (−8.95, 2.08) | Behind the counter |
| Held | — | The book | A pen, then his stamp |
| Faces used | determined, smug, curious, try_smile, doubt, bluff | unimpressed, correcting, slow_lid | rest, head down |
| Never (enforced) | He never says "I was wrong" | He never says "I don't know" | He never speaks, never looks up |

- **Sidar's ground:** Sidar has his own ground function (`room.deck_ground`): the quay, the slope of the plank, then the ship's deck.

## 7. Location and set

- **The customs post:** Scenes 16–17. The drawer is still open, with the tiny ship.
- **The gangway (new):** A wooden plank with cleats from the quay edge up to ship A's deck at x −6.0, plus two posts.
- **The ledger (new):** It replaces the form on the counter. It is an open book with a dark red cover and ruled pages. Three lines of scribble appear as the officer writes, then a red stamp mark appears; it is drawn in `env.draw_form`.
- **Ship A:** Still and moored; its bob is turned off so the deck holds still under Sidar.

## 8. Shot list

| Shot | Code | In (s) | Out (s) | Length (s) | Framing and move | Content | Purpose |
|---|---|---|---|---|---|---|---|
| 01 | A | 0.00 | 4.50 | 4.50 | Wide from along the quay: the gangway, the ship, the post | Line 1; the boarding; the writing | All aboard |
| 02 | B | 4.50 | 11.25 | 6.75 | Vehbi over the ledger, a slow push in | Line 2 | Registered |
| 03 | C | 11.25 | 16.85 | 5.60 | Sidar on the deck, the sea and hills behind | Lines 3–4; the wait | Going nowhere |
| 04 | D | 16.85 | 19.80 | 2.95 | Vehbi beside the officer | Line 5 | Arrived |

## 9. Timed events

| Event | Time (s) | Source |
|---|---|---|
| Sidar's walk / up the plank | 0.30–3.40 / 2.60–3.40 | `room.S_WALK`, `room.deck_ground` |
| Vehbi's walk | 1.60–3.40 | `room.V_WALK` |
| Writing / stamp | 1.00–4.10 / 4.40 | `room.WRITE`, `room.STAMP_L` |

## 10. Sound

| Layer | What | When |
|---|---|---|
| Bed | Sea wind; water against the quay wall | Whole scene |
| Steps | On the quay; hollow on the plank; Vehbi's | 0.40–3.40 |
| Pen / stamp | Scratching; a dry thump | 1.00–4.10 / 4.40 |
| Gulls | One during the reading; one in the wait, the only sound | 7.5, 15.0 |
| Voices | Lines 1–5 | See the dialogue table |

There is no engine and no horn: the ship never moves. The effects are synthesized placeholders. There is no music.

## 11. Production status

| Stage | Status | Output |
|---|---|---|
| Story plan row | From the person's plan | Section 3 |
| Lines | From `DIALOGUE-DRAFT.md`, recorded by the person | Section 5 |
| Set | Scene 16's customs post, plus the gangway and the ledger | `project/setdef.py`, `project/env.py`, `project/room.py` |
| Direction | Done | `project/blocking.py`, `project/shots.py`, `project/acting.py` |
| Final render | Done, v01 | `final/` |
| Review by the person | Waiting | — |

## 12. Known weak points and next steps

| # | Weak point | Next step |
|---|---|---|
| 1 | On "All aboard!" Sidar is mid-walk, so the walk cycle overrides his arms and the raised arm doesn't show. | Stop him at the foot of the gangway for the line. |
| 2 | On the deck he has no shadow and his feet sit on an invisible floor; it reads as standing on glass, which suits the gag but may look like floating. | A faint shadow on the deck, drawn in `env`. |
| 3 | Line 2 is long (6.3 s) over one slow push on Vehbi. | Cut once to Sidar on deck mid-line ("Export goods") for his reaction. |
| 4 | The officer's writing reads from the scribble and the pen; his hand barely moves. | Fine at this size. |
| 5 | Effects are synthesized. | The person checks the balance. |

## 13. Decisions log

| Date | Decision | By |
|---|---|---|
| 2026-11-08 | Boarding is by a gangway onto the paper ship from Scene 16; Sidar gets his own ground (quay, plank, deck) | Claude |
| 2026-11-08 | "Bir yetkili onu deftere yazar" is the same customs officer, with a ledger on his counter | Claude |
| 2026-11-08 | The wait is silent but for one gull; the ship makes no sound | Claude |

## 14. Files

| Path | What |
|---|---|
| `S18_SCENE.md` | This document |
| `final/S18_v01.mp4`, `final/S18_v01_contact-sheet.jpg` | First render and its contact sheet |
| `project/` | The renderable engine project |
| `project/voices/` | `s1`, `v2`, `s3`, `s4`, `v5` (`.wav` and `.tsv`); `raw/` holds the files as received |

## 15. How to re-render

```
cd <path>/S18/project && python3 make_tex_harbour.py
python3 engine/toon.py <path>/S18/project lint
python3 engine/toon.py <path>/S18/project final        # about 40 min on 2 cores
```
