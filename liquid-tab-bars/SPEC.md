# 液态玻璃 100 Tab · 底部栏构建规范

照用户给的「心电图」代码骨架（见本目录 `template.html`），做 100 个**液态玻璃**风格的底部 Tab 栏，每个独立单文件。

## 固定骨架（照抄 template.html）

- 430×900 `.phone` 壳，`.hd` 头部（标题 + 副标题）、`.bd` 骨架屏卡片（`--bg/--hd1/--cx/--cb` 可调）、底部 `.tabbar` + `.tab` 按钮。
- 图标：内联 SVG（4–5 个），标签：首页/发现/消息/我的（可按主题微调，如 首页/灵感/发布/消息/我的）。
- JS：从 LBL/IC 生成 tab、点击切换 `.on`、支持 `?tab=` 深链（照抄模板 JS 逻辑）。
- 每个文件有独特的 body class（如 `g37`）承载该款的专属样式。

## 液态玻璃要求（100 款必须各不相同）

- 质感：毛玻璃 `backdrop-filter: blur+saturate`、顶部内高光、底部倒影、折射边缘光、液态流动渐变。
- 布局变化：贴底全宽 / 悬浮胶囊 / 悬浮圆角大卡 / 分段式 / 双层玻璃 / 中岛式 / 侧边胶囊+底部组合……
- 激活态变化：液滴上浮指示 / 滑动光条 / 图标发光投影 / 胶囊包裹 / 文字浮现 / 果冻回弹 / 呼吸光点 / 彩虹描边……
- 色系变化：霜雾白 / 深海蓝 / 霓虹紫 / 蜜桃粉 / 薄荷青 / 熔岩橙 / 水银银 / 墨黑 / 奶白 / 冰晶蓝 ……（深浅底交替）
- 100 款分 10 组（每人 10 款），组内也要肉眼可区分，不许换个颜色就交差。

## 交付

- 目录 `~/workspace/liquid-tab-bars/`，文件 `g01.html`–`g100.html`（每人负责的编号段见任务）。
- 每人写 `_titles_tab_<a|b|c|d|e|f|g|h|i|j>.json`：`[{"file":"g01.html","title":"标题"}]`，标题 2–6 字，**不许**与已有 bottombar 标题重名（f01–f36 行星光环/幻彩旋光等、d01–d22 已存在，完工后我统一查重改名）。
- 完工后每款用 headless chrome 截图（430×900）亲自看过、无空白错位再交：
  `/home/hatch/.cache/ms-playwright/chromium_headless_shell-1243/chrome-headless-shell-linux64/chrome-headless-shell --no-sandbox --disable-gpu --window-size=430,900 --virtual-time-budget=5000 --screenshot=/tmp/x.png "file://<文件>"`
- 动画用负延迟/both 保证截图饱满；`<i>` 设宽高先 `display:block`；零外部资源。
