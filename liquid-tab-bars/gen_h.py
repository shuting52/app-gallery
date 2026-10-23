# 生成 g71-g80 液态玻璃底部 Tab 栏（双层/异形方向）
import os, json

OUT = os.path.expanduser('~/workspace/liquid-tab-bars')

IC4 = {
 'home':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 11l8-7 8 7v9h-5v-5h-6v5H4z"/></svg>',
 'find':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><circle cx="12" cy="12" r="8"/><path d="M15.5 8.5l-2.2 4.8-4.8 2.2 2.2-4.8z"/></svg>',
 'msg':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 6h16v10H9l-5 4z"/></svg>',
 'me':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><circle cx="12" cy="8" r="4"/><path d="M4 20c1.2-4 4.2-6 8-6s6.8 2 8 6"/></svg>'}
LBL4 = {'home':'首页','find':'发现','msg':'消息','me':'我的'}
IC5 = dict(IC4); IC5['add']='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><path d="M12 5v14M5 12h14"/></svg>'
LBL5 = {'home':'首页','find':'发现','add':'','msg':'消息','me':'我的'}

def js_for(tabs, extra=''):
    return """const nav=document.querySelector('.tabbar');
const LBL=%s;const IC=%s;
Object.keys(LBL).forEach(k=>{const b=document.createElement('button');b.className='tab';
b.innerHTML='<span class="ic">'+IC[k]+'</span>'+(LBL[k]?'<span>'+LBL[k]+'</span>':'');nav.appendChild(b);});
const tabs=[...document.querySelectorAll('.tab')];
let cur=0;
function act(i){cur=i;tabs.forEach((t,j)=>t.classList.toggle('on',i===j));%s}
const svgNS='http://www.w3.org/2000/svg';
tabs.forEach(t=>{const d=document.createElement('i');d.className='dot';t.prepend(d);});
%s
tabs.forEach((t,i)=>t.addEventListener('click',()=>{act(i);try{history.replaceState(null,'','?tab='+i);}catch(e){}}));
(function(){const n=+new URLSearchParams(location.search).get('tab');
act(Number.isInteger(n)&&n>=0&&n<tabs.length?n:0);})();""" % (
        json.dumps(tabs[0], ensure_ascii=False), json.dumps(tabs[1], ensure_ascii=False),
        'moveInd(i);' if 'slide' in extra.lower() or 'sat' in extra.lower() else '', extra)

SLIDE_JS = """const sl=document.createElement('i');sl.className='slide';nav.appendChild(sl);
function moveInd(i){const t=tabs[i];sl.style.left=(t.offsetLeft+t.offsetWidth/2-26)+'px';sl.style.width='52px';}
window.addEventListener('resize',()=>moveInd(cur));"""

BASE_CSS = """*{margin:0;padding:0;box-sizing:border-box}
html,body{height:100%}
body{font-family:-apple-system,"PingFang SC","Hiragino Sans GB","Microsoft YaHei",system-ui,sans-serif;background:#07090d;display:flex;justify-content:center;color:#eef2f8}
.phone{width:430px;height:900px;position:relative;overflow:hidden;background:var(--bg,#0d1117)}
.hd{padding:54px 22px 10px;background:linear-gradient(180deg,var(--hd1,rgba(255,255,255,.08)),transparent)}
.hd h1{font-size:22px;letter-spacing:2px}
.hd p{font-size:12px;opacity:.55;margin-top:6px;letter-spacing:1px}
.bd{padding:16px 18px;display:flex;flex-direction:column;gap:14px}
.cardx{border-radius:16px;padding:16px;background:var(--cx,rgba(255,255,255,.05));border:1px solid var(--cb,rgba(255,255,255,.08))}
.sk{height:12px;border-radius:6px;background:linear-gradient(90deg,var(--s1,rgba(255,255,255,.14)),var(--s2,rgba(255,255,255,.05)));margin:8px 0}
.sk.w60{width:60%}.sk.w80{width:80%}
.tab{flex:1;background:none;border:0;color:var(--tc,#8b93a5);display:flex;flex-direction:column;align-items:center;gap:5px;font-size:11px;cursor:pointer;font-family:inherit;position:relative;padding:6px 0;z-index:2}
.tab .ic{width:26px;height:26px;display:block}
.tab .ic svg{width:100%;height:100%;display:block}
.tab .dot{display:block;position:absolute;width:0;height:0}
"""

# 每款：cls,title,5tabs?,page vars,css,extra js
D = []

# ---------- g71 双层叠嶂（深海蓝） ----------
D.append(dict(cls='g71', title='双层叠嶂', tabs5=False,
 vars='--bg:#0a1220;--hd1:rgba(125,211,252,.10);--cx:rgba(125,211,252,.06);--cb:rgba(125,211,252,.14);--ac:#7dd3fc;',
 css="""
.g71 .phone::after{content:'';position:absolute;left:-60px;right:-60px;bottom:-70px;height:300px;pointer-events:none;
 background:radial-gradient(120px 90px at 20% 60%,rgba(56,189,248,.5),transparent 70%),radial-gradient(140px 100px at 75% 40%,rgba(34,211,238,.45),transparent 70%),radial-gradient(90px 80px at 50% 80%,rgba(96,165,250,.4),transparent 70%);filter:blur(24px)}
.g71 .tabbar{position:absolute;left:18px;right:18px;bottom:26px;display:flex;z-index:5}
.g71 .tabbar::before{content:'';position:absolute;inset:12px -7px -7px 7px;border-radius:26px;background:rgba(8,18,34,.75);backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);border:1px solid rgba(125,211,252,.18);z-index:0}
.g71 .tabbar::after{content:'';position:absolute;inset:0;border-radius:26px;background:linear-gradient(160deg,rgba(125,211,252,.28),rgba(56,130,190,.12) 60%,rgba(20,40,70,.35));backdrop-filter:blur(20px) saturate(1.6);-webkit-backdrop-filter:blur(20px) saturate(1.6);border:1px solid rgba(160,220,255,.4);box-shadow:inset 0 1px 0 rgba(255,255,255,.5),0 14px 34px rgba(2,10,24,.55);z-index:1}
.g71 .tab{padding:14px 0 12px}
.g71 .tab .dot{position:absolute;bottom:5px;left:50%;width:22px;height:6px;margin-left:-11px;border-radius:4px;background:linear-gradient(90deg,#38bdf8,#7dd3fc);box-shadow:0 0 12px #38bdf8;opacity:0;transform:scaleX(.3);transition:all .35s cubic-bezier(.34,1.56,.64,1)}
.g71 .tab.on .dot{opacity:1;transform:scaleX(1)}
.g71 .tab.on{color:#bfe9ff}
.g71 .tab.on .ic{filter:drop-shadow(0 0 8px rgba(125,211,252,.9));transform:translateY(-2px)}
.g71 .tab .ic{transition:all .3s}
""", extra=''))

# ---------- g72 浪顶（深青波浪顶边） ----------
D.append(dict(cls='g72', title='浪顶', tabs5=False,
 vars='--bg:#0a1512;--hd1:rgba(45,212,191,.10);--cx:rgba(45,212,191,.06);--cb:rgba(45,212,191,.14);--ac:#2dd4bf;',
 css="""
.g72 .phone::after{content:'';position:absolute;left:-60px;right:-60px;bottom:-70px;height:300px;pointer-events:none;
 background:radial-gradient(130px 90px at 30% 55%,rgba(45,212,191,.5),transparent 70%),radial-gradient(120px 100px at 70% 65%,rgba(16,185,129,.45),transparent 70%);filter:blur(24px)}
.g72 .tabbar{position:absolute;left:0;right:0;bottom:0;display:flex;z-index:5;padding:26px 6px calc(20px + env(safe-area-inset-bottom));
 background:linear-gradient(180deg,rgba(20,40,36,.55),rgba(10,22,19,.92));backdrop-filter:blur(20px) saturate(1.5);-webkit-backdrop-filter:blur(20px) saturate(1.5);
 -webkit-mask:radial-gradient(26px at 43px 0,transparent 98%,#000) 0 0/86px 26px repeat-x,linear-gradient(#000,#000) 0 26px/100% 100% no-repeat;
 mask:radial-gradient(26px at 43px 0,transparent 98%,#000) 0 0/86px 26px repeat-x,linear-gradient(#000,#000) 0 26px/100% 100% no-repeat;
 border-top:1px solid rgba(45,212,191,.25)}
.g72 .tab{padding:10px 0 6px}
.g72 .slide{position:absolute;top:30px;height:44px;border-radius:14px;background:rgba(45,212,191,.22);border:1px solid rgba(45,212,191,.5);box-shadow:inset 0 1px 0 rgba(255,255,255,.35),0 0 18px rgba(45,212,191,.35);transition:left .35s cubic-bezier(.34,1.56,.64,1);z-index:1;pointer-events:none;display:block}
.g72 .tab .dot{display:none}
.g72 .tab.on{color:#a7f3ea}
.g72 .tab.on .ic{filter:drop-shadow(0 0 8px rgba(45,212,191,.9))}
""", extra='SLIDE'))

# ---------- g73 斜切玻璃（霓虹紫斜切） ----------
D.append(dict(cls='g73', title='斜切玻璃', tabs5=False,
 vars='--bg:#100b1c;--hd1:rgba(192,132,252,.10);--cx:rgba(192,132,252,.06);--cb:rgba(192,132,252,.14);--ac:#c084fc;',
 css="""
.g73 .phone::after{content:'';position:absolute;left:-60px;right:-60px;bottom:-70px;height:300px;pointer-events:none;
 background:radial-gradient(130px 90px at 65% 55%,rgba(168,85,247,.5),transparent 70%),radial-gradient(110px 90px at 25% 70%,rgba(217,70,239,.4),transparent 70%);filter:blur(24px)}
.g73 .tabbar{position:absolute;left:26px;right:26px;bottom:28px;display:flex;z-index:5;padding:12px 4px;
 background:linear-gradient(155deg,rgba(192,132,252,.3),rgba(120,60,200,.14) 55%,rgba(40,20,80,.4));backdrop-filter:blur(20px) saturate(1.6);-webkit-backdrop-filter:blur(20px) saturate(1.6);
 border:1px solid rgba(216,180,254,.45);box-shadow:inset 0 1px 0 rgba(255,255,255,.5),0 14px 34px rgba(20,5,40,.55);
 clip-path:polygon(5% 0,100% 0,95% 100%,0 100%)}
.g73 .tab{padding:10px 0 8px}
.g73 .tab .dot{position:absolute;top:2px;left:50%;width:8px;height:8px;margin-left:-4px;background:#e9d5ff;transform:rotate(45deg) scale(0);box-shadow:0 0 10px #c084fc;transition:transform .3s cubic-bezier(.34,1.56,.64,1)}
.g73 .tab.on .dot{transform:rotate(45deg) scale(1)}
.g73 .tab.on{color:#f0e2ff}
.g73 .tab.on .ic{filter:drop-shadow(0 0 8px rgba(192,132,252,.9))}
""", extra=''))

# ---------- g74 偏锋弧（旋转不对称，深橙） ----------
D.append(dict(cls='g74', title='偏锋弧', tabs5=False,
 vars='--bg:#160d08;--hd1:rgba(251,146,60,.10);--cx:rgba(251,146,60,.06);--cb:rgba(251,146,60,.14);--ac:#fb923c;',
 css="""
.g74 .phone::after{content:'';position:absolute;left:-60px;right:-60px;bottom:-70px;height:300px;pointer-events:none;
 background:radial-gradient(130px 90px at 70% 60%,rgba(251,146,60,.5),transparent 70%),radial-gradient(110px 90px at 20% 65%,rgba(239,68,68,.4),transparent 70%);filter:blur(24px)}
.g74 .tabbar{position:absolute;left:30px;right:30px;bottom:34px;display:flex;z-index:5;padding:14px 4px 12px;transform:rotate(-3deg);
 background:linear-gradient(160deg,rgba(251,146,60,.28),rgba(160,80,30,.12) 55%,rgba(50,25,10,.4));backdrop-filter:blur(20px) saturate(1.6);-webkit-backdrop-filter:blur(20px) saturate(1.6);
 border:1px solid rgba(253,186,116,.45);border-radius:30px 30px 30px 10px;box-shadow:inset 0 1px 0 rgba(255,255,255,.5),0 14px 34px rgba(30,10,2,.55)}
.g74 .slide{position:absolute;bottom:6px;height:4px;border-radius:3px;background:linear-gradient(90deg,#fb923c,#fdba74);box-shadow:0 0 12px #fb923c;transition:left .35s cubic-bezier(.34,1.56,.64,1);z-index:3;pointer-events:none;display:block}
.g74 .tab .dot{display:none}
.g74 .tab.on{color:#ffe7c7}
.g74 .tab.on .ic{filter:drop-shadow(0 0 8px rgba(251,146,60,.9));transform:translateY(-3px) rotate(3deg)}
.g74 .tab .ic{transition:all .3s}
""", extra='SLIDE'))

# ---------- g75 星链胶囊（胶囊+两小圆，蜜桃浅底） ----------
D.append(dict(cls='g75', title='星链胶囊', tabs5=True,
 vars='--bg:#fdf3ec;--hd1:rgba(251,146,60,.12);--cx:rgba(180,100,40,.06);--cb:rgba(180,100,40,.14);--tc:#a08a76;--ac:#f97316;--s1:rgba(180,100,40,.14);--s2:rgba(180,100,40,.05);',
 css="""body.g75{color:#4a3b2e}
.g75 .phone::after{content:'';position:absolute;left:-60px;right:-60px;bottom:-70px;height:300px;pointer-events:none;
 background:radial-gradient(130px 90px at 30% 60%,rgba(251,146,60,.35),transparent 70%),radial-gradient(120px 90px at 70% 55%,rgba(244,114,182,.3),transparent 70%);filter:blur(24px)}
.g75 .tabbar{position:absolute;left:0;right:0;bottom:0;display:flex;align-items:center;justify-content:center;gap:14px;z-index:5;padding:0 0 calc(26px + env(safe-area-inset-bottom));background:none;backdrop-filter:none;-webkit-backdrop-filter:none;border:0}
.g75 .tab{flex:none;width:56px;height:56px;border-radius:50%;padding:0;justify-content:center;gap:0;
 background:rgba(255,255,255,.55);backdrop-filter:blur(18px) saturate(1.5);-webkit-backdrop-filter:blur(18px) saturate(1.5);
 border:1px solid rgba(255,255,255,.8);box-shadow:inset 0 1px 0 #fff,0 8px 20px rgba(200,120,60,.25)}
.g75 .tab .ic{width:24px;height:24px}
.g75 .tab:nth-child(2){width:72px;border-radius:28px 10px 10px 28px;margin-right:-12px}
.g75 .tab:nth-child(3){width:72px;border-radius:10px;margin-left:-2px;margin-right:-2px}
.g75 .tab:nth-child(4){width:72px;border-radius:10px 28px 28px 10px;margin-left:-12px}
.g75 .tab .ic + span{display:none}
.g75 .tab .dot{display:none}
.g75 .tab.on{background:linear-gradient(150deg,#fdba74,#f97316);color:#fff;border-color:#fdba74;box-shadow:inset 0 1px 0 rgba(255,255,255,.6),0 8px 22px rgba(249,115,22,.5)}
.g75 .tab.on .ic{filter:drop-shadow(0 0 6px rgba(255,255,255,.8))}
""", extra=''))

# ---------- g76 贝壳弧（凹弧 dock，深绿） ----------
D.append(dict(cls='g76', title='贝壳弧', tabs5=True,
 vars='--bg:#081410;--hd1:rgba(52,211,153,.10);--cx:rgba(52,211,153,.06);--cb:rgba(52,211,153,.14);--ac:#34d399;',
 css="""
.g76 .phone::after{content:'';position:absolute;left:-60px;right:-60px;bottom:-70px;height:300px;pointer-events:none;
 background:radial-gradient(130px 90px at 50% 60%,rgba(52,211,153,.45),transparent 70%),radial-gradient(100px 80px at 20% 70%,rgba(16,185,129,.4),transparent 70%);filter:blur(24px)}
.g76 .tabbar{position:absolute;left:0;right:0;bottom:0;display:flex;z-index:5;padding:30px 10px calc(20px + env(safe-area-inset-bottom))}
.g76 .tabbar::before{content:'';position:absolute;inset:0;z-index:0;
 background:linear-gradient(180deg,rgba(16,40,32,.6),rgba(6,18,14,.94));backdrop-filter:blur(20px) saturate(1.5);-webkit-backdrop-filter:blur(20px) saturate(1.5);
 border-top:1px solid rgba(52,211,153,.3);
 -webkit-mask:radial-gradient(46px at 50% 0,transparent 96%,#000) 0 0/100% 34px no-repeat,linear-gradient(#000,#000) 0 30px/100% 100% no-repeat;
 mask:radial-gradient(46px at 50% 0,transparent 96%,#000) 0 0/100% 34px no-repeat,linear-gradient(#000,#000) 0 30px/100% 100% no-repeat}
.g76 .tab{padding:8px 0 6px}
.g76 .tab:nth-child(3){margin-top:-34px}
.g76 .tab:nth-child(3) .ic{width:52px;height:52px;border-radius:50%;display:flex;align-items:center;justify-content:center;
 background:linear-gradient(150deg,#6ee7b7,#10b981);color:#04251b;border:2px solid rgba(255,255,255,.5);box-shadow:0 8px 24px rgba(52,211,153,.55),inset 0 1px 0 rgba(255,255,255,.6)}
.g76 .tab:nth-child(3) .ic svg{width:26px;height:26px}
.g76 .tab:nth-child(3) .ic + span{display:none}
.g76 .tab .dot{position:absolute;top:4px;left:50%;width:6px;height:6px;margin-left:-3px;border-radius:50%;background:#6ee7b7;box-shadow:0 0 10px #34d399;opacity:0;transition:opacity .3s}
.g76 .tab.on .dot{opacity:1}
.g76 .tab.on{color:#a7f3d0}
.g76 .tab:nth-child(3).on .ic{box-shadow:0 8px 30px rgba(52,211,153,.9),inset 0 1px 0 rgba(255,255,255,.7)}
""", extra=''))

# ---------- g77 错层玻璃（浅蓝双层错位） ----------
D.append(dict(cls='g77', title='错层玻璃', tabs5=False,
 vars='--bg:#eef4fb;--hd1:rgba(59,130,246,.10);--cx:rgba(59,130,246,.07);--cb:rgba(59,130,246,.16);--tc:#8a97ab;--ac:#3b82f6;--s1:rgba(59,130,246,.16);--s2:rgba(59,130,246,.06);',
 css="""body.g77{color:#33415c}
.g77 .phone::after{content:'';position:absolute;left:-60px;right:-60px;bottom:-70px;height:300px;pointer-events:none;
 background:radial-gradient(130px 90px at 30% 60%,rgba(96,165,250,.4),transparent 70%),radial-gradient(120px 90px at 70% 55%,rgba(56,189,248,.35),transparent 70%);filter:blur(24px)}
.g77 .tabbar{position:absolute;left:20px;right:44px;bottom:40px;display:flex;z-index:5}
.g77 .tabbar::before{content:'';position:absolute;inset:14px -20px -14px 20px;border-radius:24px;background:rgba(255,255,255,.5);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);border:1px solid rgba(255,255,255,.85);box-shadow:0 10px 26px rgba(59,130,246,.18);z-index:0}
.g77 .tabbar::after{content:'';position:absolute;inset:0;border-radius:24px;background:linear-gradient(160deg,rgba(255,255,255,.75),rgba(219,234,254,.45));backdrop-filter:blur(20px) saturate(1.5);-webkit-backdrop-filter:blur(20px) saturate(1.5);border:1px solid rgba(255,255,255,.9);box-shadow:inset 0 1px 0 #fff,0 12px 30px rgba(59,130,246,.2);z-index:1}
.g77 .tab{padding:13px 0 11px}
.g77 .tab .dot{position:absolute;top:6px;width:26px;height:26px;border-radius:50%;background:radial-gradient(circle at 32% 30%,#dbeafe,#3b82f6 75%);box-shadow:0 4px 12px rgba(59,130,246,.5);opacity:0;transform:translateY(6px) scale(.5);transition:all .35s cubic-bezier(.34,1.56,.64,1);z-index:-1}
.g77 .tab.on .dot{opacity:1;transform:translateY(0) scale(1)}
.g77 .tab.on{color:#1d4ed8}
.g77 .tab.on .ic{filter:drop-shadow(0 0 7px rgba(59,130,246,.7))}
""", extra=''))

# ---------- g78 梯形水晶（上宽下窄，冰晶浅底） ----------
D.append(dict(cls='g78', title='梯形水晶', tabs5=False,
 vars='--bg:#f2f7fd;--hd1:rgba(14,165,233,.10);--cx:rgba(14,165,233,.07);--cb:rgba(14,165,233,.16);--tc:#8a97ab;--ac:#0ea5e9;--s1:rgba(14,165,233,.16);--s2:rgba(14,165,233,.06);',
 css="""body.g78{color:#33415c}
.g78 .phone::after{content:'';position:absolute;left:-60px;right:-60px;bottom:-70px;height:300px;pointer-events:none;
 background:radial-gradient(130px 90px at 50% 60%,rgba(14,165,233,.4),transparent 70%),radial-gradient(100px 80px at 75% 70%,rgba(165,243,252,.5),transparent 70%);filter:blur(24px)}
.g78 .tabbar{position:absolute;left:60px;right:60px;bottom:26px;display:flex;z-index:5;padding:16px 2px 12px;
 background:linear-gradient(180deg,rgba(255,255,255,.8),rgba(186,230,253,.4));backdrop-filter:blur(20px) saturate(1.7);-webkit-backdrop-filter:blur(20px) saturate(1.7);
 border:1px solid rgba(255,255,255,.95);box-shadow:inset 0 2px 0 #fff,inset 0 -8px 16px rgba(14,165,233,.12),0 14px 30px rgba(14,165,233,.22);
 clip-path:polygon(0 0,100% 0,88% 100%,12% 100%)}
.g78 .slide{position:absolute;top:8px;height:6px;border-radius:4px;background:linear-gradient(90deg,#0ea5e9,#67e8f9);box-shadow:0 0 14px #0ea5e9;transition:left .35s cubic-bezier(.34,1.56,.64,1);z-index:3;pointer-events:none;display:block}
.g78 .tab .dot{display:none}
.g78 .tab.on{color:#0369a1}
.g78 .tab.on .ic{filter:drop-shadow(0 0 8px rgba(14,165,233,.8));transform:scale(1.12)}
.g78 .tab .ic{transition:all .3s}
""", extra='SLIDE'))

# ---------- g79 潮汐双层（浅底+深色波浪层） ----------
D.append(dict(cls='g79', title='潮汐双层', tabs5=False,
 vars='--bg:#f6f1ea;--hd1:rgba(217,119,6,.10);--cx:rgba(217,119,6,.07);--cb:rgba(217,119,6,.16);--tc:#97836a;--ac:#d97706;--s1:rgba(217,119,6,.16);--s2:rgba(217,119,6,.06);',
 css="""body.g79{color:#4a3f30}
.g79 .phone::after{content:'';position:absolute;left:-60px;right:-60px;bottom:-70px;height:300px;pointer-events:none;
 background:radial-gradient(130px 90px at 40% 60%,rgba(217,119,6,.35),transparent 70%),radial-gradient(110px 90px at 70% 65%,rgba(234,88,12,.3),transparent 70%);filter:blur(24px)}
.g79 .tabbar{position:absolute;left:0;right:0;bottom:0;z-index:5}
.g79 .tide{position:absolute;left:0;right:0;bottom:0;height:118px;
 background:linear-gradient(180deg,rgba(60,35,10,.55),rgba(30,18,6,.92));backdrop-filter:blur(18px) saturate(1.4);-webkit-backdrop-filter:blur(18px) saturate(1.4);
 -webkit-mask:radial-gradient(55px at 55px -47px,transparent 97%,#000) 0 0/110px 24px repeat-x,linear-gradient(#000,#000) 0 20px/100% 100% no-repeat;
 mask:radial-gradient(55px at 55px -47px,transparent 97%,#000) 0 0/110px 24px repeat-x,linear-gradient(#000,#000) 0 20px/100% 100% no-repeat}
.g79 .tbase{position:absolute;left:24px;right:24px;bottom:16px;height:64px;border-radius:32px;
 background:rgba(255,255,255,.6);backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px);border:1px solid rgba(255,255,255,.9);box-shadow:0 10px 26px rgba(180,120,40,.2)}
.g79 .row{position:relative;display:flex;padding:24px 30px calc(22px + env(safe-area-inset-bottom))}
.g79 .tab{padding:10px 0 8px;color:#e8d9bd}
.g79 .tab .dot{position:absolute;bottom:2px;left:50%;width:20px;height:5px;margin-left:-10px;border-radius:3px;background:linear-gradient(90deg,#fbbf24,#f59e0b);box-shadow:0 0 12px #f59e0b;opacity:0;transform:scaleX(.3);transition:all .35s cubic-bezier(.34,1.56,.64,1)}
.g79 .tab.on .dot{opacity:1;transform:scaleX(1)}
.g79 .tab.on{color:#fff7e6}
.g79 .tab.on .ic{filter:drop-shadow(0 0 8px rgba(251,191,36,.9))}
""", extra='TIDE'))
# g79 需要 .tide/.tbase/.row 三层结构 —— 用 extra 标记做特殊 HTML
TIDE_HTML = True

# ---------- g80 环绕卫星（深紫，卫星点跟随激活） ----------
D.append(dict(cls='g80', title='环绕卫星', tabs5=False,
 vars='--bg:#0d0a18;--hd1:rgba(167,139,250,.10);--cx:rgba(167,139,250,.06);--cb:rgba(167,139,250,.14);--ac:#a78bfa;',
 css="""
.g80 .phone::after{content:'';position:absolute;left:-60px;right:-60px;bottom:-70px;height:300px;pointer-events:none;
 background:radial-gradient(130px 90px at 60% 55%,rgba(139,92,246,.5),transparent 70%),radial-gradient(100px 80px at 25% 70%,rgba(99,102,241,.4),transparent 70%);filter:blur(24px)}
.g80 .tabbar{position:absolute;left:22px;right:22px;bottom:28px;display:flex;z-index:5;padding:16px 4px 12px;
 background:linear-gradient(160deg,rgba(139,92,246,.22),rgba(80,50,160,.1) 55%,rgba(25,15,55,.45));backdrop-filter:blur(20px) saturate(1.6);-webkit-backdrop-filter:blur(20px) saturate(1.6);
 border:1px solid rgba(196,181,253,.4);border-radius:28px;box-shadow:inset 0 1px 0 rgba(255,255,255,.5),0 14px 34px rgba(15,5,35,.55)}
.g80 .sat{position:absolute;top:-6px;width:14px;height:14px;border-radius:50%;display:block;z-index:4;pointer-events:none;
 background:radial-gradient(circle at 35% 30%,#ede9fe,#8b5cf6 70%);box-shadow:0 0 16px #a78bfa,0 0 4px #fff;transition:left .45s cubic-bezier(.34,1.56,.64,1)}
.g80 .tab .dot{display:none}
.g80 .tab.on{color:#dcd2ff}
.g80 .tab.on .ic{filter:drop-shadow(0 0 10px rgba(167,139,250,1));transform:translateY(-2px) scale(1.1)}
.g80 .tab .ic{transition:all .3s}
""", extra='SAT'))


def build(d):
    cls, title = d['cls'], d['title']
    lbl, ic = (LBL5, IC5) if d['tabs5'] else (LBL4, IC4)
    extra = d.get('extra','')
    extra_js = ''
    if 'SLIDE' in extra: extra_js += SLIDE_JS
    if 'SAT' in extra:
        extra_js += """const sat=document.createElement('i');sat.className='sat';nav.appendChild(sat);
function moveInd(i){const t=tabs[i];sat.style.left=(t.offsetLeft+t.offsetWidth/2-7)+'px';}
window.addEventListener('resize',()=>moveInd(cur));"""
    js = js_for((lbl, ic), extra_js)
    # g79 特殊三层结构
    if cls == 'g79':
        bar_html = '<nav class="tabbar"><div class="tide"></div><div class="tbase"></div><div class="row"></div></nav>'
        # JS 里 nav 指向 .row
        js = js.replace("document.querySelector('.tabbar')", "document.querySelector('.tabbar .row')")
    else:
        bar_html = '<nav class="tabbar"></nav>'
    html = f"""<!DOCTYPE html>
<html lang="zh-CN"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<style>{BASE_CSS}{d['css']}</style></head>
<body class="{cls}"><div class="phone" style="{d['vars']}">
<div class="hd"><h1>新鲜 UI 画廊</h1><p>FRESH · BOTTOMBAR · {title}</p></div>
<div class="bd">
<div class="cardx"><div class="sk w60"></div><div class="sk"></div><div class="sk w80"></div></div>
<div class="cardx"><div class="sk w80"></div><div class="sk w60"></div></div>
<div class="cardx"><div class="sk"></div><div class="sk w60"></div><div class="sk w80"></div></div>
<div class="cardx"><div class="sk"></div><div class="sk w80"></div><div class="sk w60"></div></div>
</div>
{bar_html}
<script>
{js}
</script>
</div></body></html>"""
    with open(os.path.join(OUT, cls + '.html'), 'w', encoding='utf-8') as f:
        f.write(html)

if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    for d in D:
        build(d)
    titles = [{"file": d['cls'] + '.html', "title": d['title']} for d in D]
    with open(os.path.join(OUT, '_titles_tab_h.json'), 'w', encoding='utf-8') as f:
        json.dump(titles, f, ensure_ascii=False, indent=1)
    print('generated', len(D))
