const fs = require('fs');
const h = fs.readFileSync('upsc-aso/index.html', 'utf8');

// Find all day-card blocks and their checklist <li> items
const out = [];
const dayRe = /<div class="day-card[^"]*"[^>]*data-day="(\d+)"[^>]*>([\s\S]*?)(?=<div class="day-card|$)/g;
let m;
while ((m = dayRe.exec(h))) {
  const day = m[1], block = m[2];
  const liRe = /<li[^>]*>([\s\S]*?)<\/li>/g;
  let lm;
  while ((lm = liRe.exec(block))) {
    const raw = lm[1];
    if (/<a\s/.test(raw)) continue; // already linked
    const text = raw.replace(/<[^>]+>/g, ' ').replace(/&amp;/g, '&').replace(/\s+/g, ' ').trim();
    if (!text) continue;
    out.push({ day: +day, text });
  }
}
// fallback: if data-day attr not found, try headers
if (out.length === 0) {
  const hdrRe = /Day\s+(\d+)/g;
  console.log('FALLBACK needed — data-day attr not found');
}
fs.writeFileSync('aso-unlinked.json', JSON.stringify(out, null, 1));
console.log('total unlinked bullets:', out.length);
const days = [...new Set(out.map(o => o.day))].sort((a, b) => a - b);
console.log('days covered:', days.join(','));
out.slice(0, 60).forEach(o => console.log(`D${o.day} | ${o.text}`));
