# Project skeleton

A working 6-second scene with stand-in characters and painted-by-code textures. Copy it with `toon.py <path> new`, see it run, then replace one file at a time:

| File | What it decides | Skill |
|---|---|---|
| `config.py` | size, ground, air, light, grade | toon-set, toon-finish |
| `cast.py` | who: designs as spec dictionaries | toon-rig |
| `setdef.py` | where: the 3D set, in Blender | toon-set |
| `shots.py` | how it's seen: the camera plan | toon-direct |
| `acting.py` | what they do: blocking and acting keys | toon-direct |
| `env.py` | what else lives there | toon-set |
| `sound.py` | what's heard | toon-finish |
| `tex/`, `voices/` | painted textures, voice files and timing | toon-scene, toon-finish |
