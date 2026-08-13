#!/usr/bin/env node
/* Colony 门禁(宪法第6/7条): node 原生可跑的不变式, 一条不过即失败(exit 1)。
   用法:
     node tests/gate.mjs              # 对 colony.html 全量重跑不变式
     node tests/gate.mjs --self-test  # 门自检守卫(第6条): 注入必败用例, 验证"失败必红"
   不变式清单:
     I1 血统同步   : DOM 块标签 与 <!--COLONY-LINEAGE--> 与 stem-kmeta __LINEAGE 三方 id/版本一致
     I2 基准哈希   : core.hash(stem文本) === kmeta __STEM_HASH === 两份 lineage.stemHash
     I3 无损往返   : 每块 parseBlock(blockText(manifest, code)) 与原块 manifest/code 逐字节一致
     I4 凭证卫生   : 每块 validateCode 通过(无字面闭合标签序列)
     I5 蜕皮一致   : moltHtml(当前生效块) 产物的 lineage/块数/哈希 与输入自洽
     I6 注入健壮   : core.injectAfterHead 对 无<head>/有<head>/裸片段 输入均产出含垫片的 HTML */
import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';
import vm from 'node:vm';

const ROOT = join(dirname(fileURLToPath(import.meta.url)), '..');
const HTML_PATH = join(ROOT, 'colony.html');

function loadCore(html) { // 在隔离 vm 上下文里执行 stem 脚本(node 无 document → 不 boot), 取 __KCore
  const open = html.indexOf('<script id="stem">');
  if (open < 0) throw new Error('找不到 <script id="stem">');
  const start = open + '<script id="stem">'.length;
  const end = html.indexOf('</scr' + 'ipt>', start);
  if (end < 0) throw new Error('stem 脚本未闭合');
  const stemText = html.slice(start, end);
  const sandbox = { console };
  vm.createContext(sandbox);
  vm.runInContext(stemText, sandbox, { filename: 'stem.js' });
  if (!sandbox.__KCore) throw new Error('stem 执行后无 __KCore');
  return { core: sandbox.__KCore, stemText };
}

function kmetaOf(html) { // stem-kmeta 的 __STEM_HASH / __LINEAGE
  const seg = /<script id="stem-kmeta">([\s\S]*?)<\/script>/.exec(html);
  if (!seg) throw new Error('找不到 stem-kmeta');
  const h = /__STEM_HASH\s*=\s*"([0-9a-f]{8})"/.exec(seg[1]);
  const l = /__LINEAGE\s*=\s*([\s\S]*?);\s*$/m.exec(seg[1]);
  if (!h || !l) throw new Error('kmeta 缺 __STEM_HASH 或 __LINEAGE');
  return { hash: h[1], lineage: JSON.parse(l[1]) };
}

function runChecks(html, label) {
  const fails = [];
  const ok = (name, cond, detail) => { if (!cond) fails.push(name + (detail ? ' — ' + detail : '')); };
  let core, stemText, blocks, comment, kmeta;
  try {
    ({ core, stemText } = loadCore(html));
    blocks = core.findBlockTags(html);
    comment = core.findLineage(html);
    kmeta = kmetaOf(html);
  } catch (e) { fails.push('装载失败: ' + e.message); return report(label, fails); }

  /* I1 血统同步 */
  const domIds = blocks.map(b => b.manifest.id).sort();
  for (const [src, lin] of [['comment', comment], ['kmeta', kmeta.lineage]]) {
    const ids = (lin.blocks || []).map(b => b.id).sort();
    ok('I1.' + src + '.块数', ids.length === domIds.length, `DOM ${domIds.length} 块, ${src} 记录 ${ids.length} 块`);
    ok('I1.' + src + '.id集合', JSON.stringify(ids) === JSON.stringify(domIds),
      `缺: ${domIds.filter(x => !ids.includes(x)).join(',') || '无'}; 多: ${ids.filter(x => !domIds.includes(x)).join(',') || '无'}`);
    for (const b of blocks) {
      const rec = (lin.blocks || []).find(x => x.id === b.manifest.id);
      if (rec) ok('I1.' + src + '.版本.' + b.manifest.id, rec.version === b.manifest.version,
        `manifest v${b.manifest.version} ≠ 血统 v${rec.version}`);
    }
  }
  ok('I1.双录一致', JSON.stringify(comment) === JSON.stringify(kmeta.lineage), '页首注释与 kmeta 的 lineage 不一致');

  /* I2 基准哈希 */
  const h = core.hash(stemText);
  ok('I2.kmeta哈希', kmeta.hash === h, `kmeta ${kmeta.hash} ≠ 实算 ${h}`);
  ok('I2.comment哈希', comment.stemHash === h, `comment ${comment.stemHash} ≠ 实算 ${h}`);
  ok('I2.kmeta血统哈希', kmeta.lineage.stemHash === h, `kmeta lineage ${kmeta.lineage.stemHash} ≠ 实算 ${h}`);

  /* I3 无损往返 + I4 凭证卫生 */
  for (const b of blocks) {
    try {
      core.validateCode(b.code, b.manifest.id);
      const rt = core.parseBlock(core.blockText(b.manifest, b.code));
      ok('I3.' + b.manifest.id, JSON.stringify(rt.manifest) === JSON.stringify(b.manifest) && rt.code === core.norm(b.code), '往返不一致');
    } catch (e) { fails.push('I3/I4.' + b.manifest.id + ' — ' + e.message); }
  }

  /* I5 蜕皮一致 */
  try {
    const eff = blocks.map(b => ({ manifest: b.manifest, code: b.code, dirty: false, disabled: !!b.tagDisabled }));
    const out = core.moltHtml({ stemText, blocks: eff, bumpVersion: false, lineage: { gen: 2, parent: h, note: 'gate' } });
    const lin2 = core.findLineage(out);
    ok('I5.块数', core.findBlockTags(out).length === blocks.length);
    ok('I5.血统块数', lin2.blocks.length === blocks.length);
    ok('I5.哈希', lin2.stemHash === h);
  } catch (e) { fails.push('I5 — ' + e.message); }

  /* I6 注入健壮(P2-2 之刀的锁定测试): 三种形状都必须含垫片 */
  if (typeof core.injectAfterHead !== 'function') fails.push('I6 — core.injectAfterHead 未实现');
  else {
    const PIN = '<script>window.__pin=1</scr' + 'ipt>';
    for (const [name, doc] of [
      ['有head', '<!DOCTYPE html><html><head><title>x</title></head><body>hi</body></html>'],
      ['无head', '<html><body><script>1</scr' + 'ipt></body></html>'],
      ['裸片段', '<div>naked</div>'],
    ]) {
      let out = '';
      try { out = core.injectAfterHead(doc, PIN); } catch (e) { fails.push('I6.' + name + ' — 抛错 ' + e.message); continue; }
      ok('I6.' + name + '.含垫片', out.includes(PIN));
      ok('I6.' + name + '.原文保留', out.replace(PIN, '').replace('<head>', '').replace('</head>', '') === doc || out.includes(name === '裸片段' ? 'naked' : '<body>'));
      const headIdx = out.search(/<head[\s>]/i), pinIdx = out.indexOf(PIN);
      if (headIdx >= 0) ok('I6.' + name + '.位置', pinIdx > headIdx, '垫片须在 <head> 之后');
    }
  }

  return report(label, fails);
}

function report(label, fails) {
  if (fails.length) {
    console.error(`✗ 门禁失败(${label}): ${fails.length} 条不变式不过`);
    for (const f of fails) console.error('  · ' + f);
    return false;
  }
  console.log(`✓ 门禁通过(${label})`);
  return true;
}

const html = readFileSync(HTML_PATH, 'utf8');

if (process.argv.includes('--self-test')) {
  /* 门自检守卫(第6条): 三个必败注入, 门若不红即门坏 */
  const cases = [
    ['删一块血统', html.replace(/\{\s*"id":\s*"petri:workflow",\s*"version":\s*\d+,\s*"dirty":\s*(?:false|true)\s*\}\s*(,?)/, '')],
    ['篡改kmeta哈希', html.replace(/__STEM_HASH="[0-9a-f]{8}"/, '__STEM_HASH="deadbeef"')],
    ['篡改块版本', html.replace(/("id":"petri:[\w-]+","name":"[^"]*","version":)(\d+)/, (m, p1) => p1 + '99')], // 命中首个紧凑 manifest(血统记录是带空格的 pretty JSON, 不会误中)
  ];
  let broken = 0;
  for (const [name, bad] of cases) {
    if (bad === html) { console.error('✗ 自检用例未生效(替换没命中): ' + name); broken++; continue; }
    const silent = (() => { const e = console.error; console.error = () => { }; const r = runChecks(bad, '自检·' + name); console.error = e; return r; })();
    if (silent) { console.error('✗ 门自检失败: 注入「' + name + '」后门居然是绿的 — 守卫失效'); broken++; }
    else console.log('✓ 自检: 「' + name + '」如期变红');
  }
  process.exit(broken ? 1 : 0);
}

process.exit(runChecks(html, 'colony.html') ? 0 : 1);
