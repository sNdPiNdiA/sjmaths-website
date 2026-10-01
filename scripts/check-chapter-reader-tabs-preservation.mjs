import fs from 'node:fs';
import path from 'node:path';
import { createRequire } from 'node:module';
import { readGitBaseline } from './lib/git-baseline.mjs';
import { chapterReaderTabsTag, externalizeChapterReaderTabs, validateChapterReaderTabs } from './lib/chapter-reader-tabs.mjs';

const require = createRequire(import.meta.url);
const { ROOT, siteFiles } = require('./seo-html.cjs');
const baseline = process.argv.find(value => value.startsWith('--baseline='))?.slice('--baseline='.length)
  || '237db669da5fca0a8ff8ae6a5a601d284a367642';
const scope = file => file.endsWith('/index.html')
  && (file.startsWith('class-11-maths/chapter-wise-notes/')
    || file.startsWith('class-12-maths/chapter-wise-notes/')
    || file.startsWith('class-9-maths/'));
const pages = siteFiles().filter(scope);
const assetPath = path.join(ROOT, 'assets/js/chapter-reader-tabs.js');
const runtime = validateChapterReaderTabs(fs.readFileSync(assetPath, 'utf8'));
let migrated = 0;
for await (const [file, bytes] of readGitBaseline(pages, { root: ROOT, baseline })) {
  const original = bytes.toString('utf8');
  const expected = externalizeChapterReaderTabs(original, runtime);
  const current = fs.readFileSync(path.join(ROOT, file), 'utf8');
  if (expected !== original) migrated++;
  if (current !== expected) throw new Error(`Unexpected page/content change: ${file}`);
}
if (migrated !== 25 || pages.length < migrated) throw new Error(`Expected 25 exact controller replacements; found ${migrated} across ${pages.length} pages.`);
console.log(JSON.stringify({ baseline, pages: pages.length, exactReplacements: migrated, untouched: pages.length - migrated, sharedTag: chapterReaderTabsTag }, null, 2));
