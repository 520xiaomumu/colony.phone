# 界面设计（05-ui-shell）

> 魂：**Figma：选中即改、设计 token、组件化**

## Colony 现有挂钩

- `ui/apps provide`
- `ui.state/applySkin(新)`
- `桌面/任务栏/窗口`
- `GENE tokens`
- `点选编辑`

## 开源项目清单（本目录已抓取 12 个独特仓库）

| # | 仓库 | Stars | 桥接级 | 可吸收到本 Petri 的功能 | 本地快照 |
|---|---|---|---|---|---|
| 1 | [GrapesJS/grapesjs](https://github.com/GrapesJS/grapesjs) | 26131 | A | 组件树+样式面板 | `snippets/GrapesJS__grapesjs__README.md` |
| 2 | [clauderic/dnd-kit](https://github.com/clauderic/dnd-kit) | 17543 | A | 桌面图标拖拽精细化 | `snippets/clauderic__dnd-kit__README.md` |
| 3 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw) | 129652 | A | 无限画布交互 | `snippets/excalidraw__excalidraw__README.md` |
| 4 | [facebook/react](https://github.com/facebook/react) | 247251 | A | 组件模型对照 | `snippets/facebook__react__README.md` |
| 5 | [floating-ui/floating-ui](https://github.com/floating-ui/floating-ui) | 32700 | A | 可复制 token 化组件(shadcn) | `snippets/floating-ui__floating-ui__README.md` |
| 6 | [penpot/penpot](https://github.com/penpot/penpot) | 58614 | A/C | 组件/约束/token——只取思想，不搬整站 | `snippets/penpot__penpot__README.md` |
| 7 | [pmndrs/react-spring](https://github.com/pmndrs/react-spring) | 29136 | A | 动效（克制使用） | `snippets/pmndrs__react-spring__README.md` |
| 8 | [prevwong/craft.js](https://github.com/prevwong/craft.js) | 8721 | A | 可序列化编辑器状态 | `snippets/prevwong__craft.js__README.md` |
| 9 | [radix-ui/primitives](https://github.com/radix-ui/primitives) | 19164 | A | 无样式可访问控件 | `snippets/radix-ui__primitives__README.md` |
| 10 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui) | 121380 | A | 可复制 token 化组件(shadcn) | `snippets/shadcn-ui__ui__README.md` |
| 11 | [tldraw/tldraw](https://github.com/tldraw/tldraw) | 49789 | A | 画布选中/变换模型 → 点选编辑 | `snippets/tldraw__tldraw__README.md` |
| 12 | [webstudio-is/webstudio](https://github.com/webstudio-is/webstudio) | 8840 | A | 可视化样式系统 | `snippets/webstudio-is__webstudio__README.md` |

## 建议优先并入的能力切片（仍不落码，仅规划）

1. tldraw/craft 选中-变换模型
1. penpot token/组件思想
1. grapesjs 样式面板
1. dnd-kit 桌面拖拽
1. floating-ui 属性面板

## 许可证提示

本目录快照仅供 Colony 研发对照；**上游许可证仍适用**。并入 Petri 前须逐项核对 SPDX，优先 MIT/Apache-2.0，避免传染性协议进入单文件发行物。
