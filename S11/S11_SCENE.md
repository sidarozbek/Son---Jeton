# Son Jeton · Scene 11 · The Birds

| Field | Value |
|---|---|
| Series | Son Jeton |
| Scene | 11 of 24 |
| Title | The Birds |
| Status | In review: v02 delivered (longer stamps), awaiting the person's notes |
| Current version | v02 (`final/S11_v02.mp4`), an edit of v01 |
| Runtime | 19.02 s (456 frames at 24 fps) |
| Format | 1280 × 720, 24 fps, H.264, AAC 48 kHz |
| Location | The office of "Kuş Bankerlik" (Scene 10's set) |
| Period | 1981–82 |
| Characters | Sidar, Vehbi, the six people in the queue (silent) |
| Spoken language | English; the stamp and the clipping are in Turkish |
| Stamp | D4 |
| Series canon | `../00_Series/BIBLE.md`; story plan in `../00_Series/SCENE-INDEX.md`; lines in `../00_Series/DIALOGUE-DRAFT.md` |
| Previous scene | `../S10/S10_SCENE.md` |
| Next scene | `../S12/S12_SCENE.md` |
| Last updated | 2026-11-08 |

---

## 1. Logline

The coins on the banker's counter turn into birds, and the flock grows as the rate climbs. Each bird carries a coin from the newest customer to the oldest, and Sidar calls it profit while Vehbi calls it a chain.

## 2. Purpose

- **Topic:** How a banker's scheme works. The money from new depositors pays the old ones, so the scheme needs ever more newcomers.
- **The picture:** Fantasy, in Sidar's world. The birds carry the coin from the back of the queue to the front.
- **The stamp:** D4 gives the documented part. The January decisions freed interest rates, bankers offered high interest, and the system only ran while new customers kept coming.
- **Comic engine:** Two names for the same picture: "profit" and "a chain".

## 3. Synopsis

At Kuş Bankerlik the board reads %90, and the coins on the window's counter turn into birds one by one and fly up under the ceiling. The board climbs to %120, then %150, and the flock grows with it. A bird takes a coin from the newest customer at the back of the queue and carries it to the oldest one at the front, who smiles. Vehbi follows it with his finger: "Look. New money pays the old customers." Sidar, lecturing: "That's called profit." Another bird carries another coin. Vehbi: "That's called a chain." The stamp comes down. The clipping, under the headline "FAİZLER SERBEST", reads: "24 Ocak 1980 kararlarıyla faizler serbest bırakıldı. Bankerler yüksek faiz önerdi; sistem ancak yeni müşteriler geldikçe dönebiliyordu." It holds to the end.

### From the story plan (canon, verbatim)

| Field | Story plan |
|---|---|
| Plan timecode | 3:20 |
| Part | Banker |
| What happens | Kasadaki paralar kuşa dönüşür. Faiz arttıkça sürü büyür. |
| Joke or surprise | Kuşlar yeni gelenin parasını eski müşteriye taşır. |
| “Sınavda çıkar” stamp | D4 |

- **The plan's D4 text:** "Faizler 24 Ocak kararlarıyla serbest kaldı. Bankerler yüksek faiz sundu, faiz ödemek için daha yüksek faizle borçlanmak zorunda kaldı."
- **The plan's sources:** Çukurova Üniversitesi and an Ankara Üniversitesi lecture note, marked "Arama özeti".

## 4. Beat sheet

| Time (s) | Beat |
|---|---|
| 0.00 | The office, the queue, the board at %90, coins on the window's counter. |
| 0.80–2.20 | The five coins turn into birds, one after another, and fly up to circle under the ceiling. Everyone looks up. |
| 2.60 / 6.50 | The board shows %120, then %150. The flock grows to 34 birds. |
| 3.00–5.20 | The first carry: the newest customer (q5) holds out a coin, a bird takes it up the queue, and the oldest (q0) catches it and smiles. |
| 3.20 | Line 1. Vehbi's finger tracks the bird. |
| 6.20 | Line 2, with a raised finger. |
| 7.00–8.80 | The second carry. |
| 8.20 | Line 3. |
| 9.90–10.55 | The stamp (D4). Everyone jolts and looks up. |
| 10.40–15.00 | The clipping holds. |

## 5. Dialogue

| # | Character | Line (as spoken) | Turkish equivalent | Start (s) | Length (s) | Voice file | Direction |
|---|---|---|---|---|---|---|---|
| 1 | Vehbi | "Look. New money pays the old customers." | "Bak. Yeni gelenin parası eskilere gidiyor." | 3.20 | 2.56 | `project/voices/v1.wav` | Following one bird with his finger. |
| 2 | Sidar | "That's called profit." | "Buna kâr denir." | 6.20 | 1.59 | `project/voices/s2.wav` | Lecturing. |
| 3 | Vehbi | "That's called a chain." | "Buna zincir denir." | 8.20 | 1.07 | `project/voices/v3.wav` | Dry. |

- **Voices:** Generated in Voicebox from the consenting cloned voices. Silence trimmed from both ends, 48 kHz mono. The files as received are in `project/voices/raw/`.

## 6. Characters in this scene

| | Sidar | Vehbi | The queue |
|---|---|---|---|
| Position | (4.70, 2.60) | (3.95, 2.35) | As at the end of Scene 10 |
| Faces used | smug, determined | unimpressed, correcting | rest, curious; q0 almost_smile on each catch |
| Business | A raised finger on "profit" | His finger tracks the bird | q5 holds out a coin; q0 catches it |

## 7. Location and set

- **The office:** Scene 10's office, unchanged. The board starts at %90 and adds %120 and %150. The first card is now full size from frame 0, which fixes Scene 10's blank first frames.
- **The coins:** Five lie on the window's counter, at (3.0, 5.25, 1.04).
- **The birds:** An original design: a small golden-brown bird with an oval body, a head with an eye, and two curved wings that flap.
  - They are drawn in `env.top` at 3D positions, each about 0.11 m across.
  - The first five rise out of the coin pile, then circle under the ceiling around (3.1, 3.4, 2.45).
  - The flock grows with every rise of the rate, up to 34 birds.
  - The carrying bird is a little bigger and has a coin under it. It flies in an arc from q5's hand to q0's hand, at 3.0–5.2 and again at 7.0–8.8.
- **The stamp and the clipping:** From `stamp.py`.

## 8. Shot list

| Shot | Code | In (s) | Out (s) | Length (s) | Framing and move | Content | Purpose |
|---|---|---|---|---|---|---|---|
| 01 | A | 0.00 | 2.60 | 2.60 | High wide, tilting up from the counter to the ceiling | The coins become birds | The fantasy |
| 02 | B | 2.60 | 6.00 | 3.40 | From the right: the whole queue and the flock | The first carry; line 1 | The mechanism |
| 03 | C | 6.00 | 8.00 | 2.00 | Sidar from the front left | Line 2 | Profit |
| 04 | D | 8.00 | 9.80 | 1.80 | Vehbi | Line 3 | A chain |
| 05 | E | 9.80 | 15.00 | 5.20 | High wide; the stamp and the clipping over it | D4 | The fact |

## 9. Timed events

| Event | Time (s) | Source |
|---|---|---|
| Coins hatch into birds | 0.80–2.20 | `room.HATCH` |
| Board %120 / %150 | 2.60 / 6.50 | `room.RATE_TIMES` |
| Flock size | Grows to 34 | `room.flock_size` |
| Carries | 3.00–5.20, 7.00–8.80 | `room.CARRIES` |
| Stamp / clipping | 9.90–10.55 / from 10.40 | `room.STAMP`, `room.CLIP` |

## 10. Sound

| Layer | What | When |
|---|---|---|
| Bed | Office hum, lower under the clipping | Whole scene |
| Hatching | A clink, then a flutter, for each coin | 0.80–2.20 |
| Flock | Wingbeats growing denser; a chirp now and then | 2.50–9.90 |
| Board | A clatter of flaps at each rise | 2.60, 6.50 |
| Coins | A click at each hand-over | 3.00, 5.20, 7.00, 8.80 |
| Stamp | Rush, THUNK (0.3), lift; newsprint | 9.90–10.75 |
| Voices | Lines 1–3 | See the dialogue table |

## 11. Production status

| Stage | Status | Output |
|---|---|---|
| Story plan row | From the person's plan | Section 3 |
| Stamp text | Checked against the source on 2026-11-08, and narrowed | `project/room.py`, sources below |
| Lines | From `DIALOGUE-DRAFT.md`, recorded by the person | Section 5 |
| Set | Scene 10's office | `project/setdef.py`, `project/make_tex_banker.py` |
| Birds | New | `project/env.py` |
| Direction | Done | `project/blocking.py`, `project/shots.py`, `project/acting.py` |
| Final render | Done, v01 | `final/` |
| Review by the person | Waiting | — |

## 12. Known weak points and next steps

| # | Weak point | Next step |
|---|---|---|
| 1 | In the opening wide shot the coin pile is partly hidden behind the front of the queue, so the moment the coins become birds is small. | A short insert on the counter. |
| 2 | The birds are drawn over the characters, not depth-sorted; a bird can show over someone's head that is nearer to the camera. | Keep the flock high under the ceiling, as now. |
| 3 | The carrying bird is easy to miss in the wide shot among the flock. | Make it bigger, or give it a short insert. |
| 4 | D4 has been checked against one academic source's abstract, not the person's textbook. | Compare it with the textbook before the script is locked. |
| 5 | Effects are synthesized. | The person checks the balance. |

## 13. Decisions log

| Date | Decision | By |
|---|---|---|
| 2026-11-08 | D4 narrowed to what the source states. The plan's "faiz ödemek için daha yüksek faizle borçlanmak zorunda kaldı" is not in the abstract, so it was replaced by "sistem ancak yeni müşteriler geldikçe dönebiliyordu". | Claude, after checking the source |
| 2026-11-08 | The coins become birds on the window's counter (the "kasa" is behind the window, so the counter is where we see the money) | Claude |
| 2026-11-08 | The birds are an original simple design, golden-brown, drawn as 2D shapes in 3D space | Claude |
| 2026-11-09 | v02: the person asked for the decisions and the exam questions to be shown longer. The frame is held at 12.50 s: +4.0 s on the clipping (D4); the sound under the hold is the second before it, looped. Made from v01 with `../00_Full/hold.py`, no re-render. The project files still describe v01's timing. | The person; Claude |
| 2026-11-10 | v02 remade: the first v02 looped the last second of sound under the hold, so sounds repeated. Now the frame is held at 13.92 s for +4.0 s, and the sound under it is the room tone of [12.42, 13.92] s tiled with crossfades; no voice or effect repeats. Made from v01 with `../00_Full/hold2.py`. | The person's note; Claude |

## 14. Files

| Path | What |
|---|---|
| `S11_SCENE.md` | This document |
| `final/S11_v01.mp4`, `final/S11_v01_contact-sheet.jpg` | First render and its contact sheet |
| `final/S11_v02.mp4` | v02: the stamps held longer (see the decisions log) |
| `project/` | The renderable engine project |
| `project/env.py` | The birds, the coins, the carries; light; the stamp call |
| `project/voices/` | `v1`, `s2`, `v3` (`.wav` and `.tsv`); `raw/` holds the files as received |

## 15. How to re-render

```
cd <path>/S11/project && python3 make_tex_banker.py
python3 engine/toon.py <path>/S11/project lint
python3 engine/toon.py <path>/S11/project final        # about 40 min on 2 cores
```

## Sources for D4

- [Çukurova Üniversitesi İİBF Dergisi: banker krizi makalesi](https://dergipark.org.tr/tr/pub/cuiibfd/article/1385920). From the abstract:
  - "Faiz oranlarının 24 Ocak 1980 kararlarıyla serbest bırakılması bankerlere rahat bir çalışma ortamı sağlamıştı."
  - "yatırımcılara yüksek faiz oranları önerdiler."
  - "Bankerliğin devamı için yeni müşterilerin sisteme girmesi zorunluydu."
- [Alanya Alaaddin Keykubat Üniversitesi: Türkiye Finans Tarihinde Ponzi Dolandırıcılık Sisteminin Erken Örneği: Banker Krizi](https://acikerisim.alanya.edu.tr/items/831b7c2c-08a5-408e-9abf-db8afbd2583c/full). The English abstract says the same.
