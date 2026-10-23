#!/usr/bin/env python3
"""全部案例 · 画廊总库：分类首页 + 卡片网格 + 点击预览全屏演示 + 一键复制"""
import os, html, base64, io
from PIL import Image

HOME = os.path.expanduser('~')
SHOT_DIR = os.path.join(HOME, 'workspace/preview-shots/master')
OUT = os.path.join(HOME, 'workspace/your_files/全部案例-画廊总库.html')

PARTS = [
 ("UI 组件库 · 第一批", "21 套 · 从 CSS 案例扩展的整套组件库", [
   ("workspace/star-ui-kit/star-ui.html", "STAR 星芒"),
   ("workspace/gloss-ui-kit/gloss-ui.html", "GLOSS 柔光"),
   ("workspace/neu-ui-kit/neu-ui.html", "NEU 柔影"),
   ("workspace/glass-ui-kit/glass-ui.html", "GLASS 雾面"),
   ("workspace/jelly-ui-kit/jelly-ui.html", "JELLY 果冻"),
   ("workspace/doodle-ui-kit/doodle-ui.html", "DOODLE 手绘"),
   ("workspace/share-ui-kit/share-ui.html", "SHARE 分享"),
   ("workspace/washi-ui-kit/washi-ui.html", "WASHI 和纸"),
   ("workspace/lever-ui-kit/lever-ui.html", "LEVER 拨杆"),
   ("workspace/tilt-ui-kit/tilt-ui.html", "TILT 3D 倾斜"),
   ("workspace/beat-ui-kit/beat-ui.html", "BEAT 律动"),
   ("workspace/pixel-ui-kit/pixel-ui.html", "PIXEL 像素"),
   ("workspace/neon-ui-kit/neon-ui.html", "NEON 霓虹"),
   ("workspace/gold-ui-kit/gold-ui.html", "GOLD 轻奢金"),
   ("workspace/ink-ui-kit/ink-ui.html", "INK 水墨"),
   ("workspace/candy-ui-kit/candy-ui.html", "CANDY 糖果"),
   ("workspace/cyber-ui-kit/cyber-ui.html", "CYBER 赛博"),
   ("workspace/forest-ui-kit/forest-ui.html", "FOREST 森林"),
   ("workspace/sunset-ui-kit/sunset-ui.html", "SUNSET 日落"),
   ("workspace/clay-ui-kit/clay-ui.html", "CLAY 黏土"),
   ("workspace/mono-ui-kit/mono-ui.html", "MONO 极简黑白"),
 ]),
 ("UI 组件库 · 20 套风格", "20 套 · APP设计Skill 风格全套", [
   ("workspace/skill-ui-kits/s01-clay.html", "S01 黏土可爱"),
   ("workspace/skill-ui-kits/s02-guochao.html", "S02 国潮"),
   ("workspace/skill-ui-kits/s03-neon.html", "S03 霓虹"),
   ("workspace/skill-ui-kits/s04-cream.html", "S04 奶油"),
   ("workspace/skill-ui-kits/s05-hkretro.html", "S05 复古港风"),
   ("workspace/skill-ui-kits/s06-neu.html", "S06 新拟态"),
   ("workspace/skill-ui-kits/s07-doodle.html", "S07 手绘"),
   ("workspace/skill-ui-kits/s08-bento.html", "S08 Bento 格栅"),
   ("workspace/skill-ui-kits/s09-glass.html", "S09 液态玻璃"),
   ("workspace/skill-ui-kits/s10-brutal.html", "S10 新丑风"),
   ("workspace/skill-ui-kits/s11-aero.html", "S11 千禧复兴"),
   ("workspace/skill-ui-kits/s12-dopamine.html", "S12 多巴胺"),
   ("workspace/skill-ui-kits/s13-swiss.html", "S13 瑞士大字报"),
   ("workspace/skill-ui-kits/s14-flat.html", "S14 扁平插画"),
   ("workspace/skill-ui-kits/s15-anime.html", "S15 二次元"),
   ("workspace/skill-ui-kits/s16-aurora.html", "S16 弥散渐变"),
   ("workspace/skill-ui-kits/s17-street.html", "S17 暗黑街头"),
   ("workspace/skill-ui-kits/s18-morandi.html", "S18 莫兰迪"),
   ("workspace/skill-ui-kits/s19-medical.html", "S19 轻医疗"),
   ("workspace/skill-ui-kits/s20-voucher.html", "S20 复古票据"),
 ]),
 ("更新弹窗 · 10 款风格", "10 款 · 安装 / 更新弹窗", [
   ("workspace/update-modals/m01-glass.html", "01 液态玻璃"),
   ("workspace/update-modals/m02-neon.html", "02 暗黑霓虹"),
   ("workspace/update-modals/m03-clay.html", "03 黏土可爱"),
   ("workspace/update-modals/m04-mono.html", "04 极简线条"),
   ("workspace/update-modals/m05-pixel.html", "05 像素复古"),
   ("workspace/update-modals/m06-guochao.html", "06 国潮风"),
   ("workspace/update-modals/m07-cyber.html", "07 赛博 HUD"),
   ("workspace/update-modals/m08-candy.html", "08 糖果马卡龙"),
   ("workspace/update-modals/m09-gold.html", "09 轻奢黑金"),
   ("workspace/update-modals/m10-doodle.html", "10 手绘涂鸦"),
 ]),
 ("更新交互 · 10 组新概念", "10 组 · 没见过的更新交互", [
   ("workspace/update-modals/m11-cube.html", "11 魔方复原"),
   ("workspace/update-modals/m12-rocket.html", "12 火箭发射"),
   ("workspace/update-modals/m13-zipper.html", "13 拉链拉合"),
   ("workspace/update-modals/m14-lock.html", "14 开锁"),
   ("workspace/update-modals/m15-ecg.html", "15 心电苏醒"),
   ("workspace/update-modals/m16-calligraphy.html", "16 书法书写"),
   ("workspace/update-modals/m17-jigsaw.html", "17 拼图拼合"),
   ("workspace/update-modals/m18-moon.html", "18 月相"),
   ("workspace/update-modals/m19-bloom.html", "19 花朵绽放"),
   ("workspace/update-modals/m20-domino.html", "20 多米诺"),
 ]),
 ("更新交互 · 第二批", "10 组 · 更新交互新概念", [
   ("workspace/update-modals/m21-paperplane.html", "21 纸飞机"),
   ("workspace/update-modals/m22-egg.html", "22 破壳孵化"),
   ("workspace/update-modals/m23-fingerprint.html", "23 指纹解锁"),
   ("workspace/update-modals/m24-sprout.html", "24 破土而出"),
   ("workspace/update-modals/m25-hourglass.html", "25 沙漏"),
   ("workspace/update-modals/m26-weaving.html", "26 织布机"),
   ("workspace/update-modals/m27-icebreak.html", "27 破冰"),
   ("workspace/update-modals/m28-kaleidoscope.html", "28 万花筒"),
   ("workspace/update-modals/m29-balloon.html", "29 热气球"),
   ("workspace/update-modals/m30-abacus.html", "30 算盘"),
 ]),
]

EXTRA_CATS = [
 ("组件 · 加载动画", "20 组 · 各不相同的加载动效", "L", "workspace/components/loaders"),
 ("组件 · 按钮特效", "20 组 · 点击触发的按钮动效", "B", "workspace/components/buttons"),
 ("组件 · 开关切换", "20 组 · 各不相同的开关概念", "T", "workspace/components/toggles"),
 ("组件 · 进度指示", "20 组 · 0→100 的进度演绎", "P", "workspace/components/progress"),
 ("组件 · 通知提醒", "20 组 · 各不相同的 Toast 通知", "N", "workspace/components/toasts"),
 ("APP · 功能模块全套", "10 套 · 账户/内容/交易/通知等模块设计", "M", "workspace/app-designs/modules"),
 ("APP · 产品方向全套", "16 套 · 16 个产品方向完整 App", "V", "workspace/app-designs/verticals"),
 ("APP · 电商细分全套", "12 套 · 12 种电商形态完整 App", "E", "workspace/app-designs/ecommerce"),
 ("玩机 · Xposed 模块", "Xposed 框架模块", "X", "workspace/_removed"),
 ("组件 · 底部Tab栏", "22 款 · 各不相同的底部 Tab 栏", "D", "workspace/tab-bars"),
 ("新鲜 · 启动页", "36 组 · 各不相同的 App 启动页", "S", "workspace/fresh-ui/splash"),
 ("新鲜 · 顶部栏", "36 组 · 各不相同的顶部导航栏", "H", "workspace/fresh-ui/topbar"),
 ("新鲜 · 底部栏", "36 组 · 各不相同的新鲜底部导航", "F", "workspace/fresh-ui/bottombar"),
 ("新鲜 · 欢迎弹窗", "36 组 · 各不相同的欢迎弹窗", "W", "workspace/fresh-ui/welcome"),
 ("新鲜 · 更新弹窗", "36 组 · 各不相同的新鲜更新弹窗", "U", "workspace/fresh-ui/update"),
 ("新鲜 · App界面", "36 组 · 各不相同的 App 界面", "A", "workspace/fresh-ui/appscreen"),
 ("液态 · UI主题", "10 套 · 液态全套组件库", "Q", "workspace/liquid-ui-kits"),
 ("液态 · 页签卡片", "8 组 · 页签卡片分组", "R", "workspace/liquid-tab-cards"),
 ("液态 · Tab栏", "100 款 · 液态玻璃底部栏", "Z", "workspace/liquid-tab-bars"),
 ("液态 · 通知卡", "100 款 · 液态玻璃通知卡", "Y", "workspace/liquid-notify-cards"),
 ("液态 · App套装", "12 套 · 液态玻璃整套 App 界面", "G", "workspace/liquid-glass-apps"),
]
EXTRA_SHOT_DIR = os.path.join(HOME, 'workspace/preview-shots/components')

def load_extra():
    import json, glob
    parts = []
    for cname, cdesc, code, d in EXTRA_CATS:
        raw = []
        mf = os.path.join(HOME, d, 'manifest.json')
        if os.path.exists(mf):
            raw += json.load(open(mf, encoding='utf-8'))
        for tf in sorted(glob.glob(os.path.join(HOME, d, '_titles_*.json'))):
            raw += json.load(open(tf, encoding='utf-8'))
        seen, ks = set(), []
        for e in raw:
            if e['file'] in seen:
                continue
            seen.add(e['file'])
            rel = d + '/' + e['file']
            if os.path.exists(os.path.join(HOME, rel)):
                ks.append((rel, e['title']))
        ks = [(rel, f"{code}{i+1:02d} " + t) for i, (rel, t) in enumerate(ks)]
        # 空分类也占位，保证 cat 编号与 EXTRA_CATS 顺序稳定（如下架的玩机 Xposed）
        parts.append((cname, cdesc, ks))
    return parts

def extra_shot_path(rel):
    return os.path.join(EXTRA_SHOT_DIR, rel.replace('/', '_') + '.png')

CHROME = '/home/hatch/.cache/ms-playwright/chromium_headless_shell-1243/chrome-headless-shell-linux64/chrome-headless-shell'
def take_extra_shot(rel):
    import subprocess
    out = extra_shot_path(rel)
    if os.path.exists(out):
        return out
    os.makedirs(EXTRA_SHOT_DIR, exist_ok=True)
    src = os.path.join(HOME, rel)
    subprocess.run([CHROME, '--no-sandbox', '--disable-gpu', '--window-size=430,900',
                    '--virtual-time-budget=6000', f'--screenshot={out}', f'file://{src}'],
                   capture_output=True, timeout=90)
    return out

def shot_file(rel):
    return os.path.join(SHOT_DIR, rel.replace('/', '_') + '.png')

def thumb_b64(png, w=360):
    im = Image.open(png).convert('RGB')
    r = w / im.width
    im = im.resize((w, int(im.height * r)), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, 'JPEG', quality=66)
    return base64.b64encode(buf.getvalue()).decode()

# ---- 数据 ----
ALL_PARTS = list(PARTS) + load_extra()
for _cname, _cdesc, _ks in ALL_PARTS[len(PARTS):]:
    from concurrent.futures import ThreadPoolExecutor
    _rels = [r for r, _ in _ks]
    print('extra shots:', _cname, len(_rels))
    list(ThreadPoolExecutor(max_workers=6).map(take_extra_shot, _rels))
    for _r in _rels:
        import shutil
        _dst = os.path.join(SHOT_DIR, _r.replace('/', '_') + '.png')
        _src = extra_shot_path(_r)
        if os.path.exists(_src) and not os.path.exists(_dst):
            shutil.copy(_src, _dst)
NEW_TITLES = set()
NEW_CATS = {25}
NEW_LABEL = "液态App套装 12"
def is_new(t):
    return any(t == nt or t.endswith(' ' + nt) for nt in NEW_TITLES)
items = []   # {id, cat, title, code, thumb}
n = 0
for ci, (cname, cdesc, ks) in enumerate(ALL_PARTS):
    for rel, title in ks:
        n += 1
        code = open(os.path.join(HOME, rel), encoding='utf-8').read()
        items.append({'id': n, 'cat': ci, 'title': title,
                      'code': code, 'thumb': thumb_b64(shot_file(rel))})
print('items:', n)


# ---- HTML ----
CSS = '''
*{margin:0;padding:0;box-sizing:border-box}
body{background:#05070e;color:#eef1f8;font-family:-apple-system,"PingFang SC","Microsoft YaHei",sans-serif;min-height:100vh;overflow-x:hidden}
a{color:inherit}
.bg{position:fixed;inset:0;z-index:-1;overflow:hidden;background:#05070e}
.bg i{position:absolute;border-radius:50%;filter:blur(90px);opacity:.55;animation:drift 18s ease-in-out infinite alternate}
.bg i:nth-child(1){width:55vw;height:55vw;left:-12vw;top:-14vw;background:radial-gradient(circle,rgba(30,90,255,.4),transparent 70%)}
.bg i:nth-child(2){width:48vw;height:48vw;right:-10vw;top:22vh;background:radial-gradient(circle,rgba(168,85,247,.4),transparent 70%);animation-delay:-6s}
.bg i:nth-child(3){width:60vw;height:60vw;left:20vw;bottom:-24vw;background:radial-gradient(circle,rgba(14,165,233,.4),transparent 70%);animation-delay:-12s}
@keyframes drift{to{transform:translate(6vw,4vh) scale(1.15)}}
.top{position:sticky;top:0;z-index:40;background:rgba(10,15,26,.55);backdrop-filter:blur(22px) saturate(1.6);-webkit-backdrop-filter:blur(22px) saturate(1.6);border-bottom:1px solid rgba(255,255,255,.09);box-shadow:inset 0 1px 0 rgba(255,255,255,.12)}
.top-in{max-width:1280px;margin:0 auto;padding:12px 18px;display:flex;align-items:center;gap:14px;flex-wrap:wrap}
.logo{font-size:17px;font-weight:800;letter-spacing:1px;cursor:pointer}
.logo b{background:linear-gradient(120deg,#6ee7ff,#a78bfa,#f9a8d4);-webkit-background-clip:text;background-clip:text;color:transparent}
.tabs{display:flex;gap:8px;flex-wrap:wrap}
.tabs button{background:rgba(255,255,255,.06);color:#c6cede;border:1px solid rgba(255,255,255,.12);border-radius:20px;padding:7px 14px;font-size:13px;cursor:pointer;backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px);transition:all .2s}
.tabs button.on{background:linear-gradient(135deg,#6ee7ff,#a78bfa);color:#0a0f1c;border-color:transparent;font-weight:700;box-shadow:0 4px 18px rgba(124,140,255,.45)}
.search{margin-left:auto;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.12);color:#eef1f8;border-radius:20px;padding:7px 14px;font-size:13px;width:170px;outline:none;backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px)}
.search::placeholder{color:#8b94ab}
.hero{max-width:1280px;margin:0 auto;padding:44px 18px 8px}
.hero h1{font-size:32px;letter-spacing:2px;font-weight:800}
.hero h1 b{background:linear-gradient(120deg,#6ee7ff,#a78bfa,#f9a8d4,#6ee7ff);background-size:300% 100%;-webkit-background-clip:text;background-clip:text;color:transparent;animation:flow 8s linear infinite}
@keyframes flow{to{background-position:300% 0}}
.hero p{color:#aab3cc;margin-top:12px;font-size:14px}
.hero .pill{display:inline-block;margin-top:14px;padding:8px 18px;border-radius:24px;background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.14);backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);font-size:13px;color:#dfe6f5;box-shadow:inset 0 1px 0 rgba(255,255,255,.2)}
.view{max-width:1280px;margin:0 auto;padding:18px;display:none}
.view.on{display:block}
.cats{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:18px}
.cat{position:relative;background:linear-gradient(135deg,rgba(255,255,255,.1),rgba(255,255,255,.03));backdrop-filter:blur(18px);-webkit-backdrop-filter:blur(18px);border:1px solid rgba(255,255,255,.14);border-radius:20px;overflow:hidden;cursor:pointer;transition:transform .25s,box-shadow .25s;box-shadow:inset 0 1px 0 rgba(255,255,255,.22),0 10px 34px rgba(0,0,0,.35)}
.cat:hover{transform:translateY(-5px);box-shadow:inset 0 1px 0 rgba(255,255,255,.3),0 18px 44px rgba(0,0,0,.45),0 0 24px rgba(124,140,255,.25)}
.cat::after{content:"";position:absolute;inset:0;border-radius:20px;pointer-events:none;background:linear-gradient(105deg,transparent 40%,rgba(255,255,255,.14) 50%,transparent 60%);transform:translateX(-120%);transition:transform .7s}
.cat:hover::after{transform:translateX(120%)}
.cat .thumbs{display:grid;grid-template-columns:1fr 1fr;gap:6px;padding:12px 12px 0}
.cat .thumbs img{width:100%;aspect-ratio:9/14;object-fit:cover;object-position:top;border-radius:12px;border:1px solid rgba(255,255,255,.1)}
.cat .meta{padding:14px 18px 16px}
.cat .meta h3{font-size:16px}
.cat .meta p{color:#aab3cc;font-size:13px;margin-top:6px}
.cat .go{font-size:13px;margin-top:10px;display:block;color:#8fd8ff}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:16px}
.card{position:relative;background:linear-gradient(150deg,rgba(255,255,255,.09),rgba(255,255,255,.025));border:1px solid rgba(255,255,255,.12);border-radius:18px;overflow:hidden;transition:transform .22s,box-shadow .22s;box-shadow:inset 0 1px 0 rgba(255,255,255,.16),0 8px 26px rgba(0,0,0,.32)}
.card:hover{transform:translateY(-4px);box-shadow:inset 0 1px 0 rgba(255,255,255,.24),0 14px 34px rgba(0,0,0,.42),0 0 20px rgba(124,140,255,.22)}
.card .pv{position:relative;aspect-ratio:9/13;background:#0a0f1c;overflow:hidden}
.card .pv img.ph{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:top;display:block}
.card .pv .live{position:absolute;inset:0;overflow:hidden}
.card .pv .live iframe{width:430px;height:900px;border:0;display:block;transform-origin:top left}.card .pv .live iframe{pointer-events:none}
.card .pv .fsbtn{position:absolute;top:8px;right:8px;z-index:5;width:32px;height:32px;border-radius:50%;border:1px solid rgba(255,255,255,.35);background:rgba(8,12,22,.55);backdrop-filter:blur(6px);-webkit-backdrop-filter:blur(6px);color:#fff;font-size:15px;cursor:pointer;display:flex;align-items:center;justify-content:center;transition:transform .15s,background .15s}
.card .pv .fsbtn:hover{background:rgba(110,231,255,.5);transform:scale(1.12)}
.card .pv .newb{position:absolute;top:8px;left:8px;z-index:5;background:linear-gradient(135deg,#ff4d6d,#ff8a3d);color:#fff;font-size:10px;font-weight:800;letter-spacing:.08em;padding:4px 9px;border-radius:10px;box-shadow:0 4px 14px rgba(255,77,109,.55);animation:newPulse 1.6s ease-in-out infinite}
@keyframes newPulse{0%,100%{transform:scale(1)}50%{transform:scale(1.12)}}
.card.hl{box-shadow:0 0 0 3px #ff4d6d,0 0 34px rgba(255,77,109,.65)!important}
#newpill{position:fixed;left:50%;bottom:86px;transform:translateX(-50%);z-index:210;display:flex;align-items:center;gap:9px;background:linear-gradient(135deg,rgba(255,77,109,.92),rgba(255,138,61,.92));color:#fff;font-size:13.5px;font-weight:700;padding:11px 18px;border-radius:26px;cursor:pointer;box-shadow:0 10px 32px rgba(255,77,109,.5);animation:pillIn .5s cubic-bezier(.2,.8,.3,1.3) both,pillFloat 2.2s ease-in-out .6s infinite;white-space:nowrap;max-width:92vw}
#newpill small{font-weight:400;opacity:.92}
#newpill #newx{font-style:normal;opacity:.85;padding:2px 4px;font-size:12px}
@keyframes pillIn{from{opacity:0;transform:translateX(-50%) translateY(26px) scale(.9)}}
@keyframes pillFloat{0%,100%{transform:translateX(-50%) translateY(0)}50%{transform:translateX(-50%) translateY(-5px)}}
.card .ft{padding:10px 12px;display:flex;align-items:center;gap:8px}
.card .ft h4{font-size:13.5px;flex:1;min-width:0;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.copy{background:linear-gradient(135deg,#6ee7ff,#a78bfa);color:#0a0f1c;border:0;padding:7px 13px;border-radius:10px;font-size:12px;font-weight:700;cursor:pointer;white-space:nowrap;box-shadow:0 3px 12px rgba(124,140,255,.4)}
.copy.ok{background:linear-gradient(135deg,#34d399,#22b573);color:#04120c}
.back{background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.14);color:#eef1f8;border-radius:20px;padding:7px 16px;font-size:13px;cursor:pointer;margin-bottom:14px;backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px)}
.chead{font-size:20px;margin:4px 0 6px;font-weight:700}
.chead span{color:#aab3cc;font-size:13px;margin-left:10px;font-weight:400}
.cdesc{color:#aab3cc;font-size:13px;margin-bottom:16px}
.subchips{display:flex;gap:8px;flex-wrap:wrap;max-width:1280px;margin:0 auto 14px;padding:0 18px}
.subchips button{border:1px solid rgba(255,255,255,.14);background:rgba(255,255,255,.06);color:#c6cede;border-radius:20px;padding:7px 16px;font-size:12.5px;cursor:pointer;transition:all .2s;backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px)}
.subchips button.on{background:linear-gradient(135deg,#6ee7ff,#a78bfa);border-color:transparent;color:#0a0f1c;font-weight:700;box-shadow:0 4px 16px rgba(124,140,255,.4)}
.subtag{font-size:10px;color:#9fd8ff;border:1px solid rgba(143,216,255,.3);background:rgba(143,216,255,.08);border-radius:10px;padding:2px 8px;white-space:nowrap;flex-shrink:0}
.gnum{font-size:10px;color:#ffd479;border:1px solid rgba(255,212,121,.35);background:rgba(255,212,121,.08);border-radius:10px;padding:2px 8px;white-space:nowrap;flex-shrink:0;font-variant-numeric:tabular-nums;letter-spacing:1px}
.toast{position:fixed;bottom:26px;left:50%;transform:translateX(-50%);background:rgba(20,28,44,.8);backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px);border:1px solid rgba(255,255,255,.16);color:#fff;padding:10px 24px;border-radius:24px;font-size:14px;opacity:0;transition:opacity .3s;z-index:200;box-shadow:0 8px 30px rgba(0,0,0,.4)}
.empty{color:#aab3cc;text-align:center;padding:60px 0}
.pv{overflow:hidden;position:relative}
.ripple{position:absolute;border-radius:50%;background:rgba(140,220,255,.45);transform:scale(0);animation:rip .6s ease-out forwards;pointer-events:none}
@keyframes rip{to{transform:scale(4);opacity:0}}
.card{transform-style:preserve-3d;will-change:transform;animation:cardIn .5s cubic-bezier(.2,.7,.3,1.2) both;animation-delay:var(--d,0ms)}
@keyframes cardIn{from{opacity:0;transform:translateY(22px) scale(.97)}}
.copy:active,.tabs button:active,.subchips button:active{transform:scale(.93)}
.copy,.tabs button,.subchips button,.back{transition:transform .12s}
@media (prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}}
@media(max-width:640px){.grid{grid-template-columns:repeat(2,1fr)}.search{width:120px}.hero h1{font-size:24px}}
'''

JS = '''const $=s=>document.querySelector(s),$$=s=>[...document.querySelectorAll(s)];
const views={home:$('#v-home')};
const CAT2G=__CAT2G__;
let curG=-1,curS=-1;
const q=()=>$('#q').value.trim().toLowerCase();
function show(name,sub){const go=()=>{$$('.view').forEach(v=>v.classList.remove('on'));views[name].classList.add('on');
$$('.tabs button').forEach(b=>b.classList.toggle('on',b.dataset.v===name));window.scrollTo(0,0);$('#q').value='';
const sr=$('#srch');if(sr)sr.style.display='none';const cs=$('#v-home .cats');if(cs)cs.style.display='';
if(name[0]==='g')setSub(+name.slice(1),sub===undefined?-1:sub);else{curG=-1;curS=-1;}};
if(document.startViewTransition){document.startViewTransition(go);}else{go();}}
$$('.tabs button').forEach(b=>b.onclick=()=>show(b.dataset.v));
$('.logo').onclick=()=>show('home');
$$('.cat').forEach(c=>c.onclick=()=>show('g'+c.dataset.c));
function getCode(el){const b=el.dataset.b64;const bin=atob(b);const u8=Uint8Array.from(bin,c=>c.charCodeAt(0));return new TextDecoder().decode(u8);}
function openDemo(id){const card=document.querySelector('.card .pv[data-id="'+id+'"]');
const t=getCode(card.closest('.card'));
const u=URL.createObjectURL(new Blob([t],{type:'text/html'}));
const w=window.open(u,'_blank');
if(!w){location.href=u;}}
const blobCache={};
function blobUrl(card){const id=card.querySelector('.pv').dataset.id;
if(!blobCache[id])blobCache[id]=URL.createObjectURL(new Blob([getCode(card)],{type:'text/html'}));
return blobCache[id];}
function fitIfr(pv,ifr){const w=pv.clientWidth;if(w)ifr.style.transform='scale('+(w/430)+')';}
const liveIO=new IntersectionObserver(es=>{es.forEach(en=>{if(!en.isIntersecting)return;
const pv=en.target;liveIO.unobserve(pv);
const card=pv.closest('.card');const lv=pv.querySelector('.live');if(!lv||lv._done)return;lv._done=1;
const ifr=document.createElement('iframe');
ifr.setAttribute('scrolling','auto');ifr.setAttribute('title','demo');
ifr.onload=()=>{const ph=pv.querySelector('img.ph');if(ph)ph.style.display='none';};
ifr.src=blobUrl(card);lv.appendChild(ifr);fitIfr(pv,ifr);});},{rootMargin:'700px'});
function bindPv(root){root.querySelectorAll('.pv').forEach(p=>{if(p._b)return;p._b=1;
if(p.querySelector('.live'))liveIO.observe(p);
p.style.cursor='pointer';
p.addEventListener('click',e=>{if(e.target.closest('.fsbtn'))return;openDemo(p.dataset.id);});});}
document.addEventListener('click',e=>{const b=e.target.closest('.fsbtn');
if(b){e.stopPropagation();openDemo(b.dataset.id);}});
let rsz;window.addEventListener('resize',()=>{clearTimeout(rsz);rsz=setTimeout(()=>{
$$('.pv .live iframe').forEach(f=>fitIfr(f.closest('.pv'),f));},180);});
const np=document.getElementById('newpill');
if(np){np.addEventListener('click',e=>{if(e.target.id==='newx'){np.style.display='none';return;}
np.style.display='none';show('g'+NEW_G,NEW_S);
setTimeout(()=>{const cs=$$('#v-g'+NEW_G+' .card[data-new="1"]');
cs.forEach(c=>c.classList.add('hl'));
if(cs[0])cs[0].scrollIntoView({behavior:'smooth',block:'center'});
setTimeout(()=>cs.forEach(c=>c.classList.remove('hl')),3200);},450);});}
function bindCopy(root){root.querySelectorAll('.copy[data-id]').forEach(b=>{if(b._b)return;b._b=1;
b.onclick=e=>{e.stopPropagation();doCopy(b.dataset.id,b);};});}
function bindTilt(root){if(!matchMedia('(pointer:fine)').matches)return;
root.querySelectorAll('.card').forEach(c=>{if(c._t)return;c._t=1;
c.addEventListener('mousemove',e=>{const r=c.getBoundingClientRect();
const x=(e.clientX-r.left)/r.width-.5,y=(e.clientY-r.top)/r.height-.5;
c.style.transform='perspective(800px) rotateX('+(-y*7)+'deg) rotateY('+(x*7)+'deg) translateY(-3px)';});
c.addEventListener('mouseleave',()=>{c.style.transform='';});});}
bindPv(document);bindCopy(document);bindTilt(document);
const toast=$('#toast');let tt;
function copied(b){b.textContent='已复制 ✓';b.classList.add('ok');toast.style.opacity=1;clearTimeout(tt);
tt=setTimeout(()=>{toast.style.opacity=0;},1500);setTimeout(()=>{b.textContent='复制代码';b.classList.remove('ok');},1600);}
function doCopy(id,btn){const card=document.querySelector('.card .pv[data-id="'+id+'"]');const t=getCode(card.closest('.card'));
if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(t).then(()=>copied(btn)).catch(()=>fallback());}else fallback();
function fallback(){const ta=document.createElement('textarea');ta.value=t;document.body.appendChild(ta);ta.select();
try{document.execCommand('copy');copied(btn);}catch(e){}ta.remove();}}
function setSub(gi,si){curG=gi;curS=si;
$$('#chips-g'+gi+' button').forEach(b=>b.classList.toggle('on',+b.dataset.s===si));
const query=q();let vis=0;
$$('#v-g'+gi+' .card').forEach(c=>{
const ok=(si===-1||+c.dataset.sub===si)&&(!query||c.dataset.title.toLowerCase().includes(query));
c.style.display=ok?'':'none';if(ok)vis++;});
$('#empty-g'+gi).style.display=vis?'none':'block';}
$$('.subchips').forEach(ch=>{const gi=+ch.id.replace('chips-g','');
ch.querySelectorAll('button').forEach(b=>b.onclick=()=>setSub(gi,+b.dataset.s));});
$('#q').addEventListener('input',()=>{const query=q();
if(curG===-1){
const cats=$('#v-home .cats'),sr=$('#srch'),grid=$('#g-srch');
if(!query){cats.style.display='';sr.style.display='none';return;}
cats.style.display='none';sr.style.display='';grid.innerHTML='';
let n=0;
$$('.view[id^="v-g"] .card').forEach(c=>{
if(c.dataset.title.toLowerCase().includes(query)){grid.appendChild(c.cloneNode(true));n++;}});
$('#srch-n').textContent='共 '+n+' 组';
$('#empty-srch').style.display=n?'none':'block';
bindPv(grid);bindCopy(grid);bindTilt(grid);
}else{setSub(curG,curS);}});
const qs=new URLSearchParams(location.search);
if(qs.get('g')!==null&&views['g'+qs.get('g')]){const gi=+qs.get('g');
show('g'+gi,qs.get('s')===null?-1:+qs.get('s'));}
else if(qs.get('cat')!==null){const m=CAT2G[+qs.get('cat')];if(m){show('g'+m[0],m[1]);}}
if(qs.get('demo')){const id=qs.get('demo');if(document.querySelector('.pv[data-id="'+id+'"]'))openDemo(id);}
'''


import json
# ---- 分组 ----
GROUPS = [
 ("UI 组件库", "51 套 · 整套风格组件库", [0, 1, 21]),
 ("更新交互", "30 组 · 弹窗与更新动效", [2, 3, 4]),
 ("组件特效", "222 组 · 加载/按钮/开关/进度/通知/底栏", [5, 6, 7, 8, 9, 14, 23]),
 ("App 全套设计", "38 套 · 多页面 App 原型", [10, 11, 12]),
 ("新鲜设计", "324 组 · 启动页/顶部/底部/弹窗/App界面/页签卡片/通知卡/App套装", [15, 16, 17, 18, 19, 20, 22, 24, 25]),
]
SHORT = {0:"第一批",1:"20套风格",2:"弹窗10款",3:"新概念10组",4:"第二批",
         5:"加载动画",6:"按钮特效",7:"开关切换",8:"进度指示",9:"通知提醒",
         10:"功能模块",11:"产品方向",12:"电商细分",14:"底部Tab栏",
         15:"启动页",16:"顶部栏",17:"底部栏",18:"欢迎弹窗",19:"更新弹窗",20:"App界面",21:"液态主题",22:"页签卡片",23:"液态Tab栏",24:"通知卡片",25:"App套装"}
CAT2G = {}
for gi, (_, _, cis) in enumerate(GROUPS):
    for ci in cis:
        CAT2G[ci] = [gi, ci]

# 组副标题里的数量按实际条目动态计算，避免新增批次后数字过期
# （如 2026-10-20 上线页"新鲜设计"副标题仍写 224 组，实际已 332 组）
_fixed_groups = []
for _gn, _gd, _cis in GROUPS:
    _p = _gd.split(' ', 2)
    if len(_p) == 3 and _p[0].isdigit() and _p[1] in ('组', '套'):
        _cnt = len([x for x in items if x['cat'] in _cis])
        _gd = f'{_cnt} {_p[1]} {_p[2]}'
    _fixed_groups.append((_gn, _gd, _cis))
GROUPS = _fixed_groups

# 全站编号：按页面展示顺序（大组→子分类→条目）分配
_gn = 0
for _gn_, _gd_, _cis_ in GROUPS:
    for _ci_ in _cis_:
        for _x in [x for x in items if x['cat'] == _ci_]:
            _gn += 1
            _x['gnum'] = _gn

# ---- 视图 ----
_new_cats = {x['cat'] for x in items if is_new(x['title'])} | {c for c in NEW_CATS if any(x['cat'] == c for x in items)}
NEW_G, NEW_S = 0, -1
for _gi, (_gn, _gd, _cis) in enumerate(GROUPS):
    for _c in _cis:
        if _c in _new_cats:
            NEW_G, NEW_S = _gi, _c
            break
    if NEW_S != -1:
        break
home_groups = []
for gi, (gname, gdesc, cis) in enumerate(GROUPS):
    g_items = [x for x in items if x['cat'] in cis]
    th = ''.join(f'<img loading="lazy" src="data:image/jpeg;base64,{x["thumb"]}" alt="">' for x in g_items[:4])
    subs = ' · '.join(f'{SHORT[ci]} {len([x for x in items if x["cat"] == ci])}组' for ci in cis)
    home_groups.append(f'''<div class="cat" data-c="{gi}"><div class="thumbs">{th}</div>
<div class="meta"><h3>{html.escape(gname)}</h3><p>{html.escape(gdesc)}</p><p>{html.escape(subs)}</p><span class="go">进入大组 →</span></div></div>''')

group_views = []
for gi, (gname, gdesc, cis) in enumerate(GROUPS):
    g_items = [x for x in items if x['cat'] in cis]
    chips = ['<button data-s="-1" class="on">全部</button>'] + \
            [f'<button data-s="{ci}">{html.escape(SHORT[ci])}</button>' for ci in cis]
    cards = []
    for ci2, x in enumerate(g_items):
        _d = (ci2 % 20) * 35
        b64 = base64.b64encode(x['code'].encode('utf-8')).decode()
        cards.append(f'''<div class="card" style="--d:{_d}ms" data-sub="{x["cat"]}" data-title="{html.escape(x["title"], quote=True)} {x["gnum"]:03d}" data-b64="{b64}"{' data-new="1"' if (is_new(x["title"]) or x["cat"] in NEW_CATS) else ''}>
<div class="pv" data-id="{x["id"]}"><img class="ph" loading="lazy" src="data:image/jpeg;base64,{x["thumb"]}" alt="{html.escape(x["title"], quote=True)}"><div class="live"></div>{'<span class="newb">NEW</span>' if (is_new(x["title"]) or x["cat"] in NEW_CATS) else ''}<button class="fsbtn" data-id="{x["id"]}" title="全屏打开">⛶</button></div>
<div class="ft"><span class="gnum">№{x["gnum"]:03d}</span><span class="subtag">{html.escape(SHORT[x["cat"]])}</span><h4 id="h-{x["id"]}">{html.escape(x["title"])}</h4><button class="copy" data-id="{x["id"]}">复制代码</button></div></div>''')
    group_views.append(f'''<div class="view" id="v-g{gi}">
<button class="back" onclick="show('home')">← 返回全部分类</button>
<div class="chead">{html.escape(gname)}<span>共 {len(g_items)} 组 · 预览可直接试玩</span></div>
<div class="subchips" id="chips-g{gi}">{''.join(chips)}</div>
<div class="grid" id="g-g{gi}">{''.join(cards)}</div><div class="empty" id="empty-g{gi}" style="display:none">没有匹配的案例</div></div>''')

tabs = ['<button data-v="home" class="on">全部分类</button>'] + \
       [f'<button data-v="g{gi}">{html.escape(gname)}</button>' for gi, (gname, _, _) in enumerate(GROUPS)]

home_search = '''<div id="srch" style="display:none"><div class="chead">搜索结果<span id="srch-n"></span></div><div class="grid" id="g-srch"></div><div class="empty" id="empty-srch" style="display:none">没有匹配的案例</div></div>'''

page = ('<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8">'
 '<meta name="viewport" content="width=device-width,initial-scale=1">'
 '<title>全部案例 · 画廊总库</title><style>' + CSS + '</style></head><body><div class="bg"><i></i><i></i><i></i></div>'
 '<div class="top"><div class="top-in"><div class="logo">全部案例 · <b>画廊总库</b></div>'
 '<div class="tabs">' + ''.join(tabs) + '</div>'
 '<input class="search" id="q" placeholder="搜索案例…"></div></div>'
 '<div class="hero"><h1>设计开发 <b>APP 案例</b>总库</h1><p>' + str(n) + ' 组案例 · 预览可直接试玩 · 每组代码一键复制</p><span class="pill">液态玻璃主题 · 全面升级版</span></div>'
 '<div class="view on" id="v-home"><div class="cats">' + ''.join(home_groups) + '</div>' + home_search + '</div>'
 + ''.join(group_views) +
  '<div class="toast" id="toast">代码已复制</div>' +
 (f'<div id="newpill" data-g="{NEW_G}" data-s="{NEW_S}">✨ 新增 {html.escape(NEW_LABEL)} <small>点我直达 →</small><i id="newx" title="关闭">✕</i></div>' if (NEW_TITLES or NEW_CATS) else '') +
 '<script>' + JS.replace('__CAT2G__', json.dumps(CAT2G)).replace('const CAT2G=', f'const NEW_G={NEW_G},NEW_S={NEW_S},CAT2G=') + '</script></body></html>')

# views 字典补全（JS 里引用 views['gN']）
page = page.replace("const views={home:$('#v-home')};",
                    "const views={home:$('#v-home')" + ''.join(f",g{gi}:$('#v-g{gi}')" for gi in range(len(GROUPS))) + "};")

open(OUT, 'w', encoding='utf-8').write(page)
print('written', OUT, len(page)//1024, 'KB')
