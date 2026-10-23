#!/usr/bin/env python3
"""生成 n21-n30 液态玻璃通知卡片（日程提醒方向）"""
import os

D = os.path.dirname(os.path.abspath(__file__))

CORE_CSS = """
*{box-sizing:border-box}
body{min-height:100vh;margin:0;padding:48px 18px;color:#fff;
font:15px/1.45 -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
background:VARBG;background-attachment:fixed}
main{width:min(440px,100%);margin:0 auto;display:grid;gap:18px}
.heading{padding:4px 6px 8px}
.eyebrow{margin:0 0 8px;color:VARHINT;font-size:11px;letter-spacing:.18em}
h1{margin:0;font-size:30px;letter-spacing:-.04em}
.hint{margin:7px 0 0;color:VARHINT}
.card{position:relative;isolation:isolate;overflow:hidden;padding:18px;
border:1px solid VARBORDER;border-radius:28px;
background:VARGLASS;
-webkit-backdrop-filter:blur(VARBLUR) saturate(VARSAT);
backdrop-filter:blur(VARBLUR) saturate(VARSAT);
box-shadow:inset 0 1px 0 rgba(255,255,255,.42),inset 0 -1px 0 rgba(255,255,255,.08),0 20px 48px rgba(8,8,24,.28)}
.card::before{content:"";position:absolute;z-index:0;inset:0;border-radius:inherit;pointer-events:none;
background:linear-gradient(VARANGLE,rgba(255,255,255,.34) 0%,rgba(255,255,255,.08) 18%,transparent 42%,transparent 72%,VARHLT 100%);opacity:.8}
.card::after{content:"";position:absolute;z-index:0;VARARCPOS;width:VARARCW;height:VARARCH;
border:1px solid rgba(255,255,255,.22);border-radius:50%;
background:radial-gradient(ellipse,rgba(255,255,255,.22),transparent 68%);filter:blur(2px);
transform:rotate(VARARCROT);pointer-events:none}
.card>*{position:relative;z-index:1}
.top,.title-line{display:flex;align-items:center;justify-content:space-between;gap:12px}
.top{margin-bottom:17px}
.pill{padding:6px 12px;border:1px solid rgba(255,255,255,.30);border-radius:999px;
background:rgba(255,255,255,.10);color:rgba(255,255,255,.94);font-size:12px;
box-shadow:inset 0 1px rgba(255,255,255,.18)}
.avatars{display:flex;align-items:center;padding-left:8px}
.avatar{display:grid;width:29px;height:29px;margin-left:-8px;place-items:center;
border:1px solid rgba(255,255,255,.55);border-radius:50%;background:VARAV;color:#fff;
font-size:11px;box-shadow:0 3px 10px rgba(18,12,36,.2)}
.more{margin-left:7px;color:rgba(255,255,255,.72);font-size:12px}
.row{display:flex;align-items:center;gap:12px;min-width:0}
.face{display:grid;flex:0 0 48px;height:48px;place-items:center;
border:1px solid rgba(255,255,255,.45);border-radius:50%;background:VARAV;color:#fff;
font-size:19px;font-weight:650;box-shadow:inset 0 1px 5px rgba(255,255,255,.5),0 5px 15px rgba(15,12,35,.2)}
.face.sq{border-radius:16px}
.copy{flex:1;min-width:0}
.title-line{margin-bottom:5px}
.title-line strong{overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
time,.preview{color:rgba(255,255,255,.72);font-size:12px}
.preview{overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.unread{flex:0 0 auto;color:#d8d2ff;font-size:12px;font-weight:600}
/* 专属组件 */
.cd{display:flex;gap:8px;align-items:baseline;margin:2px 0 4px}
.cd b{font-size:38px;font-weight:700;letter-spacing:.04em;font-variant-numeric:tabular-nums}
.cd span{font-size:12px;color:rgba(255,255,255,.66)}
.cal{flex:0 0 54px;height:60px;border-radius:14px;display:grid;place-content:center;
border:1px solid rgba(255,255,255,.4);background:rgba(255,255,255,.12);
box-shadow:inset 0 1px 0 rgba(255,255,255,.3)}
.cal b{font-size:22px;line-height:1}
.cal i{font-style:normal;font-size:10px;color:rgba(255,255,255,.7);white-space:nowrap}
.btns{display:flex;gap:10px;margin-top:14px}
.btn{flex:1;padding:11px 0;border-radius:14px;border:1px solid rgba(255,255,255,.35);
background:rgba(255,255,255,.12);color:#fff;font-size:13px;cursor:pointer;font-family:inherit}
.btn.solid{background:linear-gradient(135deg,VARACC1,VARACC2);border-color:transparent;font-weight:700;
box-shadow:0 6px 18px rgba(10,10,30,.35)}
.prog{height:10px;border-radius:6px;background:rgba(255,255,255,.14);margin-top:14px;overflow:hidden}
.prog i{display:block;height:100%;border-radius:6px;background:linear-gradient(90deg,VARACC1,VARACC2)}
.progtxt{display:flex;justify-content:space-between;font-size:12px;color:rgba(255,255,255,.72);margin-top:6px}
.sw{position:relative;width:52px;height:30px;flex:0 0 auto}
.sw input{position:absolute;opacity:0;inset:0;margin:0;cursor:pointer}
.sw em{position:absolute;inset:0;border-radius:999px;background:rgba(255,255,255,.18);
border:1px solid rgba(255,255,255,.35);transition:.25s}
.sw em::after{content:"";position:absolute;top:3px;left:3px;width:22px;height:22px;border-radius:50%;
background:#fff;transition:.25s;box-shadow:0 2px 6px rgba(0,0,0,.3)}
.sw input:checked+em{background:linear-gradient(135deg,VARACC1,VARACC2)}
.sw input:checked+em::after{left:25px}
.chk{display:flex;align-items:center;gap:10px;padding:9px 0;border-bottom:1px solid rgba(255,255,255,.10);
font-size:13px}
.chk:last-child{border-bottom:0}
.chk .box{flex:0 0 20px;height:20px;border-radius:7px;border:1.5px solid rgba(255,255,255,.5);
display:grid;place-items:center;font-size:13px;color:#fff}
.chk.done .box{background:linear-gradient(135deg,VARACC1,VARACC2);border-color:transparent}
.chk.done span{color:rgba(255,255,255,.5);text-decoration:line-through}
.ringwrap{display:flex;align-items:center;gap:14px}
.ringwrap svg{flex:0 0 auto}
.bigtime{font-size:52px;font-weight:700;letter-spacing:.02em;font-variant-numeric:tabular-nums;line-height:1.1}
.sub{font-size:12px;color:rgba(255,255,255,.68)}
@supports not ((backdrop-filter:blur(1px)) or (-webkit-backdrop-filter:blur(1px))){.card{background:rgba(43,35,68,.88)}}
@media (prefers-reduced-motion:reduce){.card{transition:none}}
"""

ITEMS = [
 dict(num=21, cls="nc21", title="会议倒计时", eyebrow="LIQUID GLASS · MEETING", h1="会议提醒",
      hint="重要的会，一场都别错过。",
      bg="radial-gradient(ellipse at 18% 12%, rgba(56,120,255,.85), transparent 36%),radial-gradient(ellipse at 85% 30%, rgba(20,60,140,.9), transparent 38%),radial-gradient(ellipse at 50% 92%, rgba(90,40,180,.75), transparent 40%),linear-gradient(150deg,#0b1e4a,#101a3a 55%,#141b38)",
      hintc="rgba(190,215,255,.68)",
      glass="linear-gradient(135deg,rgba(120,170,255,.22),rgba(255,255,255,.07) 48%,rgba(120,150,255,.14))",
      blur="28px", sat="160%", border="rgba(140,180,255,.32)", angle="118deg", hlt="rgba(150,200,255,.18)",
      arcpos="top:-58px;right:-42px", arcw="190px", arch="130px", arcrot="-20deg",
      av="linear-gradient(135deg,#7fb2ff,#4a6fe0 70%,#2b3fa0)",
      acc1="#5aa2ff", acc2="#7a5cff",
      body="""
<section class="card"><div class="top"><span class="pill">会议 · 10:30</span>
<div class="avatars"><i class="avatar">陈</i><i class="avatar">沈</i><i class="avatar">陆</i><span class="more">+5</span></div></div>
<div class="cd"><b>02</b><span>时</span><b>14</b><span>分</span><b>52</b><span>秒</span></div>
<div class="row"><div class="face">审</div><div class="copy">
<div class="title-line"><strong>新品评审会</strong><time>会议室 A · 3F</time></div>
<div class="preview">请提前准备好原型演示稿</div></div></div>
<div class="btns"><button class="btn">稍后提醒</button><button class="btn solid">加入会议</button></div></section>
<section class="card"><div class="top"><span class="pill">例会 · 明天</span><time>09:00</time></div>
<div class="row"><div class="face">例</div><div class="copy">
<div class="title-line"><strong>团队周例会</strong><time>线上</time></div>
<div class="preview">各组同步本周进展与风险项</div></div>
<span class="unread">距今 21 小时</span></div></section>"""),

 dict(num=22, cls="nc22", title="生日快乐", eyebrow="LIQUID GLASS · BIRTHDAY", h1="生日祝福",
      hint="记得对重要的人说生日快乐。",
      bg="radial-gradient(ellipse at 80% 15%, rgba(255,180,120,.9), transparent 36%),radial-gradient(ellipse at 12% 40%, rgba(255,110,150,.8), transparent 38%),radial-gradient(ellipse at 55% 90%, rgba(200,90,120,.7), transparent 40%),linear-gradient(150deg,#3a1c2e,#47263a 55%,#331d33)",
      hintc="rgba(255,220,200,.68)",
      glass="linear-gradient(135deg,rgba(255,205,170,.22),rgba(255,255,255,.08) 48%,rgba(255,160,190,.16))",
      blur="20px", sat="180%", border="rgba(255,200,170,.34)", angle="65deg", hlt="rgba(255,190,150,.20)",
      arcpos="bottom:-60px;left:-40px", arcw="200px", arch="140px", arcrot="25deg",
      av="linear-gradient(135deg,#ffc79e,#ff8fb0 70%,#d06090)",
      acc1="#ff9a6a", acc2="#ff5f9a",
      body="""
<section class="card"><div class="top"><span class="pill">今天 · 生日</span><span class="more">🎂 就是今天</span></div>
<div class="row"><div class="face">妈</div><div class="copy">
<div class="title-line"><strong>妈妈的生日</strong><time>全天</time></div>
<div class="preview">记得打电话，蛋糕已下单 18:00 送达</div></div></div>
<div class="btns"><button class="btn solid">送上祝福</button></div></section>
<section class="card"><div class="top"><span class="pill">还有 3 天</span><time>10-25</time></div>
<div class="row"><div class="face">满</div><div class="copy">
<div class="title-line"><strong>林小满生日派对</strong><time>19:00 · 老地方</time></div>
<div class="preview">记得带礼物，着装要求：亮色</div></div>
<span class="unread">3 天后</span></div></section>"""),

 dict(num=23, cls="nc23", title="航班登机", eyebrow="LIQUID GLASS · FLIGHT", h1="航班提醒",
      hint="登机口关闭前，别让飞机等你。",
      bg="radial-gradient(ellipse at 20% 85%, rgba(255,170,80,.85), transparent 38%),radial-gradient(ellipse at 85% 20%, rgba(80,160,255,.85), transparent 36%),radial-gradient(ellipse at 50% 50%, rgba(40,80,180,.5), transparent 45%),linear-gradient(155deg,#16294d,#1d2c55 55%,#241f4a)",
      hintc="rgba(200,225,255,.68)",
      glass="linear-gradient(135deg,rgba(140,190,255,.20),rgba(255,255,255,.07) 48%,rgba(255,180,120,.14))",
      blur="22px", sat="170%", border="rgba(150,200,255,.30)", angle="150deg", hlt="rgba(160,205,255,.18)",
      arcpos="top:-50px;left:-50px", arcw="180px", arch="120px", arcrot="35deg",
      av="linear-gradient(135deg,#8fc3ff,#4a7fe0 70%,#2b4fa0)",
      acc1="#4a9aff", acc2="#ff9a5a",
      body="""
<section class="card"><div class="top"><span class="pill">登机提醒</span><span class="unread">45 分钟后起飞</span></div>
<div class="row"><div class="face sq">✈</div><div class="copy">
<div class="title-line"><strong>CA1832 · 北京 → 上海</strong><time>登机口 B12</time></div>
<div class="preview">座位 24A · 请提前 30 分钟到达登机口</div></div></div>
<div class="btns"><button class="btn">查看登机牌</button><button class="btn solid">去值机</button></div></section>
<section class="card"><div class="top"><span class="pill">延误通知</span><time>刚刚</time></div>
<div class="row"><div class="face sq">◷</div><div class="copy">
<div class="title-line"><strong>MU5101 延误 40 分钟</strong><time>天气原因</time></div>
<div class="preview">预计起飞 21:20，已为您保留餐食</div></div></div></section>"""),

 dict(num=24, cls="nc24", title="吃药提醒", eyebrow="LIQUID GLASS · MEDS", h1="用药提醒",
      hint="按时吃药，身体才听你的话。",
      bg="radial-gradient(ellipse at 15% 20%, rgba(120,230,190,.8), transparent 36%),radial-gradient(ellipse at 85% 75%, rgba(60,180,160,.75), transparent 38%),radial-gradient(ellipse at 55% 45%, rgba(140,240,210,.4), transparent 42%),linear-gradient(150deg,#0f3a34,#14443c 55%,#103a3a)",
      hintc="rgba(200,245,225,.68)",
      glass="linear-gradient(135deg,rgba(255,255,255,.24),rgba(255,255,255,.10) 48%,rgba(150,240,200,.14))",
      blur="18px", sat="165%", border="rgba(255,255,255,.32)", angle="100deg", hlt="rgba(170,245,215,.18)",
      arcpos="top:-55px;right:-35px", arcw="170px", arch="120px", arcrot="-30deg",
      av="linear-gradient(135deg,#8fe8c0,#3fb98f 70%,#1f8a68)",
      acc1="#3fd08f", acc2="#22a5b0",
      body="""
<section class="card"><div class="top"><span class="pill">早 8:00</span>
<label class="sw"><input type="checkbox" checked><em></em></label></div>
<div class="row"><div class="face">维</div><div class="copy">
<div class="title-line"><strong>维生素 D · 1 粒</strong><time>饭后服用</time></div>
<div class="preview">连续服用第 12 天，继续保持</div></div></div>
<div class="btns"><button class="btn">稍后 10 分钟</button><button class="btn solid">已服用</button></div></section>
<section class="card"><div class="top"><span class="pill">晚 20:00</span>
<label class="sw"><input type="checkbox"><em></em></label></div>
<div class="row"><div class="face">压</div><div class="copy">
<div class="title-line"><strong>降压药 · 半片</strong><time>睡前服用</time></div>
<div class="preview">服药后请静坐 5 分钟再活动</div></div></div></section>"""),

 dict(num=25, cls="nc25", title="健身打卡", eyebrow="LIQUID GLASS · FITNESS", h1="运动提醒",
      hint="今天的汗，是明天的光。",
      bg="radial-gradient(ellipse at 85% 15%, rgba(255,120,60,.9), transparent 36%),radial-gradient(ellipse at 10% 80%, rgba(255,60,90,.75), transparent 38%),radial-gradient(ellipse at 55% 45%, rgba(255,160,60,.45), transparent 42%),linear-gradient(150deg,#3d1520,#471a24 55%,#331420)",
      hintc="rgba(255,215,190,.68)",
      glass="linear-gradient(135deg,rgba(255,150,110,.22),rgba(255,255,255,.07) 48%,rgba(255,120,90,.15))",
      blur="26px", sat="175%", border="rgba(255,170,120,.32)", angle="135deg", hlt="rgba(255,170,120,.20)",
      arcpos="bottom:-55px;right:-45px", arcw="210px", arch="140px", arcrot="-15deg",
      av="linear-gradient(135deg,#ffa07a,#ff6a5a 70%,#d04040)",
      acc1="#ff7a4a", acc2="#ff3d6a",
      body="""
<section class="card"><div class="top"><span class="pill">今日训练</span><span class="more">🔥 连续 12 天</span></div>
<div class="ringwrap">
<svg width="86" height="86" viewBox="0 0 86 86"><circle cx="43" cy="43" r="36" fill="none" stroke="rgba(255,255,255,.15)" stroke-width="9"/><circle cx="43" cy="43" r="36" fill="none" stroke="url(#fg)" stroke-width="9" stroke-linecap="round" stroke-dasharray="226" stroke-dashoffset="90" transform="rotate(-90 43 43)"/><defs><linearGradient id="fg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#ff7a4a"/><stop offset="1" stop-color="#ff3d6a"/></linearGradient></defs><text x="43" y="49" text-anchor="middle" fill="#fff" font-size="17" font-weight="700">3/5</text></svg>
<div class="copy"><div class="title-line"><strong>胸 + 三头 · 45 分钟</strong></div>
<div class="preview">18:30 开始，本周还差 2 次达标</div></div></div>
<div class="btns"><button class="btn solid">开始打卡</button></div></section>
<section class="card"><div class="top"><span class="pill">恢复提醒</span><time>21:00</time></div>
<div class="row"><div class="face">睡</div><div class="copy">
<div class="title-line"><strong>今晚早点睡</strong><time>目标 23:00</time></div>
<div class="preview">肌肉在睡眠中生长，别熬夜</div></div></div></section>"""),

 dict(num=26, cls="nc26", title="课程提醒", eyebrow="LIQUID GLASS · CLASS", h1="课程表",
      hint="下一节课，别迟到。",
      bg="radial-gradient(ellipse at 20% 15%, rgba(150,110,255,.85), transparent 36%),radial-gradient(ellipse at 88% 70%, rgba(90,60,200,.8), transparent 38%),radial-gradient(ellipse at 50% 45%, rgba(190,150,255,.4), transparent 42%),linear-gradient(150deg,#241a4d,#2c2158 55%,#1f1845)",
      hintc="rgba(215,200,255,.68)",
      glass="linear-gradient(135deg,rgba(170,140,255,.22),rgba(255,255,255,.07) 48%,rgba(150,120,255,.14))",
      blur="24px", sat="170%", border="rgba(180,150,255,.32)", angle="80deg", hlt="rgba(190,160,255,.18)",
      arcpos="top:-60px;left:-45px", arcw="185px", arch="125px", arcrot="20deg",
      av="linear-gradient(135deg,#b49aff,#7a5fe0 70%,#4a35b0)",
      acc1="#9a7bff", acc2="#6a4ae0",
      body="""
<section class="card"><div class="top"><span class="pill">下一节 · 08:00</span><span class="unread">25 分钟后</span></div>
<div class="row"><div class="cal"><b>23</b><i>10月 · 周四</i></div><div class="copy">
<div class="title-line"><strong>高等数学</strong><time>08:00–09:40</time></div>
<div class="preview">教学楼 302 · 记得带习题册</div></div></div>
<div class="btns"><button class="btn">查看课表</button><button class="btn solid">导航前往</button></div></section>
<section class="card"><div class="top"><span class="pill">下午</span><time>14:00</time></div>
<div class="row"><div class="cal"><b>23</b><i>10月 · 周四</i></div><div class="copy">
<div class="title-line"><strong>英语口语</strong><time>14:00–15:30</time></div>
<div class="preview">外教课 · 提前 10 分钟到语音室</div></div></div></section>"""),

 dict(num=27, cls="nc27", title="纪念日", eyebrow="LIQUID GLASS · MEMORY", h1="重要日子",
      hint="每一个值得纪念的日子，都闪闪发光。",
      bg="radial-gradient(ellipse at 15% 80%, rgba(255,150,170,.85), transparent 36%),radial-gradient(ellipse at 85% 20%, rgba(230,140,160,.8), transparent 38%),radial-gradient(ellipse at 55% 50%, rgba(255,190,200,.4), transparent 42%),linear-gradient(150deg,#3d1e2c,#4a2436 55%,#331a28)",
      hintc="rgba(255,210,220,.68)",
      glass="linear-gradient(135deg,rgba(255,255,255,.16),rgba(255,255,255,.06) 48%,rgba(255,170,190,.14))",
      blur="30px", sat="150%", border="rgba(255,190,205,.30)", angle="160deg", hlt="rgba(255,180,200,.18)",
      arcpos="top:-52px;right:-50px", arcw="200px", arch="135px", arcrot="-25deg",
      av="linear-gradient(135deg,#ffb0c0,#e07090 70%,#b04070)",
      acc1="#ff8fa8", acc2="#e05080",
      body="""
<section class="card"><div class="top"><span class="pill">就是今天</span><span class="more">💗 相识 1000 天</span></div>
<div class="cd"><b>1000</b><span>天</span></div>
<div class="row"><div class="face">念</div><div class="copy">
<div class="title-line"><strong>相识纪念日</strong><time>全天</time></div>
<div class="preview">餐厅已订好 19:00，别忘了花</div></div></div>
<div class="btns"><button class="btn solid">写下心愿</button></div></section>
<section class="card"><div class="top"><span class="pill">倒计时</span><span class="unread">还有 30 天</span></div>
<div class="row"><div class="face">婚</div><div class="copy">
<div class="title-line"><strong>婚礼 · 三亚</strong><time>11-21</time></div>
<div class="preview">伴手礼清单还差 3 项没确认</div></div></div></section>"""),

 dict(num=28, cls="nc28", title="待办清单", eyebrow="LIQUID GLASS · TODO", h1="今日待办",
      hint="一件一件来，都会搞定的。",
      bg="radial-gradient(ellipse at 85% 15%, rgba(70,200,190,.8), transparent 36%),radial-gradient(ellipse at 12% 75%, rgba(40,140,160,.75), transparent 38%),radial-gradient(ellipse at 55% 45%, rgba(110,220,210,.4), transparent 42%),linear-gradient(150deg,#0e3a3c,#123f42 55%,#0c3336)",
      hintc="rgba(195,240,235,.68)",
      glass="linear-gradient(135deg,rgba(140,230,220,.20),rgba(255,255,255,.07) 48%,rgba(120,210,200,.13))",
      blur="20px", sat="165%", border="rgba(150,235,225,.30)", angle="45deg", hlt="rgba(160,240,230,.18)",
      arcpos="bottom:-58px;left:-42px", arcw="190px", arch="130px", arcrot="30deg",
      av="linear-gradient(135deg,#7fdcd0,#35a8a0 70%,#1f7a75)",
      acc1="#3fc8b8", acc2="#1f9a90",
      body="""
<section class="card"><div class="top"><span class="pill">今日 · 3/5</span><span class="more">加油，还差 2 件</span></div>
<div class="chk done"><span class="box">✓</span><span>回复房东关于续租的消息</span></div>
<div class="chk done"><span class="box">✓</span><span>给阳台的绿萝浇水</span></div>
<div class="chk"><span class="box"></span><span>打印明天的会议资料</span></div>
<div class="chk"><span class="box"></span><span>预约周六的洗牙</span></div>
<div class="chk"><span class="box"></span><span>把旧衣服捐出去</span></div>
<div class="prog"><i style="width:60%"></i></div>
<div class="progtxt"><span>已完成 3 件</span><span>60%</span></div></section>
<section class="card"><div class="top"><span class="pill">明日预告</span><time>4 件待办</time></div>
<div class="row"><div class="face">明</div><div class="copy">
<div class="title-line"><strong>明天的第一件事</strong><time>07:30</time></div>
<div class="preview">晨跑 5 公里，跑鞋已放在门口</div></div></div></section>"""),

 dict(num=29, cls="nc29", title="喝水提醒", eyebrow="LIQUID GLASS · WATER", h1="补水时间",
      hint="多喝水，皮肤会替你说谢谢。",
      bg="radial-gradient(ellipse at 20% 20%, rgba(120,190,255,.85), transparent 36%),radial-gradient(ellipse at 85% 80%, rgba(60,130,230,.8), transparent 38%),radial-gradient(ellipse at 55% 50%, rgba(150,210,255,.4), transparent 42%),linear-gradient(150deg,#123a5e,#163f66 55%,#0f2f52)",
      hintc="rgba(200,230,255,.68)",
      glass="linear-gradient(135deg,rgba(255,255,255,.26),rgba(255,255,255,.12) 48%,rgba(150,200,255,.15))",
      blur="16px", sat="160%", border="rgba(255,255,255,.36)", angle="120deg", hlt="rgba(170,215,255,.20)",
      arcpos="top:-55px;left:-40px", arcw="175px", arch="120px", arcrot="15deg",
      av="linear-gradient(135deg,#8fc8ff,#3f8fe0 70%,#1f5fae)",
      acc1="#4aa8ff", acc2="#2a7ae0",
      body="""
<section class="card"><div class="top"><span class="pill">15:00 · 该喝水了</span><span class="more">💧 第 5 杯</span></div>
<div class="prog"><i style="width:60%"></i></div>
<div class="progtxt"><span>已喝 1200ml</span><span>目标 2000ml</span></div>
<div class="btns"><button class="btn">稍后提醒</button><button class="btn solid">记录一杯</button></div></section>
<section class="card"><div class="top"><span class="pill">久坐提醒</span><time>刚刚</time></div>
<div class="row"><div class="face">坐</div><div class="copy">
<div class="title-line"><strong>起来活动一下</strong><time>已坐 90 分钟</time></div>
<div class="preview">站起来走走，顺便把水喝了</div></div>
<span class="unread">动起来</span></div></section>"""),

 dict(num=30, cls="nc30", title="早起闹钟", eyebrow="LIQUID GLASS · ALARM", h1="闹钟",
      hint="新的一天，从准时醒来开始。",
      bg="radial-gradient(ellipse at 50% 100%, rgba(255,150,90,.85), transparent 40%),radial-gradient(ellipse at 85% 10%, rgba(255,120,140,.7), transparent 36%),radial-gradient(ellipse at 10% 25%, rgba(120,90,200,.6), transparent 38%),linear-gradient(160deg,#2b1a3d,#3a2140 55%,#4a2a35)",
      hintc="rgba(255,220,200,.68)",
      glass="linear-gradient(135deg,rgba(255,180,140,.20),rgba(255,255,255,.07) 48%,rgba(255,150,170,.13))",
      blur="24px", sat="170%", border="rgba(255,190,150,.30)", angle="170deg", hlt="rgba(255,190,160,.18)",
      arcpos="bottom:-60px;right:-40px", arcw="195px", arch="130px", arcrot="-35deg",
      av="linear-gradient(135deg,#ffb08a,#e0705a 70%,#b04040)",
      acc1="#ff9a6a", acc2="#ff5f7a",
      body="""
<section class="card"><div class="top"><span class="pill">起床闹钟 · 工作日</span>
<label class="sw"><input type="checkbox" checked><em></em></label></div>
<div class="bigtime">06:30</div>
<div class="sub">距离响铃还有 8 小时 12 分 · 铃声：晨光</div>
<div class="btns"><button class="btn">贪睡 10 分钟</button><button class="btn solid">关闭闹钟</button></div></section>
<section class="card"><div class="top"><span class="pill">午休小憩</span>
<label class="sw"><input type="checkbox" checked><em></em></label></div>
<div class="row"><div class="face">午</div><div class="copy">
<div class="title-line"><strong>12:30 · 20 分钟</strong><time>每天</time></div>
<div class="preview">小睡一下，下午效率翻倍</div></div></div></section>"""),
]

HTML = """<!doctype html>
<html lang="zh-CN">
<head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<style>{css}</style>
</head>
<body class="{cls}">
<main>
<header class="heading"><p class="eyebrow">{eyebrow}</p><h1>{h1}</h1><p class="hint">{hint}</p></header>
{cards}
</main>
</body>
</html>
"""

def build(it):
    css = CORE_CSS
    repl = {
        "VARBG": it["bg"], "VARHINT": it["hintc"], "VARGLASS": it["glass"],
        "VARBLUR": it["blur"], "VARSAT": it["sat"], "VARBORDER": it["border"],
        "VARANGLE": it["angle"], "VARHLT": it["hlt"],
        "VARARCPOS": it["arcpos"], "VARARCW": it["arcw"], "VARARCH": it["arch"],
        "VARARCROT": it["arcrot"], "VARAV": it["av"],
        "VARACC1": it["acc1"], "VARACC2": it["acc2"],
    }
    for k, v in repl.items():
        css = css.replace(k, v)
    return HTML.format(title=it["title"], css=css, cls=it["cls"],
                       eyebrow=it["eyebrow"], h1=it["h1"], hint=it["hint"],
                       cards=it["body"])

for it in ITEMS:
    fn = os.path.join(D, f"n{it['num']}.html")
    open(fn, "w", encoding="utf-8").write(build(it))
    print("wrote", fn, len(build(it))//1024, "KB")
