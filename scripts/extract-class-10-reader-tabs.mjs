import fs from 'node:fs';
import path from 'node:path';
import { createRequire } from 'node:module';
import { commitBuildWrites } from './lib/build-transaction.mjs';
import { class10ReaderTabsTag, externalizeClass10ReaderTabs, getClass10ReaderTabsRuntime, validateClass10ReaderTabs } from './lib/class-10-reader-tabs.mjs';

const require = createRequire(import.meta.url);
const { ROOT, siteFiles } = require('./seo-html.cjs');
const apply = process.argv.includes('--apply');
const pages = siteFiles().filter(file => file.startsWith('class-10-maths/chapter-wise-notes/') && file.endsWith('/index.html'));
const sample = 'class-10-maths/chapter-wise-notes/chapter-1-real-numbers/index.html';
const sampleHtml = fs.readFileSync(path.join(ROOT, sample), 'utf8');
const existingAsset = path.join(ROOT, 'assets/js/class-10-reader-tabs.js');
let runtime;
if (fs.existsSync(existingAsset)) runtime = getClass10ReaderTabsRuntime();
else {
  const source = [...sampleHtml.matchAll(/<script>([\s\S]*?)<\/script>/gi)].map(match => match[1]).find(script => {
    try { validateClass10ReaderTabs(script); return true; } catch { return false; }
  });
  if (!source) throw new Error(`Exact Class 10 reader tab runtime not found in ${sample}.`);
  runtime = validateClass10ReaderTabs(source);
}

const writes = new Map();
const changed = [];
for (const file of pages) {
  const absolute = path.join(ROOT, file);
  const before = fs.readFileSync(absolute, 'utf8');
  const hasExact = [...before.matchAll(/<script>([\s\S]*?)<\/script>/gi)].some(match => {
    try { validateClass10ReaderTabs(match[1]); return true; } catch { return false; }
  });
  if (!hasExact) continue;
  for (const required of ['nav-tab-item', 'nav-tab-pill', 'mobile-dock-btn', 'dockDrawerOverlay', 'tab-iframe']) {
    if (!before.includes(required)) throw new Error(`Required controller markup ${required} is missing in ${file}.`);
  }
  if (before.includes('data-class-10-reader-tabs="shared"')) throw new Error(`Duplicate Class 10 controller marker in ${file}.`);
  const after = externalizeClass10ReaderTabs(before, runtime, { strict: true });
  changed.push(file);
  writes.set(absolute, Buffer.from(after, 'utf8'));
}
if (![0, 14].includes(changed.length)) throw new Error(`Expected 0 or 14 exact controller replacements; found ${changed.length}.`);
if (apply) {
  if (!fs.existsSync(existingAsset)) writes.set(existingAsset, Buffer.from(`${runtime}\n`, 'utf8'));
  commitBuildWrites(writes);
}
console.log(JSON.stringify({ mode: apply ? 'apply' : 'dry-run', scannedPages: pages.length, exactReplacements: changed.length, untouchedPages: pages.length - changed.length, asset: class10ReaderTabsTag, writes: writes.size }, null, 2));
