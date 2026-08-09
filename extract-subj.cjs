const fs = require('fs');
const path = require('path');
const subs = ['hindi', 'sanskrit', 'english', 'science', 'teaching-skills', 'life-skill-management', 'information-technology', 'child-psychology', 'environmental-social-studies', 'mathematics', 'logical-reasoning', 'gk-current-affairs'];
const out = [];
for (const s of subs) {
  const f = path.join('up-assistant-teacher', s, 'index.html');
  if (!fs.existsSync(f)) { out.push('### ' + s + ' :: NO INDEX'); continue; }
  const h = fs.readFileSync(f, 'utf8');
  const re = /href="([^"]+)"/g;
  let m;
  const links = [];
  const prefix = '/up-assistant-teacher/' + s + '/';
  while ((m = re.exec(h))) {
    const href = m[1];
    if (href.indexOf(prefix) === 0) {
      const rest = href.slice(prefix.length);
      const seg = rest.split('/')[0];
      if (seg && !seg.includes('.') && !seg.includes('#') && !seg.includes('?') && seg !== 'index.html' && links.indexOf(seg) === -1) links.push(seg);
    }
  }
  out.push('### ' + s + ' (' + links.length + ')');
  links.forEach(l => out.push('  ' + l));
}
fs.writeFileSync('subj-index-list.txt', out.join('\n'), 'utf8');
console.log('done');
