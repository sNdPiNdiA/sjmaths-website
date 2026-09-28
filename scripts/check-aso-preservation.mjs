// Allow only the exact shared style replacement versus Git's baseline.
import fs from 'node:fs';
import path from 'node:path';
import { readGitBaseline } from './lib/git-baseline.mjs';
import { createRequire } from 'node:module';
import { externalizeAsoStyles } from './lib/aso-styles.mjs';
const require = createRequire(import.meta.url);
const { ROOT, siteFiles } = require('./seo-html.cjs');
const baseline = process.argv.find(arg => arg.startsWith('--baseline='))?.slice(11) || 'HEAD';
const files = siteFiles().filter(file => file.startsWith('upsc-aso/') && file.endsWith('.html'));
const normalize = html => externalizeAsoStyles(html.replace(/\r\n/g, '\n'));
const failures = [];
for await (const [file, bytes] of readGitBaseline(files, { root: ROOT, baseline })) {
  const before = bytes.toString('utf8');
  const after = fs.readFileSync(path.join(ROOT, file), 'utf8');
  if (normalize(before) !== normalize(after)) failures.push(file);
}
console.log(JSON.stringify({ baseline, pages: files.length, unexpectedChanges: failures }, null, 2));
if (failures.length) process.exitCode = 1;
