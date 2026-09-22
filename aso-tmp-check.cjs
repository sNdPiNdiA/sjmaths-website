// Temp check: how many plain spans exist, are they inside <li>, and show day-96 sample
const fs = require('fs');
const h = fs.readFileSync('upsc-aso/index.html', 'utf8');
const spans = [...h.matchAll(/<span class="microtopic-link microtopic-plain">[\s\S]*?<\/span>/g)];
console.log('plain spans:', spans.length);
let inLi = 0;
for (const s of spans) {
  const before = h.slice(Math.max(0, s.index - 300), s.index);
  if (before.lastIndexOf('<li') > before.lastIndexOf('</li>')) inLi++;
}
console.log('inside <li>:', inLi, 'of', spans.length);
const i = h.indexOf('aso-cb-d96-m1');
console.log('--- day96 m1 context:');
console.log(h.slice(i - 150, i + 450));
console.log('=== now still-plain after first pass, grouped by day with day topics ===');
let raw = require('./upsc-aso/topics_v2.json');
if (!Array.isArray(raw)) raw = raw.topics || raw.TOPICS || Object.values(raw).find(Array.isArray);
const byDay = new Map();
for (const t of raw) {
  if (!byDay.has(t.day)) byDay.set(t.day, []);
  byDay.get(t.day).push(t);
}
const liRe = /<li[^>]*>(?:(?!<li[\s>])(?!<\/li>))[\s\S]*?<\/li>/g;
let lastDay = null;
for (const m of h.match(liRe) || []) {
  const li = m;
  if (!li.includes('microtopic-plain')) continue;
  const dm = li.match(/aso-cb-d(\d+)-/);
  const day = dm ? Number(dm[1]) : null;
  const label = li.replace(/<span class="microtopic-link microtopic-plain">([\s\S]*?)<\/span>/, '$1')
    .replace(/<[^>]+>/g, '').replace(/&amp;/g, '&').replace(/\s+/g, ' ').trim();
  console.log(`d${day} :: ${label}`);
  if (day !== lastDay) {
    lastDay = day;
    for (const t of (byDay.get(day) || [])) console.log(`     [topic] ${t.title} -> ${t.subject_slug}/${t.slug}`);
  }
}