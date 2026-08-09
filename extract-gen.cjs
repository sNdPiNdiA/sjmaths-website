const fs = require('fs');
const path = require('path');
const subs = ['hindi', 'sanskrit', 'english', 'science', 'teaching-skills', 'life-skill-management', 'information-technology'];
const out = [];
for (const s of subs) {
  const f = path.join('up-assistant-teacher', s, 'generate-microtopics.cjs');
  const txt = fs.readFileSync(f, 'utf8');
  // Get the MICROTOPICS array literal
  const start = txt.indexOf('const MICROTOPICS = [');
  const closeIdx = txt.indexOf('];', start);
  const arr = txt.slice(start, closeIdx + 1);
  // Parse each { dir: '...', name: '...', hindiName: '...' ... } block
  const dirRe = /dir:\s*'([^']+)'/g;
  const nmRe = /name:\s*'([^']+)'/g;
  const hiRe = /hindiName:\s*'([^']+)'/g;
  const dirs = [...arr.matchAll(dirRe)].map(x => x[1]);
  const names = [...arr.matchAll(nmRe)].map(x => x[1]);
  const his = [...arr.matchAll(hiRe)].map(x => x[1]);
  out.push('### ' + s + ' (' + dirs.length + ')');
  dirs.forEach((d, i) => out.push('  ' + (i + 1) + '. ' + d + ' || ' + (names[i] || '') + ' || ' + (his[i] || '')));
}
fs.writeFileSync('gen-list.txt', out.join('\n'), 'utf8');
console.log('done');
