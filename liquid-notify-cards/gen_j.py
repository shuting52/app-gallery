# -*- coding: utf-8 -*-
"""生成 n91-n100 液态玻璃通知卡片（东方质感组）"""
import os

OUT = os.path.dirname(os.path.abspath(__file__))

CSS = """
*{box-sizing:border-box;margin:0;padding:0}
html,body{min-height:100%}
body{
  position:relative;
  padding:48px 18px 64px;
  color:VARink;
  font:15px/1.45 -apple-system,BlinkMacSystemFont,"PingFang SC","Hiragino Sans GB","Microsoft YaHei",system-ui,sans-serif;
  background:VARbase;
  background-attachment:fixed;
  overflow-x:hidden;
}
.bg{
  position:fixed;inset:-6%;z-index:0;pointer-events:none;
  background:VARgrads;
  animation:drift 30s ease-in-out infinite alternate;
  animation-delay:-15s;
}
@keyframes drift{
  from{transform:translate3d(-1.5%,-1%,0) scale(1.03) rotate(0deg)}
  to{transform:translate3d(1.5%,1.5%,0) scale(1.07) rotate(1.5deg)}
}
main{position:relative;z-index:1;width:min(440px,100%);margin:0 auto;display:grid;gap:18px}
.heading{padding:4px 6px 8px}
.eyebrow{margin:0 0 8px;color:VARmut;font-size:11px;letter-spacing:.18em}
h1{margin:0;font-size:30px;letter-spacing:-.02em;color:VARink}
.hint{margin:7px 0 0;color:VARmut}
.card{
  position:relative;isolation:isolate;overflow:hidden;
  padding:18px;border-radius:28px;
  border:1px solid VARbd;
  background:VARtex,VARcardbg;
  -webkit-backdrop-filter:blur(24px) saturate(175%);
  backdrop-filter:blur(24px) saturate(175%);
  box-shadow:
    inset 0 1px 0 VARhi,
    inset 0 -1px 0 rgba(0,0,0,.06),
    0 20px 48px VARsh;
  transition:transform .25s ease,border-color .25s ease;
}
.card::before{
  content:"";position:absolute;z-index:0;inset:0;border-radius:inherit;pointer-events:none;
  background:
    linear-gradient(VARhlang,
      VARhl1 0%,
      VARhl2 18%,
      transparent 42%,
      transparent 72%,
      VARhl3 100%);
  opacity:.8;
  animation:sheen 9s ease-in-out infinite alternate;
  animation-delay:-4s;
}
@keyframes sheen{from{opacity:.55}to{opacity:.95}}
.card::after{
  content:"";position:absolute;z-index:0;
  top:VARaxt;right:VARaxr;width:VARaxw;height:VARaxh;
  border:1px solid VARbd2;border-radius:50%;
  background:radial-gradient(ellipse,VARaxbg,transparent 68%);
  filter:blur(2px);transform:rotate(VARaxrot);pointer-events:none;
}
.card>*{position:relative;z-index:1}
.card:hover{transform:translateY(-3px);border-color:VARbdh}
.top,.title-line{display:flex;align-items:center;justify-content:space-between;gap:12px}
.top{margin-bottom:15px}
.pill{
  padding:6px 12px;border:1px solid VARpbd;border-radius:999px;
  background:VARpbg;color:VARpink;font-size:12px;
  box-shadow:inset 0 1px VARhi;white-space:nowrap;
}
.avatars{display:flex;align-items:center;padding-left:8px}
.avatar{
  display:grid;width:29px;height:29px;margin-left:-8px;place-items:center;
  border:1px solid VARabd;border-radius:50%;
  background:linear-gradient(135deg,#8a7a6a,#5d5a72 70%,#3f4456);
  color:#fff;font-size:11px;font-style:normal;
  box-shadow:0 3px 10px rgba(10,8,18,.25);
}
.more{margin-left:7px;color:VARmut;font-size:12px}
.row{display:flex;align-items:center;gap:12px;min-width:0}
.face{
  display:grid;flex:0 0 48px;height:48px;place-items:center;
  border:1px solid VARfbd;border-radius:50%;
  background:#6a7285;color:#fff;font-size:19px;font-weight:650;
  box-shadow:inset 0 1px 5px rgba(255,255,255,.45),0 5px 15px rgba(10,8,20,.22);
}
.copy{flex:1;min-width:0}
.title-line{margin-bottom:5px}
.title-line strong{overflow:hidden;text-overflow:ellipsis;white-space:nowrap;color:VARink}
time,.preview{color:VARmut;font-size:12px}
.preview{overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.unread{flex:0 0 auto;color:VARunr;font-size:12px;font-weight:600;white-space:nowrap}
.dot{flex:0 0 auto;width:9px;height:9px;border-radius:50%;background:VARdotbg;box-shadow:0 0 8px VARdotbg}
.actions{display:flex;gap:10px;margin-top:14px}
.btn{
  flex:1;padding:10px 0;text-align:center;border-radius:14px;font-size:13px;cursor:pointer;
  border:1px solid VARbbd;background:VARbbg;color:VARbink;
  box-shadow:inset 0 1px VARhi;
}
.btn.pri{background:VARpribg;border-color:VARpribd;color:#fff}
.prog{height:8px;border-radius:5px;background:VARprogbg;margin-top:12px;overflow:hidden}
.prog i{display:block;height:100%;width:VARpw;border-radius:5px;background:VARprogfg}
.pmeta{display:flex;justify-content:space-between;margin-top:6px;font-size:11px;color:VARmut}
@supports not ((backdrop-filter:blur(1px)) or (-webkit-backdrop-filter:blur(1px))){
  .card{background:VARfallback}
}
@media (prefers-reduced-motion:reduce){.card,.bg,.card::before{animation:none;transition:none}}
"""

CARD = """
<section class="card">
  <div class="top">
    <span class="pill">{pill}</span>
    <div class="avatars" aria-label="members">{avatars}</div>
  </div>
  <div class="row">
    <div class="face" style="background:{facebg}">{face}</div>
    <div class="copy">
      <div class="title-line"><strong>{name}</strong><time>{time}</time></div>
      <div class="preview">{preview}</div>
    </div>
    {tail}
  </div>
  {extra}
</section>"""

SHELL = """<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<style>{css}</style>
</head>
<body>
<div class="bg"></div>
<main>
<header class="heading">
<p class="eyebrow">{eyebrow}</p>
<h1>{h1}</h1>
<p class="hint">{hint}</p>
</header>
{cards}
</main>
</body>
</html>"""


def avatars(items, more=None):
    s = ''.join('<i class="avatar">%s</i>' % a for a in items)
    if more:
        s += '<span class="more">%s</span>' % more
    return s


def tail_unread(txt):
    return '<span class="unread">%s</span>' % txt


def card(pill, avs, more, face, facebg, name, time, preview, tail='', extra=''):
    return CARD.format(
        pill=pill, avatars=avatars(avs, more), face=face, facebg=facebg,
        name=name, time=time, preview=preview, tail=tail, extra=extra)


def actions(btns):
    # btns: list of (label, primary?)
    inner = ''.join('<span class="btn%s">%s</span>' % (' pri' if p else '', l) for l, p in btns)
    return '<div class="actions">%s</div>' % inner


def prog(pct, label=''):
    return ('<div class="prog"><i style="width:%d%%"></i></div><div class="pmeta"><span>%s</span><span>%d%%</span></div>'
            % (pct, label, pct))


DARK = dict(ink='#ffffff', mut='rgba(255,255,255,.68)', unr='#e6dcff',
            hi='rgba(255,255,255,.42)', bd='rgba(255,255,255,.28)',
            bdh='rgba(255,255,255,.46)', bd2='rgba(255,255,255,.22)',
            pbd='rgba(255,255,255,.30)', pbg='rgba(255,255,255,.10)', pink='rgba(255,255,255,.94)',
            abd='rgba(255,255,255,.55)', fbd='rgba(255,255,255,.45)',
            bbd='rgba(255,255,255,.25)', bbg='rgba(255,255,255,.08)', bink='rgba(255,255,255,.92)',
            fallback='rgba(30,26,44,.92)')
LIGHT = dict(ink='#2b2620', mut='rgba(60,52,40,.66)', unr='#a33b2a',
             hi='rgba(255,255,255,.65)', bd='rgba(60,50,35,.22)',
             bdh='rgba(60,50,35,.4)', bd2='rgba(120,100,70,.25)',
             pbd='rgba(60,50,35,.28)', pbg='rgba(255,255,255,.5)', pink='rgba(50,42,30,.92)',
             abd='rgba(255,255,255,.8)', fbd='rgba(255,255,255,.7)',
             bbd='rgba(60,50,35,.22)', bbg='rgba(255,255,255,.55)', bink='rgba(50,42,30,.9)',
             fallback='rgba(245,240,228,.94)')

THEMES = [
    # ---------------- n91 墨团晕开（深底水墨）
    dict(file='n91.html', title='墨团晕开', eyebrow='LIQUID GLASS · 墨', hint='墨分五色，消息也有浓淡。',
         tone=DARK,
         base='linear-gradient(150deg,#0d0b12,#141020 60%,#0a0f1c)',
         grads=('radial-gradient(ellipse 46% 34% at 18% 22%, rgba(88,60,120,.55), transparent 70%),'
                'radial-gradient(ellipse 40% 30% at 80% 30%, rgba(40,80,120,.45), transparent 70%),'
                'radial-gradient(ellipse 55% 40% at 55% 85%, rgba(30,30,50,.9), transparent 70%)'),
         cardbg='linear-gradient(135deg, rgba(255,255,255,.14), rgba(255,255,255,.05) 48%, rgba(120,110,160,.10))',
         tex='none', sh='rgba(5,5,14,.4)',
         hlang='118deg', hl1='rgba(255,255,255,.30)', hl2='rgba(255,255,255,.07)', hl3='rgba(160,150,220,.14)',
         axt='-58px', axr='-42px', axw='190px', axh='130px', axrot='-20deg', axbg='rgba(200,190,240,.20)',
         prib='linear-gradient(135deg,#4a3a6e,#2c2344)', pribdr='rgba(150,130,200,.5)',
         progb='rgba(255,255,255,.12)', progf='linear-gradient(90deg,#8f7fc8,#5f52a8)', dotb='#b9a8ff',
         cards=[
             card('私聊', ['砚'], None, '砚', 'linear-gradient(145deg,#6b5a8e,#3a3054 60%,#232032)', '沈砚',
                  '21:07', '那幅山水的皴法，我琢磨出点门道了', tail_unread('3 条未读')),
             card('群聊', ['墨', '宣', '砚'], '+5', '墨', 'linear-gradient(145deg,#4a5a7e,#2c3550 60%,#1a2030)', '墨友雅集',
                  '昨天', '周六去琉璃厂看展，报名接龙', tail_unread('12 条未读')),
             card('日程', ['展'], None, '展', 'linear-gradient(145deg,#7e6a4a,#50402c 60%,#33291c)', '「宋人山水」特展',
                  '本周', '特展本周末闭幕，余票不多', tail_unread(''),
                  extra=actions([('查看详情', True), ('稍后提醒', False)])),
         ]),
    # ---------------- n92 米白宣纸（浅底）
    dict(file='n92.html', title='米白宣纸', eyebrow='LIQUID GLASS · 纸', hint='一纸素白，托住每一条消息。',
         tone=LIGHT,
         base='linear-gradient(150deg,#f7f2e6,#efe6d2 60%,#e7dcc4)',
         grads=('radial-gradient(ellipse 40% 30% at 15% 20%, rgba(190,150,100,.30), transparent 70%),'
                'radial-gradient(ellipse 44% 32% at 85% 35%, rgba(150,170,190,.28), transparent 70%),'
                'radial-gradient(ellipse 50% 36% at 55% 88%, rgba(170,130,90,.22), transparent 70%)'),
         cardbg='linear-gradient(135deg, rgba(255,255,255,.55), rgba(255,255,255,.28) 48%, rgba(230,215,185,.35))',
         tex=('url("data:image/svg+xml,%3Csvg xmlns=\'http://www.w3.org/2000/svg\' width=\'140\' height=\'140\'%3E'
              '%3Cfilter id=\'n\'%3E%3CfeTurbulence type=\'fractalNoise\' baseFrequency=\'0.85\' numOctaves=\'2\'/%3E'
              '%3C/filter%3E%3Crect width=\'140\' height=\'140\' filter=\'url(%23n)\' opacity=\'0.10\'/%3E%3C/svg%3E")'),
         sh='rgba(90,70,40,.18)',
         hlang='118deg', hl1='rgba(255,255,255,.7)', hl2='rgba(255,255,255,.25)', hl3='rgba(200,170,120,.25)',
         axt='-52px', axr='-36px', axw='170px', axh='120px', axrot='-24deg', axbg='rgba(255,255,255,.5)',
         prib='linear-gradient(135deg,#8a6a45,#6b4f30)', pribdr='rgba(120,90,55,.5)',
         progb='rgba(90,70,45,.14)', progf='linear-gradient(90deg,#b08d55,#8a6a45)', dotb='#b03a26',
         cards=[
             card('快递', ['丰'], None, '丰', 'linear-gradient(145deg,#a8895a,#7c6240 60%,#5c4a30)', '顺丰速运',
                  '10:22', '您的宣纸已到达丰台营业部', tail_unread(''),
                  extra=actions([('查看物流', True)])),
             card('系统', ['墨'], None, '墨', 'linear-gradient(145deg,#6a6a72,#4a4a54 60%,#33333a)', '墨盒余量',
                  '09:05', '黑色墨盒余量不足 15%，建议备货', tail_unread('')),
             card('订单', ['斋'], None, '斋', 'linear-gradient(145deg,#9a5a4a,#6e3f34 60%,#4e2c24)', '荣宝斋',
                  '昨天', '您预订的《芥子园画谱》已发货', tail_unread('1 条未读')),
         ]),
    # ---------------- n93 印泥朱砂（深底+朱砂）
    dict(file='n93.html', title='印泥朱砂', eyebrow='LIQUID GLASS · 印', hint='一枚朱砂，落款每一条到账。',
         tone=DARK,
         base='linear-gradient(150deg,#160d0d,#241414 60%,#120b0e)',
         grads=('radial-gradient(ellipse 42% 32% at 20% 24%, rgba(190,60,45,.5), transparent 70%),'
                'radial-gradient(ellipse 38% 30% at 82% 32%, rgba(120,50,60,.4), transparent 70%),'
                'radial-gradient(ellipse 52% 38% at 55% 86%, rgba(60,25,25,.85), transparent 70%)'),
         cardbg='linear-gradient(135deg, rgba(255,255,255,.13), rgba(255,255,255,.05) 48%, rgba(200,90,70,.10))',
         tex='none', sh='rgba(10,4,4,.45)',
         hlang='118deg', hl1='rgba(255,235,225,.32)', hl2='rgba(255,235,225,.07)', hl3='rgba(220,110,90,.16)',
         axt='-60px', axr='-48px', axw='200px', axh='140px', axrot='-16deg', axbg='rgba(220,100,80,.22)',
         prib='linear-gradient(135deg,#b03a26,#7e2418)', pribdr='rgba(220,110,90,.55)',
         progb='rgba(255,255,255,.12)', progf='linear-gradient(90deg,#d86a50,#a83a26)', dotb='#ff7a5c',
         cards=[
             card('验证码', ['付'], None, '付', 'linear-gradient(145deg,#8e4a3a,#5e2f26 60%,#40201a)', '微信支付',
                  '刚刚', '验证码 739182，请勿泄露给他人', tail_unread('')),
             card('支付', ['张'], None, '张', 'linear-gradient(145deg,#a85a3a,#70402a 60%,#4e2c1c)', '转账到账',
                  '18:44', '张刻石向您转账 ¥880.00', tail_unread(''),
                  extra=actions([('查看账单', True)])),
             card('社交', ['白'], None, '白', 'linear-gradient(145deg,#7a5a6a,#4e3a46 60%,#362832)', '新关注',
                  '17:20', '篆刻家白石山关注了你', tail_unread(''),
                  extra=actions([('回关', True), ('忽略', False)])),
         ]),
    # ---------------- n94 雾面磨砂（哑光）
    dict(file='n94.html', title='雾面磨砂', eyebrow='LIQUID GLASS · 雾', hint='雾面之下，消息也放轻了脚步。',
         tone=DARK,
         base='linear-gradient(150deg,#1a1c22,#23262f 60%,#14161b)',
         grads=('radial-gradient(ellipse 40% 30% at 18% 22%, rgba(140,150,170,.35), transparent 70%),'
                'radial-gradient(ellipse 42% 32% at 82% 34%, rgba(110,120,150,.32), transparent 70%),'
                'radial-gradient(ellipse 54% 38% at 55% 86%, rgba(50,55,70,.8), transparent 70%)'),
         cardbg='linear-gradient(135deg, rgba(200,205,215,.16), rgba(200,205,215,.07) 48%, rgba(160,165,180,.08))',
         tex='none', sh='rgba(5,6,10,.4)',
         hlang='118deg', hl1='rgba(255,255,255,.16)', hl2='rgba(255,255,255,.05)', hl3='rgba(190,195,210,.10)',
         axt='-54px', axr='-40px', axw='180px', axh='125px', axrot='-22deg', axbg='rgba(210,215,225,.14)',
         prib='linear-gradient(135deg,#5a6272,#3c424e)', pribdr='rgba(170,178,195,.4)',
         progb='rgba(255,255,255,.10)', progf='linear-gradient(90deg,#9aa2b5,#6a7285)', dotb='#aeb6c8',
         cards=[
             card('邮件', ['邮'], None, '邮', 'linear-gradient(145deg,#6a7285,#484e5c 60%,#33363f)', '收件箱',
                  '11:30', '季度总结的附件已更新，请查收', tail_unread('2 封未读')),
             card('日历', ['会'], None, '会', 'linear-gradient(145deg,#5a6a7e,#3c4450 60%,#2a2f38)', '会议提醒',
                  '10:15', '10:30 评审会 · 三楼会议室', tail_unread('15 分钟后')),
             card('天气', ['霜'], None, '霜', 'linear-gradient(145deg,#7e8a9e,#565e6e 60%,#3c424e)', '霜降',
                  '07:00', '明日降温 8℃，注意添衣保暖', tail_unread('')),
         ]),
    # ---------------- n95 缝线皮革（皮纹）
    dict(file='n95.html', title='缝线皮革', eyebrow='LIQUID GLASS · 革', hint='针脚细密，装得下长途的消息。',
         tone=DARK,
         base='linear-gradient(150deg,#1c130c,#2b1d10 60%,#120c07)',
         grads=('radial-gradient(ellipse 42% 32% at 20% 24%, rgba(160,110,60,.42), transparent 70%),'
                'radial-gradient(ellipse 40% 30% at 82% 32%, rgba(110,75,45,.38), transparent 70%),'
                'radial-gradient(ellipse 52% 38% at 55% 86%, rgba(60,38,20,.85), transparent 70%)'),
         cardbg='linear-gradient(135deg, rgba(220,180,130,.13), rgba(220,180,130,.05) 48%, rgba(160,110,60,.10))',
         tex=('repeating-linear-gradient(45deg, rgba(0,0,0,.10) 0 2px, transparent 2px 7px),'
              'repeating-linear-gradient(-45deg, rgba(0,0,0,.10) 0 2px, transparent 2px 7px)'),
         sh='rgba(12,7,3,.5)',
         hlang='118deg', hl1='rgba(255,230,190,.26)', hl2='rgba(255,230,190,.06)', hl3='rgba(200,150,90,.14)',
         axt='-56px', axr='-44px', axw='185px', axh='128px', axrot='-18deg', axbg='rgba(220,180,130,.18)',
         prib='linear-gradient(135deg,#8a5f34,#5f3f20)', pribdr='rgba(210,160,100,.5)',
         progb='rgba(255,255,255,.10)', progf='linear-gradient(90deg,#c8965a,#8a5f34)', dotb='#e0a860',
         cards=[
             card('订单', ['匠'], None, '匠', 'linear-gradient(145deg,#8a6a42,#5c452a 60%,#40301c)', '皮具定制',
                  '16:40', '您定制的钱包已进入缝制阶段', tail_unread(''),
                  extra=prog(65, '缝制中')),
             card('物流', ['丰'], None, '丰', 'linear-gradient(145deg,#6e5a42,#4a3c2a 60%,#33291c)', '顺丰速运',
                  '14:02', '包裹已到达北京转运中心', tail_unread('')),
             card('会员', ['匠'], None, '会', 'linear-gradient(145deg,#7c5a38,#523c24 60%,#3a2a18)', '匠人俱乐部',
                  '昨天', '您的会员积分将于月底到期', tail_unread(''),
                  extra=actions([('查看权益', True)])),
         ]),
    # ---------------- n96 发丝银（金属拉丝）
    dict(file='n96.html', title='发丝银', eyebrow='LIQUID GLASS · 银', hint='一丝一缕，皆是分明的消息。',
         tone=DARK,
         base='linear-gradient(150deg,#15161a,#202228 60%,#0e0f12)',
         grads=('radial-gradient(ellipse 40% 30% at 18% 22%, rgba(180,185,200,.35), transparent 70%),'
                'radial-gradient(ellipse 42% 32% at 82% 34%, rgba(150,158,180,.32), transparent 70%),'
                'radial-gradient(ellipse 54% 38% at 55% 86%, rgba(70,75,90,.8), transparent 70%)'),
         cardbg='linear-gradient(135deg, rgba(230,235,245,.15), rgba(230,235,245,.06) 48%, rgba(190,195,210,.09))',
         tex=('repeating-linear-gradient(90deg, rgba(255,255,255,.055) 0 1px, transparent 1px 4px),'
              'repeating-linear-gradient(0deg, rgba(0,0,0,.05) 0 1px, transparent 1px 5px)'),
         sh='rgba(5,6,8,.42)',
         hlang='118deg', hl1='rgba(255,255,255,.34)', hl2='rgba(255,255,255,.08)', hl3='rgba(200,205,220,.16)',
         axt='-58px', axr='-42px', axw='190px', axh='130px', axrot='-20deg', axbg='rgba(230,235,245,.20)',
         prib='linear-gradient(135deg,#8a93a8,#5c6376)', pribdr='rgba(200,208,225,.5)',
         progb='rgba(255,255,255,.10)', progf='linear-gradient(90deg,#c2c9da,#8a93a8)', dotb='#d5dbe8',
         cards=[
             card('音乐', ['琴'], None, '琴', 'linear-gradient(145deg,#7a8296,#4e5464 60%,#363a46)', '正在播放',
                  '现在', '《高山流水》· 古琴独奏', tail_unread(''),
                  extra=actions([('暂停', True), ('下一首', False)])),
             card('系统', ['iO'], None, '更', 'linear-gradient(145deg,#8a93a8,#5c6376 60%,#414654)', 'iOS 更新',
                  '09:12', 'iOS 27.1 可用，建议 Wi-Fi 下更新', tail_unread(''),
                  extra=prog(38, '下载中')),
             card('运动', ['步'], None, '步', 'linear-gradient(145deg,#6a7a8e,#465060 60%,#323842)', '今日步数',
                  '18:00', '已走 8,632 步，超过 82% 的朋友', tail_unread('')),
         ]),
    # ---------------- n97 瓷上冰裂（青瓷冰裂纹）
    dict(file='n97.html', title='瓷上冰裂', eyebrow='LIQUID GLASS · 瓷', hint='开片有声，消息如冰裂般清脆。',
         tone=DARK,
         base='linear-gradient(150deg,#0f1a18,#182826 60%,#0a1413)',
         grads=('radial-gradient(ellipse 42% 32% at 20% 24%, rgba(120,180,165,.4), transparent 70%),'
                'radial-gradient(ellipse 40% 30% at 82% 32%, rgba(90,140,150,.36), transparent 70%),'
                'radial-gradient(ellipse 52% 38% at 55% 86%, rgba(35,60,58,.85), transparent 70%)'),
         cardbg='linear-gradient(135deg, rgba(220,240,235,.14), rgba(220,240,235,.06) 48%, rgba(140,180,170,.10))',
         tex=('url("data:image/svg+xml,%3Csvg xmlns=\'http://www.w3.org/2000/svg\' width=\'220\' height=\'220\'%3E'
              '%3Cg stroke=\'%23ffffff\' stroke-opacity=\'0.16\' fill=\'none\' stroke-width=\'1\'%3E'
              '%3Cpath d=\'M12 24 L64 74 L58 134 L104 186\'/%3E'
              '%3Cpath d=\'M64 74 L124 64 L174 104\'/%3E'
              '%3Cpath d=\'M58 134 L22 176\'/%3E'
              '%3Cpath d=\'M124 64 L144 12 L196 44\'/%3E'
              '%3Cpath d=\'M174 104 L150 160 L190 200\'/%3E%3C/g%3E%3C/svg%3E")'),
         sh='rgba(4,10,9,.45)',
         hlang='118deg', hl1='rgba(235,250,245,.30)', hl2='rgba(235,250,245,.07)', hl3='rgba(150,200,190,.15)',
         axt='-56px', axr='-38px', axw='180px', axh='126px', axrot='-26deg', axbg='rgba(220,245,238,.18)',
         prib='linear-gradient(135deg,#4e8a80,#2e5a54)', pribdr='rgba(150,200,190,.5)',
         progb='rgba(255,255,255,.10)', progf='linear-gradient(90deg,#8ac0b4,#4e8a80)', dotb='#9ad8c8',
         cards=[
             card('拍卖', ['嘉'], None, '嘉', 'linear-gradient(145deg,#5a8a80,#3a5a54 60%,#283c38)', '嘉德拍卖',
                  '14:00', '您关注的南宋哥窑盘口瓶即将开拍', tail_unread(''),
                  extra=actions([('进入直播', True)])),
             card('订单', ['窑'], None, '窑', 'linear-gradient(145deg,#6a9a90,#465e5a 60%,#323e3c)', '景德镇',
                  '11:26', '您拍下的青瓷茶盏已发货', tail_unread('')),
             card('群聊', ['陈'], None, '陈', 'linear-gradient(145deg,#4e7a72,#324e4a 60%,#233532)', '瓷器雅集',
                  '昨天', '老陈分享了一件开片冰裂纹笔洗', tail_unread('6 条未读')),
         ]),
    # ---------------- n98 钴蓝青花（青花瓷）
    dict(file='n98.html', title='钴蓝青花', eyebrow='LIQUID GLASS · 青', hint='青花一笔，勾出消息的轮廓。',
         tone=DARK,
         base='linear-gradient(150deg,#0d1424,#16233c 60%,#0a0f1e)',
         grads=('radial-gradient(ellipse 42% 32% at 20% 24%, rgba(70,110,190,.5), transparent 70%),'
                'radial-gradient(ellipse 40% 30% at 82% 32%, rgba(50,90,170,.45), transparent 70%),'
                'radial-gradient(ellipse 52% 38% at 55% 86%, rgba(25,40,80,.85), transparent 70%)'),
         cardbg='linear-gradient(135deg, rgba(235,242,255,.15), rgba(235,242,255,.06) 48%, rgba(120,150,220,.11))',
         tex='none', sh='rgba(5,8,18,.45)',
         hlang='118deg', hl1='rgba(235,242,255,.32)', hl2='rgba(235,242,255,.07)', hl3='rgba(130,160,230,.16)',
         axt='-60px', axr='-44px', axw='195px', axh='135px', axrot='-18deg', axbg='rgba(180,200,250,.20)',
         prib='linear-gradient(135deg,#3a5f9e,#26406e)', pribdr='rgba(140,170,240,.55)',
         progb='rgba(255,255,255,.10)', progf='linear-gradient(90deg,#7a9ed8,#3a5f9e)', dotb='#9ab8f0',
         cards=[
             card('天气', ['雨'], None, '雨', 'linear-gradient(145deg,#4a6a9e,#30486e 60%,#22344e)', '暴雨预警',
                  '07:30', '未来 2 小时有强降雨，请注意防范', tail_unread(''),
                  extra=actions([('查看详情', True)])),
             card('航班', ['航'], None, '航', 'linear-gradient(145deg,#5a7aae,#3c547e 60%,#2a3c5a)', '国航 CA1831',
                  '08:15', '登机口变更为 D27，请前往登机', tail_unread('重要')),
             card('日程', ['茶'], None, '茶', 'linear-gradient(145deg,#3e5a94,#2a3f68 60%,#1e2c48)', '青花雅集',
                  '周日', '周日青花雅集 · 颐和园听鹂馆', tail_unread('')),
         ]),
    # ---------------- n99 淡墨生宣（近白极简）
    dict(file='n99.html', title='淡墨生宣', eyebrow='LIQUID GLASS · 淡', hint='淡到极处，消息自有回甘。',
         tone=LIGHT,
         base='linear-gradient(150deg,#fbfaf6,#f4f1e9 60%,#ece8db)',
         grads=('radial-gradient(ellipse 40% 30% at 16% 20%, rgba(170,160,145,.25), transparent 70%),'
                'radial-gradient(ellipse 42% 32% at 84% 34%, rgba(150,160,175,.22), transparent 70%),'
                'radial-gradient(ellipse 50% 36% at 55% 88%, rgba(160,150,135,.18), transparent 70%)'),
         cardbg='linear-gradient(135deg, rgba(255,255,255,.6), rgba(255,255,255,.32) 48%, rgba(235,228,214,.4))',
         tex='none', sh='rgba(100,90,70,.14)',
         hlang='118deg', hl1='rgba(255,255,255,.75)', hl2='rgba(255,255,255,.28)', hl3='rgba(190,180,165,.28)',
         axt='-50px', axr='-34px', axw='165px', axh='118px', axrot='-28deg', axbg='rgba(255,255,255,.55)',
         prib='linear-gradient(135deg,#6a6558,#4a463c)', pribdr='rgba(100,95,85,.45)',
         progb='rgba(80,75,65,.12)', progf='linear-gradient(90deg,#8a8474,#5f5a4e)', dotb='#8a7a5a',
         cards=[
             card('读书', ['读'], None, '读', 'linear-gradient(145deg,#8a8474,#5f5a4e 60%,#443f35)', '微信读书',
                  '22:10', '《长安的荔枝》已读到 62%', tail_unread(''),
                  extra=prog(62, '阅读进度')),
             card('专注', ['汐'], None, '汐', 'linear-gradient(145deg,#7a8a96,#525c66 60%,#3a4048)', '潮汐',
                  '21:00', '今日已专注 25 分钟，继续保持', tail_unread('')),
             card('备忘', ['记'], None, '记', 'linear-gradient(145deg,#9a8a72,#6e6452 60%,#4e483a)', '提醒事项',
                  '明天', '记得给阳台的兰花浇水', tail_unread('')),
         ]),
    # ---------------- n100 铜锈青铜（青铜+铜绿）
    dict(file='n100.html', title='铜锈青铜', eyebrow='LIQUID GLASS · 铜', hint='千年铜绿，锈住时间的消息。',
         tone=DARK,
         base='linear-gradient(150deg,#141210,#221d14 60%,#0d0b08)',
         grads=('radial-gradient(ellipse 42% 32% at 20% 24%, rgba(90,140,120,.4), transparent 70%),'
                'radial-gradient(ellipse 40% 30% at 82% 32%, rgba(150,110,60,.38), transparent 70%),'
                'radial-gradient(ellipse 52% 38% at 55% 86%, rgba(55,45,28,.85), transparent 70%)'),
         cardbg='linear-gradient(135deg, rgba(230,210,170,.13), rgba(230,210,170,.05) 48%, rgba(120,150,130,.10))',
         tex=('url("data:image/svg+xml,%3Csvg xmlns=\'http://www.w3.org/2000/svg\' width=\'140\' height=\'140\'%3E'
              '%3Cfilter id=\'n\'%3E%3CfeTurbulence type=\'fractalNoise\' baseFrequency=\'0.7\' numOctaves=\'2\'/%3E'
              '%3C/filter%3E%3Crect width=\'140\' height=\'140\' filter=\'url(%23n)\' opacity=\'0.12\'/%3E%3C/svg%3E")'),
         sh='rgba(10,7,4,.5)',
         hlang='118deg', hl1='rgba(240,225,190,.28)', hl2='rgba(240,225,190,.06)', hl3='rgba(140,170,150,.15)',
         axt='-58px', axr='-40px', axw='188px', axh='130px', axrot='-21deg', axbg='rgba(200,190,150,.18)',
         prib='linear-gradient(135deg,#7a6a45,#4e4228)', pribdr='rgba(200,175,120,.5)',
         progb='rgba(255,255,255,.10)', progf='linear-gradient(90deg,#a8945f,#6e5f38)', dotb='#c8a860',
         cards=[
             card('银行', ['工'], None, '工', 'linear-gradient(145deg,#8a7a52,#5c4f34 60%,#413724)', '工商银行',
                  '13:45', '尾号 8821 支出 ¥1,200.00', tail_unread('')),
             card('基金', ['定'], None, '定', 'linear-gradient(145deg,#6e8a72,#485c48 60%,#333f34)', '定投',
                  '09:00', '本月定投已扣款成功', tail_unread('')),
             card('安全', ['安'], None, '安', 'linear-gradient(145deg,#9a7a52,#6a5436 60%,#4a3c26)', '安全中心',
                  '昨天', '新设备登录提醒 · iPhone 17', tail_unread(''),
                  extra=actions([('查看详情', True), ('是我本人', False)])),
         ]),
]

CSS_VARS = ['ink', 'mut', 'unr', 'hi', 'bd', 'bdh', 'bd2', 'pbd', 'pbg', 'pink',
            'abd', 'fbd', 'bbd', 'bbg', 'bink', 'fallback']


def build(t):
    v = dict(t['tone'])
    v.update({k: t[k] for k in
              ('base', 'grads', 'cardbg', 'tex', 'sh', 'hlang', 'hl1', 'hl2', 'hl3',
               'axt', 'axr', 'axw', 'axh', 'axrot', 'axbg',
               'prib', 'pribdr', 'progb', 'progf', 'dotb')})
    css = CSS
    css = css.replace('VARink', v['ink']).replace('VARmut', v['mut']).replace('VARunr', v['unr'])
    css = css.replace('VARhi', v['hi']).replace('VARbdh', v['bdh']).replace('VARbd2', v['bd2'])
    css = css.replace('VARbd', v['bd'])
    css = css.replace('VARpbd', v['pbd']).replace('VARpbg', v['pbg']).replace('VARpink', v['pink'])
    css = css.replace('VARabd', v['abd']).replace('VARfbd', v['fbd'])
    css = css.replace('VARbbd', v['bbd']).replace('VARbbg', v['bbg']).replace('VARbink', v['bink'])
    css = css.replace('VARfallback', v['fallback'])
    css = css.replace('VARbase', v['base']).replace('VARgrads', v['grads'])
    css = css.replace('VARcardbg', v['cardbg']).replace('VARtex', v['tex']).replace('VARsh', v['sh'])
    css = css.replace('VARhlang', v['hlang']).replace('VARhl1', v['hl1'])
    css = css.replace('VARhl2', v['hl2']).replace('VARhl3', v['hl3'])
    css = css.replace('VARaxt', v['axt']).replace('VARaxr', v['axr']).replace('VARaxw', v['axw'])
    css = css.replace('VARaxh', v['axh']).replace('VARaxrot', v['axrot']).replace('VARaxbg', v['axbg'])
    css = css.replace('VARpribg', v['prib']).replace('VARpribd', v['pribdr'])
    css = css.replace('VARprogbg', v['progb']).replace('VARprogfg', v['progf'])
    css = css.replace('VARdotbg', v['dotb'])
    # .prog i width var: keep literal VARpw replaced per-card below
    css = css.replace('VARpw', '0%')
    cards_html = '\n'.join(t['cards'])
    # per-card progress widths already inline
    html = SHELL.format(title=t['title'], css=css, eyebrow=t['eyebrow'],
                        h1=t['title'], hint=t['hint'], cards=cards_html)
    return html


def main():
    titles = []
    for t in THEMES:
        html = build(t)
        assert 'VAR' not in html, 'unreplaced var in ' + t['file']
        path = os.path.join(OUT, t['file'])
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        titles.append({'file': t['file'], 'title': t['title']})
        print('wrote', t['file'], len(html) // 1024, 'KB')
    import json
    with open(os.path.join(OUT, '_titles_nc_j.json'), 'w', encoding='utf-8') as f:
        json.dump(titles, f, ensure_ascii=False, indent=1)
    print('wrote _titles_nc_j.json')


if __name__ == '__main__':
    main()
