"""One-off asset prep for arrogism-new.html (Figma Frame 28).
Run: python -I build_assets.py  (from _build)"""
import os, re
from PIL import Image
from fontTools import subset
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
A = os.path.join(ROOT, 'assets', 'img')
FONTS = os.path.join(ROOT, 'assets', 'fonts')
REF = os.path.dirname(os.path.abspath(__file__))


def sub(src, dst, text, pre=None):
    f = TTFont(src)
    if pre:
        f = pre(f)
    o = subset.Options(); o.flavor = 'woff2'; o.layout_features = ['*']
    s = subset.Subsetter(o); s.populate(text=text); s.subset(f)
    f.flavor = 'woff2'; f.save(dst)
    print(dst, os.path.getsize(dst))


# 1) heading font: No.128 上首玄黑体
sub(os.path.join(os.environ['LOCALAPPDATA'], 'Microsoft', 'Windows', 'Fonts', 'No.128-上首玄黑体.ttf'),
    os.path.join(FONTS, 'xuanhei-f28.woff2'), '叙事向RPG游戏项目概述故事线IP特色核心概念交互原型实机演示<> ')
# 2) tag font: Noto Sans SC Bold (pinned from the variable font)
sub(r'C:\Windows\Fonts\NotoSansSC-VF.ttf', os.path.join(FONTS, 'notosc-bold-f28.woff2'), '<>叙事探索收集',
    pre=lambda f: instancer.instantiateVariableFont(f, {'wght': 700}))

# 3) raster -> webp at ~2x display size
for name, w in [('img213', 1920), ('img144', 2992), ('img143', 1722), ('img151', 2180), ('img88', 173)]:
    im = Image.open(os.path.join(A, name + '.png'))
    if im.width > w:
        im = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
    out = os.path.join(A, name + '.webp')
    im.save(out, 'WEBP', quality=88, method=6)
    print(out, im.size, os.path.getsize(out))

# 4) hero tiles: rebuild the two Figma tile groups (plain rects) in hero-card coordinates
rects = []
for fn, dy in [('tiles-dark.svg', 360 - 39), ('tiles-light.svg', 678 - 39)]:
    svg = open(os.path.join(REF, 'vec', fn), encoding='utf-8').read()
    body = re.findall(r'<rect id="Rectangle [^>]*/>', svg)
    rects.append(f'<g transform="translate(-34 {dy})">' + ''.join(body) + '</g>')
    print(fn, len(body), 'rects')
with open(os.path.join(A, 'hero-tiles.svg'), 'w', encoding='utf-8') as f:
    f.write('<svg xmlns="http://www.w3.org/2000/svg" width="1814" height="960" viewBox="0 0 1814 960" fill="none">'
            + ''.join(rects) + '</svg>')
