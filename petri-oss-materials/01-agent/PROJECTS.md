# 全能 agent（01-agent）

> 魂：**pi 极简通用为主 + DeepSeek×Hermes 自进化**

## Colony 现有挂钩

- `四原语 read/write/edit/run`
- `agent.loop`
- `runtime.* 眼手`
- `skill:petri:agent:*`
- `LLMLite 兜底`

## 开源项目清单（本目录已抓取 13 个独特仓库）

| # | 仓库 | Stars | 桥接级 | 可吸收到本 Petri 的功能 | 本地快照 |
|---|---|---|---|---|---|
| 1 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | 230990 | A/B | skill 自进化环、跨会话 state、gateway；DeepSeek 外脑经 bridge 挂载 | `snippets/NousResearch__hermes-agent__AGENTS.md` |
| 2 | [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands) | 84126 | B | 软件工程工具面；经 endpoint/runtime 外挂 | `snippets/OpenHands__OpenHands__README.md` |
| 3 | [OpenHands/software-agent-sdk](https://github.com/OpenHands/software-agent-sdk) | 988 | B | 软件工程工具面；经 endpoint/runtime 外挂 | `snippets/OpenHands__software-agent-sdk__README.md` |
| 4 | [badlogic/pi](https://github.com/badlogic/pi) | 95 | A | 极简 harness / tool loop / 可组合扩展——对齐四原语哲学 | `snippets/badlogic__pi__README.md` |
| 5 | [browser-use/browser-use](https://github.com/browser-use/browser-use) | 109321 | A | 浏览器观察-行动环 → runtime.snapshot/click | `snippets/browser-use__browser-use__README.md` |
| 6 | [browserbase/stagehand](https://github.com/browserbase/stagehand) | 23948 | A | 自愈选择器 → runtime 眼手鲁棒性 | `snippets/browserbase__stagehand__README.md` |
| 7 | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | 57108 | A | 角色/任务板隐喻 → 群聊成员职责 | `snippets/crewAIInc__crewAI__README.md` |
| 8 | [huggingface/smolagents](https://github.com/huggingface/smolagents) | 28815 | A | 最小 CodeAgent/ToolCallingAgent 循环可蒸馏 | `snippets/huggingface__smolagents__README.md` |
| 9 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | 39741 | A | 状态图、checkpoint、中断恢复 → agent.loop/verify | `snippets/langchain-ai__langgraph__README.md` |
| 10 | [microsoft/agent-framework](https://github.com/microsoft/agent-framework) | 12824 | A/B | MS 多 agent 图与 A2A 适配思路 | `snippets/microsoft__agent-framework__README.md` |
| 11 | [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | 28655 | A | handoff/guardrail 模式 | `snippets/openai__openai-agents-python__README.md` |
| 12 | [pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai) | 19315 | A | 工具 schema/校验 → callCap 参数纪律 | `snippets/pydantic__pydantic-ai__README.md` |
| 13 | [steipete/pi-mono](https://github.com/steipete/pi-mono) | 12 | A | 极简 harness / tool loop / 可组合扩展——对齐四原语哲学 | `snippets/steipete__pi-mono__README.md` |

## 建议优先并入的能力切片（仍不落码，仅规划）

1. Hermes skill 自进化 → kv:skill 写回闭环
1. pi 极简 tool loop 对齐四原语
1. smolagents CodeAgent 对照 run js
1. browser-use/stagehand → runtime 眼手自愈
1. langgraph checkpoint → loop/verify 恢复

## 许可证提示

本目录快照仅供 Colony 研发对照；**上游许可证仍适用**。并入 Petri 前须逐项核对 SPDX，优先 MIT/Apache-2.0，避免传染性协议进入单文件发行物。
