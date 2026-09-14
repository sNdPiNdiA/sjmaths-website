// Compare this working tree with HEAD; duplicate copies may disappear, unique
// question text, solutions and authored inline data must remain present.
const fs = require('fs');
const path = require('path');
const { execFileSync } = require('child_process');
const cheerio = require('cheerio');
const { ROOT, compact } = require('./seo-html.cjs');
const files = execFileSync('git', ['-c', 'core.safecrlf=false', 'diff', '--name-only', '-z', '--', '*.html'], { cwd: ROOT, encoding: 'utf8', maxBuffer: 10e6 }).split('\0').filter(Boolean);
let checked = 0, items = 0, recoveredInvalidEmbeddedData = 0;
const failures = [];
for (let start = 0; start < files.length; start += 30) {
  const batch = files.slice(start, start + 30);
  const blobs = execFileSync('git', ['cat-file', '--batch'], { cwd: ROOT, input: batch.map(file => 'HEAD:' + file).join('\n') + '\n', maxBuffer: 120e6 });
  let offset = 0;
  for (const file of batch) {
    const headerEnd = blobs.indexOf(10, offset);
    const header = blobs.subarray(offset, headerEnd).toString('utf8');
    const size = Number(header.split(' ').at(-1));
    if (!Number.isFinite(size)) throw new Error(`Cannot read HEAD:${file}`);
    const before = blobs.subarray(headerEnd + 1, headerEnd + 1 + size).toString('utf8');
    offset = headerEnd + 1 + size + 1;
    if (!/question-card|upsc-page-data|embedded-study-guide-data/.test(before)) continue;
    const after = fs.readFileSync(path.join(ROOT, file), 'utf8');
    const old = cheerio.load(before), next = cheerio.load(after);
    for (const selector of ['.question-text', '.q-text', '.final-ans', '.final-answer', '.step', '#upsc-page-data', '#embedded-study-guide-data']) {
      const retained = new Set(next(selector).map((_, el) => compact(next(el).text())).get());
      const originals = new Set(old(selector).map((_, el) => compact(old(el).text())).get().filter(Boolean));
      for (const value of originals) {
        items++;
        if (retained.has(value)) continue;
        // Six legacy UPSSSC shells contained truncated/invalid inline JSON. Their
        // repair is valid only when the new JSON parses and contains every authored
        // section from the sibling data.json byte-for-byte at the object level.
        if (selector === '#upsc-page-data') {
          try {
            JSON.parse(value);
          } catch {
            try {
              const current = JSON.parse(next(selector).first().text());
              const authored = JSON.parse(fs.readFileSync(path.join(ROOT, path.posix.dirname(file), 'data.json'), 'utf8'));
              if (Object.entries(authored).every(([key, item]) => JSON.stringify(current[key]) === JSON.stringify(item))) {
                recoveredInvalidEmbeddedData++;
                continue;
              }
            } catch {}
          }
        }
        failures.push({ file, selector, preview: value.slice(0, 100) });
      }
    }
    checked++;
  }
}
const report = { comparedWith: 'HEAD', modifiedHtml: files.length, checkedPages: checked, uniqueContentItems: items, recoveredInvalidEmbeddedData, failures };
fs.mkdirSync(path.join(ROOT, 'scratch'), { recursive: true });
fs.writeFileSync(path.join(ROOT, 'scratch/seo-preservation.json'), JSON.stringify(report, null, 2) + '\n');
console.log(JSON.stringify(report, null, 2));
if (failures.length) process.exitCode = 1;
