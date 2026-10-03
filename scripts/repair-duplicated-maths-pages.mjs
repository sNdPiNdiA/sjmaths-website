import fs from 'node:fs';
import path from 'node:path';
import vm from 'node:vm';
import { createRequire } from 'node:module';
import { fileURLToPath } from 'node:url';
import { commitBuildWrites } from './lib/build-transaction.mjs';

const require = createRequire(import.meta.url);
const { recoverRepeatedBodyPage } = require('./lib/recover-katex-expanded-pages.cjs');
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const roots = [
  'class-9-maths', 'class-10-maths', 'class-11-maths', 'class-12-maths',
  'class-9-advanced-maths', 'class-9-advanced-science', 'class-9-science',
  'class-10-science', 'class-11-physics', 'class-12-physics',
  'smart-learning', 'ssc-cgl', 'upsc'
];
const apply = process.argv.includes('--apply');
const repairSource = fs.readFileSync(path.join(root, 'scripts/fix_maths_rendering_all_files.mjs'), 'utf8');
const blockMatch = repairSource.match(/const KATEX_HEAD_BLOCK = (`[\s\S]*?`);/);
if (!blockMatch) throw new Error('Cannot find the maintained KaTeX head template.');
const katexBlock = vm.runInNewContext(blockMatch[1]);

function walk(dir) {
  if (!fs.existsSync(dir)) return [];
  return fs.readdirSync(dir, { withFileTypes: true }).flatMap(entry => {
    const file = path.join(dir, entry.name);
    if (entry.isDirectory()) return walk(file);
    return entry.isFile() && entry.name.endsWith('.html') ? [file] : [];
  });
}

function count(source, expression) {
  return [...source.matchAll(expression)].length;
}

const candidates = roots.flatMap(directory => walk(path.join(root, directory)));
const writes = new Map();
const changed = [];
for (const file of candidates) {
  const before = fs.readFileSync(file, 'utf8');
  if (!before.includes("{ left: '$', right: '$', display: true },")) continue;
  const after = recoverRepeatedBodyPage(before, katexBlock);
  if (!after || count(after, /<html\b/gi) !== 1 || count(after, /<head\b/gi) !== 1 ||
      count(after, /<\/head\s*>/gi) !== 1 || count(after, /<body\b/gi) !== 1 ||
      count(after, /<\/html\s*>/gi) !== 1 ||
      !after.includes("{ left: '$$', right: '$$', display: true },") ||
      !after.includes("{ left: '$', right: '$', display: false },") ||
      after.includes("{ left: '$', right: '$', display: true },")) {
    throw new Error(`${path.relative(root, file)}: strict KaTeX recovery failed; refusing partial batch.`);
  }
  changed.push(file);
  writes.set(file, Buffer.from(after, 'utf8'));
}

if (![0, 96].includes(changed.length)) {
  throw new Error(`Expected 0 (already repaired) or 96 verified repeated-body pages; found ${changed.length}. Refusing to write.`);
}
if (apply) commitBuildWrites(writes);
const repairedByFolder = {};
for (const file of changed) {
  const folder = path.relative(root, file).split(path.sep)[0];
  repairedByFolder[folder] = (repairedByFolder[folder] || 0) + 1;
  const repaired = apply ? fs.readFileSync(file, 'utf8') : writes.get(file).toString('utf8');
  if (count(repaired, /<html\b/gi) !== 1 || count(repaired, /<body\b/gi) !== 1 ||
      count(repaired, /<\/html\s*>/gi) !== 1) throw new Error(`${path.relative(root, file)}: post-repair validation failed.`);
}
console.log(JSON.stringify({ mode: apply ? 'apply' : 'dry-run', scannedHtmlFiles: candidates.length, repairedPages: changed.length, folders: repairedByFolder, bodyContentsPreserved: true }, null, 2));
