# Son Jeton · Scene 07 · The First Stamp

| Field | Value |
|---|---|
| Series | Son Jeton |
| Scene | 07 of 24 |
| Title | The First Stamp |
| Status | In review: v02 delivered (longer stamps), awaiting the person's notes |
| Current version | v02 (`final/S07_v02.mp4`), an edit of v01 |
| Runtime | 21.58 s (518 frames at 24 fps) |
| Format | 1280 × 720, 24 fps, H.264, AAC 48 kHz |
| Location | Inside the corner grocer's, just after midnight (Scene 06 continues) |
| Period | 25 January 1980, small hours |
| Characters | Sidar (landlord), Vehbi (tenant), the grocer (silent) |
| Spoken language | English; the stamp, the clipping and the textbook are in Turkish |
| Stamp | D1 |
| Series canon | `../00_Series/BIBLE.md`; story plan in `../00_Series/SCENE-INDEX.md`; lines in `../00_Series/DIALOGUE-DRAFT.md` |
| Previous scene | `../S06/S06_SCENE.md` |
| Next scene | `../S08/S08_SCENE.md` |
| Last updated | 2026-11-08 |

---

## 1. Logline

The first "Sınavda çıkar" stamp comes down, and the shop turns into a newspaper clipping: one dollar is now seventy lira. Vehbi's textbook says the same. Sidar takes the stamp as recognition of his thirty years at the bank.

## 2. Purpose

- **Topic:** The series' first documented fact. Everything before this was Sidar's fantasy; the stamp is the only thing in the show that is true. This scene establishes how a stamp looks, sounds and works, and later stamps (D2–D8) reuse `project/stamp.py`.
- **What the audience should take away:**
  - With the 24 January 1980 decisions, the lira was devalued.
  - One US dollar became 70 lira.
- **Comic engine:**
  - The fact and the book agree, so Vehbi is right as usual.
  - Sidar claims the stamp for himself, the same way he claims everything.

## 3. Synopsis

The shop, as Scene 06 left it, still has its swollen price cards. A big rubber stamp comes down out of the top of the frame. THUNK: everyone flinches, and a red SINAVDA ÇIKAR mark is left on the picture. The picture turns into a newspaper clipping, dated 25 OCAK 1980, under the headline "1 DOLAR 70 LİRA". The body text reads "24 Ocak 1980 kararlarıyla Türk lirası devalüe edildi: 1 ABD doları 70 lira oldu." The shop itself is the halftone photo, with the stamp over it. The clipping holds for 3.6 s and turns back into the shop.

Vehbi opens his book and holds it up. Insert, the page: "24 Ocak 1980: 1 ABD doları = 70 TL", underlined. Vehbi: "Seventy lira to the dollar. Same as the book." Sidar, moved, hand on heart: "Thirty years at the bank, and finally someone stamps my work." Vehbi: "It's not your stamp." Sidar, palms out, sincerely puzzled: "Whose else would it be?"

### From the story plan (canon, verbatim)

| Field | Story plan |
|---|---|
| Plan timecode | 2:00 |
| Part | 24 Ocak |
| What happens | Damga vurulur, görüntü gazete kupürüne döner. Vehbi kitabını gösterir: Rakam kitapta da aynıdır. |
| Joke or surprise | Sidar damgayı kendi mesleki başarısı sanar. |
| “Sınavda çıkar” stamp | D1 |

Plan's D1 text: "24 Ocak 1980 kararlarıyla dolar 70 liraya çıktı ve sabit kur politikası bırakıldı." Source: CNN Türk; plan status: "Sayfa açıldı".

Source: the person's doc “Son Jeton: 8 Dakikalık Hikâye Planı”. Where it conflicts with a later decision in the decisions log, the later decision wins.

## 4. Beat sheet

| Time (s) | Beat |
|---|---|
| 0.00 | The shop as Scene 06 left it. |
| 0.25–0.62 | The rubber stamp comes down out of the top of the frame. THUNK at 0.62: all three flinch and look up; a small frame shake. |
| 0.62–1.10 | The red mark sits on the picture. |
| 0.75–1.10 | The picture turns into the newspaper clipping. |
| 1.10–4.70 | The clipping holds: date, headline, the three-line body, the shop as a halftone photo, the stamp. |
| 4.70–5.05 | Back to the shop. |
| 5.00 | Vehbi opens the book and holds it up. |
| 5.05–7.40 | Insert: the textbook page, a slow push towards the underlined line. |
| 5.50 | Line 1 (over the insert, then on Vehbi from 7.40). |
| 9.50 | Line 2, hand on heart, eyes up to where the stamp came from. |
| 13.60 | Line 3. |
| 14.90 | Line 4, palms out. |
| 17.60 | End. |

## 5. Dialogue

| # | Character | Line (as spoken) | Turkish equivalent | Start (s) | Length (s) | Voice file | Direction |
|---|---|---|---|---|---|---|---|
| 1 | Vehbi | "Seventy lira to the dollar. Same as the book." | "Dolar yetmiş lira. Kitapta da aynı." | 5.50 | 3.66 | `project/voices/v1.wav` | Book open beside the clipping, satisfied. |
| 2 | Sidar | "Thirty years at the bank, and finally someone stamps my work." | "Bankada otuz yıl, sonunda biri işimi damgaladı." | 9.50 | 3.78 | `project/voices/s2.wav` | Moved, proud, hand on heart. |
| 3 | Vehbi | "It's not your stamp." | "O senin damgan değil." | 13.60 | 0.98 | `project/voices/v3.wav` | Flat. |
| 4 | Sidar | "Whose else would it be?" | "Başka kimin olacak?" | 14.90 | 1.49 | `project/voices/s4.wav` | Sincerely puzzled. |

- **Voices:** Generated in Voicebox from the consenting cloned voices. Silence trimmed from both ends, 48 kHz mono; the files as received are in `project/voices/raw/`.

## 6. Characters in this scene

| | Sidar | Vehbi | The grocer |
|---|---|---|---|
| Position | (3.40, 2.35), right | (1.60, 2.30), left | (1.95, 4.40), behind the counter |
| Held | — | The book, opened and held up (5.0–9.2) | — |
| Faces used | determined, smug, curious | unimpressed, correcting, slow_lid | curious, doubt |
| Never (enforced) | No embarrassed face; doesn't say "I was wrong" | Doesn't say "I don't know" | Never speaks |

## 7. Location and set

- **The shop:** Scene 06's shop, unchanged: the cards are still at 2.6 times their size, and the clock shows past twelve.
- **The stamp, the clipping and the textbook page:** All three are drawn over the finished picture in `project/stamp.py`, which later stamp scenes reuse.
  - **The stamp:** A cartoon rubber stamp with a wooden knob and handle and a dark rubber block. It comes down, hits, and lifts away. The mark is a red rounded frame reading "SINAVDA ÇIKAR", turned 8°, with uneven ink.
  - **The clipping:** A newsprint page with torn edges, turned 1.5°, with a shadow, on a dark table.
    - At the top: the date line "— 25 OCAK 1980 —" and the headline "1 DOLAR 70 LİRA" in serif.
    - Below: three lines of body text, and the rest of the column as grey lines with nothing readable.
    - The current frame appears as a halftone photo, with the red mark over it.
    - There is no masthead and no real newspaper's name.
  - **The textbook page:** An open book on a dark table, headed "TÜRKİYE EKONOMİSİ" and "Bölüm 4 · 1980 sonrası". All the text is grey lines except the one entry: "24 Ocak 1980: / 1 ABD doları = 70 TL", underlined in pencil.
- **Text:** In Turkish, because the audience will meet these facts in Turkish exams. The spoken lines stay in English.

## 8. Shot list

| Shot | Code | In (s) | Out (s) | Length (s) | Framing and move | Content | Purpose |
|---|---|---|---|---|---|---|---|
| 01 | A | 0.00 | 5.05 | 5.05 | Wide three-shot; the stamp and the clipping over it | D1 | The fact |
| 02 | B | 5.05 | 7.40 | 2.35 | Insert: the textbook page, slow push | Line 1 begins | The book agrees |
| 03 | C | 7.40 | 9.40 | 2.00 | Vehbi with the book held up | Line 1 ends | Satisfied |
| 04 | D | 9.40 | 13.40 | 4.00 | Sidar, slow push in | Line 2 | He takes the credit |
| 05 | E | 13.40 | 14.80 | 1.40 | Vehbi | Line 3 | Flat |
| 06 | F | 14.80 | 17.60 | 2.80 | Sidar, wider, the grocer and the cards | Line 4 | Sincerely puzzled |

## 9. Timed events

| Event | Time (s) | Source |
|---|---|---|
| Stamp down / hit / lifted | 0.25 / 0.62 / 0.90 | `room.STAMP` |
| Clipping in / hold / out | 0.75–1.10 / to 4.70 / 5.05 | `room.CLIP`, `room.clip` |
| Book opens | 5.00 | `room.BOOK_OPEN` |
| Textbook insert | 5.05–7.40 | `room.PAGE` |

## 10. Sound

| Layer | What | When |
|---|---|---|
| Bed | The bulb's hum, lowered under the clipping | Whole scene |
| Stamp | A rush down, a heavy rubber THUNK, a lift | 0.25–0.75 |
| Clipping | Newsprint rustle in and out | 0.75, 4.70 |
| Book | The cover and a page | 4.90–5.15 |
| Voices | Lines 1–4 | See the dialogue table |

The effects are synthesized placeholders. There is no music.

## 11. Production status

| Stage | Status | Output |
|---|---|---|
| Story plan row | From the person's plan | Section 3 |
| Stamp text | Checked against sources on 2026-11-08; narrowed (see the decisions log) | `project/room.py` |
| Lines | From `DIALOGUE-DRAFT.md`, recorded by the person | Section 5 |
| Rig | Reused | `project/cast.py` |
| Set | Scene 06's shop | `project/setdef.py`, `project/room.py` |
| Stamp, clipping, page | New and reusable | `project/stamp.py` |
| Direction | Done | `project/blocking.py`, `project/shots.py`, `project/acting.py` |
| Voices | Done | `project/voices/` |
| Sound | Placeholder | `project/sound.py` |
| Final render | Done, v01 | `final/` |
| Review by the person | Waiting | — |

## 12. Known weak points and next steps

| # | Weak point | Next step |
|---|---|---|
| 1 | The stamp's fact has been checked against web sources, not against the person's textbook. | The person compares D1 with their textbook before the script is locked, as the plan asks. |
| 2 | The stamp tool is drawn flat over the picture; it doesn't cast a shadow or touch anything in the shop. | A stylised device; fine unless the person wants it in the room. |
| 3 | Sidar's hand on his heart is mostly below the frame in shot D. | Widen shot D. |
| 4 | The textbook insert is a drawn page, not the 3D book in Vehbi's hand. | It reads as an insert; keep. |
| 5 | Effects are synthesized; nobody here can hear the mix. | The person checks the balance. |

## 13. Decisions log

| Date | Decision | By |
|---|---|---|
| 2026-11-08 | D1 narrowed to what the sources agree on: "24 Ocak 1980 kararlarıyla Türk lirası devalüe edildi: 1 ABD doları 70 lira oldu." The plan's second half ("sabit kur politikası bırakıldı") is left out. One source dates the daily exchange rate to 1 May 1981, another puts it inside the January 1980 programme. | Claude, after checking sources |
| 2026-11-08 | The stamp, clipping and textbook text are in Turkish; the spoken lines stay in English | Claude |
| 2026-11-08 | The clipping has no masthead and no real newspaper's name, only a date line | Claude |
| 2026-11-08 | Stamp, clipping and page live in `stamp.py`, reused for D2–D8 | Claude |
| 2026-11-09 | v02: the person asked for the decisions and the exam questions to be shown longer. The frame is held at 3.00 s: +4.0 s on the clipping (D1); the sound under the hold is the second before it, looped. Made from v01 with `../00_Full/hold.py`, no re-render. The project files still describe v01's timing. | The person; Claude |
| 2026-11-10 | v02 remade: the first v02 looped the last second of sound under the hold, so sounds repeated. Now the frame is held at 4.17 s for +4.0 s, and the sound under it is the room tone of [2.67, 4.17] s tiled with crossfades; no voice or effect repeats. Made from v01 with `../00_Full/hold2.py`. | The person's note; Claude |

## 14. Files

| Path | What |
|---|---|
| `S07_SCENE.md` | This document |
| `final/S07_v01.mp4` | First render, with voices |
| `final/S07_v01_contact-sheet.jpg` | Contact sheet of v01 |
| `project/` | The renderable engine project |
| `project/stamp.py` | The stamp, the newspaper clipping and the textbook insert (reusable) |
| `project/room.py` | Timing, and the stamp's text with its sources |
| `project/voices/` | `v1`, `s2`, `v3` and `s4` (`.wav` and `.tsv`); `raw/` holds the files as received |

## 15. How to re-render

```
cd <path>/S07/project && python3 make_tex_shop.py
python3 engine/toon.py <path>/S07/project lint
python3 engine/toon.py <path>/S07/project final        # about 35 min on 2 cores
```

## Sources for D1

- [Ekonomim: Dışa Açılma Dönemi](https://www.ekonomim.com/sozluk/disa-acilma-donemi): "Dolar 47 liradan 70 liraya yükseltildi." It dates the daily exchange rate to 1 May 1981.
- [CNN Türk: Tarihte bugün, 4 Ağustos](https://www.cnnturk.com/yasam/tarihte-bugun-4-agustos-240295): "24 ocak 1980 kararları sonrasında … bir dolar 70 liraya yükseldi."
- [Yeni Şafak: 40th year of Turkey's transition to liberal economy](https://en.yenisafak.com/economy/40th-year-of-turkeys-transition-to-liberal-economy-3510319): It puts the devaluation at 37.2% and places the daily rate inside the programme, with no date.
