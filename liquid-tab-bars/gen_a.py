#!/usr/bin/env python3
"""生成 g01-g10 液态玻璃悬浮胶囊 Tab 栏"""
import os
D = os.path.expanduser('~/workspace/liquid-tab-bars')

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
.tabbar{position:absolute;left:18px;right:18px;bottom:26px;display:flex;align-items:stretch;border-radius:30px;padding:10px 8px;backdrop-filter:blur(22px) saturate(1.7);-webkit-backdrop-filter:blur(22px) saturate(1.7);box-shadow:inset 0 1px 0 rgba(255,255,255,.25),0 12px 34px rgba(0,0,0,.35)}
.tab{flex:1;background:none;border:0;color:var(--tc,#8b93a5);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:5px;font-size:11px;cursor:pointer;font-family:inherit;position:relative;padding:8px 0;z-index:1}
.tab .ic{width:26px;height:26px;display:block}
.tab .ic svg{width:100%;height:100%;display:block}
.tab i.dot{display:block;width:8px;height:8px}
"""

BASE_JS = """const nav=document.querySelector('.tabbar');
const LBL=%LBL%;
const IC={home:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 11l8-7 8 7v9h-5v-5h-6v5H4z"/></svg>',find:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><circle cx="12" cy="12" r="8"/><path d="M15.5 8.5l-2.2 4.8-4.8 2.2 2.2-4.8z"/></svg>',msg:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 6h16v10H9l-5 4z"/></svg>',me:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><circle cx="12" cy="8" r="4"/><path d="M4 20c1.2-4 4.2-6 8-6s6.8 2 8 6"/></svg>'};
Object.keys(LBL).forEach(k=>{const b=document.createElement('button');b.className='tab';
b.innerHTML='<i class="dot"></i><span class="ic">'+IC[k]+'</span><span class="tx">'+LBL[k]+'</span>';nav.appendChild(b);});
const tabs=[...document.querySelectorAll('.tab')];
let cur=0;
function act(i,instant){cur=i;tabs.forEach((t,j)=>t.classList.toggle('on',i===j));afterAct&&afterAct(i,instant);}
let afterAct=null;
tabs.forEach((t,i)=>t.addEventListener('click',()=>{act(i);try{history.replaceState(null,'','?tab='+i);}catch(e){}}));
(function(){const n=+new URLSearchParams(location.search).get('tab');
act(Number.isInteger(n)&&n>=0&&n<tabs.length?n:0,true);})();
"""

LBL4 = "{home:'首页',find:'发现',msg:'消息',me:'我的'}"

CARDS = """<div class="cardx"><div class="sk w60"></div><div class="sk"></div><div class="sk w80"></div></div>
<div class="cardx"><div class="sk w80"></div><div class="sk w60"></div></div>
<div class="cardx"><div class="sk"></div><div class="sk w60"></div><div class="sk w80"></div></div>
<div class="cardx"><div class="sk"></div><div class="sk w80"></div><div class="sk w60"></div></div>"""

V = []

# g01 幻彩流光：深底 + 彩虹流动轮廓光 + 滑动光条
V.append(dict(code='g01', title='幻彩流光', css="""
.g01{--bg:#0a0c14;--hd1:rgba(140,120,255,.14);--cx:rgba(255,255,255,.05);--cb:rgba(255,255,255,.09);--tc:#9aa0b4}
.g01 .phone{background:radial-gradient(120% 60% at 20% 0%,rgba(255,90,180,.16),transparent 60%),radial-gradient(120% 60% at 85% 20%,rgba(90,200,255,.14),transparent 60%),#0a0c14}
.g01 .tabbar{background:linear-gradient(135deg,rgba(30,34,52,.55),rgba(16,18,30,.55)) padding-box,linear-gradient(135deg,#ff5aa8,#a06bff,#4fd8ff,#7dffb0,#ff5aa8) border-box;background-size:auto,300% 300%;border:1.5px solid transparent;animation:flow 7s linear infinite;animation-delay:-3s}
@keyframes flow{to{background-position:0 0,300% 0}}
.g01 .ind{position:absolute;top:10px;bottom:10px;left:calc(8px + var(--i,0)*(100% - 16px)/4);width:calc((100% - 16px)/4);border-radius:20px;background:linear-gradient(135deg,rgba(255,90,168,.35),rgba(120,120,255,.35));box-shadow:0 0 18px rgba(150,120,255,.55),inset 0 1px 0 rgba(255,255,255,.4);transition:left .38s cubic-bezier(.34,1.4,.4,1)}
.g01 .ind.noanim{transition:none}
.g01 .tab.on{color:#fff}
.g01 .tab .tx{transition:color .3s}
""", js="""afterAct=function(i,instant){let ind=nav.querySelector('.ind');if(!ind){ind=document.createElement('i');ind.className='ind';ind.style.display='block';nav.prepend(ind);}if(instant){ind.classList.add('noanim');}nav.style.setProperty('--i',i);if(instant){requestAnimationFrame(()=>requestAnimationFrame(()=>ind.classList.remove('noanim')));}};"""))

# g02 晨雾霜白：浅底 + 白霜玻璃 + 液滴上浮指示
V.append(dict(code='g02', title='晨雾霜白', css="""
.g02{--bg:#eef1f6;--hd1:rgba(255,255,255,.7);--cx:rgba(255,255,255,.6);--cb:rgba(20,40,80,.08);--tc:#8a93a8;color:#22304a}
.g02 body,.g02{color:#22304a}
.g02 .phone{background:radial-gradient(120% 55% at 15% 0%,rgba(170,210,255,.5),transparent 60%),radial-gradient(100% 50% at 90% 25%,rgba(255,200,220,.4),transparent 60%),#eef1f6}
.g02 .hd p{color:#7a86a0}
.g02 .tabbar{background:linear-gradient(135deg,rgba(255,255,255,.72),rgba(255,255,255,.45)) padding-box,linear-gradient(135deg,rgba(160,200,255,.9),rgba(255,255,255,.4),rgba(190,170,255,.9)) border-box;border:1px solid transparent;box-shadow:inset 0 1px 0 #fff,0 12px 30px rgba(120,150,200,.35)}
.g02 .tab.on{color:#3a6fd8}
.g02 .tab .drop{position:absolute;top:2px;width:9px;height:9px;border-radius:50% 50% 50% 6px;transform:rotate(45deg) scale(0);background:linear-gradient(135deg,#7db4ff,#b48cff);box-shadow:0 2px 8px rgba(90,140,255,.6)}
.g02 .tab.on .drop{animation:rise .5s cubic-bezier(.34,1.7,.4,1) both;animation-delay:-.1s}
@keyframes rise{from{transform:rotate(45deg) translateY(8px) scale(0)}to{transform:rotate(45deg) translateY(0) scale(1)}}
""", js="""tabs.forEach(t=>{const d=document.createElement('i');d.className='drop';d.style.display='block';t.prepend(d);});"""))

# g03 深海荧光：深底蓝青 + 图标发光投影
V.append(dict(code='g03', title='深海荧光', css="""
.g03{--bg:#04121c;--hd1:rgba(60,220,255,.12);--cx:rgba(255,255,255,.05);--cb:rgba(120,220,255,.12);--tc:#7d8fa3}
.g03 .phone{background:radial-gradient(110% 55% at 80% 0%,rgba(0,180,220,.18),transparent 60%),radial-gradient(110% 55% at 10% 15%,rgba(40,120,255,.16),transparent 60%),#04121c}
.g03 .tabbar{background:linear-gradient(135deg,rgba(10,40,60,.6),rgba(4,18,28,.6)) padding-box,linear-gradient(135deg,rgba(80,220,255,.8),rgba(80,220,255,.1),rgba(120,140,255,.8)) border-box;border:1px solid transparent}
.g03 .tab.on{color:#5fe6ff}
.g03 .tab .ic{transition:filter .3s,transform .3s}
.g03 .tab.on .ic{filter:drop-shadow(0 0 8px rgba(95,230,255,.95)) drop-shadow(0 6px 10px rgba(95,230,255,.5));transform:translateY(-2px)}
.g03 .tab::after{content:"";position:absolute;bottom:4px;left:50%;width:26px;height:6px;margin-left:-13px;border-radius:50%;background:radial-gradient(closest-side,rgba(95,230,255,.7),transparent);opacity:0;transition:opacity .3s}
.g03 .tab.on::after{opacity:1}
""", js=""))

# g04 蜜桃气泡：浅底粉 + 胶囊包裹激活
V.append(dict(code='g04', title='蜜桃气泡', css="""
.g04{--bg:#fdf1ec;--hd1:rgba(255,255,255,.8);--cx:rgba(255,255,255,.65);--cb:rgba(220,120,140,.12);--tc:#a08a92;color:#4a2c34}
.g04{color:#4a2c34}
.g04 .phone{background:radial-gradient(110% 55% at 15% 0%,rgba(255,170,190,.45),transparent 60%),radial-gradient(100% 50% at 88% 22%,rgba(255,200,140,.4),transparent 60%),#fdf1ec}
.g04 .hd p{color:#b08a92}
.g04 .tabbar{background:linear-gradient(135deg,rgba(255,255,255,.75),rgba(255,240,244,.5)) padding-box,linear-gradient(135deg,#ff9eb0,#ffc98a,#ff9eb0) border-box;background-size:auto,250% 250%;border:1px solid transparent;animation:flow4 6s linear infinite;animation-delay:-2s;box-shadow:inset 0 1px 0 #fff,0 12px 30px rgba(230,140,160,.35)}
@keyframes flow4{to{background-position:0 0,250% 0}}
.g04 .tab .wrap{position:absolute;inset:6px 4px;border-radius:20px;background:linear-gradient(135deg,rgba(255,150,175,.35),rgba(255,190,130,.3));box-shadow:inset 0 1px 0 rgba(255,255,255,.7),0 4px 14px rgba(255,150,175,.35);transform:scale(.6);opacity:0;transition:transform .35s cubic-bezier(.34,1.6,.4,1),opacity .25s;z-index:-1}
.g04 .tab{position:relative;z-index:1}
.g04 .tab.on{color:#d64570}
.g04 .tab.on .wrap{transform:scale(1);opacity:1}
""", js="""tabs.forEach(t=>{const w=document.createElement('i');w.className='wrap';w.style.display='block';t.prepend(w);});"""))

# g05 霓虹紫电：深底紫霓虹 + 文字浮现 + 果冻图标
V.append(dict(code='g05', title='霓虹紫电', css="""
.g05{--bg:#0d0716;--hd1:rgba(180,90,255,.14);--cx:rgba(255,255,255,.05);--cb:rgba(180,120,255,.14);--tc:#8d84a8}
.g05 .phone{background:radial-gradient(110% 55% at 85% 0%,rgba(190,80,255,.2),transparent 60%),radial-gradient(110% 55% at 10% 18%,rgba(90,60,255,.18),transparent 60%),#0d0716}
.g05 .tabbar{background:linear-gradient(135deg,rgba(40,22,70,.6),rgba(16,8,28,.6)) padding-box,linear-gradient(135deg,#c95bff,#7b5bff,#ff5bc8,#c95bff) border-box;background-size:auto,300% 300%;border:1.5px solid transparent;animation:flow5 8s linear infinite;animation-delay:-4s}
@keyframes flow5{to{background-position:0 0,300% 0}}
.g05 .tab .tx{opacity:0;transform:translateY(6px);transition:opacity .3s,transform .35s cubic-bezier(.34,1.7,.4,1)}
.g05 .tab.on{color:#e0a6ff}
.g05 .tab.on .tx{opacity:1;transform:translateY(0)}
.g05 .tab.on .ic{animation:jelly .55s cubic-bezier(.34,1.8,.4,1);animation-delay:-.15s;filter:drop-shadow(0 0 10px rgba(200,120,255,.9))}
@keyframes jelly{0%{transform:scale(.6)}60%{transform:scale(1.18)}100%{transform:scale(1)}}
""", js=""))

# g06 薄荷冰晶：浅底青 + 呼吸光点
V.append(dict(code='g06', title='薄荷冰晶', css="""
.g06{--bg:#eef7f3;--hd1:rgba(255,255,255,.8);--cx:rgba(255,255,255,.6);--cb:rgba(60,170,150,.12);--tc:#8a9aa0;color:#23403c}
.g06{color:#23403c}
.g06 .phone{background:radial-gradient(110% 55% at 12% 0%,rgba(140,230,210,.5),transparent 60%),radial-gradient(100% 50% at 88% 20%,rgba(170,200,255,.35),transparent 60%),#eef7f3}
.g06 .hd p{color:#7d9490}
.g06 .tabbar{background:linear-gradient(135deg,rgba(255,255,255,.7),rgba(240,250,248,.45)) padding-box,linear-gradient(135deg,rgba(110,220,195,.9),rgba(255,255,255,.3),rgba(150,190,255,.9)) border-box;border:1px solid transparent;box-shadow:inset 0 1px 0 #fff,0 12px 30px rgba(110,190,170,.35)}
.g06 .tab.on{color:#0e9f86}
.g06 .tab .bdot{position:absolute;bottom:5px;width:7px;height:7px;border-radius:50%;background:#2fd6b4;box-shadow:0 0 10px #2fd6b4;opacity:0}
.g06 .tab.on .bdot{opacity:1;animation:breath 2s ease-in-out infinite;animation-delay:-1s}
@keyframes breath{50%{transform:scale(1.7);box-shadow:0 0 16px #2fd6b4}}
""", js="""tabs.forEach(t=>{const d=document.createElement('i');d.className='bdot';d.style.display='block';t.prepend(d);});"""))

# g07 熔岩流金：深底橙红 + 熔岩上涌填充
V.append(dict(code='g07', title='熔岩流金', css="""
.g07{--bg:#120806;--hd1:rgba(255,140,60,.14);--cx:rgba(255,255,255,.05);--cb:rgba(255,150,80,.14);--tc:#a08a7d}
.g07 .phone{background:radial-gradient(110% 55% at 80% 0%,rgba(255,110,40,.2),transparent 60%),radial-gradient(110% 55% at 12% 16%,rgba(255,60,60,.16),transparent 60%),#120806}
.g07 .tabbar{background:linear-gradient(135deg,rgba(60,25,12,.6),rgba(20,10,6,.6)) padding-box,linear-gradient(135deg,#ff8a3d,#ff4d4d,#ffc93d,#ff8a3d) border-box;background-size:auto,300% 300%;border:1.5px solid transparent;animation:flow7 7s linear infinite;animation-delay:-2.5s}
@keyframes flow7{to{background-position:0 0,300% 0}}
.g07 .tab .fill{position:absolute;left:10px;right:10px;bottom:8px;height:0;border-radius:16px;background:linear-gradient(180deg,rgba(255,150,60,.4),rgba(255,80,40,.25));box-shadow:inset 0 1px 0 rgba(255,200,140,.5);transition:height .4s cubic-bezier(.34,1.3,.4,1);z-index:-1}
.g07 .tab{position:relative;z-index:1}
.g07 .tab.on{color:#ffb03d}
.g07 .tab.on .fill{height:calc(100% - 16px)}
.g07 .tab.on .ic{filter:drop-shadow(0 0 8px rgba(255,150,60,.9))}
""", js="""tabs.forEach(t=>{const f=document.createElement('i');f.className='fill';f.style.display='block';t.prepend(f);});"""))

# g08 水银镜面：银灰 + 涟漪扩散
V.append(dict(code='g08', title='水银镜面', css="""
.g08{--bg:#e8eaee;--hd1:rgba(255,255,255,.85);--cx:rgba(255,255,255,.55);--cb:rgba(100,110,130,.14);--tc:#8b93a5;color:#2c3440}
.g08{color:#2c3440}
.g08 .phone{background:radial-gradient(110% 55% at 85% 0%,rgba(190,200,215,.6),transparent 60%),radial-gradient(100% 50% at 12% 20%,rgba(255,255,255,.8),transparent 60%),#e8eaee}
.g08 .hd p{color:#8b93a5}
.g08 .tabbar{background:linear-gradient(135deg,rgba(255,255,255,.65),rgba(225,230,238,.45)) padding-box,linear-gradient(135deg,#c8d2e0,#ffffff,#aeb9cc) border-box;border:1px solid transparent;box-shadow:inset 0 1px 0 #fff,0 12px 30px rgba(140,150,170,.4)}
.g08 .tab.on{color:#4a5a75}
.g08 .tab .ring{position:absolute;top:50%;left:50%;width:44px;height:44px;margin:-22px 0 0 -22px;border-radius:50%;border:2px solid rgba(120,140,170,.0)}
.g08 .tab.on .ring{animation:ripple 2.2s ease-out infinite;animation-delay:-.6s}
@keyframes ripple{0%{transform:scale(.5);border-color:rgba(120,140,170,.7);opacity:1}100%{transform:scale(1.25);border-color:rgba(120,140,170,0);opacity:0}}
.g08 .tab.on .ic{filter:drop-shadow(0 2px 4px rgba(90,110,140,.5))}
""", js="""tabs.forEach(t=>{const r=document.createElement('i');r.className='ring';r.style.display='block';t.prepend(r);});"""))

# g09 墨夜星河：纯黑底 + 星点 + 激活星光闪
V.append(dict(code='g09', title='墨夜星河', css="""
.g09{--bg:#050507;--hd1:rgba(255,255,255,.07);--cx:rgba(255,255,255,.045);--cb:rgba(255,255,255,.08);--tc:#7d7d8f}
.g09 .phone{background:radial-gradient(1.5px 1.5px at 12% 8%,#fff,transparent),radial-gradient(1.5px 1.5px at 32% 22%,#cdd6ff,transparent),radial-gradient(2px 2px at 68% 6%,#fff,transparent),radial-gradient(1.5px 1.5px at 86% 18%,#ffe9c9,transparent),radial-gradient(1.5px 1.5px at 48% 12%,#fff,transparent),radial-gradient(120% 60% at 70% 0%,rgba(90,80,200,.22),transparent 60%),#050507}
.g09 .tabbar{background:linear-gradient(135deg,rgba(28,28,38,.55),rgba(10,10,16,.55)) padding-box,linear-gradient(135deg,rgba(255,255,255,.35),rgba(255,255,255,.05),rgba(200,190,255,.4)) border-box;border:1px solid transparent}
.g09 .tab.on{color:#fff}
.g09 .tab .star{position:absolute;top:6px;right:calc(50% - 26px);font-size:10px;color:#ffe9a8;opacity:0;line-height:1}
.g09 .tab.on .star{opacity:1;animation:twk 1.8s ease-in-out infinite;animation-delay:-.9s;text-shadow:0 0 8px #ffd479}
@keyframes twk{50%{transform:scale(1.6) rotate(20deg);opacity:.6}}
.g09 .tab.on .ic{filter:drop-shadow(0 0 9px rgba(255,230,170,.85))}
""", js="""tabs.forEach(t=>{const s=document.createElement('i');s.className='star';s.style.display='block';s.textContent='✦';t.prepend(s);});"""))

# g10 奶油果冻：奶白浅底 + 果冻按压缩放
V.append(dict(code='g10', title='奶油果冻', css="""
.g10{--bg:#faf3e8;--hd1:rgba(255,255,255,.85);--cx:rgba(255,255,255,.65);--cb:rgba(200,160,120,.14);--tc:#a89a86;color:#4d4238}
.g10{color:#4d4238}
.g10 .phone{background:radial-gradient(110% 55% at 14% 0%,rgba(255,215,170,.5),transparent 60%),radial-gradient(100% 50% at 86% 20%,rgba(255,190,200,.35),transparent 60%),#faf3e8}
.g10 .hd p{color:#a89a86}
.g10 .tabbar{background:linear-gradient(135deg,rgba(255,255,255,.8),rgba(255,248,238,.55)) padding-box,linear-gradient(135deg,#ffd9a8,#ffb3c2,#fff3d9) border-box;background-size:auto,250% 250%;border:1px solid transparent;animation:flow10 6s linear infinite;animation-delay:-1.5s;box-shadow:inset 0 1px 0 #fff,0 12px 30px rgba(210,170,130,.4)}
@keyframes flow10{to{background-position:0 0,250% 0}}
.g10 .tab{transition:transform .18s}
.g10 .tab:active{transform:scale(.86,.78)}
.g10 .tab.on{color:#e0784f}
.g10 .tab.on .ic{animation:jm .5s cubic-bezier(.34,1.8,.4,1);animation-delay:-.12s}
@keyframes jm{0%{transform:scale(.7,.6)}55%{transform:scale(1.15,1.08)}100%{transform:scale(1)}}
.g10 .tab .jdot{position:absolute;bottom:6px;width:22px;height:5px;border-radius:3px;background:linear-gradient(90deg,#ffb37d,#ff8fb0);opacity:0;transform:scaleX(.4);transition:opacity .3s,transform .35s cubic-bezier(.34,1.7,.4,1)}
.g10 .tab.on .jdot{opacity:1;transform:scaleX(1)}
""", js="""tabs.forEach(t=>{const j=document.createElement('i');j.className='jdot';j.style.display='block';t.prepend(j);});"""))

HTML = """<!DOCTYPE html>
<html lang="zh-CN"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<style>{base}{css}</style></head>
<body class="{code}"><div class="phone">
<div class="hd"><h1>新鲜 UI 画廊</h1><p>FRESH · BOTTOMBAR · {title}</p></div>
<div class="bd">
{CARDS}
</div>
<nav class="tabbar"></nav>
<script>
{js_base}
{js}
</script>
</div></body></html>
"""

import json
titles = []
for v in V:
    html = HTML.format(title=v['title'], base=BASE_CSS, css=v['css'], code=v['code'],
                       CARDS=CARDS, js_base=BASE_JS.replace('%LBL%', LBL4), js=v['js'])
    open(os.path.join(D, v['code'] + '.html'), 'w', encoding='utf-8').write(html)
    titles.append({"file": v['code'] + '.html', "title": v['title']})
json.dump(titles, open(os.path.join(D, '_titles_tab_a.json'), 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
print('wrote', len(V), 'files')
for t in titles: print(t['file'], t['title'])
