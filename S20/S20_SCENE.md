# Son Jeton · Scene 20 · The Paper Token

| Field | Value |
|---|---|
| Series | Son Jeton |
| Scene | 20 of 24 |
| Title | The Paper Token |
| Status | In review: first render delivered, awaiting the person's notes |
| Current version | v01 (`final/S20_v01.mp4`) |
| Runtime | 13.00 s (312 frames at 24 fps) |
| Format | 1280 × 720, 24 fps, H.264, AAC 48 kHz |
| Location | The harbour, at a payphone on the harbour office's wall |
| Period | Mid-1980s |
| Characters | Sidar, Vehbi (the customs officer is off screen) |
| Spoken language | English |
| Stamp | None |
| Series canon | `../00_Series/BIBLE.md`; story plan in `../00_Series/SCENE-INDEX.md`; lines in `../00_Series/DIALOGUE-DRAFT.md` |
| Previous scene | `../S19/S19_SCENE.md` |
| Next scene | `../S21/S21_SCENE.md` |
| Last updated | 2026-11-09 |

---

## 1. Logline

Sidar holds up his last token, and it turns see-through in his fingers: it exists only on paper. He pushes it into the payphone anyway. The line crackles, and the harbour folds away like a sheet of paper, with no token left.

## 2. Purpose

- **What it does for the story:** The fifth token is lost (the plan's world rule: "Beşinci jeton kaybolur, altıncısı 1989'da bulunur"). The leap to 1989 happens without a token, which sets up Scenes 21–22.
- **Echo:** The see-through ships of Scenes 15–19 reach Sidar's own token. Paper-ruled lines and a red margin rule appear on it, as on the ships.
- **Transition:** The paper fold from Scene 03 returns, after a crackle on the line.

## 3. Synopsis

At a payphone on the harbour office's wall, Sidar holds up a token, solemnly: "Last one. Token five." As they look, it turns see-through in his fingers, faintly ruled like a form. Vehbi: "It's… see-through." Sidar, defensive: "It's a perfectly good tok—" He turns and pushes it into the slot anyway, and it is gone. The line crackles over the end of his word: the picture tears, splits and snows. Then the whole harbour folds up like a sheet of paper, with the two of them in it, and shrinks away.

### From the story plan (canon, verbatim)

| Field | Story plan |
|---|---|
| Plan timecode | 6:20 |
| Part | Hayali ihracat |
| What happens | Sidar beşinci jetonu atar. Jeton saydamlaşıp kaybolur: Yalnızca kâğıt üzerinde vardır. |
| Joke or surprise | Hat cızırdar ve onları jetonsuz hâlde savurur. |
| “Sınavda çıkar” stamp | — |

## 4. Beat sheet

| Time (s) | Beat |
|---|---|
| 0.55 | The token held up. |
| 0.80 | Line 1. |
| 2.90–4.00 | It turns see-through, ruled like a form. Both stare; Sidar goes blank. |
| 4.30 | Line 2. |
| 6.10 | Line 3, to Vehbi, then he turns to the phone. |
| 7.25 | Into the slot; gone. |
| 7.95 | The crackle over "tok—": both jolt; the picture tears and snows. |
| 8.90–12.40 | The paper fold. |
| 13.00 | End, on the small folded sheet. |

## 5. Dialogue

| # | Character | Line (as spoken) | Turkish equivalent | Start (s) | Length (s) | Voice file | Direction |
|---|---|---|---|---|---|---|---|
| 1 | Sidar | "Last one. Token five." | "Sonuncusu. Beşinci jeton." | 0.80 | 1.67 | `project/voices/s1.wav` | Solemn. |
| 2 | Vehbi | "It's… see-through." | "Bu… saydam." | 4.30 | 1.41 | `project/voices/v2.wav` | Staring at it. |
| 3 | Sidar | "It's a perfectly good tok—" | "Gayet sağlam bir jet—" | 6.10 | 1.93 | `project/voices/s3.wav` | Cut off by the crackle. |

- **Voices:** Generated in Voicebox from the consenting cloned voices. Silence trimmed from both ends, 48 kHz mono. The files as received are in `project/voices/raw/`.

## 6. Characters in this scene

| | Sidar | Vehbi |
|---|---|---|
| Position | At the phone, (−13.35, 0.2) | (−12.5, −0.7) |
| Held | Token five | The book |
| Faces used | rest, blank, bluff, panic | rest, curious, one_brow, panic |
| Never (enforced) | He never says "I was wrong" | He never says "I don't know" |

## 7. Location and set

- **The harbour:** As in Scenes 15–19. Ship A is moored and its containers are open; the invoices from Scene 19 lie on the quay and the deck.
- **The payphone (new here):** On the harbour office's side wall, at (−13.94, 0.2), 1.05 m up, facing the quay. It is Scene 03's original design.
- **Token five:** Drawn in `env.draw_token`. It fades from gold to see-through (`room.see`) and gains blue ruled lines and a red margin rule.
- **The crackle and the fold:** Whole-picture effects in `project/fold.py`. The fold is Scene 03's paper fold; the crackle is new (`fold.crackle`): slipping bands, split colour plates, snow.

## 8. Shot list

| Shot | Code | In (s) | Out (s) | Length (s) | Framing and move | Content | Purpose |
|---|---|---|---|---|---|---|---|
| 01 | A | 0.00 | 4.15 | 4.15 | Sidar at the phone, the token up | Line 1; the token goes see-through | The last one |
| 02 | B | 4.15 | 5.95 | 1.80 | Vehbi | Line 2 | Named |
| 03 | C | 5.95 | 8.20 | 2.25 | Over Vehbi to Sidar and the phone | Line 3; into the slot; the crackle begins | Denial |
| 04 | D | 8.20 | 13.00 | 4.80 | High wide | The crackle; the paper fold | Gone, without a token |

## 9. Timed events

| Event | Time (s) | Source |
|---|---|---|
| Token up | 0.55 | `room.TOKEN_UP` |
| See-through | 2.90–4.00 | `room.SEE`, `room.see` |
| Into the slot | 7.25 | `room.COIN_IN` |
| Crackle | 7.95 on | `room.CRACKLE`, `room.crackle` |
| Paper fold | 8.90–12.40 | `room.FOLD`, `room.fold` |

## 10. Sound

| Layer | What | When |
|---|---|---|
| Bed | Sea wind; water against the quay wall; pulled away in the fold | Whole scene |
| Token | A faint paper rustle as it turns; into the slot, a whisper of paper with no clink | 3.10; 7.45 |
| Line | Crackling hiss, building | 7.95 on |
| Fold | Three whooshes and a soft tap | 9.10–12.40 |
| Voices | Lines 1–3 | See the dialogue table |

The effects are synthesized placeholders. There is no music.

## 11. Production status

| Stage | Status | Output |
|---|---|---|
| Story plan row | From the person's plan | Section 3 |
| Lines | From `DIALOGUE-DRAFT.md`, recorded by the person | Section 5 |
| Set | The harbour, plus the payphone | `project/setdef.py`, `project/room.py` |
| Effects | The see-through token, the crackle, the fold | `project/env.py`, `project/fold.py` |
| Direction | Done | `project/blocking.py`, `project/shots.py`, `project/acting.py` |
| Final render | Done, v01 | `final/` |
| Review by the person | Waiting | — |

## 12. Known weak points and next steps

| # | Weak point | Next step |
|---|---|---|
| 1 | The token is held at chest height and is small; the change to see-through reads, but it's a small thing in the frame. | A close insert of the token in his fingers as it turns. |
| 2 | Sidar turns his back to the camera for the end of line 3 ("…tok—") as he goes to the slot. | Acceptable: the crackle takes over; or an insert of the slot. |
| 3 | The crackle is a digital-looking glitch (slipping bands, colour split). | A softer, analogue look if wanted. |
| 4 | Effects are synthesized. | The person checks the balance. |

## 13. Decisions log

| Date | Decision | By |
|---|---|---|
| 2026-11-09 | "Jeton saydamlaşır" uses the paper ships' look on the token: see-through, ruled, a red margin rule | Claude |
| 2026-11-09 | "Hat onları savurur" is the crackle, then Scene 03's paper fold; Scene 21 can open by unfolding into 1989 | Claude |
| 2026-11-09 | The payphone is on the harbour office's wall, so the scene stays in the harbour set | Claude |

## 14. Files

| Path | What |
|---|---|
| `S20_SCENE.md` | This document |
| `final/S20_v01.mp4`, `final/S20_v01_contact-sheet.jpg` | First render and its contact sheet |
| `project/` | The renderable engine project |
| `project/fold.py` | The paper fold (from Scene 03) and the line's crackle |
| `project/voices/` | `s1`, `v2`, `s3` (`.wav` and `.tsv`); `raw/` holds the files as received |

## 15. How to re-render

```
cd <path>/S20/project && python3 make_tex_harbour.py
python3 engine/toon.py <path>/S20/project lint
python3 engine/toon.py <path>/S20/project final        # about 30 min on 2 cores
```
