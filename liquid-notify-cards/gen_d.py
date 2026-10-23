#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成 n31–n40 液态玻璃通知卡（音乐运动方向）"""
import os

DIR = os.path.dirname(os.path.abspath(__file__))

BASE_CSS = """
*{box-sizing:border-box}
body{min-height:100vh;margin:0;padding:48px 18px;color:%(fg)s;
font:15px/1.45 -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
background:%(bg)s;background-attachment:fixed}
main{width:min(440px,100%%);margin:0 auto;display:grid;gap:18px}
.heading{padding:4px 6px 8px}
.eyebrow{margin:0 0 8px;color:%(dim)s;font-size:11px;letter-spacing:.18em}
h1{margin:0;font-size:30px;letter-spacing:-.04em}
.hint{margin:7px 0 0;color:%(dim)s}
.card{position:relative;isolation:isolate;overflow:hidden;padding:18px;
border:1px solid %(bdc)s;border-radius:%(br)s;
background:%(cardbg)s;
-webkit-backdrop-filter:blur(%(blur)spx) saturate(%(sat)s%%);
backdrop-filter:blur(%(blur)spx) saturate(%(sat)s%%);
box-shadow:inset 0 1px 0 %(inset)s,inset 0 -1px 0 rgba(255,255,255,.08),0 20px 48px %(shd)s;
transition:transform .25s ease,border-color .25s ease}
.card::before{content:"";position:absolute;z-index:0;inset:0;border-radius:inherit;pointer-events:none;
background:linear-gradient(%(hldeg)s,rgba(255,255,255,.34) 0%%,rgba(255,255,255,.08) 18%%,
transparent 42%%,transparent 72%%,%(hltint)s 100%%);opacity:.8}
.card::after{content:"";position:absolute;z-index:0;top:%(ab_t)s;right:%(ab_r)s;
width:%(ab_w)s;height:%(ab_h)s;border:1px solid rgba(255,255,255,.22);border-radius:50%%;
background:radial-gradient(ellipse,rgba(255,255,255,.22),transparent 68%%);
filter:blur(2px);transform:rotate(%(ab_rot)s);pointer-events:none}
.card>*{position:relative;z-index:1}
.card:hover{transform:translateY(-3px);border-color:%(bdh)s}
.top,.title-line{display:flex;align-items:center;justify-content:space-between;gap:12px}
.top{margin-bottom:17px}
.pill{padding:6px 12px;border:1px solid %(bdc)s;border-radius:999px;background:rgba(255,255,255,.10);
color:%(fg)s;font-size:12px;box-shadow:inset 0 1px rgba(255,255,255,.18);white-space:nowrap}
.avatars{display:flex;align-items:center;padding-left:8px}
.avatar{display:grid;width:29px;height:29px;margin-left:-8px;place-items:center;
border:1px solid rgba(255,255,255,.55);border-radius:50%%;background:linear-gradient(135deg,%(av)s);
color:#fff;font-size:11px;box-shadow:0 3px 10px rgba(18,12,36,.2)}
.more{margin-left:7px;color:%(dim)s;font-size:12px}
.row{display:flex;align-items:center;gap:12px;min-width:0}
.face{display:grid;flex:0 0 48px;height:48px;place-items:center;border:1px solid rgba(255,255,255,.45);
border-radius:50%%;background:linear-gradient(145deg,%(av)s);color:#fff;font-size:19px;font-weight:650;
box-shadow:inset 0 1px 5px rgba(255,255,255,.5),0 5px 15px rgba(15,12,35,.2)}
.copy{flex:1;min-width:0}
.title-line{margin-bottom:5px}
.title-line strong{overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
time,.preview{color:%(dim)s;font-size:12px}
.preview{overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.unread{flex:0 0 auto;color:%(acc)s;font-size:12px;font-weight:600}
"""

# 各款的额外 CSS
EXTRA = {
 "n31": """
.prog{height:5px;border-radius:3px;background:rgba(255,255,255,.14);margin:14px 0 4px;overflow:hidden}
.prog i{display:block;height:100%;width:64%;border-radius:3px;background:linear-gradient(90deg,#b388ff,#7c6cf0);
box-shadow:0 0 12px rgba(150,130,255,.8)}
.ctrl{display:flex;align-items:center;justify-content:center;gap:26px;margin-top:14px}
.cbtn{width:44px;height:44px;border-radius:50%;border:1px solid rgba(255,255,255,.4);display:grid;place-items:center;
color:#fff;background:rgba(255,255,255,.12);font-size:16px;cursor:pointer}
.cbtn.big{width:60px;height:60px;font-size:22px;background:linear-gradient(135deg,#9d7bff,#6f5bd0);
box-shadow:0 8px 22px rgba(120,95,220,.55)}
.cover{width:56px;height:56px;border-radius:14px;flex:0 0 56px;background:linear-gradient(135deg,#3b2a6e,#8f6bd8 55%,#d96ba8);
display:grid;place-items:center;font-size:24px;box-shadow:0 6px 16px rgba(20,10,40,.35);border:1px solid rgba(255,255,255,.35)}
.times{display:flex;justify-content:space-between;font-size:11px;color:rgba(255,255,255,.6)}""",
 "n33": """
.nums{display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px;margin-top:14px}
.num{background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.14);border-radius:14px;padding:10px 6px;text-align:center}
.num b{display:block;font-size:19px;letter-spacing:-.02em}
.num span{font-size:11px;color:rgba(255,255,255,.62)}""",
 "n34": """
.ringwrap{display:flex;align-items:center;gap:16px;margin-top:6px}
.ring{flex:0 0 96px}
.ring svg{width:96px;height:96px;transform:rotate(-90deg)}
.ring .bgc{fill:none;stroke:rgba(255,255,255,.14);stroke-width:9}
.ring .fgc{fill:none;stroke:url(#g34);stroke-width:9;stroke-linecap:round;stroke-dasharray:264;stroke-dashoffset:66}
.ringtxt{font-size:11px;color:rgba(255,255,255,.66)}""",
 "n35": """
.bars{display:flex;align-items:flex-end;gap:7px;height:64px;margin-top:14px;padding:0 2px}
.bars i{flex:1;border-radius:5px;background:linear-gradient(180deg,#8fb7ff,#3d5a9e);min-height:14px;
box-shadow:inset 0 1px 0 rgba(255,255,255,.35)}
.bars i.deep{background:linear-gradient(180deg,#b39dff,#4a3a8f)}
.legend{display:flex;gap:14px;font-size:11px;color:rgba(255,255,255,.62);margin-top:10px}
.legend em{font-style:normal;display:inline-block;width:8px;height:8px;border-radius:50%;margin-right:5px}""",
 "n36": """
.ecg{width:100%;height:56px;margin-top:12px}
.ecg .base{fill:none;stroke:#ff7b7b;stroke-width:1.6;opacity:.32}
.ecg .live{fill:none;stroke:#ff7b7b;stroke-width:2;stroke-dasharray:120 560;animation:beat 3.2s linear infinite;animation-delay:-1.1s;
filter:drop-shadow(0 0 6px rgba(255,110,110,.8))}
@keyframes beat{to{stroke-dashoffset:-680}}
.big{font-size:34px;font-weight:700;letter-spacing:-.03em}
.unit{font-size:13px;color:rgba(255,255,255,.6);margin-left:6px}""",
 "n37": """
.btn{padding:9px 18px;border-radius:999px;border:0;font-size:13px;font-weight:700;color:#0c2415;cursor:pointer;
background:linear-gradient(135deg,#9df2b4,#4fd07e);box-shadow:0 6px 18px rgba(80,210,120,.45)}
.tag{font-size:11px;color:rgba(255,255,255,.66);border:1px dashed rgba(255,255,255,.3);border-radius:8px;padding:3px 8px;margin-right:6px}""",
 "n38": """
.playrow{display:flex;align-items:center;gap:12px;margin-top:12px}
.pbtn{width:46px;height:46px;border-radius:50%;border:0;display:grid;place-items:center;font-size:18px;color:#fff;cursor:pointer;
background:linear-gradient(135deg,#ff7ab8,#c05df0);box-shadow:0 8px 20px rgba(230,110,190,.5)}""",
 "n39": """
.stats{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:14px}
.stat{border-radius:14px;padding:12px;background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.13)}
.stat b{font-size:18px}.stat span{display:block;font-size:11px;color:rgba(255,255,255,.62);margin-top:2px}""",
 "n40": """
.breath{width:110px;height:110px;margin:16px auto 6px;border-radius:50%;display:grid;place-items:center;
background:radial-gradient(circle,rgba(255,255,255,.35),rgba(255,255,255,.06) 70%);
border:1px solid rgba(255,255,255,.4);animation:bre 5s ease-in-out infinite;animation-delay:-2s;font-size:13px}
@keyframes bre{0%,100%{transform:scale(1);opacity:.85}50%{transform:scale(1.18);opacity:1}}
.timer{text-align:center;font-size:12px;color:rgba(255,255,255,.66)}""",
}

# (文件, 标题, eyebrow, h1, hint, 主题参数, 卡片html)
CARDS = {}

# ---------- n31 正在播放 · 声浪此刻 ----------
C31 = dict(fg="#fff", dim="rgba(255,255,255,.68)", acc="#cfc4ff",
 bg="""radial-gradient(ellipse at 18% 12%, rgba(124,108,240,.9), transparent 36%),
 radial-gradient(ellipse at 85% 40%, rgba(217,107,168,.75), transparent 38%),
 radial-gradient(ellipse at 50% 92%, rgba(58,42,110,.85), transparent 40%),
 linear-gradient(150deg,#141026,#2c1d4d 55%,#18122e)""",
 bdc="rgba(255,255,255,.28)", br="28px", blur=24, sat=175, inset="rgba(255,255,255,.42)",
 shd="rgba(8,8,24,.28)", bdh="rgba(255,255,255,.46)",
 cardbg="linear-gradient(135deg,rgba(255,255,255,.20),rgba(255,255,255,.08) 48%,rgba(190,150,255,.12))",
 hldeg="118deg", hltint="rgba(206,180,255,.16)",
 ab_t="-58px", ab_r="-42px", ab_w="190px", ab_h="130px", ab_rot="-20deg",
 av="#8f6bd8, #d96ba8 70%, #3b2a6e")

# ---------- n32 歌单推荐 · 歌单速递 ----------
C32 = dict(fg="#fff", dim="rgba(255,255,255,.66)", acc="#9df2d8",
 bg="""radial-gradient(ellipse at 80% 15%, rgba(45,200,170,.8), transparent 36%),
 radial-gradient(ellipse at 12% 45%, rgba(60,120,220,.7), transparent 38%),
 radial-gradient(ellipse at 55% 90%, rgba(18,60,80,.9), transparent 40%),
 linear-gradient(150deg,#0e2426,#123f44 55%,#0b1c20)""",
 bdc="rgba(255,255,255,.26)", br="24px", blur=20, sat=160, inset="rgba(255,255,255,.38)",
 shd="rgba(4,20,22,.3)", bdh="rgba(255,255,255,.44)",
 cardbg="linear-gradient(135deg,rgba(255,255,255,.17),rgba(255,255,255,.06) 50%,rgba(120,230,200,.10))",
 hldeg="64deg", hltint="rgba(170,255,225,.15)",
 ab_t="-40px", ab_r="-60px", ab_w="170px", ab_h="150px", ab_rot="15deg",
 av="#2dc8aa, #3c78dc 70%, #123f44")

# ---------- n33 跑步完成 · 跑步总结 ----------
C33 = dict(fg="#fff", dim="rgba(255,255,255,.68)", acc="#ffd9a8",
 bg="""radial-gradient(ellipse at 15% 18%, rgba(255,150,80,.9), transparent 36%),
 radial-gradient(ellipse at 85% 35%, rgba(230,90,90,.75), transparent 38%),
 radial-gradient(ellipse at 55% 90%, rgba(120,50,40,.85), transparent 40%),
 linear-gradient(150deg,#241016,#4d1f18 55%,#1c0f12)""",
 bdc="rgba(255,255,255,.3)", br="30px", blur=22, sat=170, inset="rgba(255,255,255,.45)",
 shd="rgba(24,8,8,.3)", bdh="rgba(255,255,255,.5)",
 cardbg="linear-gradient(135deg,rgba(255,255,255,.2),rgba(255,255,255,.07) 48%,rgba(255,170,110,.12))",
 hldeg="120deg", hltint="rgba(255,190,140,.16)",
 ab_t="-64px", ab_r="-30px", ab_w="200px", ab_h="120px", ab_rot="-32deg",
 av="#ff9650, #e65a5a 70%, #782828")

# ---------- n34 步数目标 · 步数冲刺 ----------
C34 = dict(fg="#fff", dim="rgba(255,255,255,.66)", acc="#a8d4ff",
 bg="""radial-gradient(ellipse at 82% 12%, rgba(80,150,255,.85), transparent 36%),
 radial-gradient(ellipse at 15% 42%, rgba(90,90,220,.7), transparent 38%),
 radial-gradient(ellipse at 55% 92%, rgba(30,40,110,.85), transparent 40%),
 linear-gradient(150deg,#101a38,#1c2c5c 55%,#0e1428)""",
 bdc="rgba(255,255,255,.26)", br="26px", blur=26, sat=180, inset="rgba(255,255,255,.4)",
 shd="rgba(6,10,30,.32)", bdh="rgba(255,255,255,.46)",
 cardbg="linear-gradient(135deg,rgba(255,255,255,.18),rgba(255,255,255,.07) 50%,rgba(140,180,255,.12))",
 hldeg="100deg", hltint="rgba(170,200,255,.15)",
 ab_t="-50px", ab_r="-55px", ab_w="180px", ab_h="140px", ab_rot="10deg",
 av="#5096ff, #5a5adc 70%, #1e286e")

# ---------- n35 睡眠报告 · 深睡报告 ----------
C35 = dict(fg="#fff", dim="rgba(255,255,255,.62)", acc="#c3b8ff",
 bg="""radial-gradient(ellipse at 50% 8%, rgba(90,80,180,.75), transparent 40%),
 radial-gradient(ellipse at 88% 60%, rgba(50,60,140,.7), transparent 38%),
 radial-gradient(ellipse at 10% 85%, rgba(40,50,120,.8), transparent 40%),
 linear-gradient(160deg,#0c0e24,#1a1c3e 55%,#0a0c1e)""",
 bdc="rgba(255,255,255,.22)", br="28px", blur=28, sat=160, inset="rgba(255,255,255,.35)",
 shd="rgba(4,4,18,.34)", bdh="rgba(255,255,255,.42)",
 cardbg="linear-gradient(135deg,rgba(255,255,255,.15),rgba(255,255,255,.05) 50%,rgba(150,140,255,.10))",
 hldeg="130deg", hltint="rgba(190,180,255,.14)",
 ab_t="-44px", ab_r="-48px", ab_w="175px", ab_h="135px", ab_rot="-14deg",
 av="#8fb7ff, #6a5aae 70%, #2a2a5e")

# ---------- n36 心率提醒 · 心率警报 ----------
C36 = dict(fg="#fff", dim="rgba(255,255,255,.68)", acc="#ffb0b0",
 bg="""radial-gradient(ellipse at 20% 15%, rgba(255,90,90,.85), transparent 36%),
 radial-gradient(ellipse at 85% 45%, rgba(200,50,80,.7), transparent 38%),
 radial-gradient(ellipse at 50% 92%, rgba(90,20,30,.85), transparent 40%),
 linear-gradient(150deg,#240d12,#4d151c 55%,#1a0a0e)""",
 bdc="rgba(255,255,255,.3)", br="24px", blur=20, sat=175, inset="rgba(255,255,255,.44)",
 shd="rgba(20,6,8,.32)", bdh="rgba(255,255,255,.5)",
 cardbg="linear-gradient(135deg,rgba(255,255,255,.19),rgba(255,255,255,.07) 48%,rgba(255,130,130,.12))",
 hldeg="112deg", hltint="rgba(255,170,170,.16)",
 ab_t="-56px", ab_r="-36px", ab_w="185px", ab_h="125px", ab_rot="-26deg",
 av="#ff6b6b, #c83250 70%, #5a141e")

# ---------- n37 健身课程 · 燃脂课堂 ----------
C37 = dict(fg="#fff", dim="rgba(255,255,255,.68)", acc="#b8f5c8",
 bg="""radial-gradient(ellipse at 15% 20%, rgba(90,220,140,.85), transparent 36%),
 radial-gradient(ellipse at 85% 38%, rgba(60,190,160,.7), transparent 38%),
 radial-gradient(ellipse at 55% 90%, rgba(20,90,60,.85), transparent 40%),
 linear-gradient(150deg,#0d2418,#14402a 55%,#0a1a12)""",
 bdc="rgba(255,255,255,.28)", br="28px", blur=22, sat=170, inset="rgba(255,255,255,.42)",
 shd="rgba(6,20,12,.3)", bdh="rgba(255,255,255,.48)",
 cardbg="linear-gradient(135deg,rgba(255,255,255,.19),rgba(255,255,255,.07) 48%,rgba(150,240,180,.11))",
 hldeg="96deg", hltint="rgba(190,255,205,.15)",
 ab_t="-52px", ab_r="-62px", ab_w="185px", ab_h="145px", ab_rot="18deg",
 av="#5adc8c, #3cbe9c 70%, #145a36")

# ---------- n38 新歌上线 · 新歌首发 ----------
C38 = dict(fg="#fff", dim="rgba(255,255,255,.68)", acc="#ffc4dd",
 bg="""radial-gradient(ellipse at 82% 14%, rgba(255,120,180,.85), transparent 36%),
 radial-gradient(ellipse at 12% 40%, rgba(190,90,240,.7), transparent 38%),
 radial-gradient(ellipse at 55% 92%, rgba(90,40,120,.85), transparent 40%),
 linear-gradient(150deg,#22102a,#3d1a44 55%,#180c20)""",
 bdc="rgba(255,255,255,.3)", br="30px", blur=24, sat=180, inset="rgba(255,255,255,.46)",
 shd="rgba(20,8,28,.3)", bdh="rgba(255,255,255,.52)",
 cardbg="linear-gradient(135deg,rgba(255,255,255,.21),rgba(255,255,255,.08) 48%,rgba(255,150,200,.13))",
 hldeg="70deg", hltint="rgba(255,190,220,.16)",
 ab_t="-60px", ab_r="-40px", ab_w="195px", ab_h="128px", ab_rot="-22deg",
 av="#ff7ab8, #c05df0 70%, #5a2878")

# ---------- n39 骑行记录 · 骑行轨迹 ----------
C39 = dict(fg="#fff", dim="rgba(255,255,255,.66)", acc="#bfe3ff",
 bg="""radial-gradient(ellipse at 18% 16%, rgba(110,200,255,.85), transparent 36%),
 radial-gradient(ellipse at 85% 42%, rgba(80,140,230,.7), transparent 38%),
 radial-gradient(ellipse at 55% 92%, rgba(30,60,120,.85), transparent 40%),
 linear-gradient(150deg,#0e1c30,#18345c 55%,#0b1424)""",
 bdc="rgba(255,255,255,.26)", br="26px", blur=24, sat=170, inset="rgba(255,255,255,.4)",
 shd="rgba(6,12,28,.32)", bdh="rgba(255,255,255,.46)",
 cardbg="linear-gradient(135deg,rgba(255,255,255,.18),rgba(255,255,255,.06) 50%,rgba(140,200,255,.11))",
 hldeg="124deg", hltint="rgba(180,215,255,.15)",
 ab_t="-46px", ab_r="-52px", ab_w="178px", ab_h="138px", ab_rot="8deg",
 av="#6ec8ff, #508ce6 70%, #1e3c78")

# ---------- n40 冥想提醒 · 冥想时刻 ----------
C40 = dict(fg="#fff", dim="rgba(255,255,255,.7)", acc="#ffe3c4",
 bg="""radial-gradient(ellipse at 50% 10%, rgba(255,200,150,.8), transparent 40%),
 radial-gradient(ellipse at 85% 55%, rgba(200,150,220,.65), transparent 38%),
 radial-gradient(ellipse at 12% 80%, rgba(150,180,220,.7), transparent 40%),
 linear-gradient(160deg,#2a1c2e,#4d2f3a 55%,#1c2030)""",
 bdc="rgba(255,255,255,.3)", br="32px", blur=26, sat=165, inset="rgba(255,255,255,.48)",
 shd="rgba(16,10,20,.3)", bdh="rgba(255,255,255,.52)",
 cardbg="linear-gradient(135deg,rgba(255,255,255,.22),rgba(255,255,255,.09) 48%,rgba(255,210,170,.13))",
 hldeg="84deg", hltint="rgba(255,220,190,.17)",
 ab_t="-54px", ab_r="-44px", ab_w="190px", ab_h="132px", ab_rot="-18deg",
 av="#f8c79e, #c89ec8 70%, #72678e")

THEMES = {"n31":C31,"n32":C32,"n33":C33,"n34":C34,"n35":C35,"n36":C36,"n37":C37,"n38":C38,"n39":C39,"n40":C40}

HEAD = {
 "n31":("NOW PLAYING","声浪此刻","耳机里的世界，正在加载。"),
 "n32":("PLAYLIST","歌单速递","为你挑的歌，先听为敬。"),
 "n33":("RUNNING","跑步总结","今天的风，追上了你。"),
 "n34":("STEPS","步数冲刺","离目标，只差一小段路。"),
 "n35":("SLEEP","深睡报告","昨晚的梦，睡得很好。"),
 "n36":("HEALTH","心率警报","身体在说话，别错过。"),
 "n37":("WORKOUT","燃脂课堂","下一节课，已经备好。"),
 "n38":("NEW MUSIC","新歌首发","第一时间，听见新鲜。"),
 "n39":("CYCLING","骑行轨迹","轮子转过的地方都算数。"),
 "n40":("MINDFULNESS","冥想时刻","给大脑放个小假。"),
}

BODIES = {
"n31": """
<section class="card">
  <div class="top"><span class="pill">正在播放</span><span class="more">夜跑歌单</span></div>
  <div class="row">
    <div class="cover">♪</div>
    <div class="copy">
      <div class="title-line"><strong>城市夜行者</strong><time>3:42</time></div>
      <div class="preview">雾岛乐队 · 《霓虹漫步》</div>
    </div>
  </div>
  <div class="prog"><i></i></div>
  <div class="times"><span>2:16</span><span>-1:26</span></div>
  <div class="ctrl"><div class="cbtn">⏮</div><div class="cbtn big">⏸</div><div class="cbtn">⏭</div></div>
</section>
<section class="card">
  <div class="top"><span class="pill">下一首</span><span class="more">18:20 推送</span></div>
  <div class="row">
    <div class="face">岚</div>
    <div class="copy">
      <div class="title-line"><strong>岚山电台</strong><time>刚刚</time></div>
      <div class="preview">为你续播：《云端慢跑》混音版</div>
    </div>
    <span class="unread">▶ 试听</span>
  </div>
</section>""",
"n32": """
<section class="card">
  <div class="top"><span class="pill">为你推荐</span><div class="avatars"><i class="avatar">爵</i><i class="avatar">电</i><i class="avatar">民</i><span class="more">12 首</span></div></div>
  <div class="row">
    <div class="face">单</div>
    <div class="copy">
      <div class="title-line"><strong>雨后慢跑歌单</strong><time>今日</time></div>
      <div class="preview">根据你的跑步节奏生成 · 48 分钟</div>
    </div>
    <span class="unread">收藏</span>
  </div>
</section>
<section class="card">
  <div class="top"><span class="pill">好友在听</span><div class="avatars"><i class="avatar">舟</i><i class="avatar">麦</i></div></div>
  <div class="row">
    <div class="face">舟</div>
    <div class="copy">
      <div class="title-line"><strong>陈舟</strong><time>12:05</time></div>
      <div class="preview">分享了歌单《骑行不打烊》给你</div>
    </div>
    <span class="unread">查看</span>
  </div>
</section>""",
"n33": """
<section class="card">
  <div class="top"><span class="pill">跑步完成</span><span class="more">晨跑 · 公园环线</span></div>
  <div class="row">
    <div class="face">跑</div>
    <div class="copy">
      <div class="title-line"><strong>5.2 公里，拿下！</strong><time>07:32</time></div>
      <div class="preview">比上周快了 1 分 20 秒，继续保持</div>
    </div>
  </div>
  <div class="nums">
    <div class="num"><b>5.20</b><span>公里</span></div>
    <div class="num"><b>32:10</b><span>用时</span></div>
    <div class="num"><b>6'12"</b><span>平均配速</span></div>
  </div>
</section>
<section class="card">
  <div class="top"><span class="pill">成就</span><time>刚刚</time></div>
  <div class="row">
    <div class="face">徽</div>
    <div class="copy">
      <div class="title-line"><strong>解锁「破晓跑者」</strong></div>
      <div class="preview">连续 7 天 7 点前开跑，太自律了</div>
    </div>
    <span class="unread">领取</span>
  </div>
</section>""",
"n34": """
<section class="card">
  <div class="top"><span class="pill">步数目标</span><time>21:40</time></div>
  <div class="ringwrap">
    <div class="ring"><svg viewBox="0 0 96 96"><defs><linearGradient id="g34" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#7db4ff"/><stop offset="1" stop-color="#5a5adc"/></linearGradient></defs><circle class="bgc" cx="48" cy="48" r="42"/><circle class="fgc" cx="48" cy="48" r="42"/></svg></div>
    <div class="copy">
      <div class="title-line"><strong>8,432 / 10,000 步</strong></div>
      <div class="preview">再走 15 分钟就能达标，加油</div>
      <div class="ringtxt" style="margin-top:6px">今日已消耗约 320 千卡</div>
    </div>
  </div>
</section>
<section class="card">
  <div class="top"><span class="pill">好友动态</span><div class="avatars"><i class="avatar">桐</i><i class="avatar">屿</i></div></div>
  <div class="row">
    <div class="face">桐</div>
    <div class="copy">
      <div class="title-line"><strong>林桐已达标</strong><time>20:15</time></div>
      <div class="preview">她今天走了 12,480 步，为她点赞</div>
    </div>
    <span class="unread">点赞</span>
  </div>
</section>""",
"n35": """
<section class="card">
  <div class="top"><span class="pill">睡眠报告</span><time>07:00</time></div>
  <div class="row">
    <div class="face">眠</div>
    <div class="copy">
      <div class="title-line"><strong>昨晚睡了 7 小时 26 分</strong></div>
      <div class="preview">深睡 1 小时 48 分 · 睡眠评分 86</div>
    </div>
  </div>
  <div class="bars"><i class="deep" style="height:88%"></i><i style="height:52%"></i><i class="deep" style="height:96%"></i><i style="height:44%"></i><i style="height:60%"></i><i class="deep" style="height:82%"></i><i style="height:38%"></i><i style="height:55%"></i></div>
  <div class="legend"><span><em style="background:#b39dff"></em>深睡</span><span><em style="background:#8fb7ff"></em>浅睡</span></div>
</section>
<section class="card">
  <div class="top"><span class="pill">睡眠建议</span></div>
  <div class="row">
    <div class="copy">
      <div class="title-line"><strong>今晚 23:10 准备入睡</strong></div>
      <div class="preview">保持规律作息，深睡时长会更稳</div>
    </div>
    <span class="unread">设提醒</span>
  </div>
</section>""",
"n36": """
<section class="card">
  <div class="top"><span class="pill">心率提醒</span><time>14:22</time></div>
  <div class="row">
    <div class="copy">
      <div class="title-line"><strong>静息心率偏高</strong></div>
      <div class="preview">过去 1 小时平均 102 bpm，建议休息一下</div>
    </div>
    <div><span class="big">102</span><span class="unit">bpm</span></div>
  </div>
  <svg class="ecg" viewBox="0 0 400 56" preserveAspectRatio="none"><path class="base" d="M0 30 H90 l10-10 10 16 8-34 10 40 8-12 h20 l10-10 10 16 8-34 10 40 8-12 H400"/><path class="live" d="M0 30 H90 l10-10 10 16 8-34 10 40 8-12 h20 l10-10 10 16 8-34 10 40 8-12 H400"/></svg>
</section>
<section class="card">
  <div class="top"><span class="pill">运动恢复</span><time>昨日</time></div>
  <div class="row">
    <div class="face">恢</div>
    <div class="copy">
      <div class="title-line"><strong>心率已回到正常区间</strong></div>
      <div class="preview">昨晚跑步后 2 小时恢复至 68 bpm</div>
    </div>
  </div>
</section>""",
"n37": """
<section class="card">
  <div class="top"><span class="pill">课程提醒</span><time>18:00</time></div>
  <div class="row">
    <div class="face">燃</div>
    <div class="copy">
      <div class="title-line"><strong>今晚 19:30 · 高强度间歇</strong><time></time></div>
      <div class="preview">教练：阿哲 · 还有 12 个名额</div>
    </div>
  </div>
  <div class="row" style="margin-top:14px">
    <span class="tag">45 分钟</span><span class="tag">中高强度</span>
    <span style="flex:1"></span><button class="btn">立即预约</button>
  </div>
</section>
<section class="card">
  <div class="top"><span class="pill">打卡</span><div class="avatars"><i class="avatar">哲</i><i class="avatar">南</i><i class="avatar">葵</i><span class="more">+5</span></div></div>
  <div class="row">
    <div class="face">哲</div>
    <div class="copy">
      <div class="title-line"><strong>阿哲完成了今日训练</strong><time>17:42</time></div>
      <div class="preview">深蹲 80kg × 8 · 你也别偷懒</div>
    </div>
    <span class="unread">回一个火</span>
  </div>
</section>""",
"n38": """
<section class="card">
  <div class="top"><span class="pill">新歌首发</span><span class="more">刚刚上线</span></div>
  <div class="row">
    <div class="face">碟</div>
    <div class="copy">
      <div class="title-line"><strong>《雾海灯塔》正式发布</strong><time>10:00</time></div>
      <div class="preview">白昼乐队 · 全新专辑 · 共 10 首</div>
    </div>
  </div>
  <div class="playrow"><button class="pbtn">▶</button>
    <div class="copy"><div class="preview">主打歌《雾海灯塔》 · 4:12</div></div>
    <span class="unread">整专播放</span>
  </div>
</section>
<section class="card">
  <div class="top"><span class="pill">艺人动态</span><div class="avatars"><i class="avatar">昼</i></div></div>
  <div class="row">
    <div class="face">昼</div>
    <div class="copy">
      <div class="title-line"><strong>白昼乐队</strong><time>09:30</time></div>
      <div class="preview">“这张专辑写给所有失眠的夜。”</div>
    </div>
    <span class="unread">关注</span>
  </div>
</section>""",
"n39": """
<section class="card">
  <div class="top"><span class="pill">骑行完成</span><span class="more">滨江绿道</span></div>
  <div class="row">
    <div class="face">骑</div>
    <div class="copy">
      <div class="title-line"><strong>18.6 公里，骑得漂亮</strong><time>16:48</time></div>
      <div class="preview">用时 58 分 24 秒 · 平均时速 19.1 km/h</div>
    </div>
  </div>
  <div class="stats">
    <div class="stat"><b>412</b><span>消耗千卡</span></div>
    <div class="stat"><b>132</b><span>平均心率 bpm</span></div>
    <div class="stat"><b>86 m</b><span>累计爬升</span></div>
    <div class="stat"><b>78 rpm</b><span>平均踏频</span></div>
  </div>
</section>
<section class="card">
  <div class="top"><span class="pill">路线推荐</span></div>
  <div class="row">
    <div class="copy">
      <div class="title-line"><strong>周末试试「湖畔环线」</strong></div>
      <div class="preview">22 公里 · 风景好 · 难度适中</div>
    </div>
    <span class="unread">查看路线</span>
  </div>
</section>""",
"n40": """
<section class="card">
  <div class="top"><span class="pill">冥想提醒</span><time>21:30</time></div>
  <div class="breath">呼吸</div>
  <div class="timer">跟随圆圈 · 吸气 4 秒 · 呼气 6 秒</div>
  <div class="row" style="margin-top:14px;justify-content:center">
    <span class="preview">今晚 10 分钟「晚安冥想」还没开始</span>
  </div>
</section>
<section class="card">
  <div class="top"><span class="pill">本周回顾</span></div>
  <div class="row">
    <div class="face">静</div>
    <div class="copy">
      <div class="title-line"><strong>已冥想 4 天，共 52 分钟</strong></div>
      <div class="preview">专注时长超过 82% 的用户，继续</div>
    </div>
    <span class="unread">开始</span>
  </div>
</section>""",
}

TITLES = {
 "n31":"声浪此刻","n32":"歌单速递","n33":"跑步总结","n34":"步数冲刺","n35":"深睡报告",
 "n36":"心率警报","n37":"燃脂课堂","n38":"新歌首发","n39":"骑行轨迹","n40":"冥想时刻",
}

PAGE = """<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>液态玻璃通知卡片 · %(title)s</title>
<style>
%(css)s
%(extra)s
@supports not ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {
  .card { background: rgba(43,35,68,.88); }
}
@media (prefers-reduced-motion: reduce) {
  .card { transition: none; }
  .breath,.ecg path { animation: none; }
}
</style>
</head>
<body>
<main>
<header class="heading">
<p class="eyebrow">%(eyebrow)s</p>
<h1>%(h1)s</h1>
<p class="hint">%(hint)s</p>
</header>
%(body)s
</main>
</body>
</html>
"""

def build():
    for fid in sorted(TITLES):
        th = dict(THEMES[fid])
        css = BASE_CSS % th
        eyebrow, h1, hint = HEAD[fid]
        html = PAGE % dict(title=TITLES[fid], css=css, extra=EXTRA.get(fid, ""),
                           eyebrow=eyebrow, h1=h1, hint=hint, body=BODIES[fid])
        with open(os.path.join(DIR, fid + ".html"), "w", encoding="utf-8") as f:
            f.write(html)
        print("wrote", fid)
    entries = [{"file": fid + ".html", "title": TITLES[fid]} for fid in sorted(TITLES)]
    import json
    with open(os.path.join(DIR, "_titles_nc_d.json"), "w", encoding="utf-8") as f:
        json.dump(entries, f, ensure_ascii=False, indent=1)
    print("titles json ok")

if __name__ == "__main__":
    build()
