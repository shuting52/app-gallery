# APP 全套设计方案 · 构建规范（38 套：10 功能模块 + 16 产品方向 + 12 电商细分）

目标：38 个类目，每个一整套 App 设计方案。单文件 HTML，纯手写 CSS/JS，无框架无 CDN，中文界面。
截图工具：`CH=/home/hatch/.cache/ms-playwright/chromium_headless_shell-1243/chrome-headless-shell-linux64/chrome-headless-shell`，
`$CH --no-sandbox --disable-gpu --window-size=430,900 --virtual-time-budget=5000 --screenshot=<png> "file://<html>"`。

## 通用要求（每套必须）
1. 单文件 = 一个完整 App 原型：手机框（max-width 430px 居中），底部 Tab 栏 4–5 个，点 Tab 切换页面（JS），**每套 ≥4 个真实页面**。
2. 每套有独立视觉风格（配色/字体系/组件样式），38 套之间不重样。
3. 页面内容贴合类目真实业务（中文文案、列表/卡片/表单/图表等，不许 lorem ipsum）。
4. 禁用 `alert()`；无外部资源；JS 经 `node --check` 或浏览器无报错。
5. 每套写完 headless 截图自验（默认 Tab + 至少 1 个内页），白屏/报错修好再交。
6. 完工后在所属目录写 `_titles_<tag>.json`（tag 见下表）：`[{"file":"m01-auth.html","title":"账户与身份"}, …]`。

## 一、功能模块 10 套 → `~/workspace/app-designs/modules/`
| tag | 文件 | 类目 | 必含页面 |
|---|---|---|---|
| mod-a | m01-auth.html | 账户与身份 | 注册、登录、个人资料、权限管理 |
| mod-a | m02-core.html | 核心功能 | 3 个关键流程（如扫码快传/智能搜索/一键操作） |
| mod-a | m03-content.html | 内容与信息 | 内容浏览、搜索、分类、详情页 |
| mod-b | m04-social.html | 互动与沟通 | 评论、消息、分享、社区 |
| mod-b | m05-trade.html | 交易与服务 | 商品/服务展示、下单、支付、订单管理 |
| mod-b | m06-notify.html | 通知与提醒 | 推送通知、站内信、提醒设置 |
| mod-c | m07-profile.html | 个人中心 | 收藏、历史记录、偏好设置 |
| mod-c | m08-help.html | 帮助与反馈 | 常见问题、客服、意见反馈 |
| mod-c | m09-security.html | 系统与安全 | 隐私设置、数据权限、账号安全、错误处理 |
| mod-d | m10-ops.html | 运营与管理 | 活动、会员、优惠、数据分析 + 配套后台管理系统（后台概览页） |

## 二、产品方向 16 套 → `~/workspace/app-designs/verticals/`
每套选一个代表性产品做完整 App（≥4 页）：
| tag | 文件 | 类目→代表产品 |
|---|---|---|
| ver-a | v01-tools.html | 工具类→去水印工具（首页/解析/历史/我的） |
| ver-a | v02-edu.html | 学习教育类→背单词（学习/词库/统计/我的） |
| ver-a | v03-teach.html | 教师教学类→课堂点名与作业（点名/作业/家校/我的） |
| ver-a | v04-health.html | 健康管理类→生理期记录（记录/日历/统计/我的） |
| ver-b | v05-medical.html | 医疗服务类→预约挂号（挂号/问诊/报告/我的） |
| ver-b | v06-life.html | 生活服务类→家政预约（下单/师傅/订单/我的） |
| ver-b | v07-shop.html | 电商购物类→综合商城（首页/分类/购物车/我的） |
| ver-b | v08-fun.html | 内容娱乐类→短视频（推荐/发现/消息/我的） |
| ver-c | v09-community.html | 社交社区类→兴趣社区（动态/圈子/消息/我的） |
| ver-c | v10-travel.html | 出行交通类→打车（叫车/行程/钱包/我的） |
| ver-c | v11-finance.html | 财务管理类→记账（记账/图表/预算/我的） |
| ver-c | v12-work.html | 工作效率类→待办日程（待办/日历/项目/我的） |
| ver-d | v13-design.html | 创作设计类→海报制作（模板/编辑/作品/我的） |
| ver-d | v14-trip.html | 旅游本地类→行程规划（行程/酒店/景点/我的） |
| ver-d | v15-family.html | 儿童与家庭类→育儿记录（记录/成长/提醒/我的） |
| ver-d | v16-biz.html | 企业服务类→数据看板（看板/客户/考勤/我的） |

## 三、电商细分 12 套 → `~/workspace/app-designs/ecommerce/`
每套一个电商形态的完整购物 App（≥4 页：首页/分类或直播/购物车/我的）：
| tag | 文件 | 形态 |
|---|---|---|
| eco-a | e01-general.html | 综合电商 |
| eco-a | e02-brand.html | 品牌自营商城 |
| eco-a | e03-vertical.html | 垂直品类电商（美妆） |
| eco-a | e04-social.html | 社交电商 |
| eco-a | e05-live.html | 直播电商 |
| eco-a | e06-group.html | 团购与拼团 |
| eco-b | e07-secondhand.html | 二手与闲置交易 |
| eco-b | e08-crossborder.html | 跨境电商 |
| eco-b | e09-b2b.html | B2B 批发采购 |
| eco-b | e10-local.html | 本地零售与即时配送 |
| eco-b | e11-digital.html | 数字商品电商 |
| eco-b | e12-subscribe.html | 订阅制电商 |

## 回报
列出文件绝对路径 + `_titles_<tag>.json` 路径，说明自验方式。
