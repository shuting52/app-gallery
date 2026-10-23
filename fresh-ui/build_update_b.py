#!/usr/bin/env python3
"""生成 fresh-ui/update B 组 u19-u36"""
import os

OUT = os.path.expanduser("~/workspace/fresh-ui/update")
os.makedirs(OUT, exist_ok=True)

BASE_CSS = """
*{margin:0;padding:0;box-sizing:border-box}
html,body{height:100%}
body{background:#0b0d12;display:flex;align-items:center;justify-content:center;min-height:100vh;
font-family:-apple-system,"PingFang SC","Hiragino Sans GB","Microsoft YaHei",sans-serif}
.phone{width:430px;height:900px;position:relative;overflow:hidden;background:#eef0f5;flex-shrink:0}
.mock{position:absolute;inset:0}
.status{height:34px;background:#fff}
.apphead{display:flex;align-items:center;gap:10px;padding:14px 18px;background:#fff}
.logo{width:38px;height:38px;border-radius:12px;background:linear-gradient(135deg,#7ab8ff,#b48cff)}
.apptitle{font-size:17px;font-weight:700;color:#222}
.sk{margin:14px 18px;background:#fff;border-radius:14px;padding:14px;box-shadow:0 2px 10px rgba(0,0,0,.05)}
.sk i{display:block;height:12px;border-radius:6px;background:#e6e9f0;margin-bottom:10px}
.sk i:last-child{margin-bottom:0}
.sk i.w60{width:60%}.sk i.w80{width:80%}
.tabbar{position:absolute;bottom:0;left:0;right:0;height:70px;background:#fff;display:flex;border-top:1px solid #eee}
.tabbar i{flex:1;display:block;position:relative}
.tabbar i::after{content:"";position:absolute;left:50%;top:16px;width:26px;height:26px;margin-left:-13px;border-radius:9px;background:#e6e9f0}
.tabbar i.on::after{background:linear-gradient(135deg,#7ab8ff,#b48cff)}
.mask{position:absolute;inset:0;background:rgba(10,14,24,.55);backdrop-filter:blur(3px);
animation:fadeIn .5s ease both;z-index:5}
@keyframes fadeIn{from{opacity:0}to{opacity:1}}
.modal{position:absolute;left:35px;right:35px;top:150px;z-index:6;border-radius:22px;padding:22px 20px 20px;
box-shadow:0 24px 60px rgba(0,0,0,.35);animation:popIn .65s cubic-bezier(.2,.9,.3,1.25) both}
@keyframes popIn{from{opacity:0;transform:scale(.7) translateY(40px)}to{opacity:1;transform:scale(1) translateY(0)}}
.art{height:150px;position:relative;overflow:hidden;border-radius:14px;margin-bottom:14px}
.art i{display:block}
.ver{display:inline-block;font-size:11px;padding:4px 10px;border-radius:20px;background:rgba(127,140,160,.15);color:#8a94a6;margin-bottom:8px}
.ver b{color:#ff6b5e}
.modal h2{font-size:21px;margin-bottom:10px;letter-spacing:1px}
.log{list-style:none;margin-bottom:14px}
.log li{font-size:13px;line-height:1.5;padding:6px 0 6px 22px;position:relative;color:#5a6478}
.log li::before{content:"";position:absolute;left:4px;top:12px;width:8px;height:8px;border-radius:50%;background:#7ab8ff}
.prog{height:8px;border-radius:4px;background:#e8ebf2;overflow:hidden;margin-bottom:14px}
.prog i{display:block;height:100%;width:0;border-radius:4px;background:linear-gradient(90deg,#7ab8ff,#b48cff);transition:width .25s}
.btns{display:flex;gap:10px}
.btns button{flex:1;height:46px;border:none;border-radius:14px;font-size:15px;font-weight:700;cursor:pointer;font-family:inherit}
.later{background:#eef0f5;color:#5a6478}
.go{background:linear-gradient(135deg,#ff9d5c,#ff6b5e);color:#fff;box-shadow:0 8px 20px rgba(255,107,94,.4)}
.go:disabled{opacity:.7;cursor:default}
.reopen{position:absolute;bottom:110px;left:50%;transform:translateX(-50%);z-index:7;display:none;
border:none;border-radius:30px;padding:12px 26px;font-size:14px;font-weight:700;cursor:pointer;
background:#fff;color:#333;box-shadow:0 10px 30px rgba(0,0,0,.25);font-family:inherit}
.phone.gone .modal,.phone.gone .mask{opacity:0;pointer-events:none;transition:opacity .35s}
.phone.gone .reopen{display:block;animation:popIn .4s both}
@keyframes spin{to{transform:rotate(360deg)}}
@keyframes spinRev{to{transform:rotate(-360deg)}}
"""

DARK = """
.modal{background:#151b29;color:#eef1f8}
.modal .log li{color:#9aa6bd}
.modal .later{background:#232c42;color:#aeb8cf}
.modal .prog{background:#232c42}
.modal .ver{background:rgba(255,255,255,.08);color:#8fa0bf}
"""
LIGHT = """
.modal{background:#ffffff;color:#222}
"""

SHARED_JS = """
const ph=document.querySelector('.phone'),go=document.querySelector('.go'),
later=document.querySelector('.later'),reopen=document.querySelector('.reopen'),
bar=document.querySelector('.prog i');
go.onclick=()=>{if(go.dataset.done){hide();return;}
go.disabled=true;go.textContent='下载中…';let p=0;
const t=setInterval(()=>{p+=Math.random()*13+7;
if(p>=100){p=100;clearInterval(t);bar.style.width='100%';
go.disabled=false;go.textContent='进入应用';go.dataset.done='1';}
else{bar.style.width=p+'%';}},200);};
later.onclick=hide;reopen.onclick=()=>{ph.classList.remove('gone');};
function hide(){ph.classList.add('gone');}
"""

CONCEPTS = [
# u19 卷轴新篇
{"file":"u19.html","title":"卷轴新篇","card":LIGHT,"accent":"#8a6d3b",
 "logs":["全新水墨主题，笔墨更温润","长图导出支持卷轴式排版","修复 12 处细节体验问题"],
 "art_html":'<div class="scroll"><div class="rod"></div><div class="paper"><span>迎新版</span></div><div class="rod"></div></div>',
 "art_css":""".art{background:linear-gradient(#2a2118,#171008)}
.scroll{display:flex;align-items:center;justify-content:center;height:150px}
.rod{width:11px;height:128px;border-radius:6px;background:linear-gradient(90deg,#5e4023,#8a6238,#5e4023);flex-shrink:0}
.paper{width:150px;height:104px;margin:0 -2px;background:linear-gradient(#f8f1dc,#e7d9b8);
transform-origin:left center;animation:unroll 1.1s cubic-bezier(.3,.8,.3,1) both;
box-shadow:inset 0 0 24px rgba(138,109,59,.25);display:flex;align-items:center;justify-content:center}
@keyframes unroll{from{transform:scaleX(0)}to{transform:scaleX(1)}}
.paper span{writing-mode:vertical-rl;font-size:26px;font-weight:800;color:#3a3226;letter-spacing:6px;
animation:fadeIn 1s .5s both}"""},

# u20 齿轮咬合
{"file":"u20.html","title":"齿轮咬合","card":DARK,"accent":"#b08d4f",
 "logs":["底层引擎重构，运转更顺滑","新增机械质感动效主题","启动速度提升 40%"],
 "art_html":'<div class="gears"><div class="gear g1"></div><div class="gear g2"></div><div class="gear g3"></div></div>',
 "art_css":""".art{background:linear-gradient(#241d12,#100c07)}
.gears{position:relative;height:150px}
.gear{position:absolute;border-radius:50%;
background:repeating-conic-gradient(#c49a55 0 14deg,#7d5f31 14deg 28deg);
animation:spin 7s linear infinite}
.gear::after{content:"";position:absolute;inset:26%;border-radius:50%;background:#241d12;
border:4px solid #c49a55}
.g1{width:96px;height:96px;left:52px;top:27px}
.g2{width:64px;height:64px;left:150px;top:20px;animation:spinRev 5s linear infinite}
.g2::after{inset:24%}
.g3{width:48px;height:48px;left:170px;top:88px;animation-duration:4s}
.g3::after{inset:22%}"""},

# u21 深海下潜
{"file":"u21.html","title":"深海下潜","card":DARK,"accent":"#5cc8ff",
 "logs":["深海模式：更沉浸的夜间阅读","新增潜水艇主题小组件","内存占用降低 30%"],
 "art_html":'<div class="sea"><i class="ray r1"></i><i class="ray r2"></i><i class="ray r3"></i><div class="sub"></div><i class="bub b1"></i><i class="bub b2"></i><i class="bub b3"></i><i class="bub b4"></i></div>',
 "art_css":""".sea{position:absolute;inset:0;background:linear-gradient(#0a3d66,#020e1c);overflow:hidden}
.ray{position:absolute;top:-30px;width:36px;height:220px;
background:linear-gradient(rgba(140,210,255,.28),transparent);transform:skewX(-16deg);
animation:sway 6s ease-in-out infinite alternate}
.r1{left:60px}.r2{left:150px;animation-delay:-2s}.r3{left:250px;animation-delay:-4s}
@keyframes sway{from{transform:skewX(-16deg) translateX(0)}to{transform:skewX(-16deg) translateX(26px)}}
.sub{position:absolute;left:50%;top:24px;width:52px;height:24px;margin-left:-26px;border-radius:13px;
background:linear-gradient(#ffe29a,#ffb35c);box-shadow:0 0 18px rgba(255,200,110,.7);
animation:dive 6s ease-in-out infinite alternate}
.sub::after{content:"";position:absolute;right:8px;top:7px;width:10px;height:10px;border-radius:50%;background:#0a3d66}
@keyframes dive{from{transform:translateY(0)}to{transform:translateY(72px)}}
.bub{position:absolute;bottom:-16px;border-radius:50%;border:2px solid rgba(160,220,255,.6);
animation:rise 4.5s linear infinite}
.b1{left:40px;width:12px;height:12px;animation-delay:-1s}
.b2{left:120px;width:8px;height:8px;animation-delay:-3s}
.b3{left:230px;width:14px;height:14px;animation-delay:-2s}
.b4{left:320px;width:9px;height:9px;animation-delay:-4s}
@keyframes rise{to{transform:translateY(-190px)}}"""},

# u22 书页翻飞
{"file":"u22.html","title":"书页翻飞","card":LIGHT,"accent":"#7a6ff0",
 "logs":["阅读器新增翻页动效","书架支持无限层叠","夜间模式更护眼"],
 "art_html":'<div class="book"><div class="page p1"></div><div class="page p2"></div><div class="spine"></div></div>',
 "art_css":""".art{background:linear-gradient(#efe9fb,#dcd2f5)}
.book{position:relative;width:150px;height:120px;margin:15px auto}
.spine{position:absolute;left:50%;top:0;width:8px;height:120px;margin-left:-4px;border-radius:4px;background:#5a4fc4}
.page{position:absolute;left:50%;top:4px;width:67px;height:112px;background:#fff;border-radius:0 8px 8px 0;
transform-origin:left center;box-shadow:2px 2px 8px rgba(90,79,196,.2);animation:flip 3.2s ease-in-out infinite}
.page::after{content:"";position:absolute;inset:10px 8px;border-left:2px solid #e3def7}
.p1{animation-delay:0s}.p2{animation-delay:-1.6s;background:#f6f3ff}
@keyframes flip{0%{transform:rotateY(0)}45%,55%{transform:rotateY(-178deg)}100%{transform:rotateY(-178deg)}}"""},

# u23 星座连线
{"file":"u23.html","title":"星座连线","card":DARK,"accent":"#b48cff",
 "logs":["星空导航页全新上线","新增 12 款星座主题","手势操作全面优化"],
 "art_html":'''<svg class="sky" viewBox="0 0 330 150">
<line x1="40" y1="105" x2="95" y2="52"/><line x1="95" y1="52" x2="160" y2="72"/>
<line x1="160" y1="72" x2="225" y2="38"/><line x1="225" y1="38" x2="290" y2="100"/>
<circle class="st" cx="40" cy="105" r="5"/><circle class="st" cx="95" cy="52" r="6"/>
<circle class="st" cx="160" cy="72" r="5"/><circle class="st" cx="225" cy="38" r="7"/>
<circle class="st" cx="290" cy="100" r="5"/></svg>''',
 "art_css":""".art{background:linear-gradient(#0d0b26,#1c1445)}
.sky{width:100%;height:150px}
.sky line{stroke:#b48cff;stroke-width:1.6;stroke-dasharray:400;stroke-dashoffset:400;
animation:draw 1.6s ease forwards}
.sky line:nth-of-type(2){animation-delay:.25s}.sky line:nth-of-type(3){animation-delay:.5s}
.sky line:nth-of-type(4){animation-delay:.75s}
@keyframes draw{to{stroke-dashoffset:0}}
.st{fill:#fff;filter:drop-shadow(0 0 6px #cdb4ff);animation:tw 2.4s ease-in-out infinite alternate}
.st:nth-of-type(2){animation-delay:-.6s}.st:nth-of-type(3){animation-delay:-1.2s}
.st:nth-of-type(4){animation-delay:-1.8s}.st:nth-of-type(5){animation-delay:-.3s}
@keyframes tw{from{opacity:.55}to{opacity:1}}"""},

# u24 蜂巢筑新
{"file":"u24.html","title":"蜂巢筑新","card":LIGHT,"accent":"#f0a832",
 "logs":["社区板块改版，氛围更甜","新增蜂蜜罐成就体系","消息推送更及时"],
 "art_html":'<div class="hive"><div class="hex"></div><div class="hex"></div><div class="hex"></div><div class="hex"></div><div class="hex"></div><div class="hex"></div><div class="hex"></div></div>',
 "art_css":""".art{background:linear-gradient(#fff6e3,#ffe9c2)}
.hive{display:flex;flex-wrap:wrap;justify-content:center;align-content:center;height:150px;
width:230px;margin:0 auto;padding-top:8px}
.hex{width:56px;height:62px;margin:3px;
background:linear-gradient(160deg,#ffd873,#f0a832);
clip-path:polygon(50% 0,100% 25%,100% 75%,50% 100%,0 75%,0 25%);
animation:hpop .55s cubic-bezier(.2,.9,.3,1.4) both}
.hex:nth-child(1){animation-delay:.05s}.hex:nth-child(2){animation-delay:.15s}
.hex:nth-child(3){animation-delay:.25s}.hex:nth-child(4){animation-delay:.35s}
.hex:nth-child(5){animation-delay:.45s}.hex:nth-child(6){animation-delay:.55s}
.hex:nth-child(7){animation-delay:.65s;background:linear-gradient(160deg,#ff9d5c,#e86a2c)}
@keyframes hpop{from{transform:scale(0)}to{transform:scale(1)}}"""},

# u25 磁带回潮
{"file":"u25.html","title":"磁带回潮","card":LIGHT,"accent":"#e8632c",
 "logs":["复古播放器皮肤回归","新增磁带收藏架功能","音质算法全面升级"],
 "art_html":'<div class="tape"><div class="reel r1"></div><div class="reel r2"></div><div class="tline"></div><div class="twin"></div></div>',
 "art_css":""".art{background:linear-gradient(#f7e8d8,#ecd7bd)}
.tape{position:relative;width:210px;height:118px;margin:16px auto;border-radius:14px;
background:linear-gradient(160deg,#ef7434,#c74e1f);box-shadow:0 10px 24px rgba(199,78,31,.35)}
.reel{position:absolute;top:20px;width:46px;height:46px;border-radius:50%;background:#f7efdd;
animation:spin 2.6s linear infinite}
.reel::after{content:"";position:absolute;inset:8px;border-radius:50%;
background:repeating-conic-gradient(#4a3826 0 40deg,#f7efdd 40deg 120deg)}
.r1{left:30px}.r2{right:30px;animation-duration:3.4s}
.tline{position:absolute;left:30px;right:30px;top:36px;height:3px;background:#3a2a1c}
.twin{position:absolute;left:60px;right:60px;bottom:14px;height:26px;border-radius:6px;
background:#3a2a1c;clip-path:polygon(8% 0,92% 0,100% 100%,0 100%)}"""},

# u26 摩天轮转
{"file":"u26.html","title":"摩天轮转","card":DARK,"accent":"#ff8fab",
 "logs":["乐园主题乐翻天","新增旋转木马小组件","签到玩法全面翻新"],
 "art_html":'''<div class="park"><div class="wheel"><div class="rim"></div>
<div class="sp s1"><div class="cab"></div></div><div class="sp s2"><div class="cab"></div></div>
<div class="sp s3"><div class="cab"></div></div><div class="sp s4"><div class="cab"></div></div>
<div class="sp s5"><div class="cab"></div></div><div class="sp s6"><div class="cab"></div></div>
<div class="hub"></div></div><div class="stand"></div></div>''',
 "art_css":""".art{background:linear-gradient(#1b1030,#3a1c4e)}
.park{position:relative;height:150px}
.wheel{position:absolute;left:50%;top:6px;width:128px;height:128px;margin-left:-64px;animation:spin 14s linear infinite}
.rim{position:absolute;inset:0;border-radius:50%;border:5px solid #ff8fab}
.sp{position:absolute;inset:0}
.s2{transform:rotate(60deg)}.s3{transform:rotate(120deg)}.s4{transform:rotate(180deg)}
.s5{transform:rotate(240deg)}.s6{transform:rotate(300deg)}
.cab{position:absolute;left:54px;top:-11px;width:20px;height:16px;border-radius:5px;background:#7ab8ff;
animation:spinRev 14s linear infinite;box-shadow:0 0 10px rgba(122,184,255,.8)}
.hub{position:absolute;left:50%;top:50%;width:14px;height:14px;margin:-7px;border-radius:50%;background:#ffd479}
.stand{position:absolute;left:50%;top:120px;width:0;height:0;margin-left:-34px;
border-left:34px solid transparent;border-right:34px solid transparent;border-bottom:26px solid #5a3a6e}"""},

# u27 熔岩新生
{"file":"u27.html","title":"熔岩新生","card":DARK,"accent":"#ff7a3c",
 "logs":["性能如火山爆发般提升","新增熔岩暗黑主题","崩溃率下降 90%"],
 "art_html":'<div class="volc"><div class="glow"></div><div class="mtn"></div><i class="lv l1"></i><i class="lv l2"></i><i class="lv l3"></i><i class="lv l4"></i><i class="lv l5"></i></div>',
 "art_css":""".art{background:linear-gradient(#170d0d,#2e1410)}
.volc{position:relative;height:150px;overflow:hidden}
.glow{position:absolute;left:50%;top:18px;width:120px;height:120px;margin-left:-60px;border-radius:50%;
background:radial-gradient(rgba(255,122,60,.55),transparent 70%);animation:fadeIn 1s both}
.mtn{position:absolute;left:50%;bottom:0;width:0;height:0;margin-left:-75px;
border-left:75px solid transparent;border-right:75px solid transparent;border-bottom:96px solid #40261e}
.mtn::after{content:"";position:absolute;left:-16px;top:78px;width:32px;height:18px;border-radius:50%;
background:radial-gradient(#ffcf6b,#ff7a3c)}
.lv{position:absolute;left:50%;bottom:88px;width:9px;height:9px;margin-left:-4px;border-radius:50%;
background:radial-gradient(#ffe29a,#ff7a3c);animation:erupt 2.2s ease-out infinite}
.l1{animation-delay:-.2s}.l2{animation-delay:-.8s;margin-left:-18px}
.l3{animation-delay:-1.3s;margin-left:12px}.l4{animation-delay:-1.7s;margin-left:-8px}
.l5{animation-delay:-.5s;margin-left:20px}
@keyframes erupt{0%{transform:translateY(0) scale(1);opacity:1}100%{transform:translateY(-70px) scale(.3);opacity:0}}"""},
]
