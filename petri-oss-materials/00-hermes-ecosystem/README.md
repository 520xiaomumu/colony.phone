# Hermes / DeepSeek 插件与技能生态素材

> 官方插件索引目前条目少，但 `topic:hermes-agent` 旁系生态很大。本目录专收 Hermes 相关，供 agent / bridge / plugin / code 共用。

## 已抓取

- `snippets/plugin_index.json` — Hermes 内置插件索引 seed（5 条官方登记）
- 多个官方/社区 README（example-plugins、self-evolution、Function-Calling、Bot-Mode、yantrikdb、skills-guard、mnemosyne、claude-mem、codegraph、colleague-skill、community-plugins 等）

## 对 Colony 的用法

| 生态能力 | 建议 Petri | A/B |
|---|---|---|
| Skills Hub + 检疫锁 | agent / porter | A |
| plugin.yaml + ctx.llm 范例 | plugin-manager | A |
| 记忆压缩/召回 | agent | A |
| 代码知识图 | code | A/B |
| Telegram Business / 外脑 | bridge | B |
| Self-evolution 优化器 | — | B（产物回灌 skill） |

详见上级目录 `VOLUME_AND_ABSORBABLE.md` §1。
