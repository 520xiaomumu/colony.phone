# 代码解读（06-code）

> 魂：**AI IDE：小白教学 + 精准编辑 + git**

## Colony 现有挂钩

- `分层解析 L0–L3`
- `ana: 地图`
- `源码管理器`
- `选中即问 agent`
- `ANALYZER_HTML`

## 开源项目清单（本目录已抓取 12 个独特仓库）

| # | 仓库 | Stars | 桥接级 | 可吸收到本 Petri 的功能 | 本地快照 |
|---|---|---|---|---|---|
| 1 | [Aider-AI/aider](https://github.com/Aider-AI/aider) | 48246 | A | repo map + unified diff + git 提交 | `snippets/Aider-AI__aider__README.md` |
| 2 | [TabbyML/tabby](https://github.com/TabbyML/tabby) | 33826 | B | 自托管补全服务 | `snippets/TabbyML__tabby__README.md` |
| 3 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | 197744 | A/B | 终端 agent 交互 | `snippets/anomalyco__opencode__README.md` |
| 4 | [ast-grep/ast-grep](https://github.com/ast-grep/ast-grep) | 15527 | A | 结构化搜索替换 → edit 原语增强 | `snippets/ast-grep__ast-grep__README.md` |
| 5 | [coder/code-server](https://github.com/coder/code-server) | 78839 | C/B | 厚 IDE 宿主——勿 Electron 化；可外链 | `snippets/coder__code-server__docs__README.md` |
| 6 | [continuedev/continue](https://github.com/continuedev/continue) | 35493 | A | 解释/补全/仓库感知提示词与 UX | `snippets/continuedev__continue__README.md` |
| 7 | [gitui-org/gitui](https://github.com/gitui-org/gitui) | 22395 | A | 可复制 token 化组件(shadcn) | `snippets/gitui-org__gitui__README.md` |
| 8 | [jesseduffield/lazygit](https://github.com/jesseduffield/lazygit) | 81356 | A | git 操作信息架构 | `snippets/jesseduffield__lazygit__README.md` |
| 9 | [microsoft/monaco-editor](https://github.com/microsoft/monaco-editor) | 46554 | A | 浏览器内编辑器 | `snippets/microsoft__monaco-editor__README.md` |
| 10 | [sourcegraph/cody-public-snapshot](https://github.com/sourcegraph/cody-public-snapshot) | 3806 | A | 代码问答/导航 | `snippets/sourcegraph__cody-public-snapshot__README.md` |
| 11 | [tree-sitter/tree-sitter](https://github.com/tree-sitter/tree-sitter) | 26655 | A | 语法树精准 range | `snippets/tree-sitter__tree-sitter__README.md` |
| 12 | [voideditor/void](https://github.com/voideditor/void) | 28843 | C/A | IDE 壳反例；可学侧栏布局 | `snippets/voideditor__void__README.md` |

## 建议优先并入的能力切片（仍不落码，仅规划）

1. aider repomap + diff 应用
1. continue 教学解释流
1. tree-sitter/ast-grep 精准编辑
1. monaco 嵌入解读页
1. lazygit 信息架构做 git 面板

## 许可证提示

本目录快照仅供 Colony 研发对照；**上游许可证仍适用**。并入 Petri 前须逐项核对 SPDX，优先 MIT/Apache-2.0，避免传染性协议进入单文件发行物。
