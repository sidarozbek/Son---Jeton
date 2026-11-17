# Son Jeton · Scene 19 · Of Invoices

| Field | Value |
|---|---|
| Series | Son Jeton |
| Scene | 19 of 24 |
| Title | Of Invoices |
| Status | In review: v02 delivered (longer stamps), awaiting the person's notes |
| Current version | v02 (`final/S19_v02.mp4`), an edit of v01 |
| Runtime | 19.79 s (475 frames at 24 fps) |
| Format | 1280 × 720, 24 fps, H.264, AAC 48 kHz |
| Location | The customs post; Sidar on the deck of the paper ship (Scene 18 continues) |
| Period | Mid-1980s |
| Characters | Sidar, Vehbi, the customs officer (silent) |
| Spoken language | English; the stamp and the clipping are in Turkish |
| Stamp | D7 |
| Series canon | `../00_Series/BIBLE.md`; story plan in `../00_Series/SCENE-INDEX.md`; lines in `../00_Series/DIALOGUE-DRAFT.md` |
| Previous scene | `../S18/S18_SCENE.md` |
| Next scene | `../S20/S20_SCENE.md` |
| Last updated | 2026-11-08 |

---

## 1. Logline

The stamp explains fictitious exports. The containers on Sidar's ship swing open empty, and invoices burst out of them and rain over the harbour. Vehbi is right, but Sidar catches an invoice and waves it like proof.

## 2. Purpose

- **Topic:** Fictitious exports, "hayali ihracat" (D7): exports shown on paper but never sent, with fake invoices used to claim tax refunds.
- **The picture:** Fantasy, in Sidar's world. The invoices are blank forms with a red mark, carrying no names and no figures.
- **Comic engine:**
  - Vehbi's three-item list plays out on screen, item by item.
  - Sidar turns the evidence into his trophy.
  - "Of invoices!"

## 3. Synopsis

Sidar is still on the deck of the paper ship, with Vehbi on the quay below. The stamp comes down. The clipping, headlined "HAYALİ İHRACAT", reads: "Mal gönderilmiş gibi gösterildi; sahte faturayla devletten vergi iadesi alındı." Vehbi counts on his fingers: "Empty containers…" The lids of the three containers swing open behind Sidar, and there is nothing inside. "…Fake invoices…" Invoices burst out of them, high into the air, and flutter down over the deck, the quay and the water. "…Refunds for goods that never left." One flutters into Sidar's hand. He waves it high: "Told you!" Vehbi: "You said the ships were full." Sidar, triumphant: "Of invoices!"

### From the story plan (canon, verbatim)

| Field | Story plan |
|---|---|
| Plan timecode | 6:00 |
| Part | Hayali ihracat |
| What happens | Damga hayali ihracatı anlatır. Boş konteynerler açılır, içlerinden fatura yağar. |
| Joke or surprise | Vehbi haklıdır, ama Sidar “Demiştim” diye fatura sallar. |
| “Sınavda çıkar” stamp | D7 |

- **The plan's D7 text:** "Hayali ihracat: Mal gönderilmiş gibi gösterilir, sahte faturayla devletten vergi iadesi alınır."

## 4. Beat sheet

| Time (s) | Beat |
|---|---|
| 0.60–1.25 | The stamp (D7). |
| 1.10–5.50 | The clipping. |
| 5.80 | Line 1: one, two, three on his fingers. |
| 6.25–6.90 | The lids swing open; the containers are empty. Sidar turns to look. |
| 7.30 | Invoices burst out of all three containers. Sidar: "realizing". |
| 7.30–15.80 | They rain down and settle on the quay and the deck; those in the water sink. |
| 9.40 | Sidar sees an opportunity (smug). |
| 10.20–10.60 | One flutters into his hand. |
| 10.75 | Line 2, waving it high. |
| 11.60 | Line 3. |
| 13.70 | Line 4, triumphant. |
| 15.80 | End. |

## 5. Dialogue

| # | Character | Line (as spoken) | Turkish equivalent | Start (s) | Length (s) | Voice file | Direction |
|---|---|---|---|---|---|---|---|
| 1 | Vehbi | "Empty containers. Fake invoices. Refunds for goods that never left." | "Boş konteyner. Sahte fatura. Hiç gitmeyen mala iade." | 5.80 | 4.55 | `project/voices/v1.wav` | Clear, quick, counting on his fingers. |
| 2 | Sidar | "Told you!" | "Demiştim!" | 10.75 | 0.47 | `project/voices/s2.wav` | Waving an invoice. |
| 3 | Vehbi | "You said the ships were full." | "Gemiler dolu demiştin." | 11.60 | 1.73 | `project/voices/v3.wav` | Patient. |
| 4 | Sidar | "Of invoices!" | "Faturayla!" | 13.70 | 1.09 | `project/voices/s4.wav` | Triumphant. |

- **Voices:** Generated in Voicebox from the consenting cloned voices. Silence trimmed from both ends, 48 kHz mono. The files as received are in `project/voices/raw/`.

## 6. Characters in this scene

| | Sidar | Vehbi | The customs officer |
|---|---|---|---|
| Position | On ship A's deck, (−6.45, 5.0), 1.0 m above the quay | On the quay below, (−6.6, 2.6) | Behind the counter |
| Held | An invoice, from 10.60 | The book | His stamp |
| Faces used | smug, realizing, try_smile, bluff | unimpressed, correcting, slow_lid, one_brow | rest, head down |
| Never (enforced) | He never says "I was wrong" | He never says "I don't know" | He never speaks, never looks up |

## 7. Location and set

- **The customs post and the gangway:** As in Scene 18.
- **The containers' lids (new):** On ship A, each container's top is its own face and swings open about its back edge (`room.lid`, in `env.draw_ship`).
- **The invoices (new):**
  - **Look:** 72 sheets, 0.30 × 0.21 m: a ruled form with a red mark in the corner.
  - **Motion:** Each is shot up out of a container, then flutters down, drifting and swaying. Sheets on the quay or the deck stay where they land; sheets in the water sink (`room.sheet`).
  - **Drawing:** Sheets beyond both characters are drawn under them, the rest over them (`env.draw_sheets`).
  - **The one Sidar catches:** It goes to his hand and is then drawn with him, waved.

## 8. Shot list

| Shot | Code | In (s) | Out (s) | Length (s) | Framing and move | Content | Purpose |
|---|---|---|---|---|---|---|---|
| 01 | A | 0.00 | 5.60 | 5.60 | High wide from the land; the stamp and the clipping over it | D7 | The fact |
| 02 | B | 5.60 | 10.65 | 5.05 | High two-shot along the quay, widening | Line 1; lids; the burst; the rain; the catch | Proof, made visible |
| 03 | C | 10.65 | 11.50 | 0.85 | Sidar on the deck from the quay | Line 2 | Trophy |
| 04 | D | 11.50 | 13.55 | 2.05 | Vehbi, the counter behind him | Line 3 | Patience |
| 05 | E | 13.55 | 15.80 | 2.25 | Sidar | Line 4 | Of invoices |

## 9. Timed events

| Event | Time (s) | Source |
|---|---|---|
| Stamp / clipping | 0.60–1.25 / 1.10–5.50 | `room.STAMP`, `room.CLIP` |
| Lids | 6.25, 6.45, 6.65 | `room.LIDS`, `room.lid` |
| Burst | 7.30 (staggered 0–1 s) | `room.BURST`, `room.SHEETS` |
| Catch | 10.20–10.60 | `room.CATCH` |

## 10. Sound

| Layer | What | When |
|---|---|---|
| Bed | Sea wind; water against the quay wall; lowered under the clipping | Whole scene |
| Stamp | Rush, THUNK (gain 0.25), newsprint | 0.60–1.30 |
| Lids | A hollow clank each | 6.45, 6.65, 6.85 |
| Invoices | A rush, then paper rustling, thinning out | 7.25–13.00 |
| Catch / waving | Paper | 10.60 on |
| Voices | Lines 1–4 | See the dialogue table |

The effects are synthesized placeholders. There is no music.

## 11. Production status

| Stage | Status | Output |
|---|---|---|
| Story plan row | From the person's plan | Section 3 |
| Stamp text | Checked against sources on 2026-11-08 | `project/room.py`, sources below |
| Lines | From `DIALOGUE-DRAFT.md`, recorded by the person | Section 5 |
| Set | Scene 18's set, plus the lids and the invoices | `project/env.py`, `project/room.py` |
| Direction | Done | `project/blocking.py`, `project/shots.py`, `project/acting.py` |
| Final render | Done, v01 | `final/` |
| Review by the person | Waiting | — |

## 12. Known weak points and next steps

| # | Weak point | Next step |
|---|---|---|
| 1 | D7 has been checked against open-university course material and a thesis abstract, not the person's textbook. | Compare it with the textbook before the script is locked. |
| 2 | The lids open behind Sidar's head in the two-shot; with see-through containers, "empty" is easy to miss. | A short insert looking down into an open container. |
| 3 | Invoices between the two characters can be drawn over the farther one. | Fine at this distance. |
| 4 | A gangway post stands right by Sidar's legs on the deck. | Move the post or Sidar. |
| 5 | The invoices land near the quay edge and on the deck; none reach Vehbi's side of the quay, so his close-up has no paper around him. | Throw a few further inland. |
| 6 | Effects are synthesized. | The person checks the balance. |

## 13. Decisions log

| Date | Decision | By |
|---|---|---|
| 2026-11-08 | D7 wording: "Mal gönderilmiş gibi gösterildi; sahte faturayla devletten vergi iadesi alındı." The plan's present tense was put in the past; date line "1980'LER". No company or person is named. | Claude, after checking sources |
| 2026-11-08 | The containers open on Vehbi's "Empty containers" and the invoices burst on "Fake invoices": his list plays out as he says it | Claude |
| 2026-11-08 | "Demiştim" is Sidar waving a caught invoice; "Told you!" as recorded | Claude |
| 2026-11-09 | v02: the person asked for the decisions and the exam questions to be shown longer. The frame is held at 3.00 s: +4.0 s on the clipping (D7); the sound under the hold is the second before it, looped. Made from v01 with `../00_Full/hold.py`, no re-render. The project files still describe v01's timing. | The person; Claude |
| 2026-11-10 | v02 remade: the first v02 looped the last second of sound under the hold, so sounds repeated. Now the frame is held at 4.17 s for +4.0 s, and the sound under it is the room tone of [2.37, 4.17] s tiled with crossfades; no voice or effect repeats. Made from v01 with `../00_Full/hold2.py`. | The person's note; Claude |

## 14. Files

| Path | What |
|---|---|
| `S19_SCENE.md` | This document |
| `final/S19_v01.mp4`, `final/S19_v01_contact-sheet.jpg` | First render and its contact sheet |
| `final/S19_v02.mp4` | v02: the stamps held longer (see the decisions log) |
| `project/` | The renderable engine project |
| `project/voices/` | `v1`, `s2`, `v3`, `s4` (`.wav` and `.tsv`); `raw/` holds the files as received |

## 15. How to re-render

```
cd <path>/S19/project && python3 make_tex_harbour.py
python3 engine/toon.py <path>/S19/project lint
python3 engine/toon.py <path>/S19/project final        # about 40 min on 2 cores
```

## Sources for D7

- [Anadolu Üniversitesi AÖF ders materyali (soru-cevap): fictitious exports in 1980s Turkey](https://aof.sorular.net/sorucevap/what-can-be-said-about-fictitious-exports-in-1980s-of-turkey):
  - "Fictitious exports were fabricated transactions to take advantage of export incentives, especially tax refunds."
  - Some exports were claimed even though nothing was shipped.
- [YÖK tezi: İhracat işlemlerinde katma değer vergisi uygulaması…](https://acikbilim.yok.gov.tr/handle/20.500.12812/27755?show=full):
  - "Naylon fatura ve hayali ihracat olayına adı karışanlar, haksız bir şekilde katma değer vergisi iadesi hakkını elde etmektedirler."
  - The tax refund was abolished after fictitious export cases came to light.
