import fs from 'node:fs';
import path from 'node:path';

const root = path.join(process.cwd(), 'mathematics');

function analyze(dir, depth = 0) {
  let leaves = [];
  let hubs = [];
  const entries = fs.readdirSync(dir, { withFileTypes: true });
  const hasIndex = entries.some(e => e.isFile() && e.name === 'index.html');
  const subDirs = entries.filter(e => e.isDirectory());

  if (hasIndex) {
    if (subDirs.length === 0) {
      leaves.push(dir);
    } else {
      hubs.push(dir);
    }
  }

  for (const s of subDirs) {
    const res = analyze(path.join(dir, s.name), depth + 1);
    leaves = leaves.concat(res.leaves);
    hubs = hubs.concat(res.hubs);
  }

  return { leaves, hubs };
}

const { leaves, hubs } = analyze(root);
console.log('Leaf topics count:', leaves.length);
console.log('Intermediate hubs count:', hubs.length);
console.log('Intermediate hubs:');
hubs.forEach(d => console.log(' ', path.relative(process.cwd(), d)));
