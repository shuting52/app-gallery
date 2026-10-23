# 216 组新鲜 UI 设计 · 构建规范

目标：6 大类 × 36 组 = 216 组，全部单文件 HTML，纯手写 CSS（无框架、无 Tailwind CDN、无 Google Fonts，系统字体回退），内联 SVG 装饰，零外部资源。

## 目录与文件

```
~/workspace/fresh-ui/
  splash/     启动页      s01.html … s36.html
  topbar/     顶部栏      h01.html … h36.html
  bottombar/  底部栏      f01.html … f36.html
  welcome/    欢迎弹窗    w01.html … w36.html
  update/    更新弹窗    u01.html … u36.html
  appscreen/  App界面     a01.html … a36.html
```

每类由 2 个 agent 分工：A 负责 01–18，B 负责 19–36。
每人产出 `_titles_<类>_a.json` / `_titles_<类>_b.json`，格式：
`[{"file":"s01.html","title":"星河启程"}, …]`（顺序即展示顺序）

## 通用铁律

1. 单文件、UTF-8；`<meta viewport>`；页面尺寸按 **430×900** 设计（画廊截图即此尺寸）。
2. 酷炫 CSS 动态特效：keyframes / transition 为主；**截图在虚拟时间约 6 秒抓取且动画会冻结**——首屏必须用 `animation-delay: -2s`（负延迟）或 `both/forwards` 让截图瞬间画面已饱满好看；避免"前 2 秒空白再出场"的设计。
3. 文案全部原创，2–6 字标题，类内 36 个标题互不重复、风格词不扎堆。
4. 行内元素（`<i>`/`<span>`）要设宽高必须先 `display:block/inline-block`。
5. 开关类组件（如有）`.switch` 必须 `position:relative` + 固定宽高。
6. 每个 agent 完工后用 headless chrome 抽查 2 个文件截图，空白/报错必须修好再交：
   `/home/hatch/.cache/ms-playwright/chromium_headless_shell-1243/chrome-headless-shell-linux64/chrome-headless-shell --no-sandbox --disable-gpu --window-size=430,900 --virtual-time-budget=6000 --screenshot=/tmp/x.png "file:///home/hatch/workspace/fresh-ui/<类>/<文件>"`

## 各类展示形态

- **splash 启动页**：整屏 430×900 开场动画（Logo 演绎 / 进度 / 粒子 / 液体 / 翻页等 36 种不同概念），3s 左右，结束后停在品牌页或循环；加"重新播放"按钮。
- **topbar 顶部栏**：430×900 mock App（简单内容列表打底）+ 顶部导航栏。36 种：大标题收缩 / 搜索框融合 / 毛玻璃 / 分段切换 / 双排信息 / 沉浸透明随滚动实化等。滚动内容时顶栏要有动效。
- **bottombar 底部栏**：mock App 上下文 + 底部 4–5 个 tab，可点击切换（激活态动效），支持 `?tab=N` 深链。**必须与 `~/workspace/tab-bars/manifest.json` 里 22 款不重样**（先读一遍它的 title）。
- **welcome 欢迎弹窗**：mock App 背景（模糊）+ 中央欢迎弹窗：新人礼 / 功能导览 / 权限请求 / 会员开通等 36 种。入场动画 + 可关闭/行动按钮可用 + "重新弹出"按钮。
- **update 更新弹窗**：mock App 背景 + 更新弹窗：版本号/更新日志/进度条/立即更新 36 种新鲜演绎。**必须与 `~/workspace/update-modals/` 的 m01–m30 不重样**（读一遍 manifest title）。
- **appscreen App界面**：完整单屏 App 界面：音乐/天气/健身/阅读/社交/番茄钟等任选 36 种不同产品，带微交互（可点、可滑）。

## 验收标准

- 36 文件齐、json 顺序与文件对应、title 无重复。
- 抽查截图：首屏饱满、无空白、无横向溢出、无 console 级报错（肉眼）。
- 动效在真机浏览器流畅（transform/opacity 为主，避免重排动画）。
