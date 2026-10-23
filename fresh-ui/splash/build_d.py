#!/usr/bin/env python3
"""s55-s72 启动页生成器（D组）"""
import os

OUT = os.path.dirname(os.path.abspath(__file__))

TPL = """<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>__TITLE__</title><style>
*{margin:0;padding:0;box-sizing:border-box}
html,body{height:100%}
body{width:430px;height:900px;margin:0 auto;position:relative;overflow:hidden;
font-family:-apple-system,"PingFang SC","Microsoft YaHei","Noto Sans CJK SC",sans-serif;
background:__BG__;color:#fff}
.scene{position:absolute;inset:0}
__CSS__
.brand{position:absolute;left:0;right:0;bottom:118px;text-align:center;z-index:5;
color:__BCOL__;opacity:0;animation:brandIn 1s ease 2.2s both}
.brand h1{font-size:34px;letter-spacing:8px;font-weight:800}
.brand p{font-size:13px;letter-spacing:3px;margin-top:10px;opacity:.75}
@keyframes brandIn{from{opacity:0;transform:translateY(18px)}to{opacity:1;transform:none}}
.replay{position:absolute;left:50%;bottom:44px;transform:translateX(-50%);z-index:6;
padding:10px 28px;border-radius:24px;border:1px solid rgba(255,255,255,.45);
background:rgba(255,255,255,.14);color:__BCOL__;font-size:14px;letter-spacing:2px;cursor:pointer}
</style></head><body>
<div class="scene">__HTML__</div>
<div class="brand"><h1>__BRAND__</h1><p>__SLOGAN__</p></div>
<button class="replay" onclick="location.reload()">重新播放</button>
</body></html>
"""

SCENES = []

# ---------- s55 灯塔夜航 ----------
SCENES.append(dict(
key="s55", title="灯塔夜航", brand="灯塔夜航", slogan="为你照亮前路",
bg="linear-gradient(180deg,#040816 0%,#0a1430 55%,#12224d 100%)", bcol="#fff",
css="""
.stars{position:absolute;inset:0;background-image:radial-gradient(circle,#fff 1.2px,transparent 1.7px),radial-gradient(circle,#fff 1px,transparent 1.5px),radial-gradient(circle,#cfe4ff 1.4px,transparent 1.9px);background-size:130px 110px,90px 150px,180px 100px;background-position:0 0,40px 60px,80px 20px;animation:tw 3s ease-in-out infinite alternate}
@keyframes tw{to{opacity:.3}}
.rock{position:absolute;bottom:118px;left:50%;transform:translateX(-50%);width:320px;height:100px;background:#080d20;border-radius:50% 50% 0 0/100% 100% 0 0}
.tower{position:absolute;bottom:170px;left:50%;transform:translateX(-50%);width:64px;height:230px;background:repeating-linear-gradient(180deg,#f2f4f8 0 26px,#d33a3a 26px 52px);clip-path:polygon(18% 0,82% 0,100% 100%,0 100%)}
.lamp{position:absolute;bottom:394px;left:50%;transform:translateX(-50%);width:46px;height:36px;background:#ffe9a8;border-radius:8px;box-shadow:0 0 42px 14px rgba(255,220,130,.55);animation:lamp 2.4s ease-in-out infinite}
@keyframes lamp{50%{box-shadow:0 0 64px 24px rgba(255,220,130,.8)}}
.roof{position:absolute;bottom:426px;left:50%;transform:translateX(-50%);width:0;height:0;border-left:36px solid transparent;border-right:36px solid transparent;border-bottom:32px solid #1a2340}
.beam{position:absolute;bottom:400px;left:50%;width:360px;height:74px;transform-origin:0 50%;background:linear-gradient(90deg,rgba(255,232,150,.8),transparent);clip-path:polygon(0 42%,100% 0,100% 100%,0 58%);animation:sweep 7s linear infinite}
@keyframes sweep{to{transform:rotate(360deg)}}
.sea{position:absolute;bottom:0;left:0;right:0;height:150px;background:linear-gradient(180deg,#0d1b3f,#060b1d)}
.wv{position:absolute;bottom:64px;left:-70px;width:570px;height:56px;background:rgba(100,150,255,.16);border-radius:46%;animation:wv 5s ease-in-out infinite alternate}
.wv.b{bottom:22px;animation-delay:-2.5s;background:rgba(100,150,255,.1)}
@keyframes wv{to{transform:translateX(56px)}}
""",
html="""<div class="stars"></div><div class="beam"></div><div class="rock"></div><div class="tower"></div><div class="lamp"></div><div class="roof"></div><div class="sea"><div class="wv"></div><div class="wv b"></div></div>"""))

# ---------- s56 热气球 ----------
clouds = "".join(
f'<div class="cl" style="top:{t}px;animation-duration:{d}s;animation-delay:{dl}s;transform:scale({s})"></div>'
for t, d, dl, s in [(120,26,-8,1),(220,34,-20,.7),(340,30,-2,1.2),(470,38,-28,.85),(580,26,-14,1.05)])
SCENES.append(dict(
key="s56", title="热气球", brand="热气球", slogan="乘风而起 拥抱天空",
bg="linear-gradient(180deg,#6ec1f5 0%,#bfe6fb 55%,#eaf8ff 100%)", bcol="#1a3a5c",
css="""
.sun{position:absolute;top:70px;right:56px;width:86px;height:86px;border-radius:50%;background:radial-gradient(circle at 38% 35%,#fff6c8,#ffd93d 65%,#ffb52e);box-shadow:0 0 50px 18px rgba(255,200,60,.5)}
.cl{position:absolute;left:-170px;width:130px;height:44px;background:#fff;border-radius:44px;opacity:.92;animation:drift linear infinite}
.cl::before{content:"";position:absolute;left:24px;top:-24px;width:56px;height:56px;background:#fff;border-radius:50%}
.cl::after{content:"";position:absolute;left:66px;top:-16px;width:42px;height:42px;background:#fff;border-radius:50%}
@keyframes drift{to{transform:translateX(640px)}}
.bln{position:absolute;left:50%;top:170px;transform:translateX(-50%);animation:bob 4.2s ease-in-out infinite}
@keyframes bob{50%{transform:translateX(-50%) translateY(-26px)}}
.env{width:172px;height:200px;margin:0 auto;background:repeating-linear-gradient(90deg,#ff6b6b 0 24px,#ffd93d 24px 48px,#6bcbff 48px 72px,#b78cff 72px 96px);border-radius:50% 50% 48% 48%/58% 58% 42% 42%;box-shadow:inset -20px -14px 0 rgba(0,0,0,.08)}
.neck{width:74px;height:42px;margin:-4px auto 0;background:#8a6d4a;clip-path:polygon(22% 0,78% 0,100% 100%,0 100%)}
.basket{width:58px;height:46px;margin:0 auto;background:linear-gradient(#b9835a,#8a5f3c);border-radius:6px 6px 14px 14px}
.bird{position:absolute;width:34px;height:12px;border:3px solid rgba(60,90,120,.7);border-color:rgba(60,90,120,.7) transparent transparent transparent;border-radius:50%;animation:bob 3s ease-in-out infinite}
""",
html=f"""<div class="sun"></div>{clouds}
<div class="bird" style="left:70px;top:420px"></div><div class="bird" style="left:330px;top:480px;animation-delay:-1.4s"></div>
<div class="bln"><div class="env"></div><div class="neck"></div><div class="basket"></div></div>"""))

# ---------- s57 雪夜 ----------
flakes = "".join(
f'<i class="sn" style="left:{l}px;width:{w}px;height:{w}px;animation-duration:{d}s;animation-delay:{dl}s;opacity:{o}"></i>'
for l, w, d, dl, o in [(20,7,9,-2,.9),(60,5,11,-7,.7),(105,8,8,-4,.95),(150,4,12,-9,.6),(195,6,10,-1,.85),(240,9,7.5,-5,1),(285,5,11,-3,.7),(330,7,9.5,-8,.9),(375,4,12,-6,.6),(410,6,10,-2,.8),(45,6,10.5,-5.5,.8),(130,9,8.5,-1.5,.95),(220,5,11.5,-7.5,.65),(310,8,9,-4.5,.9),(355,6,10,-9.5,.75),(90,4,12,-3.5,.6),(175,7,9,-6.5,.85),(265,5,11,-.5,.7)])
SCENES.append(dict(
key="s57", title="雪夜", brand="雪夜", slogan="万籁俱寂 唯雪有声",
bg="linear-gradient(180deg,#0b1230 0%,#1b2b5e 70%,#2c427f 100%)", bcol="#fff",
css="""
.moon{position:absolute;top:80px;right:60px;width:92px;height:92px;border-radius:50%;background:radial-gradient(circle at 36% 34%,#fffbe8,#e8ecf5 70%,#c9d2e8);box-shadow:0 0 60px 20px rgba(230,236,250,.25)}
.sn{position:absolute;top:-24px;border-radius:50%;background:#fff;animation:fall linear infinite}
@keyframes fall{to{transform:translateY(950px)}}
.pine{position:absolute;bottom:60px;width:0;height:0;border-left:58px solid transparent;border-right:58px solid transparent;border-bottom:150px solid #081230}
.pine::after{content:"";position:absolute;left:-58px;top:96px;border-left:58px solid transparent;border-right:58px solid transparent;border-bottom:44px solid rgba(220,232,250,.85)}
.gnd{position:absolute;bottom:-70px;left:-60px;width:550px;height:190px;background:#dfe8f5;border-radius:50%}
""",
html=f"""<div class="moon"></div>{flakes}
<div class="pine" style="left:36px"></div><div class="pine" style="left:150px;transform:scale(.72);transform-origin:bottom"></div><div class="pine" style="right:40px;transform:scale(1.15);transform-origin:bottom"></div>
<div class="gnd"></div>"""))

# ---------- s58 枫落 ----------
leaves = "".join(
f'<i class="lf" style="left:{l}px;animation-duration:{d}s;animation-delay:{dl}s;background:{c};width:{w}px;height:{w}px"></i>'
for l, d, dl, c, w in [(30,7,-1,"#d63c2f",26),(90,8.5,-4,"#e8762b",22),(150,7.5,-2.5,"#f2b134",28),(210,9,-6,"#d63c2f",24),(270,7,-3.5,"#c23b2e",26),(330,8,-5,"#e8762b",22),(390,7.5,-1.5,"#f2b134",28),(60,9,-7,"#e8762b",24),(180,7,-.5,"#d63c2f",26),(300,8.5,-3,"#f2b134",22),(240,7.5,-5.5,"#c23b2e",28),(120,8,-2,"#d63c2f",24)])
SCENES.append(dict(
key="s58", title="枫落", brand="枫落", slogan="一叶知秋 意满人间",
bg="linear-gradient(180deg,#ff9d5c 0%,#f2705c 60%,#c9504a 100%)", bcol="#fff",
css="""
.lf{position:absolute;top:-44px;border-radius:100% 6px 100% 6px;animation:lfFall linear infinite;box-shadow:inset -4px -4px 0 rgba(0,0,0,.12)}
@keyframes lfFall{to{transform:translateY(970px) rotate(560deg)}}
.pile{position:absolute;bottom:-60px;left:-60px;width:550px;height:170px;background:linear-gradient(#b3402f,#8f2f24);border-radius:50%}
.sun2{position:absolute;top:90px;left:50%;transform:translateX(-50%);width:110px;height:110px;border-radius:50%;background:radial-gradient(circle at 40% 38%,#fff3c0,#ffd93d 70%);box-shadow:0 0 70px 26px rgba(255,200,80,.45)}
""",
html=f"""<div class="sun2"></div>{leaves}<div class="pile"></div>"""))

# ---------- s59 蒲公英 ----------
spokes = "".join(f'<i style="transform:rotate({a}deg)"></i>' for a in range(0, 360, 15))
seeds = "".join(
f'<i class="sd {v}" style="left:{l}px;top:{t}px;animation-delay:{dl}s"></i>'
for l, t, dl, v in [(215,330,-1,"v1"),(215,330,-3,"v2"),(215,330,-5,"v3"),(215,330,-2.2,"v1"),(215,330,-4.4,"v2"),(215,330,-6,"v3")])
SCENES.append(dict(
key="s59", title="蒲公英", brand="蒲公英", slogan="风起时 奔赴下一场相遇",
bg="linear-gradient(180deg,#a8dcf2 0%,#d9f2e2 65%,#cde6c6 100%)", bcol="#2a5a3a",
css="""
.stem{position:absolute;left:50%;top:430px;width:6px;height:280px;margin-left:-3px;background:linear-gradient(#4d8f5f,#3a7048);border-radius:3px}
.head{position:absolute;left:50%;top:300px;width:130px;height:130px;margin-left:-65px}
.head i{position:absolute;left:50%;top:50%;width:2px;height:62px;margin-left:-1px;background:rgba(255,255,255,.95);transform-origin:50% 0}
.head i::after{content:"";position:absolute;top:-7px;left:50%;transform:translateX(-50%);width:9px;height:9px;border-radius:50%;background:#fff;box-shadow:0 0 8px #fff}
.core{position:absolute;left:50%;top:50%;width:26px;height:26px;margin:-13px 0 0 -13px;border-radius:50%;background:radial-gradient(circle at 40% 35%,#fff,#d8ecce)}
.sd{position:absolute;width:9px;height:9px;border-radius:50%;background:#fff;box-shadow:0 0 8px #fff;animation-duration:7s;animation-timing-function:linear;animation-iteration-count:infinite}
.sd.v1{animation-name:sd1}.sd.v2{animation-name:sd2}.sd.v3{animation-name:sd3}
@keyframes sd1{to{transform:translate(190px,-150px)}}
@keyframes sd2{to{transform:translate(-170px,-120px)}}
@keyframes sd3{to{transform:translate(120px,-190px)}}
.gnd2{position:absolute;bottom:-80px;left:-60px;width:550px;height:200px;background:#a9cf9a;border-radius:50%}
""",
html=f"""<div class="gnd2"></div><div class="stem"></div><div class="head">{spokes}<div class="core"></div></div>{seeds}"""))

# ---------- s60 蝶变 ----------
SCENES.append(dict(
key="s60", title="蝶变", brand="蝶变", slogan="破茧之日 光华初绽",
bg="linear-gradient(180deg,#33255a 0%,#6b4a8f 60%,#a87bc0 100%)", bcol="#fff",
css="""
.thread{position:absolute;top:0;left:50%;width:3px;height:190px;margin-left:-1.5px;background:rgba(220,200,170,.7)}
.coc{position:absolute;top:180px;left:50%;transform:translateX(-50%);width:56px;height:94px;background:linear-gradient(180deg,#9a7f56,#5e4a30);border-radius:50%;box-shadow:inset -8px -6px 0 rgba(0,0,0,.18)}
.bf{position:absolute;left:50%;top:430px;animation:rise 6s ease-in-out infinite}
@keyframes rise{0%,100%{transform:translate(-50%,0)}50%{transform:translate(-50%,-64px)}}
.wing{position:absolute;top:0;width:58px;height:76px;background:linear-gradient(135deg,#ff9d da,#c86bff);background:linear-gradient(135deg,#ff9dda,#c86bff);animation:flap .55s ease-in-out infinite alternate}
.wing.l{left:-58px;border-radius:50% 50% 50% 50%/62% 62% 38% 38%;transform-origin:right center}
.wing.r{left:0;border-radius:50% 50% 50% 50%/62% 62% 38% 38%;transform-origin:left center;animation-name:flapR}
@keyframes flap{to{transform:scaleX(.22)}}
@keyframes flapR{to{transform:scaleX(.22)}}
.bd2{position:absolute;left:-4px;top:8px;width:8px;height:66px;background:#2e2044;border-radius:4px}
.ant{position:absolute;top:2px;width:2px;height:22px;background:#2e2044}
.ant.l{left:-2px;transform:rotate(-18deg);transform-origin:bottom}
.ant.r{left:6px;transform:rotate(18deg);transform-origin:bottom}
.spk{position:absolute;border-radius:50%;background:#ffe9a8;box-shadow:0 0 10px #ffe9a8;animation:tw2 2.2s ease-in-out infinite alternate}
@keyframes tw2{to{opacity:.15;transform:scale(.7)}}
""",
html="""<div class="thread"></div><div class="coc"></div>
<div class="spk" style="left:90px;top:300px;width:8px;height:8px"></div>
<div class="spk" style="left:320px;top:360px;width:6px;height:6px;animation-delay:-1s"></div>
<div class="spk" style="left:250px;top:600px;width:9px;height:9px;animation-delay:-.5s"></div>
<div class="bf"><div class="wing l"></div><div class="wing r"></div><div class="bd2"></div><div class="ant l"></div><div class="ant r"></div></div>"""))
