#!/usr/bin/env python3
"""part2: u28-u36 + 生成"""
import os, json
exec(open(os.path.expanduser("~/workspace/fresh-ui/build_update_b.py"), encoding="utf-8").read())  # part1: BASE_CSS/DARK/LIGHT/SHARED_JS/CONCEPTS

CONCEPTS2 = [
# u28 灯塔指引
{"file":"u28.html","title":"灯塔指引","card":DARK,"accent":"#ffe9a8",
 "logs":["新手引导如灯塔般清晰","新增夜间航行模式","搜索直达更精准"],
 "art_html":'<div class="night"><div class="beamwrap"><div class="beam"></div></div><div class="tower"><div class="lamp"></div></div><div class="sea2"></div></div>',
 "art_css":""".night{position:absolute;inset:0;background:linear-gradient(#060a1c,#0e1a3a);overflow:hidden}
.tower{position:absolute;left:50%;bottom:34px;width:36px;height:88px;margin-left:-18px;
background:repeating-linear-gradient(#f4f1e8 0 11px,#d23c3c 11px 22px);
clip-path:polygon(28% 0,72% 0,100% 100%,0 100%)}
.lamp{position:absolute;top:-12px;left:50%;width:20px;height:14px;margin-left:-10px;border-radius:4px;
background:#ffe9a8;box-shadow:0 0 16px #ffe9a8}
.beamwrap{position:absolute;left:50%;bottom:112px;width:0;height:0;animation:spin 5s linear infinite}
.beam{position:absolute;left:0;top:-13px;width:150px;height:26px;
background:linear-gradient(90deg,rgba(255,233,168,.75),transparent);
clip-path:polygon(0 42%,100% 0,100% 100%,0 58%)}
.sea2{position:absolute;left:0;right:0;bottom:0;height:34px;
background:linear-gradient(rgba(60,120,200,.35),rgba(20,50,110,.6))}"""},

# u29 伞降更新
{"file":"u29.html","title":"伞降更新","card":LIGHT,"accent":"#ff6b6b",
 "logs":["新功能空投已送达","更新包体积缩减一半","断点续传更可靠"],
 "art_html":'<div class="drop"><div class="chute"></div><div class="rope r1"></div><div class="rope r2"></div><div class="box">NEW</div><i class="cl c1"></i><i class="cl c2"></i></div>',
 "art_css":""".art{background:linear-gradient(#bfe3ff,#e8f4ff)}
.drop{position:relative;height:150px;animation:descend 5s ease-in-out infinite alternate}
@keyframes descend{from{transform:translateY(-6px)}to{transform:translateY(14px)}}
.chute{width:128px;height:62px;margin:8px auto 0;border-radius:64px 64px 6px 6px;
background:repeating-linear-gradient(90deg,#ff6b6b 0 16px,#fff 16px 32px);
animation:sway2 3s ease-in-out infinite alternate;box-shadow:0 6px 16px rgba(255,107,107,.35)}
@keyframes sway2{from{transform:rotate(-4deg)}to{transform:rotate(4deg)}}
.rope{position:absolute;top:66px;width:2px;height:34px;background:#8a94a6}
.rope.r1{left:146px;transform:rotate(12deg)}.rope.r2{right:146px;transform:rotate(-12deg)}
.box{width:52px;height:52px;margin:26px auto 0;border-radius:10px;background:linear-gradient(135deg,#8a6d3b,#6b5227);
color:#ffe9a8;font-size:13px;font-weight:800;display:flex;align-items:center;justify-content:center;
box-shadow:0 8px 18px rgba(107,82,39,.4)}
.cl{position:absolute;background:#fff;border-radius:20px;opacity:.9;animation:drift 7s linear infinite}
.c1{left:30px;top:40px;width:56px;height:18px}
.c2{right:24px;top:96px;width:44px;height:14px;animation-delay:-3.5s}
@keyframes drift{from{transform:translateX(-14px)}to{transform:translateX(14px)}}"""},

# u30 气泡上浮
{"file":"u30.html","title":"气泡上浮","card":DARK,"accent":"#8cdcff",
 "logs":["界面如气泡般轻盈","新增悬浮球快捷操作","滑动跟手性提升"],
 "art_html":'<div class="liquid"><i class="bb b1"></i><i class="bb b2"></i><i class="bb b3"></i><i class="bb b4"></i><i class="bb b5"></i><i class="bb b6"></i><i class="bb b7"></i><i class="bb b8"></i></div>',
 "art_css":""".liquid{position:absolute;inset:0;background:linear-gradient(#0e3a5c,#081f38);overflow:hidden}
.bb{position:absolute;bottom:-34px;border-radius:50%;
background:radial-gradient(circle at 32% 30%,rgba(255,255,255,.85),rgba(140,220,255,.12) 65%);
border:1px solid rgba(160,220,255,.35);animation:rise 6s linear infinite}
.b1{left:24px;width:34px;height:34px;animation-delay:-1s}
.b2{left:80px;width:18px;height:18px;animation-delay:-3.4s}
.b3{left:130px;width:44px;height:44px;animation-delay:-5s}
.b4{left:190px;width:22px;height:22px;animation-delay:-2.2s}
.b5{left:240px;width:30px;height:30px;animation-delay:-4.4s}
.b6{left:290px;width:15px;height:15px;animation-delay:-.6s}
.b7{left:160px;width:12px;height:12px;animation-delay:-5.6s}
.b8{left:55px;width:20px;height:20px;animation-delay:-2.8s}
@keyframes rise{0%{transform:translateY(0)}100%{transform:translateY(-200px)}}"""},

# u31 礼花绽放
{"file":"u31.html","title":"礼花绽放","card":LIGHT,"accent":"#ff5c8a",
 "logs":["庆祝！全新版本登场","新增节日限定主题","分享功能更好玩"],
 "art_html":'<div class="party"><div class="pop"></div><i class="cf f1"></i><i class="cf f2"></i><i class="cf f3"></i><i class="cf f4"></i><i class="cf f5"></i><i class="cf f6"></i><i class="cf f7"></i><i class="cf f8"></i><i class="cf f9"></i><i class="cf f10"></i></div>',
 "art_css":""".art{background:linear-gradient(#2b1e3e,#4a2a5e)}
.party{position:relative;height:150px;overflow:hidden}
.pop{position:absolute;left:50%;bottom:6px;width:0;height:0;margin-left:-22px;
border-left:22px solid transparent;border-right:22px solid transparent;border-bottom:44px solid #ffd479}
.cf{position:absolute;top:-16px;width:9px;height:13px;border-radius:2px;animation:cfall 3.8s linear infinite}
.f1{left:12%;background:#ff5c8a;animation-delay:-.4s}.f2{left:24%;background:#ffd479;animation-delay:-1.8s}
.f3{left:36%;background:#5cc8ff;animation-delay:-2.9s}.f4{left:48%;background:#7be495;animation-delay:-1.1s}
.f5{left:60%;background:#b48cff;animation-delay:-3.3s}.f6{left:72%;background:#ff9d5c;animation-delay:-.9s}
.f7{left:84%;background:#ff5c8a;animation-delay:-2.2s}.f8{left:18%;background:#5cc8ff;animation-delay:-3.7s}
.f9{left:66%;background:#ffd479;animation-delay:-1.5s}.f10{left:90%;background:#7be495;animation-delay:-2.6s}
@keyframes cfall{to{transform:translateY(190px) rotate(560deg)}}"""},

# u32 声呐探测
{"file":"u32.html","title":"声呐探测","card":DARK,"accent":"#2ee68c",
 "logs":["新功能雷达扫描上线","附近的人更精准","隐私保护再升级"],
 "art_html":'<div class="radar"><div class="sweep"></div><i class="blip p1"></i><i class="blip p2"></i><i class="blip p3"></i><div class="ring g1"></div><div class="ring g2"></div></div>',
 "art_css":""".art{background:#04120c}
.radar{position:relative;width:150px;height:150px;margin:0 auto;border-radius:50%;overflow:hidden;
background:radial-gradient(circle,#06301f 0%,#02120c 72%);border:2px solid #1f7a52}
.sweep{position:absolute;inset:0;border-radius:50%;
background:conic-gradient(rgba(46,230,140,.75),transparent 80deg);animation:spin 3.2s linear infinite}
.ring{position:absolute;border:1px solid rgba(46,230,140,.35);border-radius:50%}
.ring.g1{inset:24px}.ring.g2{inset:50px}
.blip{position:absolute;width:9px;height:9px;border-radius:50%;background:#5cff9d;
box-shadow:0 0 10px #5cff9d;animation:blink 3.2s ease-out infinite}
.blip.p1{left:96px;top:44px}.blip.p2{left:52px;top:92px;animation-delay:-1.1s}
.blip.p3{left:100px;top:104px;animation-delay:-2.1s}
@keyframes blink{0%,15%{opacity:1;transform:scale(1.4)}60%,100%{opacity:.15;transform:scale(.8)}}"""},

# u33 凤凰涅槃
{"file":"u33.html","title":"凤凰涅槃","card":DARK,"accent":"#ff9d5c",
 "logs":["浴火重生，全面焕新","旧数据一键迁移","性能涅槃提升 2 倍"],
 "art_html":'<div class="fire"><div class="fl f1"></div><div class="fl f2"></div><div class="fl f3"></div><i class="emb e1"></i><i class="emb e2"></i><i class="emb e3"></i><i class="emb e4"></i></div>',
 "art_css":""".art{background:linear-gradient(#1c0d08,#3a1408)}
.fire{position:relative;height:150px;overflow:hidden}
.fl{position:absolute;bottom:8px;left:50%;transform-origin:bottom center;
border-radius:50% 50% 46% 46%/64% 64% 36% 36%;animation:flick 1.1s ease-in-out infinite alternate}
.f1{width:78px;height:96px;margin-left:-39px;background:linear-gradient(#ff7a3c,#e8380c)}
.f2{width:54px;height:68px;margin-left:-27px;background:linear-gradient(#ffcf6b,#ff7a3c);animation-delay:-.4s}
.f3{width:32px;height:42px;margin-left:-16px;background:linear-gradient(#fff6d8,#ffcf6b);animation-delay:-.8s}
@keyframes flick{from{transform:translateX(-50%) scaleY(1) skewX(0deg)}to{transform:translateX(-50%) scaleY(1.14) skewX(5deg)}}
.emb{position:absolute;bottom:20px;left:50%;width:7px;height:7px;border-radius:50%;
background:radial-gradient(#ffe29a,#ff7a3c);animation:erupt 2.4s ease-out infinite}
.e1{animation-delay:-.3s;margin-left:-24px}.e2{animation-delay:-1.1s;margin-left:18px}
.e3{animation-delay:-1.8s;margin-left:-6px}.e4{animation-delay:-.7s;margin-left:30px}
@keyframes erupt{0%{transform:translateY(0);opacity:1}100%{transform:translateY(-90px);opacity:0}}"""},

# u34 风车悠转
{"file":"u34.html","title":"风车悠转","card":LIGHT,"accent":"#7ab8ff",
 "logs":["清新田园风主题","新增慢生活小组件","耗电优化更持久"],
 "art_html":'<div class="mill"><div class="blades"><i class="bd b1"></i><i class="bd b2"></i><i class="bd b3"></i><i class="bd b4"></i><div class="hub2"></div></div><div class="mtow"></div><div class="hill"></div></div>',
 "art_css":""".art{background:linear-gradient(#aee2ff,#e3f4ff)}
.mill{position:relative;height:150px;overflow:hidden}
.mtow{position:absolute;left:50%;bottom:18px;width:30px;height:96px;margin-left:-15px;
background:linear-gradient(90deg,#a37c50,#c49a68);clip-path:polygon(32% 0,68% 0,100% 100%,0 100%)}
.blades{position:absolute;left:50%;top:2px;width:104px;height:104px;margin-left:-52px;animation:spin 8s linear infinite}
.bd{position:absolute;left:49px;top:2px;width:7px;height:50px;border-radius:4px;background:#fdf6e8;
transform-origin:3.5px 50px;box-shadow:0 2px 6px rgba(0,0,0,.12)}
.bd.b2{transform:rotate(90deg)}.bd.b3{transform:rotate(180deg)}.bd.b4{transform:rotate(270deg)}
.hub2{position:absolute;left:50%;top:50%;width:14px;height:14px;margin:-7px;border-radius:50%;background:#e8632c}
.hill{position:absolute;left:-20px;right:-20px;bottom:0;height:34px;border-radius:50% 50% 0 0;background:#8fd694}"""},

# u35 套娃层叠
{"file":"u35.html","title":"套娃层叠","card":LIGHT,"accent":"#e86a6a",
 "logs":["层层惊喜等你开","新增盲盒抽奖玩法","会员权益再加码"],
 "art_html":'<div class="dolls"><div class="doll d1"></div><div class="doll d2"></div><div class="doll d3"></div></div>',
 "art_css":""".art{background:linear-gradient(#fff0e8,#ffe0d2)}
.dolls{display:flex;align-items:flex-end;justify-content:center;gap:14px;height:150px;padding-bottom:18px}
.doll{border-radius:48% 48% 46% 46%/60% 60% 40% 40%;position:relative;animation:hpop .6s cubic-bezier(.2,.9,.3,1.4) both}
.doll::before{content:"";position:absolute;left:50%;top:26%;width:8px;height:8px;margin-left:-14px;border-radius:50%;
background:#3a2a24;box-shadow:20px 0 0 #3a2a24}
.doll::after{content:"";position:absolute;left:12%;right:12%;top:52%;height:10px;border-radius:6px;background:rgba(255,255,255,.55)}
.d1{width:72px;height:96px;background:linear-gradient(#f07878,#d94f4f)}
.d2{width:58px;height:78px;background:linear-gradient(#ffd873,#f0b73a);animation-delay:.18s}
.d2::before{margin-left:-12px;box-shadow:16px 0 0 #3a2a24;width:7px;height:7px}
.d3{width:44px;height:60px;background:linear-gradient(#9bdc8b,#6fb85f);animation-delay:.36s}
.d3::before{margin-left:-10px;box-shadow:13px 0 0 #3a2a24;width:6px;height:6px}
@keyframes hpop{from{transform:scale(0) translateY(30px)}to{transform:scale(1) translateY(0)}}"""},

# u36 翻牌时刻
{"file":"u36.html","title":"翻牌时刻","card":DARK,"accent":"#ffd479",
 "logs":["翻开新版本新惊喜","新增卡牌收集玩法","每日翻牌赢好礼"],
 "art_html":'<div class="flipwrap"><div class="flipcard"><div class="face front">?</div><div class="face back">NEW</div></div></div>',
 "art_css":""".art{background:linear-gradient(#141b33,#232c52)}
.flipwrap{height:150px;display:flex;align-items:center;justify-content:center;perspective:600px}
.flipcard{position:relative;width:104px;height:142px;transform-style:preserve-3d;animation:flipY 3.6s ease-in-out infinite}
@keyframes flipY{0%,12%{transform:rotateY(0)}48%,62%{transform:rotateY(180deg)}88%,100%{transform:rotateY(360deg)}}
.face{position:absolute;inset:0;border-radius:16px;display:flex;align-items:center;justify-content:center;
backface-visibility:hidden;-webkit-backface-visibility:hidden}
.front{background:linear-gradient(150deg,#2b3a55,#1a2340);color:#ffd479;font-size:44px;font-weight:800;
border:2px solid rgba(255,212,121,.4)}
.back{background:linear-gradient(135deg,#ffd479,#ff9d5c);color:#4a2c08;font-size:26px;font-weight:800;
transform:rotateY(180deg);letter-spacing:2px}"""},
]


ALL = CONCEPTS + CONCEPTS2
assert len(ALL) == 18, len(ALL)

titles = []
for c in ALL:
    card_css = c["card"]
    html = ("<!DOCTYPE html><html lang=\"zh-CN\"><head><meta charset=\"utf-8\">"
        "<meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">"
        "<title>版本更新 · " + c["title"] + "</title><style>" + BASE_CSS + card_css + c["art_css"] +
        "\n.go{background:linear-gradient(135deg," + c["accent"] + "," + c["accent"] + "cc);"
        "box-shadow:0 8px 20px " + c["accent"] + "66}"
        "\n.log li::before{background:" + c["accent"] + "}"
        "\n.prog i{background:linear-gradient(90deg," + c["accent"] + "," + c["accent"] + "aa)}"
        "</style></head><body><div class=\"phone\">"
        "<div class=\"mock\"><div class=\"status\"></div>"
        "<div class=\"apphead\"><div class=\"logo\"></div><div class=\"apptitle\">灵犀笔记</div></div>"
        "<div class=\"sk\"><i class=\"w80\"></i><i></i><i class=\"w60\"></i></div>"
        "<div class=\"sk\"><i class=\"w60\"></i><i class=\"w80\"></i></div>"
        "<div class=\"sk\"><i></i><i class=\"w60\"></i></div>"
        "<div class=\"tabbar\"><i class=\"on\"></i><i></i><i></i><i></i></div></div>"
        "<div class=\"mask\"></div>"
        "<div class=\"modal\"><div class=\"art\">" + c["art_html"] + "</div>"
        "<div class=\"ver\">v4.1.0 &nbsp;→&nbsp; <b>v4.2.0</b></div>"
        "<h2>" + c["title"] + "</h2><ul class=\"log\">" +
        "".join("<li>" + l + "</li>" for l in c["logs"]) +
        "</ul><div class=\"prog\"><i></i></div>"
        "<div class=\"btns\"><button class=\"later\">稍后再说</button>"
        "<button class=\"go\">立即更新</button></div></div>"
        "<button class=\"reopen\">↻ 重新弹出更新</button>"
        "</div><script>" + SHARED_JS + "</script></body></html>")
    open(os.path.join(OUT, c["file"]), "w", encoding="utf-8").write(html)
    titles.append({"file": c["file"], "title": c["title"]})

open(os.path.join(OUT, "_titles_update_b.json"), "w", encoding="utf-8").write(
    json.dumps(titles, ensure_ascii=False, indent=1))
print("wrote", len(ALL), "files")
print([t["title"] for t in titles])
