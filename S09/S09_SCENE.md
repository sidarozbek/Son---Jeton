# Son Jeton · Scene 09 · The Third Token

| Field | Value |
|---|---|
| Series | Son Jeton |
| Scene | 09 of 24 |
| Title | The Third Token |
| Status | In review: v02 delivered (longer stamps), awaiting the person's notes |
| Current version | v02 (`final/S09_v02.mp4`), an edit of v01 |
| Runtime | 20.58 s (494 frames at 24 fps) |
| Format | 1280 × 720, 24 fps, H.264, AAC 48 kHz |
| Location | The street from Scene 04, by the grocer's (shutter down), morning |
| Period | 12 September 1980 |
| Characters | Sidar (landlord), Vehbi (tenant) |
| Spoken language | None: nobody speaks. The stamp and the clipping are in Turkish. |
| Stamp | D3 |
| Series canon | `../00_Series/BIBLE.md`; story plan in `../00_Series/SCENE-INDEX.md` |
| Previous scene | `../S08/S08_SCENE.md` |
| Next scene | `../S10/S10_SCENE.md` |
| Last updated | 2026-11-08 |

---

## 1. Logline

The morning of 12 September 1980. The street from January is empty, the shutters are down, and nobody speaks. Sidar drops the third token without a word, and a quiet stamp records that the January decisions went on after the coup.

## 2. Purpose

- **Topic:** The coup, treated with restraint. The scene only records the economic fact the plan asks for (D3); it doesn't depict the coup itself.
- **Tone:** The series rule is that the coup is never a subject for jokes. The plan asks for no joke here, so the scene has none:
  - nothing fantastic happens, and nobody speaks;
  - Sidar isn't smug;
  - the stamp is quieter than the others, and nobody flinches.
- **What it does for the story:** The fantasy pauses. Sidar's tokens become something he spends without ceremony.

## 3. Synopsis

The street from Scene 04, on a grey September morning. There is no snow, the grocer's shutter is down, and nothing moves. Sidar and Vehbi stand on the sidewalk. Vehbi looks slowly along the empty street, one way and then the other. Sidar walks to a payphone on the wall, and Vehbi follows a few steps behind. Sidar takes out the third token, looks at it a moment, and drops it in. The stamp comes down, more quietly than before. The clipping, under the headline "12 EYLÜL 1980", reads: "Askerî darbeden sonra 24 Ocak kararları uygulanmaya devam etti." It holds to the end.

### From the story plan (canon, verbatim)

| Field | Story plan |
|---|---|
| Plan timecode | 2:40 |
| Part | 12 Eylül |
| What happens | Sessiz ve boş bir sokak, sabah. Fantastik görüntüler durur, kimse konuşmaz. Sidar sessizce üçüncü jetonu atar. |
| Joke or surprise | Şaka yok. |
| “Sınavda çıkar” stamp | D3 |

The plan's D3 text is "12 Eylül 1980 askeri darbesinden sonra 24 Ocak kararları uygulanmaya devam etti." Its sources (an academic article and Kure Ansiklopedi) were marked "Arama özeti".

## 4. Beat sheet

| Time (s) | Beat |
|---|---|
| 0.00–4.60 | Very wide and still: the empty street, the two of them small on the sidewalk. Wind, and a far-off bird. |
| 3.00–6.60 | Vehbi looks slowly along the street, one way and then the other. |
| 5.50–8.70 | Sidar walks to the payphone on the wall; Vehbi follows a few steps behind. |
| 8.60 | Sidar takes out the third token and looks at it. |
| 10.10 | The token goes into the slot. |
| 10.80–11.50 | The stamp, quieter than before. They look up slowly and don't flinch. |
| 11.35–16.60 | The clipping holds. |

## 5. Dialogue

None, by the plan: "kimse konuşmaz".

## 6. Characters in this scene

| | Sidar | Vehbi |
|---|---|---|
| Path | (5.45, 4.65) → the payphone at (8.25, 5.42) | (4.60, 4.75) → (7.35, 5.00) |
| Held | The third token | The book |
| Faces used | rest (heavier lids, no smug) | rest (lids a little heavier, brows slightly up) |

## 7. Location and set

- **The street:** Scene 04's street, in September. The road and pavement were repainted without snow, and the snow heaps, the snow on the awning and the snow on the van were removed.
- **The grocer's:** Its front is a rolled-down metal shutter under the same BAKKAL sign board, and the calendar is gone.
- **The street lamps:** Off.
- **The payphone:** On the facade right of the grocer, at x 8.4. It is Scene 03's design.
- **Light:**
  - Flat, cool, grey daylight (gain 0.78, 0.80, 0.84), a little brighter higher up.
  - The sky is pale grey.
  - Saturation is lowered for the set (0.70) and for the characters (0.80).
- **The stamp and the clipping:** From `stamp.py`. There is no textbook insert.

## 8. Shot list

| Shot | Code | In (s) | Out (s) | Length (s) | Framing and move | Content | Purpose |
|---|---|---|---|---|---|---|---|
| 01 | A | 0.00 | 4.60 | 4.60 | Very wide, almost still | The empty street | Silence |
| 02 | B | 4.60 | 6.60 | 2.00 | Vehbi | He looks along the street | He sees it |
| 03 | C | 6.60 | 8.60 | 2.00 | Following the walk | To the phone | — |
| 04 | D | 8.60 | 10.75 | 2.15 | Sidar in profile at the phone | The third token | Without ceremony |
| 05 | E | 10.75 | 16.60 | 5.85 | Wide; the stamp and the clipping over it | D3 | The fact |

## 9. Timed events

| Event | Time (s) | Source |
|---|---|---|
| Token out / into the slot | 8.60 / 10.10 | `room.TOKEN_OUT`, `room.COIN_IN` |
| Stamp / clipping | 10.80–11.50 / from 11.35 | `room.STAMP`, `room.CLIP` |

## 10. Sound

| Layer | What | When |
|---|---|---|
| Wind | Steady, the only bed; no hum | Whole scene |
| Bird | One far-off bird, twice | 2.40, 7.10 |
| Steps | Slow steps to the phone | 5.50–8.70 |
| Token | Clink and a short rattle | 10.25 |
| Stamp | One soft thud (gain 0.15, half the earlier stamps); newsprint | 11.20, 11.35 |

There is no music and no speech.

## 11. Production status

| Stage | Status | Output |
|---|---|---|
| Story plan row | From the person's plan | Section 3 |
| Stamp text | Checked against sources on 2026-11-08 | `project/room.py`, sources below |
| Set | Scene 04's street, in September | `project/setdef.py`, `project/make_tex_street.py` |
| Direction | Done | `project/blocking.py`, `project/shots.py`, `project/acting.py` |
| Sound | Placeholder | `project/sound.py` |
| Final render | Done, v01 | `final/` |
| Review by the person | Waiting | — |

## 12. Known weak points and next steps

| # | Weak point | Next step |
|---|---|---|
| 1 | The D3 fact has been checked against web sources, not the person's textbook. | Compare it with the textbook before the script is locked. |
| 2 | Sidar's hand with the token sits low in shot D, so the token is small. | A higher reach in the next pass. |
| 3 | The plan's "kimse konuşmaz" is kept literally, and the scene is carried by silence. It should be watched with sound to judge whether the silence holds. | The person checks the length. |
| 4 | Effects are synthesized. | The person checks the balance. |

## 13. Decisions log

| Date | Decision | By |
|---|---|---|
| 2026-11-08 | No military imagery: the scene shows only an empty street and shutters, and the stamp carries the fact | Claude |
| 2026-11-08 | The stamp is quieter (half gain) and nobody flinches, unlike Scenes 07–08 | Claude |
| 2026-11-08 | D3 headline "12 EYLÜL 1980"; body "Askerî darbeden sonra 24 Ocak kararları uygulanmaya devam etti."; date line "EYLÜL 1980" | Claude, after checking sources |
| 2026-11-09 | v02: the person asked for the decisions and the exam questions to be shown longer. The frame is held at 13.50 s: +4.0 s on the clipping (D3); the sound under the hold is the second before it, looped. Made from v01 with `../00_Full/hold.py`, no re-render. The project files still describe v01's timing. | The person; Claude |
| 2026-11-10 | v02 remade: the first v02 looped the last second of sound under the hold, so sounds repeated. Now the frame is held at 15.58 s for +4.0 s, and the sound under it is the room tone of [14.08, 15.58] s tiled with crossfades; no voice or effect repeats. Made from v01 with `../00_Full/hold2.py`. | The person's note; Claude |

## 14. Files

| Path | What |
|---|---|
| `S09_SCENE.md` | This document |
| `final/S09_v01.mp4`, `final/S09_v01_contact-sheet.jpg` | First render and its contact sheet |
| `final/S09_v02.mp4` | v02: the stamps held longer (see the decisions log) |
| `project/` | The renderable engine project (`stamp.py` shared with Scenes 07–08) |

## 15. How to re-render

```
cd <path>/S09/project && python3 make_tex_street.py
python3 engine/toon.py <path>/S09/project lint
python3 engine/toon.py <path>/S09/project final        # about 35 min on 2 cores
```

## Sources for D3

- [Milliyet Uzmanpara: Türkiye ekonomisinde "Özallı yıllar"](https://uzmanpara.milliyet.com.tr/haber-detay/gundem2/turkiye-ekonomisinde-ozalli-yillar/45000/45536): After 12 September Özal became Deputy Prime Minister for the economy: "Gelen yönetim 24 Ocak Kararları ile başladığımız işe devam etmemi istedi."
- [Medyascope: 24 Ocak kararlarından günümüz ekonomik krizine](https://medyascope.tv/2022/01/24/dosya-haber-24-ocak-kararlarindan-gunumuz-ekonomik-krizine-uzanan-surec/): "12 Eylül darbesiyle uygulanma imkanı bulan 24 Ocak Kararları".
