# app-gallery · 设计案例画廊

线上地址：https://shuting52.github.io/app-gallery/

`index.html` 为构建产物（GitHub Pages 直接发布），由 `build_master_gallery.py` 生成。

## 源码目录

| 目录 | 内容 |
|---|---|
| `liquid-glass-apps/` | 液态 · App套装 12 套 |
| `liquid-tab-bars/` | 液态 · Tab栏 100 款 |
| `liquid-notify-cards/` | 液态 · 通知卡 100 款 |
| `liquid-tab-cards/` | 液态 · 页签卡片 8 组 |
| `liquid-ui-kits/` | 液态 · UI主题 10 套 |
| `components/` | 加载/按钮/开关/进度/通知 各 20 组 |
| `tab-bars/` | 底部 Tab 栏 22 款 |
| `app-designs/` | 功能模块/产品方向/电商细分 全套 |
| `fresh-ui/` | 启动页/顶部栏/底部栏/欢迎弹窗/更新弹窗/App界面 |
| `update-modals/` | 更新交互弹窗 |
| `liquid-glass-scaffold/` | Liquid Glass Vue3 脚手架脚本 |

## 构建

```bash
python3 build_master_gallery.py   # 输出到 your_files/全部案例-画廊总库.html
```

构建时会自动截图（`~/workspace/preview-shots/`，本地缓存，不进仓库）。
