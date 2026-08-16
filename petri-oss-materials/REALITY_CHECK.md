# 现实核对：已有能力 vs 真正净增（对照 colony 源码）

> 你说得对：**上一版「主要会新增的能力」里，有不少 Colony Petri 已经具备。**  
> 本文只在 `petri-oss-materials/` 内更新；**不改任何 Petri/colony 运行时**。  
> 对照基准：当前分支 `colony.html` 内嵌块 +（若相关）`origin/main` 新独立 Petri。

---

## 0. 结论先说

| 判断 | 说明 |
|---|---|
| **重复鼓吹** | skill 播种、记忆压缩、agent.loop、四原语、data/fs/net、工作流 DAG/Assets、plugin 读写重载、AI 多协议/测通——**本就有**，不应再算「开源新增」 |
| **真净增（值得吸收）** | OpenRouter 协议、防环信封、userscript 注入运行时、aider 式 repo map/diff、MD/模糊搜/双链、Stagehand 自愈 wait、handoff、skill 威胁扫描、Comfy 逐步预览 UI |
| **半新（整机没有、新独立 Petri 才有）** | `runtime.waitFor`、`run target:js`、`ui.state` / `ui.applySkin` / 点选——应优先**收养你已上传的 Petri**，不是再从开源抄一遍 |

修订后的「瘦路径」净增体积，大约只要原先宣称的 **40%～60%**（因为水分被挤掉了）。

---

## 1. 逐块：声称能力 → 源码真相 → 开源该抄哪份

图例：
- ✅ **已有** — Petri 已实现，开源最多当对照，不必写入  
- 🟡 **半新** — 整机没有，新独立 Petri 已有 → 优先并回，不重复造  
- ❌ **缺失** — 真净增；下列「可放进 Petri 的具体文件」才有写入价值  

### 1.1 petri:agent（整机 ~160KB）

| 我曾说的「新增」 | 真相 | 依据（已有） | 若仍要开源，具体抄什么 |
|---|---|---|---|
| skill 自进化 | ✅ 大部分已有 | `skill:petri:agent:*` 版本播种、MAP 进 kv、可 write skill | 仅缺「用后自动沉淀」→ 对照 Hermes skill 机制写 **2–4KB** 策略，不必搬仓 |
| 记忆压缩再注入 | ✅ 已有 | `condense` / 滚动摘要 / `archiveTurnMedia` / `settings:agent.memory` | **不要再加** claude-mem 整套 |
| agent.loop / verify | ✅ 已有 | `agent.loop` + `runMatchers` + `task:` rounds | LangGraph 只作概念对照 |
| 工具围栏硬化 | ✅ 已有 | ` ```tool ` + `TOOL_ALT` + `_fails` | Function-Calling 仓仅对照 |
| `runtime.waitFor` | 🟡 半新 | 整机 sdk **无** waitFor；`origin/main` 的 `petri-agent.html` **有** | **先收养新 agent**；Stagehand `waitForSelector.ts` 作增强对照 |
| `run target:js` | 🟡 半新 | 整机无；新 agent 有 | **先收养**；smolagents `agents.py` 仅对照 CodeAgent 结构（**80KB 整文件不必塞进 Petri**） |
| handoff | ❌ 缺失 | 只有群聊 `askMember`，无跨 agent 任务移交 | **可吸收**：`01-agent/snippets/openai__...__handoffs____init__.py` + `history.py` + `docs/handoffs.md` → 蒸馏成 Colony 原语约 **3–6KB** |
| skill 威胁扫描 | ❌ 缺失 | 无 | **可吸收**：`00-hermes-ecosystem/.../skills_guard.py`（37KB）→ 蒸馏规则子集 **2–5KB** |
| 选择器自愈 | ❌ 缺失 | 有 snapshot/click，无 observe→fallback | **可吸收**：Stagehand `observeService.ts` / `actHandlerUtils.ts` / `waitForSelector.ts` → 增强 runtime 约 **4–8KB** |

**agent 净增合计（诚实）**：在「已收养新 agent」前提下，额外开源蒸馏约 **9–19KB**；若整机还不收养，先 +waitFor/js（来自你的 Petri，不是开源）约 **8–15KB**。

---

### 1.2 petri:ai（整机 ~104KB）

| 声称 | 真相 | 说明 | 具体可放文件 |
|---|---|---|---|
| 多厂商/测通/打包 | ✅ 已有 | adapters + verified + configure/test + SEED | — |
| 并发闸/429 | ✅ 已有 | `withLlmSlot` | — |
| OpenRouter 一钥万模 | ❌ 缺失 | 源码中 **无** `openrouter` | **`02-ai-config/snippets/OpenRouterTeam__...__provider.ts`**（9.7KB）、`convert-to-openrouter-chat-messages.ts`（19KB）、`openrouter-chat-settings.ts`（7KB）→ 蒸馏成一个 protocol 适配器约 **4–8KB**（不必整份 TS 打进 HTML） |
| embed/rerank/image.edit | 🟡 半新 | 整机无；`petri-ai-cloud-v2` 有 | **先评估收养 cloud-v2**（注意它删了 Anthropic）；开源不是第一来源 |
| 跨厂模型别名路由 | ❌ 弱缺失 | 有活跃厂商，无 alias 表 | LiteLLM 思想手写 **1–2KB** 即可 |

**ai 净增合计**：OpenRouter 适配器 **4–8KB**；若并 cloud-v2 能力面另计（那是你的 Petri，不是开源）。

---

### 1.3 petri:bridge（整机 ~70KB）

| 声称 | 真相 | 说明 | 具体可放文件 |
|---|---|---|---|
| 群聊游标/@/互动 | ✅ 已有 | `Group.*` 齐全 | — |
| SSE/离线留言/端点大脑 | ✅ 已有 | BridgeClient + Endpoints + Brain | — |
| generation 防环信封 | ❌ 缺失 | 仅有 chatId/msgId | **`a2a/envelope.js`(4.6KB) + `loop-guard.js`(3.1KB) + `idempotency.js`(1.9KB)** → 蒸馏进 Group **4–8KB** |
| 反谄媚 | ❌ 缺失 | agent-council 仓结构弱，无现成可抄大文件 | 需另找实现或自研 **2–4KB**；**暂不要宣称已有可粘贴源码** |
| MCP / A2A card | ❌ 缺失 | — | A2A 有 `docs/specification.md`（规范，非可运行 JS）；MCP 客户端路径需另定位——**规范级 A，运行时 B/自研** |

**bridge 净增合计**：**4–8KB**（信封防环实锤）；MCP/A2A/反谄媚仍偏「规范+自研」，不是「把某某仓塞进去」。

---

### 1.4 petri:porter（整机 ~108KB）

| 声称 | 真相 | 说明 | 具体可放文件 |
|---|---|---|---|
| data/fs/net/地图/清理/导出 | ✅ 已有 | sdk 面已很全 | **不要再包装成新增** |
| 全文 `q` 搜索 | ✅ 部分已有 | `data.list {q}` | fuse 是增强不是从零 |
| 双链 / MD 渲染 / frontmatter | ❌ 缺失 | — | **fuse.min.mjs ~29KB 可嵌或换更小 basic**；marked 入口 5.5KB 作对照，实装可嵌 marked 构建或手写子集 **3–8KB**；wikilink **手写 1–2KB**（Foam 只给约定） |
| NeverWrite 审阅 | ❌ 缺失 | cleanup≠hunk 审阅 | 暂无高质量可嵌源码；自研 **3–5KB** |

**porter 净增合计**：双链+MD+模糊搜 **8–25KB**（取决于是否整嵌 fuse）。

---

### 1.5 petri:ui-shell（整机 ~68KB）

| 声称 | 真相 | 说明 | 具体可放文件 |
|---|---|---|---|
| 桌面/窗口/GENE 样式 | ✅ 已有 | — | — |
| ui.state / applySkin / 点选 | 🟡 半新 | **你的新 ui-shell 已有** | **优先收养**，不是 tldraw 整仓 |
| Figma 属性面板深化 | ❌ 仍缺 | 点选≠完整属性面板 | tldraw/grapes **只蒸馏选中模型 3–6KB**，禁止嵌整库 |

**ui 净增合计**：收养新壳后额外开源蒸馏 **3–6KB**；未收养则先把新 Petri 并回（体积以你的文件为准，非开源）。

---

### 1.6 petri:code（整机 ~144KB）

| 声称 | 真相 | 说明 | 具体可放文件 |
|---|---|---|---|
| 分层解析 / ana / 源码管理 / 问 agent | ✅ 已有 | — | — |
| aider 式 repo map | ❌ 缺失 | ana≠全仓 rank map | **`aider/repomap.py`（27KB）→ JS 重写约 5–10KB** |
| unified diff 应用 | ❌ 缺失 | 现 edit=find/replace | **`base_coder.py`（86KB）里 diff 应用段落 → 蒸馏 4–8KB**，不要整文件打进 Petri |
| git 面板 / Monaco | ❌ 缺失 | — | isomorphic-git / Monaco = **可选大件**；默认不建议为「魂」必选项 |

**code 净增合计（推荐）**：**9–18KB**（map+diff）；Monaco/git 另议。

---

### 1.7 petri:workflow（整机 ~236KB，已经很大）

| 声称 | 真相 | 说明 | 具体可放文件 |
|---|---|---|---|
| DAG/Eph/Assets/catalog/patchGraph | ✅ 已有 | 引擎已强 | **大部分 n8n/Comfy「能力」已具备形态** |
| 每节点媒体预览 UI | ❌/弱 | 有事件流，缺 Comfy 式预览 | **`execution.py`（61KB）对照队列/缓存思想 → UI+缓存策略 5–10KB** |
| 节点市场 | ❌ 缺失 | — | 检疫+列表自研为主；开源只给「市场元数据」形状 |

**workflow 净增合计**：**5–12KB**（预览/重试）；再往上容易重复造已有引擎。

---

### 1.8 petri:plugin-manager（整机 ~12KB）

| 声称 | 真相 | 说明 | 具体可放文件 |
|---|---|---|---|
| 读写/备份/重载扩展源码 | ✅ 已有 | 管理面 | — |
| userscript 运行时 | ❌ 缺失 | 当前=改 Chrome 扩展文件，不是页内脚本引擎 | **`violentmonkey/.../inject.js`（14.6KB）→ 蒸馏注入器 5–10KB** |
| @match / GM_* | ❌ 缺失 | — | 自研子集 **3–5KB** + Violentmonkey 元数据惯例 |

**plugin 净增合计**：**8–15KB**（这是少数「开源文件几乎直接对口」的块）。

---

## 2. 修订后的体积表（挤掉水分）

| Petri | 曾宣称增量 | **诚实净增（开源蒸馏）** | 备注 |
|---|---:|---:|---|
| agent | 18–35 KB | **9–19 KB**（+先收养 waitFor/js） | 记忆/loop/skill 不算新增 |
| ai | 12–25 KB | **4–8 KB**（OpenRouter） | cloud-v2 能力另算收养 |
| bridge | 15–30 KB | **4–8 KB**（信封防环） | MCP/A2A 暂不定体积 |
| porter | 20–40 KB | **8–25 KB** | 视是否嵌 fuse |
| ui-shell | 15–35 KB | **3–6 KB**（属性面板深化） | 主增量应来自收养你的新壳 |
| code | 25–40 KB | **9–18 KB** | 不含 Monaco |
| workflow | 20–40 KB | **5–12 KB** | 引擎勿重复 |
| plugin | 15–30 KB | **8–15 KB** | 注入运行时是真缺口 |
| **合计** | 140–275 | **约 50–110 KB** | 约砍半 |

---

## 3. 「哪些开源代码可以放到 Petri」——只列已下载、且对缺口有用的文件

| 缺口 | 本地快照路径 | 建议用法 |
|---|---|---|
| OpenRouter | `02-ai-config/snippets/OpenRouterTeam__ai-sdk-provider__src__provider.ts` 等 3 文件 | **改写成** `protocol:'openrouter'` 适配器，勿整贴 TS |
| 防环信封 | `03-bridge/snippets/AliceLJY__...__envelope.js` 等 | **改写**进 Group 消息管线 |
| handoff | `01-agent/snippets/openai__...__handoffs*` | **改写**为 run/call 级移交，非 Python 原样 |
| skill 扫描 | `00-hermes-ecosystem/.../skills_guard.py` | **改写**规则表为 JS |
| 眼手自愈 | `01-agent/snippets/browserbase__stagehand__...observeService/waitForSelector/actHandlerUtils` | **增强**现有 runtime.*，与新 agent 的 waitFor 合流 |
| 模糊搜 | `04-porter/snippets/krisk__fuse__dist__fuse.min.mjs`（29KB） | 可嵌或换更小构建 |
| MD | `04-porter/snippets/markedjs__marked__src__marked.ts` | 对照；嵌官方 minify 构建更合适 |
| repo map / diff | `06-code/snippets/Aider-AI__aider__aider__repomap.py` / `base_coder.py` | **算法移植**，禁止 86KB py 原样进 HTML |
| 执行预览思想 | `07-workflow/snippets/Comfy-Org__ComfyUI__execution.py` | 对照队列；UI 自研 |
| userscript 注入 | `08-plugin/snippets/violentmonkey__...__inject.js` | **最接近可直接借鉴**的实现 |

**反例（有快照但不应当「新增能力」塞进 Petri）**  
- `smolagents/agents.py`（80KB）：Colony 已有更贴合的四原语引擎  
- 整仓 Penpot/n8n/Hermes/Continue：形态冲突或已覆盖  

---

## 4. 正确的吸收顺序（承认你仓库里已有的更新）

1. **先收养** `petri-ui-shell` / `petri-agent`（以及谨慎评估 `petri-ai-cloud-v2`）——半新能力的正主是你自己的 Petri。  
2. **再开源净增**：OpenRouter → 信封防环 → userscript 注入 → aider map/diff → MD/双链 → Stagehand 增强。  
3. 每吸收一项，对照本表「✅ 已有」栏，**禁止**把已有功能再包装成开源功劳。

---

## 5. 致歉与方法论纠正

此前把「开源仓擅长的领域」和「Colony 尚未具备的缺口」混为一谈，导致体积与能力被高估。  
以后素材评估固定三问：

1. Colony **源码里有没有**？（本文 §1）  
2. 若无，**哪一个具体文件**覆盖缺口？（本文 §3）  
3. 写入是 **蒸馏 KB** 还是 **整库嵌套**？（单文件约束下默认蒸馏）
