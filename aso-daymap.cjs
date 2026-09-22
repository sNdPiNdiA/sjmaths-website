const fs = require('fs');
const h = fs.readFileSync('upsc-aso/index.html', 'utf8');
const topics = require('./upsc-aso/topics_v2.json');
const rows = Array.isArray(topics) ? topics : (topics.topics || []);

// find each syllabus li with checkbox id aso-cb-dN-mM
const liRe = /<li class="syllabus-item">[\s\S]*?<\/li>/g;
const items = [...h.matchAll(liRe)];
const byDay = {};
for (const m of items) {
  const li = m[0];
  const idm = li.match(/id="aso-cb-d(\d+)-m(\d+)"/);
  if (!idm) continue;
  const day = +idm[1];
  const linked = /class="microtopic-link"/.test(li) && /<a href/.test(li);
  // extract visible text
  let text = li.replace(/<input[^>]*>/, '')
    .replace(/<label[^>]*>/, '')
    .replace(/<a[^>]*>/g, '')
    .replace(/<\/a>/g, '')
    .replace(/<\/label>/, '')
    .replace(/<[^>]+>/g, ' ')
    .replace(/&amp;/g, '&').replace(/&nbsp;/g, ' ')
    .replace(/\s+/g, ' ').trim();
  (byDay[day] = byDay[day] || []).push({ linked, text });
}
const days = Object.keys(byDay).map(Number).sort((a, b) => a - b);
const arg = process.argv[2] ? +process.argv[2] : null;
for (const d of days) {
  if (arg && d !== arg) continue;
  const titles = rows.filter(r => r.day === d).map(r => r.title + '  ->' + r.subject_slug + '/' + r.slug);
  console.log(`\n=== DAY ${d} ===`);
  for (const b of byDay[d]) console.log(`  [${b.linked ? 'L' : ' '}] ${b.text}`);
  for (const t of titles) console.log(`   (topic) ${t}`);
}
