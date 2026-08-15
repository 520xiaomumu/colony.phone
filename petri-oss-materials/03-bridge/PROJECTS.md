# agent 桥接（03-bridge）

> 魂：**A2A + IM 通信（grok-bot 风多 agent 群聊）**

## Colony 现有挂钩

- `BridgeClient SSE`
- `Endpoints/插件中继`
- `Group 游标/@`
- `bridge.chat/members`
- `端点当大脑`

## 开源项目清单（本目录已抓取 12 个独特仓库）

| # | 仓库 | Stars | 桥接级 | 可吸收到本 Petri 的功能 | 本地快照 |
|---|---|---|---|---|---|
| 1 | [AliceLJY/telegram-ai-bridge](https://github.com/AliceLJY/telegram-ai-bridge) | 10 | A | generation-counted A2A 信封防环 | `snippets/AliceLJY__telegram-ai-bridge__README.md` |
| 2 | [a2aproject/A2A](https://github.com/a2aproject/A2A) | 25357 | A | 官方 agent 发现与任务接口 | `snippets/a2aproject__A2A__README.md` |
| 3 | [diegofal/aibot-framework](https://github.com/diegofal/aibot-framework) | 2 | A | A2A v0.3 agent card / JSON-RPC | `snippets/diegofal__aibot-framework__README.md` |
| 4 | [discordjs/discord.js](https://github.com/discordjs/discord.js) | 26785 | B | Discord 网关 | `snippets/discordjs__discord.js__README.md` |
| 5 | [grammyjs/grammY](https://github.com/grammyjs/grammY) | 3718 | B | TG 网关实现参考 | `snippets/grammyjs__grammY__README.md` |
| 6 | [matrix-org/matrix-js-sdk](https://github.com/matrix-org/matrix-js-sdk) | 2169 | B | 去中心 IM 通道 | `snippets/matrix-org__matrix-js-sdk__README.md` |
| 7 | [modelcontextprotocol/python-sdk](https://github.com/modelcontextprotocol/python-sdk) | 24013 | A | MCP tool discovery → capabilities | `snippets/modelcontextprotocol__python-sdk__README.md` |
| 8 | [modelcontextprotocol/typescript-sdk](https://github.com/modelcontextprotocol/typescript-sdk) | 13174 | A | MCP 浏览器侧可能路径 | `snippets/modelcontextprotocol__typescript-sdk__README.md` |
| 9 | [songsid/AgEnD](https://github.com/songsid/AgEnD) | 6 | B | 多 CLI 舰队；Colony 当指挥台 | `snippets/songsid__AgEnD__README.md` |
| 10 | [team-attention/agent-council](https://github.com/team-attention/agent-council) | 139 | A | 一 agent 一身份 / 反谄媚 / 参与调度 | `snippets/team-attention__agent-council__README.md` |
| 11 | [telegraf/telegraf](https://github.com/telegraf/telegraf) | 9174 | B | TG bot 中间件模式 | `snippets/telegraf__telegraf__README.md` |
| 12 | [yogirk/agent-council](https://github.com/yogirk/agent-council) | 88 | A | 一 agent 一身份 / 反谄媚 / 参与调度 | `snippets/yogirk__agent-council__README.md` |

## 建议优先并入的能力切片（仍不落码，仅规划）

1. A2A-TG generation 信封防环
1. agent-council 反谄媚/参与调度
1. MCP tools → capabilities 镜像
1. A2A agent card 对外发现
1. grammY/telegraf 仅作外发网关(B)

## 许可证提示

本目录快照仅供 Colony 研发对照；**上游许可证仍适用**。并入 Petri 前须逐项核对 SPDX，优先 MIT/Apache-2.0，避免传染性协议进入单文件发行物。
