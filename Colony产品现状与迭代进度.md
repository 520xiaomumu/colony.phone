# Colony · 产品现状与迭代进度

> 与《Colony哲学与迭代宪法.md》以 Stem hash 互锚（宪法第 23 条）。一切当下状态、版本基准、台账在此；恒久原则见宪法。

## 版本基准

| 项 | 值 |
|---|---|
| 代际 | gen 1 |
| Stem hash（当前基准） | `14121d04` |
| 块清单 | petri:agent v2 · petri:ai v1 · petri:bridge v1 · petri:code v1 · petri:plugin-manager v1 · petri:porter v1 · petri:ui-shell v2 · petri:workflow v1 |
| 门禁 | `node tests/gate.mjs`（全量不变式）；`node tests/gate.mjs --self-test`（门自检守卫，第 6 条） |

## 修宪记录（第 4/5 条）

### 修宪 #1（本轮）
**书面理由**：全量审计（见审计计划）发现 stem 层四处待修：
1. 血统记录失真（kmeta/页首注释缺 petri:plugin-manager、ui-shell 版本 v1≠manifest v2）——违支柱二"血统如实记录"；
2. `idbStore.list` N+1 事务，大库/旧机性能不达支柱三"旧机可跑"；
3. `RT.mount` 的 SDK 垫片注入依赖 miniapp 含 `<head>`，缺失则静默失效——脆弱契约，按第 3 条沉为 core 纯函数 `injectAfterHead` 并加兜底；
4. PANEL"查看可见源码"用废弃 `document.write`；`K.download` 撤销 URL 定时过短。

**门禁**：新增 `tests/gate.mjs`（I1 血统同步 / I2 基准哈希 / I3 无损往返 / I4 凭证卫生 / I5 蜕皮一致 / I6 注入健壮），构建/改码后全量重跑；自检守卫注入三个必败用例验证"失败必红"。

**版本基准更新**：stem 文本每次改动后同步重算并更新 kmeta `__STEM_HASH` 与两份 lineage.stemHash（逐刀见台账）。

## 迭代台账（第 14 条，一刀一行；快照 = 对应 git commit）

| # | 刀 | 范围 | 变化 | 门禁 |
|---|---|---|---|---|
| 0 | 建门禁 tests/gate.mjs + 本现状文档 | 工具/文档 | 门禁初跑如期红在 I1×6 + I6（记录待修事实） | 红（by design） |
