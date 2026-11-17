# Son Jeton · Scene 17 · On Paper

| Field | Value |
|---|---|
| Series | Son Jeton |
| Scene | 17 of 24 |
| Title | On Paper |
| Status | In review: v02 delivered (longer stamps), awaiting the person's notes |
| Current version | v02 (`final/S17_v02.mp4`), an edit of v01 |
| Runtime | 18.58 s (446 frames at 24 fps) |
| Format | 1280 × 720, 24 fps, H.264, AAC 48 kHz |
| Location | The customs post on the quay (Scene 16 continues) |
| Period | Mid-1980s |
| Characters | Sidar, Vehbi, the customs officer (silent) |
| Spoken language | English; the stamp, the clipping and the textbook are in Turkish |
| Stamp | D6 |
| Series canon | `../00_Series/BIBLE.md`; story plan in `../00_Series/SCENE-INDEX.md`; lines in `../00_Series/DIALOGUE-DRAFT.md` |
| Previous scene | `../S16/S16_SCENE.md` |
| Next scene | `../S18/S18_SCENE.md` |
| Last updated | 2026-11-08 |

---

## 1. Logline

The stamp names the real export incentives of the 1980s, and Vehbi finds them in his textbook. Sidar takes the credit for putting the ships on paper. Vehbi: "That's the problem."

## 2. Purpose

- **Topic:** Export incentives after 1980, chiefly tax refunds and export credits (D6). This is the documented fact behind the paper ships.
- **What it does for the story:** It sets up D7 (fictitious exports, Scene 19). Incentives paid against paper invite paper exports.
- **Comic engine:** Sidar proudly confesses the problem as an achievement, and Vehbi names it in three words.

## 3. Synopsis

The customs post, a moment after Scene 16. Two paper ships are afloat, a tiny one still peeks out of the open drawer, and the officer is bent over his forms. The stamp comes down. The clipping, headlined "İHRACATA TEŞVİK", reads: "1980 sonrasında ihracat; vergi iadesi ve ihracat kredisi gibi teşviklerle desteklendi." Vehbi raises his textbook: "Tax refunds and export credits." Insert: the page, with "İhracat teşvikleri: vergi iadesi, ihracat kredisi" underlined. He taps the page: "It's in the book." Sidar, chest out, with a hand to his ships: "I put these ships on paper." Vehbi, flat: "That's the problem." Sidar doesn't hear it.

### From the story plan (canon, verbatim)

| Field | Story plan |
|---|---|
| Plan timecode | 5:20 |
| Part | Hayali ihracat |
| What happens | Damga ihracat teşviklerini anlatır. Vehbi kitaptan onaylar. |
| Joke or surprise | Sidar: “Bu gemileri ben kâğıda geçirdim.” |
| “Sınavda çıkar” stamp | D6 |

- **The plan's D6 text:** "1980 sonrasında ihracat, vergi iadesi ve ihracat kredileri gibi teşviklerle desteklendi."

## 4. Beat sheet

| Time (s) | Beat |
|---|---|
| 0.00 | The post: two paper ships, the tiny one in the drawer, the officer at his forms. |
| 0.60–1.25 | The stamp (D6). They look up; the officer doesn't. |
| 1.10–5.50 | The clipping. |
| 5.80 | Vehbi raises the book. |
| 6.20 | Line 1. |
| 6.75–8.35 | Insert: the textbook page. |
| 8.60, 9.20 | Two taps on the page: "It's in the book." |
| 10.40 | Line 2, chest out, a hand to the ships. |
| 13.00 | Line 3. Sidar, pleased with himself, doesn't hear it. |
| 14.58 | End. |

## 5. Dialogue

| # | Character | Line (as spoken) | Turkish equivalent | Start (s) | Length (s) | Voice file | Direction |
|---|---|---|---|---|---|---|---|
| 1 | Vehbi | "Tax refunds and export credits. It's in the book." | "Vergi iadesi ve ihracat kredisi. Kitapta var." | 6.20 | 3.69 | `project/voices/v1.wav` | Confirming, finger on the page. |
| 2 | Sidar | "I put these ships on paper." | "Bu gemileri ben kâğıda geçirdim." | 10.40 | 2.08 | `project/voices/s2.wav` | Proud. |
| 3 | Vehbi | "That's the problem." | "Sorun da o." | 13.00 | 0.76 | `project/voices/v3.wav` | Flat. |

- **Voices:** Generated in Voicebox from the consenting cloned voices. Silence trimmed from both ends, 48 kHz mono. The files as received are in `project/voices/raw/`.

## 6. Characters in this scene

| | Sidar | Vehbi | The customs officer |
|---|---|---|---|
| Position | (−7.6, 1.5), facing Vehbi | (−6.1, 0.7), facing Sidar | Behind the counter |
| Held | — | The book, raised for the line | His stamp |
| Faces used | smug, bluff | unimpressed, correcting, slow_lid | rest, head down |
| Never (enforced) | He never says "I was wrong" | He never says "I don't know" | He never speaks, never looks up |

## 7. Location and set

- **The customs post:** Scene 16's set, as Scene 16 left it.
  - **The form:** It carries three red marks.
  - **The drawer:** It stays open, with the tiny ship peeking out.
  - **The ships:** Two paper ships are afloat; the second one drifts slowly.
- **The stamp, the clipping and the textbook insert:** From `stamp.py`. The insert's underlined lines now come from `room.PAGE_LINES`.

## 8. Shot list

| Shot | Code | In (s) | Out (s) | Length (s) | Framing and move | Content | Purpose |
|---|---|---|---|---|---|---|---|
| 01 | A | 0.00 | 5.70 | 5.70 | High wide; the stamp and the clipping over it | D6 | The fact |
| 02 | B | 5.70 | 10.20 | 4.50 | Vehbi from the front left, the book raised; the page insert at 6.75–8.35 | Line 1 | It's in the book |
| 03 | C | 10.20 | 12.75 | 2.55 | Sidar, the ships behind him | Line 2 | The proud confession |
| 04 | D | 12.75 | 14.58 | 1.83 | Vehbi, closer | Line 3 | The verdict |

## 9. Timed events

| Event | Time (s) | Source |
|---|---|---|
| Stamp / clipping | 0.60–1.25 / 1.10–5.50 | `room.STAMP`, `room.CLIP` |
| Book up | 5.80 | `room.BOOK_OPEN` |
| Textbook insert | 6.75–8.35 | `room.PAGE`, `room.PAGE_LINES` |

## 10. Sound

| Layer | What | When |
|---|---|---|
| Bed | Sea wind; water against the quay wall; lowered under the clipping | Whole scene |
| Stamp | Rush, THUNK (gain 0.25), newsprint | 0.60–1.30 |
| Book | A page; two taps | 5.80; 8.60, 9.20 |
| Gulls | Far off | 5.8, 12.9 |
| Voices | Lines 1–3 | See the dialogue table |

The ships make no sound. The effects are synthesized placeholders. There is no music.

## 11. Production status

| Stage | Status | Output |
|---|---|---|
| Story plan row | From the person's plan | Section 3 |
| Stamp text | Checked against sources on 2026-11-08 | `project/room.py`, sources below |
| Lines | From `DIALOGUE-DRAFT.md`, recorded by the person | Section 5 |
| Set | Scene 16's customs post | `project/setdef.py`, `project/room.py` |
| Direction | Done | `project/blocking.py`, `project/shots.py`, `project/acting.py` |
| Final render | Done, v01 | `final/` |
| Review by the person | Waiting | — |

## 12. Known weak points and next steps

| # | Weak point | Next step |
|---|---|---|
| 1 | D6 has been checked against two thesis abstracts, not the person's textbook. The textbook insert is the show's own page, not a real book. | Compare D6 with the textbook before the script is locked. |
| 2 | Vehbi's finger points past the book from this angle rather than landing on the page. | A closer insert of the finger on the page, or a different camera. |
| 3 | The textbook insert's headings ("TÜRKİYE EKONOMİSİ", "Bölüm 4") are the same as in Scene 07. | Fine for the same book; change the chapter if wanted. |
| 4 | Effects are synthesized. | The person checks the balance. |

## 13. Decisions log

| Date | Decision | By |
|---|---|---|
| 2026-11-08 | D6 wording: "1980 sonrasında ihracat; vergi iadesi ve ihracat kredisi gibi teşviklerle desteklendi." Kept to the plan's wording; both instruments are named in the sources. Date line "1980'LER". | Claude, after checking sources |
| 2026-11-08 | The textbook insert in `stamp.py` takes its underlined lines from `room.PAGE_LINES`, so later stamps can reuse it | Claude |
| 2026-11-08 | Sidar doesn't hear "That's the problem": he never concedes | Claude |
| 2026-11-09 | v02: the person asked for the decisions and the exam questions to be shown longer. The frame is held at 3.00 s: +4.0 s on the clipping (D6); the sound under the hold is the second before it, looped. Made from v01 with `../00_Full/hold.py`, no re-render. The project files still describe v01's timing. | The person; Claude |
| 2026-11-10 | v02 remade: the first v02 looped the last second of sound under the hold, so sounds repeated. Now the frame is held at 3.46 s for +4.0 s, and the sound under it is the room tone of [1.66, 3.46] s tiled with crossfades; no voice or effect repeats. Made from v01 with `../00_Full/hold2.py`. | The person's note; Claude |

## 14. Files

| Path | What |
|---|---|
| `S17_SCENE.md` | This document |
| `final/S17_v01.mp4`, `final/S17_v01_contact-sheet.jpg` | First render and its contact sheet |
| `final/S17_v02.mp4` | v02: the stamps held longer (see the decisions log) |
| `project/` | The renderable engine project |
| `project/stamp.py` | The stamp, the clipping, the textbook insert (now with `PAGE_LINES`) |
| `project/voices/` | `v1`, `s2`, `v3` (`.wav` and `.tsv`); `raw/` holds the files as received |

## 15. How to re-render

```
cd <path>/S17/project && python3 make_tex_harbour.py
python3 engine/toon.py <path>/S17/project lint
python3 engine/toon.py <path>/S17/project final        # about 30 min on 2 cores
```

## Sources for D6

- [YÖK tezi: Export promoting policies in Turkish manufacturing industry, 1980-1986](https://acikbilim.yok.gov.tr/handle/20.500.12812/39732?show=full). From the abstract:
  - "export subsidies (tax rebates, export credits and foreign currency allocations)"
  - "The tax rebates and foreign currency allocations are the most significant promoting policies"
- [YÖK tezi: 24 Ocak Kararları sonrasında ihracatta vergi teşvik politikası uygulaması ve değerlendirilmesi](https://acikbilim.yok.gov.tr/handle/20.500.12812/333648?show=full). From the abstract:
  - "24 Ocak Kararları'nın bir bölümü, ihracatın teşvikine yönelik önlemleri kapsamaktadır."
  - Vergi iadesi "1980 sonrası ihracatın teşvikinde önemli bir paya sahip"; it ended in 1988.
