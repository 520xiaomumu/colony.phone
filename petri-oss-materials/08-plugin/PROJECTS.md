# 插件（08-plugin）

> 魂：**最轻壳（篡改猴系）；反锚 Electron**

## Colony 现有挂钩

- `plugin.* 读写重载`
- `Chrome 中继 Relay`
- `fs 工作区`
- `manifest 死穴防护`

## 开源项目清单（本目录已抓取 12 个独特仓库）

| # | 仓库 | Stars | 桥接级 | 可吸收到本 Petri 的功能 | 本地快照 |
|---|---|---|---|---|---|
| 1 | [GoogleChrome/chrome-extensions-samples](https://github.com/GoogleChrome/chrome-extensions-samples) | 17708 | A | scripting/MV3 样例 | `snippets/GoogleChrome__chrome-extensions-samples__README.md` |
| 2 | [PlasmoHQ/plasmo](https://github.com/PlasmoHQ/plasmo) | 13139 | A | 扩展框架结构 | `snippets/PlasmoHQ__plasmo__package.json` |
| 3 | [crxjs/chrome-extension-tools](https://github.com/crxjs/chrome-extension-tools) | 4152 | A | CRX 构建 | `snippets/crxjs__chrome-extension-tools__README.md` |
| 4 | [fregante/webext-storage](https://github.com/fregante/webext-storage) | 78 | A | 扩展存储 | `snippets/fregante__webext-storage__readme.md` |
| 5 | [greasemonkey/greasemonkey](https://github.com/greasemonkey/greasemonkey) | 2580 | A | userscript 元数据惯例 | `snippets/greasemonkey__greasemonkey__README.md` |
| 6 | [lobehub/lobe-chat-plugins](https://github.com/lobehub/lobe-chat-plugins) | 298 | A | 多供应商配置 UI + 插件协议 | `snippets/lobehub__lobe-chat-plugins__README.md` |
| 7 | [mozilla/web-ext](https://github.com/mozilla/web-ext) | 3126 | A | Firefox 扩展工具 | `snippets/mozilla__web-ext__README.md` |
| 8 | [mozilla/webextension-polyfill](https://github.com/mozilla/webextension-polyfill) | 3073 | A | 浏览器 API 统一 | `snippets/mozilla__webextension-polyfill__README.md` |
| 9 | [quoid/userscripts](https://github.com/quoid/userscripts) | 4702 | A | Safari 注入模型 | `snippets/quoid__userscripts__README.md` |
| 10 | [scriptscat/scriptcat](https://github.com/scriptscat/scriptcat) | 5021 | A | 中文区脚本管理器能力面 | `snippets/scriptscat__scriptcat__README.md` |
| 11 | [violentmonkey/violentmonkey](https://github.com/violentmonkey/violentmonkey) | 8740 | A | @match/@grant 注入运行时——插件北星 | `snippets/violentmonkey__violentmonkey__README.md` |
| 12 | [wxt-dev/wxt](https://github.com/wxt-dev/wxt) | 10346 | A | 扩展打包/热重载 DX | `snippets/wxt-dev__wxt__README.md` |

## 建议优先并入的能力切片（仍不落码，仅规划）

1. violentmonkey 注入运行时
1. userscript 元数据兼容
1. scriptcat 能力面
1. wxt/MV3 打包仅用于 Colony Bridge 扩展
1. 明确禁止 Electron 厚壳

## 许可证提示

本目录快照仅供 Colony 研发对照；**上游许可证仍适用**。并入 Petri 前须逐项核对 SPDX，优先 MIT/Apache-2.0，避免传染性协议进入单文件发行物。
