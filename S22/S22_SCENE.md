# Son Jeton · Scene 22 · The Sixth Token

| Field | Value |
|---|---|
| Series | Son Jeton |
| Scene | 22 of 24 |
| Title | The Sixth Token |
| Status | In review: v02 delivered (longer stamps), awaiting the person's notes |
| Current version | v02 (`final/S22_v02.mp4`), an edit of v01 |
| Runtime | 21.17 s (508 frames at 24 fps) |
| Format | 1280 × 720, 24 fps, H.264, AAC 48 kHz |
| Location | The 1989 street, at the river of money (Scene 21 continues) |
| Period | August 1989 |
| Characters | Sidar, Vehbi |
| Spoken language | English; the stamp, the clipping and the textbook are in Turkish |
| Stamp | D8 |
| Series canon | `../00_Series/BIBLE.md`; story plan in `../00_Series/SCENE-INDEX.md`; lines in `../00_Series/DIALOGUE-DRAFT.md` |
| Previous scene | `../S21/S21_SCENE.md` |
| Next scene | `../S23/S23_SCENE.md` |
| Last updated | 2026-11-09 |

---

## 1. Logline

Vehbi finds the answer in his book: since August 1989, money can cross the border freely. If money flows, a token flows too. A token comes glinting down the river of money and hops into his hand. Sidar takes the credit.

## 2. Purpose

- **Topic:** Decision No. 32 of 7 August 1989, which freed capital movements (D8).
- **What it does for the story:**
  - It turns the low point. This is the first time Vehbi's book does more than correct Sidar: it gets them home.
  - It fulfils the plan's world rule: "Beşinci jeton kaybolur, altıncısı 1989'da bulunur."
- **Character:**
  - Vehbi is right and gets the reward.
  - Sidar's anger came back, and with it his habit of taking the credit: "I taught you where to look." He still never says "I was wrong."

## 3. Synopsis

At the river of money, Vehbi opens his textbook: "August 1989. Money can cross the border freely now." Insert: the page, "7 Ağustos 1989 · 32 Sayılı Karar: sermaye hareketleri serbest", underlined. The stamp comes down. The clipping, headlined "32 SAYILI KARAR", reads: "7 Ağustos 1989 tarihli 32 Sayılı Kararla sermaye hareketleri serbestleşti." Something glints in the river. Vehbi steps to the kerb and faces upstream: "If money flows… a token flows too." A token comes turning down the river among the notes, glinting. He puts out his hand, and it hops out of the river into his palm. He holds it up to his eyes and almost smiles. Sidar, himself again: "I taught you where to look."

### From the story plan (canon, verbatim)

| Field | Story plan |
|---|---|
| Plan timecode | 7:00 |
| Part | 1989 |
| What happens | Vehbi kararı kitaptan bulur: Paranın aktığı yerde jeton da akar. Irmakta parlayan jetonu yakalar. |
| Joke or surprise | Sidar: “Nereye bakacağını ben öğrettim.” |
| “Sınavda çıkar” stamp | D8 |

- **The plan's D8 text:** "7 Ağustos 1989 tarihli 32 Sayılı Kararla sermaye hareketleri serbestleşti."

## 4. Beat sheet

| Time (s) | Beat |
|---|---|
| 0.55 | Vehbi raises the book. |
| 0.90 | Line 1, his finger on the page. |
| 2.40–4.00 | Insert: the textbook page. |
| 4.90–5.55 | The stamp (D8). |
| 5.40–9.60 | The clipping. |
| 9.80 | The glint. |
| 9.90–10.60 | Vehbi to the kerb, facing upstream. |
| 10.00 | Line 2. |
| 12.20 | His hand goes out, palm up. |
| 12.45–13.00 | The token hops out of the river into his palm. |
| 13.05 | He holds it up to his eyes and almost smiles. |
| 13.40 | Sidar goes smug. |
| 14.60 | Line 3. |
| 17.17 | End. |

## 5. Dialogue

| # | Character | Line (as spoken) | Turkish equivalent | Start (s) | Length (s) | Voice file | Direction |
|---|---|---|---|---|---|---|---|
| 1 | Vehbi | "August 1989. Money can cross the border freely now." | "Ağustos 1989. Para artık sınırı serbestçe geçebiliyor." | 0.90 | 3.68 | `project/voices/v1.wav` | Reading, finger on the page. |
| 2 | Vehbi | "If money flows… a token flows too." | "Para akıyorsa… jeton da akar." | 10.00 | 3.75 | `project/voices/v2.wav` | Working it out as he says it. |
| 3 | Sidar | "I taught you where to look." | "Nereye bakacağını ben öğrettim." | 14.60 | 1.43 | `project/voices/s3.wav` | Smug again. |

- **Voices:** Generated in Voicebox from the consenting cloned voices. Silence trimmed from both ends, 48 kHz mono. The files as received are in `project/voices/raw/`.

## 6. Characters in this scene

| | Sidar | Vehbi |
|---|---|---|
| Path | (6.1, 4.7) | (5.0, 4.85) → the kerb (5.15, 4.42), facing upstream |
| Held | — | The book; then the sixth token |
| Faces used | sad (from Scene 21), curious, smug | realizing, correcting, curious, almost_smile, unimpressed |
| Never (enforced) | He never says "I was wrong" | He never says "I don't know" |

## 7. Location and set

- **The 1989 street and the river of money:** As in Scene 21.
- **The sixth token (new):**
  - **Look:** A brass token with a hole, turning as it drifts, with a four-point glint from 9.80.
  - **Motion:** It comes down the river near the kerb, hops in an arc into Vehbi's palm (`room.token`), then is drawn with him in his hand (`env.on_actor`).
- **The stamp, the clipping and the textbook insert:** From `stamp.py`, with `PAGE_LINES`.

## 8. Shot list

| Shot | Code | In (s) | Out (s) | Length (s) | Framing and move | Content | Purpose |
|---|---|---|---|---|---|---|---|
| 01 | A | 0.00 | 4.80 | 4.80 | Vehbi with the book; the page insert at 2.40–4.00 | Line 1 | Found it |
| 02 | B | 4.80 | 9.70 | 4.90 | High wide over the river; the stamp and the clipping over it | D8 | The fact |
| 03 | C | 9.70 | 13.30 | 3.60 | Low by the river, looking downstream at Vehbi as the token comes | Line 2; the hop | A token flows too |
| 04 | D | 13.30 | 14.45 | 1.15 | Vehbi and the token, held up | The sixth token | Got it |
| 05 | E | 14.45 | 17.17 | 2.72 | Sidar | Line 3 | Credit taken |

## 9. Timed events

| Event | Time (s) | Source |
|---|---|---|
| Book / page insert | 0.55 / 2.40–4.00 | `room.BOOK_OPEN`, `room.PAGE`, `room.PAGE_LINES` |
| Stamp / clipping | 4.90–5.55 / 5.40–9.60 | `room.STAMP`, `room.CLIP` |
| Glint / reach / hop | 9.80 / 12.20 / 12.45–13.00 | `room.GLINT`, `room.REACH`, `room.HOP` |

## 10. Sound

| Layer | What | When |
|---|---|---|
| River | Running water with paper in it | Whole scene |
| Book | A page | 0.55 |
| Stamp | Rush, THUNK (gain 0.25), newsprint | 4.90–5.60 |
| Glint | A bright chime | 9.80 |
| Hop / catch | A soft rush; a small metal click and a chime | 12.45, 13.00 |
| Voices | Lines 1–3 | See the dialogue table |

The effects are synthesized placeholders. There is no music.

## 11. Production status

| Stage | Status | Output |
|---|---|---|
| Story plan row | From the person's plan | Section 3 |
| Stamp text | Checked against sources on 2026-11-09 | `project/room.py`, sources below |
| Lines | From `DIALOGUE-DRAFT.md`, recorded by the person | Section 5 |
| Set | Scene 21's street and river | `project/setdef.py`, `project/env.py` |
| Direction | Done | `project/blocking.py`, `project/shots.py`, `project/acting.py` |
| Final render | Done, v01 | `final/` |
| Review by the person | Waiting | — |

## 12. Known weak points and next steps

| # | Weak point | Next step |
|---|---|---|
| 1 | D8 has been checked against the decision's official text (date and number) and a thesis abstract, not the person's textbook. | Compare it with the textbook before the script is locked. |
| 2 | In the low river shot Sidar stands right behind Vehbi and overlaps him. | Move Sidar a step aside for that shot. |
| 3 | Close to the camera, the river reads as notes lying on the pavement rather than floating. | A water sheen and ripples near the kerb. |
| 4 | The token is drawn flat (an oval with a hole); up close it's simple. | Fine at this size. |
| 5 | Effects are synthesized. | The person checks the balance. |

## 13. Decisions log

| Date | Decision | By |
|---|---|---|
| 2026-11-09 | D8 wording kept as the plan has it; date line "AĞUSTOS 1989". Date and number checked against the decision's text: Bakanlar Kurulu 07.08.1989, no. 89/14391; Resmî Gazete 11.08.1989. | Claude, after checking sources |
| 2026-11-09 | "Irmakta parlayan jetonu yakalar" is the token hopping out of the river into his palm, so he doesn't have to kneel | Claude |
| 2026-11-09 | Sidar's sadness from Scene 21 carries in, then flips to smug when the token is found | Claude |
| 2026-11-09 | v02: the person asked for the decisions and the exam questions to be shown longer. The frame is held at 7.50 s: +4.0 s on the clipping (D8); the sound under the hold is the second before it, looped. Made from v01 with `../00_Full/hold.py`, no re-render. The project files still describe v01's timing. | The person; Claude |
| 2026-11-10 | v02 remade: the first v02 looped the last second of sound under the hold, so sounds repeated. Now the frame is held at 8.79 s for +4.0 s, and the sound under it is the room tone of [7.29, 8.79] s tiled with crossfades; no voice or effect repeats. Made from v01 with `../00_Full/hold2.py`. | The person's note; Claude |

## 14. Files

| Path | What |
|---|---|
| `S22_SCENE.md` | This document |
| `final/S22_v01.mp4`, `final/S22_v01_contact-sheet.jpg` | First render and its contact sheet |
| `final/S22_v02.mp4` | v02: the stamps held longer (see the decisions log) |
| `project/` | The renderable engine project |
| `project/voices/` | `v1`, `v2`, `s3` (`.wav` and `.tsv`); `raw/` holds the files as received |

## 15. How to re-render

```
cd <path>/S22/project && python3 make_tex_1989.py
python3 engine/toon.py <path>/S22/project lint
python3 engine/toon.py <path>/S22/project final        # about 40 min on 2 cores
```

## Sources for D8

- [TÜRMOB: Türk Parası Kıymetini Koruma Hakkında 32 Sayılı Karar](https://www.turmob.org.tr/arsiv/mbs/pratikBilgiler/TurkParasiKiymetini_32sayiliKarar-2022.pdf): the decision's date (07.08.1989, no. 89/14391) and publication (Resmî Gazete 11.08.1989, no. 20249).
- [Selçuk Üniversitesi: Finansal Serbestleşme Sürecinde Türkiye Ekonomisinde Faiz ve Kur İlişkisi](https://acikerisim.selcuk.edu.tr/items/a45719fc-fb22-45bb-ac49-b97982bd4c0e/full). From the abstract:
  - "1989 yılında alınan 32 Sayılı Karar ile finansal serbestleşme süreci başlatılarak"
  - "The Turkish economy was opened to the speculative movements of the international capital … with the law number 32 enacted in 1989"
