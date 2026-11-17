#!/usr/bin/env python3
"""Son Jeton, scene 1: every line in both cloned voices with Qwen3-TTS 0.6B Base, three takes each.

Needs, next to this file:
  refs/sidar.wav + refs/sidar.txt   10-15 s of the consenting Sidar voice, clean, spoken in character; .txt = exact words
  refs/vehbi.wav + refs/vehbi.txt   the same for Vehbi
Install:  pip install -U qwen-tts soundfile numpy
Run:      python3 gen_voices.py            (writes s1_take1.wav ... v4_take3.wav here)
Then pick the best take of each line and rename it s1.wav, v2.wav, s3.wav, v4.wav, s5.wav.

The 0.6B model has no style instruction: the delivery follows the reference clip's tone and the punctuation."""
import os
import sys

import numpy as np
import soundfile as sf
import torch
from qwen_tts import Qwen3TTSModel

HERE = os.path.dirname(os.path.abspath(__file__))
MODEL = "Qwen/Qwen3-TTS-12Hz-0.6B-Base"
TAKES = 3

LINES = {
    "sidar": [("s1", "Vehbi! ... Rent!"),
              ("s3", "I'm giving notice!"),
              ("s5", "I'm here.")],
    "vehbi": [("v2", "Clause seven: the landlord gives notice... before coming at night."),
              ("v4", "In writing.")],
}

if torch.cuda.is_available():
    dev, dt = "cuda:0", torch.bfloat16
elif torch.backends.mps.is_available():
    dev, dt = "mps", torch.float32
else:
    dev, dt = "cpu", torch.float32
print("device:", dev)
model = Qwen3TTSModel.from_pretrained(MODEL, device_map=dev, dtype=dt, attn_implementation="sdpa")


def reference(name):
    wav, sr = sf.read(os.path.join(HERE, "refs", name + ".wav"), dtype="float32")
    if wav.ndim > 1:
        wav = wav.mean(axis=1)
    wav = np.concatenate([wav, np.zeros(int(sr * .5), np.float32)])   # Half a second of tail: less bleed into the first word.
    text = open(os.path.join(HERE, "refs", name + ".txt"), encoding="utf-8").read().strip()
    return model.create_voice_clone_prompt(ref_audio=(wav, sr), ref_text=text, x_vector_only_mode=False)


for who, lines in LINES.items():
    if not os.path.exists(os.path.join(HERE, "refs", who + ".wav")):
        sys.exit(f"missing refs/{who}.wav and refs/{who}.txt")
    prompt = reference(who)
    for key, text in lines:
        for k in range(1, TAKES + 1):
            torch.manual_seed(100 * k + len(key))
            wavs, sr = model.generate_voice_clone(text=text, language="English", voice_clone_prompt=prompt)
            out = os.path.join(HERE, f"{key}_take{k}.wav")
            sf.write(out, wavs[0], sr)
            print(out, f"{len(wavs[0]) / sr:.2f}s")
