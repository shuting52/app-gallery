"""part3: s67-s72 + runner, executed with SCENES/TPL/OUT in scope"""

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
