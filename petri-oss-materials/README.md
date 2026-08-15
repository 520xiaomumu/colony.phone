# Colony · Petri 开源素材库（petri-oss-materials）

> **纪律**：本目录可任意增删改；**禁止**改动仓库内 `colony.html`、宪法/现状 md、`tests/` 等其它文件。  
> **用途**：为 8 个 Petri 对照基因表「魂」，搜集具备**源码价值**的开源项目，摘录核心 README/源码片段作后续迭代备用。  
> **上游许可证仍适用**；快照仅供研发对照，并入前须 SPDX 审查。

## 目录结构

| 子目录 | Petri | 魂（宪法） |
|---|---|---|
| [01-agent](./01-agent/) | 全能 agent | pi 极简 + DeepSeek×Hermes |
| [02-ai-config](./02-ai-config/) | AI 配置 | OpenRouter 一钥万模 |
| [03-bridge](./03-bridge/) | agent 桥接 | A2A + IM（多 agent 群聊） |
| [04-porter](./04-porter/) | 次元口袋 | 泛化 Obsidian |
| [05-ui-shell](./05-ui-shell/) | 界面设计 | Figma |
| [06-code](./06-code/) | 代码解读 | 泛化 AI IDE |
| [07-workflow](./07-workflow/) | 工作流 | n8n / ComfyUI |
| [08-plugin](./08-plugin/) | 插件 | 篡改猴轻壳；反 Electron |

每个子目录含：
- `PROJECTS.md` — ≥10 个仓库清单 + 桥接级(A/B/C) + 可吸收功能
- `snippets/` — 已下载的 README / 关键源码文件（带 MATERIAL 溯源头）

## 总报告

见 **[SUMMARY.md](./SUMMARY.md)**（汇总）与 **[VOLUME_AND_ABSORBABLE.md](./VOLUME_AND_ABSORBABLE.md)**（每块 ≥10 个 A 级可吸收项 + KB 体积估算 + Hermes 生态）。

Hermes 插件/技能生态专柜：`[00-hermes-ecosystem/](./00-hermes-ecosystem/)`。

## 刷新抓取

```bash
cd petri-oss-materials && python3 _fetch_snippets.py
```

仅网络拉取到本目录，不触碰其它路径。
