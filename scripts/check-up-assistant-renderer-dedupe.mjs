import fs from 'node:fs';
import path from 'node:path';
import { createRequire } from 'node:module';
import { readGitBaseline } from './lib/git-baseline.mjs';
import { extractUpAssistantDuplicateRuntime, removeUpAssistantDuplicateRuntime } from './lib/up-assistant-renderer-dedupe.mjs';

const require = createRequire(import.meta.url);
const { ROOT, siteFiles } = require('./seo-html.cjs');
const baseline = process.argv.find(value => value.startsWith('--baseline='))?.slice('--baseline='.length)
  || '237db669da5fca0a8ff8ae6a5a601d284a367642';
const pages = siteFiles().filter(file => file.startsWith('up-assistant-teacher/') && file.endsWith('/index.html'));
let runtime = null;
let removed = 0;
let untouched = 0;
for await (const [file, bytes] of readGitBaseline(pages, { root: ROOT, baseline })) {
  const original = bytes.toString('utf8');
  runtime ||= extractUpAssistantDuplicateRuntime(original);
  const expected = removeUpAssistantDuplicateRuntime(original, runtime);
  const current = removeUpAssistantDuplicateRuntime(fs.readFileSync(path.join(ROOT, file), 'utf8'), runtime);
  if (expected !== original) removed++;
  else untouched++;
  if (current !== expected) {
    let offset = 0;
    while (offset < Math.min(current.length, expected.length) && current[offset] === expected[offset]) offset++;
    throw new Error(`Unexpected page/content change: ${file} (expected ${expected.length} chars, found ${current.length}; first mismatch ${offset}: ${JSON.stringify(expected.slice(offset - 32, offset + 60))} vs ${JSON.stringify(current.slice(offset - 32, offset + 60))}).`);
  }
}
if (pages.length !== 264 || removed !== 153 || untouched !== 111) {
  throw new Error(`Expected 264 pages (153 exact removals, 111 unchanged); found ${pages.length} (${removed} removed, ${untouched} unchanged).`);
}
console.log(JSON.stringify({ baseline, pages: pages.length, exactDuplicateRemovals: removed, byteIdenticalUntouched: untouched }, null, 2));
