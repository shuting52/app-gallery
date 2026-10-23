#!/usr/bin/env python3
# chunk3: w13-w18 + 落盘。用法: python3 build_a3.py
import os, json

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "build_a.py")
src = open(SRC, encoding="utf-8").read()
ns = {"__name__": "__build__", "__file__": SRC}
exec(src, ns)
ITEMS = ns["ITEMS"]; HEAD = ns["HEAD"]; OUT = ns["OUT"]

# ============ w13 寿星礼 ============
ITEMS.append(dict(
 file="w13.html", title="寿星礼", pbg="linear-gradient(160deg,#1c1026,#0e0912)",
 mock=ns["MOCK_HOME"], enter="ePop",
 mcss="background:linear-gradient(165deg,#33203f,#1d1226);--ac:#ff9a6a;--ds:#d8bce8;--tc:#fff;border:1px solid rgba(255,154,106,.35);overflow:hidden",
 html="""<div class="cake"><div class="flame"></div><div class="candle"></div><div class="l3"></div><div class="l2"></div><div class="l1"></div></div>
<h2 class="tt">生日快乐</h2><p class="ds">听说今天是你的生日<br>一份蛋糕券 + 神秘礼物已备好</p>
<button class="btn" id="go">许个愿 · 领礼物</button><button class="ghost" id="no">不是今天</button>
<span class="cf f1"></span><span class="cf f2"></span><span class="cf f3"></span><span class="cf f4"></span><span class="cf f5"></span>""",
 css=""".cake{width:150px;margin:0 auto;position:relative;padding-top:44px}
.candle{width:12px;height:40px;margin:0 auto;background:repeating-linear-gradient(45deg,#ff6a9a,#ff6a9a 6px,#fff 6px,#fff 12px);border-radius:4px;position:relative;z-index:2}
.flame{width:18px;height:26px;margin:0 auto 2px;background:radial-gradient(circle at 50% 75%,#fff8d0 0 22%,#ffc93c 40%,#ff7a2b 70%,transparent 72%);border-radius:50% 50% 50% 50%/60% 60% 40% 40%;transform-origin:50% 100%;animation:flick .5s ease-in-out infinite alternate;position:relative;z-index:3}
@keyframes flick{from{transform:scale(1) rotate(-4deg)}to{transform:scale(1.12,1.2) rotate(4deg)}}
.l3,.l2,.l1{border-radius:10px;margin:0 auto;position:relative}
.l3{width:70px;height:26px;background:linear-gradient(180deg,#ff9ac8,#e05e9a);z-index:1}
.l2{width:104px;height:30px;background:linear-gradient(180deg,#c8a2ff,#9a6ae0);margin-top:-6px}
.l1{width:138px;height:34px;background:linear-gradient(180deg,#8fd0ff,#4a8fe0);margin-top:-6px}
.cf{display:block;position:absolute;top:-16px;width:10px;height:14px;border-radius:2px;animation:fall 3s linear infinite;opacity:.9}
.f1{left:8%;background:#ff6a9a;animation-delay:-0.4s}.f2{left:26%;background:#ffd479;animation-delay:-1.6s}
.f3{left:52%;background:#5ec8ff;animation-delay:-2.4s}.f4{left:74%;background:#b06aff;animation-delay:-1s}
.f5{left:90%;background:#3ddc84;animation-delay:-2s}
@keyframes fall{0%{transform:translateY(0) rotate(0)}100%{transform:translateY(420px) rotate(340deg)}}""",
 js="""document.getElementById('go').onclick=function(){this.textContent='愿望收到 ✓ 礼物已发放';this.classList.add('off')};
document.getElementById('no').onclick=function(){ov.classList.add('hide')};"""))

# ============ w14 一分钟 ============
ITEMS.append(dict(
 file="w14.html", title="一分钟", pbg="linear-gradient(160deg,#12141f,#0a0b10)",
 mock=ns["MOCK_SOCIAL"], enter="eUp",
 mcss="background:linear-gradient(165deg,#1e2233,#141724);--ac:#7ab8ff;--ds:#a9b4cc;--tc:#fff;border:1px solid rgba(122,184,255,.25)",
 html="""<div class="qmark">?</div>
<h2 class="tt">一分钟小调研</h2><p class="ds">你是从哪里知道我们的？<br>帮我们做得更好</p>
<div class="opts">
<div class="opt" data-v="朋友推荐">朋友推荐</div>
<div class="opt" data-v="短视频">短视频</div>
<div class="opt" data-v="应用商店">应用商店</div>
<div class="opt" data-v="偶然发现">偶然发现</div>
</div>
<button class="btn off" id="go">提交</button><button class="ghost" id="no">跳过</button>""",
 css=""".qmark{width:72px;height:72px;margin:0 auto;border-radius:50%;background:linear-gradient(135deg,#7ab8ff,#3a5fd0);font-size:38px;font-weight:900;line-height:72px;color:#fff;box-shadow:0 8px 24px rgba(122,184,255,.4);animation:wob2 2.8s ease-in-out infinite}
@keyframes wob2{0%,100%{transform:rotate(-6deg)}50%{transform:rotate(6deg)}}
.opts{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:14px}
.opt{border:1px solid rgba(255,255,255,.16);border-radius:12px;padding:13px 6px;font-size:14px;cursor:pointer;transition:all .22s;color:var(--ds)}
.opt.on{border-color:#7ab8ff;background:rgba(122,184,255,.14);color:#fff;box-shadow:0 0 14px rgba(122,184,255,.25)}""",
 js="""var go=document.getElementById('go'),opts=document.querySelectorAll('.opt');
opts.forEach(function(o){o.onclick=function(){opts.forEach(function(x){x.classList.remove('on')});o.classList.add('on');go.classList.remove('off')}});
go.onclick=function(){var v=document.querySelector('.opt.on').dataset.v;this.textContent='感谢参与 · '+v+' ✓';this.classList.add('off')};
document.getElementById('no').onclick=function(){ov.classList.add('hide')};"""))

# ============ w15 指上舞 ============
ITEMS.append(dict(
 file="w15.html", title="指上舞", pbg="linear-gradient(160deg,#101a1e,#0a1013)",
 mock=ns["MOCK_SOCIAL"], enter="eLeft",
 mcss="background:linear-gradient(165deg,#16262c,#0e1a1f);--ac:#3ddc84;--ds:#a8d4c2;--tc:#f2fff8;border:1px solid rgba(61,220,132,.3)",
 html="""<div class="gtrack"><div class="gcard">‹</div><div class="gcard mid">●</div><div class="gcard">›</div><div class="finger"></div></div>
<h2 class="tt">手势小教学</h2><p class="ds">左右滑动卡片，快速切换内容<br>试着跟手指一起动起来</p>
<button class="btn" id="go">我知道了</button>""",
 css=""".gtrack{position:relative;height:120px;margin:6px 0 2px}
.gcard{position:absolute;top:14px;width:76px;height:92px;border-radius:14px;background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.14);font-size:30px;line-height:92px;color:#3ddc84}
.gcard.mid{left:50%;transform:translateX(-50%);background:rgba(61,220,132,.14);border-color:#3ddc84}
.gcard:first-child{left:18px}.gcard:last-of-type{right:18px}
.finger{position:absolute;top:64px;left:50%;width:34px;height:34px;margin-left:-17px;border-radius:50%;background:radial-gradient(circle at 35% 30%,rgba(255,255,255,.85),rgba(255,255,255,.25));border:2px solid #3ddc84;box-shadow:0 0 18px rgba(61,220,132,.6);animation:swipe 2.4s ease-in-out infinite;z-index:2}
@keyframes swipe{0%,100%{transform:translateX(-72px)}50%{transform:translateX(72px)}}""",
 js="""document.getElementById('go').onclick=function(){ov.classList.add('hide')};"""))

# ============ w16 铃先知 ============
ITEMS.append(dict(
 file="w16.html", title="铃先知", pbg="linear-gradient(160deg,#1a1410,#100c08)",
 mock=ns["MOCK_HOME"], enter="eDrop",
 mcss="background:linear-gradient(165deg,#2c2118,#1a140e);--ac:#f6c453;--ds:#d8c8a4;--tc:#fff4dd;border:1px solid rgba(246,196,83,.3)",
 html="""<div class="bellwrap"><div class="bell">🔔</div><span class="wave w1"></span><span class="wave w2"></span></div>
<h2 class="tt">不错过每条消息</h2><p class="ds">开启通知，好友消息、订单动态<br>第一时间送达</p>
<div class="prow"><span>🔔 新消息通知</span><span class="sw on" id="sw"><i></i></span></div>
<button class="btn" id="go">开启通知</button><button class="ghost" id="no">保持安静</button>""",
 css=""".bellwrap{position:relative;width:110px;height:110px;margin:0 auto}
.bell{font-size:64px;line-height:110px;transform-origin:50% 12%;animation:ring 1.8s ease-in-out infinite}
@keyframes ring{0%,100%{transform:rotate(0)}12%{transform:rotate(16deg)}24%{transform:rotate(-13deg)}36%{transform:rotate(9deg)}48%{transform:rotate(-6deg)}60%{transform:rotate(0)}}
.wave{display:block;position:absolute;top:50%;left:50%;width:90px;height:90px;margin:-45px 0 0 -45px;border-radius:50%;border:2px solid #f6c453;opacity:0;animation:wv 1.8s ease-out infinite}
.w2{animation-delay:-0.9s}
@keyframes wv{0%{transform:scale(.5);opacity:.8}100%{transform:scale(1.35);opacity:0}}
.prow{display:flex;justify-content:space-between;align-items:center;background:rgba(255,255,255,.05);border-radius:12px;padding:11px 14px;margin-top:14px;font-size:14px}
.sw{position:relative;display:inline-block;width:48px;height:28px;border-radius:14px;background:rgba(255,255,255,.16);cursor:pointer;transition:background .25s;flex-shrink:0}
.sw i{display:block;position:absolute;top:3px;left:3px;width:22px;height:22px;border-radius:50%;background:#fff;transition:left .25s}
.sw.on{background:#f6c453}.sw.on i{left:23px}""",
 js="""var sw=document.getElementById('sw');
sw.onclick=function(){sw.classList.toggle('on')};
document.getElementById('go').onclick=function(){sw.classList.add('on');this.textContent='通知已开启 ✓';this.classList.add('off')};
document.getElementById('no').onclick=function(){ov.classList.add('hide')};"""))

# ============ w17 钱袋开 ============
ITEMS.append(dict(
 file="w17.html", title="钱袋开", pbg="linear-gradient(160deg,#101826,#080b10)",
 mock=ns["MOCK_SHOP"], enter="eFlip",
 mcss="background:transparent;box-shadow:none;padding:28px 8px 22px;--ac:#5ec8ff;--ds:#a9c4dc",
 html="""<div class="flip" id="flip"><div class="face front"><div class="chip"></div><div class="fno">6228 •••• •••• 0000</div><div class="fnm">零钱钱包 · 待激活</div></div>
<div class="face back"><div class="stripe"></div><div class="ok">✓ 已开通</div></div></div>
<h2 class="tt" style="color:#fff">开通零钱钱包</h2><p class="ds" style="color:#a9c4dc">红包、返现自动入账<br>提现免手续费 · 实时到账</p>
<button class="btn" id="go" style="background:#5ec8ff">立即开通</button><button class="ghost" id="no" style="color:#8b94a3">暂不开通</button>""",
 css=""".flip{position:relative;width:308px;height:180px;margin:0 auto 6px;perspective:800px}
.face{position:absolute;inset:0;border-radius:18px;backface-visibility:hidden;-webkit-backface-visibility:hidden;transition:transform .7s cubic-bezier(.3,.8,.3,1);overflow:hidden}
.front{background:linear-gradient(120deg,#1d3a5f,#0f2240 60%,#14324e);border:1px solid rgba(94,200,255,.4);padding:20px;text-align:left;box-shadow:0 16px 40px rgba(0,0,0,.45)}
.chip{width:46px;height:34px;border-radius:7px;background:linear-gradient(135deg,#ffe9a8,#d8a93c);margin-bottom:26px}
.fno{font-size:16px;letter-spacing:3px;color:#cfe6ff}.fnm{font-size:12px;color:#7ab8ff;margin-top:8px}
.back{background:linear-gradient(120deg,#123a2a,#0c2a1f);border:1px solid rgba(61,220,132,.5);transform:rotateY(180deg);display:flex;flex-direction:column;align-items:center;justify-content:center}
.stripe{width:100%;height:40px;background:#0a0d12;margin-bottom:16px}
.ok{font-size:22px;color:#3ddc84;font-weight:800}
.flip.done .front{transform:rotateY(180deg)}.flip.done .back{transform:rotateY(360deg)}""",
 js="""document.getElementById('go').onclick=function(){document.getElementById('flip').classList.add('done');this.textContent='钱包已开通 ✓';this.classList.add('off')};
document.getElementById('no').onclick=function(){ov.classList.add('hide')};"""))

# ============ w18 约在先 ============
ITEMS.append(dict(
 file="w18.html", title="约在先", pbg="linear-gradient(160deg,#141a16,#0a0d0b)",
 mock=ns["MOCK_SOCIAL"], enter="eBlur",
 mcss="background:linear-gradient(165deg,#1c2620,#121915);--ac:#3ddc84;--ds:#b8d4c2;--tc:#f2fff8;border:1px solid rgba(61,220,132,.3)",
 html="""<div class="doc">📜</div>
<h2 class="tt">社区公约</h2><p class="ds">欢迎来到友善社区<br>请先阅读并同意以下约定</p>
<div class="rules">
<b>一、</b>友善交流，不发表攻击、侮辱性言论。<br><br>
<b>二、</b>不发布广告、色情、暴力等违规内容。<br><br>
<b>三、</b>尊重原创，转载请注明出处。<br><br>
<b>四、</b>不泄露他人隐私信息。<br><br>
<b>五、</b>违规三次将限制发言，严重者封禁。
</div>
<label class="agree"><span class="box" id="box"><i>✓</i></span>我已阅读并同意《社区公约》</label>
<button class="btn off" id="go">进入社区</button>""",
 css=""".doc{font-size:56px;animation:float2 2.6s ease-in-out infinite}
@keyframes float2{0%,100%{transform:translateY(0)}50%{transform:translateY(-8px)}}
.rules{max-height:150px;overflow-y:auto;text-align:left;font-size:13px;line-height:1.7;color:var(--ds);background:rgba(255,255,255,.05);border-radius:12px;padding:14px;margin-top:12px}
.rules b{color:#3ddc84}
.agree{display:flex;align-items:center;gap:10px;font-size:13px;color:var(--ds);margin-top:14px;cursor:pointer;text-align:left}
.box{display:inline-block;position:relative;width:24px;height:24px;border-radius:7px;border:2px solid rgba(255,255,255,.3);flex-shrink:0;transition:all .25s}
.box i{display:none;position:absolute;inset:0;font-style:normal;color:#062a18;font-weight:900;font-size:15px;line-height:20px;text-align:center}
.box.on{background:#3ddc84;border-color:#3ddc84}.box.on i{display:block}""",
 js="""var box=document.getElementById('box'),go=document.getElementById('go');
box.parentElement.onclick=function(){box.classList.toggle('on');go.classList.toggle('off',!box.classList.contains('on'))};
go.onclick=function(){ov.classList.add('hide')};"""))

# ---- 落盘 ----
for it in ITEMS:
    page = HEAD
    for k, tok in [("file",""),("title","%%TITLE%%"),("pbg","%%PBG%%"),("mock","%%MOCK%%"),
                   ("enter","%%ENTER%%"),("mcss","%%MCSS%%"),("html","%%MODAL_HTML%%"),
                   ("css","%%EXTRA_CSS%%"),("js","%%EXTRA_JS%%")]:
        if tok:
            page = page.replace(tok, it[k])
    open(os.path.join(OUT, it["file"]), "w", encoding="utf-8").write(page)

titles = [{"file": it["file"], "title": it["title"]} for it in ITEMS]
open(os.path.join(OUT, "_titles_welcome_a.json"), "w", encoding="utf-8").write(
    json.dumps(titles, ensure_ascii=False, indent=1))
print("files:", len(ITEMS))
print("titles:", [t["title"] for t in titles])
print("unique:", len(set(t["title"] for t in titles)) == len(titles))
