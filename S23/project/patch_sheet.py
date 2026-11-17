"""Redraw S23's exam-sheet inserts (env.sheet) into an existing render, keeping every other frame and the sound.
usage: python3 patch_sheet.py <project> <src.mp4> <dst.mp4> [check]"""
import sys, subprocess, numpy as np
proj, src, dst = sys.argv[1:4]
check = len(sys.argv) > 4
sys.path.insert(0, '/home/claude/toon-studio/Toon-Studio/engine'); sys.path.insert(0, proj)
import os; os.chdir(proj)
import room as R, env as E
ev = E.Env.__new__(E.Env); ev._sheet = {}
W, H, FPS = 1280, 720, 24
n = int(subprocess.run(['ffprobe', '-v', 'error', '-count_frames', '-select_streams', 'v', '-show_entries', 'stream=nb_read_frames', '-of', 'csv=p=0', src], capture_output=True, text=True).stdout)
dec = subprocess.Popen(['ffmpeg', '-v', 'error', '-i', src, '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], stdout=subprocess.PIPE)
if not check:
    enc = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                            '-i', src, '-map', '0:v', '-map', '1:a', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p',
                            '-c:a', 'copy', dst], stdin=subprocess.PIPE)
diffs, changed = [], 0
for i in range(n):
    f = np.frombuffer(dec.stdout.read(W * H * 3), np.uint8).reshape(H, W, 3)
    t = i / FPS
    for k, (a, b) in enumerate(R.Q):
        if a <= t < b:
            new = np.clip(ev.sheet(W, H, k, t), 0, 255).astype(np.uint8)
            if check:
                diffs.append(np.abs(new.astype(int) - f.astype(int)).mean())
            f = new; changed += 1
            break
    if not check:
        enc.stdin.write(f.tobytes())
if not check:
    enc.stdin.close(); enc.wait()
print('frames', n, 'replaced', changed, 'mean abs diff vs source' if check else '', np.round(np.mean(diffs), 2) if diffs else '')
