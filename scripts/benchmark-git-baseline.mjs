// Read-only comparison of the old per-file Git calls and the shared batch reader.
import { execFileSync } from 'node:child_process';
import { createRequire } from 'node:module';
import crypto from 'node:crypto';
import { performance } from 'node:perf_hooks';
import { readGitBaseline } from './lib/git-baseline.mjs';
const require = createRequire(import.meta.url);
const { ROOT, siteFiles } = require('./seo-html.cjs');
const limit = Number(process.argv.find(arg => arg.startsWith('--limit='))?.slice(8) || 100);
if (!Number.isSafeInteger(limit) || limit < 1) throw new Error('Use a positive integer limit.');
const files = siteFiles().filter(file => file.startsWith('upsc/') && file.endsWith('.html')).slice(0, limit);
const hash = bytes => crypto.createHash('sha256').update(bytes).digest('hex');
const legacy = new Map();
let started = performance.now();
for (const file of files) legacy.set(file, hash(execFileSync('git', ['show', `HEAD:${file}`], { cwd: ROOT, maxBuffer: 10e6 })));
const legacyMs = performance.now() - started;
started = performance.now();
const differences = [];
let seen = 0;
for await (const [file, bytes] of readGitBaseline(files, { root: ROOT })) {
  if (hash(bytes) !== legacy.get(file)) differences.push(file);
  seen++;
}
const batchMs = performance.now() - started;
console.log(JSON.stringify({ scope: 'Git baseline reads only, not whole audit/build time; second reader may benefit from warm filesystem cache', files: files.length, seen, differences, legacyMs, batchMs, ratio: legacyMs / batchMs }, null, 2));
if (differences.length || seen !== files.length) process.exitCode = 1;
