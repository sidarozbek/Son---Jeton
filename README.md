# Son Jeton · Production folder

An animated comedy series of 24 scenes, made with Toon Studio. This folder holds everything that belongs to the production: series canon, one folder per scene, every render and the files to re-make them.

## Layout

```
Son-Jeton/
├── README.md                  This file: layout, naming, how to work
├── 00_Series/
│   ├── BIBLE.md               Style Lock and character cards (series canon)
│   ├── SCENE-INDEX.md         All 24 scenes: title, location, cast, runtime, status
│   └── SCENE-TEMPLATE.md      The empty scene document every scene starts from
├── S01/                       One folder per scene, S01 to S24
│   ├── S01_SCENE.md           The master document: everything about the scene
│   ├── S01_BRIEF.md           The approved brief
│   ├── final/                 Rendered versions and contact sheets
│   ├── project/               The renderable engine project (code, voices, textures)
│   ├── review/                Test frames, animatic, checks
│   └── archive/               Superseded files, kept, never deleted
├── S02/
│   └── S02_SCENE.md
└── … to S24/
```

Scenes start with only their `Sxx_SCENE.md`. The other subfolders are added as the work produces them.

## Naming

| Kind | Pattern | Example |
|---|---|---|
| Scene folder | `Sxx` (two digits) | `S07` |
| Scene document | `Sxx_SCENE.md` | `S07_SCENE.md` |
| Brief | `Sxx_BRIEF.md` | `S07_BRIEF.md` |
| Render | `Sxx_vNN_<short-note>.mp4` | `S01_v03_voiced.mp4` |
| Contact sheet | `Sxx_vNN_contact-sheet.jpg` | `S01_v03_contact-sheet.jpg` |
| Animatic | `Sxx_animatic.mp4` | `S01_animatic.mp4` |
| Voice line | `<speaker><line>.wav`, with lip timing in a `.tsv` of the same name | `s1.wav` and `s1.tsv` (Sidar, line 1); `v2.wav` (Vehbi, line 2) |
| Raw voice delivery | `project/voices/raw/` | as received |

- **Versions:** Numbers only go up. Old versions are never overwritten or deleted; they stay in `final/`, and the scene document says which version is current.
- **Text conventions:** Documents and code are in English. Spoken lines keep their Turkish original beside them in the dialogue table. Times are in scene seconds with two decimals; the engine runs at 24 fps.

## The scene document

Every `Sxx_SCENE.md` has the same 15 sections in the same order, so any two scenes can be compared line for line:

1. Logline
2. Purpose
3. Synopsis
4. Beat sheet
5. Dialogue
6. Characters in this scene
7. Location and set
8. Shot list
9. Timed events
10. Sound
11. Production status
12. Known weak points and next steps
13. Decisions log
14. Files
15. How to re-render

- **Unknowns:** Anything not yet decided is written `[TBD]`, never guessed.
- **Decisions:** Every decision the person makes goes into the decisions log with its date.

## Series rules (from the person; they hold until changed)

- Everything free; the work is non-commercial.
- Exploring length is about 20 s per scene, and a scene may run longer if it needs to.
- Every character has four fingers and no thumb.
- Sidar and Vehbi are the same height; their looks follow the person's reference photos.
- Voices are cloned only from people who consented, and the two leads sound clearly different. No real public figure is cloned.
- Originality: nothing from existing shows (characters, designs, gadgets, premises).
- Every delivery names its weak points and the next step.

## Status

See `00_Series/SCENE-INDEX.md`.
