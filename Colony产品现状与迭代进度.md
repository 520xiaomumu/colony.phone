# Colony · 产品现状与迭代进度

> 与《Colony哲学与迭代宪法.md》以 Stem hash 互锚（宪法第 23 条）。一切当下状态、版本基准、台账在此；恒久原则见宪法。

## 版本基准

| 项 | 值 |
|---|---|
| 代际 | gen 1 |
| Stem hash（当前基准） | `295b382d`（初始 `14121d04`，修宪 #1 四刀演进，逐刀见台账） |
| 块清单 | petri:agent v3 · petri:ai v1 · petri:bridge v1 · petri:code v1 · petri:plugin-manager v1 · petri:porter v2 · petri:ui-shell v3 · petri:workflow v1 |
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
| 1 | P0-1 血统同步 | 页首注释+kmeta（非 stem 文本，hash 不变） | 补 petri:plugin-manager v1；ui-shell 版本 1→2；两份记录一致 | I1–I5 绿；I6 仍红（下一刀的锁定测试） |
| 2 | P2-2 垫片注入健壮化 | stem（core+宿主）；基准 `14121d04`→`141c2928` | 新增 core.injectAfterHead（零 DOM 沉 core，第 3 条）；RT.mount 改消费之，miniapp 无 `<head>` 不再静默丢 SDK | 全绿（I6 转绿）+ 自检绿 |
| 3 | P1-1 idbStore.list 单事务批量 | stem（宿主）；基准 `141c2928`→`369b8af8` | getAllKeys+getAll 同事务对齐取回，前缀内存过滤；消灭每键一事务的 N+1（旧机可跑，支柱三） | 全绿 + 自检绿 |
| 4 | P2-1+P3-1 PANEL 源码查看/下载定时 | stem（宿主）；基准 `369b8af8`→`295b382d` | 源码查看改 Blob 新页（去废弃 document.write，防弹窗拦截 null 崩）；revokeObjectURL 800ms→60s | 全绿 + 自检绿 |
| 5 | porter scan 短时缓存 | petri:porter v1→2（血统同 bump） | makeDataAPI.scan 加 800ms 读缓存 + data.set/del/copy/cleanup 即时失效；含全文趟不缓存；离线快照同享。门自检"篡改块版本"用例改通用正则（防版本 bump 失配） | 全绿 + 自检绿 |
