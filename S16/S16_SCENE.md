# Son Jeton · Scene 16 · The Filing Cabinet

| Field | Value |
|---|---|
| Series | Son Jeton |
| Scene | 16 of 24 |
| Title | The Filing Cabinet |
| Status | In review: first render delivered, awaiting the person's notes |
| Current version | v01 (`final/S16_v01.mp4`) |
| Runtime | 13.58 s (326 frames at 24 fps) |
| Format | 1280 × 720, 24 fps, H.264, AAC 48 kHz |
| Location | The harbour from Scene 15, at a customs post on the quay |
| Period | Mid-1980s |
| Characters | Sidar, Vehbi, the customs officer (new, silent) |
| Spoken language | English; the sign is in Turkish |
| Stamp | None (the officer's stamp is a sound effect, not a "Sınavda çıkar" stamp) |
| Series canon | `../00_Series/BIBLE.md`; story plan in `../00_Series/SCENE-INDEX.md`; lines in `../00_Series/DIALOGUE-DRAFT.md` |
| Previous scene | `../S15/S15_SCENE.md` |
| Next scene | `../S17/S17_SCENE.md` |
| Last updated | 2026-11-08 |

---

## 1. Logline

An imaginary customs officer stamps a form, and a new see-through ship climbs out of his filing cabinet and hops into the sea. Sidar is proud of it. Vehbi points at the cabinet, and Sidar genuinely wants to know where else ships come from.

## 2. Purpose

- **Topic:** It sets up export on paper (D6 in Scene 17, D7 in Scene 19). A stamp makes a ship; the paperwork is the ship.
- **The picture:** Fantasy, in Sidar's world. There are no numbers, names or claims on screen.
- **Comic engine:**
  - Cause and effect played completely straight: stamp, drawer, ship.
  - Sidar's sincere question.
  - The officer never looks up.

## 3. Synopsis

On the quay outside the harbour office stands a customs officer at a standing counter, with a grey filing cabinet beside him. He stamps a form: thunk. The top drawer of the cabinet slides open, a tiny folded paper ship rises out of it, and then it hops over the quay edge, growing as it goes. It lands in the water full size and see-through, like the ships in Scene 15. Sidar watches Vehbi's face rather than the ship: "See? One stamp, one ship." The officer stamps again, and another ship climbs out of the drawer. Vehbi, deadpan, with a finger at the cabinet: "It came out of a filing cabinet." Sidar, palms up, genuinely asking: "Where else do ships come from?" The officer stamps a third time. The drawer opens, and a tiny ship peeks out.

### From the story plan (canon, verbatim)

| Field | Story plan |
|---|---|
| Plan timecode | 5:00 |
| Part | Hayali ihracat |
| What happens | Hayali gümrükçü kâğıda damga vurunca yeni bir saydam gemi belirir. |
| Joke or surprise | Gemi denize değil, evrak dolabından çıkar. |
| “Sınavda çıkar” stamp | — |

## 4. Beat sheet

| Time (s) | Beat |
|---|---|
| 0.00 | The customs post: officer, counter, cabinet; Sidar and Vehbi. |
| 0.70 | Stamp one. The drawer opens (1.00); a tiny ship rises out (1.25–1.70). |
| 1.70–3.70 | It hops over the quay edge, growing, and lands full size. |
| 4.00 | Line 1. Sidar watches Vehbi, not the ship. |
| 6.30 | Stamp two; the second ship comes out (6.85) and lands further out (9.30), then drifts off. |
| 7.20 | Line 2, a finger at the cabinet. |
| 10.10 | Line 3, palms up. |
| 12.15 | Stamp three; the drawer opens; a tiny ship peeks out and stays there. |
| 13.58 | End. |

## 5. Dialogue

| # | Character | Line (as spoken) | Turkish equivalent | Start (s) | Length (s) | Voice file | Direction |
|---|---|---|---|---|---|---|---|
| 1 | Sidar | "See? One stamp, one ship." | "Gördün mü? Bir damga, bir gemi." | 4.00 | 1.99 | `project/voices/s1.wav` | Proud. |
| 2 | Vehbi | "It came out of a filing cabinet." | "Evrak dolabından çıktı." | 7.20 | 2.24 | `project/voices/v2.wav` | Deadpan. |
| 3 | Sidar | "Where else do ships come from?" | "Gemiler başka nereden çıkar?" | 10.10 | 1.54 | `project/voices/s3.wav` | Genuinely asking. |

- **Voices:** Generated in Voicebox from the consenting cloned voices. Silence trimmed from both ends, 48 kHz mono. The files as received are in `project/voices/raw/`.
- **Line 3's file:** The file for line 3 arrived as `v3.wav`. In `DIALOGUE-DRAFT.md` the line is Sidar's (`s3`), so it is used as Sidar's line and saved as `s3.wav`; the original is kept as `raw/v3.wav`. If the take was recorded in Vehbi's voice, it should be re-recorded.
- **The officer:** He has no line; his stamp is a sound.

## 6. Characters in this scene

| | Sidar | Vehbi | The customs officer |
|---|---|---|---|
| Position | (−7.6, 1.5), facing Vehbi | (−6.1, 0.7), facing Sidar | (−9.95, 1.2), behind the counter, facing +x |
| Held | — | The book | A plain wooden rubber stamp |
| Faces used | smug, asking | rest, curious, unimpressed, correcting, slow_lid | rest, head down |
| Never (enforced) | He never says "I was wrong" | He never says "I don't know" | He never speaks, never looks up |

- **The customs officer (new):**
  - **Design:** Original, generic and silent. He is the grocer's build in a navy uniform coat with a peaked cap, 1.72 m tall, with four fingers like everyone else.
  - **Code:** `project/cast.py` (`OFFICER`).
  - **How he stamps:** His right hand is pinned onto the form for each blow.

## 7. Location and set

- **The harbour:** Scene 15's set (`project/make_tex_harbour.py`, `project/setdef.py`). The crates by the office were removed so they don't block the post.
- **The customs post (new):**
  - **Counter:** A standing wooden counter at (−9.0, 1.2), 0.95 m high.
  - **Form:** A form with ruled lines lies on the counter. A red square mark appears for every stamp, drawn in `env.draw_form`.
  - **Filing cabinet:** Grey, 1.3 m tall, at (−9.9, 2.4), with its drawers facing the quay.
  - **Top drawer:** Its own object. It slides out 0.38 m after each stamp and shuts once the ship is out (`room.drawer`, `setdef.animate`).
- **The ships:**
  - **New ones:** They come out of the drawer as tiny folded paper ships. At that size they are nearly opaque; as they grow they become see-through (`room.ship_state`, `env.draw_ship`).
  - **The hop:** An arc over the quay edge, turning a little as it goes.
  - **Background:** Two ships from Scene 15 drift further out.

## 8. Shot list

| Shot | Code | In (s) | Out (s) | Length (s) | Framing and move | Content | Purpose |
|---|---|---|---|---|---|---|---|
| 01 | A | 0.00 | 3.85 | 3.85 | High wide from the land | Stamp one; the first ship | Cause and effect |
| 02 | B | 3.85 | 6.20 | 2.35 | Sidar, the new ship behind him | Line 1 | Pride |
| 03 | C | 6.20 | 8.60 | 2.40 | Vehbi from the front left | Line 2 begins | Deadpan |
| 04 | C2 | 8.60 | 9.95 | 1.35 | Wide | Line 2 ends; ship two lands | Proof |
| 05 | D | 9.95 | 11.95 | 2.00 | Sidar, closer | Line 3 | The sincere question |
| 06 | E | 11.95 | 13.58 | 1.63 | The cabinet, pushing in | Stamp three; a tiny ship peeks out | The button |

## 9. Timed events

| Event | Time (s) | Source |
|---|---|---|
| Stamps | 0.70, 6.30, 12.15 | `room.STAMPS` |
| Drawer out / in | Stamp + 0.30 / stamp + 1.45 (the last stays open) | `room.drawer` |
| Ship rises / hops / lands | Stamp + 0.55 / + 1.00 / + 3.00 | `room.RISE`, `room.FLY` |

## 10. Sound

| Layer | What | When |
|---|---|---|
| Bed | Sea wind; water against the quay wall | Whole scene |
| Stamp | A dry wooden thump with a click | Each stamp |
| Drawer | Rolling open on runners; shutting | Stamp + 0.30; stamp + 1.45 |
| Paper | Unfolding as a ship rises | Stamp + 0.55 |
| Hop / plop | A soft rush; a small splash on landing | Ships one and two |
| Gulls | Far off | 2.2, 9.8 |
| Voices | Lines 1–3 | See the dialogue table |

The ships themselves make no sound. The effects are synthesized placeholders. There is no music.

## 11. Production status

| Stage | Status | Output |
|---|---|---|
| Story plan row | From the person's plan | Section 3 |
| Lines | From `DIALOGUE-DRAFT.md`, recorded by the person | Section 5 |
| Rig | The customs officer, new | `project/cast.py` |
| Set | Scene 15's harbour, plus the customs post | `project/setdef.py`, `project/room.py` |
| Direction | Done | `project/blocking.py`, `project/shots.py`, `project/acting.py` |
| Final render | Done, v01 | `final/` |
| Review by the person | Waiting | — |

## 12. Known weak points and next steps

| # | Weak point | Next step |
|---|---|---|
| 1 | Line 3's file was named `v3`; it is used as Sidar's line. | The person confirms it is Sidar's voice, or re-records it. |
| 2 | The ship coming out of the drawer is small in the wide shot; the moment it rises is easy to miss before it starts hopping. | A short insert of the drawer for the first ship too, like the last shot. |
| 3 | The rubber stamp is drawn from simple circles and is small; the stamping reads mostly from the arm and the sound. | A better stamp prop, or a close-up of the stamp on the form. |
| 4 | In Vehbi's shot his pointing finger aims off screen; the cabinet isn't in that frame. | The wide shot right after shows the cabinet and the second ship. |
| 5 | Close up, the landed ships behind Sidar read as glass boxes (as in Scene 15). | The same fix as Scene 15. |
| 6 | In Sidar's last close-up ("Where else...") the frame cuts through his beard; his mouth sits at the bottom edge. | Tilt the camera down a little. |
| 7 | Effects are synthesized. | The person checks the balance. |

## 13. Decisions log

| Date | Decision | By |
|---|---|---|
| 2026-11-08 | A new silent character: the customs officer, in a navy uniform and a peaked cap, on the grocer's build | Claude |
| 2026-11-08 | "Gemi evrak dolabından çıkar" is shown as a tiny paper ship rising out of the top drawer and growing as it hops into the sea | Claude |
| 2026-11-08 | Three stamps: the rule of three, and the last ship stays in the drawer as the button | Claude |
| 2026-11-08 | Sidar watches Vehbi's face, not the ships: he is proud of the trick, not curious about it | Claude |
| 2026-11-08 | The file `v3.wav` is used as Sidar's line 3, as in the draft | Claude |

## 14. Files

| Path | What |
|---|---|
| `S16_SCENE.md` | This document |
| `final/S16_v01.mp4`, `final/S16_v01_contact-sheet.jpg` | First render and its contact sheet |
| `project/` | The renderable engine project |
| `project/voices/` | `s1`, `v2`, `s3` (`.wav` and `.tsv`); `raw/` holds the files as received (`s1`, `v2`, `v3`) |

## 15. How to re-render

```
cd <path>/S16/project && python3 make_tex_harbour.py
python3 engine/toon.py <path>/S16/project lint
python3 engine/toon.py <path>/S16/project final        # about 30 min on 2 cores
```
