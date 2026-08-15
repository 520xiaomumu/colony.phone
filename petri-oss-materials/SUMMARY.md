# 总结报告：8 Petri × 开源素材（源码价值向）

**日期**：2026-08-15  
**范围**：仅新建目录 `petri-oss-materials/`（本报告所在处）。**未修改** `colony.html`、宪法、现状文档、tests 或任何 Petri 运行时代码。  
**目标**：每块至少 10 个真正具备源码价值的开源项目；摘录核心片段备用；标明哪些功能可按迭代哲学桥进对应 Petri。

---

## 1. 规模一览

| Petri | 独特仓库数 | 本地快照文件（约） | 代表北星 |
|---|---:|---:|---|
| 01 全能 agent | 13 | 16 | Hermes · pi · smolagents · browser-use · LangGraph |
| 02 AI 配置 | 12 | 12+ | LiteLLM · OpenRouter provider · one-api · ollama · vLLM |
| 03 agent 桥接 | 12 | 12 | A2A 规范 · MCP · telegram-ai-bridge · agent-council · grammY |
| 04 次元口袋 | 13 | 14 | Logseq · SilverBullet · Foam · Siyuan · NeverWrite |
| 05 界面设计 | 12 | 13 | Penpot · tldraw · GrapesJS · craft.js · dnd-kit |
| 06 代码解读 | 12 | 15 | Aider（含 repomap 源码）· Continue · Monaco · ast-grep · tree-sitter |
| 07 工作流 | 10 | 12 | n8n · ComfyUI（含 execution.py）· Langflow · Flowise · Activepieces |
| 08 插件 | 12 | 15 | Violentmonkey（含 inject.js）· ScriptCat · WXT · Greasemonkey · chrome samples |
| **合计** | **≥96 仓次** | **100+ 文件** | — |

每块明细与「可吸收功能」见各目录 `PROJECTS.md`；原始字节在 `snippets/`。

---

## 2. 桥接纪律（宪法对齐）

| 级 | 含义 | 例子 |
|---|---|---|
| **A** | 可蒸馏进 Petri（概念/算法/协议形状用 JS 重写） | Violentmonkey 注入模型；Aider repo map；smolagents 工具环；OpenRouter 协议头 |
| **B** | 进程外挂（CLI/服务经 bridge / net.fetch / 插件中继） | Hermes CLI 当外脑；vLLM/Ollama；Telegram 网关 |
| **C** | 反例或过重 | Electron IDE 壳、Penpot 整站、code-server 厚宿主——只学教训 |

**禁止**：把 Python/Rust 巨仓整段打进单文件；引入 Electron 厚壳；先开市场后补检疫。

---

## 3. 按 Petri：最值得下一轮「吸收」的功能（从素材反推）

### 3.1 全能 agent（pi + Hermes）
- **已有素材亮点**：`smolagents/agents.py` 最小循环；Hermes `AGENTS.md`；browser-use / Stagehand 眼手；LangGraph checkpoint。
- **可加进 Petri 的功能**：① skill 实战后写回（Hermes 自进化的 A 蒸馏）；② `run js` 与 CodeAgent 对齐；③ 选择器自愈（Stagehand）；④ loop 的 checkpoint/恢复（LangGraph）。
- **外挂 B**：Hermes+DeepSeek 经现有 bridge 端点大脑，不进 HTML。

### 3.2 AI 配置（OpenRouter）
- **缺口**：当前 Colony / cloud-v2 **仍无 OpenRouter 原生协议**；素材已备 LiteLLM、OpenRouter provider、one-api/new-api。
- **可加进 Petri**：`protocol:'openrouter'`（单 Key、厂商/模型名、Referer 头）；模型列表走 `/api/v1/models`；文档写明「自托管镜像 = LiteLLM」。
- **cloud-v2 的 embed/rerank/image.edit**：属能力宽度，与「一钥万模」正交——建议魂（OpenRouter）与形（多模态）分两刀。

### 3.3 桥接（A2A + IM）
- **可加进 Petri**：generation-counted 信封防环（telegram-ai-bridge）；反谄媚/参与调度（agent-council）；MCP → `capabilities` 镜像；A2A agent card。
- **B**：grammY/Discord/Matrix 仅作外发通道。

### 3.4 次元口袋（Obsidian）
- **可加进 Petri**：wikilink / block-id（Logseq/Siyuan/Foam）；浏览器端笔记壳（SilverBullet，与单文件气质最近）；AI 改动审阅（NeverWrite）。
- **不要**：嵌 Obsidian Electron。

### 3.5 界面（Figma）
- **可加进 Petri**（尤其可叠加你新上传的 ui-shell）：选中-变换（tldraw）；样式面板（GrapesJS）；可序列化编辑器状态（craft.js）；token（Penpot 思想 + 现有 GENE/applySkin）；拖拽（dnd-kit）。

### 3.6 代码解读（AI IDE）
- **已抓源码**：`aider/repomap.py`、`base_coder.py`——直接对照价值最高。
- **可加进 Petri**：repo map；unified diff 应用；tree-sitter/ast-grep 精准 edit；Monaco 嵌解读页；小白「解释」流（Continue）；git 面板信息架构（lazygit）。

### 3.7 工作流（n8n/Comfy）
- **已抓源码**：`ComfyUI/execution.py`。
- **可加进 Petri**：节点 JSON 契约（n8n）；执行队列与中间产物（Comfy）；LLM 节点拼装 UX（Langflow/Flowise）；触发器市场 + 检疫（Activepieces）。

### 3.8 插件（篡改猴）
- **已抓源码**：`violentmonkey/.../inject.js`。
- **可加进 Petri**：`@match`/`@grant` 子集；脚本热加载进 miniapp iframe；与现有 Chrome 中继分工（中继=特权，userscript=轻逻辑）。
- **明确 C**：任何 Electron 壳方案。

---

## 4. 与「新上传 Petri」的关系（只评不改）

| 新文件 | 素材如何帮它贴魂 |
|---|---|
| `petri-ui-shell.html`（ui.state/applySkin/点选） | 直接叠 tldraw/grapes/craft/dnd 素材做下一刀属性面板 |
| `petri-agent.html`（waitFor / run js） | 叠 smolagents/Hermes/Stagehand 素材做自进化与眼手 |
| `petri-ai-cloud-v2`（embed/rerank/edit） | 能力面已扩；**必须另补 OpenRouter 素材刀**才算魂对齐 |

---

## 5. 建议的「反复」顺序（仍可先只扩素材）

1. 你确认每块 PROJECTS 里 **Top 3 必吸**（或划掉不想碰的仓）。  
2. 我可以在本目录继续深挖：把 Top 3 的**更多具体源码文件**拉进 `snippets/`（仍不动 colony）。  
3. 你点头「动手」后，才按宪法第 12 条把 A 级蒸馏进 Petri；B 级只接线。

---

## 6. 如何审阅本素材库

```text
petri-oss-materials/
  README.md          ← 导航
  SUMMARY.md         ← 本报告
  0x-*/PROJECTS.md   ← 每块 ≥10 仓表
  0x-*/snippets/     ← 带溯源头的原文快照
  _fetch_snippets.py ← 可重复拉取
  _fetch_catalog.json
```

打开任意 `PROJECTS.md` 的「建议优先并入」列表，即可开始下一轮产品取舍对话。
