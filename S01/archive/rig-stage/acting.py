"""Turnaround: both stand side by side facing +x, idle. Sidar on the left of frame from the front, Vehbi on the right."""

# Sidar's own default face: brows down, lids low, a glare. Use it wherever he is at rest.
SIDAR_REST = dict(lid=.28, brow=-.25)

POS = dict(sidar=(0.0, 3.65), vehbi=(0.0, 2.75))


SIDAR_FACES_VEHBI = [('rest', 'unimpressed'), ('angry', 'one_brow'), ('determined', 'correcting'), ('smug', 'smug'),
                     ('grimace', 'doubt'), ('collapse', 'realizing'), ('forced_smile', 'panic'), ('panic', 'collapse')]


def root(name, t):
    return POS[name]


def direct(cast, cfg):
    s, v = cast['sidar'], cast['vehbi']
    s.face(0, .01, 'angry')
    s.face(4.0, .2, 'rest', **SIDAR_REST)
    v.face(0, .01, 'unimpressed')
    # Expression test. Limits must hold: Sidar never sheepish, Vehbi never panicked.
    for i, (fs, fv) in enumerate(SIDAR_FACES_VEHBI):
        s.face(6 + i * .5, .12, fs, **(SIDAR_REST if fs == 'rest' else {}))
        v.face(6 + i * .5, .12, fv)
    # Speech test with placeholder timing (tools/fake_cues.py).
    v.face(10, .1, 'unimpressed')
    s.face(10, .1, 'rest', **SIDAR_REST)
    v.line(10.2, 'voices/test_vehbi.tsv', 'clause seven')
    s.line(12.6, 'voices/test_sidar.tsv', 'giving notice')
    s.face(12.5, .1, 'angry')
    for pup, seed in ((s, 1), (v, 2)):
        pup.auto_blink(seed, cfg.END)
