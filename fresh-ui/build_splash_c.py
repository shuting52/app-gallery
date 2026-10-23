#!/usr/bin/env python3
"""生成 s37-s54 启动页（C 组，18 组）"""
import json, os

BASE = """*{margin:0;padding:0;box-sizing:border-box}
html,body{height:100%}
body{background:#070a12;display:flex;align-items:center;justify-content:center;font-family:-apple-system,"PingFang SC","Microsoft YaHei",sans-serif;overflow:hidden}
.stage{position:relative;width:430px;height:900px;flex:none;overflow:hidden}
.stage i{display:block;position:absolute}
.brand{position:absolute;left:0;right:0;bottom:104px;text-align:center;z-index:50;animation:brandIn 1s .9s both}
.brand h1{font-size:32px;letter-spacing:10px;text-indent:10px;color:#fff;font-weight:700;text-shadow:0 2px 24px rgba(0,0,0,.45)}
.brand p{margin-top:10px;font-size:11px;letter-spacing:5px;color:rgba(255,255,255,.62)}
@keyframes brandIn{from{opacity:0;transform:translateY(18px)}to{opacity:1;transform:none}}
.replay{position:absolute;bottom:30px;left:50%;transform:translateX(-50%);z-index:60;background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.35);color:#fff;font-size:12px;letter-spacing:2px;padding:9px 24px;border-radius:20px;cursor:pointer;backdrop-filter:blur(6px);-webkit-backdrop-filter:blur(6px)}
.shade{position:absolute;left:0;right:0;bottom:0;height:360px;background:linear-gradient(transparent,rgba(8,6,18,.78));z-index:40;pointer-events:none}
"""

TPL = """<!DOCTYPE html>
<html lang="zh-CN"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>__TITLE__</title>
<style>
""" + BASE + """
.stage{background:__BG__}
__CSS__
</style></head><body>
<div class="stage" id="stage">
__HTML__
<div class="shade"></div>
<div class="brand"><h1>__BRAND__</h1><p>__SUB__</p></div>
<button class="replay" onclick="var s=document.getElementById('stage');s.replaceWith(s.cloneNode(true))">重新播放</button>
</div>
</body></html>"""

D = []

# ---------- s37 蜂鸟掠影 ----------
D.append(dict(file="s37.html", title="蜂鸟掠影", brand="蜂鸟", sub="HUMMINGBIRD",
bg="linear-gradient(#131b3a 0%,#3c2f5e 42%,#a3543f 66%,#e8935a 80%,#241c38 100%)",
css="""
.sun{width:130px;height:130px;left:150px;top:300px;border-radius:50%;background:radial-gradient(circle at 50% 50%,#ffe9b8,#ffb35c 58%,rgba(255,179,92,0) 72%);animation:sunGlow 3s ease-in-out infinite alternate}
@keyframes sunGlow{to{transform:scale(1.1);opacity:.9}}
.bird{width:96px;height:64px;left:236px;top:290px;z-index:5;animation:hover 1.5s ease-in-out infinite alternate}
@keyframes hover{to{transform:translateY(-16px)}}
.bird .bd{width:58px;height:30px;left:18px;top:17px;border-radius:50%;background:linear-gradient(135deg,#46e6c8,#14808f)}
.bird .bk{width:28px;height:8px;left:70px;top:24px;border-radius:0 9px 9px 0;background:#f4d35e}
.bird .eye{width:7px;height:7px;left:58px;top:22px;border-radius:50%;background:#0e2028}
.wing{width:66px;height:26px;top:4px;border-radius:50%;background:radial-gradient(circle at 50% 50%,rgba(200,255,246,.95),rgba(70,230,200,.12) 70%);filter:blur(2px);transform-origin:85% 80%}
.w1{left:4px;animation:flap .15s ease-in-out infinite alternate}
.w2{left:16px;animation:flap .15s -.075s ease-in-out infinite alternate;opacity:.65}
@keyframes flap{from{transform:rotate(-40deg) scaleY(1)}to{transform:rotate(30deg) scaleY(.3)}}
.flower{width:120px;height:340px;left:60px;bottom:120px;transform-origin:50% 100%;animation:sway 4s ease-in-out infinite alternate;z-index:4}
@keyframes sway{to{transform:rotate(5deg)}}
.flower .stem{width:7px;height:250px;left:56px;bottom:0;border-radius:4px;background:linear-gradient(90deg,#2e7d4f,#57b06e)}
.flower .bl{width:96px;height:96px;left:12px;top:0;border-radius:50%;background:radial-gradient(circle at 50% 50%,#ffd9e6 0 20%,#f06a9a 21% 46%,#c2436f 47% 60%,rgba(194,67,111,0) 62%)}
.flower .lf{width:44px;height:20px;left:60px;top:190px;border-radius:50%;background:#3f9e5f;transform:rotate(-24deg)}
.pt{width:16px;height:11px;border-radius:50%;background:#f7b8cf;opacity:.9;animation:drift 7s linear infinite}
.p1{left:120px;top:200px;animation-delay:-1s}.p2{left:200px;top:120px;animation-delay:-3.4s}
.p3{left:90px;top:330px;animation-delay:-5.2s}.p4{left:300px;top:180px;animation-delay:-6.1s}
@keyframes drift{0%{transform:translate(0,0) rotate(0);opacity:0}12%{opacity:.95}100%{transform:translate(-140px,220px) rotate(200deg);opacity:0}}
""",
html="""
<i class="sun"></i>
<i class="bird"><i class="wing w1"></i><i class="wing w2"></i><i class="bd"></i><i class="eye"></i><i class="bk"></i></i>
<i class="flower"><i class="stem"></i><i class="bl"></i><i class="lf"></i></i>
<i class="pt p1"></i><i class="pt p2"></i><i class="pt p3"></i><i class="pt p4"></i>
"""))

# ---------- s38 孔雀羽屏 ----------
D.append(dict(file="s38.html", title="孔雀羽屏", brand="孔雀", sub="PEACOCK",
bg="radial-gradient(circle at 50% 28%,#10414b,#071418 78%)",
css="""
.fan{width:0;height:0;left:215px;bottom:210px;z-index:5}
.feather{left:-8px;bottom:0;width:16px;height:330px;border-radius:50% 50% 0 0/100% 100% 0 0;background:linear-gradient(#35d9ab,#0d7a64);transform:rotate(var(--r)) scaleY(0);transform-origin:50% 100%;animation:open 1.3s var(--dl) both}
@keyframes open{to{transform:rotate(var(--r)) scaleY(1)}}
.feather::after{content:"";position:absolute;top:16px;left:50%;transform:translateX(-50%);width:30px;height:38px;border-radius:50%;background:radial-gradient(circle at 50% 34%,#8ffce6,#189a7d 52%,#0a3a32 78%);animation:eye 2.6s ease-in-out infinite alternate}
@keyframes eye{to{box-shadow:0 0 18px 4px rgba(120,250,220,.55)}}
.pbody{width:74px;height:110px;left:178px;bottom:120px;border-radius:50%;background:linear-gradient(135deg,#1f8f76,#0c4a3f);z-index:6;animation:brandIn 1s .9s both}
.pbody .hd{width:34px;height:34px;left:20px;top:-16px;border-radius:50%;background:#27a985}
.pbody .hd::after{content:"";position:absolute;left:24px;top:8px;width:12px;height:7px;border-radius:0 7px 7px 0;background:#f4d35e}
.spark{width:6px;height:6px;border-radius:50%;background:#aef7e4;animation:tw 2s ease-in-out infinite alternate}
.s1{left:80px;top:180px}.s2{left:340px;top:240px;animation-delay:-.7s}.s3{left:150px;top:120px;animation-delay:-1.3s}.s4{left:290px;top:90px;animation-delay:-.4s}
@keyframes tw{to{opacity:.15;transform:scale(.6)}}
""",
html="".join([f'<i class="fan"><i class="feather" style="--r:{r}deg;--dl:{dl}s"></i></i>'
               for r, dl in [(-80,.9),(-60,.75),(-40,.6),(-20,.45),(0,.3),(20,.45),(40,.6),(60,.75),(80,.9)]])
+ """
<i class="pbody"><i class="hd"></i></i>
<i class="spark s1"></i><i class="spark s2"></i><i class="spark s3"></i><i class="spark s4"></i>
"""))

# ---------- s39 风暴之眼 ----------
D.append(dict(file="s39.html", title="风暴之眼", brand="风暴眼", sub="STORM EYE",
bg="linear-gradient(#0c1420,#1b2940 58%,#0a1018)",
css="""
.ring{border:3px dashed rgba(150,190,230,.5);border-radius:50%;left:50%;top:36%;transform:translate(-50%,-50%)}
.r1{width:210px;height:210px;left:50%;animation:spin 14s linear infinite}
.r2{width:310px;height:310px;left:50%;animation:spinR 22s linear infinite;border-color:rgba(150,190,230,.32)}
.r3{width:410px;height:410px;left:50%;animation:spin 34s linear infinite;border-color:rgba(150,190,230,.2)}
@keyframes spin{to{transform:translate(-50%,-50%) rotate(360deg)}}
@keyframes spinR{to{transform:translate(-50%,-50%) rotate(-360deg)}}
.eye{width:96px;height:96px;left:50%;top:36%;transform:translate(-50%,-50%);border-radius:50%;background:radial-gradient(circle at 50% 50%,#fdf6e3,#ffd166 55%,rgba(255,209,102,0) 74%);animation:pulse 2.4s ease-in-out infinite alternate;z-index:5}
@keyframes pulse{to{transform:translate(-50%,-50%) scale(1.12)}}
.rain{position:absolute;left:-40px;right:-40px;top:-60px;bottom:-60px;background:repeating-linear-gradient(100deg,transparent 0 16px,rgba(170,205,245,.13) 16px 18px);animation:rain .45s linear infinite}
@keyframes rain{to{transform:translateY(26px)}}
.flash{position:absolute;inset:0;background:radial-gradient(circle at 70% 20%,rgba(200,220,255,.5),transparent 45%);opacity:0;animation:flash 5s ease-in-out infinite}
@keyframes flash{0%,88%,100%{opacity:0}92%,94%{opacity:.8}}
""",
html="""
<i class="rain"></i><i class="flash"></i>
<i class="ring r1"></i><i class="ring r2"></i><i class="ring r3"></i><i class="eye"></i>
"""))

# ---------- s40 隧道穿行 ----------
D.append(dict(file="s40.html", title="隧道穿行", brand="隧道", sub="TUNNEL",
bg="#04060b",
css="""
.core{width:70px;height:70px;left:50%;top:40%;transform:translate(-50%,-50%);border-radius:50%;background:radial-gradient(circle at 50% 50%,#fff,#9fdcff 55%,rgba(159,220,255,0) 75%);animation:core 2.2s ease-in-out infinite alternate;z-index:5}
@keyframes core{to{transform:translate(-50%,-50%) scale(1.25)}}
.tr{border:2px solid rgba(130,205,255,.65);border-radius:50%;left:50%;top:40%;width:130px;height:130px;transform:translate(-50%,-50%) scale(.15);opacity:0;animation:rush 1.9s linear infinite}
.t1{animation-delay:0s}.t2{animation-delay:-.38s}.t3{animation-delay:-.76s}.t4{animation-delay:-1.14s}.t5{animation-delay:-1.52s}
@keyframes rush{0%{transform:translate(-50%,-50%) scale(.15);opacity:0}22%{opacity:1}100%{transform:translate(-50%,-50%) scale(2.7);opacity:0}}
.streak{width:3px;height:130px;border-radius:2px;background:linear-gradient(rgba(160,215,255,0),rgba(160,215,255,.8),rgba(160,215,255,0));animation:streak .7s linear infinite}
.st1{left:36px;top:120px}.st2{left:70px;top:520px;animation-delay:-.2s}.st3{left:360px;top:200px;animation-delay:-.45s}.st4{left:392px;top:600px;animation-delay:-.1s}.st5{left:20px;top:700px;animation-delay:-.55s}
@keyframes streak{from{transform:translateY(-160px)}to{transform:translateY(220px)}}
""",
html="""
<i class="core"></i>
<i class="tr t1"></i><i class="tr t2"></i><i class="tr t3"></i><i class="tr t4"></i><i class="tr t5"></i>
<i class="streak st1"></i><i class="streak st2"></i><i class="streak st3"></i><i class="streak st4"></i><i class="streak st5"></i>
"""))

# ---------- s41 星火篝火 ----------
D.append(dict(file="s41.html", title="星火篝火", brand="篝火", sub="BONFIRE",
bg="linear-gradient(#090e1e,#151b32 68%,#0a0d16)",
css="""
.star{width:4px;height:4px;border-radius:50%;background:#cfe0ff;animation:tw 2.4s ease-in-out infinite alternate}
.a1{left:60px;top:140px}.a2{left:360px;top:100px;animation-delay:-.8s}.a3{left:200px;top:60px;animation-delay:-1.6s}.a4{left:300px;top:300px;animation-delay:-.4s}
@keyframes tw{to{opacity:.2}}
.glow{width:340px;height:340px;left:45px;top:330px;border-radius:50%;background:radial-gradient(circle at 50% 50%,rgba(255,150,60,.4),transparent 68%);animation:flick2 1.8s ease-in-out infinite alternate}
@keyframes flick2{to{transform:scale(1.08);opacity:.85}}
.log{width:170px;height:26px;left:130px;top:640px;border-radius:13px;background:linear-gradient(#6b4426,#4a2c17);z-index:6}
.l1{transform:rotate(11deg)}.l2{transform:rotate(-11deg)}
.fl{left:50%;bottom:250px;border-radius:8px 50% 50% 50%;transform:rotate(45deg);transform-origin:50% 100%;z-index:5}
.f1{width:118px;height:118px;margin-left:-59px;background:linear-gradient(135deg,#ff7b2d,#ff3d00);animation:flick .55s ease-in-out infinite alternate;filter:blur(1px)}
.f2{width:80px;height:80px;margin-left:-40px;background:linear-gradient(135deg,#ffc53d,#ff8a00);animation:flick .45s -.15s ease-in-out infinite alternate}
.f3{width:44px;height:44px;margin-left:-22px;background:linear-gradient(135deg,#fff3b0,#ffd23d);animation:flick .38s -.3s ease-in-out infinite alternate}
@keyframes flick{from{transform:rotate(45deg) scale(.96,1.02)}to{transform:rotate(45deg) scale(1.05,1.15)}}
.emb{width:7px;height:7px;border-radius:50%;background:#ffcf6e;box-shadow:0 0 10px 3px rgba(255,180,80,.8);animation:rise 3.4s linear infinite;opacity:0}
.e1{left:180px;top:560px;animation-delay:-.4s}.e2{left:215px;top:540px;animation-delay:-1.5s;animation-duration:2.8s}
.e3{left:250px;top:570px;animation-delay:-2.4s}.e4{left:195px;top:590px;animation-delay:-3s;animation-duration:4.2s}
@keyframes rise{0%{transform:translate(0,0);opacity:0}14%{opacity:1}100%{transform:translate(36px,-420px);opacity:0}}
""",
html="""
<i class="star a1"></i><i class="star a2"></i><i class="star a3"></i><i class="star a4"></i>
<i class="glow"></i>
<i class="fl f1"></i><i class="fl f2"></i><i class="fl f3"></i>
<i class="log l1"></i><i class="log l2"></i>
<i class="emb e1"></i><i class="emb e2"></i><i class="emb e3"></i><i class="emb e4"></i>
"""))

# ---------- s42 蛛网晨露 ----------
D.append(dict(file="s42.html", title="蛛网晨露", brand="蛛网", sub="DEWDROP",
bg="linear-gradient(#f9dcae,#eda87e 52%,#96657a)",
css="""
.web{left:50%;top:60px;transform:translateX(-50%);z-index:4}
.web line,.web polygon{stroke:rgba(255,255,255,.85);stroke-width:2;fill:none;stroke-dasharray:100;stroke-dashoffset:100;animation:draw 2.2s .2s both}
.web .r2{animation-delay:.5s}.web .r3{animation-delay:.8s}.web .r4{animation-delay:1.1s}
@keyframes draw{to{stroke-dashoffset:0}}
.dew{width:13px;height:13px;border-radius:50%;background:radial-gradient(circle at 32% 30%,#fff,rgba(190,225,255,.35) 60%,rgba(160,200,240,.15));box-shadow:0 0 8px rgba(255,255,255,.7);z-index:5;animation:tw2 2.2s ease-in-out infinite alternate}
.d1{left:196px;top:150px}.d2{left:238px;top:196px;animation-delay:-.6s}.d3{left:158px;top:230px;animation-delay:-1.2s}
.d4{left:262px;top:258px;animation-delay:-.3s}.d5{left:206px;top:292px;animation-delay:-1.7s}
@keyframes tw2{to{transform:scale(1.25);opacity:.75}}
.thread{width:2px;height:120px;left:300px;top:0;background:rgba(255,255,255,.7);transform-origin:50% 0;animation:sway2 3.4s ease-in-out infinite alternate;z-index:5}
@keyframes sway2{to{transform:rotate(7deg)}}
.spider{width:26px;height:32px;left:287px;top:118px;border-radius:50%;background:radial-gradient(circle at 50% 35%,#5a4a68,#241d2e 75%);transform-origin:50% -118px;animation:sway2 3.4s ease-in-out infinite alternate;z-index:5}
.leaf{width:150px;height:60px;left:-30px;bottom:130px;border-radius:50%;background:linear-gradient(#4a7d3f,#2c5a2c);transform:rotate(-14deg);z-index:3}
.leaf2{width:170px;height:66px;left:300px;bottom:90px;border-radius:50%;background:linear-gradient(#557f42,#2f5c2b);transform:rotate(12deg);z-index:3}
""",
html="""
<svg class="web" width="300" height="340" viewBox="0 0 300 340">
<polygon class="r1" pathLength="100" points="150,20 256,80 256,200 150,260 44,200 44,80"/>
<polygon class="r2" pathLength="100" points="150,70 222,112 222,196 150,238 78,196 78,112"/>
<polygon class="r3" pathLength="100" points="150,112 193,137 193,187 150,212 107,187 107,137"/>
<polygon class="r4" pathLength="100" points="150,146 172,159 172,185 150,198 128,185 128,159"/>
<line pathLength="100" x1="150" y1="0" x2="150" y2="280"/>
<line pathLength="100" x1="30" y1="60" x2="270" y2="220"/>
<line pathLength="100" x1="270" y1="60" x2="30" y2="220"/>
<line pathLength="100" x1="80" y1="20" x2="220" y2="270"/>
<line pathLength="100" x1="220" y1="20" x2="80" y2="270"/>
</svg>
<i class="thread"></i><i class="spider"></i>
<i class="dew d1"></i><i class="dew d2"></i><i class="dew d3"></i><i class="dew d4"></i><i class="dew d5"></i>
<i class="leaf"></i><i class="leaf2"></i>
"""))

# ---------- s43 蒲公英 ----------
D.append(dict(file="s43.html", title="飞絮逐风", brand="飞絮逐风", sub="DANDELION",
bg="linear-gradient(#bfe0f2,#e9f6ee 68%,#cfe8d6)",
css="""
.halo{width:280px;height:280px;left:75px;top:60px;border-radius:50%;background:radial-gradient(circle at 50% 50%,rgba(255,250,220,.95),rgba(255,250,220,0) 68%)}
.plant{width:130px;height:420px;left:60px;bottom:150px;z-index:4}
.plant .stem{width:8px;height:300px;left:61px;bottom:0;border-radius:4px;background:linear-gradient(90deg,#4a9e5f,#79c78d)}
.plant .head{width:120px;height:120px;left:5px;top:0;border-radius:50%;
background:repeating-conic-gradient(rgba(255,255,255,.9) 0 7deg,transparent 7deg 15deg);
-webkit-mask:radial-gradient(circle at 50% 50%,#000 58%,transparent 64%);
mask:radial-gradient(circle at 50% 50%,#000 58%,transparent 64%);
animation:spinSlow 26s linear infinite}
@keyframes spinSlow{to{transform:rotate(360deg)}}
.seed{width:34px;height:14px;z-index:5;animation:fly 9s linear infinite;opacity:0}
.seed::before{content:"";position:absolute;left:0;top:6px;width:22px;height:2px;background:rgba(255,255,255,.9)}
.seed::after{content:"";position:absolute;right:0;top:4px;width:9px;height:9px;border-radius:50%;background:#fff;box-shadow:0 0 8px rgba(255,255,255,.9)}
.sd1{left:110px;top:220px;animation-delay:-1s;--dx:260px}
.sd2{left:110px;top:250px;animation-delay:-3.5s;--dx:300px;animation-duration:11s}
.sd3{left:110px;top:200px;animation-delay:-6s;--dx:230px;animation-duration:8s}
.sd4{left:110px;top:270px;animation-delay:-7.6s;--dx:330px;animation-duration:12s}
@keyframes fly{0%{transform:translate(0,0) rotate(0);opacity:0}10%{opacity:1}100%{transform:translate(var(--dx),-140px) rotate(160deg);opacity:0}}
.grass{width:200px;height:90px;border-radius:50%;background:linear-gradient(#5aa86e,#3a7d4e);z-index:3}
.g1{left:-40px;bottom:120px}.g2{left:280px;bottom:100px}
""",
html="""
<i class="halo"></i>
<i class="plant"><i class="stem"></i><i class="head"></i></i>
<i class="seed sd1"></i><i class="seed sd2"></i><i class="seed sd3"></i><i class="seed sd4"></i>
<i class="grass g1"></i><i class="grass g2"></i>
"""))

# ---------- s44 竹节生长 ----------
D.append(dict(file="s44.html", title="竹节生长", brand="竹", sub="BAMBOO",
bg="linear-gradient(#dcefe2,#b7dcc6 58%,#8db69c)",
css="""
.seg{width:36px;left:197px;border-radius:15px;background:linear-gradient(90deg,#3c8a5c,#74c184 50%,#3c8a5c);transform:scaleY(0);transform-origin:50% 100%;animation:grow .9s both;z-index:5}
.sg1{height:130px;bottom:130px;animation-delay:.2s}.sg2{height:130px;bottom:260px;animation-delay:.8s}
.sg3{height:130px;bottom:390px;animation-delay:1.4s}.sg4{height:110px;bottom:520px;animation-delay:2s}
@keyframes grow{to{transform:scaleY(1)}}
.joint{width:44px;height:10px;left:193px;border-radius:5px;background:#2f6e47;transform:scaleX(0);animation:grow2 .5s both;z-index:6}
.j1{bottom:256px;animation-delay:.9s}.j2{bottom:386px;animation-delay:1.5s}.j3{bottom:516px;animation-delay:2.1s}
@keyframes grow2{to{transform:scaleX(1)}}
.bleaf{width:64px;height:24px;border-radius:50%;background:linear-gradient(135deg,#4da264,#2c6e42);transform:scale(0);animation:leafIn .6s both;z-index:6}
.bl1{left:222px;bottom:480px;transform-origin:0 50%;animation-delay:2.3s}
.bl2{left:140px;bottom:360px;transform:rotate(24deg);transform-origin:100% 50%;animation-delay:1.7s}
.bl3{left:226px;bottom:250px;transform-origin:0 50%;animation-delay:1.1s}
@keyframes leafIn{to{transform:scale(1) rotate(var(--rr,0deg))}}
.ground{position:absolute;left:0;right:0;bottom:0;height:140px;background:linear-gradient(#7ba889,#4e7d5f);z-index:4}
.mist{width:220px;height:70px;border-radius:50%;background:rgba(255,255,255,.5);filter:blur(14px);animation:mist 7s ease-in-out infinite alternate;z-index:7}
.m1{left:40px;bottom:120px}.m2{left:220px;bottom:90px;animation-delay:-3.4s}
@keyframes mist{to{transform:translateX(60px);opacity:.6}}
.shoot{width:20px;height:60px;left:320px;bottom:130px;border-radius:50% 50% 0 0/100% 100% 0 0;background:#4da264;transform:scaleY(0);transform-origin:50% 100%;animation:grow .8s 2.4s both;z-index:5}
""",
html="""
<i class="seg sg1"></i><i class="seg sg2"></i><i class="seg sg3"></i><i class="seg sg4"></i>
<i class="joint j1"></i><i class="joint j2"></i><i class="joint j3"></i>
<i class="bleaf bl1" style="--rr:18deg"></i><i class="bleaf bl2"></i><i class="bleaf bl3" style="--rr:-14deg"></i>
<i class="shoot"></i>
<i class="ground"></i>
<i class="mist m1"></i><i class="mist m2"></i>
"""))

# ---------- s45 飞瀑流泉 ----------
D.append(dict(file="s45.html", title="飞瀑流泉", brand="飞瀑", sub="WATERFALL",
bg="linear-gradient(#9fd0e8,#d9edf6 70%,#bcdcec)",
css="""
.cliff{width:170px;height:640px;top:60px;background:linear-gradient(100deg,#5a6a78,#3c4854);z-index:4}
.c1{left:-30px;clip-path:polygon(0 0,100% 6%,78% 100%,0 100%)}
.c2{right:-30px;left:auto;clip-path:polygon(0 6%,100% 0,100% 100%,22% 100%)}
.c1{left:-30px}.c2{left:290px}
.fall{left:148px;top:110px;width:134px;height:560px;z-index:5;background:repeating-linear-gradient(0deg,rgba(255,255,255,.95) 0 9px,rgba(190,225,242,.5) 9px 21px);-webkit-mask:linear-gradient(90deg,transparent,#000 18%,#000 82%,transparent);mask:linear-gradient(90deg,transparent,#000 18%,#000 82%,transparent);animation:flow 1s linear infinite}
@keyframes flow{to{background-position:0 42px}}
.foam{left:120px;top:640px;width:190px;height:70px;border-radius:50%;background:rgba(255,255,255,.75);filter:blur(12px);animation:foam 2.2s ease-in-out infinite alternate;z-index:6}
@keyframes foam{to{transform:scaleX(1.15);opacity:.7}}
.pool{position:absolute;left:40px;right:40px;bottom:60px;height:150px;z-index:3}
.rip{left:50%;top:40px;width:200px;height:56px;margin-left:-100px;border:2px solid rgba(255,255,255,.7);border-radius:50%;transform:scale(.3);opacity:0;animation:rip 3s ease-out infinite}
.rp2{animation-delay:-1.5s}
@keyframes rip{0%{transform:scale(.3);opacity:0}25%{opacity:.9}100%{transform:scale(1.5);opacity:0}}
.drop{width:8px;height:14px;border-radius:50%;background:rgba(255,255,255,.9);animation:drop 1.6s linear infinite;opacity:0;z-index:6}
.dp1{left:170px;top:600px;animation-delay:-.3s}.dp2{left:230px;top:620px;animation-delay:-1s}.dp3{left:200px;top:640px;animation-delay:-.7s}
@keyframes drop{0%{transform:translateY(0);opacity:0}20%{opacity:1}100%{transform:translateY(-90px);opacity:0}}
""",
html="""
<i class="cliff c1"></i><i class="cliff c2"></i>
<i class="fall"></i>
<i class="pool"><i class="rip rp1"></i><i class="rip rp2"></i></i>
<i class="foam"></i>
<i class="drop dp1"></i><i class="drop dp2"></i><i class="drop dp3"></i>
"""))

# ---------- s46 冰川崩裂 ----------
D.append(dict(file="s46.html", title="冰川崩裂", brand="冰川", sub="GLACIER",
bg="linear-gradient(#d4ecf7,#a9cde6 58%,#7fa9cd)",
css="""
.ice{width:430px;height:660px;left:0;top:110px;clip-path:polygon(0 38%,14% 20%,30% 34%,46% 12%,62% 30%,78% 16%,92% 32%,100% 24%,100% 100%,0 100%);background:linear-gradient(#eaf6fd,#b9d9ee 60%,#8fb8d8);z-index:4}
.crack{left:0;top:110px;z-index:5}
.crack polyline{stroke:#2e5a7d;stroke-width:4;fill:none;stroke-linecap:round;stroke-dasharray:100;stroke-dashoffset:100;animation:draw 1.6s .5s both}
@keyframes draw{to{stroke-dashoffset:0}}
.shard{width:54px;height:70px;background:linear-gradient(135deg,#f2fafd,#a9cfe8);clip-path:polygon(50% 0,100% 62%,72% 100%,28% 100%,0 62%);z-index:6;opacity:0;animation:shardFall 1.8s both}
.sh1{left:120px;top:270px;--dl:.9s;--rr:40deg}.sh2{left:200px;top:240px;--dl:1.2s;--rr:-55deg}
.sh3{left:280px;top:280px;--dl:1.5s;--rr:70deg}
.shard{animation-delay:var(--dl)}
@keyframes shardFall{0%{opacity:0;transform:translateY(0) rotate(0)}12%{opacity:1}100%{opacity:1;transform:translateY(400px) rotate(var(--rr))}}
.snow{width:7px;height:7px;border-radius:50%;background:#fff;animation:snow 5s linear infinite;opacity:0}
.sn1{left:60px;top:0;animation-delay:-1s}.sn2{left:170px;top:0;animation-delay:-2.6s}.sn3{left:290px;top:0;animation-delay:-4s}.sn4{left:380px;top:0;animation-delay:-.4s}
@keyframes snow{0%{transform:translate(0,0);opacity:0}10%{opacity:.95}100%{transform:translate(-60px,700px);opacity:0}}
.sea{position:absolute;left:0;right:0;bottom:0;height:170px;background:linear-gradient(#5f93bd,#3a6a92);z-index:3}
""",
html="""
<svg class="crack" width="430" height="560" viewBox="0 0 430 560">
<polyline pathLength="100" points="198,52 170,150 205,240 160,340 190,440"/>
<polyline pathLength="100" points="205,240 260,290 250,360" style="animation-delay:1.1s"/>
</svg>
<i class="ice"></i>
<i class="shard sh1"></i><i class="shard sh2"></i><i class="shard sh3"></i>
<i class="snow sn1"></i><i class="snow sn2"></i><i class="snow sn3"></i><i class="snow sn4"></i>
<i class="sea"></i>
"""))

# ---------- s47 孔明灯 ----------
D.append(dict(file="s47.html", title="天灯祈愿", brand="天灯祈愿", sub="SKY LANTERN",
bg="linear-gradient(#0a0f2e,#1c1440 58%,#37214c)",
css="""
.star{width:4px;height:4px;border-radius:50%;background:#dfe8ff;animation:tw 2.6s ease-in-out infinite alternate}
.t1{left:70px;top:120px}.t2{left:180px;top:70px;animation-delay:-1s}.t3{left:300px;top:150px;animation-delay:-1.8s}.t4{left:120px;top:300px;animation-delay:-.5s}.t5{left:350px;top:60px;animation-delay:-2.2s}
@keyframes tw{to{opacity:.15}}
.moon{width:90px;height:90px;left:300px;top:80px;border-radius:50%;background:radial-gradient(circle at 38% 35%,#fdf6dd,#e8d9a8 70%);box-shadow:0 0 50px 14px rgba(253,246,221,.25)}
.lan{width:66px;height:88px;z-index:5;animation:rise 12s linear infinite}
.lan .bd{width:66px;height:70px;left:0;top:8px;border-radius:46% 46% 44% 44%/60% 60% 40% 40%;background:radial-gradient(circle at 50% 32%,#ffe9bb,#ff9d5c 62%,#dd6428);box-shadow:0 0 44px 14px rgba(255,170,90,.42)}
.lan .tp{width:34px;height:12px;left:16px;top:0;border-radius:6px;background:#b4501f}
.lan .fl{width:20px;height:14px;left:23px;top:66px;border-radius:50%;background:radial-gradient(circle at 50% 50%,#fff3b0,#ff9d3d 70%);animation:flick .4s ease-in-out infinite alternate}
@keyframes flick{to{transform:scale(1.15);opacity:.85}}
.n1{left:80px;animation-duration:13s;animation-delay:-2s}
.n2{left:190px;animation-duration:10s;animation-delay:-6s;--sc:.72}
.n3{left:300px;animation-duration:15s;animation-delay:-9s;--sc:.55}
.n4{left:140px;animation-duration:11s;animation-delay:-4s;--sc:.85}
@keyframes rise{0%{top:860px;transform:translateX(0) scale(var(--sc,1))}50%{transform:translateX(26px) scale(var(--sc,1))}100%{top:-140px;transform:translateX(-14px) scale(var(--sc,1))}}
.mts{position:absolute;left:0;right:0;bottom:0;height:220px;background:linear-gradient(#241a3e,#120d22);clip-path:polygon(0 100%,0 55%,12% 30%,24% 58%,38% 34%,52% 62%,66% 40%,80% 66%,92% 48%,100% 70%,100% 100%);z-index:4}
""",
html="""
<i class="star t1"></i><i class="star t2"></i><i class="star t3"></i><i class="star t4"></i><i class="star t5"></i>
<i class="moon"></i>
<i class="lan n1"><i class="tp"></i><i class="bd"></i><i class="fl"></i></i>
<i class="lan n2"><i class="tp"></i><i class="bd"></i><i class="fl"></i></i>
<i class="lan n3"><i class="tp"></i><i class="bd"></i><i class="fl"></i></i>
<i class="lan n4"><i class="tp"></i><i class="bd"></i><i class="fl"></i></i>
<i class="mts"></i>
"""))

# ---------- s48 水车悠悠 ----------
D.append(dict(file="s48.html", title="水车悠悠", brand="水车", sub="WATERWHEEL",
bg="linear-gradient(#bcdff0,#e8f3e6 52%,#a8cbd8)",
css="""
.cloud{width:120px;height:44px;border-radius:22px;background:rgba(255,255,255,.92);animation:cloud 16s ease-in-out infinite alternate;z-index:2}
.cl1{left:40px;top:90px}.cl2{left:250px;top:150px;animation-delay:-8s;transform:scale(.7)}
@keyframes cloud{to{transform:translateX(70px)}}
.wheel{width:230px;height:230px;left:100px;top:320px;z-index:5;animation:spin 16s linear infinite}
@keyframes spin{to{transform:rotate(360deg)}}
.wheel .rim{width:230px;height:230px;left:0;top:0;border-radius:50%;border:10px solid #7a5230}
.wheel .hub{width:34px;height:34px;left:98px;top:98px;border-radius:50%;background:#5a3a20}
.spoke{width:8px;height:214px;left:111px;top:8px;background:#8a5f36;transform:rotate(var(--r));transform-origin:50% 50%}
.paddle{width:34px;height:20px;background:#6b4426;border-radius:4px;transform:rotate(var(--r)) translateY(-104px);transform-origin:50% 114px;left:98px;top:101px}
.axle{width:16px;height:120px;left:207px;top:430px;background:#5a3a20;z-index:4}
.river{position:absolute;left:0;right:0;bottom:0;height:300px;background:linear-gradient(#7fb8d4,#4a86ad);z-index:3}
.wave{height:34px;border-radius:50%;background:rgba(255,255,255,.35);animation:wave 5s ease-in-out infinite alternate}
.wv1{left:-30px;right:-30px;bottom:230px}.wv2{left:-50px;right:-50px;bottom:150px;animation-delay:-2.5s}
@keyframes wave{to{transform:translateX(46px)}}
.hut{width:110px;height:80px;left:290px;top:230px;background:#6b4a30;clip-path:polygon(0 38%,50% 0,100% 38%,100% 100%,0 100%);z-index:4}
.reed{width:6px;height:70px;border-radius:3px;background:#3f7d4f;transform-origin:50% 100%;animation:sway3 3.6s ease-in-out infinite alternate;z-index:6}
.rd1{left:50px;bottom:180px}.rd2{left:70px;bottom:170px;animation-delay:-1.2s}.rd3{left:370px;bottom:190px;animation-delay:-2s}
@keyframes sway3{to{transform:rotate(9deg)}}
""",
html="".join([f'<i class="wheel"><i class="rim"></i>'
               + "".join([f'<i class="spoke" style="--r:{r}deg"></i>' for r in range(0,180,45)])
               + "".join([f'<i class="paddle" style="--r:{r}deg"></i>' for r in range(0,360,45)])
               + '<i class="hub"></i></i>'])
+ """
<i class="cloud cl1"></i><i class="cloud cl2"></i>
<i class="hut"></i><i class="axle"></i>
<i class="river"></i>
<i class="wave wv1"></i><i class="wave wv2"></i>
<i class="reed rd1"></i><i class="reed rd2"></i><i class="reed rd3"></i>
"""))

# ---------- s49 深海潜行 ----------
D.append(dict(file="s49.html", title="深海潜行", brand="深潜", sub="DEEP DIVE",
bg="linear-gradient(#07305a,#041c34 55%,#020d18)",
css="""
.ray{width:70px;height:700px;top:-60px;background:linear-gradient(rgba(140,200,255,.16),transparent 80%);transform:skewX(-12deg);transform-origin:50% 0;animation:raysway 7s ease-in-out infinite alternate}
.ry1{left:90px}.ry2{left:220px;animation-delay:-2.4s}.ry3{left:330px;animation-delay:-4.8s}
@keyframes raysway{to{transform:skewX(10deg)}}
.sub{width:200px;height:66px;left:50px;top:430px;z-index:6;animation:cruise 10s ease-in-out infinite alternate}
@keyframes cruise{to{transform:translate(150px,-34px)}}
.sub .hull{width:200px;height:66px;left:0;top:0;border-radius:40px;background:linear-gradient(#4a7ea3,#22415e)}
.sub .nose{width:60px;height:66px;left:150px;top:0;border-radius:0 40px 40px 0;background:linear-gradient(#5a90b3,#2a4c6e)}
.sub .tower{width:44px;height:34px;left:80px;top:-24px;border-radius:10px 10px 0 0;background:#2a4c6e}
.sub .port{width:14px;height:14px;border-radius:50%;background:radial-gradient(circle at 35% 30%,#bfe6ff,#5a90b3);top:26px}
.pt1{left:56px}.pt2{left:88px}.pt3{left:120px}
.sub .prop{width:10px;height:44px;left:-8px;top:11px;border-radius:5px;background:rgba(190,225,255,.5);filter:blur(3px);animation:prop .3s linear infinite}
@keyframes prop{to{transform:rotate(360deg)}}
.sonar{border:2px solid rgba(120,200,255,.55);border-radius:50%;left:150px;top:463px;width:60px;height:60px;transform:translate(-50%,-50%) scale(.4);opacity:0;animation:sonar 3.2s ease-out infinite;z-index:5}
.sn2{animation-delay:-1.07s}.sn3{animation-delay:-2.13s}
@keyframes sonar{0%{transform:translate(-50%,-50%) scale(.4);opacity:0}20%{opacity:.9}100%{transform:translate(-50%,-50%) scale(3.4);opacity:0}}
.bub{width:10px;height:10px;border-radius:50%;background:radial-gradient(circle at 35% 30%,rgba(255,255,255,.9),rgba(160,210,245,.25));animation:bub 6s linear infinite;opacity:0;z-index:5}
.b1{left:120px;top:500px;animation-delay:-1s}.b2{left:150px;top:520px;animation-delay:-3s;animation-duration:7s}
.b3{left:90px;top:540px;animation-delay:-4.6s}
@keyframes bub{0%{transform:translateY(0);opacity:0}12%{opacity:.9}100%{transform:translateY(-380px);opacity:0}}
.floor{position:absolute;left:0;right:0;bottom:0;height:130px;background:linear-gradient(#0a2036,#050f1c);clip-path:polygon(0 100%,0 45%,18% 20%,35% 48%,55% 28%,75% 52%,90% 34%,100% 50%,100% 100%);z-index:4}
.weed{width:12px;height:90px;bottom:60px;border-radius:6px;background:linear-gradient(#1d5a44,#0e3527);transform-origin:50% 100%;animation:weed 4s ease-in-out infinite alternate;z-index:5}
.wd1{left:80px}.wd2{left:330px;animation-delay:-2s;height:70px}
@keyframes weed{to{transform:rotate(10deg)}}
""",
html="""
<i class="ray ry1"></i><i class="ray ry2"></i><i class="ray ry3"></i>
<i class="sub"><i class="hull"></i><i class="nose"></i><i class="tower"></i><i class="port pt1"></i><i class="port pt2"></i><i class="port pt3"></i><i class="prop"></i></i>
<i class="sonar sn1"></i><i class="sonar sn2"></i><i class="sonar sn3"></i>
<i class="bub b1"></i><i class="bub b2"></i><i class="bub b3"></i>
<i class="floor"></i><i class="weed wd1"></i><i class="weed wd2"></i>
"""))

# ---------- s50 热气球 ----------
D.append(dict(file="s50.html", title="气球漫游", brand="气球漫游", sub="BALLOON",
bg="linear-gradient(#ffd9a0,#ffab7c 38%,#e8899c 62%,#7c5f9e)",
css="""
.sunglow{width:200px;height:200px;left:115px;top:130px;border-radius:50%;background:radial-gradient(circle at 50% 50%,rgba(255,246,220,.95),rgba(255,246,220,0) 68%)}
.mts{position:absolute;left:0;right:0;bottom:0;height:330px;z-index:4}
.mts .m1{position:absolute;left:0;right:0;bottom:0;height:220px;background:#6a4a7e;clip-path:polygon(0 100%,0 60%,14% 25%,28% 62%,44% 35%,60% 68%,76% 42%,90% 64%,100% 50%,100% 100%)}
.mts .m2{position:absolute;left:0;right:0;bottom:0;height:150px;background:#4a3260;clip-path:polygon(0 100%,0 70%,20% 40%,36% 72%,55% 45%,72% 75%,88% 55%,100% 72%,100% 100%)}
.bal{z-index:6;transform:scale(var(--sc,1));animation:bob 5s ease-in-out infinite alternate}
.bal .env{width:112px;height:132px;left:0;top:0;border-radius:50% 50% 50% 50%/56% 56% 44% 44%;background:repeating-linear-gradient(90deg,#ff6b6b 0 15px,#ffe66d 15px 30px)}
.bal .rope1{width:3px;height:44px;left:32px;top:126px;background:rgba(90,60,40,.8)}
.bal .rope2{width:3px;height:44px;left:77px;top:126px;background:rgba(90,60,40,.8)}
.bal .bask{width:40px;height:30px;left:36px;top:166px;border-radius:5px;background:linear-gradient(#9a6a42,#6e4526)}
.bl1{left:60px;top:180px;animation-duration:5s}
.bl2{left:250px;top:120px;--sc:.68;animation-duration:6.4s;animation-delay:-2s}
.bl2 .env{background:repeating-linear-gradient(90deg,#4ecdc4 0 15px,#f7fff7 15px 30px)}
.bl3{left:160px;top:300px;--sc:.45;animation-duration:7.2s;animation-delay:-4s}
.bl3 .env{background:repeating-linear-gradient(90deg,#a78bfa 0 15px,#fbcfe8 15px 30px)}
@keyframes bob{to{transform:translateY(-26px) scale(var(--sc,1))}}
.cloud{width:130px;height:46px;border-radius:23px;background:rgba(255,255,255,.9);animation:cloud 18s ease-in-out infinite alternate;z-index:5}
.cc1{left:20px;top:420px}.cc2{left:280px;top:500px;animation-delay:-9s;transform:scale(.7)}
@keyframes cloud{to{transform:translateX(80px)}}
""",
html="""
<i class="sunglow"></i>
<i class="bal bl1"><i class="env"></i><i class="rope1"></i><i class="rope2"></i><i class="bask"></i></i>
<i class="bal bl2"><i class="env"></i><i class="rope1"></i><i class="rope2"></i><i class="bask"></i></i>
<i class="bal bl3"><i class="env"></i><i class="rope1"></i><i class="rope2"></i><i class="bask"></i></i>
<i class="cloud cc1"></i><i class="cloud cc2"></i>
<i class="mts"><i class="m1"></i><i class="m2"></i></i>
"""))

# ---------- s51 旋转木马 ----------
D.append(dict(file="s51.html", title="旋转木马", brand="木马", sub="CAROUSEL",
bg="linear-gradient(#2a1a3e,#4c2a58 58%,#221231)",
css="""
.canopy{width:360px;height:130px;left:35px;top:150px;clip-path:polygon(50% 0,100% 100%,0 100%);background:repeating-conic-gradient(from 0deg at 50% 100%,#ff6b8a 0 12deg,#fdf0f0 12deg 24deg);z-index:6}
.crown{width:26px;height:26px;left:202px;top:128px;border-radius:50%;background:radial-gradient(circle at 35% 30%,#ffe66d,#e0a92d);box-shadow:0 0 24px 8px rgba(255,230,109,.5);z-index:7}
.deck{width:380px;height:60px;left:25px;top:560px;border-radius:50%;background:linear-gradient(#8a5a8a,#5a3560);z-index:4}
.pole{width:8px;height:290px;left:50%;top:270px;margin-left:-4px;background:linear-gradient(90deg,#d9b36a,#f4d68a,#d9b36a);z-index:5}
.horse{width:90px;height:120px;z-index:6;animation:gallop 1.6s ease-in-out infinite alternate}
.h1{left:60px;top:400px}.h2{left:175px;top:380px;animation-delay:-.5s}.h3{left:285px;top:400px;animation-delay:-1s}
@keyframes gallop{to{transform:translateY(-30px)}}
.horse .bd{width:62px;height:34px;left:14px;top:52px;border-radius:50%;background:linear-gradient(135deg,#f2e3d5,#c9a184)}
.horse .neck{width:20px;height:44px;left:58px;top:22px;border-radius:10px;background:#dfc0a4;transform:rotate(18deg)}
.horse .head{width:30px;height:20px;left:66px;top:12px;border-radius:50% 50% 40% 40%;background:#efcfae;transform:rotate(12deg)}
.horse .mane{width:12px;height:40px;left:52px;top:24px;border-radius:6px;background:#8a4a3a;transform:rotate(14deg)}
.horse .leg{width:9px;height:40px;top:82px;border-radius:5px;background:#c9a184}
.lg1{left:24px}.lg2{left:40px}.lg3{left:58px}.lg4{left:72px}
.horse .saddle{width:34px;height:14px;left:28px;top:46px;border-radius:7px;background:#d94f6a}
.light{width:10px;height:10px;border-radius:50%;background:#ffe66d;box-shadow:0 0 12px 4px rgba(255,230,109,.7);animation:blink 1.2s ease-in-out infinite alternate;z-index:7}
.lt1{left:60px;top:268px}.lt2{left:130px;top:250px;animation-delay:-.4s}.lt3{left:215px;top:244px;animation-delay:-.8s}
.lt4{left:300px;top:250px;animation-delay:-.2s}.lt5{left:365px;top:268px;animation-delay:-.6s}
@keyframes blink{to{opacity:.25}}
.ground2{position:absolute;left:0;right:0;bottom:0;height:200px;background:#1a0f28;z-index:3}
""",
html="""
<i class="ground2"></i>
<i class="deck"></i>
<i class="canopy"></i><i class="crown"></i>
<i class="light lt1"></i><i class="light lt2"></i><i class="light lt3"></i><i class="light lt4"></i><i class="light lt5"></i>
<i class="horse h1"><i class="pole" style="left:41px;top:-130px;margin:0"></i><i class="bd"></i><i class="neck"></i><i class="head"></i><i class="mane"></i><i class="saddle"></i><i class="leg lg1"></i><i class="leg lg2"></i><i class="leg lg3"></i><i class="leg lg4"></i></i>
<i class="horse h2"><i class="pole" style="left:41px;top:-110px;margin:0"></i><i class="bd"></i><i class="neck"></i><i class="head"></i><i class="mane"></i><i class="saddle"></i><i class="leg lg1"></i><i class="leg lg2"></i><i class="leg lg3"></i><i class="leg lg4"></i></i>
<i class="horse h3"><i class="pole" style="left:41px;top:-130px;margin:0"></i><i class="bd"></i><i class="neck"></i><i class="head"></i><i class="mane"></i><i class="saddle"></i><i class="leg lg1"></i><i class="leg lg2"></i><i class="leg lg3"></i><i class="leg lg4"></i></i>
"""))

# ---------- s52 雨后彩虹 ----------
D.append(dict(file="s52.html", title="雨后彩虹", brand="彩虹", sub="RAINBOW",
bg="linear-gradient(#a8e0f5,#e2f4fb 58%,#d2ead8)",
css="""
.sunglow{width:170px;height:170px;left:280px;top:70px;border-radius:50%;background:radial-gradient(circle at 50% 50%,rgba(255,248,220,.95),rgba(255,248,220,0) 68%)}
.sun{width:76px;height:76px;left:327px;top:117px;border-radius:50%;background:radial-gradient(circle at 40% 35%,#fffbe8,#ffdf6e 70%);box-shadow:0 0 40px 12px rgba(255,223,110,.5)}
.ray2{width:130px;height:10px;left:300px;top:150px;transform-origin:100% 50%;background:linear-gradient(90deg,transparent,rgba(255,230,130,.7));animation:sunspin 12s linear infinite}
@keyframes sunspin{to{transform:rotate(360deg)}}
.rb{left:50%;top:330px;border-radius:50%;border:15px solid transparent;transform:translateX(-50%) scale(.6);opacity:0;animation:arc 1.4s both;transform-origin:50% 0}
.a1{width:360px;height:360px;margin-left:-180px;border-top-color:#ff6b6b;animation-delay:.3s}
.a2{width:328px;height:328px;margin-left:-164px;border-top-color:#ffa94d;animation-delay:.5s}
.a3{width:296px;height:296px;margin-left:-148px;border-top-color:#ffe66d;animation-delay:.7s}
.a4{width:264px;height:264px;margin-left:-132px;border-top-color:#51cf66;animation-delay:.9s}
.a5{width:232px;height:232px;margin-left:-116px;border-top-color:#4dabf7;animation-delay:1.1s}
@keyframes arc{to{transform:translateX(-50%) scale(1);opacity:.92}}
.cloud{width:150px;height:56px;border-radius:28px;background:#fff;box-shadow:0 8px 20px rgba(150,180,200,.35);z-index:6;animation:part 3s 1s both}
.ccl{left:60px;top:250px;--tx:-190px}.ccr{left:230px;top:300px;--tx:190px}
@keyframes part{to{transform:translateX(var(--tx));opacity:.85}}
.hill{position:absolute;left:0;right:0;bottom:0;height:200px;background:linear-gradient(#8fce8f,#5da465);clip-path:polygon(0 100%,0 55%,20% 30%,40% 60%,60% 35%,80% 62%,100% 45%,100% 100%);z-index:5}
.drop2{width:6px;height:12px;border-radius:50%;background:rgba(140,190,230,.8);animation:drop2 1.2s ease-in both;z-index:7}
.dr1{left:120px;top:180px;animation-delay:.2s}.dr2{left:320px;top:220px;animation-delay:.5s}.dr3{left:220px;top:140px;animation-delay:.8s}
@keyframes drop2{to{transform:translateY(420px);opacity:0}}
""",
html="""
<i class="sunglow"></i><i class="sun"></i><i class="ray2"></i>
<i class="rb a1"></i><i class="rb a2"></i><i class="rb a3"></i><i class="rb a4"></i><i class="rb a5"></i>
<i class="cloud ccl"></i><i class="cloud ccr"></i>
<i class="drop2 dr1"></i><i class="drop2 dr2"></i><i class="drop2 dr3"></i>
<i class="hill"></i>
"""))

# ---------- s53 枫叶纷飞 ----------
D.append(dict(file="s53.html", title="枫叶纷飞", brand="枫叶", sub="MAPLE",
bg="linear-gradient(#f9e0ae,#f2b26e 62%,#d98a4e)",
css="""
.branch{width:280px;height:26px;left:-40px;top:120px;border-radius:13px;background:linear-gradient(#5a3a24,#3c2415);transform:rotate(14deg);z-index:4}
.tw{width:120px;height:14px;border-radius:7px;background:#4a2e1a;z-index:4}
.tw1{left:120px;top:150px;transform:rotate(-24deg)}.tw2{left:40px;top:200px;transform:rotate(38deg)}
.leaf{width:30px;height:30px;background:linear-gradient(135deg,#ef6a4d,#b03224);clip-path:polygon(50% 0,63% 34%,98% 34%,70% 56%,83% 90%,50% 69%,17% 90%,30% 56%,2% 34%,37% 34%);z-index:5;animation:fall 8s linear infinite;opacity:0}
@keyframes fall{0%{transform:translate(0,-70px) rotate(0);opacity:0}8%{opacity:1}100%{transform:translate(var(--sx),980px) rotate(620deg);opacity:.9}}
.ground3{position:absolute;left:0;right:0;bottom:0;height:190px;background:linear-gradient(#a8642f,#7c4a20);z-index:3}
.pile{width:200px;height:60px;border-radius:50%;background:#b34a28;z-index:4}
.pl1{left:40px;bottom:90px}.pl2{left:220px;bottom:70px;transform:scale(.75)}
""",
html="".join([f'<i class="leaf" style="left:{x}px;top:-40px;--sx:{sx}px;animation-duration:{du}s;animation-delay:{dl}s"></i>'
               for x, sx, du, dl in [(30,90,7,-1),(90,-70,8.5,-3),(150,60,7.6,-5.4),(210,-90,9,-2.2),(270,80,7.2,-6.8),
                                      (330,-60,8.8,-4.4),(60,110,9.4,-7.9),(120,-110,7.8,-.6),(240,40,8.2,-5.9),
                                      (300,100,7.4,-3.3),(180,-40,9.8,-8.6),(360,70,8,-6.2)]])
+ """
<i class="branch"></i><i class="tw tw1"></i><i class="tw tw2"></i>
<i class="ground3"></i><i class="pile pl1"></i><i class="pile pl2"></i>
"""))

# ---------- s54 荷开并蒂 ----------
D.append(dict(file="s54.html", title="莲开时节", brand="莲开时节", sub="LOTUS",
bg="linear-gradient(#c4e6da,#93c6b4 58%,#62a088)",
css="""
.pad{border-radius:50%;background:radial-gradient(circle at 40% 35%,#5da87e,#2f6e4e 75%);z-index:4}
.pd1{width:130px;height:52px;left:36px;top:560px}.pd2{width:100px;height:42px;left:300px;top:620px}.pd3{width:80px;height:34px;left:200px;top:700px}
.ripple{border:2px solid rgba(255,255,255,.55);border-radius:50%;left:215px;top:600px;width:120px;height:44px;margin-left:-60px;transform:scale(.4);opacity:0;animation:rip2 4s ease-out infinite;z-index:5}
.rr2{animation-delay:-2s}
@keyframes rip2{0%{transform:scale(.4);opacity:0}25%{opacity:.85}100%{transform:scale(1.9);opacity:0}}
.lotus{width:0;height:0;left:215px;top:640px;z-index:6}
.pt{left:-27px;bottom:0;width:54px;height:130px;border-radius:50% 50% 8px 8px/100% 100% 8px 8px;background:linear-gradient(#ffc2d4,#ef6a9c);transform:rotate(var(--r)) scale(.15);transform-origin:50% 100%;animation:bloom 1.7s var(--dl) both}
@keyframes bloom{to{transform:rotate(var(--r)) scale(1)}}
.bud{width:44px;height:56px;left:-22px;bottom:0;border-radius:50% 50% 50% 50%/60% 60% 40% 40%;background:radial-gradient(circle at 50% 35%,#ffd9e6,#f0789f 70%);transform:scale(0);animation:bud 1s 1.9s both;z-index:7}
@keyframes bud{to{transform:scale(1)}}
.fly{width:70px;height:26px;z-index:8;animation:flypath 7s ease-in-out infinite}
.fly .bdy{width:34px;height:8px;left:18px;top:9px;border-radius:4px;background:#3a6a8f}
.fly .wg{width:26px;height:12px;top:2px;border-radius:50%;background:rgba(220,240,255,.75);transform-origin:100% 50%}
.wg1{left:2px;animation:wing2 .18s ease-in-out infinite alternate}
.wg2{left:42px;animation:wing2 .18s -.09s ease-in-out infinite alternate}
@keyframes wing2{to{transform:scaleY(.3)}}
@keyframes flypath{0%{left:-80px;top:300px}30%{left:180px;top:220px}55%{left:330px;top:330px}80%{left:120px;top:420px}100%{left:-80px;top:300px}}
""",
html="".join([f'<i class="lotus"><i class="pt" style="--r:{r}deg;--dl:{dl}s"></i></i>'
               for r, dl in [(-72,1.2),(-48,.9),(-24,.6),(0,.3),(24,.6),(48,.9),(72,1.2)]])
+ """<i class="lotus"><i class="bud"></i></i>""" + """
<i class="pad pd1"></i><i class="pad pd2"></i><i class="pad pd3"></i>
<i class="ripple rr1"></i><i class="ripple rr2"></i>
<i class="fly"><i class="bdy"></i><i class="wg wg1"></i><i class="wg wg2"></i></i>
"""))

# ---------- 组装 ----------
OUT = os.path.expanduser("~/workspace/fresh-ui/splash")
titles = []
for d in D:
    html = TPL.replace("__TITLE__", d["title"]).replace("__BRAND__", d["brand"]) \
             .replace("__SUB__", d["sub"]).replace("__BG__", d["bg"]) \
             .replace("__CSS__", d["css"]).replace("__HTML__", d["html"])
    open(os.path.join(OUT, d["file"]), "w", encoding="utf-8").write(html)
    titles.append({"file": d["file"], "title": d["title"]})
json.dump(titles, open(os.path.join(OUT, "_titles_splash_c.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
print("wrote", len(D), "files")
