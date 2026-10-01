import fs from 'node:fs';
import path from 'node:path';
import { createRequire } from 'node:module';
import { commitBuildWrites } from './lib/build-transaction.mjs';
import { extractUpAssistantDuplicateRuntime, getUpAssistantDuplicateRuntime, removeUpAssistantDuplicateRuntime } from './lib/up-assistant-renderer-dedupe.mjs';
import { readGitBaseline } from './lib/git-baseline.mjs';

const require = createRequire(import.meta.url);
const { ROOT, siteFiles } = require('./seo-html.cjs');
const apply = process.argv.includes('--apply');
const baseline = '237db669da5fca0a8ff8ae6a5a601d284a367642';
const assetPath = path.join(ROOT, 'assets/js/up-assistant-tabs.js');
const pages = siteFiles().filter(file => file.startsWith('up-assistant-teacher/') && file.endsWith('/index.html'));
const sample = 'up-assistant-teacher/child-psychology/creating-conducive-learning-environment/index.html';
let runtime = fs.existsSync(assetPath) ? getUpAssistantDuplicateRuntime() : null;
if (!runtime) {
  for await (const [, bytes] of readGitBaseline([sample], { root: ROOT, baseline })) runtime = extractUpAssistantDuplicateRuntime(bytes.toString('utf8'));
}
if (!runtime) throw new Error('Could not recover the exact duplicate script from the audited baseline.');
const sourceRenderer = fs.readFileSync(path.join(ROOT, 'assets/js/upsc-renderer.js'), 'utf8');
for (const marker of ['studyTabs.addEventListener("click"', 'setAttribute("aria-selected"', 'renderTabContent(tabName)']) {
  if (!sourceRenderer.includes(marker)) throw new Error(`UP Assistant shared renderer no longer owns tab behavior: ${marker}`);
}
const minifiedRenderer = fs.readFileSync(path.join(ROOT, 'assets/js/upsc-renderer.min.js'), 'utf8');
for (const marker of ['.tab-btn', 'aria-selected', 'innerHTML=n']) {
  if (!minifiedRenderer.includes(marker)) throw new Error(`The minified renderer is missing shared tab behavior: ${marker}`);
}

const writes = new Map();
const changedPages = [];
for (const file of pages) {
  const absolute = path.join(ROOT, file);
  const before = fs.readFileSync(absolute, 'utf8');
  const hasInline = [...before.matchAll(/<script>([\s\S]*?)<\/script>/gi)].some(match => match[1].trim() === runtime);
  const hasReference = /<script\b(?=[^>]*\bdata-up-assistant-tabs-runtime=["']shared["'])[^>]*>\s*<\/script\s*>/i.test(before);
  if (!hasInline && !hasReference) continue;
  if (hasInline && hasReference) throw new Error(`Both inline and external duplicate runtimes found in ${file}.`);
  if (!/src=["'][^"']*upsc-renderer(?:\.min)?\.js(?:\?[^"']*)?["']/.test(before)
      || !/id=["']upsc-page-data["']/.test(before)
      || !/class=["'][^"']*\bstudy-tabs\b/.test(before)) {
    throw new Error(`Renderer-owned tab markup is incomplete in ${file}; refusing removal.`);
  }
  const after = removeUpAssistantDuplicateRuntime(before, runtime, { strict: true });
  if (after === before) throw new Error(`Expected removal did not change ${file}.`);
  changedPages.push(file);
  writes.set(absolute, Buffer.from(after, 'utf8'));
}
if (![0, 153].includes(changedPages.length) || pages.length !== 264) {
  throw new Error(`Expected 264 pages and either 0 or 153 duplicate runtimes; found ${pages.length} and ${changedPages.length}.`);
}

if (apply) {
  commitBuildWrites(writes);
  if (fs.existsSync(assetPath)) fs.unlinkSync(assetPath);
}
console.log(JSON.stringify({ mode: apply ? 'apply' : 'dry-run', scannedPages: pages.length, duplicateRuntimesRemoved: changedPages.length, untouchedPages: pages.length - changedPages.length, writes: writes.size }, null, 2));
