# 工作流（07-workflow）

> 魂：**n8n / ComfyUI：可见可搭可学的流程脊椎**

## Colony 现有挂钩

- `Engine DAG`
- `Eph 即焚`
- `Assets`
- `workflow.* SDK`
- `画布编辑器`

## 开源项目清单（本目录已抓取 10 个独特仓库）

| # | 仓库 | Stars | 桥接级 | 可吸收到本 Petri 的功能 | 本地快照 |
|---|---|---|---|---|---|
| 1 | [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) | 127750 | A | 可复制 token 化组件(shadcn) | `snippets/Comfy-Org__ComfyUI__README.md` |
| 2 | [FlowiseAI/Flowise](https://github.com/FlowiseAI/Flowise) | 55366 | A | 低代码 agent 流 | `snippets/FlowiseAI__Flowise__README.md` |
| 3 | [PrefectHQ/prefect](https://github.com/PrefectHQ/prefect) | 23629 | A | 任务重试/状态 | `snippets/PrefectHQ__prefect__README.md` |
| 4 | [activepieces/activepieces](https://github.com/activepieces/activepieces) | 23803 | A | 极简 harness / tool loop / 可组合扩展——对齐四原语哲学 | `snippets/activepieces__activepieces__README.md` |
| 5 | [huginn/huginn](https://github.com/huginn/huginn) | 49795 | A | agent 自动化场景库 | `snippets/huginn__huginn__README.md` |
| 6 | [langflow-ai/langflow](https://github.com/langflow-ai/langflow) | 153267 | A | LLM 节点拼装 UX | `snippets/langflow-ai__langflow__README.md` |
| 7 | [n8n-io/n8n](https://github.com/n8n-io/n8n) | 200742 | A | 节点 JSON 契约、凭证、执行语义 | `snippets/n8n-io__n8n__README.md` |
| 8 | [node-red/node-red](https://github.com/node-red/node-red) | 23536 | A | 事件流连线模型 | `snippets/node-red__node-red__README.md` |
| 9 | [temporalio/sdk-typescript](https://github.com/temporalio/sdk-typescript) | 896 | A | 持久工作流/重放 | `snippets/temporalio__sdk-typescript__README.md` |
| 10 | [windmill-labs/windmill](https://github.com/windmill-labs/windmill) | 17550 | B | 脚本即工作流 | `snippets/windmill-labs__windmill__README.md` |

## 建议优先并入的能力切片（仍不落码，仅规划）

1. n8n 节点 JSON 契约
1. ComfyUI execution 队列/缓存
1. langflow/flowise LLM 节点 UX
1. activepieces 触发器市场(检疫)
1. temporal 重试/重放语义

## 许可证提示

本目录快照仅供 Colony 研发对照；**上游许可证仍适用**。并入 Petri 前须逐项核对 SPDX，优先 MIT/Apache-2.0，避免传染性协议进入单文件发行物。
