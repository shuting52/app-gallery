#!/usr/bin/env python3
"""20 组加载动画 · 生成脚本（纯 CSS keyframes，无 JS）"""
import os

OUT = os.path.expanduser('~/workspace/components/loaders')
os.makedirs(OUT, exist_ok=True)

TPL = """<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} · 加载动画</title><style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{min-height:100vh;background:{bg};display:flex;flex-direction:column;align-items:center;justify-content:center;
font-family:-apple-system,"PingFang SC","Microsoft YaHei",sans-serif;color:#e8eaf0;padding:24px 12px}}
h1{{font-size:15px;font-weight:600;letter-spacing:4px;color:{ac};margin-bottom:6px}}
.sub{{font-size:11px;color:#8a90a6;margin-bottom:30px;letter-spacing:3px}}
.stage{{width:360px;max-width:94vw;height:300px;position:relative;display:flex;align-items:center;justify-content:center}}
{css}
</style></head><body><h1>{title}</h1><div class="sub">LOADING · 加载中</div><div class="stage">{body}</div></body></html>"""

def W(title, bg, ac, css, body):
    return TPL.format(title=title, bg=bg, ac=ac, css=css, body=body)

items = []

# ---------- l01 呼吸光点 ----------
css = """.bd{display:flex;gap:18px}
.bd i{width:22px;height:22px;border-radius:50%;background:radial-gradient(circle at 35% 35%,#a5f3fc,#22d3ee 70%);
box-shadow:0 0 18px #22d3ee;animation:br 1.8s ease-in-out infinite}
.bd i:nth-child(2){animation-delay:.18s}.bd i:nth-child(3){animation-delay:.36s}
.bd i:nth-child(4){animation-delay:.54s}.bd i:nth-child(5){animation-delay:.72s}
@keyframes br{0%,100%{transform:scale(.35);opacity:.25}50%{transform:scale(1.15);opacity:1}}"""
items.append(("l01.html", "呼吸光点", "radial-gradient(600px 400px at 50% 40%,#0e2a38,#070b12 70%)", "#22d3ee",
              css, '<div class="bd"><i></i><i></i><i></i><i></i><i></i></div>'))

# ---------- l02 液态gooey合并 ----------
css = """.goo{width:220px;height:220px;position:relative;filter:url(#goof)}
.goo .b{position:absolute;width:46px;height:46px;top:87px;left:87px;border-radius:50%;background:#a78bfa}
.goo .c{animation:gp 2.6s ease-in-out infinite}
.goo .s{animation:gm 2.6s ease-in-out infinite}
.goo .s1{--dx:74px;--dy:0}.goo .s2{--dx:-74px;--dy:0}.goo .s3{--dx:0;--dy:74px}.goo .s4{--dx:0;--dy:-74px}
@keyframes gm{0%,100%{transform:translate(0,0)}50%{transform:translate(var(--dx),var(--dy))}}
@keyframes gp{0%,100%{transform:scale(1)}50%{transform:scale(1.25)}}"""
body = ('<svg width="0" height="0" style="position:absolute"><defs><filter id="goof">'
        '<feGaussianBlur in="SourceGraphic" stdDeviation="14" result="b"/>'
        '<feColorMatrix in="b" values="1 0 0 0 0 0 1 0 0 0 0 0 1 0 0 0 0 0 22 -12"/></filter></defs></svg>'
        '<div class="goo"><div class="b c"></div><div class="b s s1"></div><div class="b s s2"></div>'
        '<div class="b s s3"></div><div class="b s s4"></div></div>')
items.append(("l02.html", "液态合并", "radial-gradient(600px 400px at 50% 40%,#1d1440,#0a0716 70%)", "#a78bfa", css, body))

# ---------- l03 赛博扫描线 ----------
css = """.panel{width:290px;height:190px;position:relative;overflow:hidden;border:1px solid rgba(34,211,238,.5);
background:repeating-linear-gradient(0deg,transparent 0 17px,rgba(34,211,238,.09) 17px 18px),
repeating-linear-gradient(90deg,transparent 0 17px,rgba(34,211,238,.09) 17px 18px),rgba(8,20,28,.6)}
.scan{position:absolute;left:0;right:0;height:4px;top:-8px;
background:linear-gradient(90deg,transparent,#22d3ee 30%,#bff6ff 50%,#22d3ee 70%,transparent);
box-shadow:0 0 22px 4px rgba(34,211,238,.8);animation:sc 2.4s linear infinite}
@keyframes sc{to{transform:translateY(210px)}}
.cn{position:absolute;width:22px;height:22px;border:2px solid #22d3ee}
.cn.tl{top:8px;left:8px;border-right:0;border-bottom:0}.cn.tr{top:8px;right:8px;border-left:0;border-bottom:0}
.cn.bl{bottom:8px;left:8px;border-right:0;border-top:0}.cn.br{bottom:8px;right:8px;border-left:0;border-top:0}
.stx{position:absolute;bottom:12px;width:100%;text-align:center;font-size:11px;letter-spacing:4px;color:#7ee7f7;animation:blk 1.2s steps(2) infinite}
@keyframes blk{50%{opacity:.35}}"""
body = ('<div class="panel"><div class="scan"></div><div class="cn tl"></div><div class="cn tr"></div>'
        '<div class="cn bl"></div><div class="cn br"></div><div class="stx">SCANNING · 扫描中</div></div>')
items.append(("l03.html", "赛博扫描线", "radial-gradient(600px 400px at 50% 40%,#062a33,#04090d 70%)", "#22d3ee", css, body))

# ---------- l04 纸飞机环绕 ----------
css = """.orb{width:230px;height:230px;position:relative;animation:spn 7s linear infinite}
.orb .ring{position:absolute;inset:0;border:1.5px dashed rgba(255,255,255,.28);border-radius:50%}
.plane{position:absolute;top:-16px;left:50%;margin-left:-17px;width:34px;height:30px;
background:linear-gradient(135deg,#fff,#bcd7ff);clip-path:polygon(0 100%,50% 0,100% 100%,50% 76%);
filter:drop-shadow(0 4px 8px rgba(150,190,255,.5));animation:bob 1.4s ease-in-out infinite}
@keyframes bob{50%{margin-top:-9px}}
@keyframes spn{to{transform:rotate(360deg)}}
.hub{position:absolute;top:50%;left:50%;width:56px;height:56px;margin:-28px 0 0 -28px;border-radius:50%;
background:radial-gradient(circle at 35% 35%,#cfe6ff,#5b8def 75%);box-shadow:0 0 30px rgba(91,141,239,.8);
display:flex;align-items:center;justify-content:center;font-size:11px;color:#0b1c3f;font-weight:700}
.orbfix{position:relative;width:230px;height:230px}"""
body = ('<div class="orbfix"><div class="orb"><div class="ring"></div><div class="plane"></div></div>'
        '<div class="hub">LOAD</div></div>')
items.append(("l04.html", "纸飞机环绕", "radial-gradient(600px 400px at 50% 40%,#101b3a,#070a16 70%)", "#8fb4ff", css, body))

# ---------- l05 DNA双螺旋 ----------
pairs = []
for i in range(12):
    d = i * 0.16
    pairs.append(f'<div class="pr" style="animation-delay:{d:.2f}s"><i class="dl"></i><i class="dr"></i><b class="rg"></b></div>')
css = """.dna{display:flex;flex-direction:column;gap:2px}
.pr{width:130px;height:24px;position:relative;animation:tw 2.4s ease-in-out infinite}
.pr i{position:absolute;top:7px;width:11px;height:11px;border-radius:50%}
.dl{left:14px;background:#f472b6;box-shadow:0 0 10px #f472b6}
.dr{right:14px;background:#38bdf8;box-shadow:0 0 10px #38bdf8}
.rg{position:absolute;left:30px;right:30px;top:11.5px;height:2px;background:rgba(255,255,255,.35);transform-origin:center}
@keyframes tw{0%,100%{transform:translateY(-9px)}50%{transform:translateY(9px)}}
.pr .rg{animation:rgw 2.4s ease-in-out infinite}
@keyframes rgw{0%,100%{transform:scaleX(.25);opacity:.3}50%{transform:scaleX(1);opacity:.9}}"""
# rung delays must match pair delays -> set inline
pairs2 = []
for i in range(12):
    d = i * 0.16
    pairs2.append(f'<div class="pr" style="animation-delay:{d:.2f}s"><i class="dl"></i><i class="dr"></i><b class="rg" style="animation-delay:{d:.2f}s"></b></div>')
body = '<div class="dna">' + ''.join(pairs2) + '</div>'
items.append(("l05.html", "DNA双螺旋", "radial-gradient(600px 400px at 50% 40%,#160f2e,#08060f 70%)", "#f472b6", css, body))

# ---------- l06 波浪方块 ----------
cells = ''.join(f'<i style="animation-delay:{((c%8)*0.09 + (r)*0.06):.2f}s"></i>' for r in range(4) for c in range(8))
css = """.wb{display:grid;grid-template-columns:repeat(8,26px);gap:9px}
.wb i{width:26px;height:26px;border-radius:6px;background:linear-gradient(135deg,#34d399,#0ea5e9);
animation:wv 1.5s ease-in-out infinite;box-shadow:0 0 10px rgba(52,211,153,.35)}
@keyframes wv{0%,100%{transform:scaleY(.25);opacity:.45}50%{transform:scaleY(1);opacity:1}}"""
items.append(("l06.html", "波浪方块", "radial-gradient(600px 400px at 50% 40%,#06251d,#040c0a 70%)", "#34d399", css,
              f'<div class="wb">{cells}</div>'))

# ---------- l07 星系旋转 ----------
stars = ''.join(f'<i class="st" style="left:{(i*67)%100}%;top:{(i*41)%100}%;animation-delay:{(i*0.37)%2:.2f}s"></i>' for i in range(24))
css = """.gal{width:270px;height:270px;position:relative}
.st{position:absolute;width:3px;height:3px;border-radius:50%;background:#fff;animation:twk 2s ease-in-out infinite}
@keyframes twk{50%{opacity:.15}}
.core{position:absolute;top:50%;left:50%;width:44px;height:44px;margin:-22px 0 0 -22px;border-radius:50%;
background:radial-gradient(circle at 40% 40%,#fff7d6,#fbbf24 55%,#b45309);box-shadow:0 0 34px 10px rgba(251,191,36,.55);
animation:core 3s ease-in-out infinite}
@keyframes core{50%{transform:scale(1.12)}}
.ring{position:absolute;top:50%;left:50%;border:1px solid rgba(255,255,255,.16);border-radius:50%;animation:spn linear infinite}
.r1{width:120px;height:120px;margin:-60px 0 0 -60px;animation-duration:5s}
.r2{width:185px;height:185px;margin:-92.5px 0 0 -92.5px;animation-duration:9s;animation-direction:reverse}
.r3{width:250px;height:250px;margin:-125px 0 0 -125px;animation-duration:15s}
.pl{position:absolute;top:-6px;left:50%;margin-left:-6px;width:12px;height:12px;border-radius:50%}
.r1 .pl{background:#38bdf8;box-shadow:0 0 12px #38bdf8}.r2 .pl{background:#f472b6;box-shadow:0 0 12px #f472b6}
.r3 .pl{background:#a78bfa;box-shadow:0 0 12px #a78bfa;width:9px;height:9px;margin-left:-4.5px;top:-4.5px}
@keyframes spn{to{transform:rotate(360deg)}}"""
body = (f'<div class="gal">{stars}<div class="ring r1"><i class="pl"></i></div>'
        '<div class="ring r2"><i class="pl"></i></div><div class="ring r3"><i class="pl"></i></div><div class="core"></div></div>')
items.append(("l07.html", "星系旋转", "#05060e", "#fbbf24", css, body))

# ---------- l08 打字机 ----------
css = """.twr{position:relative;height:44px;width:320px}
.ph{position:absolute;left:0;top:8px;white-space:nowrap;overflow:hidden;width:0;font-size:19px;color:#e8eaf0;
border-right:3px solid #4ade80;animation:typ 9s linear infinite;letter-spacing:1px}
.ph:nth-child(2){animation-delay:3s}.ph:nth-child(3){animation-delay:6s}
@keyframes typ{0%{width:0;opacity:1}20%{width:24ch;opacity:1}30%{width:24ch;opacity:1}
33%{width:24ch;opacity:0}33.5%{width:0;opacity:0}100%{width:0;opacity:0}}
.ph .ct{animation:blk .7s steps(2) infinite;color:#4ade80}
@keyframes blk{50%{opacity:0}}"""
body = ('<div class="twr"><div class="ph">正在连接服务器…<span class="ct">▍</span></div>'
        '<div class="ph">正在加载资源文件…<span class="ct">▍</span></div>'
        '<div class="ph">正在渲染精美界面…<span class="ct">▍</span></div></div>')
items.append(("l08.html", "打字机", "radial-gradient(600px 400px at 50% 40%,#0c1a12,#050806 70%)", "#4ade80", css, body))

# ---------- l09 光环morph ----------
css = """.halo{width:150px;height:150px;position:relative;animation:mph 5s ease-in-out infinite}
.halo::before{content:"";position:absolute;inset:0;border-radius:50%;
background:conic-gradient(from 0deg,#f0f,#ff0,#0ff,#f0f);filter:blur(2px);
animation:mph2 5s ease-in-out infinite,spn 3s linear infinite}
.halo::after{content:"";position:absolute;inset:14px;background:#0b0d16;border-radius:inherit;animation:mph2 5s ease-in-out infinite}
@keyframes mph{0%,100%{border-radius:50%;transform:rotate(0) scale(1)}33%{border-radius:32% 68% 62% 38%/44% 36% 64% 56%;transform:rotate(120deg) scale(1.08)}
66%{border-radius:64% 36% 38% 62%/58% 64% 36% 42%;transform:rotate(240deg) scale(.94)}}
@keyframes mph2{0%,100%{border-radius:50%}33%{border-radius:32% 68% 62% 38%/44% 36% 64% 56%}66%{border-radius:64% 36% 38% 62%/58% 64% 36% 42%}}
@keyframes spn{to{transform:rotate(360deg)}}
.halo{filter:drop-shadow(0 0 22px rgba(217,70,239,.55))}"""
items.append(("l09.html", "光环morph", "radial-gradient(600px 400px at 50% 40%,#1c0f24,#0a060f 70%)", "#e879f9", css,
              '<div class="halo"></div>'))

# ---------- l10 折纸翻转 ----------
tiles = ''.join(f'<i style="animation-delay:{i*0.14:.2f}s"></i>' for i in range(6))
css = """.fl{display:flex;gap:8px;perspective:500px}
.fl i{width:42px;height:58px;border-radius:6px;background:linear-gradient(135deg,#fbbf24,#f97316);
box-shadow:0 6px 14px rgba(249,115,22,.35);animation:flp 1.9s ease-in-out infinite}
@keyframes flp{0%,100%{transform:rotateX(0)}50%{transform:rotateX(180deg);background:linear-gradient(135deg,#fde68a,#fb923c)}}"""
items.append(("l10.html", "折纸翻转", "radial-gradient(600px 400px at 50% 40%,#241505,#0d0803 70%)", "#fbbf24", css,
              f'<div class="fl">{tiles}</div>'))

# ---------- l11 泡泡上升 ----------
import random
random.seed(7)
bubs = []
for i in range(9):
    left = random.randint(4, 92); sz = random.randint(16, 44); dur = round(random.uniform(3.2, 5.6), 2)
    dl = round(random.uniform(0, 4), 2); dx = random.randint(-34, 34)
    bubs.append(f'<i style="left:{left}%;width:{sz}px;height:{sz}px;animation-duration:{dur}s;animation-delay:-{dl}s;--dx:{dx}px"></i>')
css = """.bubs{width:340px;height:290px;position:relative;overflow:hidden;
background:linear-gradient(180deg,#0a2740 0%,#06121f 70%);border-radius:18px;border:1px solid rgba(125,211,252,.2)}
.bubs i{position:absolute;display:block;bottom:-50px;border-radius:50%;
background:radial-gradient(circle at 32% 30%,rgba(255,255,255,.85) 0 12%,rgba(125,211,252,.28) 45%,rgba(125,211,252,.06) 75%);
border:1px solid rgba(186,230,253,.35);animation:rise linear infinite}
@keyframes rise{0%{transform:translate(0,0) scale(.7);opacity:0}12%{opacity:.95}
88%{opacity:.9}100%{transform:translate(var(--dx),-360px) scale(1.05);opacity:0}}"""
items.append(("l11.html", "泡泡上升", "radial-gradient(600px 400px at 50% 40%,#0a1c30,#04080e 70%)", "#7dd3fc", css,
              '<div class="bubs">' + ''.join(bubs) + '</div>'))

# ---------- l12 磁吸粒子 ----------
arms = []
for i in range(10):
    a = i * 36
    arms.append(f'<div class="w" style="transform:rotate({a}deg)"><i class="pt" style="animation-delay:{(i*0.24)%2.4:.2f}s"></i></div>')
css = """.magw{width:300px;height:300px;position:relative}
.mag{position:absolute;top:50%;left:50%;width:104px;height:52px;margin:-26px 0 0 -52px;border-radius:10px;
background:linear-gradient(90deg,#ef4444 50%,#f8fafc 50%);box-shadow:0 0 26px rgba(239,68,68,.5);
animation:mgp 2.4s ease-in-out infinite;display:flex;align-items:center;justify-content:center}
.mag b{font-size:12px;color:#0f172a;letter-spacing:2px}
@keyframes mgp{50%{transform:scale(1.1);box-shadow:0 0 40px rgba(239,68,68,.8)}}
.w{position:absolute;top:50%;left:50%;width:0;height:0}
.pt{position:absolute;top:-6px;left:118px;width:12px;height:12px;margin-top:-6px;border-radius:50%;
background:#fbbf24;box-shadow:0 0 12px #fbbf24;animation:att 2.4s ease-in-out infinite}
@keyframes att{0%,100%{transform:translateX(0);opacity:.85}50%{transform:translateX(-66px);opacity:1}}"""
body = '<div class="magw"><div class="mag"><b>N · S</b></div>' + ''.join(arms) + '</div>'
items.append(("l12.html", "磁吸粒子", "radial-gradient(600px 400px at 50% 40%,#200d0d,#0b0505 70%)", "#fbbf24", css, body))

# ---------- l13 霓虹均衡器 ----------
bars = []
for i in range(14):
    dur = round(random.uniform(0.45, 1.05), 2); dl = round(random.uniform(0, 0.9), 2)
    bars.append(f'<i style="animation-duration:{dur}s;animation-delay:{dl}s"></i>')
css = """.eq{display:flex;gap:9px;align-items:flex-end;height:150px}
.eq i{display:block;width:15px;height:100%;border-radius:7px;background:linear-gradient(to top,#d946ef,#22d3ee);
box-shadow:0 0 14px rgba(217,70,239,.8),0 0 30px rgba(34,211,238,.4);
transform-origin:bottom;animation:eqb ease-in-out infinite alternate}
@keyframes eqb{from{transform:scaleY(.12)}to{transform:scaleY(1)}}"""
items.append(("l13.html", "霓虹均衡器", "radial-gradient(600px 400px at 50% 40%,#170b26,#08040f 70%)", "#e879f9", css,
              '<div class="eq">' + ''.join(bars) + '</div>'))

# ---------- l14 方块掉落 ----------
drops = []
for i in range(6):
    dl = i * 0.55
    drops.append(f'<i style="left:{20+i*52}px;animation-delay:-{dl:.2f}s;background:{["#f472b6","#38bdf8","#a78bfa","#34d399","#fbbf24","#fb7185"][i]}"></i>')
css = """.dp{width:340px;height:290px;position:relative;overflow:hidden;border-bottom:3px solid rgba(255,255,255,.25);border-radius:6px}
.dp i{position:absolute;top:-46px;width:44px;height:44px;border-radius:8px;opacity:0;animation:drp 3.6s ease-in infinite;
box-shadow:0 6px 16px rgba(0,0,0,.4)}
@keyframes drp{0%{transform:translateY(0) rotate(0);opacity:0}6%{opacity:1}
68%{transform:translateY(268px) rotate(8deg);opacity:1}
76%{transform:translateY(248px) rotate(0)}84%{transform:translateY(268px)}
92%,100%{transform:translateY(268px);opacity:0}}"""
items.append(("l14.html", "方块掉落", "radial-gradient(600px 400px at 50% 40%,#131c33,#070a14 70%)", "#a78bfa", css,
              '<div class="dp">' + ''.join(drops) + '</div>'))

# ---------- l15 钟摆 ----------
pivs = []
for i in range(5):
    cls = 'p1' if i == 0 else ('p5' if i == 4 else 'pm')
    pivs.append(f'<div class="piv {cls}" style="left:{70+i*56}px"><i class="str"></i><i class="bl"></i></div>')
css = """.cr{width:340px;height:280px;position:relative}
.bar{position:absolute;top:30px;left:40px;right:40px;height:10px;border-radius:5px;background:linear-gradient(180deg,#64748b,#334155)}
.piv{position:absolute;top:40px;width:0;transform-origin:top center}
.p1{animation:sw1 2s ease-in-out infinite}.p5{animation:sw5 2s ease-in-out infinite}
.str{display:block;width:3px;height:120px;background:rgba(226,232,240,.7);margin:0 auto}
.bl{display:block;width:30px;height:30px;margin:-2px 0 0 -15px;border-radius:50%;
background:radial-gradient(circle at 35% 30%,#f1f5f9,#94a3b8 70%);box-shadow:0 6px 12px rgba(0,0,0,.45)}
@keyframes sw1{0%,50%,100%{transform:rotate(0)}18%{transform:rotate(38deg)}36%{transform:rotate(0)}}
@keyframes sw5{0%,50%,100%{transform:rotate(0)}68%{transform:rotate(-38deg)}86%{transform:rotate(0)}}
.shd{position:absolute;bottom:38px;left:60px;right:60px;height:14px;border-radius:50%;background:rgba(0,0,0,.4);filter:blur(6px)}"""
body = '<div class="cr"><div class="bar"></div>' + ''.join(pivs) + '<div class="shd"></div></div>'
items.append(("l15.html", "牛顿钟摆", "radial-gradient(600px 400px at 50% 40%,#1a2233,#090c14 70%)", "#cbd5e1", css, body))

# ---------- l16 涟漪扩散 ----------
rps = ''.join(f'<i style="animation-delay:-{i*0.65:.2f}s"></i>' for i in range(4))
css = """.rpw{width:300px;height:300px;position:relative}
.rpw i{position:absolute;display:block;top:50%;left:50%;width:26px;height:26px;margin:-13px 0 0 -13px;border-radius:50%;
border:3px solid #22d3ee;animation:rip 2.6s ease-out infinite}
@keyframes rip{0%{transform:scale(1);opacity:1}100%{transform:scale(9);opacity:0}}
.dotc{position:absolute;top:50%;left:50%;width:22px;height:22px;margin:-11px 0 0 -11px;border-radius:50%;
background:radial-gradient(circle at 35% 35%,#bff6ff,#22d3ee 70%);box-shadow:0 0 24px #22d3ee;animation:br2 2.6s ease-in-out infinite}
@keyframes br2{50%{transform:scale(1.35)}}"""
items.append(("l16.html", "涟漪扩散", "radial-gradient(600px 400px at 50% 40%,#06222b,#03090c 70%)", "#22d3ee", css,
              '<div class="rpw">' + rps + '<div class="dotc"></div></div>'))

# ---------- l17 骰子滚动 ----------
def face(pips):
    cells = ''.join('<b class="pip"></b>' if i in pips else '<b></b>' for i in range(9))
    return f'<div class="fc">{cells}</div>'
faces = (face({4}) + face({0, 8}) + face({0, 4, 8}) + face({0, 2, 6, 8}) + face({0, 2, 4, 6, 8}) + face({0, 2, 3, 5, 6, 8}))
css = """.dcw{width:200px;height:200px;perspective:600px;position:relative}
.cube{width:110px;height:110px;position:absolute;top:45px;left:45px;transform-style:preserve-3d;animation:tbl 3.4s cubic-bezier(.6,.05,.3,1) infinite}
@keyframes tbl{0%{transform:rotateX(0) rotateY(0)}50%{transform:rotateX(-180deg) rotateY(-180deg)}100%{transform:rotateX(-360deg) rotateY(-360deg)}}
.fc{position:absolute;width:110px;height:110px;border-radius:16px;background:linear-gradient(135deg,#fff,#dbe4f0);
display:grid;grid-template-columns:repeat(3,1fr);grid-template-rows:repeat(3,1fr);padding:16px;
box-shadow:inset 0 0 0 2px rgba(15,23,42,.08)}
.fc .pip{width:20px;height:20px;border-radius:50%;background:#0f172a;place-self:center}
.fc:nth-child(1){transform:translateZ(55px)}.fc:nth-child(2){transform:rotateY(180deg) translateZ(55px)}
.fc:nth-child(3){transform:rotateY(90deg) translateZ(55px)}.fc:nth-child(4){transform:rotateY(-90deg) translateZ(55px)}
.fc:nth-child(5){transform:rotateX(90deg) translateZ(55px)}.fc:nth-child(6){transform:rotateX(-90deg) translateZ(55px)}
.dsh{position:absolute;bottom:6px;left:50%;width:120px;height:16px;margin-left:-60px;border-radius:50%;
background:rgba(0,0,0,.45);filter:blur(7px);animation:sh 3.4s cubic-bezier(.6,.05,.3,1) infinite}
@keyframes sh{0%,100%{transform:scaleX(1);opacity:.8}50%{transform:scaleX(.55);opacity:.4}}"""
items.append(("l17.html", "骰子滚动", "radial-gradient(600px 400px at 50% 40%,#12233d,#060a13 70%)", "#f8fafc", css,
              '<div class="dcw"><div class="cube">' + faces + '</div><div class="dsh"></div></div>'))

# ---------- l18 像素爱心 ----------
heart = [".XX.XX.", "XXXXXXX", "XXXXXXX", ".XXXXX.", "..XXX..", "...X..."]
px = []
for r, row in enumerate(heart):
    for c, ch in enumerate(row):
        if ch == 'X':
            px.append(f'<i style="animation-delay:{(r*7+c)*0.07:.2f}s"></i>')
css = """.htw{animation:beat 1.6s ease-in-out infinite}
.ht{display:grid;grid-template-columns:repeat(7,30px);gap:5px}
.ht i{width:30px;height:30px;border-radius:5px;background:linear-gradient(135deg,#fb7185,#e11d48);
box-shadow:0 0 12px rgba(244,63,94,.6);transform:scale(0);animation:pop .5s cubic-bezier(.2,1.6,.4,1) forwards}
@keyframes pop{to{transform:scale(1)}}
@keyframes beat{0%,100%{transform:scale(1)}12%{transform:scale(1.12)}24%{transform:scale(1)}}"""
items.append(("l18.html", "像素爱心", "radial-gradient(600px 400px at 50% 40%,#2b0d18,#0d0408 70%)", "#fb7185", css,
              '<div class="htw"><div class="ht">' + ''.join(px) + '</div></div>'))

# ---------- l19 黑洞吸积 ----------
motes = ''.join(f'<i class="dw" style="animation-duration:{5+i*0.9:.1f}s"><b style="transform:rotate({i*45}deg) translateX({86+(i%3)*16}px)"></b></i>' for i in range(8))
css = """.bh{width:280px;height:280px;position:relative}
.hole{position:absolute;top:50%;left:50%;width:92px;height:92px;margin:-46px 0 0 -46px;border-radius:50%;background:#000;
box-shadow:0 0 34px 10px rgba(255,150,60,.4),0 0 90px 30px rgba(255,110,40,.16);z-index:3;animation:hp 4s ease-in-out infinite}
@keyframes hp{50%{box-shadow:0 0 44px 14px rgba(255,150,60,.55),0 0 110px 36px rgba(255,110,40,.22)}}
.dk{position:absolute;top:50%;left:50%;border-radius:50%;transform:rotateX(72deg);animation:spn linear infinite}
.dk1{width:180px;height:180px;margin:-90px 0 0 -90px;border:2px dashed rgba(255,190,110,.55);animation-duration:6s}
.dk2{width:238px;height:238px;margin:-119px 0 0 -119px;border:1.5px dashed rgba(255,140,80,.3);animation-duration:11s;animation-direction:reverse}
@keyframes spn{to{transform:rotateX(72deg) rotateZ(360deg)}}
.dw{position:absolute;top:50%;left:50%;width:0;height:0;transform:rotateX(72deg);animation:spn2 linear infinite}
@keyframes spn2{to{transform:rotateX(72deg) rotateZ(-360deg)}}
.dw b{position:absolute;width:9px;height:9px;margin:-4.5px;border-radius:50%;background:#ffd9a0;box-shadow:0 0 10px #ffb35c}
.hole::after{content:"";position:absolute;inset:-16px;border-radius:50%;border:2px solid rgba(255,180,100,.25)}"""
body = f'<div class="bh"><div class="dk dk1"></div><div class="dk dk2"></div>{motes}<div class="hole"></div></div>'
items.append(("l19.html", "黑洞吸积", "#040308", "#ffb35c", css, body))

# ---------- l20 彩虹桥 ----------
cols = ["#ef4444", "#f97316", "#facc15", "#22c55e", "#38bdf8", "#a78bfa"]
arcs = ''.join(f'<i class="arc" style="width:{300-i*30}px;height:{300-i*30}px;border-top-color:{c};animation-delay:-{i*0.22:.2f}s"></i>' for i, c in enumerate(cols))
css = """.rb{width:320px;height:200px;position:relative;overflow:hidden}
.arc{position:absolute;display:block;bottom:-148px;left:50%;transform:translateX(-50%);border-radius:50%;
border:13px solid transparent;opacity:0;animation:arc 4.5s ease-out infinite}
@keyframes arc{0%{opacity:0;transform:translateX(-50%) scale(.6)}25%{opacity:1}70%{opacity:1;transform:translateX(-50%) scale(1)}
100%{opacity:0;transform:translateX(-50%) scale(1)}}
.tw{position:absolute;bottom:0;left:50%;width:300px;height:150px;margin-left:-150px;transform-origin:50% 100%;animation:spn 4.5s linear infinite}
@keyframes spn{to{transform:rotate(180deg)}}
.td{position:absolute;display:block;top:-7px;left:50%;width:14px;height:14px;margin-left:-7px;border-radius:50%;
background:#fff;box-shadow:0 0 16px #fff,0 0 34px #fde68a}
.gnd{position:absolute;bottom:0;left:30px;right:30px;height:3px;background:rgba(255,255,255,.25);border-radius:2px}"""
body = f'<div class="rb">{arcs}<div class="tw"><i class="td"></i></div><div class="gnd"></div></div>'
items.append(("l20.html", "彩虹桥", "radial-gradient(600px 400px at 50% 100%,#1b1440,#070512 75%)", "#facc15", css, body))

# ---------- 写文件 ----------
import json
manifest = []
for fname, title, bg, ac, css, body in items:
    p = os.path.join(OUT, fname)
    open(p, 'w', encoding='utf-8').write(W(title, bg, ac, css, body))
    assert 'alert(' not in open(p, encoding='utf-8').read()
    manifest.append({"file": fname, "title": title})
open(os.path.join(OUT, 'manifest.json'), 'w', encoding='utf-8').write(
    json.dumps(manifest, ensure_ascii=False, indent=2))
print('wrote', len(items), 'files + manifest.json')
