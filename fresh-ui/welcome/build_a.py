#!/usr/bin/env python3
# 生成 welcome A 组 w01-w18
import os, json

OUT = os.path.dirname(os.path.abspath(__file__))

HEAD = """<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>%%TITLE%%</title>
<style>
*{margin:0;padding:0;box-sizing:border-box;-webkit-tap-highlight-color:transparent}
body{font-family:-apple-system,BlinkMacSystemFont,"PingFang SC","Hiragino Sans GB","Microsoft YaHei",system-ui,sans-serif;background:#04060a;color:#eef2f7;display:flex;justify-content:center;min-height:100vh}
.phone{width:430px;height:900px;position:relative;overflow:hidden;background:%%PBG%%}
/* ---- mock app ---- */
.mk{padding:54px 20px 0;opacity:.85}
.sb{display:flex;justify-content:space-between;font-size:13px;color:#cfd6e2;margin-bottom:14px}
.mknav{font-size:22px;font-weight:800;margin:2px 0 16px}
.mkbanner{height:110px;border-radius:16px;background:linear-gradient(120deg,#2a3350,#3c2a50);margin-bottom:14px}
.mkrow{display:flex;gap:12px;align-items:center;background:rgba(255,255,255,.05);border-radius:14px;padding:12px;margin-bottom:10px}
.mkav{width:44px;height:44px;border-radius:50%;background:linear-gradient(135deg,#4a5a80,#2c3650);flex-shrink:0}
.mkln{height:10px;border-radius:5px;background:rgba(255,255,255,.12);margin:5px 0}
.mkgrid{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.mkcard{border-radius:14px;background:rgba(255,255,255,.05);padding:10px}
.mkph{height:80px;border-radius:10px;background:linear-gradient(135deg,#33405e,#232c46);margin-bottom:8px}
.mksearch{height:42px;border-radius:21px;background:rgba(255,255,255,.08);margin-bottom:16px}
.mkalbum{height:230px;border-radius:18px;background:linear-gradient(135deg,#3b2a5e,#1f2a4e);margin-bottom:14px}
.mkbar{height:6px;border-radius:3px;background:rgba(255,255,255,.12);margin:14px 0 6px;position:relative}
.mkbar i{display:block;position:absolute;left:0;top:0;bottom:0;width:38%;border-radius:3px;background:#7ab8ff}
.mkctl{display:flex;justify-content:center;gap:26px;margin-top:14px}
.mkctl i{display:block;width:46px;height:46px;border-radius:50%;background:rgba(255,255,255,.1)}
/* ---- overlay / modal ---- */
.ov{position:absolute;inset:0;z-index:30;display:flex;align-items:center;justify-content:center;background:rgba(5,8,13,.52);backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px)}
.ov.hide{display:none}
.modal{position:relative;width:340px;border-radius:24px;padding:28px 24px 22px;text-align:center;%%MCSS%%;animation:%%ENTER%% .6s cubic-bezier(.2,.9,.28,1.18) both;box-shadow:0 24px 70px rgba(0,0,0,.5)}
.x{position:absolute;top:10px;right:12px;width:30px;height:30px;border-radius:50%;border:0;background:rgba(255,255,255,.14);color:#fff;font-size:17px;cursor:pointer;line-height:30px;padding:0}
.btn{display:block;width:100%;border:0;border-radius:14px;padding:14px;font-size:16px;font-weight:700;cursor:pointer;margin-top:18px;background:var(--ac,#ffd479);color:#1a1405;transition:transform .15s}
.btn:active{transform:scale(.96)}
.btn.off{opacity:.35;pointer-events:none}
.ghost{background:none;border:0;color:var(--ds,#9aa3b2);font-size:13px;margin-top:12px;cursor:pointer;width:100%}
.rp{position:absolute;left:50%;bottom:22px;transform:translateX(-50%);z-index:40;border:1px solid rgba(255,255,255,.28);background:rgba(8,12,18,.72);color:#fff;border-radius:999px;padding:10px 24px;font-size:13px;cursor:pointer;backdrop-filter:blur(6px);white-space:nowrap}
h2.tt{font-size:21px;margin:12px 0 8px;letter-spacing:2px;color:var(--tc,#fff)}
p.ds{font-size:13.5px;line-height:1.75;color:var(--ds,#aeb6c2)}
@keyframes ePop{from{opacity:0;transform:scale(.62) translateY(46px)}to{opacity:1;transform:none}}
@keyframes eUp{from{opacity:0;transform:translateY(130px)}to{opacity:1;transform:none}}
@keyframes eFlip{from{opacity:0;transform:perspective(700px) rotateX(-72deg)}to{opacity:1;transform:none}}
@keyframes eLeft{from{opacity:0;transform:translateX(-170px) rotate(-7deg)}to{opacity:1;transform:none}}
@keyframes eBlur{from{opacity:0;transform:scale(1.16);filter:blur(16px)}to{opacity:1;transform:none;filter:blur(0)}}
@keyframes eDrop{0%{opacity:0;transform:translateY(-280px)}62%{opacity:1;transform:translateY(14px)}80%{transform:translateY(-7px)}100%{opacity:1;transform:none}}
%%EXTRA_CSS%%
</style></head><body>
<div class="phone">
%%MOCK%%
<div class="ov" id="ov"><div class="modal" id="md">
<button class="x" id="cx" aria-label="关闭">×</button>
%%MODAL_HTML%%
</div></div>
<button class="rp" id="rp">↻ 重新弹出</button>
</div>
<script>
var ov=document.getElementById('ov'),md=document.getElementById('md');
document.getElementById('cx').onclick=function(){ov.classList.add('hide')};
ov.addEventListener('click',function(e){if(e.target===ov)ov.classList.add('hide')});
document.getElementById('rp').onclick=function(){ov.classList.remove('hide');md.style.animation='none';void md.offsetWidth;md.style.animation=''};
%%EXTRA_JS%%
</script>
</body></html>"""

MOCK_SOCIAL = """<div class="mk"><div class="sb"><span>9:41</span><span>●●●</span></div>
<div class="mknav">动态</div><div class="mkbanner"></div>
<div class="mkrow"><div class="mkav"></div><div style="flex:1"><div class="mkln" style="width:40%"></div><div class="mkln" style="width:90%"></div></div></div>
<div class="mkrow"><div class="mkav"></div><div style="flex:1"><div class="mkln" style="width:55%"></div><div class="mkln" style="width:75%"></div></div></div>
<div class="mkrow"><div class="mkav"></div><div style="flex:1"><div class="mkln" style="width:35%"></div><div class="mkln" style="width:85%"></div></div></div></div>"""

MOCK_SHOP = """<div class="mk"><div class="sb"><span>9:41</span><span>●●●</span></div>
<div class="mksearch"></div><div class="mknav">商城</div>
<div class="mkgrid"><div class="mkcard"><div class="mkph"></div><div class="mkln" style="width:70%"></div><div class="mkln" style="width:40%"></div></div>
<div class="mkcard"><div class="mkph"></div><div class="mkln" style="width:60%"></div><div class="mkln" style="width:45%"></div></div>
<div class="mkcard"><div class="mkph"></div><div class="mkln" style="width:75%"></div><div class="mkln" style="width:35%"></div></div>
<div class="mkcard"><div class="mkph"></div><div class="mkln" style="width:55%"></div><div class="mkln" style="width:50%"></div></div></div></div>"""

MOCK_MUSIC = """<div class="mk"><div class="sb"><span>9:41</span><span>●●●</span></div>
<div class="mknav">在听</div><div class="mkalbum"></div>
<div class="mkln" style="width:55%"></div><div class="mkln" style="width:30%"></div>
<div class="mkbar"><i></i></div>
<div class="mkctl"><i></i><i></i><i></i></div></div>"""

MOCK_HOME = """<div class="mk"><div class="sb"><span>9:41</span><span>●●●</span></div>
<div class="mknav">首页</div><div class="mkbanner"></div>
<div class="mkrow"><div class="mkav" style="border-radius:12px"></div><div style="flex:1"><div class="mkln" style="width:60%"></div></div></div>
<div class="mkrow"><div class="mkav" style="border-radius:12px"></div><div style="flex:1"><div class="mkln" style="width:45%"></div></div></div>
<div class="mkrow"><div class="mkav" style="border-radius:12px"></div><div style="flex:1"><div class="mkln" style="width:70%"></div></div></div>
<div class="mkrow"><div class="mkav" style="border-radius:12px"></div><div style="flex:1"><div class="mkln" style="width:50%"></div></div></div></div>"""

ITEMS = []

# ============ w01 红包到 ============
ITEMS.append(dict(
 file="w01.html", title="红包到", pbg="linear-gradient(160deg,#1a0d12,#0d0a10)",
 mock=MOCK_HOME, enter="eDrop",
 mcss="background:linear-gradient(165deg,#d42b2b 0%,#a31515 60%,#7c0d0d 100%);--ac:#f6c453;--ds:#ffd7d7;--tc:#fff8ec;overflow:hidden",
 html="""<div class="env"><div class="flap"></div><div class="seal">福</div><div class="amt">¥<b>8.8</b></div></div>
<h2 class="tt">新人见面礼</h2><p class="ds">欢迎加入！这只红包专为你准备<br>无门槛 · 直接抵扣</p>
<button class="btn" id="go">开心收下</button><button class="ghost" id="no">下次再说</button>
<span class="coin c1"></span><span class="coin c2"></span><span class="coin c3"></span>""",
 css=""".env{width:150px;height:110px;margin:2px auto 0;background:linear-gradient(180deg,#e04242,#b01a1a);border-radius:0 0 18px 18px;position:relative;box-shadow:0 10px 26px rgba(0,0,0,.35)}
.flap{position:absolute;top:0;left:0;right:0;height:56px;background:linear-gradient(180deg,#c22525,#a31515);clip-path:polygon(0 0,100% 0,50% 100%);transform-origin:top;animation:flap 2.4s ease-in-out -0.6s infinite}
@keyframes flap{0%,100%{transform:rotateX(0)}50%{transform:rotateX(38deg)}}
.seal{position:absolute;top:34px;left:50%;transform:translateX(-50%);width:52px;height:52px;border-radius:50%;background:radial-gradient(circle at 35% 30%,#ffe9a8,#e8a93c 60%,#b97a1c);color:#8a1d00;font-size:24px;font-weight:900;line-height:52px;box-shadow:0 4px 10px rgba(0,0,0,.3)}
.amt{position:absolute;bottom:8px;left:0;right:0;color:#ffe9a8;font-size:15px}.amt b{font-size:26px}
.coin{display:block;position:absolute;width:22px;height:22px;border-radius:50%;background:radial-gradient(circle at 35% 30%,#ffe9a8,#e8a93c 65%,#9c6414);box-shadow:0 0 12px #f6c453;animation:rise 2.2s ease-in infinite}
.c1{left:14%;bottom:30px;animation-delay:-0.4s}.c2{left:48%;bottom:22px;animation-delay:-1.3s}.c3{left:80%;bottom:34px;animation-delay:-2s}
@keyframes rise{0%{transform:translateY(0);opacity:0}25%{opacity:1}100%{transform:translateY(-190px);opacity:0}}""",
 js="""document.getElementById('go').onclick=function(){this.textContent='已放入钱包 ✓';this.classList.add('off')};
document.getElementById('no').onclick=function(){ov.classList.add('hide')};"""))

# ============ w02 三步游 ============
ITEMS.append(dict(
 file="w02.html", title="三步游", pbg="linear-gradient(160deg,#0c1226,#0a0d18)",
 mock=MOCK_SOCIAL, enter="eLeft",
 mcss="background:linear-gradient(165deg,#1c2340,#12172c);--ac:#7ab8ff;--ds:#a9b8d8;--tc:#fff;border:1px solid rgba(122,184,255,.25);overflow:hidden",
 html="""<div class="tour"><div class="track" id="trk">
<div class="pg"><div class="pic p1"></div><h2 class="tt">发现新鲜事</h2><p class="ds">为你精选全网热榜<br>滑一下就有新世界</p></div>
<div class="pg"><div class="pic p2"></div><h2 class="tt">结识同好</h2><p class="ds">三千个兴趣小组<br>总有一个等你加入</p></div>
<div class="pg"><div class="pic p3"></div><h2 class="tt">记录生活</h2><p class="ds">一键发布图文视频<br>让每一刻都被看见</p></div>
</div></div>
<div class="dots" id="dots"><i class="on"></i><i></i><i></i></div>
<button class="btn" id="nx">下一步</button>""",
 css=""".tour{overflow:hidden;border-radius:14px}.track{display:flex;width:300%;transition:transform .45s cubic-bezier(.3,.8,.3,1)}
.pg{width:33.3333%;padding:6px 4px 0}
.pic{width:120px;height:120px;margin:0 auto 4px;border-radius:34px;position:relative;overflow:hidden}
.p1{background:conic-gradient(from 40deg,#ff9a6a,#ff5e8a,#b06aff,#5ec8ff,#5effb0,#ff9a6a);animation:spin 7s linear infinite}
.p2{background:linear-gradient(135deg,#5ec8ff,#2b6fe0)}
.p2::after{content:"";position:absolute;inset:34px;border-radius:50%;background:#fff;box-shadow:0 0 0 12px rgba(255,255,255,.25);animation:pulse 1.8s ease-in-out infinite}
.p3{background:#1a2138;border:2px dashed #7ab8ff}
.p3::after{content:"+";position:absolute;inset:0;color:#7ab8ff;font-size:64px;line-height:116px}
@keyframes spin{to{transform:rotate(360deg)}}
@keyframes pulse{0%,100%{transform:scale(1)}50%{transform:scale(1.18)}}
.dots{display:flex;justify-content:center;gap:8px;margin:14px 0 2px}
.dots i{display:block;width:8px;height:8px;border-radius:4px;background:rgba(255,255,255,.22);transition:all .3s}
.dots i.on{width:26px;background:#7ab8ff}""",
 js="""var i=0,trk=document.getElementById('trk'),dots=document.getElementById('dots').children,nx=document.getElementById('nx');
function go(k){i=k;trk.style.transform='translateX(-'+(k*33.3333)+'%)';
for(var j=0;j<3;j++)dots[j].className=j===k?'on':'';
nx.textContent=k===2?'开始体验':'下一步'}
nx.onclick=function(){if(i<2)go(i+1);else ov.classList.add('hide')};
var sx=0;trk.addEventListener('touchstart',function(e){sx=e.touches[0].clientX},{passive:true});
trk.addEventListener('touchend',function(e){var dx=e.changedTouches[0].clientX-sx;if(dx<-40&&i<2)go(i+1);if(dx>40&&i>0)go(i-1)});"""))

# ============ w03 开定位 ============
ITEMS.append(dict(
 file="w03.html", title="开定位", pbg="linear-gradient(160deg,#08131f,#0a0f16)",
 mock=MOCK_HOME, enter="ePop",
 mcss="background:linear-gradient(165deg,#0f2a22,#0b1d18);--ac:#3ddc84;--ds:#a8d4c2;--tc:#f2fff8;border:1px solid rgba(61,220,132,.25)",
 html="""<div class="radar"><div class="sweep"></div><div class="pin">◈</div></div>
<h2 class="tt">开启定位服务</h2><p class="ds">为你推荐附近的美食、优惠<br>与同城新鲜事</p>
<div class="prow"><span>📍 定位权限</span><span class="sw on" data-k="0"><i></i></span></div>
<div class="prow"><span>🔔 消息通知</span><span class="sw" data-k="1"><i></i></span></div>
<div class="prow"><span>📷 相机权限</span><span class="sw" data-k="2"><i></i></span></div>
<button class="btn" id="go">一键全部开启</button><button class="ghost" id="no">暂不需要</button>""",
 css=""".radar{width:130px;height:130px;margin:0 auto;border-radius:50%;position:relative;background:radial-gradient(circle,rgba(61,220,132,.16) 0 32%,transparent 33%),repeating-radial-gradient(circle,rgba(61,220,132,.35) 0 2px,transparent 2px 42px);border:1px solid rgba(61,220,132,.4)}
.sweep{position:absolute;inset:0;border-radius:50%;background:conic-gradient(from 0deg,rgba(61,220,132,.55),transparent 26%);animation:spin 2.6s linear infinite}
@keyframes spin{to{transform:rotate(360deg)}}
.pin{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);color:#3ddc84;font-size:26px;text-shadow:0 0 14px #3ddc84}
.prow{display:flex;justify-content:space-between;align-items:center;background:rgba(255,255,255,.05);border-radius:12px;padding:11px 14px;margin-top:10px;font-size:14px}
.sw{position:relative;display:inline-block;width:48px;height:28px;border-radius:14px;background:rgba(255,255,255,.16);cursor:pointer;transition:background .25s;flex-shrink:0}
.sw i{display:block;position:absolute;top:3px;left:3px;width:22px;height:22px;border-radius:50%;background:#fff;transition:left .25s}
.sw.on{background:#3ddc84}.sw.on i{left:23px}""",
 js="""var sws=document.querySelectorAll('.sw');
sws.forEach(function(s){s.onclick=function(){s.classList.toggle('on')}});
document.getElementById('go').onclick=function(){sws.forEach(function(s){s.classList.add('on')});this.textContent='已全部开启 ✓';this.classList.add('off')};
document.getElementById('no').onclick=function(){ov.classList.add('hide')};"""))

# ============ w04 曜石卡 ============
ITEMS.append(dict(
 file="w04.html", title="曜石卡", pbg="linear-gradient(160deg,#101014,#08080c)",
 mock=MOCK_MUSIC, enter="eFlip",
 mcss="background:linear-gradient(165deg,#17171f,#0c0c11);--ac:#e8b93c;--ds:#b9b3a4;--tc:#ffe9ad;border:1px solid rgba(232,185,60,.35)",
 html="""<div class="vip"><div class="shine"></div><div class="vtop">OBSIDIAN<span>VIP</span></div><div class="vno">8888 •••• •••• 0001</div><div class="vnm">黑曜会员 · 专属礼遇</div></div>
<h2 class="tt">开通黑曜会员</h2><p class="ds">免广告 · 无损音质 · 专属皮肤<br>首月仅需一杯咖啡钱</p>
<div class="plans"><div class="plan on" data-p="连续包月 ¥12/月"><b>连续包月</b><span>¥12/月</span></div>
<div class="plan" data-p="年卡 ¥118/年"><b>年卡</b><span>¥118/年</span></div></div>
<button class="btn" id="go">立即开通</button><button class="ghost">恢复购买</button>""",
 css=""".vip{border-radius:16px;padding:18px 16px;text-align:left;background:linear-gradient(120deg,#23232e,#101016 60%,#1d1a12);border:1px solid rgba(232,185,60,.5);position:relative;overflow:hidden;margin-bottom:4px}
.shine{position:absolute;top:0;bottom:0;width:70px;background:linear-gradient(100deg,transparent,rgba(255,236,180,.35),transparent);transform:skewX(-18deg);animation:sh 2.8s ease-in-out -1s infinite;left:-90px}
@keyframes sh{0%{left:-90px}55%,100%{left:360px}}
.vtop{font-size:15px;letter-spacing:4px;color:#e8b93c;font-weight:800}.vtop span{border:1px solid #e8b93c;border-radius:6px;font-size:10px;padding:1px 6px;margin-left:8px;letter-spacing:1px}
.vno{font-size:14px;letter-spacing:3px;color:#8f887a;margin:14px 0 6px}
.vnm{font-size:12px;color:#e8b93c}
.plans{display:flex;gap:10px;margin-top:14px}
.plan{flex:1;border:1px solid rgba(255,255,255,.16);border-radius:12px;padding:12px 6px;cursor:pointer;transition:all .25s}
.plan b{display:block;font-size:14px;margin-bottom:4px}.plan span{font-size:12px;color:var(--ds)}
.plan.on{border-color:#e8b93c;background:rgba(232,185,60,.1);box-shadow:0 0 16px rgba(232,185,60,.25)}""",
 js="""var ps=document.querySelectorAll('.plan');
ps.forEach(function(p){p.onclick=function(){ps.forEach(function(x){x.classList.remove('on')});p.classList.add('on')}});
document.getElementById('go').onclick=function(){var p=document.querySelector('.plan.on');this.textContent='已开通 · '+p.dataset.p;this.classList.add('off')};"""))

# ============ w05 七日签 ============
ITEMS.append(dict(
 file="w05.html", title="七日签", pbg="linear-gradient(160deg,#141021,#0b0a12)",
 mock=MOCK_SOCIAL, enter="eUp",
 mcss="background:linear-gradient(165deg,#241d3d,#161226);--ac:#b06aff;--ds:#c3b8e8;--tc:#fff;border:1px solid rgba(176,106,255,.3)",
 html="""<div class="cal"><div class="day done">一<i>✓</i></div><div class="day done">二<i>✓</i></div><div class="day today">三<i>签</i></div><div class="day">四</div><div class="day">五</div><div class="day">六</div><div class="day">日</div></div>
<h2 class="tt">每日签到</h2><p class="ds" id="tx">已连续签到 <b>2</b> 天 · 今日签到<br>可领取 <b>10</b> 积分</p>
<div class="pbar"><i id="fill"></i></div>
<button class="btn" id="go">立即签到</button>""",
 css=""".cal{display:grid;grid-template-columns:repeat(7,1fr);gap:6px;margin-bottom:6px}
.day{position:relative;aspect-ratio:.86;border-radius:10px;background:rgba(255,255,255,.06);font-size:12px;color:var(--ds);display:flex;align-items:center;justify-content:center}
.day i{position:absolute;top:3px;right:4px;font-style:normal;font-size:9px;color:#3ddc84}
.day.done{background:rgba(176,106,255,.16);color:#d9c8ff}
.day.today{background:linear-gradient(135deg,#b06aff,#7a3fe0);color:#fff;font-weight:800;animation:tpulse 1.6s ease-in-out infinite}
.day.today i{color:#fff}
@keyframes tpulse{0%,100%{box-shadow:0 0 0 0 rgba(176,106,255,.5)}50%{box-shadow:0 0 0 9px rgba(176,106,255,0)}}
.pbar{height:8px;border-radius:4px;background:rgba(255,255,255,.1);margin:14px 0 2px;overflow:hidden}
.pbar i{display:block;height:100%;width:28%;border-radius:4px;background:linear-gradient(90deg,#b06aff,#5ec8ff);transition:width .6s}""",
 js="""document.getElementById('go').onclick=function(){
var t=document.querySelector('.day.today');t.classList.remove('today');t.classList.add('done');t.querySelector('i').textContent='✓';
document.getElementById('fill').style.width='43%';
document.getElementById('tx').innerHTML='已连续签到 <b>3</b> 天 · +10 积分已到账<br>明天继续，奖励翻倍';
this.textContent='签到成功 ✓';this.classList.add('off')};"""))

# ============ w06 邀友赏 ============
ITEMS.append(dict(
 file="w06.html", title="邀友赏", pbg="linear-gradient(160deg,#0e1a26,#090e14)",
 mock=MOCK_SOCIAL, enter="eBlur",
 mcss="background:linear-gradient(165deg,#123043,#0c1e2c);--ac:#5ec8ff;--ds:#a9c8dc;--tc:#f0f9ff;border:1px solid rgba(94,200,255,.3)",
 html="""<div class="duo"><div class="ava a1">你</div><div class="ava a2">友</div><div class="lnk"></div></div>
<h2 class="tt">邀请好友 · 各得好礼</h2><p class="ds">好友接受邀请，你们各得 <b>¥5</b><br>无上限 · 上不封顶</p>
<div class="codebox"><span id="code">FRIEND-8X2K</span><button id="cp">复制</button></div>
<button class="btn" id="go">去邀请好友</button><button class="ghost" id="no">稍后再说</button>""",
 css=""".duo{position:relative;height:96px;margin-bottom:2px}
.ava{position:absolute;top:8px;width:72px;height:72px;border-radius:50%;font-size:22px;font-weight:800;line-height:72px;color:#fff}
.a1{left:88px;background:linear-gradient(135deg,#5ec8ff,#2b6fe0);z-index:2;animation:bob 2.4s ease-in-out infinite}
.a2{right:88px;background:linear-gradient(135deg,#ff9a6a,#e05e2b);animation:bob 2.4s ease-in-out -1.2s infinite}
@keyframes bob{0%,100%{transform:translateY(0)}50%{transform:translateY(-8px)}}
.lnk{position:absolute;top:40px;left:150px;right:150px;border-top:3px dashed rgba(94,200,255,.6)}
.codebox{display:flex;align-items:center;justify-content:space-between;background:rgba(255,255,255,.06);border:1px dashed rgba(94,200,255,.5);border-radius:12px;padding:12px 14px;margin-top:14px;font-size:15px;letter-spacing:2px}
.codebox button{border:0;border-radius:8px;background:var(--ac);color:#06283a;font-weight:700;padding:8px 16px;font-size:13px;cursor:pointer}""",
 js="""document.getElementById('cp').onclick=function(){this.textContent='已复制 ✓';var c=this;setTimeout(function(){c.textContent='复制'},1400)};
document.getElementById('go').onclick=function(){ov.classList.add('hide')};
document.getElementById('no').onclick=function(){ov.classList.add('hide')};"""))


# ============ w07 验真身 ============
ITEMS.append(dict(
 file="w07.html", title="验真身", pbg="linear-gradient(160deg,#101826,#0a0d14)",
 mock=MOCK_HOME, enter="eUp",
 mcss="background:linear-gradient(165deg,#1a2338,#111827);--ac:#7ab8ff;--ds:#a9b8d8;--tc:#fff;border:1px solid rgba(122,184,255,.25)",
 html="""<div class="idc"><div class="face">◉</div><div class="scan"></div></div>
<h2 class="tt">实名认证</h2><p class="ds">完成认证，解锁提现、发布<br>与更多专属权益</p>
<div class="steps">
<div class="step done"><i>✓</i><div><b>绑定手机</b><span>已完成</span></div></div>
<div class="step now"><i>2</i><div><b>身份证验证</b><span>进行中</span></div></div>
<div class="step"><i>3</i><div><b>人脸识别</b><span>待进行</span></div></div>
</div>
<button class="btn" id="go">开始验证</button><button class="ghost" id="no">以后再说</button>""",
 css=""".idc{width:110px;height:110px;margin:0 auto;border-radius:28px;background:linear-gradient(135deg,#2b3a5e,#182238);position:relative;overflow:hidden}
.face{font-size:52px;line-height:110px;color:#7ab8ff}
.scan{position:absolute;left:8px;right:8px;height:3px;border-radius:2px;background:#7ab8ff;box-shadow:0 0 12px #7ab8ff;animation:scan 2.2s ease-in-out infinite}
@keyframes scan{0%,100%{top:12px}50%{top:94px}}
.steps{margin-top:14px;text-align:left}
.step{display:flex;gap:12px;align-items:center;padding:10px 4px;position:relative}
.step::before{content:"";position:absolute;left:17px;top:44px;bottom:-8px;width:2px;background:rgba(255,255,255,.12)}
.step:last-child::before{display:none}
.step i{display:block;width:36px;height:36px;border-radius:50%;background:rgba(255,255,255,.1);color:#8b94a3;font-style:normal;font-weight:800;line-height:36px;text-align:center;flex-shrink:0;font-size:15px}
.step b{display:block;font-size:14px}.step span{font-size:12px;color:var(--ds)}
.step.done i{background:#3ddc84;color:#062a18}
.step.now i{background:#7ab8ff;color:#0a1c38;animation:tpulse2 1.6s ease-in-out infinite}
@keyframes tpulse2{0%,100%{box-shadow:0 0 0 0 rgba(122,184,255,.5)}50%{box-shadow:0 0 0 8px rgba(122,184,255,0)}}""",
 js="""document.getElementById('go').onclick=function(){this.textContent='验证中…';var b=this;setTimeout(function(){b.textContent='验证通过 ✓';b.classList.add('off')},1200)};
document.getElementById('no').onclick=function(){ov.classList.add('hide')};"""))

# ============ w08 新手令 ============
ITEMS.append(dict(
 file="w08.html", title="新手令", pbg="linear-gradient(160deg,#1c1408,#100c06)",
 mock=MOCK_SHOP, enter="ePop",
 mcss="background:linear-gradient(165deg,#2e2314,#1c150c);--ac:#f6c453;--ds:#d8c8a4;--tc:#fff4dd;border:1px solid rgba(246,196,83,.3)",
 html="""<div class="flag">令</div>
<h2 class="tt">新手任务令</h2><p class="ds" id="tx">完成 <b>3</b> 个任务，领取 <b>¥20</b> 大礼包<br>已完成 <b id="n">0</b>/3</p>
<div class="tasks">
<div class="task" data-t="完善头像资料"><i></i><span>完善头像资料</span><em>+¥5</em></div>
<div class="task" data-t="首次发布动态"><i></i><span>首次发布动态</span><em>+¥5</em></div>
<div class="task" data-t="关注 3 位好友"><i></i><span>关注 3 位好友</span><em>+¥10</em></div>
</div>
<div class="pbar"><i id="fill"></i></div>
<button class="btn off" id="go">领取 ¥20 大礼包</button>""",
 css=""".flag{width:84px;height:84px;margin:0 auto;border-radius:22px;background:linear-gradient(135deg,#f6c453,#d18a1f);color:#4a2c00;font-size:44px;font-weight:900;line-height:84px;box-shadow:0 8px 24px rgba(246,196,83,.35);animation:wob 2.6s ease-in-out infinite}
@keyframes wob{0%,100%{transform:rotate(-4deg)}50%{transform:rotate(4deg)}}
.tasks{margin-top:12px;text-align:left}
.task{display:flex;align-items:center;gap:12px;background:rgba(255,255,255,.05);border-radius:12px;padding:12px 14px;margin-top:8px;cursor:pointer;font-size:14px;transition:all .25s}
.task i{display:block;width:24px;height:24px;border-radius:50%;border:2px solid rgba(255,255,255,.3);flex-shrink:0;transition:all .25s;position:relative}
.task.done i{background:#f6c453;border-color:#f6c453}
.task.done i::after{content:"✓";position:absolute;inset:0;color:#4a2c00;font-size:14px;font-weight:900;line-height:20px;text-align:center;font-style:normal}
.task.done{opacity:.65}.task.done span{text-decoration:line-through}
.task em{margin-left:auto;font-style:normal;color:#f6c453;font-size:12px;font-weight:700}
.pbar{height:8px;border-radius:4px;background:rgba(255,255,255,.1);margin:14px 0 2px;overflow:hidden}
.pbar i{display:block;height:100%;width:0;border-radius:4px;background:linear-gradient(90deg,#f6c453,#ff9a3c);transition:width .5s}""",
 js="""var n=0,go=document.getElementById('go');
document.querySelectorAll('.task').forEach(function(t){t.onclick=function(){
t.classList.toggle('done');n=document.querySelectorAll('.task.done').length;
document.getElementById('n').textContent=n;document.getElementById('fill').style.width=(n/3*100)+'%';
if(n===3){go.classList.remove('off')}}});
go.onclick=function(){this.textContent='¥20 已到账 ✓';this.classList.add('off')};"""))

# ============ w09 券在手 ============
ITEMS.append(dict(
 file="w09.html", title="券在手", pbg="linear-gradient(160deg,#1a1020,#0e0a12)",
 mock=MOCK_SHOP, enter="eLeft",
 mcss="background:linear-gradient(165deg,#2c1c34,#1a1220);--ac:#ff6a9a;--ds:#d8b8c8;--tc:#fff;border:1px solid rgba(255,106,154,.3)",
 html="""<div class="ticket"><div class="stub"><b>¥50</b><span>满 299 可用</span></div><div class="info"><b>新人专享券</b><span>全场通用 · 7 天有效</span><span>不可叠加使用</span></div></div>
<h2 class="tt">见面先领券</h2><p class="ds">这张券只发给今天注册的你<br>过期可不补发哦</p>
<button class="btn" id="go">立即领取</button><button class="ghost" id="no">不需要</button>""",
 css=""".ticket{display:flex;margin:4px 0 2px;filter:drop-shadow(0 8px 20px rgba(255,106,154,.25))}
.stub{width:118px;background:linear-gradient(135deg,#ff6a9a,#d63a6e);border-radius:14px 0 0 14px;padding:20px 8px;color:#fff;position:relative}
.stub b{display:block;font-size:32px}.stub span{font-size:11px;opacity:.85}
.stub::after{content:"";position:absolute;top:-8px;bottom:-8px;right:-9px;width:18px;background:radial-gradient(circle at 9px 9px,transparent 7px,rgba(0,0,0,0) 7px)}
.info{flex:1;background:rgba(255,255,255,.07);border:1px solid rgba(255,106,154,.35);border-left:0;border-radius:0 14px 14px 0;padding:16px 12px;text-align:left;position:relative}
.info::before{content:"";position:absolute;left:-1px;top:12px;bottom:12px;border-left:2px dashed rgba(255,106,154,.6)}
.info b{display:block;font-size:15px;margin-bottom:6px;color:#ffb3c8}.info span{display:block;font-size:11.5px;color:var(--ds);line-height:1.7}
.ticket{animation:tick 2.8s ease-in-out infinite}
@keyframes tick{0%,100%{transform:rotate(-1.4deg)}50%{transform:rotate(1.4deg)}}""",
 js="""document.getElementById('go').onclick=function(){this.textContent='已放入卡包 ✓';this.classList.add('off')};
document.getElementById('no').onclick=function(){ov.classList.add('hide')};"""))

# ============ w10 声入耳 ============
ITEMS.append(dict(
 file="w10.html", title="声入耳", pbg="linear-gradient(160deg,#0d1626,#080c14)",
 mock=MOCK_MUSIC, enter="eBlur",
 mcss="background:linear-gradient(165deg,#152238,#0d1626);--ac:#5ec8ff;--ds:#a9c4dc;--tc:#f0f8ff;border:1px solid rgba(94,200,255,.3)",
 html="""<div class="eq"><i></i><i></i><i></i><i></i><i></i><i></i><i></i></div>
<div class="mic">🎙</div>
<h2 class="tt">语音助手上线</h2><p class="ds">长按说话，它帮你搜歌、定闹钟<br>查天气，动口不动手</p>
<button class="btn" id="go">试试说句话</button><button class="ghost" id="no">跳过</button>""",
 css=""".eq{display:flex;align-items:flex-end;justify-content:center;gap:7px;height:64px;margin-bottom:8px}
.eq i{display:block;width:9px;border-radius:5px;background:linear-gradient(180deg,#5ec8ff,#2b6fe0);animation:eq 1.1s ease-in-out infinite;transform-origin:bottom}
.eq i:nth-child(1){height:38px;animation-delay:-0.1s}.eq i:nth-child(2){height:56px;animation-delay:-0.5s}
.eq i:nth-child(3){height:30px;animation-delay:-0.8s}.eq i:nth-child(4){height:62px;animation-delay:-0.3s}
.eq i:nth-child(5){height:42px;animation-delay:-0.9s}.eq i:nth-child(6){height:54px;animation-delay:-0.6s}
.eq i:nth-child(7){height:34px;animation-delay:-0.2s}
@keyframes eq{0%,100%{transform:scaleY(.35)}50%{transform:scaleY(1)}}
.mic{width:76px;height:76px;margin:2px auto;border-radius:50%;background:radial-gradient(circle at 35% 30%,#8fdcff,#2b6fe0);font-size:34px;line-height:76px;box-shadow:0 0 0 0 rgba(94,200,255,.45);animation:mring 1.8s ease-out infinite}
@keyframes mring{0%{box-shadow:0 0 0 0 rgba(94,200,255,.45)}100%{box-shadow:0 0 0 22px rgba(94,200,255,0)}}""",
 js="""document.getElementById('go').onclick=function(){this.textContent='我在听…请说话';var b=this;setTimeout(function(){b.textContent='收到 ✓ 为你打开语音助手';b.classList.add('off')},1400)};
document.getElementById('no').onclick=function(){ov.classList.add('hide')};"""))

# ============ w11 夜未央 ============
ITEMS.append(dict(
 file="w11.html", title="夜未央", pbg="linear-gradient(160deg,#0a0e18,#060810)",
 mock=MOCK_HOME, enter="eFlip",
 mcss="background:linear-gradient(165deg,#1b2340,#10142a);--ac:#ffd479;--ds:#a9b4d8;--tc:#fff;border:1px solid rgba(255,212,121,.3);transition:background .5s",
 html="""<div class="orb"><div class="core"></div><div class="rays"><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i></div></div>
<h2 class="tt" id="t">试试深色模式</h2><p class="ds">夜晚不刺眼，省电又护眼<br>一键切换，随心而变</p>
<div class="prow"><span>🌙 深色模式</span><span class="sw" id="sw"><i></i></span></div>
<button class="btn" id="go">开启深色模式</button>""",
 css=""".orb{width:104px;height:104px;margin:0 auto;position:relative}
.core{position:absolute;inset:14px;border-radius:50%;background:radial-gradient(circle at 35% 30%,#ffe9a8,#f6b93c 65%,#d18a1f);box-shadow:0 0 34px rgba(246,185,60,.55);transition:all .5s}
.rays i{display:block;position:absolute;left:50%;top:50%;width:4px;height:14px;border-radius:2px;background:#f6b93c;transform-origin:2px -44px;opacity:.85}
.rays i:nth-child(1){transform:rotate(0deg) translateY(-44px)}.rays i:nth-child(2){transform:rotate(45deg) translateY(-44px)}
.rays i:nth-child(3){transform:rotate(90deg) translateY(-44px)}.rays i:nth-child(4){transform:rotate(135deg) translateY(-44px)}
.rays i:nth-child(5){transform:rotate(180deg) translateY(-44px)}.rays i:nth-child(6){transform:rotate(225deg) translateY(-44px)}
.rays i:nth-child(7){transform:rotate(270deg) translateY(-44px)}.rays i:nth-child(8){transform:rotate(315deg) translateY(-44px)}
.orb{animation:slowspin 14s linear infinite}
@keyframes slowspin{to{transform:rotate(360deg)}}
.modal.night .core{background:radial-gradient(circle at 65% 35%,#dfe8ff,#8fa3cc 65%,#5a6c96);box-shadow:0 0 30px rgba(160,190,255,.5)}
.modal.night .rays{opacity:0}.modal.night{--ac:#8fa3cc}
.prow{display:flex;justify-content:space-between;align-items:center;background:rgba(255,255,255,.05);border-radius:12px;padding:11px 14px;margin-top:14px;font-size:14px}
.sw{position:relative;display:inline-block;width:48px;height:28px;border-radius:14px;background:rgba(255,255,255,.16);cursor:pointer;transition:background .25s;flex-shrink:0}
.sw i{display:block;position:absolute;top:3px;left:3px;width:22px;height:22px;border-radius:50%;background:#fff;transition:left .25s}
.sw.on{background:#ffd479}.sw.on i{left:23px}""",
 js="""var sw=document.getElementById('sw'),md=document.getElementById('md');
function setNight(on){sw.classList.toggle('on',on);md.classList.toggle('night',on);
document.getElementById('t').textContent=on?'深色模式已开启':'试试深色模式'}
sw.onclick=function(){setNight(!sw.classList.contains('on'))};
document.getElementById('go').onclick=function(){setNight(true);this.textContent='已开启 ✓';this.classList.add('off')};"""))

# ============ w12 云归来 ============
ITEMS.append(dict(
 file="w12.html", title="云归来", pbg="linear-gradient(160deg,#0e1c2a,#090f16)",
 mock=MOCK_SOCIAL, enter="eDrop",
 mcss="background:linear-gradient(165deg,#14293d,#0d1a29);--ac:#5ec8ff;--ds:#a9c8dc;--tc:#f0f9ff;border:1px solid rgba(94,200,255,.3)",
 html="""<div class="ringwrap"><svg viewBox="0 0 120 120" class="ring"><circle cx="60" cy="60" r="52" class="bg"/><circle cx="60" cy="60" r="52" class="fg" id="fg"/></svg><div class="cloud">☁</div><div class="pct" id="pct">0%</div></div>
<h2 class="tt">云端同步</h2><p class="ds">聊天记录、收藏与设置<br>多设备实时同步，永不丢失</p>
<button class="btn" id="go">开始同步</button><button class="ghost" id="no">稍后手动同步</button>""",
 css=""".ringwrap{width:140px;height:140px;margin:0 auto;position:relative}
.ring{width:140px;height:140px;transform:rotate(-90deg)}
.ring circle{fill:none;stroke-width:10;stroke-linecap:round}
.ring .bg{stroke:rgba(255,255,255,.1)}
.ring .fg{stroke:url(#g);stroke:#5ec8ff;stroke-dasharray:326.7;stroke-dashoffset:326.7;transition:stroke-dashoffset 1.2s ease}
.cloud{position:absolute;top:34px;left:0;right:0;font-size:40px;animation:float 2.6s ease-in-out infinite}
@keyframes float{0%,100%{transform:translateY(0)}50%{transform:translateY(-7px)}}
.pct{position:absolute;bottom:26px;left:0;right:0;font-size:17px;font-weight:800;color:#5ec8ff}""",
 js="""var p=0,timer=null;
document.getElementById('go').onclick=function(){var b=this;b.classList.add('off');b.textContent='同步中…';
timer=setInterval(function(){p+=8;if(p>=100){p=100;clearInterval(timer);b.textContent='同步完成 ✓'}
document.getElementById('fg').style.strokeDashoffset=326.7*(1-p/100);
document.getElementById('pct').textContent=p+'%'},160)};
document.getElementById('no').onclick=function(){ov.classList.add('hide')};"""))
