# AI 配置（02-ai-config）

> 魂：**OpenRouter：一处配置、万模可用**

## Colony 现有挂钩

- `ctx.provide('llm')`
- `ai.chat/chatStream/imagine/…`
- `protocol adapters`
- `ai.configure/test`
- `PROVIDER_SEED`

## 开源项目清单（本目录已抓取 12 个独特仓库）

| # | 仓库 | Stars | 桥接级 | 可吸收到本 Petri 的功能 | 本地快照 |
|---|---|---|---|---|---|
| 1 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | 56412 | A/B | OpenRouter 魂的自托管镜像；路由/fallback | `snippets/BerriAI__litellm__README.md` |
| 2 | [Helicone/helicone](https://github.com/Helicone/helicone) | 6073 | A | 请求追踪字段 | `snippets/Helicone__helicone__README.md` |
| 3 | [OpenRouterTeam/ai-sdk-provider](https://github.com/OpenRouterTeam/ai-sdk-provider) | 674 | A | OpenRouter header/模型名约定 | `snippets/OpenRouterTeam__ai-sdk-provider__README.md` |
| 4 | [Portkey-AI/gateway](https://github.com/Portkey-AI/gateway) | 12736 | A/B | 可观测、限流、多供应商策略 | `snippets/Portkey-AI__gateway__README.md` |
| 5 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | 45222 | A | 极简 harness / tool loop / 可组合扩展——对齐四原语哲学 | `snippets/QuantumNous__new-api__README.md` |
| 6 | [anthropics/anthropic-sdk-typescript](https://github.com/anthropics/anthropic-sdk-typescript) | 2084 | A | 极简 harness / tool loop / 可组合扩展——对齐四原语哲学 | `snippets/anthropics__anthropic-sdk-typescript__README.md` |
| 7 | [lobehub/lobe-chat](https://github.com/lobehub/lobe-chat) | 81715 | A | 多供应商配置 UI + 插件协议 | `snippets/lobehub__lobe-chat__README.md` |
| 8 | [ollama/ollama](https://github.com/ollama/ollama) | 178589 | B | 本地一键；已有 local 协议 | `snippets/ollama__ollama__README.md` |
| 9 | [open-webui/open-webui](https://github.com/open-webui/open-webui) | 148847 | A | 模型连接器 UX / 多模态输入 | `snippets/open-webui__open-webui__README.md` |
| 10 | [openai/openai-node](https://github.com/openai/openai-node) | 11119 | A | chat/completions 形状事实源 | `snippets/openai__openai-node__README.md` |
| 11 | [songquanpeng/one-api](https://github.com/songquanpeng/one-api) | 36391 | A | 极简 harness / tool loop / 可组合扩展——对齐四原语哲学 | `snippets/songquanpeng__one-api__README.md` |
| 12 | [vllm-project/vllm](https://github.com/vllm-project/vllm) | 89118 | B | 本地高吞吐；protocol:local | `snippets/vllm-project__vllm__README.md` |

## 建议优先并入的能力切片（仍不落码，仅规划）

1. OpenRouter 原生 protocol 适配器
1. litellm 作为自托管镜像文档+兼容
1. one-api/new-api 仅作部署选项
1. openai/anthropic SDK 形状校正适配器
1. open-webui/lobe 配置 UX 参考

## 许可证提示

本目录快照仅供 Colony 研发对照；**上游许可证仍适用**。并入 Petri 前须逐项核对 SPDX，优先 MIT/Apache-2.0，避免传染性协议进入单文件发行物。
