import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = path.dirname(fileURLToPath(import.meta.url));
const weeklyRoot = path.join(root, 'data', 'weekly');
function files(dir) { return fs.readdirSync(dir, { withFileTypes: true }).flatMap(e => e.isDirectory() ? files(path.join(dir, e.name)) : e.name.endsWith('.json') ? [path.join(dir, e.name)] : []); }
function repair(value) {
  let result = String(value);
  for (let i = 0; i < 3 && /[ÃÂà¤]/.test(result); i++) {
    const next = Buffer.from(result, 'latin1').toString('utf8');
    if (next === result || next.includes('\uFFFD')) break;
    result = next;
  }
  return result;
}
for (const file of files(weeklyRoot)) {
  const data = JSON.parse(fs.readFileSync(file, 'utf8').replace(/^\uFEFF/, ''));
  for (const topic of data.topics || []) {
    if (!topic.hi) continue;
    for (const key of ['category', 'title', 'importance', 'detail', 'exam', 'remember']) topic.hi[key] = repair(topic.hi[key]);
    topic.hi.facts = (topic.hi.facts || []).map(repair);
  }
  fs.writeFileSync(file, `${JSON.stringify(data, null, 2)}\n`, 'utf8');
  console.log(`Repaired ${path.relative(root, file)}`);
}
