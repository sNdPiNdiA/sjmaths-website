// Only exact runtime replacement is allowed; all authored content stays intact.
import fs from 'node:fs';
import path from 'node:path';
import { createRequire } from 'node:module';
import { readGitBaseline } from './lib/git-baseline.mjs';
import { externalizeAgricultureRuntime } from './lib/agriculture-runtime.mjs';
const require = createRequire(import.meta.url);
const { ROOT, siteFiles } = require('./seo-html.cjs');
const baseline = process.argv.find(arg => arg.startsWith('--baseline='))?.slice(11) || 'HEAD';
const files = siteFiles().filter(file => file.startsWith('agriculture/') && file.endsWith('.html'));
const normalize = html => externalizeAgricultureRuntime(html.replace(/\r\n/g, '\n'));
const failures = [];
for await (const [file, bytes] of readGitBaseline(files, { root: ROOT, baseline })) {
  if (normalize(bytes.toString('utf8')) !== normalize(fs.readFileSync(path.join(ROOT, file), 'utf8'))) failures.push(file);
}
console.log(JSON.stringify({ baseline, pages: files.length, unexpectedChanges: failures }, null, 2));
if (failures.length) process.exitCode = 1;
