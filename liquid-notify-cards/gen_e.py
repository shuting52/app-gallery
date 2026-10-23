# n41-n50 支付金融 · 液态玻璃通知卡
import os

BASE_CSS = """*{{box-sizing:border-box}}
body{{min-height:100vh;margin:0;padding:48px 18px;color:#fff;
font:15px/1.45 -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
background:{bg};background-attachment:fixed}}
main{{{{width:min(440px,100%);margin:0 auto;display:grid;gap:18px}}}}
.heading{{{{padding:4px 6px 8px}}}}
.eyebrow{{{{margin:0 0 8px;color:rgba(255,255,255,.68);font-size:11px;letter-spacing:.18em}}}}
h1{{{{margin:0;font-size:30px;letter-spacing:-.04em}}}}
.hint{{{{margin:7px 0 0;color:rgba(255,255,255,.68)}}}}
.card{{{{position:relative;isolation:isolate;overflow:hidden;padding:18px;
border:1px solid {edge};border-radius:28px;
background:{glass};
-webkit-backdrop-filter:blur({blur}px) saturate(175%);
backdrop-filter:blur({blur}px) saturate(175%);
box-shadow:inset 0 1px 0 rgba(255,255,255,.42),inset 0 -1px 0 rgba(255,255,255,.08),0 20px 48px rgba(8,8,24,.28);
transition:transform .25s ease,border-color .25s ease}}}}
.card::before{{{{content:"";position:absolute;z-index:0;inset:0;border-radius:inherit;pointer-events:none;
background:linear-gradient({hldeg}deg,rgba(255,255,255,{hl1}) 0%,rgba(255,255,255,.08) 18%,transparent 42%,transparent 72%,{hltint} 100%);opacity:.8}}}}
.card::after{{{{content:"";position:absolute;z-index:0;{arcpos};
width:{arcw}px;height:{arch}px;border:1px solid rgba(255,255,255,.22);border-radius:50%;
background:radial-gradient(ellipse,rgba(255,255,255,.22),transparent 68%);
filter:blur(2px);transform:rotate({arcrot}deg);pointer-events:none}}}}
.card>*{{{{position:relative;z-index:1}}}}
.card:hover{{{{transform:translateY(-3px);border-color:rgba(255,255,255,.46)}}}}
.top,.title-line{{{{display:flex;align-items:center;justify-content:space-between;gap:12px}}}}
.top{{{{margin-bottom:17px}}}}
.pill{{{{padding:6px 12px;border:1px solid rgba(255,255,255,.30);border-radius:999px;background:rgba(255,255,255,.10);color:rgba(255,255,255,.94);font-size:12px;box-shadow:inset 0 1px rgba(255,255,255,.18)}}}}
.row{{{{display:flex;align-items:center;gap:12px;min-width:0}}}}
.face{{{{display:grid;flex:0 0 48px;height:48px;place-items:center;border:1px solid rgba(255,255,255,.45);border-radius:50%;background:{face};color:#fff;font-size:19px;font-weight:650;box-shadow:inset 0 1px 5px rgba(255,255,255,.5),0 5px 15px rgba(15,12,35,.2)}}}}
.copy{{{{flex:1;min-width:0}}}}
.title-line{{{{margin-bottom:5px}}}}
.title-line strong{{{{overflow:hidden;text-overflow:ellipsis;white-space:nowrap}}}}
time,.preview{{{{color:rgba(255,255,255,.72);font-size:12px}}}}
.preview{{{{overflow:hidden;text-overflow:ellipsis;white-space:nowrap}}}}
.unread{{{{flex:0 0 auto;color:#d8d2ff;font-size:12px;font-weight:600}}}}
.amt{{{{font-size:26px;font-weight:700;letter-spacing:-.02em;margin:2px 0 6px}}}}
.amt.in{{{{color:{inc}}}}}
.amt.out{{{{color:{outc}}}}}
.tag{{{{font-size:11px;padding:4px 10px;border-radius:999px;border:1px solid rgba(255,255,255,.25);background:rgba(255,255,255,.08)}}}}
.btns{{{{display:flex;gap:10px;margin-top:14px}}}}
.btn{{{{flex:1;padding:11px 0;border-radius:14px;border:1px solid rgba(255,255,255,.3);background:rgba(255,255,255,.12);color:#fff;font-size:13px;font-weight:600;cursor:pointer;font-family:inherit}}}}
.btn.pri{{{{background:{pri};border-color:transparent}}}}
.bar{{{{height:8px;border-radius:4px;background:rgba(255,255,255,.14);margin-top:12px;overflow:hidden}}}}
.bar i{{{{display:block;height:100%;border-radius:4px;background:{barbg};width:{barw}}}}}
@supports not ((backdrop-filter:blur(1px)) or (-webkit-backdrop-filter:blur(1px))){{{{.card{{{{background:rgba(43,35,68,.88)}}}}}}}}
@media (prefers-reduced-motion:reduce){{{{.card{{{{transition:none}}}}}}}}"""

def card_html(c):
    top = f'<div class="top"><span class="pill">{c["pill"]}</span>'
    if c.get("tag"): top += f'<span class="tag">{c["tag"]}</span>'
    top += '</div>'
    body = f'<div class="row"><div class="face">{c["icon"]}</div><div class="copy">'
    body += f'<div class="title-line"><strong>{c["title"]}</strong><time>{c["time"]}</time></div>'
    if c.get("amt"): body += f'<div class="amt {c["amtcls"]}">{c["amt"]}</div>'
    body += f'<div class="preview">{c["preview"]}</div></div>'
    if c.get("unread"): body += f'<span class="unread">{c["unread"]}</span>'
    body += '</div>'
    if c.get("bar"): body += f'<div class="bar"><i style="width:{c["bar"]}"></i></div>'
    if c.get("btns"): body += '<div class="btns">' + ''.join(
        f'<button class="btn{" pri" if i==0 else ""}">{b}</button>' for i, b in enumerate(c["btns"])) + '</div>'
    return f'<section class="card">{top}{body}</section>'

def page(p):
    cards = ''.join(card_html(c) for c in p["cards"])
    css = BASE_CSS.format(**p["style"])
    return f"""<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{p["title"]}</title>
<style>{css}</style>
</head>
<body>
<main>
<header class="heading">
<p class="eyebrow">{p["eyebrow"]}</p>
<h1>{p["h1"]}</h1>
<p class="hint">{p["hint"]}</p>
</header>
{cards}
</main>
</body>
</html>"""

F = "linear-gradient(145deg,rgba(255,225,194,.88),rgba(190,139,204,.78) 58%,rgba(111,133,201,.8))"
def sty(bg, **kw):
    d = dict(edge="rgba(255,255,255,.28)",
             glass="linear-gradient(135deg,rgba(255,255,255,.20),rgba(255,255,255,.08) 48%,rgba(202,170,255,.12))",
             blur=24, hldeg=118, hl1=".34", hltint="rgba(255,206,234,.16)",
             arcpos="top:-58px;right:-42px", arcw=190, arch=130, arcrot=-20,
             face=F, inc="#7dffb0", outc="#ffb3b3", pri="rgba(255,255,255,.22)",
             barbg="linear-gradient(90deg,#7dffb0,#34d399)", barw="60%")
    d.update(kw); d["bg"] = bg
    return d

items = [
# n41 收款到账 · 翡翠绿
dict(title="收款到账", eyebrow="PAY · INCOME", h1="收款", hint="每一笔入账，都值得被看见。",
 style=sty("radial-gradient(ellipse at 18% 22%,rgba(52,211,153,.85),transparent 34%),radial-gradient(ellipse at 80% 40%,rgba(16,122,87,.8),transparent 36%),radial-gradient(ellipse at 50% 90%,rgba(6,78,59,.85),transparent 38%),linear-gradient(150deg,#052e22,#064e3b 55%,#022c22)",
           glass="linear-gradient(135deg,rgba(255,255,255,.22),rgba(255,255,255,.09) 48%,rgba(110,255,190,.14))", hltint="rgba(160,255,210,.16)"),
 cards=[
  dict(pill="收款", icon="¥", title="微信收款到账", time="14:02", amt="+12,800.00", amtcls="in",
       preview="付款方：云杉贸易 · 备注：三月货款尾款", unread="查看"),
  dict(pill="到账", icon="💰", title="支付宝到账通知", time="11:47", amt="+3,250.00", amtcls="in",
       preview="转账方：林小满 · 备注：AA 聚餐"),
  dict(pill="入账", icon="🏦", title="银行入账提醒", time="09:15", amt="+8,642.30", amtcls="in",
       preview="尾号 8821 储蓄卡 · 工资补贴到账", btns=["查看明细","已读"]),
 ]),
# n42 转账成功 · 深海蓝紫
dict(title="转账成功", eyebrow="PAY · TRANSFER", h1="转账", hint="钱已出发，准时抵达。",
 style=sty("radial-gradient(ellipse at 82% 18%,rgba(129,140,248,.85),transparent 34%),radial-gradient(ellipse at 15% 45%,rgba(76,29,149,.85),transparent 36%),radial-gradient(ellipse at 60% 88%,rgba(30,27,75,.9),transparent 38%),linear-gradient(150deg,#0b0b28,#1e1b4b 55%,#0f0f2e)",
           hldeg=62, hltint="rgba(180,190,255,.16)", arcpos="bottom:-58px;left:-42px", arcrot=20),
 cards=[
  dict(pill="已转出", icon="➚", title="转账成功", time="16:20", amt="-5,000.00", amtcls="out",
       preview="收款方：陈默然 · 实时到账"),
  dict(pill="跨境", icon="🌐", title="跨境汇款已受理", time="10:08", amt="-1,200.00", amtcls="out",
       preview="收款方：S. Tanaka · 预计 1-2 个工作日到账", btns=["查看进度"]),
  dict(pill="AA", icon="👥", title="AA 收款发起", time="08:30",
       preview="向「周末露营」群 6 人发起 AA，每人 ¥186", unread="3 人已付"),
 ]),
# n43 信用卡账单 · 暗金香槟
dict(title="信用卡账单", eyebrow="PAY · BILL", h1="账单", hint="花得明白，还得从容。",
 style=sty("radial-gradient(ellipse at 20% 25%,rgba(251,191,36,.75),transparent 34%),radial-gradient(ellipse at 78% 42%,rgba(180,120,40,.7),transparent 36%),radial-gradient(ellipse at 52% 88%,rgba(60,40,10,.85),transparent 38%),linear-gradient(150deg,#1c1410,#3a2a18 55%,#171008)",
           glass="linear-gradient(135deg,rgba(255,255,255,.16),rgba(255,255,255,.07) 48%,rgba(255,210,120,.14))", hltint="rgba(255,220,150,.18)", hldeg=140,
           arcpos="top:-48px;left:-38px", arcw=170, arch=120, arcrot=-32,
           outc="#ffd479", pri="linear-gradient(135deg,#fbbf24,#d97706)"),
 cards=[
  dict(pill="本期账单", icon="💳", title="招商银行信用卡", time="每月 5 日", amt="¥9,872.40", amtcls="out",
       preview="最低还款 ¥987.24 · 最后还款日 10 月 23 日", bar="72%", btns=["立即还款","分期"]),
  dict(pill="已出账", icon="🧾", title="交通银行信用卡", time="每月 12 日", amt="¥2,315.80", amtcls="out",
       preview="本期新增 18 笔 · 最大一笔 ¥680 餐饮", btns=["查看账单"]),
 ]),
# n44 还款提醒 · 蜜桃粉
dict(title="还款提醒", eyebrow="PAY · REPAY", h1="还款", hint="别让逾期，偷走你的信用分。",
 style=sty("radial-gradient(ellipse at 16% 20%,rgba(249,168,212,.85),transparent 34%),radial-gradient(ellipse at 84% 38%,rgba(244,114,182,.75),transparent 36%),radial-gradient(ellipse at 55% 90%,rgba(134,25,80,.8),transparent 38%),linear-gradient(150deg,#2b0f1e,#4a1630 55%,#240b18)",
           hldeg=95, hltint="rgba(255,190,220,.18)", arcw=210, arch=140,
           barbg="linear-gradient(90deg,#f9a8d4,#ec4899)", barw="45%", pri="linear-gradient(135deg,#f472b6,#db2777)"),
 cards=[
  dict(pill="待还款", icon="⏰", title="花呗本月待还", time="3 天后到期", amt="¥1,268.00", amtcls="out",
       preview="已还 ¥1,032 / 共 ¥2,300", bar="45%", btns=["立即还款","延期"]),
  dict(pill="提醒", icon="📣", title="借呗还款提醒", time="明天 10:00", amt="¥860.00", amtcls="out",
       preview="自动扣款已开启 · 请确保余额充足", unread="去设置"),
 ]),
# n45 红包到手 · 中国红
dict(title="红包到手", eyebrow="PAY · REDPACKET", h1="红包", hint="好运气，正在派送中。",
 style=sty("radial-gradient(ellipse at 20% 22%,rgba(248,113,113,.9),transparent 34%),radial-gradient(ellipse at 80% 36%,rgba(190,18,60,.85),transparent 36%),radial-gradient(ellipse at 55% 88%,rgba(120,10,30,.85),transparent 38%),linear-gradient(150deg,#2a0a12,#5c0f1e 55%,#200710)",
           glass="linear-gradient(135deg,rgba(255,255,255,.20),rgba(255,255,255,.08) 48%,rgba(255,120,120,.14))", hltint="rgba(255,160,160,.18)",
           arcpos="top:-66px;right:-50px", arcw=220, arch=150, arcrot=-12,
           inc="#ffd479", pri="linear-gradient(135deg,#ef4444,#b91c1c)"),
 cards=[
  dict(pill="红包", icon="🧧", title="你收到一个红包", time="刚刚", amt="+88.88", amtcls="in",
       preview="来自「家人群」· 大伯：中秋快乐", btns=["开红包"]),
  dict(pill="拼手气", icon="✋", title="拼手气红包", time="12:05", amt="+36.50", amtcls="in",
       preview="来自「开黑小队」· 你是手气最佳", unread="领取"),
  dict(pill="口令", icon="🔑", title="口令红包可领", time="昨天", amt="+12.00", amtcls="in",
       preview="口令：金秋大吉 · 剩余 3 个", btns=["去领取","忽略"]),
 ]),
# n46 优惠券 · 薄荷青
dict(title="优惠券", eyebrow="PAY · COUPON", h1="优惠券", hint="省下来的，都是赚到的。",
 style=sty("radial-gradient(ellipse at 18% 24%,rgba(94,234,212,.8),transparent 34%),radial-gradient(ellipse at 82% 40%,rgba(45,212,191,.7),transparent 36%),radial-gradient(ellipse at 50% 88%,rgba(13,90,85,.85),transparent 38%),linear-gradient(150deg,#062a28,#0d4a45 55%,#041e1c)",
           hldeg=200, hltint="rgba(160,255,240,.16)", arcpos="bottom:-50px;right:-40px", arcw=180, arch=125, arcrot=28,
           pri="linear-gradient(135deg,#2dd4bf,#0d9488)"),
 cards=[
  dict(pill="满减券", icon="🎟", title="满 199 减 50", time="3 天后过期", preview="全场通用 · 仅剩 1 张", btns=["立即使用"]),
  dict(pill="免邮券", icon="📦", title="全场免邮券 ×2", time="7 天后过期", preview="无门槛 · 支持叠加满减", unread="去看看"),
  dict(pill="新人券", icon="🎁", title="新人专享 8 折", time="长期有效", preview="首单立享 · 最高抵 ¥30", btns=["领取"]),
 ]),
# n47 股价提醒 · 霓虹紫
dict(title="股价提醒", eyebrow="PAY · STOCK", h1="行情", hint="涨跌之间，保持冷静。",
 style=sty("radial-gradient(ellipse at 85% 20%,rgba(192,38,211,.85),transparent 34%),radial-gradient(ellipse at 12% 42%,rgba(59,130,246,.8),transparent 36%),radial-gradient(ellipse at 58% 90%,rgba(20,10,40,.9),transparent 38%),linear-gradient(150deg,#0d0618,#241040 55%,#0a0616)",
           hldeg=160, hltint="rgba(220,170,255,.18)", arcw=200, arch=135,
           inc="#4ade80", outc="#f87171", pri="linear-gradient(135deg,#a855f7,#6d28d9)"),
 cards=[
  dict(pill="涨", icon="📈", title="宁德时代 涨超 5%", time="10:32", amt="+5.32%", amtcls="in",
       preview="现价 ¥268.40 · 触发你的价格提醒", unread="查看"),
  dict(pill="跌", icon="📉", title="贵州茅台 跌破提醒", time="14:55", amt="-2.18%", amtcls="out",
       preview="现价 ¥1,482.00 · 跌破 ¥1,500 预警线", btns=["查看","加自选"]),
  dict(pill="分红", icon="💹", title="分红到账", time="09:30", amt="+486.00", amtcls="in",
       preview="沪深 300ETF 现金分红已派发"),
 ]),
# n48 生活缴费 · 青蓝
dict(title="生活缴费", eyebrow="PAY · UTILITY", h1="缴费", hint="柴米油盐，皆是生活。",
 style=sty("radial-gradient(ellipse at 15% 22%,rgba(56,189,248,.85),transparent 34%),radial-gradient(ellipse at 82% 40%,rgba(14,116,144,.8),transparent 36%),radial-gradient(ellipse at 52% 88%,rgba(8,51,68,.88),transparent 38%),linear-gradient(150deg,#08222e,#0e3a4a 55%,#061820)",
           hldeg=230, hltint="rgba(150,220,255,.16)", arcpos="top:-52px;left:-44px", arcw=185, arch=128, arcrot=-25,
           pri="linear-gradient(135deg,#38bdf8,#0284c7)"),
 cards=[
  dict(pill="电费", icon="⚡", title="电费账单", time="本月", amt="¥126.50", amtcls="out",
       preview="户号 882103 · 用电 212 度 · 余额不足请充值", btns=["立即缴费"]),
  dict(pill="水费", icon="💧", title="水费已缴清", time="昨天", amt="¥48.20", amtcls="out",
       preview="户号 771204 · 自动扣款成功"),
  dict(pill="燃气", icon="🔥", title="燃气费提醒", time="5 天后到期", amt="¥86.00", amtcls="out",
       preview="户号 990211 · 逾期将影响用气", unread="去缴费"),
 ]),
# n49 工资到账 · 墨绿金
dict(title="工资到账", eyebrow="PAY · SALARY", h1="工资", hint="努力，终有回响。",
 style=sty("radial-gradient(ellipse at 20% 20%,rgba(212,175,55,.7),transparent 34%),radial-gradient(ellipse at 80% 42%,rgba(34,100,70,.85),transparent 36%),radial-gradient(ellipse at 55% 90%,rgba(6,40,26,.9),transparent 38%),linear-gradient(150deg,#0a1f16,#143b28 55%,#071510)",
           glass="linear-gradient(135deg,rgba(255,255,255,.18),rgba(255,255,255,.07) 48%,rgba(230,200,120,.13))", hltint="rgba(240,215,140,.18)",
           hldeg=75, arcw=195, arch=132, inc="#fbbf24", pri="linear-gradient(135deg,#d4af37,#a67c1a)"),
 cards=[
  dict(pill="工资", icon="💼", title="10 月工资到账", time="今日 09:00", amt="+18,500.00", amtcls="in",
       preview="发放方：星野科技 · 税后实发", btns=["查看工资条"]),
  dict(pill="奖金", icon="🏆", title="季度奖金到账", time="昨日", amt="+6,000.00", amtcls="in",
       preview="Q3 绩效奖金 · 已扣税", unread="查看"),
 ]),
# n50 汇率提醒 · 深海青
dict(title="汇率提醒", eyebrow="PAY · FOREX", h1="汇率", hint="全球的钱，本地的心。",
 style=sty("radial-gradient(ellipse at 82% 22%,rgba(45,212,191,.75),transparent 34%),radial-gradient(ellipse at 16% 44%,rgba(2,80,100,.85),transparent 36%),radial-gradient(ellipse at 58% 90%,rgba(3,40,55,.9),transparent 38%),linear-gradient(150deg,#04141c,#072b38 55%,#030e14)",
           hldeg=290, hltint="rgba(140,240,225,.16)", arcpos="bottom:-56px;left:-46px", arcw=190, arch=130, arcrot=22,
           inc="#5eead4", pri="linear-gradient(135deg,#14b8a6,#0f766e)"),
 cards=[
  dict(pill="美元", icon="$", title="美元兑人民币 7.12", time="实时", amt="7.1245", amtcls="in",
       preview="较昨日 +0.08% · 触发你的 7.10 提醒", btns=["去换汇"]),
  dict(pill="日元", icon="¥", title="日元汇率新低", time="1 小时前", amt="0.0482", amtcls="out",
       preview="100 日元兑 ¥4.82 · 适合购汇", unread="查看"),
  dict(pill="欧元", icon="€", title="欧元小幅走强", time="3 小时前", amt="7.8561", amtcls="in",
       preview="较昨日 +0.12% · 留学缴费可关注"),
 ]),
]

titles = ["收款到账","转账成功","信用卡账单","还款提醒","红包到手","优惠券","股价提醒","生活缴费","工资到账","汇率提醒"]

os.makedirs("/home/hatch/workspace/liquid-notify-cards", exist_ok=True)
for i, p in enumerate(items):
    n = 41 + i
    html = page(p)
    open(f"/home/hatch/workspace/liquid-notify-cards/n{n}.html", "w", encoding="utf-8").write(html)
print("wrote 10 files")

import json
json.dump([{"file": f"n{41+i}.html", "title": t} for i, t in enumerate(titles)],
          open("/home/hatch/workspace/liquid-notify-cards/_titles_nc_e.json", "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
print("titles json ok")
