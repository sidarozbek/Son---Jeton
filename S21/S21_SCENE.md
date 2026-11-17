# Son Jeton · Scene 21 · Here Either

| Field | Value |
|---|---|
| Series | Son Jeton |
| Scene | 21 of 24 |
| Title | Here Either |
| Status | In review: first render delivered, awaiting the person's notes |
| Current version | v01 (`final/S21_v01.mp4`) |
| Runtime | 15.00 s (360 frames at 24 fps) |
| Format | 1280 × 720, 24 fps, H.264, AAC 48 kHz |
| Location | The street of Scenes 04 and 09, a summer evening; the grocer's is an exchange office now |
| Period | August 1989 |
| Characters | Sidar, Vehbi |
| Spoken language | English; the signs and the calendar are in Turkish |
| Stamp | None |
| Series canon | `../00_Series/BIBLE.md`; story plan in `../00_Series/SCENE-INDEX.md`; lines in `../00_Series/DIALOGUE-DRAFT.md` |
| Previous scene | `../S20/S20_SCENE.md` |
| Next scene | `../S22/S22_SCENE.md` |
| Last updated | 2026-11-09 |

---

## 1. Logline

The paper unfolds into August 1989. A river of money flows down the street they first stood in, and they have no tokens left. For the first time, Sidar's anger goes out.

## 2. Purpose

- **What it does for the story:** It opens the 1989 part. It is the low point: no tokens, the exam ten hours away.
- **Tone:** The plan asks for a short, quiet moment of loneliness, without breaking the magic. So there is no joke and no music. The river of money keeps flowing through the whole scene; the fantasy stays.
- **Setting up D8 (Scene 22):** In "Paranın aktığı yerde jeton da akar", the money that flows here is the money that flows across the border in Scene 22.

## 3. Synopsis

Scene 20's folded sheet opens out, and it is the same street as in Scenes 04 and 09, on a summer evening in August 1989. The grocer's shop is now an exchange office: a red DÖVİZ sign, a rate board, a calendar reading AĞUSTOS 1989. Where the cobbled road was, a river of banknotes flows past: hundreds of plain coloured notes drifting along like water. The two of them stand at its edge. Sidar opens his hands; they are empty. Vehbi, not as a reproach, just a fact: "No tokens. The exam's in ten hours." Sidar looks at the river, and the anger goes out of him. Quietly: "They won't believe me here either." Nobody says anything. The camera rises, leaving two small figures at the edge of a river of money that keeps flowing.

### From the story plan (canon, verbatim)

| Field | Story plan |
|---|---|
| Plan timecode | 6:40 |
| Part | 1989 |
| What happens | Ağustos 1989. Sokakta döviz ırmağı akar. Jeton yok, sınav yaklaşıyor. Sidar'ın öfkesi ilk kez söner: “Burada da inanmazlar.” |
| Joke or surprise | Yalnızlığın kısa ve sessiz anı, sihir bozulmaz. |
| “Sınavda çıkar” stamp | — |

## 4. Beat sheet

| Time (s) | Beat |
|---|---|
| 0.00–2.40 | The unfold: Scene 20's fold, backwards. |
| 2.40–4.90 | The river; both looking down at it. Sidar's hands open: empty. |
| 5.00 | Line 1. |
| 8.30 | Sidar looks at the river; his brows lift, his shoulders drop. |
| 9.60 | Line 2. |
| 11.50–15.00 | Silence; the crane up. |
| 15.00 | End. |

## 5. Dialogue

| # | Character | Line (as spoken) | Turkish equivalent | Start (s) | Length (s) | Voice file | Direction |
|---|---|---|---|---|---|---|---|
| 1 | Vehbi | "No tokens. The exam's in ten hours." | "Jeton yok. Sınava on saat var." | 5.00 | 3.13 | `project/voices/v1.wav` | A fact, not a reproach. |
| 2 | Sidar | "They won't believe me here either." | "Burada da inanmazlar." | 9.60 | 1.84 | `project/voices/s2.wav` | Quiet; the anger gone. |

- **Voices:** Generated in Voicebox from the consenting cloned voices. Silence trimmed from both ends, 48 kHz mono. The files as received are in `project/voices/raw/`.

## 6. Characters in this scene

| | Sidar | Vehbi |
|---|---|---|
| Position | (6.1, 4.7), on the sidewalk at the river's edge | (5.0, 4.85) |
| Held | Nothing | The book |
| Faces used | blank, rest with the brows lifted (sad, not angry) | blank, curious, rest |
| Never (enforced) | He never says "I was wrong" | He never says "I don't know" |

## 7. Location and set

- **The street:** Scenes 04 and 09's street (`project/setdef.py`), now in August 1989.
  - **Surfaces:** No snow; dry cobbles and pavement (`project/make_tex_1989.py`).
  - **Light:** The street lamps are lit, the sun is low and warm, the sky is peach.
  - **Cleared:** The parked van and the tree are gone, so the river can run there.
- **The exchange office (new):** It replaces the grocer's front (`tex/doviz.jpg`). It has a deep red sign reading DÖVİZ (the plain word, no brand), a rate board reading ALIŞ / SATIŞ with blank rows, a glass door, and a wall calendar reading AĞUSTOS 1989. There is no day on the calendar; the date belongs to D8.
- **The payphone:** Still on the wall. They have no token.
- **The river of money:**
  - **Notes:** 1500 original, generic notes in six colours, each with a border, an oval and three lines. They show no real currency, no portrait and no emblem.
  - **Motion:** They drift down the street over the road, faster in mid-stream, turning and riding the ripples, over a faint green sheen (`room.note`, `env.behind`).
  - **Hiding:** The kerb and the lamp post hide them where nearer.

## 8. Shot list

| Shot | Code | In (s) | Out (s) | Length (s) | Framing and move | Content | Purpose |
|---|---|---|---|---|---|---|---|
| 01 | A | 0.00 | 4.90 | 4.90 | High, down the street: the river comes towards us; the unfold over it | The unfold; the river | 1989 |
| 02 | B | 4.90 | 8.30 | 3.40 | Vehbi, from over the river | Line 1 | The fact |
| 03 | C | 8.30 | 11.90 | 3.60 | Sidar, a slow push in | Line 2 | The anger goes out |
| 04 | D | 11.90 | 15.00 | 3.10 | Crane up and back over the river | Silence | Alone, the magic intact |

## 9. Timed events

| Event | Time (s) | Source |
|---|---|---|
| Unfold | 0.00–2.40 | `room.UNFOLD`, `room.unfold` |
| The river | Whole scene | `room.NOTES`, `room.note` |

## 10. Sound

| Layer | What | When |
|---|---|---|
| Unfold | The fold's three whooshes, backwards | 0.10–2.30 |
| River | Running water with a paper crackle in it, steady | 1.60 on |
| Bed | Evening air, a low far-off hum | Whole scene |
| Voices | Lines 1–2 | See the dialogue table |

There is no music. The effects are synthesized placeholders.

## 11. Production status

| Stage | Status | Output |
|---|---|---|
| Story plan row | From the person's plan | Section 3 |
| Lines | From `DIALOGUE-DRAFT.md`, recorded by the person | Section 5 |
| Set | The street, re-dressed for 1989 | `project/setdef.py`, `project/make_tex_1989.py` |
| River | New | `project/env.py`, `project/room.py` |
| Direction | Done | `project/blocking.py`, `project/shots.py`, `project/acting.py` |
| Final render | Done, v01 | `final/` |
| Review by the person | Waiting | — |

## 12. Known weak points and next steps

| # | Weak point | Next step |
|---|---|---|
| 1 | The river reads as notes scattered thickly over the cobbles more than as flowing water; the flow shows in motion, not in stills. | Denser notes in mid-stream, a stronger water sheen, or ripple lines. |
| 2 | In the two close-ups the river is out of frame, so the dialogue plays against the shop front. | Tilt down to keep the notes in the bottom of the frame. |
| 3 | Sidar's sad face is the "rest" face with the brows lifted; it's subtle at this size. | Fine for a quiet beat; a closer shot if wanted. |
| 4 | Effects are synthesized. | The person checks the balance. |

## 13. Decisions log

| Date | Decision | By |
|---|---|---|
| 2026-11-09 | 1989 is the street of Scenes 04 and 09, the grocer's now an exchange office: the same place, nine years on | Claude |
| 2026-11-09 | "Döviz ırmağı" is a river of original, generic notes over the road; no real currency is drawn | Claude |
| 2026-11-09 | The scene opens by running Scene 20's paper fold backwards | Claude |
| 2026-11-09 | No music; the river's sound carries the silence | Claude |

## 14. Files

| Path | What |
|---|---|
| `S21_SCENE.md` | This document |
| `final/S21_v01.mp4`, `final/S21_v01_contact-sheet.jpg` | First render and its contact sheet |
| `project/` | The renderable engine project |
| `project/make_tex_1989.py` | Paints the exchange office, the dry cobbles and pavement into `tex/` |
| `project/fold.py` | The paper fold (here run backwards) |
| `project/voices/` | `v1`, `s2` (`.wav` and `.tsv`); `raw/` holds the files as received |

## 15. How to re-render

```
cd <path>/S21/project && python3 make_tex_1989.py
python3 engine/toon.py <path>/S21/project lint
python3 engine/toon.py <path>/S21/project final        # about 35 min on 2 cores
```
