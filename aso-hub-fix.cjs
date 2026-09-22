// Fix hub checklist links: map every syllabus-item bullet to the correct topic page
const fs = require('fs'), path = require('path');
const BASE = path.join(__dirname, 'upsc-aso');
const PILLARS = fs.readdirSync(BASE).filter(d => fs.statSync(path.join(BASE, d)).isDirectory() && !d.startsWith('.'));
const HUB_FILES = new Set(PILLARS); // folder names at BASE level (pillar hubs)

// 1) registry: pillar/slug -> title (from <title> tag of index.html)
const registry = [];
for (const p of PILLARS) {
  const subs = fs.readdirSync(path.join(BASE, p)).filter(d => fs.statSync(path.join(BASE, p, d)).isDirectory());
  for (const s of subs) {
    const f = path.join(BASE, p, s, 'index.html');
    if (!fs.existsSync(f)) { console.log('MISSING PAGE: ' + p + '/' + s); continue; }
    const html = fs.readFileSync(f, 'utf8');
    let title = (html.match(/<title>([^<]+)<\/title>/) || [])[1] || s;
    title = title.split(/\s+\|\s+/)[0].replace(/\s*[—–]\s*Coming Soon\s*$/i, '').trim();
    registry.push({ pillar: p, slug: s, title });
  }
}
console.log('registry size:', registry.length);

const norm = t => t.toLowerCase().replace(/&amp;/g, '&').replace(/&[a-z]+;/g, ' ')
  .replace(/[^a-z0-9]+/g, ' ').replace(/\s+/g, ' ').trim();
const STOP = new Set(['the','a','an','of','and','or','vs','in','on','for','to','with','by','at','as']);
const toks = t => norm(t).split(' ').filter(w => w && !STOP.has(w) && w.length > 1);
function bestMatch(label) {
  const lt = toks(label);
  if (!lt.length) return null;
  let best = null, bestScore = 0;
  for (const r of registry) {
    const rt = toks(r.title);
    const rs = new Set(rt);
    let inter = 0;
    for (const w of new Set(lt)) if (rs.has(w)) inter++;
    const score = inter / Math.max(1, Math.min(lt.length, rt.length));
    if (score > bestScore) { bestScore = score; best = r; }
  }
  return bestScore >= 0.6 ? best : null;
}
// 2) rewrite every syllabus-item link in the hub
let hub = fs.readFileSync(path.join(BASE, 'index.html'), 'utf8');
const itemRe = /(<li class="syllabus-item">[^<]*<input[^>]*aria-label="Mark ([^"]*) as complete"[^>]*>[\s\S]*?<a\s)(href=")([^"]*)("[^>]*>)([\s\S]*?)(<\/a>)/g;
let changed = 0, unlinked = 0, kept = 0;
hub = hub.replace(itemRe, (full, pre, label, h1, href, h2, inner, close) => {
  const m = bestMatch(label);
  const text = inner.replace(/<[^>]+>/g, '').trim();
  if (!m) {
    unlinked++;
    return full.replace(/<a\s[^>]*>[\s\S]*?<\/a>/, `<span class="link-plain">${text}</span>`);
  }
  const target = `/upsc-aso/${m.pillar}/${m.slug}/`;
  if (href !== target) { changed++; } else kept++;
  return full.replace(/href="[^"]*"/, `href="${target}"`);
});
console.log(`bullets -> retargeted: ${changed} | already correct: ${kept} | no confident match (link removed): ${unlinked}`);
// 3) insert "Complete Topic Index" section grouped by pillar (before the tracker/guide section)
const PILLAR_TITLES = {
  'fluid-mechanics-machinery': 'Fluid Mechanics & Machinery',
  'heat-transfer': 'Heat Transfer',
  'aerodynamics-performance-stability': 'Aerodynamics, Performance & Stability',
  'aircraft-structures-materials': 'Aircraft Structures & Materials',
  'propulsion': 'Propulsion',
  'aircraft-systems-instrumentation-maintenance': 'Aircraft Systems, Instrumentation & Maintenance',
  'avionics-navigation-surveillance': 'Avionics, Navigation & Surveillance',
  'atc-aerodromes-flight-planning': 'Air Traffic Control, Aerodromes & Flight Planning',
  'regulations-aviation-safety': 'Aircraft Rules, Regulations & Aviation Safety',
};
let idx = '<section class="hub-section" id="topic-index" aria-labelledby="topic-index-h">\n';
idx += '    <h2 id="topic-index-h">Complete Topic Index (All Subjects)</h2>\n';
idx += '    <p>Every study module of the 100-day ASO plan, grouped by subject. Modules marked \u201cComing Soon\u201d are being prepared.</p>\n';
for (const p of PILLARS) {
  const topics = registry.filter(r => r.pillar === p);
  idx += `    <details class="topic-index-group" ${topics.length ? 'open' : ''}>\n`;
  idx += `      <summary>${PILLAR_TITLES[p] || p} <span class="topic-count">${topics.length} topics</span></summary>\n      <ul class="topic-index-list">\n`;
  for (const t of topics) {
    const soon = fs.existsSync(path.join(BASE, p, t.slug, 'index.html')) &&
      fs.readFileSync(path.join(BASE, p, t.slug, 'index.html'), 'utf8').includes('Coming Soon');
    idx += `        <li><a href="/upsc-aso/${p}/${t.slug}/">${t.title}</a>${soon ? ' <span class="soon-tag">Coming Soon</span>' : ''}</li>\n`;
  }
  idx += '      </ul>\n    </details>\n';
}
idx += '  </section>\n';
// insert before the Progress Tracker section (fallback: before </main>)
let pos = hub.search(/<section[^>]*(?:id="progress-tracker"|class="[^"]*progress)[^>]*>/i);
if (pos < 0) pos = hub.search(/<h2[^>]*>[^<]*Progress Tracker/i);
if (pos < 0) pos = hub.indexOf('</main>');
if (pos < 0) { console.error('NO INSERTION POINT'); process.exit(1); }
hub = hub.slice(0, pos) + idx + '\n' + hub.slice(pos);
fs.writeFileSync(path.join(BASE, 'index.html'), hub, 'utf8');
console.log('hub written. topic-index inserted at char', pos);

// 4) create hub index.html for pillars that lack one
const hubCss = ':root{--glass-bg:rgba(255,255,255,0.96);--glass-border:rgba(255,255,255,0.25);--shadow-lg:0 10px 30px -5px rgba(30,60,114,0.12);--accent-gradient:linear-gradient(135deg,#1e3c72,#2a5298,#d4af37)}.module-container{max-width:1100px;margin:2rem auto;padding:2rem 1.5rem}.breadcrumb-nav{display:flex;align-items:center;gap:.5rem;font-size:.9rem;color:#718096;margin-bottom:1.5rem;flex-wrap:wrap}.breadcrumb-nav a{color:#2b6cb0;text-decoration:none}.breadcrumb-nav a:hover{text-decoration:underline}.pillar-header{background:var(--glass-bg);border:1px solid var(--glass-border);border-radius:1.25rem;padding:2rem;box-shadow:var(--shadow-lg);position:relative;overflow:hidden;margin-bottom:2rem}.pillar-header::before{content:\'\';position:absolute;top:0;left:0;width:5px;height:100%;background:var(--accent-gradient)}.pillar-header h1{font-family:\'Outfit\',sans-serif;font-size:2rem;font-weight:800;color:#1a202c;margin-bottom:.5rem}.pillar-header p{color:#4a5568}.topic-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:1rem}.topic-card{background:var(--glass-bg);border:1px solid var(--glass-border);border-radius:1rem;padding:1.1rem 1.25rem;box-shadow:var(--shadow-lg);transition:transform .15s,box-shadow .15s}.topic-card:hover{transform:translateY(-2px)}.topic-card a{color:#1e3c72;font-weight:600;text-decoration:none}.topic-card a:hover{text-decoration:underline}.soon-tag{display:inline-block;margin-left:.4rem;padding:.1rem .55rem;border-radius:999px;font-size:.7rem;font-weight:700;letter-spacing:.05em;text-transform:uppercase;background:#edf2f7;color:#718096}@media(max-width:640px){.pillar-header h1{font-size:1.5rem}}';
let madeHubs = 0;
for (const p of PILLARS) {
  const hf = path.join(BASE, p, 'index.html');
  if (fs.existsSync(hf)) continue;
  const name = PILLAR_TITLES[p] || p;
  const topics = registry.filter(r => r.pillar === p).map(t => {
    const soon = fs.readFileSync(path.join(BASE, p, t.slug, 'index.html'), 'utf8').includes('Coming Soon');
    return `      <div class="topic-card"><a href="/upsc-aso/${p}/${t.slug}/">${t.title}</a>${soon ? '<span class="soon-tag">Coming Soon</span>' : ''}</div>`;
  }).join('\n');
  const page = `<!DOCTYPE html>\n<html lang="en">\n<head>\n    <meta charset="UTF-8">\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <title>${name} | UPSC Air Safety Officer (ASO) Study Hub</title>\n    <meta name="description" content="All study modules for ${name} in the UPSC Air Safety Officer (DGCA) Recruitment Test preparation — part of the structured 100-day ASO plan on SJ Maths.">\n    <link rel="canonical" href="https://sjmaths.com/upsc-aso/${p}/">\n    <link rel="icon" type="image/png" href="/favicon.png">\n    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Outfit:wght@500;600;700;800&display=swap" rel="stylesheet">\n    <style>${hubCss}</style>\n</head>\n<body>\n<div class="module-container">\n    <nav class="breadcrumb-nav" aria-label="Breadcrumb"><a href="/">Home</a><span>›</span><a href="/upsc-aso/">UPSC ASO Hub</a><span>›</span><span>${name}</span></nav>\n    <header class="pillar-header">\n        <h1>${name}</h1>\n        <p>${topics ? registry.filter(r => r.pillar === p).length : 0} study modules &middot; UPSC Air Safety Officer (DGCA) 100-day preparation plan.</p>\n    </header>\n    <div class="topic-grid">\n${topics || '      <div class="topic-card">Modules coming soon.</div>'}\n    </div>\n    <p style="margin-top:2rem"><a href="/upsc-aso/">← Back to the ASO Preparation Hub</a></p>\n</div>\n</body>\n</html>\n`;
  fs.writeFileSync(hf, page, 'utf8');
  madeHubs++;
}
console.log('pillar hub pages created:', madeHubs);



