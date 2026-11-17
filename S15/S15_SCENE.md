# Son Jeton · Scene 15 · Paper Goods

| Field | Value |
|---|---|
| Series | Son Jeton |
| Scene | 15 of 24 |
| Title | Paper Goods |
| Status | In review: first render delivered, awaiting the person's notes |
| Current version | v01 (`final/S15_v01.mp4`) |
| Runtime | 13.00 s (312 frames at 24 fps) |
| Format | 1280 × 720, 24 fps, H.264, AAC 48 kHz |
| Location | An imaginary harbour, a clear day (the set for Scenes 15–19) |
| Period | Mid-1980s |
| Characters | Sidar, Vehbi |
| Spoken language | English; the signs are in Turkish |
| Stamp | None |
| Series canon | `../00_Series/BIBLE.md`; story plan in `../00_Series/SCENE-INDEX.md`; lines in `../00_Series/DIALOGUE-DRAFT.md` |
| Previous scene | `../S14/S14_SCENE.md` |
| Next scene | `../S16/S16_SCENE.md` |
| Last updated | 2026-11-08 |

---

## 1. Logline

Pale, see-through cargo ships glide past the quay without a sound. Sidar presents them as "full of goods", Vehbi puts his hand straight through a hull, and Sidar insists they are full of paper goods.

## 2. Purpose

- **Topic:** It opens the "hayali ihracat" part. The ships exist on paper only; the facts come later, in D6 (Scene 17) and D7 (Scene 19).
- **The picture:** Fantasy, in Sidar's world. There are no numbers, names or claims on screen.
- **Comic engine:**
  - Sidar's grand claim meets Vehbi's hand going through the hull.
  - "Paper goods" is both Sidar's defence and the truth.

## 3. Synopsis

A harbour on a clear day: a concrete quay with bollards, a warehouse marked ANTREPO, a small harbour office with a GÜMRÜK sign, a crane, and hills across the water. Three cargo ships drift by in silence. They are pale and see-through, ruled like forms, with a red margin line near the bow. Sidar turns to us with his arms wide: "Ships. Full of goods." Vehbi walks to the edge, stands side-on to the nearest ship and puts his hand out to touch the hull. It goes straight in; rings spread on the hull, and the hull keeps sliding past his fingers with a rustle of paper. Without taking his hand out, Vehbi turns to Sidar: "Full of what?" Sidar, defensive: "Goods! Paper goods." Vehbi takes his hand back and looks at it: there is nothing on it.

### From the story plan (canon, verbatim)

| Field | Story plan |
|---|---|
| Plan timecode | 4:40 |
| Part | Hayali ihracat |
| What happens | Liman. Yarı saydam gemiler sessizce dolaşır. |
| Joke or surprise | Vehbi bir gemiye dokunur, eli içinden geçer. |
| “Sınavda çıkar” stamp | — |

## 4. Beat sheet

| Time (s) | Beat |
|---|---|
| 0.00 | The harbour; three see-through ships drift by; they look out to sea. |
| 2.20 | Sidar turns to the camera. |
| 2.70 | Line 1, arms wide, then wider on "Full of goods". |
| 4.30–5.25 | Vehbi walks to the quay edge and stands side-on to ship A. |
| 5.55–6.15 | His right hand goes sideways into the hull; at 6.05 rings spread and the paper rustles. His eyes go wide. |
| 7.10 | Line 2, hand still inside, head turned to Sidar. |
| 8.60 | Line 3: both hands up on "Goods!", a finger at the ship on "Paper goods". |
| 10.40–10.85 | Vehbi takes his hand out and looks at his palm, then at Sidar. Sidar looks away at his ships. |
| 13.00 | End. |

## 5. Dialogue

| # | Character | Line (as spoken) | Turkish equivalent | Start (s) | Length (s) | Voice file | Direction |
|---|---|---|---|---|---|---|---|
| 1 | Sidar | "Ships. Full of goods." | "Gemiler. Mal dolu." | 2.70 | 1.40 | `project/voices/s1.wav` | Grand, arms wide. |
| 2 | Vehbi | "Full of what?" | "Ne dolu?" | 7.10 | 0.65 | `project/voices/v2.wav` | His hand inside the hull. |
| 3 | Sidar | "Goods! Paper goods." | "Mal! Kâğıt üstünde mal." | 8.60 | 1.53 | `project/voices/s3.wav` | Defensive. |

- **Voices:** Generated in Voicebox from the consenting cloned voices. Silence trimmed from both ends, 48 kHz mono. The files as received are in `project/voices/raw/`.

## 6. Characters in this scene

| | Sidar | Vehbi |
|---|---|---|
| Path | Stays at (−1.0, 2.7) | (0.35, 2.85) → the quay edge (0.62, 3.78), side-on |
| Held | — | The book (left hand) |
| Faces used | smug, determined, bluff | rest, curious, blank, one_brow, unimpressed |
| Never (enforced) | He never says "I was wrong" | He never says "I don't know" |

- **The hand:** Vehbi's right hand is pinned to a point in the world inside the hull, (0.62, 4.50, 1.02). The ship moves and the hand doesn't, so the hull slides through it.

## 7. Location and set

- **The harbour:** An original, generic harbour (`project/make_tex_harbour.py`, `project/setdef.py`, `project/room.py`), the set for Scenes 15–19.
  - **Quay:** Concrete slabs along x, with the edge at y 4.0. The sea is 1 m below, out to a far shore of hazy hills with small houses.
  - **On the quay:** Four bollards, crates, a lamp post, and an orange crane frame with its jib over the water.
  - **Behind:** A long warehouse marked ANTREPO with numbered doors, and the side wall of a harbour office with a GÜMRÜK sign. The signs are plain Turkish words, not real places, and they set up the customs officer in Scene 16.
- **The ships:** An original, plain little cargo ship: a hull with a raked bow, a deckhouse aft with a funnel, and a row of empty containers. They are not in the Blender set; they are drawn in `project/env.py`.
  - **Look:** Every face is paper-pale and see-through, with faint blue ruled lines on the hull and a red margin rule near the bow, like a form.
  - **Hiding:** The set hides them where it is nearer, using a depth map of their faces.
  - **Motion:** Ship A (14 m) glides along the quay at 0.9 m/s, past Vehbi. Ships B (22 m) and C (26 m) drift further out in opposite directions, bobbing slightly.
- **The water:** Bright dashes drift on the sea.

## 8. Shot list

| Shot | Code | In (s) | Out (s) | Length (s) | Framing and move | Content | Purpose |
|---|---|---|---|---|---|---|---|
| 01 | A | 0.00 | 2.60 | 2.60 | High wide from the land | The harbour, the ships | Where we are |
| 02 | B | 2.60 | 4.30 | 1.70 | Sidar from the front, the ships behind him | Line 1 | The claim |
| 03 | C | 4.30 | 8.45 | 4.15 | Vehbi at the edge, pushing in on the hand | The touch; line 2 | The gag |
| 04 | D | 8.45 | 10.35 | 1.90 | Over Vehbi's shoulder to Sidar | Line 3 | The defence |
| 05 | E | 10.35 | 13.00 | 2.65 | Vehbi with the hull behind | The empty hand | The button |

## 9. Timed events

| Event | Time (s) | Source |
|---|---|---|
| Vehbi's walk | 4.30–5.25 | `room.V_WALK` |
| Reach / touch | 5.55–6.15 / 6.05 | `room.REACH`, `room.TOUCH` |
| Hand out | 10.40–10.85 | `room.PULL` |
| Ships | Whole scene | `room.SHIPS`, `room.ship_pose` |

## 10. Sound

| Layer | What | When |
|---|---|---|
| Bed | Sea wind | Whole scene |
| Water | Soft slaps against the quay wall | Every 1.7 s |
| Gulls | Far off | 1.1, 1.6, 11.6 |
| Ships | Nothing at all: no engine, no wake | — |
| Steps | Vehbi to the edge | 4.40–5.25 |
| Paper | A rustle as the hand goes in; a quieter one as the hull slides; one as it comes out | 6.00, 7.45, 10.40 |
| Voices | Lines 1–3 | See the dialogue table |

The effects are synthesized placeholders. There is no music.

## 11. Production status

| Stage | Status | Output |
|---|---|---|
| Story plan row | From the person's plan | Section 3 |
| Lines | From `DIALOGUE-DRAFT.md`, recorded by the person | Section 5 |
| Set | New: the harbour | `project/setdef.py`, `project/room.py`, `project/make_tex_harbour.py` |
| Ships | New, drawn | `project/env.py` |
| Direction | Done | `project/blocking.py`, `project/shots.py`, `project/acting.py` |
| Final render | Done, v01 | `final/` |
| Review by the person | Waiting | — |

## 12. Known weak points and next steps

| # | Weak point | Next step |
|---|---|---|
| 1 | Close up, the ships read more as glass panels with lines than as ships; the ship shape shows best in the wide shot. | Give shot C a glimpse of the bow or the deck edge, or add a short wide insert. |
| 2 | Inside the hull the hand is only made paler and ruled; it does not really vanish. | A stronger fade, or a cut-off line at the hull. |
| 3 | Shot D, Sidar's defence, has no ship in view; his pointing finger goes off screen. | Turn the camera so a hull shows behind him. |
| 4 | In shot C, half of Sidar's face shows at the left edge for the first second. | Move the camera a little right. |
| 5 | Effects are synthesized. | The person checks the balance. |

## 13. Decisions log

| Date | Decision | By |
|---|---|---|
| 2026-11-08 | The ships are drawn, not built in Blender, so they can be truly see-through; they are ruled like forms to say "paper" without a word | Claude |
| 2026-11-08 | The hand is pinned to a point in the world, so the moving hull slides through it | Claude |
| 2026-11-08 | Signs read ANTREPO and GÜMRÜK, plain words; no real port | Claude |
| 2026-11-08 | No year on screen; "mid-1980s" in this document only, because the dates belong to D6 and D7 | Claude |

## 14. Files

| Path | What |
|---|---|
| `S15_SCENE.md` | This document |
| `final/S15_v01.mp4`, `final/S15_v01_contact-sheet.jpg` | First render and its contact sheet |
| `project/` | The renderable engine project |
| `project/make_tex_harbour.py` | Paints the quay, the sea, the far shore, the warehouse and the office into `tex/` |
| `project/voices/` | `s1`, `v2`, `s3` (`.wav` and `.tsv`); `raw/` holds the files as received |

## 15. How to re-render

```
cd <path>/S15/project && python3 make_tex_harbour.py
python3 engine/toon.py <path>/S15/project lint
python3 engine/toon.py <path>/S15/project final        # about 30 min on 2 cores
```
