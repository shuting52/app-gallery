# 生成 n61-n70 液态玻璃通知卡（系统通知方向），照 template.html 骨架
import os, json

def css_for(bg, bd, cbg, blur, hla, spot, rot, fg, pri):
    return f"""*{{
box-sizing: border-box;
}}
body {{
min-height: 100vh;
margin: 0;
padding: 48px 18px;
color: #fff;
font: 15px/1.45 -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
background: {bg};
background-attachment: fixed;
}}
main {{
width: min(440px, 100%);
margin: 0 auto;
display: grid;
gap: 18px;
}}
.heading {{ padding: 4px 6px 8px;}}
.eyebrow {{
margin: 0 0 8px;
color: rgba(255,255,255,.68);
font-size: 11px;
letter-spacing:.18em;
}}
h1 {{ margin: 0; font-size: 30px; letter-spacing: -.04em;}}
.hint {{ margin: 7px 0 0; color: rgba(255,255,255,.68);}}
.card {{
position: relative;
isolation: isolate;
overflow: hidden;
padding: 18px;
border: 1px solid {bd};
border-radius: 28px;
background: linear-gradient(135deg, {cbg});
-webkit-backdrop-filter: blur({blur}) saturate(175%);
backdrop-filter: blur({blur}) saturate(175%);
box-shadow:
inset 0 1px 0 rgba(255,255,255,.42),
inset 0 -1px 0 rgba(255,255,255,.08),
0 20px 48px rgba(8,8,24,.28);
transition: transform.25s ease, border-color.25s ease;
}}
.card::before {{
content: "";
position: absolute;
z-index: 0;
inset: 0;
border-radius: inherit;
pointer-events: none;
background:
linear-gradient({hla},
rgba(255,255,255,.34) 0%,
rgba(255,255,255,.08) 18%,
transparent 42%,
transparent 72%,
rgba(255,206,234,.16) 100%);
opacity:.8;
}}
.card::after {{
content: "";
position: absolute;
z-index: 0;
{spot}
width: 190px;
height: 130px;
border: 1px solid rgba(255,255,255,.22);
border-radius: 50%;
background: radial-gradient(ellipse, rgba(255,255,255,.22), transparent 68%);
filter: blur(2px);
transform: rotate({rot});
pointer-events: none;
}}
.card > * {{ position: relative; z-index: 1;}}
.card:hover {{ transform: translateY(-3px); border-color: rgba(255,255,255,.46);}}
.top,.title-line {{
display: flex;
align-items: center;
justify-content: space-between;
gap: 12px;
}}
.top {{ margin-bottom: 15px;}}
.pill {{
padding: 6px 12px;
border: 1px solid rgba(255,255,255,.30);
border-radius: 999px;
background: rgba(255,255,255,.10);
color: rgba(255,255,255,.94);
font-size: 12px;
box-shadow: inset 0 1px rgba(255,255,255,.18);
}}
.dot {{
flex: 0 0 auto;
width: 10px;
height: 10px;
border-radius: 50%;
background: #fff;
box-shadow: 0 0 12px rgba(255,255,255,.9);
animation: blk 1.6s ease-in-out infinite;
animation-delay: -.8s;
}}
@keyframes blk {{ 50% {{ transform: scale(1.45);}}}}
.row {{ display: flex; align-items: center; gap: 12px; min-width: 0;}}
.face {{
display: grid;
flex: 0 0 48px;
height: 48px;
place-items: center;
border: 1px solid rgba(255,255,255,.45);
border-radius: 16px;
background: {fg};
color: #fff;
font-size: 22px;
font-weight: 650;
box-shadow: inset 0 1px 5px rgba(255,255,255,.5), 0 5px 15px rgba(15,12,35,.2);
}}
.copy {{ flex: 1; min-width: 0;}}
.title-line {{ margin-bottom: 5px;}}
.title-line strong {{ overflow: hidden; text-overflow: ellipsis; white-space: nowrap;}}
time,.preview {{ color: rgba(255,255,255,.72); font-size: 12px;}}
.preview {{ overflow: hidden; text-overflow: ellipsis; white-space: nowrap;}}
.unread {{ flex: 0 0 auto; color: #d8d2ff; font-size: 12px; font-weight: 600;}}
.actions {{ display: flex; gap: 10px; margin-top: 14px;}}
.btn {{
flex: 1;
padding: 10px 0;
border-radius: 14px;
border: 1px solid rgba(255,255,255,.30);
background: rgba(255,255,255,.12);
color: #fff;
font-size: 13px;
text-align: center;
cursor: pointer;
}}
.btn.pri {{ background: {pri}; border-color: transparent; font-weight: 700;}}
.bar {{
height: 8px;
border-radius: 5px;
background: rgba(255,255,255,.16);
margin-top: 12px;
overflow: hidden;
}}
.bar i {{
display: block;
height: 100%;
border-radius: 5px;
background: {pri};
animation: fill 1.2s ease both;
}}
@keyframes fill {{ from {{ width: 0!important;}}}}
.meta {{
display: flex;
justify-content: space-between;
font-size: 12px;
color: rgba(255,255,255,.72);
margin-top: 6px;
}}
.code {{
font-size: 34px;
font-weight: 800;
letter-spacing:.28em;
margin: 6px 0 2px;
text-align: center;
text-indent:.28em;
text-shadow: 0 2px 18px rgba(255,255,255,.25);
}}
.sw {{
flex: 0 0 auto;
position: relative;
display: block;
width: 52px;
height: 30px;
border-radius: 16px;
background: #34c759;
cursor: pointer;
}}
.sw i {{
position: absolute;
top: 3px;
left: 25px;
display: block;
width: 24px;
height: 24px;
border-radius: 50%;
background: #fff;
box-shadow: 0 2px 6px rgba(0,0,0,.3);
}}
.stats {{ display: flex; gap: 10px; margin-top: 12px;}}
.stat {{
flex: 1;
text-align: center;
padding: 10px 4px;
border-radius: 14px;
background: rgba(255,255,255,.08);
border: 1px solid rgba(255,255,255,.14);
}}
.stat b {{ display: block; font-size: 17px;}}
.stat span {{ font-size: 11px; color: rgba(255,255,255,.65);}}
@supports not ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {{
.card {{ background: rgba(43,35,68,.88);}}
}}
@media (prefers-reduced-motion: reduce) {{
.card {{ transition: none;}}
.bar i {{ animation: none;}}
.dot {{ animation: none;}}
}}
"""

PAGE_TMPL = """<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<style>
{css}
</style>
</head>
<body>
<main>
<header class="heading">
<p class="eyebrow">{eb}</p>
<h1>{h1}</h1>
<p class="hint">{hint}</p>
</header>
{cards}
</main>
</body>
</html>
"""

def C(pill, body):
    return f'<section class="card"><div class="top"><span class="pill">{pill}</span><span class="dot"></span></div>{body}</section>'

def R(face, title, time, preview, unread=""):
    u = f'<span class="unread">{unread}</span>' if unread else ''
    return (f'<div class="row"><div class="face">{face}</div><div class="copy">'
    f'<div class="title-line"><strong>{title}</strong><time>{time}</time></div>'
    f'<div class="preview">{preview}</div></div>{u}</div>')

def bar(w):
    return f'<div class="bar"><i style="width:{w}"></i></div>'

def meta(a, b):
    return f'<div class="meta"><span>{a}</span><span>{b}</span></div>'

def acts(*btns):
    inner = "".join(f'<div class="btn{(" pri" if i == 0 else "")}">{b}</div>' for i, b in enumerate(btns))
    return f'<div class="actions">{inner}</div>'

def stats(items):
    inner = "".join(f'<div class="stat"><b>{b}</b><span>{s}</span></div>' for b, s in items)
    return f'<div class="stats">{inner}</div>'

PAGES = [
# n61 系统更新 · 深蓝
dict(f="n61.html", t="系统更新", eb="SYSTEM", h1="系统更新", hint="新版本已经准备好，随时可以出发。",
bg="radial-gradient(ellipse at 18% 16%, rgba(56,130,246,.9), transparent 36%),radial-gradient(ellipse at 84% 40%, rgba(34,197,235,.7), transparent 38%),radial-gradient(ellipse at 50% 90%, rgba(30,58,138,.85), transparent 40%),linear-gradient(150deg,#0b1c33,#0e2a52 55%,#0a1830)",
bd="rgba(140,200,255,.32)", cbg="rgba(255,255,255,.20),rgba(255,255,255,.08) 48%,rgba(120,180,255,.14)",
blur="26px", hla="120deg", spot="top:-58px;right:-42px;", rot="-20deg",
fg="linear-gradient(145deg,#60a5fa,#2563eb 60%,#1e3a8a)", pri="linear-gradient(135deg,#38bdf8,#2563eb)",
cards=[
C("系统", R("⬆", "iOS 27.4 可用", "09:12", "本次更新约 1.8 GB，建议连接 Wi-Fi") + bar("72%") + meta("正在准备更新…", "72%")),
C("系统", R("✓", "更新包已下载", "08:40", "今晚 02:00 自动安装，不打扰你") + acts("立即安装", "稍后提醒")),
]),
# n62 存储告急 · 琥珀橙
dict(f="n62.html", t="存储告急", eb="STORAGE", h1="存储空间", hint="手机快装不下了，腾点地方吧。",
bg="radial-gradient(ellipse at 20% 20%, rgba(251,146,60,.9), transparent 36%),radial-gradient(ellipse at 80% 30%, rgba(234,88,12,.75), transparent 38%),radial-gradient(ellipse at 55% 88%, rgba(120,53,15,.85), transparent 40%),linear-gradient(150deg,#2a1508,#3d1f0c 55%,#221006)",
bd="rgba(255,200,140,.34)", cbg="rgba(255,255,255,.20),rgba(255,255,255,.08) 48%,rgba(255,180,100,.13)",
blur="22px", hla="64deg", spot="bottom:-62px;left:-40px;", rot="24deg",
fg="linear-gradient(145deg,#fdba74,#f97316 60%,#9a3412)", pri="linear-gradient(135deg,#fbbf24,#f97316)",
cards=[
C("系统", R("🗄", "存储空间不足", "10:05", "还剩 1.2 GB，29.1 / 32 GB 已用") + bar("91%") + meta("照片 18.4 GB", "应用 7.9 GB") + acts("一键清理", "查看详情")),
C("系统", R("📦", "微信占用 6.8 GB", "昨天", "缓存占了大头，清理不删聊天记录") + acts("去清理", "忽略")),
]),
# n63 验证码 · 紫
dict(f="n63.html", t="验证码", eb="VERIFY", h1="验证码", hint="5 分钟内有效，别告诉别人。",
bg="radial-gradient(ellipse at 16% 22%, rgba(167,139,250,.9), transparent 36%),radial-gradient(ellipse at 82% 36%, rgba(129,80,250,.75), transparent 38%),radial-gradient(ellipse at 52% 88%, rgba(76,29,149,.85), transparent 40%),linear-gradient(150deg,#1e1340,#2c1a5e 55%,#170f38)",
bd="rgba(200,170,255,.34)", cbg="rgba(255,255,255,.20),rgba(255,255,255,.08) 48%,rgba(190,140,255,.13)",
blur="24px", hla="150deg", spot="top:-58px;left:-42px;", rot="18deg",
fg="linear-gradient(145deg,#c4b5fd,#8b5cf6 60%,#5b21b6)", pri="linear-gradient(135deg,#a78bfa,#7c3aed)",
cards=[
C("安全", R("🔑", "登录验证码", "刚刚", "482163，5 分钟内有效") + '<div class="code">482163</div>' + acts("复制验证码")),
C("安全", R("📱", "新设备登录提醒", "07:58", "你的账号在 MacBook Pro 上登录") + acts("是我本人", "不是我")),
]),
# n64 安全提醒 · 绯红
dict(f="n64.html", t="安全提醒", eb="SECURITY", h1="安全中心", hint="账户有点小动静，看一眼更安心。",
bg="radial-gradient(ellipse at 20% 18%, rgba(248,113,113,.9), transparent 36%),radial-gradient(ellipse at 80% 34%, rgba(190,30,60,.78), transparent 38%),radial-gradient(ellipse at 54% 88%, rgba(90,15,30,.88), transparent 40%),linear-gradient(150deg,#2b0d14,#451420 55%,#200a10)",
bd="rgba(255,150,150,.36)", cbg="rgba(255,255,255,.20),rgba(255,255,255,.08) 48%,rgba(255,130,130,.13)",
blur="26px", hla="100deg", spot="top:-52px;right:-38px;", rot="-32deg",
fg="linear-gradient(145deg,#fca5a5,#ef4444 60%,#991b1b)", pri="linear-gradient(135deg,#f87171,#dc2626)",
cards=[
C("风险", R("🛡", "检测到异地登录", "12:47", "广东 深圳，设备未知，如非本人请冻结", "紧急") + acts("冻结账号", "查看详情")),
C("风险", R("🔒", "密码已 180 天未更换", "09:00", "建议开启两步验证，提升账户安全") + acts("立即加固", "稍后")),
]),
# n65 备份完成 · 青绿
dict(f="n65.html", t="备份完成", eb="BACKUP", h1="云备份", hint="你的回忆，已经安稳上云。",
bg="radial-gradient(ellipse at 18% 20%, rgba(45,212,191,.85), transparent 36%),radial-gradient(ellipse at 82% 34%, rgba(20,160,160,.75), transparent 38%),radial-gradient(ellipse at 52% 88%, rgba(13,80,90,.88), transparent 40%),linear-gradient(150deg,#062a2c,#0a3d40 55%,#041e20)",
bd="rgba(140,240,220,.32)", cbg="rgba(255,255,255,.20),rgba(255,255,255,.08) 48%,rgba(110,230,200,.12)",
blur="24px", hla="80deg", spot="bottom:-60px;right:-40px;", rot="14deg",
fg="linear-gradient(145deg,#5eead4,#14b8a6 60%,#0f766e)", pri="linear-gradient(135deg,#2dd4bf,#0d9488)",
cards=[
C("系统", R("☁", "备份完成", "03:12", "2.4 GB 照片与备忘录已同步到云端") + stats([("2.4 GB", "本次备份"), ("12,480", "照片"), ("100%", "完成度")])),
C("系统", R("✓", "自动备份已开启", "昨天", "每周日凌晨自动备份，无需操心") + acts("管理备份")),
]),
# n66 新功能 · 品红紫
dict(f="n66.html", t="新功能", eb="WHAT'S NEW", h1="新功能", hint="刚上线的新玩意儿，第一个告诉你。",
bg="radial-gradient(ellipse at 18% 20%, rgba(244,114,182,.9), transparent 36%),radial-gradient(ellipse at 82% 36%, rgba(168,85,247,.78), transparent 38%),radial-gradient(ellipse at 52% 88%, rgba(90,30,140,.85), transparent 40%),linear-gradient(150deg,#2c1030,#421a4e 55%,#200c2c)",
bd="rgba(240,170,255,.34)", cbg="rgba(255,255,255,.20),rgba(255,255,255,.08) 48%,rgba(230,150,255,.13)",
blur="26px", hla="135deg", spot="top:-56px;right:-44px;", rot="-12deg",
fg="linear-gradient(145deg,#f9a8d4,#d946ef 60%,#86198f)", pri="linear-gradient(135deg,#e879f9,#a855f7)",
cards=[
C("上新", R("✨", "液态桌面来了", "刚刚", "图标会呼吸的桌面主题，免费体验 7 天", "NEW") + acts("去看看", "稍后再说")),
C("上新", R("🎙", "语音备忘录 2.0", "昨天", "自动转文字，还能一键生成摘要") + acts("立即体验")),
]),
# n67 电池健康 · 柠檬绿
dict(f="n67.html", t="电池健康", eb="BATTERY", h1="电池", hint="好好用电，手机陪你更久。",
bg="radial-gradient(ellipse at 18% 20%, rgba(132,204,22,.85), transparent 36%),radial-gradient(ellipse at 82% 34%, rgba(60,160,60,.75), transparent 38%),radial-gradient(ellipse at 54% 88%, rgba(25,70,30,.88), transparent 40%),linear-gradient(150deg,#0e2408,#16330c 55%,#0a1c06)",
bd="rgba(180,240,140,.32)", cbg="rgba(255,255,255,.20),rgba(255,255,255,.08) 48%,rgba(150,230,120,.12)",
blur="22px", hla="70deg", spot="bottom:-58px;left:-44px;", rot="-24deg",
fg="linear-gradient(145deg,#bef264,#65a30d 60%,#3f6212)", pri="linear-gradient(135deg,#a3e635,#4d7c0f)",
cards=[
C("系统", R("🔋", "电池最大容量 89%", "11:20", "峰值性能正常，暂不需要更换电池") + bar("82%") + meta("当前电量", "82%")),
C("系统", R("🌙", "优化充电已开启", "昨天", "学习你的作息，睡前充到 80% 就停") + acts("保持开启", "关闭")),
]),
# n68 网络切换 · 天青（带开关）
dict(f="n68.html", t="网络切换", eb="NETWORK", h1="网络", hint="信号满格，在线每一秒。",
bg="radial-gradient(ellipse at 20% 18%, rgba(34,211,238,.88), transparent 36%),radial-gradient(ellipse at 80% 36%, rgba(40,120,240,.75), transparent 38%),radial-gradient(ellipse at 52% 88%, rgba(20,60,140,.88), transparent 40%),linear-gradient(150deg,#081c30,#0c2c52 55%,#061423)",
bd="rgba(140,220,255,.34)", cbg="rgba(255,255,255,.20),rgba(255,255,255,.08) 48%,rgba(120,210,255,.13)",
blur="24px", hla="110deg", spot="top:-60px;left:-40px;", rot="28deg",
fg="linear-gradient(145deg,#67e8f9,#0ea5e9 60%,#0c4a6e)", pri="linear-gradient(135deg,#22d3ee,#0284c7)",
cards=[
C("网络", R("📶", "已切换到 5G", "刚刚", "China Mobile，信号良好，速率 486 Mbps") + stats([("486", "Mbps 下行"), ("52", "Mbps 上行"), ("18ms", "延迟")])),
'<section class="card"><div class="top"><span class="pill">网络</span><span class="sw"><i></i></span></div>'
'<div class="row"><div class="face">🛰</div><div class="copy">'
'<div class="title-line"><strong>自动切换网络</strong></div>'
'<div class="preview">Wi-Fi 信号弱时自动用流量补上</div></div></div></section>',
]),
# n69 定位权限 · 靛蓝
dict(f="n69.html", t="定位权限", eb="PRIVACY", h1="隐私", hint="你的位置，你做主。",
bg="radial-gradient(ellipse at 18% 22%, rgba(129,140,248,.88), transparent 36%),radial-gradient(ellipse at 82% 34%, rgba(90,100,220,.75), transparent 38%),radial-gradient(ellipse at 54% 88%, rgba(45,50,120,.88), transparent 40%),linear-gradient(150deg,#141736,#20265c 55%,#0e1030)",
bd="rgba(170,180,255,.32)", cbg="rgba(255,255,255,.20),rgba(255,255,255,.08) 48%,rgba(150,160,255,.12)",
blur="26px", hla="95deg", spot="bottom:-62px;right:-44px;", rot="-18deg",
fg="linear-gradient(145deg,#a5b4fc,#6366f1 60%,#3730a3)", pri="linear-gradient(135deg,#818cf8,#4f46e5)",
cards=[
C("隐私", R("📍", "3 个应用正在使用位置", "13:05", "地图、打车、外卖，均为“使用期间”权限") + acts("管理权限", "知道了")),
C("隐私", R("👁", "剪贴板访问提醒", "昨天", "输入法读取了剪贴板 1 次，已自动拦截") + acts("始终拦截", "查看记录")),
]),
# n70 崩溃报告 · slate+红
dict(f="n70.html", t="崩溃报告", eb="DIAGNOSTICS", h1="诊断", hint="闪退这事儿，我们记下了。",
bg="radial-gradient(ellipse at 20% 20%, rgba(120,130,150,.85), transparent 36%),radial-gradient(ellipse at 80% 34%, rgba(200,60,60,.7), transparent 38%),radial-gradient(ellipse at 54% 88%, rgba(60,20,25,.88), transparent 40%),linear-gradient(150deg,#1a1214,#2c181c 55%,#120c0e)",
bd="rgba(200,170,170,.30)", cbg="rgba(255,255,255,.20),rgba(255,255,255,.08) 48%,rgba(220,140,140,.11)",
blur="24px", hla="140deg", spot="top:-54px;right:-40px;", rot="22deg",
fg="linear-gradient(145deg,#c9a0a0,#a06060 60%,#5c3030)", pri="linear-gradient(135deg,#e08080,#b05050)",
cards=[
C("系统", R("🐞", "相册闪退了 2 次", "14:33", "已生成诊断日志，帮助我们修复问题") + acts("发送报告", "忽略")),
C("系统", R("🧹", "14 天未清理缓存", "昨天", "临时文件占用 1.1 GB，建议清理") + acts("立即清理", "稍后")),
]),
]

OUT = os.path.dirname(os.path.abspath(__file__))
for p in PAGES:
    css = css_for(p["bg"], p["bd"], p["cbg"], p["blur"], p["hla"], p["spot"], p["rot"], p["fg"], p["pri"])
    html = PAGE_TMPL.format(title=p["t"], css=css, eb=p["eb"], h1=p["h1"], hint=p["hint"],
    cards="\n".join(p["cards"]))
    with open(os.path.join(OUT, p["f"]), "w", encoding="utf-8") as fh:
        fh.write(html)
    print("wrote", p["f"], p["t"])

json.dump([{"file": p["f"], "title": p["t"]} for p in PAGES],
    open(os.path.join(OUT, "_titles_nc_g.json"), "w", encoding="utf-8"),
    ensure_ascii=False, indent=1)
print("titles ok")
