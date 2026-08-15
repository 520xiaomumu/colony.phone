# 体积与可吸收规划（不改运行时代码）

> 回应三点：① 每块至少 **10 个可吸收进 Petri（A 级）** 的项目清单（此前「建议优先」只有 5 条是取舍列表，不是可吸收上限——这里补齐并严格化）；② 估算**有必要写入的功能代码 KB** 与写入后 Petri **增量体积**；③ DeepSeek×Hermes **插件/技能生态**收刮。

---

## 0. 口径说明（避免再误解）

| 口径 | 含义 |
|---|---|
| **A · 可吸收进 Petri** | 算法/协议/UI 交互可在单文件 HTML 内用 JS **重写或薄嵌**（不依赖 Node/Python 运行时） |
| **B · 外挂** | 保留为 CLI/服务，经 bridge / net.fetch / 插件中继调用 |
| **「有必要的功能代码」** | 不是把上游仓库全拷进 Petri，而是达到「魂能力」所需的**最小蒸馏体积**（手写+可选 minify 依赖） |
| **体积单位** | KB = 源码字符量量级（UTF-8）；单文件 Petri 按**增量**估 |

**诚实前提**：上游动辄数万星的仓，能进 Petri 的通常是 **2%–10% 的核心形状**；其余是壳、构建链、多语言绑定。

---

## 1. Hermes / DeepSeek 插件生态收刮

### 1.1 官方索引（已下载）
- 快照：`00-hermes-ecosystem/snippets/plugin_index.json`（Hermes 自带 seed index，2026-08-12）
- 官方插件条目（索引内目前 5 条，生态仍早期，但**旁系仓库很多**）：

| 插件 | 仓库 | 能力标签 |
|---|---|---|
| hermes-media-studio | NousResearch/hermes-media-studio | tools, dashboard |
| hermes-telegram-business | NousResearch/hermes-telegram-business | platform |
| plugin-llm-example | NousResearch/hermes-example-plugins | commands, llm |
| plugin-llm-async-example | NousResearch/hermes-example-plugins | commands, llm |
| hermes-plugin-chrome-profiles | anpicasso/hermes-plugin-chrome-profiles | tools / CDP |

### 1.2 官方与一线周边（已拉 README 到 `00-hermes-ecosystem/snippets/`）

| 仓库 | ★约 | 与 Colony 关系 |
|---|---:|---|
| NousResearch/hermes-agent | 231k | 本体；skill/plugin 机制 |
| NousResearch/hermes-agent-self-evolution | 5.0k | skill/prompt 进化管线 → **B**（产物回灌 kv:skill） |
| NousResearch/Hermes-Function-Calling | 1.4k | 函数调用数据/格式 → **A**（工具 JSON 形状） |
| NousResearch/Hermes-Bot-Mode | 0.5k | Bot 模式 UX → **A**（群聊成员行为） |
| NousResearch/hermes-paperclip-adapter | 1.8k | 适配器 → **B** |
| NousResearch/hermes-example-plugins | 33 | 插件 API 范例 → **A**（对照 Colony plugin 契约） |
| NousResearch/hermes-telegram-business | 23 | TG Business 秘书 → **B**/bridge |
| yantrikos/yantrikdb-hermes-plugin | 79 | 记忆插件 → **A/B**（记忆召回算法可蒸馏） |
| aibuild-lab/skills-guard | 9 | skill 威胁扫描 → **A**（收养检疫增强） |
| mnemosyne-oss/mnemosyne | 2.5k | 零云 AI 记忆 → **A**（SQLite/记忆形状；浏览器可用 IDB 仿） |
| 42-evey/hermes-plugins | 402 | 社区插件集 → 扫清单 |
| kaishi00/hermes-community-plugins | 47 | 社区插件 |
| Humalike/hermes-humalike-plugin | 198 | 人格/拟人插件 → **A**（MAP/角色） |
| zaycruz/hermes-opencode-plugin | 50 | OpenCode 桥 → **B** |
| thedotmack/claude-mem | 90k | 跨会话记忆压缩注入（标榜支持 Hermes）→ **A**（记忆压缩环） |
| colbymchenry/codegraph | 66k | 本地代码知识图（支持 Hermes）→ **A/B**（对照 ana:/repo map） |
| titanwings/colleague-skill | 22k | 同事式 skill → **A**（skill 形态） |

### 1.3 对 Colony 的落地含义（不写码，只规划）

| 能力 | 建议落点 | 预估写入 |
|---|---|---|
| Skill 自进化 + hub 检疫锁（hash/扫描） | petri:agent + porter 检疫 | 4–8 KB |
| Plugin manifest（plugin.yaml 形状）对照 | petri:plugin-manager | 3–6 KB |
| 记忆召回（mnemosyne/claude-mem 思想） | agent memory + porter | 6–12 KB |
| Hermes 当外脑 | bridge Endpoints / Brain | **0 KB Petri**（B 接线文档+少量适配 1–2 KB） |
| Function-calling 严格 JSON | agent 工具围栏 / ai adapters | 2–4 KB |

---

## 2. 每 Petri：≥10 个 **A 级可吸收**项目 + 体积估算

> 下列「可吸收」= 严格 A（或 A 为主）。B-only 仓不计入「至少 10 个」。

### 2.1 全能 agent — 目标增量 **+18～35 KB**（激进 Hermes 味 +28～45 KB）

| # | 可吸收项目 | 吸收什么功能 | 必要代码(KB) |
|---|---|---|---:|
| 1 | badlogic/pi / pi-mono | 极简 tool loop、可组合扩展 | 3–5 |
| 2 | huggingface/smolagents | CodeAgent / ToolCalling 环（已有 agents.py 快照） | 4–8 |
| 3 | browser-use | 观察-行动-验证环 | 3–6 |
| 4 | browserbase/stagehand | 自愈选择器 / wait | 3–5 |
| 5 | langchain-ai/langgraph | checkpoint / 中断恢复语义 | 3–6 |
| 6 | openai/openai-agents-python | handoff、guardrail 形状 | 2–4 |
| 7 | pydantic/pydantic-ai | 工具参数 schema 校验 | 2–3 |
| 8 | NousResearch/Hermes-Function-Calling | 严格 tool JSON | 1–2 |
| 9 | thedotmack/claude-mem | 会话记忆压缩再注入 | 4–8 |
| 10 | mnemosyne-oss/mnemosyne | 本地记忆索引思想 | 3–5 |
| 11 | aibuild-lab/skills-guard | skill 内容威胁扫描 | 2–4 |
| 12 | titanwings/colleague-skill | skill 卡片/触发描述规范 | 1–2 |

**写入后能力**：skill 用后写回、记忆压缩、眼手自愈 wait、loop checkpoint、工具 JSON 硬化、skill 检疫。  
**Petri 体积**：当前 agent 独立件 ~170–180 KB 量级 → 预计 **190–220 KB**（+15%～25%）。

---

### 2.2 AI 配置 — 目标增量 **+12～25 KB**

| # | 可吸收项目 | 吸收什么 | KB |
|---|---|---|---:|
| 1 | OpenRouterTeam/ai-sdk-provider | OpenRouter 头/模型名约定 | 3–5 |
| 2 | BerriAI/litellm（路由思想） | fallback/别名表（手写，不嵌 Python） | 2–4 |
| 3 | openai/openai-node | chat/completions/SSE 形状 | 2–3 |
| 4 | anthropics/anthropic-sdk-typescript | Messages 适配字段 | 3–5 |
| 5 | googleapis/js-genai | Gemini 请求形状 | 2–4 |
| 6 | open-webui/open-webui（连接器 UX） | 供应商卡片/测通 UX | 2–3 |
| 7 | lobehub/lobe-chat | 多供应商配置 IA | 2–3 |
| 8 | Helicone/helicone | 请求 id/延迟台账字段 | 1–2 |
| 9 | Portkey-AI/gateway（策略思想） | 重试/超时/分流配置项 | 1–2 |
| 10 | ollama 协议文档实践 | local 探测与模型列表 | 1–2 |
| 11 | vllm OpenAI 兼容面 | local 超时/并发默认 | 1 |
| 12 | cloud-v2 已有方向 | embed/rerank/image.edit 钩子 | 4–8 |

**写入后能力**：原生 `openrouter` 协议；更稳的适配器；可选 embed/rerank。  
**体积**：ai ~90–100 KB → **105–125 KB**。

---

### 2.3 桥接 — 目标增量 **+15～30 KB**（不含 TG 原生实现）

| # | 可吸收项目 | 吸收什么 | KB |
|---|---|---|---:|
| 1 | a2aproject/A2A | agent card / task 形状 | 3–5 |
| 2 | AliceLJY/telegram-ai-bridge | generation 信封防环 | 3–6 |
| 3 | team-attention/agent-council | 反谄媚、参与调度 | 3–5 |
| 4 | yogirk/agent-council | 多 agent 议会变体 | 2–3 |
| 5 | modelcontextprotocol/typescript-sdk | MCP tool 清单镜像 | 3–5 |
| 6 | modelcontextprotocol/python-sdk | 对照 MCP 消息框 | 1–2（文档级） |
| 7 | diegofal/aibot-framework | A2A JSON-RPC 子集 | 3–5 |
| 8 | NousResearch/Hermes-Bot-Mode | 成员发言节奏 | 1–2 |
| 9 | NousResearch/hermes-telegram-business | 审批式秘书模式思想 | 1–2 |
| 10 | discord.js（协议思想） | 网关事件去抖 | 1–2 |
| 11 | matrix-js-sdk（思想） | 房间/时间线游标 | 2–3 |
| 12 | grammY（中间件形状） | update 管道（若做 TG B 网关可复用概念） | 1–2 |

**写入后能力**：防回声信封、反谄媚、MCP→capabilities、A2A card。TG 实发仍建议 **B**。  
**体积**：bridge ~80–100 KB → **100–130 KB**。

---

### 2.4 次元口袋 — 目标增量 **+20～40 KB**

| # | 可吸收项目 | 吸收什么 | KB |
|---|---|---|---:|
| 1 | micromark/micromark | 安全 Markdown→HTML ~14KB 级可嵌或重写子集 | 8–14 |
| 2 | markedjs/marked | 轻量 MD（备选） | 5–10 |
| 3 | remarkjs/remark（思想） | AST 插件链 | 2–4（手写子集） |
| 4 | logseq 块模型 | block-id / 引用 | 3–5 |
| 5 | siyuan-note/siyuan | 块级笔记 | 2–4 |
| 6 | foambubble/foam | wikilink `[[ ]]` | 2–3 |
| 7 | silverbulletmd/silverbullet | 浏览器笔记 OS 导航 | 3–6 |
| 8 | jsgrrchg/NeverWrite | AI 改动审阅 | 3–5 |
| 9 | usememos/memos | 时间流笔记 | 2–3 |
| 10 | dendronhq/dendron | 分层命名空间 | 1–2 |
| 11 | gray-matter 类 frontmatter | YAML 头解析（可手写 1KB） | 1–2 |
| 12 | fuse.js / lunr | 全文模糊搜（可嵌 fuse ~6–12KB minify） | 6–12 |

**写入后能力**：双链跳转、MD 渲染、frontmatter、模糊搜、审阅流。  
**体积**：porter 含口袋 HTML 较大；逻辑增量 **+20～40 KB**，若嵌 micromark+fuse 上限约 **+45 KB**。

---

### 2.5 界面设计 — 目标增量 **+15～35 KB**（叠新 ui-shell）

| # | 可吸收项目 | 吸收什么 | KB |
|---|---|---|---:|
| 1 | tldraw/tldraw（选中模型） | selection / transform | 4–8 |
| 2 | excalidraw（交互） | 画布工具条 IA | 2–4 |
| 3 | GrapesJS | 样式面板字段集 | 3–6 |
| 4 | prevwong/craft.js | 可序列化编辑器状态 | 3–5 |
| 5 | clauderic/dnd-kit | 精准拖拽碰撞 | 3–5 |
| 6 | floating-ui/floating-ui | 属性浮层定位 | 2–4 |
| 7 | radix-ui/primitives | 无障碍对话框/菜单 | 2–4 |
| 8 | shadcn-ui/ui | token 化组件抄法 | 2–3 |
| 9 | penpot（思想） | 组件变体 / token 导出 JSON | 2–3 |
| 10 | webstudio-is/webstudio | 样式系统 IA | 1–2 |
| 11 | pmndrs/react-spring（克制） | 2–3 个入场动效 | 1–2 |
| 12 | 新 petri-ui-shell 自身 | ui.state / applySkin / 点选 | 已含（并回整机另计） |

**写入后能力**：真·点选属性面板、皮肤热更新、拖拽手感、浮层面板。  
**体积**：ui-shell ~70–100 KB → **90–130 KB**。

---

### 2.6 代码解读 — 目标增量 **+25～50 KB**

| # | 可吸收项目 | 吸收什么 | KB |
|---|---|---|---:|
| 1 | Aider-AI/aider `repomap.py` | repo map | 5–10（JS 重写） |
| 2 | Aider `base_coder.py` | diff 应用/提交消息 | 4–8 |
| 3 | continuedev/continue | 解释/教学对话流 | 3–5 |
| 4 | tree-sitter（wasm 可选） | 精准语法 range | 0（调 API）或 +30KB wasm |
| 5 | ast-grep/ast-grep | 结构化搜改思想 | 3–5（手写子集） |
| 6 | microsoft/monaco-editor | 编辑器（**可选嵌**，体积大） | **嵌则 +200KB+** / 或 iframe CDN **+0** |
| 7 | jesseduffield/lazygit | git 面板 IA | 3–5 |
| 8 | gitui-org/gitui | 对照 | 1–2 |
| 9 | isomorphic-git（浏览器 git） | 真·浏览器 git | 15–25（minify） |
| 10 | colbymchenry/codegraph | 代码图索引思想 | 3–6 |
| 11 | TabbyML/tabby（协议） | 补全 API 形状 | 2–3 |
| 12 | anomalyco/opencode | 终端 agent UX 对照 | 1–2 |

**写入后能力**：repo map、diff 应用、教学解释、git 面板；Monaco/isomorphic-git 为可选大件。  
**体积建议路径**：
- **瘦路径**（推荐）：不嵌 Monaco/git → **+25～40 KB**
- **胖路径**：Monaco+isomorphic-git → **+250～400 KB**（接近违「轻量」魂，需你拍板）

---

### 2.7 工作流 — 目标增量 **+20～40 KB**

| # | 可吸收项目 | 吸收什么 | KB |
|---|---|---|---:|
| 1 | n8n-io/n8n workflow 包 | 节点 JSON 契约 | 4–8 |
| 2 | Comfy-Org/ComfyUI `execution.py` | 队列/缓存中间态 | 5–10 |
| 3 | langflow-ai/langflow | LLM 节点拼装 UX | 3–5 |
| 4 | FlowiseAI/Flowise | 低代码 agent 流 | 2–4 |
| 5 | activepieces/activepieces | 触发器/动作市场结构 | 3–5 |
| 6 | node-red/node-red | 事件流连线 | 2–4 |
| 7 | windmill-labs/windmill | 脚本节点 | 2–3 |
| 8 | PrefectHQ/prefect | 重试/状态机 | 2–3 |
| 9 | huginn/huginn | agent 场景模板 | 2–3 |
| 10 | temporalio/sdk-typescript | 持久执行/重放语义 | 3–5 |
| 11 | xyflow/xyflow（React Flow） | 画布交互增强 | 可选嵌大；手写增强 3–6 |

**写入后能力**：逐步预览、节点契约、模板市场（检疫）、重试。  
**体积**：workflow 已是大块；逻辑增量 **+20～40 KB**。

---

### 2.8 插件 — 目标增量 **+15～30 KB**

| # | 可吸收项目 | 吸收什么 | KB |
|---|---|---|---:|
| 1 | violentmonkey inject.js | 注入管线 | 5–10 |
| 2 | greasemonkey | 元数据头惯例 | 1–2 |
| 3 | scriptscat/scriptcat | 脚本管理能力面 | 2–4 |
| 4 | quoid/userscripts | Safari 注入对照 | 1–2 |
| 5 | wxt-dev/wxt | MV3 扩展结构（Bridge 扩展侧） | 2–4（扩展仓，不进 HTML） |
| 6 | GoogleChrome samples scripting | `chrome.scripting` | 1–2 |
| 7 | mozilla/webextension-polyfill | API 统一 | 可选 3–5 |
| 8 | fregante/webext-storage | 存储原语 | 1–2 |
| 9 | crxjs/chrome-extension-tools | 构建对照 | 文档级 |
| 10 | lobehub/lobe-chat-plugins | 插件 manifest | 2–3 |
| 11 | NousResearch/hermes-example-plugins | host-owned LLM plugin API | 2–4 |
| 12 | anpicasso/hermes-plugin-chrome-profiles | CDP 配置切换思想 | 1–2 |

**写入后能力**：userscript `@match` 热加载进 miniapp；与中继分工。  
**体积**：plugin-manager 很小 → 从 ~8–15 KB 逻辑升到 **25～45 KB**。

---

## 3. 总表：若按「推荐瘦路径」全做一轮

| Petri | A 级可吸收仓（本表） | 建议写入 KB | 写入后增量 | 主要新能力 |
|---|---:|---:|---:|---|
| agent | 12 | 18–35 | +15%～25% | skill 自进化、记忆压缩、眼手自愈、checkpoint |
| ai | 12 | 12–25 | +15%～25% | OpenRouter 魂、更稳适配、可选 embed |
| bridge | 12 | 15–30 | +20%～30% | 防环信封、反谄媚、MCP/A2A |
| porter | 12 | 20–40 | +逻辑 20–40KB | 双链、MD、搜索、审阅 |
| ui-shell | 12 | 15–35 | +20%～35% | 属性面板、皮肤、拖拽 |
| code | 12 | 25–40（瘦） | +逻辑 25–40KB | repo map、diff、git 面板、教学 |
| workflow | 11 | 20–40 | +逻辑 20–40KB | 逐步预览、节点契约、模板 |
| plugin | 12 | 15–30 | 成倍（基数小） | userscript 运行时 |
| **合计（瘦）** | **≥95 A 项** | **~140–275 KB** | 整机约 **+0.15～0.3 MB** | — |
| code 若嵌 Monaco | — | +200～350 | 显著变胖 | 需单独拍板 |

---

## 4. 对你批评的直接回应

1. **「几乎都是 5 个以下」**  
   - 上一版每个 `PROJECTS.md` 底部「建议优先并入」只有 **5 条**，那是**优先级**，不是可吸收上限。  
   - 表格里多数块已有 **10–13 仓**；但混有 B 级，容易看起来「能进 Petri 的少」。  
   - **本文件第 2 节**改为：每块 **≥10 个严格 A 级**，并给出 KB。

2. **Hermes 插件生态**  
   - 官方 index 目前条目少（5），但 **topic:hermes-agent 周边 2700+ 仓**；已收刮官方示例插件、记忆/技能卫士、社区插件集、claude-mem、codegraph 等，放在 `00-hermes-ecosystem/`。

3. **下一步（仍可不改 colony）**  
   - 请你按块勾选：每块要上的 **Top 5 A 项**（或「按第 3 节瘦路径全做」）。  
   - 我可以继续只在本目录把 Top 项的**更多源码文件**拉进 `snippets/`，并把 KB 估测改成「按文件精确到 KB」的对照表。

---

## 5. 相关路径

- 本规划：`petri-oss-materials/VOLUME_AND_ABSORBABLE.md`（本文件）
- Hermes 生态：`petri-oss-materials/00-hermes-ecosystem/`
- 各块清单：`petri-oss-materials/0x-*/PROJECTS.md`
