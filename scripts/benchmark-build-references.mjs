// Read-only full-corpus equivalence and CPU measurement; writes evidence only.
import fs from 'node:fs';
import path from 'node:path';
import { createRequire } from 'node:module';
import { createReferenceUpdater } from './lib/build-references.mjs';
import { legacyReferenceUpdater } from './fixtures/build-references-legacy.mjs';
const require = createRequire(import.meta.url);
const { ROOT, siteFiles } = require('./seo-html.cjs');
const mapping = {};
function collect(directory, extensions) {
  if (!fs.existsSync(path.join(ROOT, directory))) return;
  for (const entry of fs.readdirSync(path.join(ROOT, directory), { withFileTypes: true })) {
    const file = path.posix.join(directory, entry.name);
    if (entry.isDirectory()) collect(file, extensions);
    else if (extensions.includes(path.extname(file)) && !file.includes('.min.')) mapping[file] = file.replace(/\.(js|css)$/, '.min.$1');
  }
}
collect('assets', ['.js', '.css']);
collect('utils', ['.js']);
for (const name of ['all', 'fontawesome']) {
  const file = `assets/vendor/fontawesome/css/${name}.min.css`;
  if (fs.existsSync(path.join(ROOT, file))) { mapping['./' + file] = './' + file; mapping[file] = file; }
}
const hashes = Object.fromEntries(Object.values(mapping).map(file => [file, '1234abcd']));
const update = createReferenceUpdater(mapping, hashes), old = legacyReferenceUpdater(mapping, hashes);
const files = siteFiles().filter(file => (file.endsWith('.html') || file === 'service-worker.js') && fs.existsSync(path.join(ROOT, file)));
const differences = [];
let oldNs = 0n, newNs = 0n, bytes = 0;
for (const [index, file] of files.entries()) {
  const source = fs.readFileSync(path.join(ROOT, file), 'utf8');
  bytes += Buffer.byteLength(source);
  let time = process.hrtime.bigint();
  const before = old(source);
  oldNs += process.hrtime.bigint() - time;
  time = process.hrtime.bigint();
  const after = update(source);
  newNs += process.hrtime.bigint() - time;
  if (before !== after) differences.push(file);
  if ((index + 1) % 2000 === 0) console.log(`Compared ${index + 1}/${files.length} files.`);
}
const result = { files: files.length, bytes, mappings: Object.keys(mapping).length, differences,
  oldMs: Number(oldNs) / 1e6, newMs: Number(newNs) / 1e6, speedup: Number(oldNs) / Number(newNs),
  scope: 'reference transformation CPU only; fixed hashes; interleaved comparison; excludes compilation, file IO and transaction costs',
};
const output = path.join(ROOT, 'scratch/refactor/build-reference-benchmark.json');
fs.mkdirSync(path.dirname(output), { recursive: true });
fs.writeFileSync(output, JSON.stringify(result, null, 2) + '\n');
console.log(JSON.stringify(result, null, 2));
if (differences.length) process.exitCode = 1;
