const fs = require('fs');
const h = fs.readFileSync('up-assistant-teacher/index.html', 'utf8');

// Find each <details class="syllabus-subsection" ...> ... </details> block
const detailsRe = /<details class="syllabus-subsection"([\s\S]*?)<\/details>/g;
let m;
const out = [];
while ((m = detailsRe.exec(h))) {
  const blk = m[1];
  const preM = blk.match(/data-prefix="([^"]+)"/);
  const grpM = blk.match(/data-grp-idx="([^"]+)"/);
  const pre = preM ? preM[1] : '?';
  const grp = grpM ? grpM[1] : '?';
  const items = [];
  const itemRe = /<li class="syllabus-item">([\s\S]*?)<\/li>/g;
  let im;
  while ((im = itemRe.exec(blk))) {
    const li = im[1];
    const idM = li.match(/id="([^"]+)"/);
    const textM = li.match(/class="syllabus-text">([\s\S]*?)<\/span>/);
    items.push((idM ? idM[1] : '?') + ' ||| ' + (textM ? textM[1].replace(/\s+/g, ' ').trim() : '?'));
  }
  out.push('### prefix=' + pre + ' grp=' + grp + ' (' + items.length + ' items)');
  items.forEach(t => out.push('  ' + t));
}
fs.writeFileSync('items-list.txt', out.join('\n'), 'utf8');
console.log('done');
