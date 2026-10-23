# 液态 · App套装 SPEC（12 套）

用户脚手架 `~/workspace/liquid-glass-scaffold/setup-liquid-glass.sh` 的微信聊天列表液态玻璃版，
扩展为 12 套完整 App 界面系列。token 必须严格沿用脚手架配方。

## 文件
`~/workspace/liquid-glass-apps/g01-chat.html` … `g12-files.html`，单文件、纯手写 CSS、无框架。

| 文件 | 标题 | 内容 |
|---|---|---|
| g01-chat.html | 聊天列表 | 还原脚手架 App.vue：msg-card + 群聊/企业好友/未读/分组 FolderCard，ChatRow |
| g02-music.html | 音乐播放器 | 专辑封面玻璃卡、进度条、播放控制、播放列表 |
| g03-weather.html | 天气预报 | 大温度、逐小时、7 日预报 |
| g04-photos.html | 精选相册 | 照片网格（CSS 渐变占位图）、相簿行 |
| g05-settings.html | 设置中心 | 设置列表行 + 开关、头像区 |
| g06-wallet.html | 钱包支付 | 余额卡、收付款按钮、账单列表 |
| g07-calendar.html | 日历日程 | 月历 + 当日日程 |
| g08-moments.html | 朋友圈 | 动态 feed（头像/文字/九宫格占位/点赞） |
| g09-dialer.html | 拨号通话 | 拨号盘、通话记录 |
| g10-fitness.html | 运动健康 | 活动圆环、数据卡 |
| g11-clock.html | 时钟闹钟 | 大时钟、闹钟列表（开关） |
| g12-files.html | 文件管理 | 文件网格/列表、存储用量条 |

## Token（照抄脚手架，一字不差）
```
--glass-radius:34px; --glass-blur:24px;
--glass-tint-top:rgba(255,255,255,.17); --glass-tint-mid:rgba(255,255,255,.05); --glass-tint-bot:rgba(255,255,255,.10);
--glass-edge-width:1.2px;
--glass-edge-strong:rgba(255,255,255,.95); --glass-edge-mid:rgba(255,255,255,.22);
--glass-edge-weak:rgba(255,255,255,.05); --glass-edge-mid2:rgba(255,255,255,.12); --glass-edge-soft:rgba(255,255,255,.78);
--glass-shadow-far:0 26px 60px -26px rgba(0,0,0,.85); --glass-shadow-near:0 10px 26px -14px rgba(0,0,0,.55);
--text-1:#fff; --text-2:rgba(255,255,255,.62); --text-3:rgba(255,255,255,.60);
--ease-liquid:cubic-bezier(.22,.9,.28,1.2);
```
.lg 卡片 = 155deg tint 渐变 + backdrop blur(24px) saturate(180%) brightness(1.06) +
inset 三层高光 + far/near 阴影；::before 液面高光（screen 混合）；::after 1.2px 渐变描边
（padding  trick + mask-composite: exclude，Chrome 加 -webkit-mask-composite: xor）。

## 壁纸
照抄 LiquidWallpaper.vue：#140a20 底 + 5 团径向色光（#ff3b5c/#ff9f1c/#ff2d55/#6b5cff/#ffd166），
blur(48px) saturate(150%)，drift 26s infinite alternate；第二层 conic 彩虹 blur(110px) opacity .5
screen 混合，34s alternate-reverse。无限动画，截图安全。

## 页面结构（每个文件）
- body 背景 #07060b；.wallpaper fixed 全屏
- .screen：宽 430、高 900，居中，padding-top 56（含状态栏），内容区可滚动
- 状态栏：9:41 / 信号/WiFi/电池（纯 CSS/字符）
- 顶部大标题 + 内容 .lg 卡片若干 + 底部 home 指示条
- 小尺寸变体用行内 style 改 --lg-r / --lg-blur（如小按钮 radius 999px）

## 约束
- 全部中文原创文案，不抄脚手架里的微信占位名（Umi/Lui 等一律换掉）
- 头像用 conic 渐变圆（照抄 Avatar.vue），照片用 CSS 渐变占位
- 容器有限动画必须在 6 秒内结束（无限 drift 除外）；不要用 startViewTransition
- 每个文件 <title> 为中文标题
