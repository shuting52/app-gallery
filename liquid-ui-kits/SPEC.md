# 液态 UI 主题 · 全套组件库构建规范（10 套）

每套 = 单文件 HTML，全套组件库 Demo，纯手写 CSS（无框架、无 Tailwind CDN、无 Google Fonts，系统字体回退），零外部资源。

## 固定结构（照抄 star-ui-kit/star-ui.html 的骨架）

- 5 个 Tab：`home` 总览 / `buttons` 按钮 / `forms` 表单 / `showcase` 展示 / `feedback` 反馈（`data-tab` 取值固定为这 5 个）。
- 底部悬浮胶囊 Tab 栏 + 滑动指示 pill，点击切换；支持 `?tab=` 深链（如 `?tab=buttons`）。
- 约 30 个组件，分布：
  - 总览：主题介绍卡 + 色板 + 字体展示 + 快速导航
  - 按钮：主/次/幽灵/危险/图标按钮、加载中按钮、液态特效按钮（波纹/填充/磁吸等）
  - 表单：输入框、搜索框、文本域、选择器、下拉、开关、复选、单选、滑块、步进器、评分、上传
  - 展示：头像、徽标、标签、卡片、列表项、轮播、折叠面板、表格、空状态、骨架屏
  - 反馈：Toast、弹窗、抽屉、进度条、加载动画、气泡提示、结果页
- 全部交互可用（开关可拨、Tab 可点、弹窗可开合）。

## 液态主题要求

- 整套围绕"液态"做设计语言：玻璃拟态、流体渐变、波纹、气泡、液滴、折射高光、backdrop-filter 毛玻璃。
- 10 套方向（每人 1 套，目录名固定）：
  1. `ocean/` 深海液态 —— 深蓝 + 生物荧光
  2. `mercury/` 水银流体 —— 银灰镜面 + 液态金属
  3. `jelly/` 果冻水滴 —— 糖果色 + Q 弹水滴
  4. `aurora/` 极光流体 —— 暗底 + 极光渐变
  5. `lava/` 熔岩流体 —— 暗底 + 熔岩橙红流动
  6. `soda/` 气泡苏打 —— 清爽薄荷 + 上浮气泡
  7. `ink/` 墨水晕染 —— 宣纸白 + 水墨晕染
  8. `frost/` 冰晶液态 —— 冰蓝 + 霜纹玻璃
  9. `honey/` 蜂蜜流体 —— 琥珀 + 粘稠流淌
  10. `neon/` 霓虹液态 —— 暗底 + 霓虹液光
- 每套要有独特的液态招牌动效（如水滴按钮、波浪进度条、气泡 Toast），10 套之间视觉语言明显区分。
- 文案原创，标题格式如「OCEAN UI · 深海液态」。

## 交付

- 目录 `~/workspace/liquid-ui-kits/<ocean|mercury|jelly|aurora|lava|soda|ink|frost|honey|neon>/`
- 文件名为 `<name>-ui.html`（如 `ocean-ui.html`）
- 附 `manifest.json`：`[{"file":"ocean-ui.html","title":"OCEAN UI · 深海液态"}]`
- 完工后用 headless chrome 逐 Tab 截图（5 张，`?tab=` 切换），亲自看过、无空白错位再交：
  `/home/hatch/.cache/ms-playwright/chromium_headless_shell-1243/chrome-headless-shell-linux64/chrome-headless-shell --no-sandbox --disable-gpu --window-size=430,900 --virtual-time-budget=5000 --screenshot=/tmp/x.png "file://<文件>?tab=buttons"`
- 注意 headless  quirks：虚拟时间下 transition 冻结、rAF 可能饿死——首屏用 `both/forwards` 或负延迟保证截图饱满；`<i>` 设宽高先 `display:block`。
