# Son Jeton · Scene 24 · I Don't Know

| Field | Value |
|---|---|
| Series | Son Jeton |
| Scene | 24 of 24 |
| Title | I Don't Know |
| Status | In review: first render delivered, awaiting the person's notes |
| Current version | v01 (`final/S24_v01.mp4`) |
| Runtime | 11.00 s (264 frames at 24 fps) |
| Format | 1280 × 720, 24 fps, H.264, AAC 48 kHz |
| Location | The corridor outside the exam hall, the present day |
| Period | The present day |
| Characters | Vehbi, his friend (new, one line), two students walking off (silent) |
| Spoken language | English |
| Stamp | None |
| Series canon | `../00_Series/BIBLE.md`; story plan in `../00_Series/SCENE-INDEX.md`; lines in `../00_Series/DIALOGUE-DRAFT.md` |
| Previous scene | `../S23/S23_SCENE.md` |
| Next scene | — (the end) |
| Last updated | 2026-11-09 |

---

## 1. Logline

After the exam a friend asks Vehbi where he was last night. For the first time in his life, he says "I don't know." Black.

## 2. Purpose

- **What it does for the story:** It pays off the series' rule: Vehbi never says "Bilmiyorum" until the finale. Here he does, and it is the true answer.
- **Tone:** Quiet and warm. There is no joke and no stamp; the line ends the film. Vehbi's last face is an almost-smile, not a worry.

## 3. Synopsis

The corridor outside the exam hall, late morning. Two students walk off towards the bright window at the end. Vehbi comes out of the hall door with his book back in his hand, light on his feet. His friend falls in beside him, then stops and turns back to him, easy: "Where were you last night?" Vehbi stops. He thinks, looking away at nothing; he blinks. Then, almost smiling: "…I don't know." Black.

### From the story plan (canon, verbatim)

| Field | Story plan |
|---|---|
| Plan timecode | 7:40 |
| Part | Final |
| What happens | Sınav çıkışı. Bir arkadaşı sorar: “Dün gece neredeydin?” Vehbi durur: “Bilmiyorum.” |
| Joke or surprise | Siyah ekran. |
| “Sınavda çıkar” stamp | — |

## 4. Beat sheet

| Time (s) | Beat |
|---|---|
| 0.00 | The corridor; two students walking off. |
| 0.45 | The door: Vehbi comes out (0.50–4.30), towards us. |
| 1.20–4.10 | The friend falls in beside him, then stops and turns back. |
| 3.00 | Line 1. |
| 4.30 | Vehbi stops. He looks away; a blink (5.40). |
| 5.90 | Line 2. Then the almost-smile. |
| 8.40 | Black. |
| 11.00 | End. |

## 5. Dialogue

| # | Character | Line (as spoken) | Turkish equivalent | Start (s) | Length (s) | Voice file | Direction |
|---|---|---|---|---|---|---|---|
| 1 | The friend | "Where were you last night?" | "Dün gece neredeydin?" | 3.00 | 1.18 | `project/voices/f1.wav` | Easy, friendly. |
| 2 | Vehbi | "…I don't know." | "…Bilmiyorum." | 5.90 | 0.58 | `project/voices/v2.wav` | After a beat. The first time. |

- **Voices:** Recorded by the person. Silence trimmed from both ends, 48 kHz mono. The files as received are in `project/voices/raw/`.
- **The friend's voice:** It is different from Sidar's and Vehbi's, as the series' voice rule asks.
- **The pause before "I don't know":** It is played as staging (4.30–5.90), not baked into the recording.

## 6. Characters in this scene

| | Vehbi | The friend | Two students |
|---|---|---|---|
| Path | Out of the hall door (0.35, 9.2) → (1.1, 5.4) | (2.4, 8.2) → beside him → (1.95, 5.6), turning back to him | Walking off towards the window |
| Held | The book (back in his hand) | — | — |
| Faces used | almost_smile, rest | rest, curious, one_brow | rest |
| Never (enforced) | Says "I don't know" for the first time, as the canon allows here | — | — |

- **The friend (new):** Original, generic: a red jumper, brown hair, 1.60 m, four fingers. Built on the same base as the queue people (`project/cast.py`, `FRIEND`).

## 7. Location and set

- **The corridor (new):** An original corridor outside the exam hall (`project/setdef.py`, `project/make_tex_corridor.py`, `project/room.py`).
  - **Walls and floor:** Scene 23's cream walls over a green dado, and a pale grey terrazzo floor.
  - **The hall door:** It stands open on the left, with the dim hall beyond.
  - **Fittings:** A tall bright window at the far end, a bench, and ceiling lights.
- **The end:** From 8.40 the picture is black (`env.post`).

## 8. Shot list

| Shot | Code | In (s) | Out (s) | Length (s) | Framing and move | Content | Purpose |
|---|---|---|---|---|---|---|---|
| 01 | A | 0.00 | 2.90 | 2.90 | Down the corridor, a slow push | The door; Vehbi comes out; the friend joins | After the exam |
| 02 | B | 2.90 | 4.40 | 1.50 | The two of them, walking up to us | Line 1 | The question |
| 03 | C | 4.40 | 11.00 | 6.60 | Vehbi close, a slow push; black at 8.40 | The beat; line 2; black | The answer |

## 9. Timed events

| Event | Time (s) | Source |
|---|---|---|
| Vehbi's walk / stop | 0.50–4.30 | `blocking.V_WALK`, `room.STOP` |
| Black | 8.40 | `room.BLACK` |

## 10. Sound

| Layer | What | When |
|---|---|---|
| Corridor | A hum of lights, distant murmur of students | To 8.40 |
| Door / steps | The hall door; Vehbi's, the friend's and the others' steps | 0.45–5.50 |
| Voices | Lines 1–2 | See the dialogue table |
| Black | Silence | 8.40–11.00 |

There is no music. The effects are synthesized placeholders.

## 11. Production status

| Stage | Status | Output |
|---|---|---|
| Story plan row | From the person's plan | Section 3 |
| Lines | From `DIALOGUE-DRAFT.md`, recorded by the person | Section 5 |
| Rig | The friend, new | `project/cast.py` |
| Set | New: the corridor | `project/setdef.py`, `project/make_tex_corridor.py` |
| Direction | Done | `project/blocking.py`, `project/shots.py`, `project/acting.py` |
| Final render | Done, v01 | `final/` |
| Review by the person | Waiting | — |

## 12. Known weak points and next steps

| # | Weak point | Next step |
|---|---|---|
| 1 | The friend is built on the generic queue-person base, so he looks related to the background crowds of Scenes 10–14 and 23. | A face of his own (glasses, freckles, a different nose) if he matters more. |
| 2 | Vehbi's "thinking" beat is a look away and a blink; the turn of the head is small. | A slower, bigger look away. |
| 3 | The cut to black is hard, with no fade, as the plan says "Siyah ekran". | A short fade if wanted. |
| 4 | Effects are synthesized. | The person checks the balance. |

## 13. Decisions log

| Date | Decision | By |
|---|---|---|
| 2026-11-09 | "Sınav çıkışı" is the corridor outside the hall, the door still open | Claude |
| 2026-11-09 | Vehbi says it almost smiling: not knowing, for once, is all right | Claude |
| 2026-11-09 | Black for 2.6 s, in silence, then the end | Claude |

## 14. Files

| Path | What |
|---|---|
| `S24_SCENE.md` | This document |
| `final/S24_v01.mp4`, `final/S24_v01_contact-sheet.jpg` | First render and its contact sheet |
| `project/` | The renderable engine project |
| `project/voices/` | `f1`, `v2` (`.wav` and `.tsv`); `raw/` holds the files as received |

## 15. How to re-render

```
cd <path>/S24/project && python3 make_tex_corridor.py
python3 engine/toon.py <path>/S24/project lint
python3 engine/toon.py <path>/S24/project final        # about 20 min on 2 cores
```
