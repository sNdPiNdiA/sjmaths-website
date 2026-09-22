// Verify: for every syllabus-item, the href (if any) equals bestMatch(label) target
const fs = require('fs'), path = require('path');
const BASE = path.join(__dirname, 'upsc-aso');
const PILLARS = fs.readdirSync(BASE).filter(d => fs.statSync(path.join(BASE, d)).isDirectory() && !d.startsWith('.'));
const registry = [];
for (const p of PILLARS) {
  for (const s of fs.readdirSync(path.join(BASE, p)).filter(d => fs.statSync(path.join(BASE, p, d)).isDirectory())) {
    const f = path.join(BASE, p, s, 'index.html');
    if (!fs.existsSync(f)) continue;
    let title = ((fs.readFileSync(f, 'utf8').match(/<title>([^<]+)<\/title>/) || [])[1] || s);
    title = title.split(/\s+\|\s+/)[0].replace(/\s*[—–]\s*Coming Soon\s*$/i, '').trim();
    registry.push({ pillar: p, slug: s, title });
  }
}
const norm = t => t.toLowerCase().replace(/&amp;/g, '&').replace(/&[a-z]+;/g, ' ').replace(/[^a-z0-9]+/g, ' ').replace(/\s+/g, ' ').trim();
const STOP = new Set(['the','a','an','of','and','or','vs','in','on','for','to','with','by','at','as']);
const toks = t => norm(t).split(' ').filter(w => w && !STOP.has(w) && w.length > 1);
// light stemming: strip trailing 's' for >3-char words
const stem = w => (w.length > 3 && w.endsWith('s')) ? w.slice(0, -1) : w;
function bestMatch(label) {
  const lt = toks(label).map(stem);
  if (!lt.length) return null;
  let best = null, bestScore = 0;
  for (const r of registry) {
    const rs = new Set(toks(r.title).map(stem));
    let inter = 0;
    for (const w of new Set(lt)) if (rs.has(w)) inter++;
    const score = inter / Math.max(1, Math.min(lt.length, rs.size));
    if (score > bestScore) { bestScore = score; best = r; }
  }
  return bestScore >= 0.6 ? best : null;
}
const hub = fs.readFileSync(path.join(BASE, 'index.html'), 'utf8');
const liRe = /<li class="syllabus-item[^"]*">[\s\S]*?<\/li>/g;
let ok = 0, mismatch = [], linked = 0, plain = 0;
let m;
while ((m = liRe.exec(hub))) {
  const li = m[0];
  const lbl = (li.match(/aria-label="Mark ([^"]*) as complete"/) || [])[1];
  if (!lbl) continue;
  const href = (li.match(/<a\s[^>]*href="([^"]+)"/) || [])[1];
  if (!href) { plain++; continue; }
  linked++;
  const bm = bestMatch(lbl);
  const target = bm ? `/upsc-aso/${bm.pillar}/${bm.slug}/` : null;
  if (target && href === target) ok++;
  else mismatch.push(`${lbl} -> ${href} (expected ${target || 'NONE — should be stripped'})`);
}
console.log(`bullets: linked=${linked} plainText=${plain} | href==expected: ${ok} | mismatches: ${mismatch.length}`);
mismatch.slice(0, 30).forEach(x => console.log('  ' + x));
