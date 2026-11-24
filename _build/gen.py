# -*- coding: utf-8 -*-
"""Generate ../index.html from Figma Frame 28 (node 757:868) coordinates.
All positions are Figma px inside a 1880x5400 stage that JS scales to the viewport.
Run: python -I gen.py"""
import os, html
OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'index.html'))
A = './assets/img/'
P = []
def add(s): P.append(s)
def e(s): return html.escape(s, quote=False)

def rect(x, y, w, h, bg='#000', extra=''):
    add(f'<i class="a" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;background:{bg};{extra}"></i>')

def t(x, y, s, size, b=False, col='#000', tr=None, lh=29, extra='', raw=False):
    tr = round(size * 0.04, 2) if tr is None else tr
    st = f'left:{x}px;top:{y}px;font-size:{size}px;letter-spacing:{tr}px;line-height:{lh}px'
    if col != '#000': st += f';color:{col}'
    add(f'<p class="a t{" b" if b else ""}" style="{st};{extra}">{s if raw else e(s)}</p>')

def ln(x, y, w, h, src, inset, rot=None, iw=None, ih=None):
    """Figma vector placement: outer box, optional centred rotated inner box, img with inset."""
    im = f'<i style="inset:{inset}"><img src="{A}{src}.svg" alt=""></i>'
    if rot is None:
        add(f'<span class="a v" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px">{im}</span>')
    else:
        add(f'<span class="a c" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px">'
            f'<span class="v" style="width:{iw}px;height:{ih}px;transform:{rot}">{im}</span></span>')

def done(gx, gy):
    """Yellow 'completed' marker (Figma groups 757:1268 etc.): box + white tick."""
    add(f'<i class="a ok" style="left:{round(gx + 2.94, 2)}px;top:{round(gy + 2.33, 2)}px"></i>')
    ln(gx, gy, 28.685, 25.278, 'imgGroup606', '0 -18.38% -8.68% 0', 'rotate(5deg)', 26.78, 23.032)

# ---------- backgrounds (z-order follows Figma) ----------
for top, flip in [(1038, True), (2118, False), (3198, True), (4278, False)]:
    add(f'<img class="a bg{" fy" if flip else ""}" src="{A}img213.webp" alt="" style="top:{top}px">')

# ---------- 交互原型 (757:1149) ----------
add('<div class="a proto" style="left:135px;top:2965.91px;width:1611px;height:906px">'
    '<iframe src="https://tiffanyttzheng-code.github.io/jiaohu-yuanxing/" title="主菜单交互原型" loading="lazy"></iframe></div>')
add('<h2 class="a hd" style="left:1487px;top:2898px">&lt; 交互原型 &gt;</h2>')
ln(111, 2942, 108.285, 103.658, 'imgGroup729', '-3.86% 0 0 0')
ln(111.93, 3791.62, 108.285, 103.658, 'imgGroup731', '-3.86% 0 0 0', 'scaleY(-1)', 108.285, 103.658)
ln(1667.71, 3796.25, 108.285, 103.658, 'imgGroup730', '-3.86% 0 0 0', 'rotate(180deg)', 108.285, 103.658)
rect(318, 3895, 1210, 42, 'rgba(255,255,255,.53)', 'border-radius:7px')
LK = 'font-size:24px;letter-spacing:2.4px;line-height:normal;color:#757575'
add(f'<p class="a t" style="left:333px;top:3901px;{LK}">全屏演示链接：</p>')
add(f'<a class="a t lk" style="left:529px;top:3901px;{LK}" href="https://tiffanyttzheng-code.github.io/jiaohu-yuanxing/" target="_blank" rel="noopener">主菜单交互原型</a>')
add(f'<p class="a t" style="left:747px;top:3901px;{LK}">https://tiffanyttzheng-code.github.io/jiaohu-yuanxing/</p>')

# ---------- 实机演示 placeholders ----------
for x, y, h in [(146, 4200, 433), (146, 4778, 432), (974, 4200, 433), (974, 4778, 432)]:
    rect(x, y, 769, h, '#fff', '')
P[-4:] = [s.replace('class="a"', 'class="a demo"') for s in P[-4:]]

# ---------- 系统概述 flowchart (757:1168) ----------
for x, y, w, h, op in [(775, 2138, 320, 52, 1), (398, 2248, 176, 52, 1), (423, 2354, 111, 52, .44),
                       (861, 2595, 149, 52, 1), (1290, 2270, 151, 52, 1)]:
    rect(x, y, w, h, '#000', '' if op == 1 else f'opacity:{op}')
for x, y, s, op in [(893, 2148, '进入游戏', 1), (445, 2258, '剧情系统', 1), (458, 2366, '主线', .44),
                    (896, 2607, '图鉴系统', 1), (1304, 2281, '地图探索系统', 1)]:
    t(x, y, s, 20, True, '#fff', extra='' if op == 1 else f'opacity:{op}')
for x, y, s in [(304, 2256, '剧情解锁'), (1326, 2235, '新地图解锁'), (304, 2356, '解锁条件'), (660, 2342, '解锁条件'),
                (304, 2379, '完成前置章节'), (736, 2342, '完成关联章节'), (355, 2475, '新剧情解锁'),
                (1198, 2359, '地图交互点位调查'), (1198, 2425, '随机出现重要NPC可进行对话')]:
    t(x, y, s, 16)
for x, y, s in [(473, 2496, '奖励'), (438, 2652, '装扮'), (1169, 2359, '①'), (1169, 2425, '②'),
                (862, 2661, '①'), (889, 2661, '联系簿'), (862, 2689, '②'), (889, 2689, '万象站'),
                (862, 2718, '③'), (889, 2718, '作品百科')]:
    t(x, y, s, 16, True)
for x, y, s in [(578, 2588, '剧情出现重要概念进入<图鉴>'), (897, 2562, '收集度'), (1107, 2588, '地图探索获得重要概念进入<图鉴>')]:
    t(x, y, s, 15)
add('<span class="a c" style="left:946px;top:2559px;width:30.322px;height:34.749px">'
    '<b class="t b" style="font-size:15px;letter-spacing:.6px;line-height:29px;transform:rotate(21.96deg)">up</b></span>')
rect(793, 2374, 36, 33, '#fff')
t(661, 2375, '随主线不定期解锁<b>支线</b>', 16, raw=True)
VECS = [  # x, y, w, h, svg, inset, rotate, inner w, inner h
    (939, 2202, 0, 38, 'imgGroup590', '0 0 0 -2px', None, 0, 0),
    (480, 2308, 0, 38, 'imgLine440', '-2px 0 0 0', 'rotate(-90deg)', 38, 0),
    (479, 2413, 0, 69, 'imgLine442', '-1px 0', 'rotate(-90deg)', 69, 0),
    (479, 2532, 0, 146, 'imgLine447', '-1px 0', 'rotate(90deg)', 146, 0),
    (500, 2532, 0, 85, 'imgLine448', '-1px 0', 'rotate(90deg)', 85, 0),
    (501, 2446, 0, 43, 'imgLine445', '-2px 0 0 0', 'rotate(-90deg)', 43, 0),
    (732, 2410, 0, 36, 'imgLine443', '-2px 0 0 0', 'rotate(-90deg)', 36, 0),
    (501, 2446, 231, 0, 'imgLine444', '-2px 0 0 0', 'rotate(180deg)', 231, 0),
    (336, 2508, 126, 0, 'imgLine446', '-2px 0 0 0', None, 0, 0),
    (479, 2457, 0, 34, 'imgArrow43', '-7.36px -2.94% -7.36px 0', 'rotate(90deg)', 34, 0),
    (501, 2616, 350, 0, 'imgArrow48', '-7.36px -0.29% -7.36px 0', None, 0, 0),
    (1023, 2615, 352, 0, 'imgArrow49', '-7.36px -0.28% -7.36px 0', 'rotate(180deg)', 352, 0),
    (478, 2677, 373, 0, 'imgArrow47', '-7.36px -0.27% -7.36px 0', None, 0, 0),
    (500, 2458, 0, 34, 'imgArrow44', '-7.36px -2.94% -7.36px 0', 'rotate(90deg)', 34, 0),
    (551, 2382, 96, 0, 'imgLine441', '-2px 0 0 0', None, 0, 0),
    (337, 2476, 0, 31, 'imgArrow45', '-7.36px -3.23% -7.36px 0', 'rotate(-90deg)', 31, 0),
    (1376, 2474, 0, 141, 'imgLine449', '-2px 0 0 0', 'rotate(-90deg)', 141, 0),
    (478, 2228.99, 895.996, 1.012, 'imgGroup591', '-98.82% 0 0 0', None, 0, 0),
    # map-system notes (757:1237) and 图鉴 brackets
    (1455, 2300, 81, 0, 'imgLine450', '-1px 0 0 0', None, 0, 0),
    (1371, 2377, 99, 0, 'imgLine451', '-1px 0 0 0', None, 0, 0),
    (1425, 2441, 45, 0, 'imgLine453', '-1px 0 0 0', None, 0, 0),
    (196, 2271, 92, 0, 'imgLine454', '-1px 0 0 0', 'rotate(180deg)', 92, 0),
    (945, 2676, 113, 0, 'imgLine459', '-1px 0 0 0', None, 0, 0),
    (945, 2706, 189, 0, 'imgLine464', '-1px 0 0 0', None, 0, 0),
    (962, 2734, 172, 0, 'imgLine465', '-1px 0 0 0', None, 0, 0),
    (1060, 2658, 8, 0, 'imgLine461', '-1px 0 0 0', None, 0, 0),
    (1060, 2695, 8, 0, 'imgLine461', '-1px 0 0 0', None, 0, 0),
    (1059, 2657, 0, 38, 'imgLine460', '-1px 0 0 0', 'rotate(90deg)', 38, 0),
]
for v in VECS:
    ln(*v)
for x, y, s in [(1546, 2283, '共有16条街道'), (1481, 2347, '可获得物品/商品信息'), (1481, 2386, '特殊点位可进行特殊互动'),
                (1481, 2367, '固定NPC可进行互动')]:
    t(x, y, s, 13)
t(1481, 2429, '重要NPC按照设定权重，随机出现在地图上，可进行交互。', 13, lh=21)
for gx, gy in [(1635, 2350), (1634.996, 2383), (46, 2284), (45, 2148), (1138, 2657), (1138.01, 2690), (1138.01, 2723)]:
    done(gx, gy)
for x, y, s in [(1672, 2357, '信息调查&商品调查 已跑通'), (1672, 2339, '四条街道交互点 已整理'), (1672, 2384, '固定NPC互动/对话已接通')]:
    t(x, y, s, 13, col='#373737')
t(48, 2257, '当前共有7章主线剧情', 14)
t(85, 2284, '已完成第零章（16节）AVG', 14, col='#373737')
add(f'<img class="a" src="{A}imgRectangle635.png" alt="" style="left:81px;top:2153px;width:171px;height:21px">')
t(85, 2149, '此标志为当前版本已完成', 14)
t(1075, 2643, '角色信息', 10)
for y, s in [(2658, '共88个有骨骼重要角色，已置入角色信息和换装功能。'), (2692, '四个类目下共128个条目'), (2724, '八个类目下共347个条目')]:
    t(1178, y, s, 14, col='#373737')
rect(1070, 2682, 62, 17)
t(1075, 2676, '换装系统', 13, True, '#fff')

# ---------- 首屏 hero (757:1317) — card 34,39 1814x960 r12; children in card coords ----------
add('<section class="a card" style="left:34px;top:39px;width:1814px;height:960px" aria-label="自负 · 叙事向RPG游戏">'
    f'<img class="a" src="{A}img213.webp" alt="" style="left:-36px;top:-11.44px;width:1885.997px;height:1060.873px;object-fit:cover">'
    f'<img class="a tiles" src="{A}hero-tiles.svg" alt="" style="left:0;top:0;width:1814px;height:960px">'
    f'<img class="a" src="{A}img144.webp" alt="自负 主要角色立绘" style="left:317.71px;top:54px;width:1495.923px;height:905.735px;object-fit:cover">'
    '<h1 class="a xh sticker" style="left:104.56px;top:350px;font-size:36px">叙事向RPG游戏</h1>'
    + ''.join(f'<p class="a tag" style="left:{x - 34}px;top:404px">&lt;{s}&gt;</p>'
              for x, s in [(125, '叙事'), (212, '探索'), (299, '收集')]) +
    '</section>')
add('<div class="a" style="left:34px;top:39px;width:428px;height:350px;overflow:hidden">'
    f'<img src="{A}img151.webp" alt="自负 ARROGISM" style="position:absolute;left:-73.28%;top:-34.42%;width:254.56%;height:174.95%;max-width:none"></div>')
ln(-64, -62, 249.418, 235.622, 'imgPolygon42', '0 6.7% 25% 6.7%', 'rotate(-37.06deg)', 208.456, 137.839)
add('<h2 class="a hd" style="left:1484px;top:4084px">&lt; 实机演示 &gt;</h2>')
rect(0, 999, 34, 4401)
rect(1846, 999, 34, 4401)
rect(0, 999, 1880, 39)

# ---------- 第二页 tabs (757:1426 / 767:1738): 项目概述 / 故事线 / IP特色 / 核心概念 ----------
OV = [
    '<b>定位：</b>本作品是一款以叙事为核心的<b class="hl">角色扮演</b>游戏。玩家将扮演主角“吴向寓”，在“宙际”这个充满幻想科技的地方，跟随剧情的推进与探索区域的扩张， 而成长、发现、感悟。',
    '<b>背景设定</b>：游戏采用原创架空世界观，由人与神在内的多种族共同构成。世界体系复杂，多价值观并存。希望给玩家们呈现一个带有成人童话质感般的沉重却温柔的世界。',
    '<b>游戏基调</b>：黑色童话风格，温馨与沉重并存的游戏氛围，呈现人们对于幸福、归属与个人信念的不同理解。',
]
def slice_(x, y, w, h, name, alt=''):
    return f'<img class="a" src="{A}p2-{name}.webp" alt="{alt}" loading="lazy" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px">'
BOX = '<i class="a pbox" style="left:117px;top:1208px;width:1637px;height:830px"></i>'
def bar(x, y, w, h):
    return f'<i class="a" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;background:#afada8"></i>'
PANELS = {
    'overview': ''.join(f'<p class="a para" style="left:142px;top:{y}px;width:619px">{s}</p>' for y, s in zip((1384, 1526, 1667), OV))
        + f'<img class="a ovimg" src="{A}p2-ov.webp" alt="项目概述插画：黑费露" style="left:896px;top:1113px;width:949.609px;height:942.992px;object-fit:cover">',
    'story': BOX
        + slice_(181.54, 1236.53, 676.174, 236.903, 'story-1', '蓝线（原笔头线）：吴向寓、有德元、非显色')
        + slice_(181.54, 1482.95, 676.174, 247.617, 'story-2', '紫线（市政厅线）：吴静、林锡斌、高知盈')
        + slice_(181.54, 1724.62, 666.651, 261.903, 'story-3', '黑线（混沌线）：王、谏立克')
        + bar(1046.23, 1300.88, 8, 597.78) + bar(962.4, 1294, 89.34, 8)
        + bar(962.4, 1596.87, 270.21, 8) + bar(962.4, 1894.66, 83.82, 8)
        + slice_(1288.86, 1190.59, 358.325, 849.996, 'story-4', '三线收束与核心：黑费露'),
    'ip': BOX
        + slice_(233, 1222, 1211, 523, 'ip-1', 'IP特色：追更制IP、解谜')
        + slice_(233, 1706, 1211, 271, 'ip-2', 'IP特色：社会关怀与真实叙事'),
    'core': BOX
        + slice_(175, 1195, 1359, 226, 'core-1', '核心概念：幸福理论')
        + slice_(175, 1421, 1359, 229, 'core-2', '核心概念：救世主罪犯')
        + slice_(175, 1650, 1359, 386, 'core-3', '核心概念：钟庭科技'),
}
TABS = [('overview', '项目概述'), ('story', '故事线'), ('core', '核心概念'), ('ip', 'IP特色')]
add('<section class="a p2" id="overview" data-tabs aria-label="项目概述">')
for i, (k, _) in enumerate(TABS):
    on = i == 0
    add(f'<div class="pn{" is-on" if on else ""}" id="pn-{k}" role="tabpanel" aria-labelledby="tb-{k}" data-panel="{k}"{"" if on else " hidden"}>{PANELS[k]}</div>')
add('<div class="a tabs" role="tablist" aria-label="项目概述切换" style="left:66px;top:1089px">')
for i, (k, label) in enumerate(TABS):
    on = i == 0
    add(f'<button class="tab{" is-on" if on else ""}" type="button" role="tab" id="tb-{k}" aria-controls="pn-{k}" '
        f'aria-selected="{"true" if on else "false"}" tabindex="{0 if on else -1}" data-tab="{k}">'
        f'<img class="tab__big" src="{A}imgRectangle627.png" alt="">'
        f'<span class="tab__small"><img src="{A}p2-paper-s.png" alt=""></span>'
        f'<span class="tab__icon"><span class="v" style="left:39px;top:0;width:39.628px;height:70.653px"><i style="inset:0 -5.05% -2.83% 0"><img src="{A}imgGroup580.svg" alt=""></i></span>'
        f'<span class="c" style="left:0;top:3px;width:50.748px;height:63.869px"><span class="v" style="width:38.728px;height:56.433px;transform:rotate(13.4deg)"><i style="inset:0 -2.59% -3.54% 0"><img src="{A}imgGroup579.svg" alt=""></i></span></span></span>'
        f'<span class="tab__label">{label}</span>'
        + ('' if on else '<i class="tab__dot" aria-hidden="true"></i>') + '</button>')
add('</div></section>')

# ---------- write page ----------
TPL = open(os.path.join(os.path.dirname(__file__), 'tpl.html'), encoding='utf-8').read()
open(OUT, 'w', encoding='utf-8').write(TPL.replace('<!--STAGE-->', '\n'.join(P)))
print('wrote', OUT, len(P), 'nodes')
