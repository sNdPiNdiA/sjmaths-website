import fs from 'node:fs';
import path from 'node:path';

function findHtml(dir) {
  let list = [];
  for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
    const p = path.join(dir, e.name);
    if (e.isDirectory()) list.push(...findHtml(p));
    else if (e.name === 'index.html') list.push(p);
  }
  return list;
}

const files = findHtml(path.join(process.cwd(), 'mathematics'));
console.log('Found:', files.length);

const sample = files.slice(0, 5).map(f => {
  const text = fs.readFileSync(f, 'utf8');
  const titleMatch = text.match(/<title>([^<]+)<\/title>/i);
  const kickerMatch = text.match(/<div class="kicker">([^<]+)<\/div>/i);
  return {
    file: path.relative(process.cwd(), f),
    title: titleMatch ? titleMatch[1].replace(/ — Mathematics.*$/, '').trim() : '',
    kicker: kickerMatch ? kickerMatch[1].trim() : ''
  };
});
console.log(JSON.stringify(sample, null, 2));
