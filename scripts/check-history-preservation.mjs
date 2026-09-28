// Compare all History pages with a Git baseline, allowing only the migrated
// stylesheet/runtime tags. Questions, formulas, links and metadata must match.
import fs from 'node:fs';
import { readGitBaseline } from './lib/git-baseline.mjs';
import { createRequire } from 'node:module';
import { externalizeHistoryStyles } from './lib/history-styles.mjs';
const require = createRequire(import.meta.url);
const { ROOT, siteFiles } = require('./seo-html.cjs');
const baseline = process.argv.find(arg => arg.startsWith('--baseline='))?.slice(11) || 'HEAD';
const files = siteFiles().filter(file => file.startsWith('history/') && file.endsWith('.html'));
const normalize = html => externalizeHistoryStyles(html.replace(/\r\n/g, '\n'))
  .replace(/<script id="history-runtime"(?: src="\/assets\/js\/history-topic\.js")?>[\s\S]*?<\/script>/g, '');
const failures = [];
for await (const [file, bytes] of readGitBaseline(files, { root: ROOT, baseline })) {
  const before = bytes.toString('utf8');
  const after = fs.readFileSync(new URL(`../${file}`, import.meta.url), 'utf8');
  if (normalize(before) !== normalize(after)) failures.push(file);
}
console.log(JSON.stringify({ baseline, pages: files.length, unexpectedChanges: failures }, null, 2));
if (failures.length) process.exitCode = 1;
