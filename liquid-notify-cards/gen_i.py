#!/usr/bin/env python3
# 生成 n81-n90 浅色柔光液态玻璃通知卡片
import os, json

OUT = os.path.dirname(os.path.abspath(__file__))

CARD_T = '''
    <section class="card">
      <div class="top">
        <span class="pill">{pill}</span>
        {right}
      </div>
      <div class="row">
        <div class="face" style="background:{face}">{face_t}</div>
        <div class="copy">
          <div class="title-line"><strong>{title}</strong><time>{time}</time></div>
          <div class="preview">{preview}</div>
        </div>
        {tail}
      </div>
      {extra}
    </section>'''

def avatars(names):
    return '<div class="avatars">' + ''.join('<i class="avatar">%s</i>' % n for n in names) + '</div>'

def C(pill, right, face, face_t, title, time, preview, tail='', extra=''):
    return dict(pill=pill, right=right, face=face, face_t=face_t, title=title,
                time=time, preview=preview, tail=tail, extra=extra)

THEMES = [
 dict(num=81, cls='n81', title='奶白晨雾', h1='通知', hint='轻一点的消息，也有自己的光。',
      bg='radial-gradient(ellipse at 14% 18%, rgba(255,214,170,.9), transparent 36%),radial-gradient(ellipse at 84% 30%, rgba(255,236,205,.9), transparent 38%),radial-gradient(ellipse at 50% 92%, rgba(186,208,232,.55), transparent 40%),linear-gradient(150deg,#faf5ea,#f3ecdc 55%,#ece4d2)',
      glass='linear-gradient(135deg,rgba(255,255,255,.62),rgba(255,255,255,.28) 48%,rgba(255,244,224,.42))',
      bd='1px solid rgba(255,255,255,.7)', hi=118, arc='top:-58px;right:-42px;width:190px;height:130px;transform:rotate(-20deg)',
      cards=[
       C('消息', avatars(['沈','苏']), 'linear-gradient(145deg,#f7b98a,#e08fb0 60%,#a98bd0)', '沈',
         '沈小满', '09:24', '周末去爬山吗？山顶有云海', '<span class="unread">2 条未读</span>'),
       C('日程', '<span class="more">明天 9:00</span>', 'linear-gradient(145deg,#9cc7f5,#7aa7e8 60%,#5f86c9)', '会',
         '团队例会', '08:00', '会议室 3F · 记得带上周报'),
      ]),
 dict(num=82, cls='n82', title='蜜桃气泡', h1='消息', hint='甜甜的气泡，咕嘟咕嘟往上冒。',
      bg='radial-gradient(ellipse at 18% 22%, rgba(255,170,150,.85), transparent 36%),radial-gradient(ellipse at 80% 28%, rgba(255,205,170,.9), transparent 38%),radial-gradient(ellipse at 52% 90%, rgba(255,190,170,.5), transparent 40%),linear-gradient(150deg,#fff2e6,#ffe4d2 55%,#ffd9c4)',
      glass='linear-gradient(135deg,rgba(255,255,255,.6),rgba(255,255,255,.26) 48%,rgba(255,220,200,.4))',
      bd='1px solid rgba(255,255,255,.68)', hi=65, arc='top:-52px;left:-40px;width:180px;height:124px;transform:rotate(24deg)',
      cards=[
       C('订单', '<span class="more">已发货</span>', 'linear-gradient(145deg,#ffb08a,#ff8a6a 60%,#e86a5a)', '茶',
         '蜜桃乌龙茶 ×2', '10:05', '包裹已从杭州仓发出，预计后天到', '',
         '<div class="prog"><i style="width:35%"></i></div>'),
       C('系统', '', 'linear-gradient(145deg,#f5a3b8,#e87f9e 60%,#c95f84)', '✦',
         '新版本可用', '昨天', 'v3.2.1 带来更顺滑的果冻动效', '<span class="dot"></span>'),
      ]),
 dict(num=83, cls='n83', title='薄荷青柠', h1='通知', hint='清清凉凉，一天都透着爽。',
      bg='radial-gradient(ellipse at 16% 20%, rgba(150,235,195,.85), transparent 36%),radial-gradient(ellipse at 82% 32%, rgba(200,245,215,.9), transparent 38%),radial-gradient(ellipse at 55% 90%, rgba(140,210,235,.5), transparent 40%),linear-gradient(150deg,#f2fbf4,#e2f5e9 55%,#d4efe0)',
      glass='linear-gradient(135deg,rgba(255,255,255,.62),rgba(255,255,255,.28) 48%,rgba(210,250,225,.42))',
      bd='1px solid rgba(255,255,255,.7)', hi=200, arc='bottom:-60px;right:-44px;width:200px;height:134px;transform:rotate(18deg)',
      cards=[
       C('天气', '<span class="more">26°</span>', 'linear-gradient(145deg,#8fd8b0,#5fb98f 60%,#3f9e74)', '☀',
         '今日晴转多云', '07:00', '午后有阵雨，记得带伞', '',
         '<div class="wrow"><span>12°</span><div class="wbar"><i style="width:62%"></i></div><span>31°</span></div>'),
       C('运动', avatars(['跑']), 'linear-gradient(145deg,#a5e0c0,#6fc79b 60%,#4da87e)', '🏃',
         '晨跑完成', '06:40', '5.2 公里 · 配速 6\'12" · 新纪录！', '<span class="unread">+120</span>'),
      ]),
 dict(num=84, cls='n84', title='雾蓝晴空', h1='消息', hint='像晴空一样，把事情说清楚。',
      bg='radial-gradient(ellipse at 15% 18%, rgba(165,200,245,.85), transparent 36%),radial-gradient(ellipse at 84% 30%, rgba(200,220,250,.9), transparent 38%),radial-gradient(ellipse at 50% 92%, rgba(150,180,230,.5), transparent 40%),linear-gradient(150deg,#f0f6fd,#dfeaf9 55%,#d2e2f5)',
      glass='linear-gradient(135deg,rgba(255,255,255,.62),rgba(255,255,255,.28) 48%,rgba(205,225,250,.42))',
      bd='1px solid rgba(255,255,255,.7)', hi=245, arc='top:-56px;right:-46px;width:186px;height:128px;transform:rotate(-14deg)',
      cards=[
       C('邮件', '<span class="more">设计组</span>', 'linear-gradient(145deg,#9dbdf0,#6f97e0 60%,#4f76c4)', '✉',
         '设计稿评审邀请', '11:20', '周四下午一起过一遍新版首页', '<span class="dot"></span>',
         '<div class="btns"><button>接受</button><button class="ghost">稍后</button></div>'),
       C('群聊', avatars(['陆','许','方']), 'linear-gradient(145deg,#8fb4ea,#5f8cd8 60%,#3f68b8)', '陆',
         '开黑小队', '21:47', '陆知遥：今晚十点，五缺一', '<span class="unread">9 条未读</span>'),
      ]),
 dict(num=85, cls='n85', title='淡紫薰衣', h1='通知', hint='薰衣草味的傍晚，适合听歌。',
      bg='radial-gradient(ellipse at 16% 20%, rgba(205,175,240,.85), transparent 36%),radial-gradient(ellipse at 82% 30%, rgba(230,200,245,.9), transparent 38%),radial-gradient(ellipse at 54% 90%, rgba(185,160,225,.5), transparent 40%),linear-gradient(150deg,#f6f1fc,#e9ddf6 55%,#ddcdf0)',
      glass='linear-gradient(135deg,rgba(255,255,255,.6),rgba(255,255,255,.26) 48%,rgba(220,195,245,.4))',
      bd='1px solid rgba(255,255,255,.68)', hi=30, arc='top:-60px;left:-46px;width:196px;height:132px;transform:rotate(28deg)',
      cards=[
       C('音乐', '<span class="more">每日推荐</span>', 'linear-gradient(145deg,#c39be8,#9a6fd0 60%,#7a52b8)', '♪',
         '《晚风告白》', '18:30', '根据你的口味推荐 · 试听 30 秒', '',
         '<div class="vbar"><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i></div>'),
       C('日程', '<span class="more">19:00</span>', 'linear-gradient(145deg,#b58fe0,#8f68c8 60%,#6f4aa8)', '🧘',
         '空中瑜伽', '今天', '带上水杯，提前 10 分钟到馆'),
      ]),
 dict(num=86, cls='n86', title='蜜瓜奶黄', h1='通知', hint='黄澄澄的好消息，总是准时到。',
      bg='radial-gradient(ellipse at 14% 20%, rgba(255,225,150,.9), transparent 36%),radial-gradient(ellipse at 84% 32%, rgba(255,240,200,.9), transparent 38%),radial-gradient(ellipse at 52% 90%, rgba(240,210,140,.5), transparent 40%),linear-gradient(150deg,#fdf8e8,#fbeecd 55%,#f7e3b8)',
      glass='linear-gradient(135deg,rgba(255,255,255,.62),rgba(255,255,255,.28) 48%,rgba(255,240,205,.44))',
      bd='1px solid rgba(255,255,255,.7)', hi=160, arc='bottom:-58px;left:-44px;width:190px;height:130px;transform:rotate(-24deg)',
      cards=[
       C('支付', '<span class="more">+128.00</span>', 'linear-gradient(145deg,#f5c86a,#e8a83f 60%,#cf8a28)', '¥',
         '收到一笔转账', '12:02', '苏棠梨 转给你，请查收', '',
         '<div class="btns"><button>查看账单</button></div>'),
       C('验证码', '<span class="more">5 分钟内有效</span>', 'linear-gradient(145deg,#e8b95f,#d09a3f 60%,#b07c28)', '🔑',
         '登录验证码', '刚刚', '【蜜瓜】验证码 4862，请勿泄露', '<span class="dot"></span>'),
      ]),
 dict(num=87, cls='n87', title='粉蓝汽水', h1='消息', hint='咕嘟咕嘟，快乐正在上浮。',
      bg='radial-gradient(ellipse at 18% 18%, rgba(255,185,215,.85), transparent 36%),radial-gradient(ellipse at 80% 30%, rgba(160,205,250,.9), transparent 38%),radial-gradient(ellipse at 52% 90%, rgba(190,175,240,.5), transparent 40%),linear-gradient(150deg,#fdf0f6,#f6e4f0 55%,#e9d4ec)',
      glass='linear-gradient(135deg,rgba(255,255,255,.6),rgba(255,255,255,.26) 48%,rgba(235,205,240,.42))',
      bd='1px solid rgba(255,255,255,.68)', hi=95, arc='top:-54px;right:-40px;width:184px;height:126px;transform:rotate(-26deg)',
      cards=[
       C('社交', avatars(['新']), 'linear-gradient(145deg,#f5a0c8,#e070a8 60%,#c05088)', '♡',
         '3 位新粉丝', '14:15', '顾南风 等关注了你', '<span class="unread">3</span>'),
       C('消息', '', 'linear-gradient(145deg,#a8c8f5,#7a9fe8 60%,#5a7fc8)', '顾',
         '顾南风', '14:02', '[语音] 点按收听', '',
         '<div class="voice"><i style="--w:46%"></i><span>12"</span></div>'),
      ]),
 dict(num=88, cls='n88', title='青瓷雾', h1='通知', hint='雾蒙蒙的早上，适合慢一点。',
      bg='radial-gradient(ellipse at 15% 20%, rgba(175,210,200,.85), transparent 36%),radial-gradient(ellipse at 84% 30%, rgba(205,225,215,.9), transparent 38%),radial-gradient(ellipse at 50% 90%, rgba(165,195,185,.5), transparent 40%),linear-gradient(150deg,#f2f7f4,#e4efe9 55%,#d6e6dd)',
      glass='linear-gradient(135deg,rgba(255,255,255,.62),rgba(255,255,255,.28) 48%,rgba(210,230,220,.42))',
      bd='1px solid rgba(255,255,255,.7)', hi=290, arc='bottom:-62px;right:-46px;width:198px;height:132px;transform:rotate(16deg)',
      cards=[
       C('系统', '<span class="more">已完成</span>', 'linear-gradient(145deg,#9fc8b8,#6fa894 60%,#4f8874)', '✓',
         '云备份完成', '03:00', '照片 1286 张 · 聊天记录已同步'),
       C('订单', '<span class="more">已签收</span>', 'linear-gradient(145deg,#8fb8a8,#5f9884 60%,#3f7864)', '📦',
         '青瓷茶杯套装', '昨天', '包裹已放入丰巢柜，取件码 88-12', '',
         '<div class="btns"><button>评价晒单</button><button class="ghost">再买一件</button></div>'),
      ]),
 dict(num=89, cls='n89', title='樱粉柔光', h1='消息', hint='樱花开了，消息也开花。',
      bg='radial-gradient(ellipse at 16% 18%, rgba(255,185,200,.85), transparent 36%),radial-gradient(ellipse at 82% 30%, rgba(255,215,225,.9), transparent 38%),radial-gradient(ellipse at 54% 90%, rgba(245,180,195,.5), transparent 40%),linear-gradient(150deg,#fdf1f4,#fae0e8 55%,#f5d2dc)',
      glass='linear-gradient(135deg,rgba(255,255,255,.6),rgba(255,255,255,.26) 48%,rgba(250,210,220,.42))',
      bd='1px solid rgba(255,255,255,.68)', hi=140, arc='top:-58px;left:-44px;width:188px;height:128px;transform:rotate(20deg)',
      cards=[
       C('消息', avatars(['棠']), 'linear-gradient(145deg,#f5a8bc,#e87f9c 60%,#c85f7e)', '棠',
         '沈棠梨', '20:18', '樱花大道开了！周六一起去拍照', '<span class="unread">1</span>'),
       C('天气', '<span class="more">樱花指数 ★★★</span>', 'linear-gradient(145deg,#f0b0c0,#dd8aa2 60%,#bd6884)', '🌸',
         '赏花好时机', '07:30', '本周六晴，微风，最适合出门'),
      ]),
 dict(num=90, cls='n90', title='象牙暖阳', h1='通知', hint='暖阳洒进来，一切都刚刚好。',
      bg='radial-gradient(ellipse at 14% 20%, rgba(255,225,180,.9), transparent 36%),radial-gradient(ellipse at 84% 30%, rgba(255,245,220,.9), transparent 38%),radial-gradient(ellipse at 50% 90%, rgba(235,215,180,.5), transparent 40%),linear-gradient(150deg,#fdfaf2,#f7f0dd 55%,#f0e4c8)',
      glass='linear-gradient(135deg,rgba(255,255,255,.64),rgba(255,255,255,.3) 48%,rgba(250,240,215,.44))',
      bd='1px solid rgba(255,255,255,.72)', hi=75, arc='bottom:-56px;left:-42px;width:186px;height:128px;transform:rotate(-18deg)',
      cards=[
       C('日程', '<span class="more">提前 2 小时</span>', 'linear-gradient(145deg,#f0c078,#dda050 60%,#bd8038)', '✈',
         '航班 MU5128', '明天', '上海 → 大理 · 记得带身份证', '<span class="dot"></span>',
         '<div class="btns"><button>值机</button><button class="ghost">改签</button></div>'),
       C('消息', '', 'linear-gradient(145deg,#e8b878,#d09550 60%,#b07538)', '妈',
         '妈妈', '19:55', '到了那边记得报平安，天冷加衣', '<span class="unread">1 条未读</span>'),
      ]),
]

EXTRA_CSS = '''
    .prog{height:8px;border-radius:5px;background:rgba(90,80,100,.12);margin-top:14px;overflow:hidden}
    .prog i{display:block;height:100%;border-radius:5px;background:linear-gradient(90deg,#e08090,#c06080)}
    .wrow{display:flex;align-items:center;gap:10px;margin-top:14px;font-size:12px;color:rgba(60,55,70,.7)}
    .wbar{flex:1;height:8px;border-radius:5px;background:rgba(90,80,100,.12);overflow:hidden}
    .wbar i{display:block;height:100%;background:linear-gradient(90deg,#8fd8b0,#f5c86a,#e08090)}
    .btns{display:flex;gap:10px;margin-top:14px}
    .btns button{flex:1;padding:10px 0;border:0;border-radius:14px;background:#5a6577;color:#fff;font-size:13px;font-weight:600;cursor:pointer;box-shadow:0 4px 12px rgba(60,55,70,.18)}
    .btns button.ghost{background:rgba(255,255,255,.55);color:rgba(60,55,70,.85);border:1px solid rgba(90,80,100,.16)}
    .vbar{display:flex;align-items:flex-end;gap:4px;height:34px;margin-top:14px}
    .vbar i{flex:1;border-radius:3px;background:linear-gradient(180deg,#b58fe0,#8f68c8);opacity:.85}
    .vbar i:nth-child(odd){height:60%}
    .vbar i:nth-child(even){height:100%}
    .vbar i:nth-child(3n){height:40%}
    .voice{display:flex;align-items:center;gap:10px;margin-top:14px}
    .voice i{flex:1;height:26px;border-radius:13px;background:linear-gradient(90deg,#a8c8f5 0 var(--w,46%),rgba(90,80,100,.14) var(--w,46%))}
    .voice span{font-size:12px;color:rgba(60,55,70,.6)}
    .dot{flex:0 0 auto;width:10px;height:10px;border-radius:50%;background:#e06080;box-shadow:0 0 8px rgba(224,96,128,.7)}
'''

PAGE_T = '''<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <style>
    * {{ box-sizing: border-box; }}
    body {{
      min-height: 100vh; margin: 0; padding: 48px 18px; color: #3a3548;
      font: 15px/1.45 -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      background: {bg}; background-attachment: fixed;
    }}
    main {{ width: min(440px, 100%); margin: 0 auto; display: grid; gap: 18px; }}
    .heading {{ padding: 4px 6px 8px; }}
    .eyebrow {{ margin: 0 0 8px; color: rgba(58,53,72,.58); font-size: 11px; letter-spacing: .18em; }}
    h1 {{ margin: 0; font-size: 30px; letter-spacing: -.04em; color: #2e2a3c; }}
    .hint {{ margin: 7px 0 0; color: rgba(58,53,72,.62); }}
    .card {{
      position: relative; isolation: isolate; overflow: hidden; padding: 18px;
      border: {bd}; border-radius: 28px; background: {glass};
      -webkit-backdrop-filter: blur(24px) saturate(175%);
      backdrop-filter: blur(24px) saturate(175%);
      box-shadow: inset 0 1px 0 rgba(255,255,255,.75), inset 0 -1px 0 rgba(255,255,255,.25), 0 18px 42px rgba(90,80,110,.16);
    }}
    .card::before {{
      content: ""; position: absolute; z-index: 0; inset: 0; border-radius: inherit;
      pointer-events: none; opacity: .85;
      background: linear-gradient({hi}deg, rgba(255,255,255,.5) 0%, rgba(255,255,255,.12) 18%, transparent 42%, transparent 72%, rgba(255,255,255,.22) 100%);
    }}
    .card::after {{
      content: ""; position: absolute; z-index: 0; {arc};
      border: 1px solid rgba(255,255,255,.5); border-radius: 50%;
      background: radial-gradient(ellipse, rgba(255,255,255,.4), transparent 68%);
      filter: blur(2px); pointer-events: none;
    }}
    .card > * {{ position: relative; z-index: 1; }}
    .top, .title-line {{ display: flex; align-items: center; justify-content: space-between; gap: 12px; }}
    .top {{ margin-bottom: 17px; }}
    .pill {{ padding: 6px 12px; border: 1px solid rgba(90,80,110,.18); border-radius: 999px; background: rgba(255,255,255,.5); color: rgba(58,53,72,.9); font-size: 12px; box-shadow: inset 0 1px rgba(255,255,255,.6); }}
    .avatars {{ display: flex; align-items: center; padding-left: 8px; }}
    .avatar {{ display: grid; width: 29px; height: 29px; margin-left: -8px; place-items: center; border: 1px solid rgba(255,255,255,.7); border-radius: 50%; background: linear-gradient(135deg, #f8c79e, #a987c8 70%, #7267a9); color: #fff; font-size: 11px; box-shadow: 0 3px 10px rgba(90,80,110,.18); }}
    .more {{ margin-left: 7px; color: rgba(58,53,72,.6); font-size: 12px; }}
    .row {{ display: flex; align-items: center; gap: 12px; min-width: 0; }}
    .face {{ display: grid; flex: 0 0 48px; height: 48px; place-items: center; border: 1px solid rgba(255,255,255,.6); border-radius: 50%; color: #fff; font-size: 19px; font-weight: 650; box-shadow: inset 0 1px 5px rgba(255,255,255,.5), 0 5px 15px rgba(90,80,110,.16); }}
    .copy {{ flex: 1; min-width: 0; }}
    .title-line {{ margin-bottom: 5px; }}
    .title-line strong {{ overflow: hidden; text-overflow: ellipsis; white-space: nowrap; color: #2e2a3c; }}
    time, .preview {{ color: rgba(58,53,72,.62); font-size: 12px; }}
    .preview {{ overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }}
    .unread {{ flex: 0 0 auto; color: #b0506e; font-size: 12px; font-weight: 600; }}
    {extra_css}
  </style>
</head>
<body class="{cls}">
  <main>
    <header class="heading">
      <p class="eyebrow">LIQUID GLASS</p>
      <h1>{h1}</h1>
      <p class="hint">{hint}</p>
    </header>
{cards}
  </main>
</body>
</html>
'''

for th in THEMES:
    cards = '\n'.join(CARD_T.format(**c) for c in th['cards'])
    html = PAGE_T.format(title=th['title'], bg=th['bg'], bd=th['bd'], glass=th['glass'],
                         hi=th['hi'], arc=th['arc'], cls=th['cls'], h1=th['h1'],
                         hint=th['hint'], cards=cards, extra_css=EXTRA_CSS)
    fn = os.path.join(OUT, 'n%d.html' % th['num'])
    open(fn, 'w', encoding='utf-8').write(html)
    print('wrote', fn)

titles = [{'file': 'n%d.html' % th['num'], 'title': th['title']} for th in THEMES]
json.dump(titles, open(os.path.join(OUT, '_titles_nc_i.json'), 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
print('titles json ok')
