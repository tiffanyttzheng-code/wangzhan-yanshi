# -*- coding: utf-8 -*-
"""Crop the 第二页 tab panels out of the Figma source images (in _build/tabs) into ../assets/img/p2-*.webp."""
import os
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, 'tabs')
OUT = os.path.join(HERE, '..', 'assets', 'img')
# name, source, box w,h, img width%, height%, left%, top%  (from Figma get_design_context)
SL = [
    ('core-1', 'src_core.png', 1359, 226, 100, 516.77, 0, -88.38),
    ('core-2', 'src_core.png', 1359, 229, 100, 510.2, 0, -206.32),
    ('core-3', 'src_core.png', 1359, 386, 100, 303.29, 0, -197.21),
    ('ip-1', 'src_ip.png', 1211, 523, 100.1, 199.71, -0.05, -32.87),
    ('ip-2', 'src_ip.png', 1211, 271, 100.1, 385.42, -0.05, -256.43),
    ('story-1', 'src_story.png', 676.174, 236.903, 169.86, 417.34, -0.25, -58.55),
    ('story-2', 'src_story.png', 676.174, 247.617, 169.86, 399.28, -0.25, -186.3),
    ('story-3', 'src_story.png', 666.651, 261.903, 172.29, 377.5, -0.25, -277.5),
    ('story-4', 'src_story.png', 358.325, 849.996, 320.53, 116.32, -220.07, -16.32),
]
for name, src, w, h, W, H, L, T in SL:
    im = Image.open(os.path.join(SRC, src))
    sx = im.width / (w * W / 100); sy = im.height / (h * H / 100)
    x0 = -w * L / 100 * sx; y0 = -h * T / 100 * sy
    box = tuple(round(v) for v in (x0, y0, x0 + w * sx, y0 + h * sy))
    c = im.crop(box).resize((round(w * 2), round(h * 2)), Image.LANCZOS)
    c.save(os.path.join(OUT, f'p2-{name}.webp'), quality=88, method=6)
    print(name, box, c.size)
ov = Image.open(os.path.join(SRC, 'src_ov.png'))
ov.resize((1900, 1886), Image.LANCZOS).save(os.path.join(OUT, 'p2-ov.webp'), quality=86, method=6)
Image.open(os.path.join(SRC, 'src_paper_s.png')).save(os.path.join(OUT, 'p2-paper-s.png'), optimize=True)
