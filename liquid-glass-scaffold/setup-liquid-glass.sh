#!/usr/bin/env bash
# ============================================================
#  Liquid Glass · Vue3 + Vite 项目脚手架
#  用法：
#     bash setup-liquid-glass.sh            # 生成到 ./liquid-glass
#     bash setup-liquid-glass.sh my-app     # 生成到 ./my-app
#  来源：用户 2026-10-23 00:07 粘贴（微信聊天列表液态玻璃版）
# ============================================================
set -euo pipefail

ROOT="${1:-liquid-glass}"
mkdir -p "$ROOT/src/components" "$ROOT/src/styles"
echo "→ 生成到: $ROOT"

# ------------------------------------------------ package.json
cat > "$ROOT/package.json" <<'VEOF'
{
  "name": "liquid-glass",
  "private": true,
  "version": "0.1.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "vue": "^3.5.13"
  },
  "devDependencies": {
    "@vitejs/plugin-vue": "^5.2.1",
    "vite": "^6.0.7"
  }
}
VEOF

# ------------------------------------------------ vite.config.js
cat > "$ROOT/vite.config.js" <<'VEOF'
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { fileURLToPath, URL } from 'node:url'

export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: { '@': fileURLToPath(new URL('./src', import.meta.url)) }
  },
  server: { host: true, port: 5173 }
})
VEOF

# ------------------------------------------------ .gitignore
cat > "$ROOT/.gitignore" <<'VEOF'
node_modules
dist
.DS_Store
*.local
VEOF

# ------------------------------------------------ index.html
cat > "$ROOT/index.html" <<'VEOF'
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover" />
  <meta name="theme-color" content="#07060b" />
  <title>Liquid Glass</title>
</head>
<body>
  <div id="app"></div>
  <script type="module" src="/src/main.js"></script>
</body>
</html>
VEOF

# ------------------------------------------------ src/main.js
cat > "$ROOT/src/main.js" <<'VEOF'
import { createApp } from 'vue'
import App from './App.vue'
import './styles/tokens.css'
import './styles/base.css'

createApp(App).mount('#app')
VEOF

# ------------------------------------------------ tokens.css
cat > "$ROOT/src/styles/tokens.css" <<'VEOF'
:root {
  /* ---- 玻璃材质 ---- */
  --glass-radius: 34px;
  --glass-blur: 24px;
  --glass-tint-top: rgba(255, 255, 255, .17);
  --glass-tint-mid: rgba(255, 255, 255, .05);
  --glass-tint-bot: rgba(255, 255, 255, .10);

  /* ---- 渐变描边 ---- */
  --glass-edge-width: 1.2px;
  --glass-edge-strong: rgba(255, 255, 255, .95);
  --glass-edge-mid:    rgba(255, 255, 255, .22);
  --glass-edge-weak:   rgba(255, 255, 255, .05);
  --glass-edge-mid2:   rgba(255, 255, 255, .12);
  --glass-edge-soft:   rgba(255, 255, 255, .78);

  /* ---- 投影 ---- */
  --glass-shadow-far:  0 26px 60px -26px rgba(0, 0, 0, .85);
  --glass-shadow-near: 0 10px 26px -14px rgba(0, 0, 0, .55);

  /* ---- 文字 ---- */
  --text-1: #fff;
  --text-2: rgba(255, 255, 255, .62);
  --text-3: rgba(255, 255, 255, .60);

  /* ---- 布局 ---- */
  --app-max: 430px;
  --gap: 14px;

  /* ---- 动效 ---- */
  --ease-liquid: cubic-bezier(.22, .9, .28, 1.2);
}
VEOF

# ------------------------------------------------ base.css
cat > "$ROOT/src/styles/base.css" <<'VEOF'
*, *::before, *::after { box-sizing: border-box }
html, body, #app { height: 100% }

body {
  margin: 0;
  font: 400 15px/1.45 -apple-system, BlinkMacSystemFont, "SF Pro Text",
        "PingFang SC", "Helvetica Neue", system-ui, sans-serif;
  color: var(--text-1);
  background: #07060b;
  overflow-x: hidden;
  -webkit-font-smoothing: antialiased;
  -webkit-tap-highlight-color: transparent;
}

.app {
  position: relative;
  z-index: 1;
  max-width: var(--app-max);
  margin: 0 auto;
  padding: 56px 14px 120px;
  display: grid;
  gap: var(--gap);
}

@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: .01ms !important;
    transition-duration: .01ms !important;
  }
}
VEOF

# ------------------------------------------------ LiquidGlass.vue
cat > "$ROOT/src/components/LiquidGlass.vue" <<'VEOF'
<template>
  <component
    :is="tag"
    class="lg"
    :class="{ 'lg--press': pressable }"
    :style="styleVars"
  >
    <slot />
  </component>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  tag:       { type: String,  default: 'section' },
  radius:    { type: Number,  default: 0 },   // 0 = 使用全局 --glass-radius
  blur:      { type: Number,  default: 0 },   // 0 = 使用全局 --glass-blur
  pressable: { type: Boolean, default: true }
})

const styleVars = computed(() => {
  const v = {}
  if (props.radius) v['--lg-r'] = props.radius + 'px'
  if (props.blur) v['--lg-blur'] = props.blur + 'px'
  return v
})
</script>

<style scoped>
.lg {
  position: relative;
  isolation: isolate;
  border-radius: var(--lg-r, var(--glass-radius));
  background: linear-gradient(
    155deg,
    var(--glass-tint-top) 0%,
    var(--glass-tint-mid) 42%,
    var(--glass-tint-bot) 100%
  );
  -webkit-backdrop-filter: blur(var(--lg-blur, var(--glass-blur))) saturate(180%) brightness(1.06);
          backdrop-filter: blur(var(--lg-blur, var(--glass-blur))) saturate(180%) brightness(1.06);
  box-shadow:
    inset 0  1px 1px -0.5px rgba(255, 255, 255, .70),
    inset 0 -1px 1px -0.5px rgba(255, 255, 255, .18),
    inset 0 14px 22px -14px rgba(255, 255, 255, .45),
    var(--glass-shadow-far),
    var(--glass-shadow-near);
  transition: transform .38s var(--ease-liquid);
}

.lg--press:active { transform: scale(.982) }

/* 液面高光（在内容下方） */
.lg::before {
  content: "";
  position: absolute;
  inset: 0;
  z-index: -1;
  border-radius: inherit;
  pointer-events: none;
  mix-blend-mode: screen;
  opacity: .85;
  background:
    radial-gradient(120% 62% at 18% -26%, rgba(255, 255, 255, .78), transparent 58%),
    radial-gradient(70% 46% at 92% -12%, rgba(255, 255, 255, .34), transparent 60%),
    repeating-linear-gradient(102deg, rgba(255, 255, 255, .055) 0 2px, transparent 2px 26px);
}

/* 渐变描边：padding 做边宽，mask 挖空中间 */
.lg::after {
  content: "";
  position: absolute;
  inset: 0;
  z-index: 1;
  border-radius: inherit;
  padding: var(--glass-edge-width);
  pointer-events: none;
  background: linear-gradient(
    150deg,
    var(--glass-edge-strong) 0%,
    var(--glass-edge-mid) 22%,
    var(--glass-edge-weak) 48%,
    var(--glass-edge-mid2) 72%,
    var(--glass-edge-soft) 100%
  );
  -webkit-mask: linear-gradient(#000 0 0) content-box, linear-gradient(#000 0 0);
          mask: linear-gradient(#000 0 0) content-box, linear-gradient(#000 0 0);
  -webkit-mask-composite: xor;
          mask-composite: exclude;
}
</style>
VEOF

# ------------------------------------------------ LiquidWallpaper.vue
cat > "$ROOT/src/components/LiquidWallpaper.vue" <<'VEOF'
<template>
  <div class="wallpaper" aria-hidden="true"><i /><i /></div>
</template>

<style scoped>
.wallpaper {
  position: fixed;
  inset: 0;
  z-index: 0;
  overflow: hidden;
  pointer-events: none;
}

.wallpaper i {
  position: absolute;
  inset: -30%;
  display: block;
  background:
    radial-gradient(42% 32% at 20% 22%, #ff3b5c 0%, transparent 62%),
    radial-gradient(38% 30% at 84% 16%, #ff9f1c 0%, transparent 60%),
    radial-gradient(52% 42% at 76% 74%, #ff2d55 0%, transparent 64%),
    radial-gradient(42% 38% at 24% 82%, #6b5cff 0%, transparent 62%),
    radial-gradient(30% 26% at 52% 48%, #ffd166 0%, transparent 68%),
    #140a20;
  filter: blur(48px) saturate(150%);
  animation: drift 26s ease-in-out infinite alternate;
}

.wallpaper i:nth-child(2) {
  background: conic-gradient(from 200deg at 50% 55%,
    #ff2d55, #ff9f0a, #ffd60a, #34c759, #0a84ff, #bf5af2, #ff2d55);
  filter: blur(110px);
  opacity: .5;
  mix-blend-mode: screen;
  animation-duration: 34s;
  animation-direction: alternate-reverse;
}

@keyframes drift {
  from { transform: translate3d(-3%, -2%, 0) scale(1.05) rotate(-3deg) }
  to   { transform: translate3d(4%, 3%, 0) scale(1.16) rotate(4deg) }
}
</style>
VEOF

# ------------------------------------------------ Avatar.vue
cat > "$ROOT/src/components/Avatar.vue" <<'VEOF'
<template>
  <span class="av" :style="styleVars" />
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  size: { type: Number, default: 46 },
  hue:  { type: Number, default: 0 }
})

const styleVars = computed(() => ({
  width:  props.size + 'px',
  height: props.size + 'px',
  '--hue': props.hue
}))
</script>

<style scoped>
.av {
  display: block;
  flex: none;
  border-radius: 50%;
  background: conic-gradient(from calc(var(--hue) * 1deg),
    #ff9f0a, #ff2d55, #bf5af2, #0a84ff, #ff9f0a);
  box-shadow: 0 0 0 1px rgba(255, 255, 255, .4), 0 6px 16px rgba(0, 0, 0, .4);
}
</style>
VEOF

# ------------------------------------------------ ChatRow.vue
cat > "$ROOT/src/components/ChatRow.vue" <<'VEOF'
<template>
  <div class="row">
    <Avatar :size="46" :hue="hue" />
    <div class="row__main">
      <div class="row__top">
        <span class="row__name">{{ name }}</span>
        <time class="row__time">{{ time }}</time>
      </div>
      <p class="row__preview">{{ preview }}</p>
    </div>
    <span v-if="unread" class="row__badge">{{ unread }} 条未读</span>
  </div>
</template>

<script setup>
import Avatar from './Avatar.vue'

defineProps({
  name:    { type: String, default: '' },
  preview: { type: String, default: '' },
  time:    { type: String, default: '' },
  unread:  { type: Number, default: 0 },
  hue:     { type: Number, default: 0 }
})
</script>

<style scoped>
.row { display: flex; align-items: center; gap: 12px; min-width: 0 }
.row__main { flex: 1; min-width: 0 }
.row__top { display: flex; align-items: baseline; gap: 8px }

.row__name {
  font-size: 16px;
  font-weight: 600;
  letter-spacing: .2px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.row__time {
  margin-left: auto;
  flex: none;
  font-size: 12px;
  color: var(--text-2);
}

.row__preview {
  margin: 3px 0 0;
  font-size: 13.5px;
  color: var(--text-3);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.row__badge {
  flex: none;
  padding: 3px 9px;
  border-radius: 999px;
  font-size: 11.5px;
  font-weight: 600;
  background: linear-gradient(135deg, #3b6bff, #8a3bff);
  box-shadow: 0 0 12px rgba(92, 92, 255, .75), inset 0 1px 0 rgba(255, 255, 255, .5);
}
</style>
VEOF

# ------------------------------------------------ FolderCard.vue
cat > "$ROOT/src/components/FolderCard.vue" <<'VEOF'
<template>
  <LiquidGlass class="folder">
    <header class="folder__head">
      <span class="folder__title">{{ title }}</span>

      <svg class="folder__tail" viewBox="0 0 100 22" preserveAspectRatio="none" aria-hidden="true">
        <path d="M0 1C18 1 26 21 100 21"
              fill="none"
              stroke="rgba(255,255,255,.32)"
              stroke-width="1.2"
              vector-effect="non-scaling-stroke" />
      </svg>

      <div class="folder__stack">
        <Avatar v-for="(h, i) in avatars" :key="i" :size="28" :hue="h" />
        <i v-if="more" class="folder__more">+{{ more }}</i>
      </div>
    </header>

    <div class="folder__body"><slot /></div>
  </LiquidGlass>
</template>

<script setup>
import LiquidGlass from './LiquidGlass.vue'
import Avatar from './Avatar.vue'

defineProps({
  title:   { type: String, default: '' },
  more:    { type: Number, default: 0 },
  avatars: { type: Array,  default: () => [] }
})
</script>

<style scoped>
.folder { padding: 10px 16px 16px }

.folder__head {
  display: flex;
  align-items: flex-end;
  gap: 0;
  margin: 0 -16px 8px;
  padding: 0 16px;
}

.folder__title {
  flex: none;
  padding: 8px 26px;
  border-radius: 999px;
  font-size: 15px;
  font-weight: 500;
  letter-spacing: .5px;
  background: rgba(255, 255, 255, .10);
  border: 1px solid rgba(255, 255, 255, .30);
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, .55);
}

.folder__tail { flex: 1; height: 26px; min-width: 20px }

.folder__stack {
  flex: none;
  display: flex;
  align-items: center;
  padding-bottom: 2px;
}

.folder__stack > * {
  margin-left: -9px;
  box-shadow: 0 0 0 2px rgba(255, 255, 255, .25);
}

.folder__more {
  display: grid;
  place-items: center;
  width: 28px;
  height: 28px;
  border-radius: 50%;
  font-size: 11px;
  font-weight: 600;
  font-style: normal;
  background: rgba(255, 255, 255, .14);
  -webkit-backdrop-filter: blur(6px);
          backdrop-filter: blur(6px);
}

.folder__body { padding-top: 6px }
</style>
VEOF

# ------------------------------------------------ App.vue（注：用户粘贴版聊天数据为微信风格占位）
cat > "$ROOT/src/App.vue" <<'VEOF'
<template>
  <LiquidWallpaper />

  <main class="app">
    <LiquidGlass class="msg-card">
      <ChatRow
        name="Umi（注明在哪添加）"
        preview="[图片]"
        time="10月17日 19:02"
        :unread="4"
        :hue="20"
      />
    </LiquidGlass>

    <FolderCard title="群聊" :more="8" :avatars="[0, 60, 120]">
      <ChatRow
        name="Lui 47 条免打扰通知"
        preview="[47条] 爱疯：[链接] 退群人员：星（群昵称未…"
        time="10月17日 19:16"
        :unread="4"
        :hue="200"
      />
    </FolderCard>

    <FolderCard title="企业好友" :more="2" :avatars="[40, 100, 160]">
      <ChatRow
        name="怀思·同程旅行小助手"
        preview="[小程序] 浏阳精选酒店"
        time="10月14日 08:41"
        :hue="120"
      />
    </FolderCard>

    <FolderCard title="未读" :more="1" :avatars="[80, 140]">
      <ChatRow
        name="Lui 47 条免打扰通知"
        preview="[47条] 爱疯：[链接] 退群人员：星（群昵称未设…"
        time="10月17日 19:16"
        :unread="4"
        :hue="260"
      />
    </FolderCard>

    <FolderCard title="分组">
      <ChatRow
        name="德发想分组「禁广」"
        preview="[4条] 东京学妹：[动画表情] 骄傲"
        time="10月17日 17:16"
        :hue="320"
      />
    </FolderCard>
  </main>
</template>

<script setup>
import LiquidWallpaper from './components/LiquidWallpaper.vue'
import LiquidGlass from './components/LiquidGlass.vue'
import ChatRow from './components/ChatRow.vue'
import FolderCard from './components/FolderCard.vue'
</script>

<style scoped>
.msg-card { padding: 16px 18px }
</style>
VEOF

# ------------------------------------------------ AGENTS.md（用户粘贴版在此截断）
cat > "$ROOT/AGENTS.md" <<'VEOF'
# AGENTS.md · Liquid Glass 主题

> 给 AI Agent 的项目说明书。**动手前请完整读完**，并按 §7 的规范改代码。

## 1. 这是什么

iOS 26 **Liquid Glass（液态玻璃）** 风格的聊天列表 UI。
纯展示层：无路由、无网络请求、无状态管理。目标是**像素级还原玻璃质感**。

## 2. 技术栈

- Vue 3 (`<script setup>`) + Vite 6
- **纯 CSS**。禁止引入 UI 库 / Tailwind / CSS-in-JS / preprocessor
- Node ≥ 18，无 TypeScript

## 3. 命令

```bash
npm install
npm run dev      # http://localhost:5173
npm run build    # 每次改完必须能通过
VEOF

echo "✓ 脚手架生成完成: $ROOT"
echo "  npm install && npm run dev"
