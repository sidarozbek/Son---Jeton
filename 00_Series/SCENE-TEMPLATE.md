# Son Jeton · Scene {NN} · {TITLE}

| Field | Value |
|---|---|
| Series | Son Jeton |
| Scene | {NN} of 24 |
| Title | [TBD] |
| Status | Not started |
| Current version | — |
| Runtime | [TBD] (target about 20 s; may run longer if the scene needs it) |
| Format | 1280 × 720, 24 fps, H.264, AAC 48 kHz |
| Location | [TBD] |
| Period | [TBD] |
| Characters | [TBD] |
| Spoken language | English |
| Series canon | `../00_Series/BIBLE.md` (Style Lock, character cards) |
| Brief | `S{NN}_BRIEF.md` (once approved) |
| Previous scene | {PREV} |
| Next scene | {NEXT} |
| Last updated | {DATE} |

---

## 1. Logline

[TBD] One sentence: who wants what, and what goes wrong.

## 2. Purpose

- **Topic:** [TBD] The real subject this scene teaches or shows.
- **Audience:** University students with short attention spans.
- **What this scene tests:** [TBD]
- **Comic engine:** [TBD] The mechanism that makes it funny.

## 3. Synopsis

[TBD] One paragraph, start to end.

## 4. Beat sheet

| Time (s) | Beat |
|---|---|
| [TBD] | [TBD] |

## 5. Dialogue

| # | Character | Line (as spoken) | Turkish original | Start (s) | Length (s) | Voice file | Direction |
|---|---|---|---|---|---|---|---|
| 1 | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] | `project/voices/[TBD].wav` | [TBD] |

## 6. Characters in this scene

The design source is `../00_Series/BIBLE.md`. Only what is particular to this scene is listed here.

| | [Character] | [Character] |
|---|---|---|
| Role here | [TBD] | [TBD] |
| Starts | [TBD] | [TBD] |
| Ends | [TBD] | [TBD] |
| Held | [TBD] | [TBD] |
| Default face | [TBD] | [TBD] |
| Faces used | [TBD] | [TBD] |
| Never (enforced) | From the bible | From the bible |
| Gags | [TBD] | [TBD] |
| Voice | From the bible | From the bible |

Show rules: four fingers and no thumb for every character; Sidar and Vehbi are the same height; reference photos take priority for looks.

## 7. Location and set

- **Description:** [TBD]
- **Size and layout:** [TBD]
- **Cultural layer:** [TBD]
- **Light:** [TBD]
- **Textures and props:** [TBD]
- **Reused from earlier scenes:** [TBD] (for example, the rented room from Scene 01: `../S01/project/setdef.py`)

## 8. Shot list

| Shot | Code | In (s) | Out (s) | Length (s) | Framing and move | Content | Purpose |
|---|---|---|---|---|---|---|---|
| 01 | A | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] |

## 9. Timed events

| Event | Time (s) | Source |
|---|---|---|
| [TBD] | [TBD] | [TBD] |

## 10. Sound

| Layer | What | When |
|---|---|---|
| Bed | [TBD] | [TBD] |
| Contact | [TBD] | [TBD] |
| Voices | See the dialogue table | — |

## 11. Production status

| Stage | Status | Output |
|---|---|---|
| Brief | Not started | `S{NN}_BRIEF.md` |
| Style Lock and character cards | Locked (series) | `../00_Series/BIBLE.md` |
| Rig | Reuse `../S01/project/cast.py` | — |
| Set | Not started | — |
| Direction | Not started | — |
| Voices | Not started | — |
| Sound | Not started | — |
| Final render | Not started | — |
| Review by the person | — | — |

## 12. Known weak points and next steps

| # | Weak point | Next step |
|---|---|---|
| — | — | — |

## 13. Decisions log

| Date | Decision | By |
|---|---|---|
| — | — | — |

## 14. Files

| Path | What |
|---|---|
| `S{NN}_SCENE.md` | This document |
| `S{NN}_BRIEF.md` | The approved brief (once made) |
| `final/` | Rendered versions: `S{NN}_vXX_<note>.mp4` |
| `project/` | The renderable engine project |
| `review/` | Test frames, contact sheets, animatic |
| `archive/` | Superseded files |

## 15. How to re-render

From a Toon Studio folder with the engine set up (`tools/setup.sh`):

```
python3 engine/toon.py <path>/S{NN}/project lint
python3 engine/toon.py <path>/S{NN}/project animatic
python3 engine/toon.py <path>/S{NN}/project final
```
