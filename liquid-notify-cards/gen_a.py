#!/usr/bin/env python3
# 生成 n01-n10 液态玻璃通知卡片（消息社交方向）
import os
OUT = os.path.dirname(os.path.abspath(__file__))

CSS = """*{box-sizing:border-box}
body{min-height:100vh;margin:0;padding:44px 18px 60px;color:VAR_T;font:15px/1.45 -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
background:VAR_BG;background-attachment:fixed}
main{width:min(440px,100%);margin:0 auto;display:grid;gap:18px}
.heading{padding:4px 6px 8px}
.eyebrow{margin:0 0 8px;color:VAR_TD;font-size:11px;letter-spacing:.18em}
h1{margin:0;font-size:30px;letter-spacing:-.04em}
.hint{margin:7px 0 0;color:VAR_TD}
.card{position:relative;isolation:isolate;overflow:hidden;padding:18px;border:1px solid VAR_CBD;border-radius:28px;
background:VAR_CBG;-webkit-backdrop-filter:blur(VAR_BLUR) saturate(VAR_SAT);backdrop-filter:blur(VAR_BLUR) saturate(VAR_SAT);
box-shadow:inset 0 1px 0 VAR_SH1,inset 0 -1px 0 rgba(255,255,255,.08),0 20px 48px rgba(8,8,24,.28);
transition:transform .25s ease,border-color .25s ease}
.card::before{content:"";position:absolute;z-index:0;inset:0;border-radius:inherit;pointer-events:none;opacity:.8;
background:linear-gradient(VAR_HLANG,VAR_HL)}
.card::after{content:"";position:absolute;z-index:0;VAR_ARCPOS;width:VAR_ARCW;height:VAR_ARCH;border:1px solid VAR_ARCBD;border-radius:50%;
background:radial-gradient(ellipse,VAR_ARCIN,transparent 68%);filter:blur(2px);transform:rotate(VAR_ARCROT);pointer-events:none}
.card>*{position:relative;z-index:1}
.card:hover{transform:translateY(-3px);border-color:VAR_CBDH}
.top,.title-line{display:flex;align-items:center;justify-content:space-between;gap:12px}
.top{margin-bottom:17px}
.pill{padding:6px 12px;border:1px solid VAR_PBD;border-radius:999px;background:VAR_PBG;color:VAR_T;font-size:12px;box-shadow:inset 0 1px rgba(255,255,255,.18);white-space:nowrap}
.avatars{display:flex;align-items:center;padding-left:8px}
.avatar{display:grid;width:29px;height:29px;margin-left:-8px;place-items:center;border:1px solid VAR_AVB;border-radius:50%;color:#fff;font-size:11px;box-shadow:0 3px 10px rgba(18,12,36,.2)}
.more{margin-left:7px;color:VAR_TD;font-size:12px}
.row{display:flex;align-items:center;gap:12px;min-width:0}
.row.rev{flex-direction:row-reverse;text-align:right}
.row.rev .copy .title-line{flex-direction:row-reverse}
.face{display:grid;flex:0 0 48px;height:48px;place-items:center;border:1px solid VAR_FBD;border-radius:50%;color:#fff;font-size:19px;font-weight:650;box-shadow:inset 0 1px 5px rgba(255,255,255,.5),0 5px 15px rgba(15,12,35,.2)}
.copy{flex:1;min-width:0}
.title-line{margin-bottom:5px}
.title-line strong{overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
time,.preview{color:VAR_TD;font-size:12px}
.preview{overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.unread{flex:0 0 auto;color:VAR_ACC;font-size:12px;font-weight:600;white-space:nowrap}
.actions{display:flex;gap:10px;margin-top:14px}
.btn{flex:1;padding:10px 0;border:0;border-radius:14px;font-size:13px;font-weight:600;cursor:pointer;color:#fff;background:VAR_BTN;box-shadow:0 6px 18px VAR_BTNS}
.btn.ghost{background:VAR_BTNG;color:VAR_T;border:1px solid VAR_CBD}
.thumb{flex:0 0 52px;width:52px;height:52px;border-radius:14px;border:1px solid VAR_CBD;background:VAR_THBG}
.voice{display:flex;align-items:center;gap:3px;height:34px;padding:0 12px;border-radius:12px;background:VAR_VBG;border:1px solid VAR_CBD}
.voice i{width:3px;border-radius:2px;background:VAR_ACC;animation:wv 1.1s ease-in-out infinite}
@keyframes wv{0%,100%{transform:scaleY(.4)}50%{transform:scaleY(1)}}
.livedot{display:inline-block;width:8px;height:8px;border-radius:50%;background:#ff4d6d;margin-right:6px;box-shadow:0 0 8px #ff4d6d;animation:blk 1.4s ease-in-out infinite}
@keyframes blk{50%{transform:scale(1.4)}}
@supports not ((backdrop-filter:blur(1px)) or (-webkit-backdrop-filter:blur(1px)){.card{background:VAR_FALLBACK}}
@media (prefers-reduced-motion:reduce){.card{transition:none}.voice i{animation:none}}"""

def avatar(ch, bg):
    return f'<i class="avatar" style="background:{bg}">{ch}</i>'

def top(pill, avs=(), more=""):
    a = "".join(avs)
    m = f'<span class="more">{more}</span>' if more else ""
    return f'<div class="top"><span class="pill">{pill}</span><div class="avatars">{a}{m}</div></div>'

def row(face_ch, face_bg, title, tm, preview, right="", rev=False):
    cls = "row rev" if rev else "row"
    return (f'<div class="{cls}"><div class="face" style="background:{face_bg}">{face_ch}</div>'
            f'<div class="copy"><div class="title-line"><strong>{title}</strong><time>{tm}</time></div>'
            f'<div class="preview">{preview}</div></div>{right}</div>')

def actions(*btns):
    b = "".join(f'<button class="btn{" ghost" if g else ""}">{t}</button>' for t, g in btns)
    return f'<div class="actions">{b}</div>'

def voice_bar(widths):
    bars = "".join(f'<i style="height:{h}px;animation-delay:-{d:.2f}s"></i>' for h, d in widths)
    return f'<div class="voice">{bars}</div>'

THEMES = [
 dict(num="n01", title="深海私语", eyebrow="DEEP SEA · DM", hint="深海里，也有人惦记你。",
  bg="radial-gradient(ellipse at 20% 15%, rgba(34,120,180,.9), transparent 36%),radial-gradient(ellipse at 85% 40%, rgba(20,60,140,.85), transparent 38%),radial-gradient(ellipse at 50% 92%, rgba(10,30,80,.9), transparent 40%),linear-gradient(160deg,#04121f,#0a2a4a 55%,#06203a)",
  t="#fff", td="rgba(255,255,255,.68)",
  cbg="linear-gradient(135deg,rgba(120,200,255,.16),rgba(255,255,255,.06) 48%,rgba(80,160,255,.10))",
  cbd="rgba(140,200,255,.30)", cbdh="rgba(140,200,255,.55)", blur="26px", sat="180%",
  sh1="rgba(180,225,255,.40)", acc="#7fd4ff",
  hlang="118deg", hl="rgba(255,255,255,.30) 0%,rgba(255,255,255,.07) 18%,transparent 42%,transparent 72%,rgba(160,220,255,.18) 100%",
  arcpos="top:-58px;right:-42px", arcw="190px", arch="130px", arcrot="-20deg",
  arcbd="rgba(160,220,255,.25)", arcin="rgba(160,220,255,.20)",
  pbd="rgba(140,200,255,.35)", pbg="rgba(120,200,255,.12)",
  avb="rgba(255,255,255,.55)", fbd="rgba(160,220,255,.45)",
  btn="linear-gradient(135deg,#2f9be8,#1a6fc4)", btns="rgba(47,155,232,.4)", btng="rgba(120,200,255,.10)",
  vbg="rgba(120,200,255,.10)", thbg="linear-gradient(135deg,#123a5e,#0a2a4a)", fallback="rgba(10,32,58,.92)"),
 dict(num="n02", title="霓虹点赞", eyebrow="NEON · LIKES", hint="你的动态，正在被点亮。",
  bg="radial-gradient(ellipse at 15% 20%, rgba(255,45,150,.85), transparent 36%),radial-gradient(ellipse at 85% 30%, rgba(140,40,255,.8), transparent 38%),radial-gradient(ellipse at 55% 90%, rgba(40,20,120,.85), transparent 40%),linear-gradient(150deg,#160a24,#2b0f3d 55%,#12082b)",
  t="#fff", td="rgba(255,255,255,.68)",
  cbg="linear-gradient(135deg,rgba(255,110,196,.18),rgba(255,255,255,.06) 48%,rgba(150,80,255,.12))",
  cbd="rgba(255,110,196,.32)", cbdh="rgba(255,110,196,.55)", blur="24px", sat="175%",
  sh1="rgba(255,255,255,.42)", acc="#ff6ec4",
  hlang="105deg", hl="rgba(255,255,255,.32) 0%,rgba(255,255,255,.07) 20%,transparent 45%,transparent 70%,rgba(255,110,196,.20) 100%",
  arcpos="top:-50px;right:-36px", arcw="180px", arch="120px", arcrot="-28deg",
  arcbd="rgba(255,110,196,.28)", arcin="rgba(255,110,196,.22)",
  pbd="rgba(255,110,196,.38)", pbg="rgba(255,110,196,.12)",
  avb="rgba(255,255,255,.55)", fbd="rgba(255,110,196,.45)",
  btn="linear-gradient(135deg,#ff5fa8,#c93ff0)", btns="rgba(255,95,168,.4)", btng="rgba(255,110,196,.10)",
  vbg="rgba(255,110,196,.10)", thbg="linear-gradient(135deg,#3d1540,#1c0a28)", fallback="rgba(52,20,64,.92)"),
 dict(num="n03", title="蜜桃群聊", eyebrow="PEACH · GROUPS", hint="热闹的群，甜甜的。",
  bg="radial-gradient(ellipse at 15% 20%, rgba(255,180,150,.9), transparent 36%),radial-gradient(ellipse at 85% 35%, rgba(255,140,170,.75), transparent 38%),radial-gradient(ellipse at 55% 90%, rgba(255,200,170,.8), transparent 40%),linear-gradient(150deg,#fff3ec,#ffe3d6 55%,#ffd9c9)",
  t="#4a2c22", td="rgba(74,44,34,.62)",
  cbg="linear-gradient(135deg,rgba(255,255,255,.55),rgba(255,255,255,.25) 48%,rgba(255,200,180,.30))",
  cbd="rgba(255,255,255,.70)", cbdh="rgba(255,255,255,.95)", blur="20px", sat="160%",
  sh1="rgba(255,255,255,.75)", acc="#d14f43",
  hlang="125deg", hl="rgba(255,255,255,.55) 0%,rgba(255,255,255,.18) 20%,transparent 45%,transparent 70%,rgba(255,170,150,.30) 100%",
  arcpos="top:-52px;right:-38px", arcw="185px", arch="125px", arcrot="-15deg",
  arcbd="rgba(255,255,255,.65)", arcin="rgba(255,255,255,.40)",
  pbd="rgba(209,79,67,.35)", pbg="rgba(209,79,67,.10)",
  avb="rgba(255,255,255,.85)", fbd="rgba(255,255,255,.70)",
  btn="linear-gradient(135deg,#f0735f,#d14f43)", btns="rgba(240,115,95,.4)", btng="rgba(255,255,255,.35)",
  vbg="rgba(209,79,67,.08)", thbg="linear-gradient(135deg,#ffd9c9,#ffc4b3)", fallback="rgba(255,235,225,.95)"),
 dict(num="n04", title="薄荷评论", eyebrow="MINT · COMMENTS", hint="清清爽爽的互动。",
  bg="radial-gradient(ellipse at 15% 20%, rgba(120,230,190,.85), transparent 36%),radial-gradient(ellipse at 85% 35%, rgba(80,200,220,.70), transparent 38%),radial-gradient(ellipse at 55% 90%, rgba(60,160,180,.75), transparent 40%),linear-gradient(150deg,#eafff5,#d9f7ec 55%,#c9efe4)",
  t="#123f36", td="rgba(18,63,54,.60)",
  cbg="linear-gradient(135deg,rgba(255,255,255,.50),rgba(255,255,255,.22) 48%,rgba(150,235,200,.28))",
  cbd="rgba(255,255,255,.65)", cbdh="rgba(255,255,255,.95)", blur="22px", sat="165%",
  sh1="rgba(255,255,255,.70)", acc="#0b8a68",
  hlang="100deg", hl="rgba(255,255,255,.50) 0%,rgba(255,255,255,.15) 20%,transparent 45%,transparent 70%,rgba(120,230,190,.30) 100%",
  arcpos="top:-64px;left:-40px", arcw="180px", arch="125px", arcrot="18deg",
  arcbd="rgba(255,255,255,.60)", arcin="rgba(255,255,255,.38)",
  pbd="rgba(11,138,104,.35)", pbg="rgba(11,138,104,.10)",
  avb="rgba(255,255,255,.85)", fbd="rgba(255,255,255,.70)",
  btn="linear-gradient(135deg,#12b981,#0b8a68)", btns="rgba(18,185,129,.4)", btng="rgba(255,255,255,.35)",
  vbg="rgba(11,138,104,.08)", thbg="linear-gradient(135deg,#c9efe4,#aee6d2)", fallback="rgba(230,250,242,.95)"),
 dict(num="n05", title="熔岩关注", eyebrow="LAVA · FOLLOWS", hint="热度，正在向你涌来。",
  bg="radial-gradient(ellipse at 15% 20%, rgba(255,110,40,.90), transparent 36%),radial-gradient(ellipse at 85% 35%, rgba(220,40,60,.80), transparent 38%),radial-gradient(ellipse at 55% 90%, rgba(120,20,40,.85), transparent 40%),linear-gradient(150deg,#200a08,#3d140d 55%,#2a0d12)",
  t="#fff", td="rgba(255,255,255,.68)",
  cbg="linear-gradient(135deg,rgba(255,150,80,.18),rgba(255,255,255,.06) 48%,rgba(255,90,60,.12))",
  cbd="rgba(255,150,90,.32)", cbdh="rgba(255,150,90,.55)", blur="24px", sat="175%",
  sh1="rgba(255,255,255,.42)", acc="#ff9a4d",
  hlang="130deg", hl="rgba(255,255,255,.30) 0%,rgba(255,255,255,.07) 18%,transparent 42%,transparent 72%,rgba(255,140,70,.20) 100%",
  arcpos="bottom:-60px;right:-40px", arcw="190px", arch="130px", arcrot="25deg",
  arcbd="rgba(255,140,70,.28)", arcin="rgba(255,140,70,.20)",
  pbd="rgba(255,150,90,.38)", pbg="rgba(255,150,90,.12)",
  avb="rgba(255,255,255,.55)", fbd="rgba(255,150,90,.45)",
  btn="linear-gradient(135deg,#ff8a3d,#e04a2a)", btns="rgba(255,138,61,.4)", btng="rgba(255,150,90,.10)",
  vbg="rgba(255,150,90,.10)", thbg="linear-gradient(135deg,#4a1a10,#2a0d08)", fallback="rgba(66,24,14,.92)"),
 dict(num="n06", title="墨晕好友", eyebrow="INK · REQUESTS", hint="新的相遇，淡墨轻点。",
  bg="radial-gradient(ellipse at 15% 20%, rgba(90,90,110,.70), transparent 36%),radial-gradient(ellipse at 85% 35%, rgba(50,50,70,.80), transparent 38%),radial-gradient(ellipse at 55% 90%, rgba(20,20,30,.90), transparent 40%),linear-gradient(150deg,#0b0b10,#17171f 55%,#0e0e14)",
  t="#fff", td="rgba(255,255,255,.66)",
  cbg="linear-gradient(135deg,rgba(200,200,220,.14),rgba(255,255,255,.05) 48%,rgba(185,167,230,.10))",
  cbd="rgba(200,200,220,.28)", cbdh="rgba(200,200,220,.50)", blur="28px", sat="150%",
  sh1="rgba(255,255,255,.35)", acc="#c9b8f5",
  hlang="95deg", hl="rgba(255,255,255,.26) 0%,rgba(255,255,255,.06) 20%,transparent 45%,transparent 70%,rgba(185,167,230,.16) 100%",
  arcpos="top:-56px;left:-44px", arcw="185px", arch="128px", arcrot="22deg",
  arcbd="rgba(200,200,220,.25)", arcin="rgba(200,200,220,.18)",
  pbd="rgba(200,200,220,.35)", pbg="rgba(200,200,220,.10)",
  avb="rgba(255,255,255,.50)", fbd="rgba(200,200,220,.40)",
  btn="linear-gradient(135deg,#8f7bd8,#6a54b8)", btns="rgba(143,123,216,.4)", btng="rgba(200,200,220,.10)",
  vbg="rgba(200,200,220,.08)", thbg="linear-gradient(135deg,#23232e,#14141a)", fallback="rgba(24,24,32,.94)"),
 dict(num="n07", title="晨雾提及", eyebrow="MIST · MENTIONS", hint="有人在雾里喊你的名字。",
  bg="radial-gradient(ellipse at 15% 20%, rgba(200,215,230,.90), transparent 36%),radial-gradient(ellipse at 85% 35%, rgba(180,200,220,.80), transparent 38%),radial-gradient(ellipse at 55% 90%, rgba(170,190,210,.85), transparent 40%),linear-gradient(150deg,#f4f7fa,#e6edf3 55%,#dde6ee)",
  t="#2c3a4a", td="rgba(44,58,74,.60)",
  cbg="linear-gradient(135deg,rgba(255,255,255,.60),rgba(255,255,255,.28) 48%,rgba(190,210,230,.32))",
  cbd="rgba(255,255,255,.75)", cbdh="rgba(255,255,255,.95)", blur="24px", sat="160%",
  sh1="rgba(255,255,255,.80)", acc="#2f6da3",
  hlang="112deg", hl="rgba(255,255,255,.60) 0%,rgba(255,255,255,.20) 20%,transparent 45%,transparent 70%,rgba(160,190,215,.32) 100%",
  arcpos="top:-60px;right:-46px", arcw="195px", arch="132px", arcrot="-24deg",
  arcbd="rgba(255,255,255,.70)", arcin="rgba(255,255,255,.42)",
  pbd="rgba(47,109,163,.35)", pbg="rgba(47,109,163,.10)",
  avb="rgba(255,255,255,.85)", fbd="rgba(255,255,255,.70)",
  btn="linear-gradient(135deg,#3f8ac2,#2f6da3)", btns="rgba(63,138,194,.4)", btng="rgba(255,255,255,.40)",
  vbg="rgba(47,109,163,.08)", thbg="linear-gradient(135deg,#dde6ee,#c9d8e6)", fallback="rgba(235,240,246,.95)"),
 dict(num="n08", title="彩虹转发", eyebrow="RAINBOW · SHARES", hint="好内容，值得被传下去。",
  bg="radial-gradient(ellipse at 10% 15%, rgba(255,90,120,.80), transparent 34%),radial-gradient(ellipse at 40% 25%, rgba(255,180,60,.70), transparent 34%),radial-gradient(ellipse at 70% 20%, rgba(90,220,150,.70), transparent 34%),radial-gradient(ellipse at 90% 45%, rgba(90,140,255,.75), transparent 36%),radial-gradient(ellipse at 50% 92%, rgba(180,90,255,.70), transparent 38%),linear-gradient(150deg,#141021,#1d1530 55%,#101a2e)",
  t="#fff", td="rgba(255,255,255,.68)",
  cbg="linear-gradient(135deg,rgba(255,255,255,.18),rgba(255,255,255,.07) 48%,rgba(180,140,255,.12))",
  cbd="rgba(255,255,255,.30)", cbdh="rgba(255,255,255,.52)", blur="24px", sat="175%",
  sh1="rgba(255,255,255,.42)", acc="#c792ff",
  hlang="120deg", hl="rgba(255,255,255,.32) 0%,rgba(255,120,180,.10) 20%,transparent 45%,transparent 70%,rgba(140,160,255,.22) 100%",
  arcpos="bottom:-56px;left:-42px", arcw="190px", arch="130px", arcrot="20deg",
  arcbd="rgba(180,160,255,.28)", arcin="rgba(180,160,255,.20)",
  pbd="rgba(180,160,255,.38)", pbg="rgba(180,160,255,.12)",
  avb="rgba(255,255,255,.55)", fbd="rgba(180,160,255,.45)",
  btn="linear-gradient(135deg,#a06cf0,#7a4fe0)", btns="rgba(160,108,240,.4)", btng="rgba(180,160,255,.10)",
  vbg="rgba(180,160,255,.10)", thbg="linear-gradient(135deg,#2c2140,#1a1430)", fallback="rgba(38,30,58,.92)"),
 dict(num="n09", title="水银语音", eyebrow="MERCURY · VOICE", hint="听，是谁的声音。",
  bg="radial-gradient(ellipse at 15% 20%, rgba(220,230,240,.85), transparent 36%),radial-gradient(ellipse at 85% 35%, rgba(170,185,200,.80), transparent 38%),radial-gradient(ellipse at 55% 90%, rgba(140,155,175,.85), transparent 40%),linear-gradient(150deg,#2a3138,#3d454e 55%,#232a31)",
  t="#fff", td="rgba(255,255,255,.66)",
  cbg="linear-gradient(135deg,rgba(230,240,250,.16),rgba(255,255,255,.06) 48%,rgba(160,200,220,.12))",
  cbd="rgba(220,230,240,.30)", cbdh="rgba(220,230,240,.52)", blur="26px", sat="150%",
  sh1="rgba(255,255,255,.45)", acc="#9fd8e8",
  hlang="108deg", hl="rgba(255,255,255,.34) 0%,rgba(255,255,255,.08) 18%,transparent 42%,transparent 72%,rgba(180,220,235,.20) 100%",
  arcpos="top:-54px;right:-40px", arcw="185px", arch="126px", arcrot="-18deg",
  arcbd="rgba(220,230,240,.30)", arcin="rgba(220,230,240,.22)",
  pbd="rgba(220,230,240,.35)", pbg="rgba(220,230,240,.10)",
  avb="rgba(255,255,255,.60)", fbd="rgba(220,230,240,.45)",
  btn="linear-gradient(135deg,#5aa8c4,#3d7f9c)", btns="rgba(90,168,196,.4)", btng="rgba(220,230,240,.10)",
  vbg="rgba(160,200,220,.12)", thbg="linear-gradient(135deg,#3d454e,#2a3138)", fallback="rgba(52,60,68,.94)"),
 dict(num="n10", title="果冻开播", eyebrow="JELLY · LIVE", hint="喜欢的主播，上线啦。",
  bg="radial-gradient(ellipse at 15% 20%, rgba(255,150,200,.90), transparent 36%),radial-gradient(ellipse at 85% 35%, rgba(255,110,160,.80), transparent 38%),radial-gradient(ellipse at 55% 90%, rgba(200,90,180,.75), transparent 40%),linear-gradient(150deg,#2b0f22,#471a38 55%,#33122b)",
  t="#fff", td="rgba(255,255,255,.68)",
  cbg="linear-gradient(135deg,rgba(255,160,210,.20),rgba(255,255,255,.07) 48%,rgba(255,120,180,.14))",
  cbd="rgba(255,160,210,.34)", cbdh="rgba(255,160,210,.58)", blur="24px", sat="180%",
  sh1="rgba(255,255,255,.45)", acc="#ff9ecf",
  hlang="122deg", hl="rgba(255,255,255,.34) 0%,rgba(255,255,255,.08) 18%,transparent 42%,transparent 72%,rgba(255,160,210,.22) 100%",
  arcpos="top:-60px;left:-38px", arcw="195px", arch="132px", arcrot="24deg",
  arcbd="rgba(255,160,210,.30)", arcin="rgba(255,160,210,.22)",
  pbd="rgba(255,160,210,.38)", pbg="rgba(255,160,210,.12)",
  avb="rgba(255,255,255,.55)", fbd="rgba(255,160,210,.45)",
  btn="linear-gradient(135deg,#ff7fb8,#f04f9a)", btns="rgba(255,127,184,.45)", btng="rgba(255,160,210,.10)",
  vbg="rgba(255,160,210,.10)", thbg="linear-gradient(135deg,#471a38,#2b0f22)", fallback="rgba(74,28,58,.93)"),
]

FG = {  # face gradients cycle
 "n01": ["linear-gradient(145deg,#3f8fd0,#1a4f86)", "linear-gradient(145deg,#57b8a8,#22705f)", "linear-gradient(145deg,#7f9ff0,#3a4fb0)"],
 "n02": ["linear-gradient(145deg,#ff7fb8,#c93f9a)", "linear-gradient(145deg,#b06cf0,#6a34c8)", "linear-gradient(145deg,#ff9a6c,#e05a3a)"],
 "n03": ["linear-gradient(145deg,#f5a06c,#d96a4a)", "linear-gradient(145deg,#f7c873,#dda04a)", "linear-gradient(145deg,#ef8fb0,#c85a80)"],
 "n04": ["linear-gradient(145deg,#4fd6a4,#1f9a6c)", "linear-gradient(145deg,#6cc8e8,#2f7fb0)", "linear-gradient(145deg,#a8e06c,#5da83a)"],
 "n05": ["linear-gradient(145deg,#ff9a4d,#d1542a)", "linear-gradient(145deg,#ff6c6c,#c23a4a)", "linear-gradient(145deg,#ffb84d,#dd8a2a)"],
 "n06": ["linear-gradient(145deg,#8f8fa8,#4a4a5e)", "linear-gradient(145deg,#a89fd0,#5e54a8)", "linear-gradient(145deg,#7a7a90,#3a3a48)"],
 "n07": ["linear-gradient(145deg,#7fb2d9,#3f7fb0)", "linear-gradient(145deg,#9fc8e0,#5a8fb8)", "linear-gradient(145deg,#6c9fc8,#2f5f8a)"],
 "n08": ["linear-gradient(145deg,#ff8f7a,#e05a6c)", "linear-gradient(145deg,#7ac8ff,#4a7fe0)", "linear-gradient(145deg,#b08fff,#7a4fd0)"],
 "n09": ["linear-gradient(145deg,#a8c8d8,#5a7f90)", "linear-gradient(145deg,#c8d8e0,#7a9098)", "linear-gradient(145deg,#90b8c8,#4a6f80)"],
 "n10": ["linear-gradient(145deg,#ff9ecf,#e05a9a)", "linear-gradient(145deg,#ffb87a,#e08a4a)", "linear-gradient(145deg,#c89eff,#8a5ae0)"],
}

def build_css(th):
    c = CSS
    for k, v in th.items():
        if k in ("num", "title", "eyebrow", "hint"):
            continue
        c = c.replace("VAR_" + k.upper(), v)
    return c

def page(th, cards_html):
    return f"""<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{th['title']}</title>
<style>{build_css(th)}</style>
</head>
<body>
<main>
<header class="heading">
<p class="eyebrow">{th['eyebrow']}</p>
<h1>{th['title']}</h1>
<p class="hint">{th['hint']}</p>
</header>
{cards_html}
</main>
</body>
</html>
"""

def write(num, th, cards):
    p = os.path.join(OUT, f"{num}.html")
    with open(p, "w", encoding="utf-8") as f:
        f.write(page(th, "\n".join(cards)))
    print("wrote", p)

WV = [(6,0),(10,.15),(16,.3),(22,.45),(28,.6),(20,.75),(12,.9)]

def main():
    T = {t["num"]: t for t in THEMES}
    F = FG
    # n01 深海私语：私聊 x3（1 张带回复按钮）
    write("n01", T["n01"], [
     '<section class="card">' + top("私聊", [avatar("沈", F["n01"][0]), avatar("聆", F["n01"][1])]) +
     row("沈", F["n01"][0], "沈聆", "21:04", "明晚的展你去吗，我多了一张票", '<span class="unread">2 条未读</span>') +
     actions(("回复", False)) + '</section>',
     '<section class="card">' + top("私聊", [avatar("顾", F["n01"][2])]) +
     row("顾", F["n01"][2], "顾潮生", "18:32", "刚把合同发你邮箱了，查收一下", '<span class="unread">1 条未读</span>', rev=True) + '</section>',
     '<section class="card">' + top("私聊", [avatar("白", F["n01"][1])]) +
     row("白", F["n01"][1], "白鹭", "12:15", "新店开业，周六来捧场呀", '<time>已读</time>') + '</section>',
    ])
    # n02 霓虹点赞：点赞 x3（带内容缩略图）
    def likecard(face_ch, i, name, tm, what):
        return ('<section class="card">' + top("点赞", [avatar(face_ch, F["n02"][i])]) +
         f'<div class="row"><div class="face" style="background:{F["n02"][i]}">{face_ch}</div>'
         f'<div class="copy"><div class="title-line"><strong>{name}</strong><time>{tm}</time></div>'
         f'<div class="preview">赞了你的{what}</div></div><div class="thumb"></div></div></section>')
    write("n02", T["n02"], [
     likecard("陆", 0, "陆燃", "10:24", "照片《城市夜跑》"),
     likecard("桃", 1, "桃子汽水", "09:02", "评论"),
     likecard("野", 2, "阿野", "昨天", "视频《雨后初晴》"),
    ])
    # n03 蜜桃群聊：群聊 x3
    write("n03", T["n03"], [
     '<section class="card">' + top("群聊", [avatar("苏", F["n03"][0]), avatar("蔓", F["n03"][1]), avatar("阿", F["n03"][2])], "+12") +
     row("苏", F["n03"][0], "露营小分队", "19:48", "苏蔓：帐篷我借到了，周五见", '<span class="unread">9 条未读</span>') + '</section>',
     '<section class="card">' + top("群聊", [avatar("陈", F["n03"][1]), avatar("皮", F["n03"][2])], "+5") +
     row("陈", F["n03"][1], "干饭小队", "18:05", "陈皮：新开的火锅店，今晚冲", '<span class="unread">3 条未读</span>') + '</section>',
     '<section class="card">' + top("群聊", [avatar("周", F["n03"][2])], "+8") +
     row("周", F["n03"][2], "读书会", "昨天", "老周：下周读《海底两万里》", '<time>已读</time>') + '</section>',
    ])
    # n04 薄荷评论：评论 x3（带查看按钮）
    write("n04", T["n04"], [
     '<section class="card">' + top("评论", [avatar("青", F["n04"][0])]) +
     row("青", F["n04"][0], "青柠", "11:20", "回复了你：这个角度绝了，求教程", '<span class="unread">新评论</span>') +
     actions(("查看", False), ("稍后", True)) + '</section>',
     '<section class="card">' + top("评论", [avatar("海", F["n04"][1])]) +
     row("海", F["n04"][1], "海盐", "10:47", "同问+1，已经收藏了", '<time>已读</time>') + '</section>',
     '<section class="card">' + top("评论", [avatar("满", F["n04"][2])]) +
     row("满", F["n04"][2], "小满", "昨天", "已试，真的好用！", '<time>已读</time>') + '</section>',
    ])
    # n05 熔岩关注：新增关注 x3（回关按钮）
    write("n05", T["n05"], [
     '<section class="card">' + top("关注", [avatar("火", F["n05"][0])]) +
     row("火", F["n05"][0], "火星电台", "14:33", "关注了你，来听听我们的新节目", '<span class="unread">新粉丝</span>') +
     actions(("回关", False)) + '</section>',
     '<section class="card">' + top("关注", [avatar("咖", F["n05"][1])]) +
     row("咖", F["n05"][1], "咖啡因漫游指南", "13:10", "关注了你，城市咖啡地图更新了", '<span class="unread">新粉丝</span>') +
     actions(("回关", False)) + '</section>',
     '<section class="card">' + top("关注", [avatar("夜", F["n05"][2])]) +
     row("夜", F["n05"][2], "夜行摄影师", "昨天", "关注了你", '<time>已互关</time>') + '</section>',
    ])
    # n06 墨晕好友：好友请求 x3（接受/忽略）
    write("n06", T["n06"], [
     '<section class="card">' + top("好友请求", [avatar("江", F["n06"][0])]) +
     row("江", F["n06"][0], "江离", "16:02", "我们是校友，方便通过一下吗", "") +
     actions(("接受", False), ("忽略", True)) + '</section>',
     '<section class="card">' + top("好友请求", [avatar("雾", F["n06"][1])]) +
     row("雾", F["n06"][1], "雾岛", "15:44", "上次展会上见过，想加个好友", "") +
     actions(("接受", False), ("忽略", True)) + '</section>',
     '<section class="card">' + top("好友请求", [avatar("南", F["n06"][2])]) +
     row("南", F["n06"][2], "南柯", "昨天", "朋友推荐的，想交流摄影", '<time>待处理</time>') + '</section>',
    ])
    # n07 晨雾提及：@提及 x3（1 张头像右）
    write("n07", T["n07"], [
     '<section class="card">' + top("@提及", [avatar("星", F["n07"][0])]) +
     row("星", F["n07"][0], "星野", "09:56", "在「周末去哪」中提到了你", '<span class="unread">@我</span>') + '</section>',
     '<section class="card">' + top("@提及", [avatar("林", F["n07"][1])]) +
     row("林", F["n07"][1], "林晚", "08:20", "在评论中提到了你：快看这个", '<span class="unread">@我</span>', rev=True) + '</section>',
     '<section class="card">' + top("@提及", [avatar("澈", F["n07"][2])]) +
     row("澈", F["n07"][2], "阿澈", "昨天", "在「旅行计划」中提到了你", '<time>已读</time>') + '</section>',
    ])
    # n08 彩虹转发：转发 x3（带缩略图）
    def sharecard(face_ch, i, name, tm, what):
        return ('<section class="card">' + top("转发", [avatar(face_ch, F["n08"][i])]) +
         f'<div class="row"><div class="face" style="background:{F["n08"][i]}">{face_ch}</div>'
         f'<div class="copy"><div class="title-line"><strong>{name}</strong><time>{tm}</time></div>'
         f'<div class="preview">转发了你的{what}</div></div><div class="thumb"></div></div></section>')
    write("n08", T["n08"], [
     sharecard("云", 0, "云朵", "17:25", "动态"),
     sharecard("风", 1, "晚风", "16:03", "视频《山间晨雾》"),
     sharecard("糖", 2, "糖炒栗子", "昨天", "文章《秋日食谱》"),
    ])
    # n09 水银语音：语音消息 x3（语音条）
    write("n09", T["n09"], [
     '<section class="card">' + top("语音", [avatar("秦", F["n09"][0])]) +
     row("秦", F["n09"][0], "秦朗", "20:11", "发来一条语音", '<span class="unread">0:42</span>') +
     '<div style="margin-top:12px">' + voice_bar(WV) + '</div></section>',
     '<section class="card">' + top("语音", [avatar("栀", F["n09"][1])]) +
     row("栀", F["n09"][1], "栀子", "19:47", "发来一条语音", '<span class="unread">1:15</span>') +
     '<div style="margin-top:12px">' + voice_bar([(h, d + .2) for h, d in WV]) + '</div></section>',
     '<section class="card">' + top("语音", [avatar("牧", F["n09"][2])]) +
     row("牧", F["n09"][2], "牧野", "昨天", "发来一条语音", '<time>已听</time>') + '</section>',
    ])
    # n10 果冻开播：开播提醒 x3（进入直播间）
    write("n10", T["n10"], [
     '<section class="card">' + top("开播", [avatar("莓", F["n10"][0])]) +
     row("莓", F["n10"][0], "草莓酱", "刚刚", '<span class="livedot"></span>正在直播：深夜电台｜聊聊最近的书', '<span class="unread">LIVE</span>') +
     actions(("进入直播间", False)) + '</section>',
     '<section class="card">' + top("开播", [avatar("荷", F["n10"][1])]) +
     row("荷", F["n10"][1], "薄荷岛主", "21:30", '<span class="livedot"></span>正在直播：带你云逛夜市', '<span class="unread">LIVE</span>') +
     actions(("进入直播间", False)) + '</section>',
     '<section class="card">' + top("开播", [avatar("橘", F["n10"][2])]) +
     row("橘", F["n10"][2], "橘子汽水", "20:05", "开播预告：明晚手账拼贴实况", '<time>预约</time>') + '</section>',
    ])

if __name__ == "__main__":
    main()
