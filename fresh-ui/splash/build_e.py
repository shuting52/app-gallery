#!/usr/bin/env python3
# s73-s90 生成器：18 组启动页
import os, random
random.seed(73)
OUT = os.path.dirname(os.path.abspath(__file__))

BASE_CSS = """*{margin:0;padding:0;box-sizing:border-box}
html,body{height:100%}
body{width:430px;min-height:900px;margin:0 auto;position:relative;overflow:hidden;color:#fff;font-family:-apple-system,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","Noto Sans CJK SC",sans-serif;background:__BG__}
#app{position:absolute;inset:0}
.brand{position:absolute;left:0;right:0;bottom:112px;text-align:center;z-index:10;opacity:0;transform:translateY(16px);animation:brandIn .9s cubic-bezier(.2,.7,.3,1.2) 2.3s both}
.brand h1{font-size:34px;letter-spacing:10px;font-weight:800;text-indent:10px}
.brand p{margin-top:10px;font-size:12px;letter-spacing:5px;opacity:.7;text-indent:5px}
@keyframes brandIn{to{opacity:1;transform:none}}
.tag{position:absolute;top:56px;left:0;right:0;text-align:center;font-size:11px;letter-spacing:8px;text-indent:8px;opacity:0;z-index:10;animation:brandIn 1s ease 2.7s both;color:rgba(255,255,255,.65)}
.replay{position:absolute;left:50%;bottom:42px;transform:translateX(-50%);z-index:20;background:rgba(255,255,255,.13);border:1px solid rgba(255,255,255,.35);color:#fff;border-radius:20px;padding:8px 24px;font-size:13px;letter-spacing:2px;cursor:pointer;backdrop-filter:blur(6px)}
"""

BASE_HTML = """<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>%s</title>
<style>%s
%s</style></head><body><div id="app">%s<div class="tag">%s</div><div class="brand"><h1>%s</h1><p>%s</p></div></div>
<button class="replay">&#8635; 重新播放</button>
<script>document.querySelector('.replay').onclick=function(){var a=document.getElementById('app');var c=a.cloneNode(true);a.replaceWith(c);};</script>
</body></html>"""

def dots(n, cls, lmin=0, lmax=410, dmin=-6, dmax=0, dur=(3,7), extra=""):
    s = []
    for i in range(n):
        l = random.uniform(lmin, lmax)
        d = random.uniform(dmin, dmax)
        t = random.uniform(*dur)
        s.append('<i class="%s" style="left:%.0fpx;animation-delay:%.2fs;animation-duration:%.2fs;%s"></i>' % (cls, l, d, t, extra))
    return "".join(s)

DESIGNS = []

# ---------- s73 火焰纹章 ----------
DESIGNS.append(dict(
    num=73, title="火焰纹章", bg="#160903", tag="FIRE EMBLEM", h1="火焰纹章", sub="燃情而来 · 烈焰新生",
    css="""
.flame{position:absolute;bottom:-30px;width:14px;height:14px;display:block;border-radius:50%;background:radial-gradient(circle,#ffd76e,#ff7a1a 60%,transparent 70%);filter:blur(2px);animation:rise linear infinite}
@keyframes rise{from{transform:translateY(0) scale(1);opacity:0}15%{opacity:1}to{transform:translateY(-880px) scale(.3);opacity:0}}
.emblem{position:absolute;left:50%;top:330px;width:150px;height:170px;transform:translateX(-50%) scale(0);animation:emb 1.1s cubic-bezier(.2,.8,.3,1.4) .7s both;filter:drop-shadow(0 0 26px rgba(255,122,26,.8))}
@keyframes emb{to{transform:translateX(-50%) scale(1)}}
.emblem .sh{position:absolute;inset:0;background:linear-gradient(160deg,#ff9a3c,#e23c0e);clip-path:polygon(50% 0,100% 22%,100% 62%,50% 100%,0 62%,0 22%)}
.emblem .in{position:absolute;inset:16px;background:#160903;clip-path:polygon(50% 0,100% 22%,100% 62%,50% 100%,0 62%,0 22%);display:flex;align-items:center;justify-content:center}
.emblem .in b{font-size:52px;color:#ffb03c;text-shadow:0 0 18px #ff7a1a;animation:flick 1.6s ease-in-out -0.5s infinite}
@keyframes flick{50%{opacity:.75;transform:scale(.94)}}
.glow{position:absolute;left:50%;top:300px;width:340px;height:340px;transform:translateX(-50%);background:radial-gradient(circle,rgba(255,110,20,.35),transparent 70%);animation:glowp 3s ease-in-out -1s infinite}
@keyframes glowp{50%{transform:translateX(-50%) scale(1.12);opacity:.7}}
""",
    html='<div class="glow"></div>' + dots(26, "flame") + '<div class="emblem"><div class="sh"></div><div class="in"><b>&#128293;</b></div></div>',
))

# ---------- s74 鲸落深海 ----------
DESIGNS.append(dict(
    num=74, title="鲸落深海", bg="linear-gradient(180deg,#06283f 0%,#041a2b 60%,#020d16 100%)", tag="DEEP WHALE", h1="鲸落深海", sub="潜入蔚蓝 · 梦境深处",
    css="""
.ray{position:absolute;top:-40px;width:90px;height:700px;display:block;background:linear-gradient(180deg,rgba(140,220,255,.14),transparent);transform:skewX(-12deg);animation:sway 7s ease-in-out infinite alternate}
@keyframes sway{to{transform:skewX(6deg) translateX(30px)}}
.whale{position:absolute;left:50%;top:180px;width:230px;height:120px;margin-left:-115px;animation:dive 3.2s ease-in-out .2s both}
@keyframes dive{from{transform:translateY(-260px) rotate(-8deg);opacity:0}30%{opacity:1}to{transform:translateY(60px) rotate(4deg);opacity:1}}
.whale .bd{position:absolute;left:20px;top:20px;width:170px;height:80px;background:linear-gradient(180deg,#3d6a8f,#16293c);border-radius:50%}
.whale .tl{position:absolute;left:0;top:38px;width:0;height:0;border-top:26px solid transparent;border-bottom:26px solid transparent;border-right:44px solid #16293c;animation:tail 2.2s ease-in-out -0.4s infinite}
@keyframes tail{50%{transform:rotate(14deg)}}
.whale .eye{position:absolute;left:150px;top:44px;width:10px;height:10px;display:block;border-radius:50%;background:#cfeaff}
.whale .fin{position:absolute;left:110px;top:88px;width:52px;height:18px;background:#16293c;border-radius:0 0 26px 26px;transform:rotate(18deg)}
.bub{position:absolute;bottom:-20px;width:10px;height:10px;display:block;border-radius:50%;border:2px solid rgba(160,220,255,.55);animation:rise2 linear infinite}
@keyframes rise2{to{transform:translateY(-860px);opacity:0}}
.sand{position:absolute;bottom:0;left:0;right:0;height:90px;background:radial-gradient(circle at 50% 130%,#0a2f47,#020d16 75%)}
""",
    html='<div class="ray" style="left:60px"></div><div class="ray" style="left:200px;animation-delay:-3s"></div><div class="ray" style="left:320px;animation-delay:-5s"></div>'
         + '<div class="whale"><div class="bd"></div><div class="tl"></div><div class="fin"></div><i class="eye"></i></div>'
         + dots(18, "bub", dur=(4, 8)) + '<div class="sand"></div>',
))

# ---------- s75 风车牧歌 ----------
DESIGNS.append(dict(
    num=75, title="风车牧歌", bg="linear-gradient(180deg,#7ec8f2 0%,#cdeafb 55%,#eef9e6 100%)", tag="WINDMILL", h1="风车牧歌", sub="田野微风 · 转动时光",
    css="""
.cloud{position:absolute;top:90px;width:120px;height:38px;display:block;background:#fff;border-radius:20px;opacity:.9;animation:drift 26s linear infinite}
.cloud::before{content:"";position:absolute;left:24px;top:-20px;width:56px;height:56px;background:#fff;border-radius:50%}
.cloud::after{content:"";position:absolute;left:64px;top:-12px;width:40px;height:40px;background:#fff;border-radius:50%}
@keyframes drift{from{transform:translateX(-160px)}to{transform:translateX(560px)}}
.mill{position:absolute;left:150px;top:300px;width:130px;height:330px}
.mill .tw{position:absolute;bottom:0;left:35px;width:60px;height:300px;background:linear-gradient(180deg,#8a6b4a,#6b4f33);clip-path:polygon(18% 0,82% 0,100% 100%,0 100%)}
.mill .blades{position:absolute;left:65px;top:34px;width:0;height:0;animation:spin 9s linear infinite}
@keyframes spin{to{transform:rotate(360deg)}}
.mill .bl{position:absolute;left:-9px;top:-104px;width:18px;height:104px;display:block;background:linear-gradient(180deg,#f3e3c2,#c9a briefly)}
.mill .bl:nth-child(1){transform:rotate(0deg)}.mill .bl:nth-child(2){transform:rotate(90deg)}
.mill .bl:nth-child(3){transform:rotate(180deg)}.mill .bl:nth-child(4){transform:rotate(270deg)}
.mill .hub{position:absolute;left:53px;top:22px;width:24px;height:24px;display:block;border-radius:50%;background:#4c3a26;z-index:2}
.tulip{position:absolute;bottom:0;width:26px;height:90px;display:block}
.tulip .st{position:absolute;bottom:0;left:12px;width:4px;height:62px;background:#3f7d3a}
.tulip .fl{position:absolute;bottom:58px;left:4px;width:20px;height:28px;background:var(--c,#e2546e);border-radius:50% 50% 40% 40%/60% 60% 40% 40%}
.ground{position:absolute;bottom:0;left:0;right:0;height:150px;background:linear-gradient(180deg,#7cbf6a,#4d8a41)}
.sun{position:absolute;right:60px;top:80px;width:74px;height:74px;display:block;border-radius:50%;background:radial-gradient(circle,#fff6c9,#ffd93d 70%);box-shadow:0 0 44px #ffe98a;animation:sun 5s ease-in-out -2s infinite}
@keyframes sun{50%{transform:scale(1.07)}}
""",
    html='<div class="sun"></div><div class="cloud" style="animation-delay:-4s"></div><div class="cloud" style="top:170px;animation-delay:-16s;transform:scale(.7)"></div>'
         + '<div class="mill"><div class="tw"></div><div class="blades"><i class="bl"></i><i class="bl"></i><i class="bl"></i><i class="bl"></i></div><i class="hub"></i></div>'
         + '<div class="ground"></div>'
         + "".join('<i class="tulip" style="left:%dpx;--c:%s"><span class="st"></span><span class="fl"></span></i>' % (x, c) for x, c in [(30,"#e2546e"),(80,"#f2a03d"),(340,"#e2546e"),(390,"#b678e2"),(250,"#f2a03d")]),
))
DESIGNS[-1]["css"] = DESIGNS[-1]["css"].replace("#c9a briefly", "#c9a06a")
DESIGNS[-1]["html"] = DESIGNS[-1]["html"].replace('<span class="st"></span><span class="fl"></span>', '<i class="st" style="display:block;position:absolute"></i><i class="fl" style="display:block;position:absolute"></i>')

# ---------- s76 纸翼长空 ----------
DESIGNS.append(dict(
    num=76, title="纸翼长空", bg="linear-gradient(180deg,#5aa7e8 0%,#a5d8f5 60%,#e3f3fd 100%)", tag="PAPER PLANE", h1="纸翼长空", sub="折一纸信 · 寄往远方",
    css="""
.plane{position:absolute;top:300px;left:-120px;width:110px;height:60px;display:block;animation:fly 3.4s cubic-bezier(.4,0,.4,1) .2s both;z-index:5}
@keyframes fly{0%{transform:translate(0,0) rotate(6deg);opacity:0}12%{opacity:1}55%{transform:translate(280px,-70px) rotate(-4deg)}100%{transform:translate(560px,20px) rotate(8deg);opacity:0}}
.plane .p{position:absolute;inset:0;background:linear-gradient(135deg,#ffffff,#cfe6f7);clip-path:polygon(0 0,100% 50%,0 100%,28% 50%)}
.plane .f{position:absolute;left:28%;top:50%;width:72%;height:2px;background:#9db8cc;transform:translateY(-50%)}
.trail{position:absolute;top:316px;left:0;width:430px;height:120px}
.trail path{stroke:#ffffff;stroke-width:3;stroke-dasharray:10 12;fill:none;opacity:.8;stroke-dashoffset:440;animation:dash 3.4s linear .2s both}
@keyframes dash{to{stroke-dashoffset:0}}
.c2{position:absolute;width:110px;height:34px;display:block;background:#fff;border-radius:18px;opacity:.85;animation:drift2 30s linear infinite}
.c2::before{content:"";position:absolute;left:22px;top:-18px;width:50px;height:50px;background:#fff;border-radius:50%}
@keyframes drift2{from{transform:translateX(480px)}to{transform:translateX(-160px)}}
.bird{position:absolute;font-size:20px;color:#3d6a8f;animation:flap 1.2s ease-in-out infinite}
@keyframes flap{50%{transform:translateY(-6px) scaleY(.8)}}
""",
    html='<svg class="trail" viewBox="0 0 430 120"><path d="M0,20 Q140,90 280,30 T430,60"/></svg>'
         + '<div class="plane"><div class="p"></div><div class="f"></div></div>'
         + '<div class="c2" style="top:140px;animation-delay:-8s"></div><div class="c2" style="top:520px;animation-delay:-22s"></div>'
         + '<span class="bird" style="left:90px;top:200px;animation-delay:-.3s">~</span><span class="bird" style="left:130px;top:180px;animation-delay:-.8s">~</span><span class="bird" style="left:330px;top:420px;animation-delay:-.5s">~</span>',
))

# ---------- s77 冰川裂变 ----------
DESIGNS.append(dict(
    num=77, title="冰川裂变", bg="linear-gradient(180deg,#0a1626 0%,#0e2740 70%,#123449 100%)", tag="GLACIER", h1="冰川裂变", sub="万年冰封 · 一瞬破晓",
    css="""
.crack{position:absolute;inset:0;width:430px;height:900px}
.crack path{stroke:#9fdcff;stroke-width:3;fill:none;filter:drop-shadow(0 0 8px #6ec6ff);stroke-dasharray:900;stroke-dashoffset:900;animation:crack 2.2s ease-out .3s both}
.crack path:nth-child(2){animation-delay:.8s}.crack path:nth-child(3){animation-delay:1.2s}
@keyframes crack{to{stroke-dashoffset:0}}
.shard{position:absolute;bottom:0;width:0;height:0;display:block;border-left:60px solid transparent;border-right:60px solid transparent;border-bottom:150px solid rgba(140,210,250,.28);animation:rise3 2.4s ease-out .9s both;transform-origin:bottom}
@keyframes rise3{from{transform:translateY(120px) scale(.6);opacity:0}to{transform:translateY(0) scale(1);opacity:1}}
.snow{position:absolute;top:-16px;width:8px;height:8px;display:block;border-radius:50%;background:#dff2ff;animation:fall linear infinite}
@keyframes fall{to{transform:translateY(940px);opacity:.2}}
.iceglow{position:absolute;left:50%;top:200px;width:380px;height:380px;transform:translateX(-50%);background:radial-gradient(circle,rgba(110,198,255,.22),transparent 70%);animation:glowp 4s ease-in-out -2s infinite}
@keyframes glowp{50%{opacity:.6;transform:translateX(-50%) scale(1.1)}}
""",
    html='<div class="iceglow"></div><svg class="crack" viewBox="0 0 430 900"><path d="M215,120 L200,300 L228,470 L198,660 L215,830"/><path d="M208,340 L120,430 L70,560"/><path d="M222,430 L320,520 L370,660"/></svg>'
         + '<div class="shard" style="left:60px"></div><div class="shard" style="left:250px;border-bottom-width:200px;animation-delay:1.1s"></div><div class="shard" style="left:150px;border-bottom-width:110px;animation-delay:1.3s"></div>'
         + dots(30, "snow", dur=(5, 10)),
))

# ---------- s78 蘑菇小屋 ----------
DESIGNS.append(dict(
    num=78, title="蘑菇小屋", bg="linear-gradient(180deg,#0b1030 0%,#16224d 60%,#0a0f24 100%)", tag="MUSHROOM", h1="蘑菇小屋", sub="森林深处 · 微光守候",
    css="""
.star{position:absolute;width:4px;height:4px;display:block;border-radius:50%;background:#fff;animation:tw 2.6s ease-in-out infinite}
@keyframes tw{50%{opacity:.25;transform:scale(.7)}}
.house{position:absolute;left:50%;bottom:190px;width:190px;height:230px;margin-left:-95px;animation:pop 1.2s cubic-bezier(.2,.8,.3,1.3) .5s both;transform-origin:bottom}
@keyframes pop{from{transform:scale(0)}to{transform:scale(1)}}
.house .stem{position:absolute;bottom:0;left:55px;width:80px;height:110px;background:linear-gradient(180deg,#f2e3c8,#d9bd92);border-radius:14px}
.house .door{position:absolute;bottom:0;left:75px;width:40px;height:66px;background:#3a2a18;border-radius:20px 20px 6px 6px;box-shadow:inset 0 0 18px #ffb84d;animation:door 3s ease-in-out -1s infinite}
@keyframes door{50%{box-shadow:inset 0 0 30px #ffcf7d}}
.house .cap{position:absolute;top:0;left:5px;width:180px;height:110px;background:radial-gradient(circle at 50% 30%,#ff6b6b,#c0392b 75%);border-radius:90px 90px 14px 14px}
.house .cap i{position:absolute;display:block;border-radius:50%;background:#ffe9e9}
.ffly{position:absolute;width:7px;height:7px;display:block;border-radius:50%;background:#eaff8a;box-shadow:0 0 12px #eaff8a;animation:fly2 ease-in-out infinite alternate}
@keyframes fly2{to{transform:translate(40px,-60px)}}
.grass{position:absolute;bottom:0;left:0;right:0;height:190px;background:radial-gradient(circle at 50% 130%,#14331c,#070d08 78%)}
""",
    html=dots(40, "star", dur=(2, 4))
         + '<div class="house"><div class="cap"><i style="left:36px;top:34px;width:20px;height:20px"></i><i style="left:86px;top:18px;width:26px;height:26px"></i><i style="left:130px;top:44px;width:16px;height:16px"></i></div><div class="stem"></div><div class="door"></div></div>'
         + '<div class="grass"></div>'
         + "".join('<i class="ffly" style="left:%dpx;top:%dpx;animation-duration:%.1fs;animation-delay:-%.1fs"></i>' % (random.randint(20,400), random.randint(300,700), random.uniform(3,6), random.uniform(0,4)) for _ in range(12)),
))

# ---------- s79 灯塔守夜 ----------
DESIGNS.append(dict(
    num=79, title="灯塔守夜", bg="linear-gradient(180deg,#060b1c 0%,#0a1830 65%,#06101f 100%)", tag="LIGHTHOUSE", h1="灯塔守夜", sub="光束所至 · 皆是归途",
    css="""
.lh{position:absolute;left:50%;bottom:170px;width:120px;height:380px;margin-left:-60px;animation:rise4 1.4s ease-out .4s both}
@keyframes rise4{from{transform:translateY(420px)}to{transform:none}}
.lh .tw{position:absolute;bottom:0;left:30px;width:60px;height:330px;background:repeating-linear-gradient(180deg,#e8e2d4 0 34px,#c0392b 34px 68px);clip-path:polygon(16% 0,84% 0,100% 100%,0 100%)}
.lh .lamp{position:absolute;top:0;left:32px;width:56px;height:56px;background:radial-gradient(circle,#fff8d0,#ffd93d 65%);border-radius:50%;box-shadow:0 0 40px #ffe98a;z-index:2}
.lh .beam{position:absolute;top:14px;left:88px;width:330px;height:70px;display:block;background:linear-gradient(90deg,rgba(255,240,170,.55),transparent);clip-path:polygon(0 42%,100% 0,100% 100%,0 58%);transform-origin:left center;animation:beam 7s linear infinite}
@keyframes beam{to{transform:rotate(360deg)}}
.lh .beam.b2{animation-delay:-3.5s}
.wave{position:absolute;bottom:0;left:0;right:0;height:170px;overflow:hidden}
.wave i{position:absolute;bottom:-70px;left:-60px;width:560px;height:170px;display:block;border-radius:45%;background:rgba(40,90,140,.35);animation:wv 9s linear infinite}
.wave i:nth-child(2){animation-delay:-3s;background:rgba(30,70,115,.4)}
.wave i:nth-child(3){animation-delay:-6s;background:rgba(22,52,88,.5)}
@keyframes wv{to{transform:rotate(360deg)}}
.st2{position:absolute;width:3px;height:3px;display:block;border-radius:50%;background:#fff;animation:tw 3s ease-in-out infinite}
@keyframes tw{50%{opacity:.2}}
""",
    html=dots(36, "st2", dur=(2, 5))
         + '<div class="lh"><div class="beam"></div><div class="beam b2"></div><div class="tw"></div><div class="lamp"></div></div>'
         + '<div class="wave"><i></i><i></i><i></i></div>',
))

# ---------- s80 气球升空 ----------
DESIGNS.append(dict(
    num=80, title="气球升空", bg="linear-gradient(180deg,#f7b267 0%,#f4845f 40%,#a06cd5 100%)", tag="BALLOON", h1="气球升空", sub="乘风而起 · 俯瞰人间",
    css="""
.bal{position:absolute;left:50%;top:560px;width:170px;height:260px;margin-left:-85px;animation:up 3s ease-in-out .3s both}
@keyframes up{from{transform:translateY(240px) scale(.92);opacity:0}to{transform:translateY(-190px);opacity:1}}
.bal .env{position:absolute;top:0;left:0;width:170px;height:150px;background:radial-gradient(circle at 50% 32%,#ff8fa3 0 26px,#ffd6a5 27px 52px,#caffbf 53px 78px,#9bf6ff 79px 104px,transparent 105px);animation:swy 4s ease-in-out -1s infinite}
@keyframes swy{50%{transform:rotate(3deg) translateX(8px)}}
.bal .ropes{position:absolute;top:140px;left:55px;width:60px;height:44px;border-left:3px solid #5b3a29;border-right:3px solid #5b3a29}
.bal .bask{position:absolute;top:182px;left:62px;width:46px;height:38px;background:linear-gradient(180deg,#8a5a3b,#5b3a29);border-radius:6px}
.bal .fire{position:absolute;top:160px;left:78px;width:14px;height:22px;display:block;background:radial-gradient(circle,#fff3b0,#ff9f1c 65%,transparent 75%);border-radius:50%;animation:flick2 .5s ease-in-out infinite alternate}
@keyframes flick2{to{transform:scaleY(1.35)}}
.cl3{position:absolute;width:130px;height:40px;display:block;background:rgba(255,255,255,.85);border-radius:22px;animation:drift3 linear infinite}
.cl3::before{content:"";position:absolute;left:26px;top:-22px;width:60px;height:60px;background:rgba(255,255,255,.85);border-radius:50%}
@keyframes drift3{from{transform:translateX(480px)}to{transform:translateX(-180px)}}
.bird2{position:absolute;color:#4a2c3f;font-size:18px;animation:flap 1.4s ease-in-out infinite}
@keyframes flap{50%{transform:translateY(-7px)}}
""",
    html='<div class="bal"><div class="env"></div><div class="ropes"></div><div class="fire"></div><div class="bask"></div></div>'
         + '<div class="cl3" style="top:180px;animation-duration:34s;animation-delay:-10s"></div><div class="cl3" style="top:420px;animation-duration:44s;animation-delay:-30s"></div><div class="cl3" style="top:640px;animation-duration:38s;animation-delay:-4s"></div>'
         + '<span class="bird2" style="left:70px;top:260px">﹏</span><span class="bird2" style="left:110px;top:240px;animation-delay:-.6s">﹏</span>',
))

# ---------- s81 彩虹飞桥 ----------
DESIGNS.append(dict(
    num=81, title="彩虹飞桥", bg="linear-gradient(180deg,#8ecae6 0%,#cfeefb 55%,#f4fbff 100%)", tag="RAINBOW", h1="彩虹飞桥", sub="雨过天晴 · 虹销雨霁",
    css="""
.rb{position:absolute;left:50%;bottom:150px;width:560px;height:280px;margin-left:-280px}
.rb i{position:absolute;left:50%;bottom:0;display:block;border-radius:50%;border:16px solid transparent;border-bottom:0;transform:translateX(-50%) scaleY(0);transform-origin:bottom;animation:arc 1.6s ease-out both}
.rb i:nth-child(1){width:520px;height:260px;border-top-color:#ff5d5d;animation-delay:.2s}
.rb i:nth-child(2){width:456px;height:228px;border-top-color:#ff9f45;animation-delay:.35s}
.rb i:nth-child(3){width:392px;height:196px;border-top-color:#ffd93d;animation-delay:.5s}
.rb i:nth-child(4){width:328px;height:164px;border-top-color:#6fbf6f;animation-delay:.65s}
.rb i:nth-child(5){width:264px;height:132px;border-top-color:#5aa7e8;animation-delay:.8s}
.rb i:nth-child(6){width:200px;height:100px;border-top-color:#b678e2;animation-delay:.95s}
@keyframes arc{to{transform:translateX(-50%) scaleY(1)}}
.sun2{position:absolute;left:56px;top:110px;width:80px;height:80px;display:block;border-radius:50%;background:radial-gradient(circle,#fff8d6,#ffd93d 70%);box-shadow:0 0 50px #ffefa0;animation:sun 2s ease-out .2s both}
@keyframes sun{from{transform:scale(0)}to{transform:scale(1)}}
.drop{position:absolute;top:-20px;width:5px;height:16px;display:block;border-radius:40%;background:rgba(120,180,230,.7);animation:fall2 linear infinite}
@keyframes fall2{to{transform:translateY(700px);opacity:0}}
.hill{position:absolute;bottom:0;left:0;right:0;height:150px;background:radial-gradient(circle at 20% 130%,#6faf62,#3c7a44 70%)}
""",
    html='<div class="sun2"></div><div class="rb"><i></i><i></i><i></i><i></i><i></i><i></i></div><div class="hill"></div>' + dots(24, "drop", dur=(1.2, 2.2)),
))

# ---------- s82 雪花结晶 ----------
DESIGNS.append(dict(
    num=82, title="雪花结晶", bg="linear-gradient(180deg,#0a1a33 0%,#10294f 60%,#0a1a33 100%)", tag="SNOWFLAKE", h1="雪花结晶", sub="冰姿玉骨 · 六出纷飞",
    css="""
.flake{position:absolute;left:50%;top:300px;width:220px;height:220px;margin-left:-110px;animation:form 2s ease-out .3s both}
@keyframes form{from{transform:scale(.2) rotate(-40deg);opacity:0}to{transform:scale(1) rotate(0);opacity:1}}
.flake .core{position:absolute;left:50%;top:50%;width:200px;height:200px;margin:-100px 0 0 -100px;animation:spin2 24s linear infinite}
@keyframes spin2{to{transform:rotate(360deg)}}
.flake .sp{position:absolute;left:50%;top:50%;width:6px;height:190px;margin:-95px 0 0 -3px;display:block;background:linear-gradient(180deg,transparent,#bfe3ff 30%,#bfe3ff 70%,transparent);border-radius:3px}
.flake .sp:nth-child(1){transform:rotate(0deg)}.flake .sp:nth-child(2){transform:rotate(60deg)}.flake .sp:nth-child(3){transform:rotate(120deg)}
.flake .ct{position:absolute;left:50%;top:50%;width:26px;height:26px;margin:-13px 0 0 -13px;display:block;border-radius:50%;background:radial-gradient(circle,#fff,#9fd0ff 70%);box-shadow:0 0 26px #bfe3ff}
.snw{position:absolute;top:-14px;width:7px;height:7px;display:block;border-radius:50%;background:#e8f4ff;animation:fall3 linear infinite}
@keyframes fall3{to{transform:translateY(940px) rotate(200deg);opacity:.3}}
.halo{position:absolute;left:50%;top:230px;width:360px;height:360px;transform:translateX(-50%);background:radial-gradient(circle,rgba(150,200,255,.18),transparent 70%);animation:glowp 5s ease-in-out -2s infinite}
@keyframes glowp{50%{opacity:.55}}
""",
    html='<div class="halo"></div><div class="flake"><div class="core"><i class="sp"></i><i class="sp"></i><i class="sp"></i></div><i class="ct"></i></div>' + dots(34, "snw", dur=(5, 11)),
))

# ---------- s83 火山苏醒 ----------
DESIGNS.append(dict(
    num=83, title="火山苏醒", bg="linear-gradient(180deg,#12060a 0%,#2b0f14 55%,#0b0406 100%)", tag="VOLCANO", h1="火山苏醒", sub="地心之火 · 喷薄而出",
    css="""
.volc{position:absolute;bottom:120px;left:50%;width:380px;height:300px;margin-left:-190px;background:linear-gradient(180deg,#3a1c22,#170a0d);clip-path:polygon(38% 0,62% 0,100% 100%,0 100%);animation:rise5 1.6s ease-out .3s both}
@keyframes rise5{from{transform:translateY(320px)}to{transform:none}}
.volc .lava{position:absolute;top:-6px;left:50%;width:120px;height:26px;margin-left:-60px;background:radial-gradient(circle,#ffd76e,#ff5a1a 60%,transparent 75%);border-radius:50%;animation:lava 1.8s ease-in-out -0.6s infinite}
@keyframes lava{50%{transform:scaleX(1.25);opacity:.85}}
.ember{position:absolute;bottom:400px;width:9px;height:9px;display:block;border-radius:50%;background:radial-gradient(circle,#ffe08a,#ff6a1a 65%);animation:erupt ease-out infinite}
@keyframes erupt{0%{transform:translate(0,0) scale(1);opacity:1}100%{transform:translate(var(--x,40px),-460px) scale(.3);opacity:0}}
.smoke{position:absolute;bottom:430px;left:50%;width:60px;height:60px;margin-left:-30px;display:block;border-radius:50%;background:rgba(120,110,115,.35);filter:blur(10px);animation:smk 5s ease-out infinite}
@keyframes smk{from{transform:translateY(0) scale(.6);opacity:.7}to{transform:translateY(-260px) scale(1.8);opacity:0}}
.flow{position:absolute;bottom:120px;left:50%;width:26px;height:250px;margin-left:-13px;background:linear-gradient(180deg,#ff8a2a,#c22e0e);filter:blur(3px);border-radius:12px;animation:flowdn 2.6s ease-in-out 1s both;transform-origin:top}
@keyframes flowdn{from{transform:scaleY(0)}to{transform:scaleY(1)}}
""",
    html='<div class="volc"><div class="lava"></div></div><div class="flow"></div>'
         + "".join('<i class="ember" style="left:%dpx;animation-duration:%.1fs;animation-delay:-%.1fs;--x:%dpx"></i>' % (random.randint(150,280), random.uniform(2.2,3.6), random.uniform(0,3), random.randint(-120,120)) for _ in range(26))
         + "".join('<i class="smoke" style="animation-delay:-%.1fs"></i>' % random.uniform(0,5) for _ in range(6)),
))

# ---------- s84 摩天轮转 ----------
DESIGNS.append(dict(
    num=84, title="摩天轮转", bg="linear-gradient(180deg,#2b1b4d 0%,#7a3b6e 55%,#e88ca0 100%)", tag="FERRIS WHEEL", h1="摩天轮转", sub="缓缓转动 · 俯瞰星城",
    css="""
.fw{position:absolute;left:50%;bottom:150px;width:330px;height:400px;margin-left:-165px;animation:rise6 1.5s ease-out .3s both}
@keyframes rise6{from{transform:translateY(430px)}to{transform:none}}
.fw .leg{position:absolute;bottom:0;left:50%;width:14px;height:150px;margin-left:-7px;background:#2b1b3d}
.fw .wheel{position:absolute;left:50%;top:0;width:300px;height:300px;margin-left:-150px;animation:spin3 26s linear infinite}
@keyframes spin3{to{transform:rotate(360deg)}}
.fw .rim{position:absolute;inset:0;border:10px solid rgba(255,220,235,.9);border-radius:50%;box-shadow:0 0 30px rgba(255,180,210,.6)}
.fw .spoke{position:absolute;left:50%;top:50%;width:6px;height:290px;margin:-145px 0 0 -3px;display:block;background:rgba(255,220,235,.75)}
.fw .spoke:nth-child(2){transform:rotate(45deg)}.fw .spoke:nth-child(3){transform:rotate(90deg)}.fw .spoke:nth-child(4){transform:rotate(135deg)}
.fw .cab{position:absolute;width:26px;height:26px;display:block;border-radius:8px;background:linear-gradient(180deg,#ffe9a8,#ffb84d);box-shadow:0 0 14px #ffd93d}
.fw .hub{position:absolute;left:50%;top:50%;width:26px;height:26px;margin:-13px 0 0 -13px;display:block;border-radius:50%;background:#fff;z-index:2}
.city{position:absolute;bottom:0;left:0;right:0;height:150px;background:#1c1030}
.city i{position:absolute;bottom:0;display:block;background:#1c1030}
.win{position:absolute;width:5px;height:7px;display:block;background:#ffe98a;animation:tw2 3s ease-in-out infinite}
@keyframes tw2{50%{opacity:.3}}
.st3{position:absolute;width:3px;height:3px;display:block;border-radius:50%;background:#fff;animation:tw2 2.8s ease-in-out infinite}
""",
    html=dots(30, "st3", dur=(2, 4))
         + '<div class="fw"><div class="leg"></div><div class="wheel"><div class="rim"></div><i class="spoke"></i><i class="spoke"></i><i class="spoke"></i><i class="spoke"></i>'
         + "".join('<i class="cab" style="left:%.0fpx;top:%.0fpx"></i>' % (150+132*__import__("math").cos(a)-13, 150+132*__import__("math").sin(a)-13) for a in [i*0.785 for i in range(8)])
         + '<i class="hub"></i></div></div>'
         + '<div class="city">' + "".join('<i style="left:%dpx;width:%dpx;height:%dpx"></i>' % (x, w, h) for x, w, h in [(0,60,70),(70,44,110),(124,60,80),(300,52,120),(362,68,90)]) + "</div>"
         + "".join('<i class="win" style="left:%dpx;bottom:%dpx;animation-delay:-%.1fs"></i>' % (random.randint(6,420), random.randint(20,110), random.uniform(0,3)) for _ in range(26)),
))

# ---------- s85 帆影远航 ----------
DESIGNS.append(dict(
    num=85, title="帆影远航", bg="linear-gradient(180deg,#ffd9a0 0%,#ff9e7d 45%,#7a4a6e 100%)", tag="SAIL AWAY", h1="帆影远航", sub="扬帆起航 · 星辰大海",
    css="""
.sun3{position:absolute;left:50%;top:330px;width:120px;height:120px;margin-left:-60px;display:block;border-radius:50%;background:radial-gradient(circle,#fff3c4,#ffb84d 70%);box-shadow:0 0 70px #ffcf7d;animation:sunb 2s ease-out .2s both}
@keyframes sunb{from{transform:scale(.4);opacity:0}to{transform:scale(1);opacity:1}}
.sea{position:absolute;bottom:0;left:0;right:0;height:330px;background:linear-gradient(180deg,#b4526e,#3d2148);overflow:hidden}
.sea .gl{position:absolute;top:0;left:50%;width:130px;height:330px;transform:translateX(-50%);background:linear-gradient(180deg,rgba(255,200,120,.5),transparent)}
.boat{position:absolute;left:50%;bottom:190px;width:170px;height:170px;margin-left:-85px;animation:sail 3s ease-in-out .4s both, bob 4s ease-in-out 3.4s infinite}
@keyframes sail{from{transform:translateX(-320px)}to{transform:translateX(0)}}
@keyframes bob{50%{transform:translateY(-10px) rotate(-2deg)}}
.boat .hull{position:absolute;bottom:0;left:15px;width:140px;height:44px;background:#3a2030;clip-path:polygon(0 0,100% 0,82% 100%,18% 100%)}
.boat .mast{position:absolute;bottom:40px;left:82px;width:6px;height:110px;background:#3a2030}
.boat .s1{position:absolute;bottom:44px;left:88px;width:0;height:0;border-left:64px solid #fdf6ec;border-top:100px solid transparent;border-bottom:6px solid transparent}
.boat .s2{position:absolute;bottom:44px;left:26px;width:0;height:0;border-right:52px solid #f2ddc0;border-top:78px solid transparent;border-bottom:6px solid transparent}
.gull{position:absolute;color:#3a2030;font-size:20px;animation:glide 6s ease-in-out infinite alternate}
@keyframes glide{to{transform:translateX(60px)}}
.wv2{position:absolute;bottom:60px;left:0;right:0;height:26px;overflow:hidden;opacity:.5}
.wv2 i{position:absolute;top:0;width:120px;height:26px;display:block;border-top:4px solid rgba(255,255,255,.5);border-radius:50%;animation:mv 7s linear infinite}
@keyframes mv{from{transform:translateX(-140px)}to{transform:translateX(480px)}}
""",
    html='<div class="sun3"></div><div class="sea"><div class="gl"></div><div class="wv2"><i style="animation-delay:-2s"></i><i style="animation-delay:-5s;top:12px"></i></div></div>'
         + '<div class="boat"><div class="s1"></div><div class="s2"></div><div class="mast"></div><div class="hull"></div></div>'
         + '<span class="gull" style="left:80px;top:200px">﹏</span><span class="gull" style="left:300px;top:150px;animation-delay:-3s">﹏</span>',
))

# ---------- s86 流星之夜 ----------
DESIGNS.append(dict(
    num=86, title="流星之夜", bg="linear-gradient(180deg,#04061a 0%,#0a1030 60%,#05081a 100%)", tag="METEOR", h1="流星之夜", sub="许个心愿 · 坠入星河",
    css="""
.meteor{position:absolute;top:-60px;width:180px;height:3px;display:block;background:linear-gradient(90deg,#fff,rgba(160,200,255,0));border-radius:2px;transform:rotate(32deg);animation:shoot linear infinite}
@keyframes shoot{0%{transform:translate(0,0) rotate(32deg);opacity:0}8%{opacity:1}100%{transform:translate(-420px,300px) rotate(32deg);opacity:0}}
.st4{position:absolute;display:block;border-radius:50%;background:#fff;animation:tw3 3s ease-in-out infinite}
@keyframes tw3{50%{opacity:.25}}
.dipper{position:absolute;left:90px;top:150px;width:150px;height:120px}
.dipper i{position:absolute;width:9px;height:9px;display:block;border-radius:50%;background:#dff0ff;box-shadow:0 0 10px #bfe0ff}
.mtn{position:absolute;bottom:0;left:0;right:0;height:200px;background:linear-gradient(180deg,transparent,#0a1230 40%)}
.mtn::before{content:"";position:absolute;bottom:0;left:-40px;width:260px;height:190px;background:#0a1230;clip-path:polygon(50% 0,100% 100%,0 100%)}
.mtn::after{content:"";position:absolute;bottom:0;right:-30px;width:300px;height:150px;background:#0d1738;clip-path:polygon(50% 0,100% 100%,0 100%)}
.moon{position:absolute;right:70px;top:120px;width:66px;height:66px;display:block;border-radius:50%;background:radial-gradient(circle at 35% 35%,#fdfbf0,#d8d2b8 75%);box-shadow:0 0 34px rgba(250,246,220,.5)}
""",
    html='<div class="moon"></div><div class="dipper"><i style="left:10px;top:20px"></i><i style="left:45px;top:8px"></i><i style="left:82px;top:16px"></i><i style="left:112px;top:44px"></i><i style="left:96px;top:82px"></i><i style="left:60px;top:96px"></i><i style="left:30px;top:70px"></i></div>'
         + "".join('<i class="meteor" style="left:%dpx;top:%dpx;animation-duration:%.1fs;animation-delay:-%.1fs"></i>' % (random.randint(200,560), random.randint(0,300), random.uniform(2.4,4.2), random.uniform(0,4)) for _ in range(9))
         + dots(60, "st4", dur=(2, 5)) + '<div class="mtn"></div>',
))

# ---------- s87 樱吹雪 ----------
DESIGNS.append(dict(
    num=87, title="樱吹雪", bg="linear-gradient(180deg,#ffd9e8 0%,#ffc2d9 45%,#f7a8c4 100%)", tag="SAKURA", h1="樱吹雪", sub="花瓣如雪 · 纷纷而落",
    css="""
.petal{position:absolute;top:-30px;width:20px;height:26px;display:block;background:radial-gradient(circle at 40% 35%,#ffe3ee,#f78fb3 75%);border-radius:60% 60% 60% 0;animation:petal linear infinite}
@keyframes petal{0%{transform:translate(0,0) rotate(0)}100%{transform:translate(var(--sx,60px),960px) rotate(560deg)}}
.branch{position:absolute;top:0;right:-30px;width:220px;height:120px;background:#5b3a33;border-radius:0 0 0 100%;transform:rotate(-14deg);transform-origin:right top;animation:grow 1.6s ease-out .2s both}
@keyframes grow{from{transform:rotate(-14deg) scaleX(0)}to{transform:rotate(-14deg) scaleX(1)}}
.blossom{position:absolute;width:22px;height:22px;display:block}
.blossom i{position:absolute;left:50%;top:50%;width:11px;height:11px;display:block;background:#ffb3cd;border-radius:50% 50% 50% 0;transform-origin:left top}
.blossom i:nth-child(1){transform:rotate(0) translate(9px,-5px)}
.blossom i:nth-child(2){transform:rotate(72deg) translate(9px,-5px)}
.blossom i:nth-child(3){transform:rotate(144deg) translate(9px,-5px)}
.blossom i:nth-child(4){transform:rotate(216deg) translate(9px,-5px)}
.blossom i:nth-child(5){transform:rotate(288deg) translate(9px,-5px)}
.blossom .cc{position:absolute;left:50%;top:50%;width:8px;height:8px;margin:-4px 0 0 -4px;display:block;border-radius:50%;background:#ffdf8a}
.pagoda{position:absolute;bottom:120px;left:60px;width:110px;height:170px;animation:rise7 1.6s ease-out .5s both}
@keyframes rise7{from{transform:translateY(200px);opacity:0}to{transform:none;opacity:1}}
.pagoda .bd2{position:absolute;bottom:0;left:25px;width:60px;height:120px;background:#7a4a3a}
.pagoda .rf{position:absolute;left:5px;width:100px;height:26px;background:#4a2c24;clip-path:polygon(50% 0,100% 100%,0 100%)}
""",
    html='<div class="branch"></div>'
         + "".join('<div class="blossom" style="left:%dpx;top:%dpx;transform:scale(%.2f)"><i></i><i></i><i></i><i></i><i></i><span class="cc" style="display:block;position:absolute"></span></div>' % (random.randint(230,400), random.randint(20,110), random.uniform(.7,1.2)) for _ in range(7))
         + '<div class="pagoda"><div class="bd2"></div><div class="rf" style="bottom:118px"></div><div class="rf" style="bottom:76px;left:12px;width:86px"></div></div>'
         + "".join('<i class="petal" style="left:%dpx;animation-duration:%.1fs;animation-delay:-%.1fs;--sx:%dpx"></i>' % (random.randint(0,410), random.uniform(5,9), random.uniform(0,8), random.randint(-90,90)) for _ in range(30)),
))

# ---------- s88 沙漠驼铃 ----------
DESIGNS.append(dict(
    num=88, title="沙漠驼铃", bg="linear-gradient(180deg,#ff9e5e 0%,#f76b3c 45%,#b23a48 100%)", tag="DESERT", h1="沙漠驼铃", sub="大漠孤烟 · 驼铃古道",
    css="""
.sun4{position:absolute;left:50%;top:210px;width:130px;height:130px;margin-left:-65px;display:block;border-radius:50%;background:radial-gradient(circle,#fff0c0,#ffb84d 68%);box-shadow:0 0 80px #ff9e5e;animation:sunb 2s ease-out .2s both}
@keyframes sunb{from{transform:scale(.4);opacity:0}to{transform:scale(1);opacity:1}}
.dune{position:absolute;bottom:0;left:-60px;width:560px;height:300px}
.dune.d1{background:radial-gradient(circle at 30% 120%,#e88a4a,#c25e2e 70%);border-radius:50% 50% 0 0/100% 100% 0 0}
.dune.d2{background:radial-gradient(circle at 70% 130%,#d9753a,#a84e26 72%);border-radius:50% 50% 0 0/90% 90% 0 0;bottom:-40px}
.camel{position:absolute;bottom:150px;left:-120px;width:110px;height:90px;animation:walk 4s linear .5s both}
@keyframes walk{to{transform:translateX(620px)}}
.camel .bd3{position:absolute;top:26px;left:14px;width:70px;height:32px;background:#2e1a10;border-radius:16px}
.camel .bd3::before{content:"";position:absolute;top:-14px;left:24px;width:26px;height:26px;background:#2e1a10;border-radius:50%}
.camel .nk{position:absolute;top:2px;left:74px;width:12px;height:44px;background:#2e1a10;transform:rotate(24deg)}
.camel .hd{position:absolute;top:0;left:88px;width:20px;height:14px;background:#2e1a10;border-radius:8px}
.camel .lg{position:absolute;top:56px;width:9px;height:34px;display:block;background:#2e1a10;animation:leg 1s ease-in-out infinite alternate}
.camel .lg:nth-child(odd){animation-delay:-.5s}
@keyframes leg{to{transform:rotate(16deg)}}
.winds{position:absolute;top:340px;width:200px;height:4px;display:block;background:linear-gradient(90deg,transparent,rgba(255,220,170,.6),transparent);border-radius:2px;animation:wind linear infinite}
@keyframes wind{from{transform:translateX(480px)}to{transform:translateX(-240px)}}
""",
    html='<div class="sun4"></div><div class="dune d1"></div><div class="dune d2"></div>'
         + '<div class="camel"><div class="bd3"></div><div class="nk"></div><div class="hd"></div><i class="lg" style="left:24px"></i><i class="lg" style="left:42px"></i><i class="lg" style="left:62px"></i><i class="lg" style="left:78px"></i></div>'
         + '<div class="winds" style="animation-duration:9s;animation-delay:-3s"></div><div class="winds" style="top:420px;animation-duration:12s;animation-delay:-8s"></div>',
))

# ---------- s89 冰海企鹅 ----------
DESIGNS.append(dict(
    num=89, title="冰海企鹅", bg="linear-gradient(180deg,#a8d8f0 0%,#d8ecf7 55%,#eef7fc 100%)", tag="PENGUIN", h1="冰海企鹅", sub="极地之约 · 冰雪朋友",
    css="""
.floe{position:absolute;bottom:110px;left:50%;width:330px;height:130px;margin-left:-165px;background:linear-gradient(180deg,#ffffff,#cfe4f2);border-radius:50%;box-shadow:0 14px 30px rgba(120,160,190,.4);animation:float 5s ease-in-out -2s infinite}
@keyframes float{50%{transform:translateY(-12px) rotate(1deg)}}
.pg{position:absolute;left:50%;bottom:190px;width:96px;height:140px;margin-left:-48px;animation:pgin 1.4s cubic-bezier(.2,.8,.3,1.3) .6s both;transform-origin:bottom}
@keyframes pgin{from{transform:scale(0)}to{transform:scale(1)}}
.pg .bdy{position:absolute;inset:0;background:linear-gradient(180deg,#2b3440,#12161d);border-radius:48px 48px 40px 40px}
.pg .bly{position:absolute;left:18px;top:44px;width:60px;height:84px;background:#fdfdfd;border-radius:50%}
.pg .e1,.pg .e2{position:absolute;top:30px;width:12px;height:14px;display:block;border-radius:50%;background:#fff}
.pg .e1{left:30px}.pg .e2{left:54px}
.pg .e1::after,.pg .e2::after{content:"";position:absolute;left:3px;top:4px;width:6px;height:7px;background:#12161d;border-radius:50%}
.pg .bk{position:absolute;left:40px;top:48px;width:0;height:0;border-left:8px solid transparent;border-right:8px solid transparent;border-top:12px solid #ff9f1c}
.pg .ft{position:absolute;bottom:-8px;width:26px;height:12px;display:block;background:#ff9f1c;border-radius:50%}
.pg .ft.f1{left:16px}.pg .ft.f2{left:54px}
.pg .wg{position:absolute;top:64px;width:16px;height:56px;display:block;background:#1c232e;border-radius:50%;animation:wave2 2.4s ease-in-out -1s infinite}
.pg .wg.w1{left:-8px;transform-origin:top}.pg .wg.w2{right:-8px;transform-origin:top}
@keyframes wave2{50%{transform:rotate(24deg)}}
.ice2{position:absolute;bottom:60px;width:54px;height:34px;display:block;background:linear-gradient(180deg,#fff,#cfe4f2);border-radius:50%;animation:float 6s ease-in-out infinite}
.sea2{position:absolute;bottom:0;left:0;right:0;height:150px;background:linear-gradient(180deg,#7fb8dd,#4a86b8)}
.snw2{position:absolute;top:-12px;width:8px;height:8px;display:block;border-radius:50%;background:#fff;animation:fall4 linear infinite}
@keyframes fall4{to{transform:translateY(940px)}}
.sun5{position:absolute;left:60px;top:90px;width:64px;height:64px;display:block;border-radius:50%;background:radial-gradient(circle,#fffbe8,#ffe98a 70%);box-shadow:0 0 36px #fff3b0}
""",
    html='<div class="sun5"></div><div class="sea2"></div><div class="floe"></div>'
         + '<div class="pg"><div class="bdy"></div><div class="bly"></div><i class="e1"></i><i class="e2"></i><div class="bk"></div><i class="wg w1"></i><i class="wg w2"></i><i class="ft f1"></i><i class="ft f2"></i></div>'
         + '<div class="ice2" style="left:40px;animation-delay:-2s"></div><div class="ice2" style="left:340px;animation-delay:-4s"></div>'
         + dots(26, "snw2", dur=(6, 11)),
))

# ---------- s90 竹林听雨 ----------
DESIGNS.append(dict(
    num=90, title="竹林听雨", bg="linear-gradient(180deg,#dfeee4 0%,#bcd8c4 50%,#8fb89a 100%)", tag="BAMBOO RAIN", h1="竹林听雨", sub="翠竹摇曳 · 雨打芭蕉",
    css="""
.bamboo{position:absolute;bottom:0;width:26px;display:block;background:linear-gradient(90deg,#4e8a52,#6fae6a 45%,#4e8a52);border-radius:8px;animation:swayb 5s ease-in-out infinite alternate;transform-origin:bottom}
@keyframes swayb{to{transform:rotate(2.4deg)}}
.bamboo::before{content:"";position:absolute;left:0;right:0;top:38%;height:5px;background:rgba(40,80,45,.5)}
.bamboo::after{content:"";position:absolute;left:0;right:0;top:68%;height:5px;background:rgba(40,80,45,.5)}
.leaf{position:absolute;width:44px;height:16px;display:block;background:linear-gradient(90deg,#3f7d44,#6fae6a);border-radius:50% 0 50% 0;transform-origin:left center;animation:leafw 3s ease-in-out infinite alternate}
@keyframes leafw{to{transform:rotate(-14deg)}}
.rainlayer{position:absolute;left:-40px;right:-40px;top:-320px;height:1280px;pointer-events:none;background:repeating-linear-gradient(93deg,transparent 0 44px,rgba(110,160,195,.5) 44px 47px,transparent 47px 96px);animation:rainfall 1.5s linear infinite}
.rainlayer.r2{background:repeating-linear-gradient(93deg,transparent 0 90px,rgba(110,160,195,.35) 90px 94px,transparent 94px 190px);animation-duration:2.3s}
@keyframes rainfall{from{top:-320px}to{top:-20px}}
.mist{position:absolute;bottom:200px;left:-60px;width:560px;height:120px;display:block;background:radial-gradient(circle,rgba(255,255,255,.5),transparent 70%);filter:blur(18px);animation:mistm 11s ease-in-out infinite alternate}
@keyframes mistm{to{transform:translateX(70px)}}
.stone{position:absolute;bottom:60px;left:150px;width:130px;height:56px;background:radial-gradient(circle at 40% 30%,#9aa5a0,#5f6a64);border-radius:50%}
""",
    html='<div class="rainlayer"></div><div class="rainlayer r2"></div><div class="mist"></div>'
         + "".join('<i class="bamboo" style="left:%dpx;height:%dpx;animation-delay:-%.1fs"></i>' % (x, h, random.uniform(0,5)) for x, h in [(24,640),(70,760),(330,700),(376,600),(150,560),(250,620)])
         + "".join('<i class="leaf" style="left:%dpx;top:%dpx;transform:rotate(%ddeg);animation-delay:-%.1fs"></i>' % (random.randint(20,380), random.randint(180,560), random.randint(-30,30), random.uniform(0,3)) for _ in range(10))
         + '<div class="stone"></div>'
         
))

def build():
    titles = []
    for d in DESIGNS:
        # 手工组装，避免 % 转义问题
        page = ("<!DOCTYPE html><html lang=\"zh-CN\"><head><meta charset=\"utf-8\">"
                "<meta name=\"viewport\" content=\"width=device-width,initial-scale=1\"><title>" + d["title"] + "</title>"
                "<style>" + BASE_CSS.replace("__BG__", d["bg"]) + d["css"] + "</style></head><body><div id=\"app\">" + d["html"]
                + "<div class=\"tag\">" + d["tag"] + "</div><div class=\"brand\"><h1>" + d["h1"] + "</h1><p>" + d["sub"] + "</p></div></div>"
                + "<button class=\"replay\">&#8635; 重新播放</button>"
                + "<script>document.querySelector('.replay').onclick=function(){var a=document.getElementById('app');var c=a.cloneNode(true);a.replaceWith(c);};</script></body></html>")
        fn = "s%02d.html" % d["num"]
        open(os.path.join(OUT, fn), "w", encoding="utf-8").write(page)
        titles.append({"file": fn, "title": d["title"]})
    import json
    json.dump(titles, open(os.path.join(OUT, "_titles_splash_e.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("built", len(titles))

if __name__ == "__main__":
    build()
