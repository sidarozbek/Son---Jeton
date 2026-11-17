# Son Jeton · Scene 13 · The Sign

| Field | Value |
|---|---|
| Series | Son Jeton |
| Scene | 13 of 24 |
| Title | The Sign |
| Status | In review: first render delivered, awaiting the person's notes |
| Current version | v01 (`final/S13_v01.mp4`) |
| Runtime | 14.60 s (350 frames at 24 fps) |
| Format | 1280 × 720, 24 fps, H.264, AAC 48 kHz |
| Location | The office of "Kuş Bankerlik" (Scene 10's set) |
| Period | 1982 |
| Characters | Sidar, Vehbi, the six people in the queue |
| Spoken language | None: nobody speaks |
| Series canon | `../00_Series/BIBLE.md`; story plan in `../00_Series/SCENE-INDEX.md` |
| Previous scene | `../S12/S12_SCENE.md` |
| Next scene | `../S14/S14_SCENE.md` |
| Last updated | 2026-11-08 |

---

## 1. Logline

The flock lifts all at once and leaves through the street door. The teller window shuts, the board goes dark, and the queue just stands there. The only thing that falls is the sign.

## 2. Purpose

- **Tone:** The tone turns. The series rule is that people losing their savings is never a subject for jokes, and the plan says so for this scene.
- **How the scene keeps to that:**
  - There is no gag and no speech.
  - There is no comic business from Sidar or Vehbi.
  - The camera holds on the faces of the people in the queue.
- **The fall:** The plan allows one thing to fall: the banker's sign. It falls without slapstick, on one hook, then to the floor.
- **What it does for the story:** It sets up the reckoning in Scene 14 (stamp D5).

## 3. Synopsis

The office is as before: the queue at the window, the board at %150, the flock circling under the ceiling. All at once the flock lifts and streams out of the street door, bird after bird, until the room is quiet. The teller window's shutter comes down and the interest board goes dark. The people in the queue stand where they are, and their heads lower slowly, one after another. One hook of the KUŞ BANKERLİK sign gives way. It swings down on the other hook, hangs, and falls to the floor. Nobody moves.

### From the story plan (canon, verbatim)

| Field | Story plan |
|---|---|
| Plan timecode | 4:00 |
| Part | Banker |
| What happens | Sürü bir anda havalanır, gişe boşalır, kuyruk sessizleşir. |
| Joke or surprise | Ton değişir: Kayıp şaka konusu olmaz, yalnızca banker tabelası düşer. |
| “Sınavda çıkar” stamp | — |

## 4. Beat sheet

| Time (s) | Beat |
|---|---|
| 0.00 | The office, the queue, %150, the flock circling. |
| 2.80 | The flock lifts at once; everyone looks up. |
| 3.20–6.50 | The birds stream out of the street door, one after another. |
| 5.60 | The shutter comes down over the teller window; the board goes dark. |
| 6.00–9.70 | The queue stands still; heads lower slowly. Vehbi looks at them. |
| 10.00 | One hook of the sign gives; it swings down on the other. |
| 10.90–11.35 | The sign falls to the floor. |
| 11.35–14.60 | Nothing. |

## 5. Dialogue

None.

## 6. Characters in this scene

| | Sidar | Vehbi | The queue |
|---|---|---|---|
| Position | (4.70, 2.60) | (3.95, 2.35) | Back in line at the window |
| Faces used | rest (lids lower, no smug) | rest (brows a little up) | rest, lids lower, brows up |
| Business | Watches the flock go, then looks down | Watches the flock go, then looks at the people in the queue | Watch the flock go; heads lower, one after another |

## 7. Location and set

- **The office:** Scene 12's office, with the queue back in line.
- **The sign (changed):** It is now its own board (`tex/sign.jpg`), hung from two hooks over the partition. The back wall is painted without it, with the two hooks left showing.
  - It pivots on its left hook: 10.0–10.9, swinging down by 0.5 rad with a small wobble.
  - Then it drops to the floor by 11.35, turning further and coming forward 0.4 m.
- **The shutter (new):** A dark wooden panel that comes down over the teller window at 5.60.
- **The interest board:** Dark from 5.60 (no card showing).
- **The flock:** The 34 birds of Scene 11 lift at 2.80. Between 3.2 and 5.4 each in turn flies out through the street door and is gone 1.1 s later.

## 8. Shot list

| Shot | Code | In (s) | Out (s) | Length (s) | Framing and move | Content | Purpose |
|---|---|---|---|---|---|---|---|
| 01 | A | 0.00 | 5.60 | 5.60 | Wide, a little high | The flock lifts and leaves | The end of it |
| 02 | B | 5.60 | 9.70 | 4.10 | From beside the shut window, a slow move along the queue's faces | Stillness | Who it happened to |
| 03 | C | 9.70 | 14.60 | 4.90 | Wide and still | The sign falls | The only fall |

## 9. Timed events

| Event | Time (s) | Source |
|---|---|---|
| Flock lifts / exits | 2.80 / 3.20–5.40 | `room.LIFT`, `room.EXIT`, `room.exit_time` |
| Shutter, board dark | 5.60 | `room.SHUTTER`, `room.BOARD_DARK` |
| Sign: hook gives / falls / lands | 10.00 / 10.90 / 11.35 | `room.SIGN_HOOK`, `room.SIGN_FALL`, `room.SIGN_LAND`, `room.sign_pose` |

## 10. Sound

| Layer | What | When |
|---|---|---|
| Bed | Office hum | Whole scene |
| Wings | The flock circling, then a rush of wings fading out of the door | 0.00–6.00 |
| Shutter | Down, with a dull thud | 5.60 |
| Sign | A hook giving, a creak; the fall on the floor | 10.00, 11.35 |

There is no music and no speech.

## 11. Production status

| Stage | Status | Output |
|---|---|---|
| Story plan row | From the person's plan | Section 3 |
| Set | Scene 12's office; the sign separated; a shutter added | `project/setdef.py`, `project/make_tex_banker.py`, `project/room.py` |
| Direction | Done | `project/blocking.py`, `project/shots.py`, `project/acting.py` |
| Final render | Done, v01 | `final/` |
| Review by the person | Waiting | — |

## 12. Known weak points and next steps

| # | Weak point | Next step |
|---|---|---|
| 1 | The last bird is still leaving as shot B begins (until 6.5 s) and passes near a face. | Bring the last exits forward by half a second. |
| 2 | The sign falls flat as a board, with no bounce or dust. | Keep it plain, as the tone asks; add a small settle if wanted. |
| 3 | The silence relies on the mix; nobody here can hear it. | The person checks the sound and the length. |

## 13. Decisions log

| Date | Decision | By |
|---|---|---|
| 2026-11-08 | No speech, no comic business; the camera holds on the queue's faces | Claude |
| 2026-11-08 | "Gişe boşalır" is shown as the shutter coming down and the board going dark | Claude |
| 2026-11-08 | The sign hangs on one hook before it falls; no slapstick | Claude |

## 14. Files

| Path | What |
|---|---|
| `S13_SCENE.md` | This document |
| `final/S13_v01.mp4`, `final/S13_v01_contact-sheet.jpg` | First render and its contact sheet |
| `project/` | The renderable engine project |

## 15. How to re-render

```
cd <path>/S13/project && python3 make_tex_banker.py
python3 engine/toon.py <path>/S13/project lint
python3 engine/toon.py <path>/S13/project final        # about 45 min on 2 cores
```
