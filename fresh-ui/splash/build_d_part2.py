"""part2: s61-s66, executed with SCENES/TPL/OUT in scope"""

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
