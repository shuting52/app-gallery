#!/usr/bin/env python3
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

# ---------- s61 萤火之森 ----------
ffs = "".join(
f'<i class="ff" style="left:{l}px;top:{t}px;animation-delay:{d1}s,{d2}s"></i>'
for l, t, d1, d2 in [(60,420,-.4,-2),(120,520,-1.2,-5),(200,380,-2,-1),(280,470,-.8,-7),(340,400,-1.6,-3),(90,600,-2.4,-4),(170,650,-.2,-6),(250,590,-1,-2.5),(320,630,-2.2,-5.5),(45,500,-1.4,-3.5),(380,540,-.6,-6.5),(140,440,-2.8,-1.5),(230,680,-1.8,-4.5),(300,350,-.9,-2.2),(65,670,-2.6,-5.8),(355,470,-1.1,-.8)])
SCENES.append(dict(
key="s61", title="萤火之森", brand="萤火之森", slogan="微光成炬 照亮长夜",
bg="linear-gradient(180deg,#04140c 0%,#0a2a18 70%,#0e3a22 100%)", bcol="#e8ffd0",
css="""
.mglow{position:absolute;top:60px;left:50%;transform:translateX(-50%);width:200px;height:200px;border-radius:50%;background:radial-gradient(circle,rgba(220,255,180,.22),transparent 70%)}
.trunk{position:absolute;bottom:0;width:34px;background:#020a06;border-radius:12px}
.canopy{position:absolute;border-radius:50%;background:#03130b}
.ff{position:absolute;width:7px;height:7px;border-radius:50%;background:#d8ff7a;box-shadow:0 0 12px 4px rgba(216,255,122,.75);animation:blink 2.6s ease-in-out infinite,drift 9s ease-in-out infinite alternate}
@keyframes blink{0%,100%{opacity:.12}50%{opacity:1}}
@keyframes drift{to{transform:translate(34px,-44px)}}
.gnd3{position:absolute;bottom:-70px;left:-60px;width:550px;height:180px;background:#04180e;border-radius:50%}
""",
html=f"""<div class="mglow"></div>
<div class="trunk" style="left:60px;height:340px"></div><div class="canopy" style="left:-10px;top:180px;width:180px;height:150px"></div>
<div class="trunk" style="right:70px;height:420px"></div><div class="canopy" style="right:-16px;top:120px;width:200px;height:170px"></div>
<div class="trunk" style="left:190px;height:280px"></div><div class="canopy" style="left:130px;top:260px;width:150px;height:120px"></div>
{ffs}<div class="gnd3"></div>"""))

# ---------- s62 深海水母 ----------
tens = "".join(
f'<i class="ten" style="left:{l}px;animation-delay:{d}s;height:{h}px"></i>'
for l, d, h in [(24,-.2,110),(44,-1.1,130),(64,-.6,100),(84,-1.5,125),(104,-.9,110),(40,-.4,120),(74,-1.3,105)])
bubbles = "".join(
f'<i class="bb" style="left:{l}px;width:{w}px;height:{w}px;animation-duration:{du}s;animation-delay:{dl}s"></i>'
for l, w, du, dl in [(80,10,7,-2),(150,7,9,-5),(260,12,8,-1),(330,8,10,-6),(200,6,7.5,-3.5),(380,9,8.5,-4)])
SCENES.append(dict(
key="s62", title="深海水母", brand="深海水母", slogan="深蓝之下 自在浮游",
bg="linear-gradient(180deg,#02182e 0%,#063a63 60%,#0a4f86 100%)", bcol="#dff2ff",
css="""
.ray{position:absolute;top:-40px;width:120px;height:500px;background:linear-gradient(rgba(160,210,255,.14),transparent);transform:skewX(-14deg)}
.jf{position:absolute;left:50%;top:290px;width:130px;margin-left:-65px;animation:rise 8s ease-in-out infinite}
@keyframes rise{50%{transform:translateY(-72px)}}
.dome{width:130px;height:82px;margin:0 auto;background:radial-gradient(circle at 50% 100%,rgba(255,180,220,.95),rgba(255,120,180,.5) 60%,rgba(255,120,180,.12));border-radius:65px 65px 14px 14px;animation:pulse 2.2s ease-in-out infinite;transform-origin:50% 100%}
@keyframes pulse{50%{transform:scaleY(.8) scaleX(1.07)}}
.ten{position:absolute;top:78px;width:5px;background:linear-gradient(rgba(255,160,200,.85),transparent);border-radius:3px;animation:sway 2.6s ease-in-out infinite alternate;transform-origin:top center;display:block}
@keyframes sway{to{transform:rotate(9deg)}}
.bb{position:absolute;bottom:-30px;border-radius:50%;background:rgba(180,220,255,.35);animation:bbUp linear infinite}
@keyframes bbUp{to{transform:translateY(-980px)}}
.jf2{position:absolute;left:70px;top:560px;width:80px;opacity:.7;animation:rise 10s ease-in-out infinite;animation-delay:-4s}
.jf2 .dome{width:80px;height:52px}
""",
html=f"""<div class="ray" style="left:60px"></div><div class="ray" style="left:250px;animation-delay:-2s"></div>
{bubbles}
<div class="jf"><div class="dome"></div>{tens}</div>
<div class="jf2"><div class="dome"></div></div>"""))

# ---------- s63 冰川纪 ----------
sparks = "".join(
f'<i class="sp" style="left:{l}px;top:{t}px;animation-delay:{d}s"></i>'
for l, t, d in [(70,200,-.5),(160,140,-1.4),(250,220,-.9),(340,160,-1.9),(110,320,-.2),(300,330,-1.1),(200,260,-1.6),(380,280,-.7)])
SCENES.append(dict(
key="s63", title="冰川纪", brand="冰川纪", slogan="纯净之境 万物澄明",
bg="linear-gradient(180deg,#a8d4ef 0%,#e8f4fb 55%,#ffffff 100%)", bcol="#2a6a9a",
css="""
.csun{position:absolute;top:80px;left:50%;transform:translateX(-50%);width:100px;height:100px;border-radius:50%;background:radial-gradient(circle at 40% 38%,#ffffff,#dceefb 70%);box-shadow:0 0 60px 22px rgba(255,255,255,.8)}
.m1{position:absolute;bottom:170px;left:-50px;width:310px;height:300px;background:linear-gradient(180deg,#ffffff,#b9d6ea);clip-path:polygon(50% 0,100% 100%,0 100%)}
.m2{position:absolute;bottom:170px;right:-60px;width:280px;height:240px;background:linear-gradient(180deg,#f2f8fd,#a9c8e2);clip-path:polygon(50% 0,100% 100%,0 100%)}
.ice{position:absolute;bottom:-90px;left:-60px;width:550px;height:220px;background:linear-gradient(#eef6fc,#d5e7f4);border-radius:50%}
.sp{position:absolute;width:6px;height:6px;border-radius:50%;background:#fff;box-shadow:0 0 10px #bfe0ff;animation:tw2 2s ease-in-out infinite alternate}
@keyframes tw2{to{opacity:.2;transform:scale(.6)}}
.cr{position:absolute;width:44px;height:44px;background:rgba(190,225,250,.5);border:2px solid rgba(255,255,255,.9);transform:rotate(45deg);animation:float 5s ease-in-out infinite alternate}
@keyframes float{to{transform:rotate(45deg) translateY(-18px)}}
""",
html=f"""<div class="csun"></div>{sparks}
<div class="m1"></div><div class="m2"></div><div class="ice"></div>
<div class="cr" style="left:80px;bottom:120px"></div>
<div class="cr" style="right:90px;bottom:90px;animation-delay:-2.5s;transform:scale(.7) rotate(45deg)"></div>"""))

# ---------- s64 沙漠驼铃 ----------
sands = "".join(
f'<i class="sdp" style="top:{t}px;animation-duration:{d}s;animation-delay:{dl}s"></i>'
for t, d, dl in [(420,7,-1),(460,9,-4),(500,8,-2.5),(540,10,-6),(580,7.5,-3),(620,9,-5.5)])
SCENES.append(dict(
key="s64", title="沙漠驼铃", brand="沙漠驼铃", slogan="大漠孤烟 长河落日",
bg="linear-gradient(180deg,#ffb75d 0%,#f79d4a 55%,#e07f3c 100%)", bcol="#5e3410",
css="""
.dsun{position:absolute;top:150px;left:50%;transform:translateX(-50%);width:130px;height:130px;border-radius:50%;background:radial-gradient(circle at 42% 38%,#fff2c0,#ffcf5e 70%);box-shadow:0 0 80px 30px rgba(255,190,90,.55)}
.dune{position:absolute;left:-80px;width:590px;border-radius:50%}
.d1{bottom:-150px;height:320px;background:#d98a3e}
.d2{bottom:-190px;height:280px;background:#c1762f}
.sdp{position:absolute;left:-20px;width:5px;height:5px;border-radius:50%;background:rgba(255,235,200,.8);animation:sand linear infinite}
@keyframes sand{to{transform:translateX(480px)}}
.bellw{position:absolute;top:330px;left:50%;margin-left:-27px;transform-origin:50% 0;animation:swing 3.2s ease-in-out infinite}
@keyframes swing{0%,100%{transform:rotate(13deg)}50%{transform:rotate(-13deg)}}
.string{width:3px;height:30px;background:#6b4a20;margin:0 auto}
.bell{width:56px;height:50px;background:linear-gradient(180deg,#f0c05a,#b57e22);border-radius:10px 10px 28px 28px;margin:0 auto;position:relative;box-shadow:0 6px 18px rgba(90,50,10,.35)}
.bell::after{content:"";position:absolute;bottom:-11px;left:50%;transform:translateX(-50%);width:17px;height:17px;border-radius:50%;background:#7a5518}
.bell::before{content:"";position:absolute;top:14px;left:50%;transform:translateX(-50%);width:30px;height:12px;border-radius:6px;background:rgba(255,240,200,.5)}
""",
html=f"""{sands}<div class="dsun"></div><div class="dune d2"></div><div class="dune d1"></div>
<div class="bellw"><div class="string"></div><div class="bell"></div></div>"""))

# ---------- s65 竹林听雨 ----------
drops = "".join(
f'<i class="rn" style="left:{l}px;animation-duration:{d}s;animation-delay:{dl}s"></i>'
for l, d, dl in [(30,.9,-.2),(70,1.1,-.7),(110,.85,-.4),(150,1,-.9),(190,.9,-.1),(230,1.05,-.6),(270,.9,-.8),(310,1.1,-.3),(350,.85,-.5),(390,1,-.65),(50,1,-.45),(130,.9,-.75),(210,1.05,-.25),(290,.9,-.55),(370,1.1,-.85),(95,.95,-.15),(175,1,-.95),(255,.9,-.35),(335,1.05,-.7),(405,.9,-.5)])
SCENES.append(dict(
key="s65", title="竹林听雨", brand="竹林听雨", slogan="雨打新篁 万竿生烟",
bg="linear-gradient(180deg,#2c6b4e 0%,#4d8f66 60%,#77b183 100%)", bcol="#fff",
css="""
.bam{position:absolute;bottom:0;width:26px;background:repeating-linear-gradient(180deg,transparent 0 64px,rgba(30,70,40,.55) 64px 68px),linear-gradient(90deg,#3c7a4b,#63a873,#3c7a4b);border-radius:13px}
.lvs{position:absolute;width:64px;height:30px;background:radial-gradient(ellipse,#5fae72,#3c7a4b);border-radius:50%;transform:rotate(-24deg)}
.rn{position:absolute;top:-46px;width:2px;height:36px;background:linear-gradient(transparent,rgba(225,242,255,.9));animation:rainFall linear infinite;display:block}
@keyframes rainFall{to{transform:translateY(970px)}}
.mist{position:absolute;bottom:-60px;left:-60px;width:550px;height:170px;background:rgba(230,245,235,.28);border-radius:50%;filter:blur(10px)}
""",
html=f"""{drops}
<div class="bam" style="left:60px;height:560px"></div><div class="lvs" style="left:30px;top:300px"></div><div class="lvs" style="left:66px;top:230px;transform:rotate(20deg)"></div>
<div class="bam" style="left:180px;height:680px"></div><div class="lvs" style="left:150px;top:180px"></div><div class="lvs" style="left:186px;top:120px;transform:rotate(18deg)"></div>
<div class="bam" style="left:320px;height:520px"></div><div class="lvs" style="left:290px;top:340px"></div>
<div class="mist"></div>"""))

# ---------- s66 荷塘月色 ----------
petals = "".join(
f'<i class="pet" style="transform:rotate({a}deg)"></i>' for a in (-54, -36, -18, 0, 18, 36, 54))
SCENES.append(dict(
key="s66", title="荷塘月色", brand="荷塘月色", slogan="月下荷香 梦入江南",
bg="linear-gradient(180deg,#0a1030 0%,#16245c 55%,#1e3a7d 100%)", bcol="#eaf2ff",
css="""
.moon2{position:absolute;top:70px;left:50%;transform:translateX(-50%);width:96px;height:96px;border-radius:50%;background:radial-gradient(circle at 38% 34%,#fffbe8,#e6ecf8 70%,#c3cde8);box-shadow:0 0 60px 20px rgba(230,236,250,.22)}
.mref{position:absolute;top:420px;left:50%;transform:translateX(-50%);width:120px;height:200px;background:linear-gradient(rgba(240,244,252,.28),transparent);filter:blur(8px);border-radius:50%}
.water{position:absolute;bottom:0;left:0;right:0;height:330px;background:linear-gradient(180deg,#14265e,#0a1740)}
.leaf{position:absolute;border-radius:50%;background:radial-gradient(circle at 35% 30%,#63c47e,#2c7a4c);box-shadow:inset -6px -6px 0 rgba(0,0,0,.12)}
.fl{position:absolute;left:50%;top:470px;width:120px;height:90px;margin-left:-60px}
.pet{position:absolute;left:50%;bottom:0;width:34px;height:58px;margin-left:-17px;background:linear-gradient(#ffd9e8,#f78fb8);border-radius:50% 50% 50% 50%/72% 72% 28% 28%;transform-origin:50% 100%}
.pod{position:absolute;left:50%;bottom:6px;width:26px;height:26px;margin-left:-13px;border-radius:50%;background:radial-gradient(circle at 40% 35%,#ffe98a,#d9a83c)}
.rp{position:absolute;border:2px solid rgba(165,205,255,.55);border-radius:50%;animation:rp 3.6s ease-out infinite}
@keyframes rp{from{width:24px;height:12px;opacity:.85}to{width:170px;height:48px;opacity:0}}
""",
html=f"""<div class="moon2"></div><div class="water"></div><div class="mref"></div>
<div class="leaf" style="left:50px;top:520px;width:110px;height:44px"></div>
<div class="leaf" style="right:60px;top:600px;width:130px;height:52px"></div>
<div class="leaf" style="left:120px;top:660px;width:90px;height:36px"></div>
<div class="fl">{petals}<div class="pod"></div></div>
<div class="rp" style="left:50%;top:560px;margin-left:-12px;animation-delay:0s"></div>
<div class="rp" style="left:50%;top:560px;margin-left:-12px;animation-delay:-1.8s"></div>"""))

# ---------- s67 樱吹雪 ----------
petals2 = "".join(
f'<i class="pt" style="left:{l}px;animation-duration:{d}s;animation-delay:{dl}s;background:{c}"></i>'
for l, d, dl, c in [(25,8,-1,"#ffb9d2"),(70,9.5,-4,"#f78fb8"),(115,8.5,-2,"#ffc9dd"),(160,10,-6,"#ffb9d2"),(205,8,-3,"#f78fb8"),(250,9,-5,"#ffc9dd"),(295,8.5,-1.5,"#ffb9d2"),(340,10,-7,"#f78fb8"),(385,9,-3.5,"#ffc9dd"),(50,8,-5.5,"#ffb9d2"),(140,9.5,-2.5,"#f78fb8"),(230,8,-6.5,"#ffc9dd"),(320,9,-4.5,"#ffb9d2"),(95,10,-3,"#ffc9dd"),(275,8.5,-7.5,"#f78fb8"),(365,9,-2,"#ffb9d2")])
SCENES.append(dict(
key="s67", title="樱吹雪", brand="樱吹雪", slogan="花瓣为信 春风作笺",
bg="linear-gradient(180deg,#ffe3ec 0%,#ffd0e0 55%,#ffc2d6 100%)", bcol="#a34a6e",
css="""
.branch{position:absolute;top:60px;right:-40px;width:300px;height:44px;background:linear-gradient(#5a3a2e,#3e2a22);border-radius:22px;transform:rotate(24deg)}
.branch::before{content:"";position:absolute;left:40px;top:-70px;width:26px;height:110px;background:linear-gradient(#5a3a2e,#3e2a22);border-radius:13px;transform:rotate(-38deg)}
.blos{position:absolute;width:26px;height:26px;border-radius:50%;background:radial-gradient(circle,#ffd9e6 30%,#f78fb8 75%)}
.pt{position:absolute;top:-30px;width:21px;height:16px;border-radius:80% 12% 80% 12%;animation:petFall linear infinite;display:block}
@keyframes petFall{to{transform:translateY(960px) translateX(70px) rotate(420deg)}}
.gndp{position:absolute;bottom:-70px;left:-60px;width:550px;height:180px;background:#f7b8cd;border-radius:50%}
""",
html=f"""<div class="branch"></div>
<div class="blos" style="left:200px;top:120px"></div><div class="blos" style="left:250px;top:180px;transform:scale(.8)"></div><div class="blos" style="left:150px;top:200px;transform:scale(1.2)"></div><div class="blos" style="left:290px;top:110px;transform:scale(.7)"></div>
{petals2}<div class="gndp"></div>"""))

# ---------- s68 银河漫游 ----------
SCENES.append(dict(
key="s68", title="银河漫游", brand="银河漫游", slogan="把星辰 折进梦里",
bg="#040614", bcol="#e8ecff",
css="""
.mw{position:absolute;top:120px;left:-140px;width:720px;height:230px;background:linear-gradient(90deg,transparent,rgba(170,195,255,.26),rgba(215,195,255,.3),rgba(170,195,255,.26),transparent);filter:blur(16px);transform:rotate(-24deg)}
.stars2{position:absolute;inset:0;background-image:radial-gradient(circle,#fff 1.3px,transparent 1.8px),radial-gradient(circle,#cfe0ff 1px,transparent 1.5px);background-size:120px 130px,80px 100px;background-position:10px 30px,50px 80px;animation:tw 2.8s ease-in-out infinite alternate}
@keyframes tw{to{opacity:.35}}
.st{position:absolute;top:150px;left:0;width:130px;height:2px;background:linear-gradient(90deg,transparent,#fff);border-radius:2px;transform:rotate(-24deg);animation:shoot 4.6s linear infinite}
@keyframes shoot{0%{transform:translate(440px,200px) rotate(-24deg);opacity:0}6%{opacity:1}28%{transform:translate(-150px,-70px) rotate(-24deg);opacity:0}100%{transform:translate(-150px,-70px) rotate(-24deg);opacity:0}}
.pl{position:absolute;left:90px;top:560px;width:90px;height:90px;border-radius:50%;background:radial-gradient(circle at 35% 32%,#ffd9a8,#e8935c 65%,#a85f2e);box-shadow:0 0 40px rgba(232,147,92,.5)}
.ring{position:absolute;left:48px;top:596px;width:174px;height:44px;border:7px solid rgba(255,220,170,.65);border-radius:50%;transform:rotate(-18deg)}
""",
html="""<div class="mw"></div><div class="stars2"></div><div class="st" style="animation-delay:-1.5s"></div><div class="st" style="top:260px;animation-delay:-3.4s"></div><div class="pl"></div><div class="ring"></div>"""))

# ---------- s69 一飞冲天 ----------
smokes = "".join(
f'<i class="sm" style="left:{l}px;bottom:{b}px;width:{w}px;height:{w}px;animation-delay:{dl}s"></i>'
for l, b, dl, w in [(150,180,-.4,46),(200,160,-1.2,60),(250,180,-2,52),(180,150,-1.8,66),(230,165,-.8,44)])
SCENES.append(dict(
key="s69", title="一飞冲天", brand="一飞冲天", slogan="心怀山海 眼有星辰",
bg="linear-gradient(180deg,#0b1e4b 0%,#2a5db0 55%,#7db9e8 100%)", bcol="#fff",
css="""
.cld{position:absolute;background:rgba(255,255,255,.85);border-radius:40px;animation:drift linear infinite}
@keyframes drift{from{transform:translateX(-180px)}to{transform:translateX(480px)}}
.rk{position:absolute;left:50%;bottom:300px;transform:translateX(-50%);animation:hover 3.4s ease-in-out infinite}
@keyframes hover{50%{transform:translate(-50%,-34px)}}
.rbody{width:76px;height:172px;margin:0 auto;background:linear-gradient(90deg,#d7dfe9,#ffffff 45%,#c3cfdd);border-radius:50% 50% 46% 46%/40% 40% 28% 28%;position:relative}
.win{position:absolute;top:54px;left:50%;transform:translateX(-50%);width:36px;height:36px;border-radius:50%;background:radial-gradient(circle at 35% 35%,#aee0ff,#2a6fb0);border:5px solid #8a97a8}
.fin{position:absolute;bottom:8px;width:32px;height:62px;background:#e14b4b}
.fin.l{left:-25px;clip-path:polygon(100% 0,100% 100%,0 100%)}
.fin.r{right:-25px;clip-path:polygon(0 0,0 100%,100% 100%)}
.flame{width:36px;height:74px;margin:3px auto 0;background:linear-gradient(#ffe27a,#ff9d3c 60%,rgba(255,120,40,0));border-radius:50% 50% 50% 50%/28% 28% 72% 72%;animation:flick .18s ease-in-out infinite alternate;transform-origin:top center}
@keyframes flick{to{transform:scaleY(1.28) scaleX(.9)}}
.sm{position:absolute;border-radius:50%;background:rgba(255,255,255,.8);filter:blur(7px);animation:smRise 2.8s ease-out infinite}
@keyframes smRise{from{transform:translateY(0) scale(.55);opacity:.9}to{transform:translateY(-170px) scale(1.7);opacity:0}}
""",
html=f"""<div class="cld" style="top:140px;width:110px;height:34px;animation-duration:30s"></div>
<div class="cld" style="top:640px;width:140px;height:40px;animation-duration:38s;animation-delay:-14s"></div>
{smokes}
<div class="rk"><div class="rbody"><div class="win"></div><div class="fin l"></div><div class="fin r"></div></div><div class="flame"></div></div>"""))

# ---------- s70 摩天轮 ----------
spokes3 = "".join(f'<i class="spoke" style="transform:rotate({a}deg)"></i>' for a in (0, 45, 90, 135))
import math
cabs = "".join(
f'<div class="cab" style="left:{150+138*math.cos(math.radians(a)):.0f}px;top:{150+138*math.sin(math.radians(a)):.0f}px"><div class="cabin" style="background:linear-gradient({c})"></div></div>'
for a, c in [(0,"#ffd93d,#ff9d3c"),(45,"#ff8fb8,#e14b7a"),(90,"#7dc9ff,#2a7fd0"),(135,"#9dffb0,#3cb56e"),(180,"#d0a8ff,#8a5cd6"),(225,"#ffb27d,#e07f3c"),(270,"#8ef0e2,#2ea89a"),(315,"#ff9d9d,#d64545")])
SCENES.append(dict(
key="s70", title="摩天轮", brand="摩天轮", slogan="兜兜转转 皆是风景",
bg="linear-gradient(180deg,#2b1a4e 0%,#7a3f8f 55%,#e88ca0 100%)", bcol="#ffe9f2",
css="""
.gndd{position:absolute;bottom:0;left:0;right:0;height:120px;background:#1d1030}
.leg{position:absolute;bottom:110px;width:26px;height:330px;background:linear-gradient(#3a2450,#241436)}
.leg.l{left:150px;transform:rotate(14deg);transform-origin:bottom}
.leg.r{right:150px;transform:rotate(-14deg);transform-origin:bottom}
.wheel{position:absolute;left:50%;top:180px;width:300px;height:300px;margin-left:-150px;animation:spin 24s linear infinite}
@keyframes spin{to{transform:rotate(360deg)}}
.rim{position:absolute;inset:0;border:10px solid rgba(255,255,255,.9);border-radius:50%;box-shadow:0 0 30px rgba(255,200,220,.5)}
.spoke{position:absolute;left:50%;top:50%;width:6px;height:292px;margin:-146px 0 0 -3px;background:rgba(255,255,255,.55);display:block}
.hub{position:absolute;left:50%;top:50%;width:34px;height:34px;margin:-17px 0 0 -17px;border-radius:50%;background:radial-gradient(circle at 38% 35%,#fff,#e8b8d0);box-shadow:0 0 20px rgba(255,220,235,.8)}
.cab{position:absolute;width:36px;height:32px;margin:-16px 0 0 -18px}
.cabin{width:100%;height:100%;border-radius:9px;animation:spinRev 24s linear infinite;box-shadow:0 4px 10px rgba(0,0,0,.3)}
@keyframes spinRev{to{transform:rotate(-360deg)}}
""",
html=f"""<div class="gndd"></div><div class="leg l"></div><div class="leg r"></div>
<div class="wheel"><div class="rim"></div>{spokes3}<div class="hub"></div>{cabs}</div>"""))

# ---------- s71 孔明灯 ----------
lans = "".join(
f'<div class="ln" style="left:{l}px;animation-duration:{d}s;animation-delay:{dl}s"><div class="lbody" style="width:{w}px;height:{h}px;animation-delay:{dl2}s"></div></div>'
for l, d, dl, w, h, dl2 in [(40,12,-2,52,62,-.5),(120,14,-7,64,76,-1.8),(210,11,-4,48,56,-1),(300,15,-9,70,84,-2.4),(370,12,-6,54,64,-.9),(170,16,-11,60,72,-2.9),(260,13,-3,46,54,-1.5),(80,15,-8,58,68,-2.1)])
SCENES.append(dict(
key="s71", title="孔明灯", brand="孔明灯", slogan="一盏心愿 直上青云",
bg="linear-gradient(180deg,#050818 0%,#0e1a3f 65%,#1a2c5e 100%)", bcol="#ffe9c8",
css="""
.stars3{position:absolute;inset:0;background-image:radial-gradient(circle,#fff 1.1px,transparent 1.6px);background-size:110px 120px;animation:tw 3.4s ease-in-out infinite alternate}
@keyframes tw{to{opacity:.4}}
.ln{position:absolute;bottom:-100px;animation-name:rise;animation-timing-function:linear;animation-iteration-count:infinite}
@keyframes rise{to{transform:translateY(-1090px)}}
.lbody{background:radial-gradient(circle at 50% 32%,#ffedbb,#ff9d4d 68%,#dd7c2c);border-radius:46% 46% 48% 48%/38% 38% 62% 62%;box-shadow:0 0 34px 10px rgba(255,170,80,.5);position:relative;animation:sway2 3.2s ease-in-out infinite alternate}
@keyframes sway2{to{transform:translateX(30px)}}
.lbody::before{content:"";position:absolute;top:-9px;left:50%;transform:translateX(-50%);width:60%;height:11px;background:#8a5a2a;border-radius:5px}
""",
html=f"""<div class="stars3"></div>{lans}"""))

# ---------- s72 剪纸迎春 ----------
bloms = "".join(
f'<i class="bl" style="left:{l}px;top:{t}px;transform:scale({s})"></i>'
for l, t, s in [(70,140,.9),(330,170,1.1),(50,560,1),(360,540,.8),(110,640,1.2),(300,660,.9)])
fpets = "".join(
f'<i class="fp" style="left:{l}px;animation-duration:{d}s;animation-delay:{dl}s"></i>'
for l, d, dl in [(60,8,-1),(140,9.5,-4),(220,8,-2.5),(300,10,-6),(370,9,-3.5),(100,8.5,-5.5),(260,9,-7),(340,8,-2)])
SCENES.append(dict(
key="s72", title="剪纸迎春", brand="剪纸迎春", slogan="剪出春光 迎来新岁",
bg="#c0272d", bcol="#fff8ee",
css="""
.trim{position:absolute;left:0;right:0;height:28px;background:repeating-linear-gradient(45deg,rgba(255,248,238,.95) 0 14px,transparent 14px 28px)}
.trim.t{top:0}.trim.b{bottom:0}
.win{position:absolute;left:50%;top:170px;width:300px;height:300px;margin-left:-150px;background:#fff8ee;border-radius:50%;box-shadow:0 0 0 16px rgba(255,248,238,.22),0 0 70px rgba(0,0,0,.3)}
.chun{position:absolute;left:50%;top:212px;width:216px;height:216px;margin-left:-108px;background:#c0272d;border-radius:50%}
.chun span{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font-size:118px;font-weight:800;color:#fff8ee;animation:glow 2.6s ease-in-out infinite}
@keyframes glow{50%{text-shadow:0 0 34px rgba(255,220,150,.95)}}
.bl{position:absolute;width:20px;height:20px;border-radius:50%;background:radial-gradient(circle,#ffe4ec 30%,#f78fb8 75%);box-shadow:0 0 8px rgba(255,180,205,.8)}
.fp{position:absolute;top:-24px;width:13px;height:13px;border-radius:80% 12% 80% 12%;background:#ffd9e4;animation:fpFall linear infinite;display:block}
@keyframes fpFall{to{transform:translateY(950px) rotate(380deg)}}
""",
html=f"""<div class="trim t"></div><div class="trim b"></div>
<div class="win"></div><div class="chun"><span>春</span></div>
{bloms}{fpets}"""))

# ---------- runner ----------
import json
# 修复 s60 的笔误行
for sc in SCENES:
    if sc["key"] == "s60":
        sc["css"] = sc["css"].replace("background:linear-gradient(135deg,#ff9d da,#c86bff);", "")
assert len(SCENES) == 18, len(SCENES)
titles = []
for sc in SCENES:
    page = TPL.replace("__TITLE__", sc["title"]).replace("__BG__", sc["bg"]) \
        .replace("__CSS__", sc["css"]).replace("__HTML__", sc["html"]) \
        .replace("__BCOL__", sc["bcol"]).replace("__BRAND__", sc["brand"]) \
        .replace("__SLOGAN__", sc["slogan"])
    fn = os.path.join(OUT, sc["key"] + ".html")
    open(fn, "w", encoding="utf-8").write(page)
    titles.append({"file": sc["key"] + ".html", "title": sc["title"]})
json.dump(titles, open(os.path.join(OUT, "_titles_splash_d.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
print("wrote", len(titles), "files + _titles_splash_d.json")
print([t["title"] for t in titles])
