// Link all unlinked syllabus-checklist bullets in upsc-aso/index.html to their topic pages.
// Matching strategy: bullet's day number (from checkbox id aso-cb-dNN-mK) -> topics for that day
// in topics_v2.json; token-overlap scoring; global fallback; report unmatched.
const fs = require('fs');
const HUB = 'upsc-aso/index.html';
const DS = 'upsc-aso/topics_v2.json';

let raw = require('./' + DS);
if (!Array.isArray(raw)) raw = raw.topics || raw.TOPICS || Object.values(raw).find(Array.isArray);
const topics = raw.map(t => ({
  day: t.day != null ? Number(t.day) : null,
  pillar: t.subject_slug || t.pillar || t.folder || t.pillar_slug || '',
  slug: t.slug || t.topic_slug || '',
  title: t.title || t.topic || t.name || ''
})).filter(t => t.slug && t.title);

const byDay = new Map();
for (const t of topics) {
  if (t.day == null) continue;
  if (!byDay.has(t.day)) byDay.set(t.day, []);
  byDay.get(t.day).push(t);
}

const STOP = new Set(('a,an,the,and,or,of,in,on,for,to,with,vs,&,at,by,from,as,is,are,its,it,' +
  'basic,basics,fundamentals,concept,concepts,intro,Introduction,practice,revise,revision,test,' +
  'mcq,mcqs,numericals,numerical,problems,questions,full,all,day,days,purpose,law,laws').split(','));
const tok = s => String(s).toLowerCase()
  .replace(/&amp;/g, ' ').replace(/[^a-z0-9]+/g, ' ').trim().split(/\s+/)
  .filter(w => w.length > 2 && !STOP.has(w));
const norm = s => String(s).replace(/&amp;/g, '&').replace(/\s+/g, ' ').trim();

function score(text, t) {
  const a = tok(text), b = new Set(tok(t.title).concat(tok(t.slug.replace(/-/g, ' '))));
  if (!a.length || !b.size) return 0;
  let hit = 0;
  for (const w of a) if (b.has(w)) hit++;
  return hit / a.length;
}

const SKIP_RE = /^(practice|revise|revision|test|analysis|output|tasks?)\b|mcq|numerical|days?\s*\d|error book|formula book|re-?solve|timed/i;

const h0 = fs.readFileSync(HUB, 'utf8');
fs.writeFileSync(HUB + '.prelink.bak', h0);

// Walk each <li> that contains a plain (unlinked) microtopic span.
const liRe = /<li[^>]*>(?:(?!<li[\s>])(?!<\/li>))[\s\S]*?<\/li>/g;
let linked = 0, skipped = 0, unmatched = [];
let html = h0.replace(liRe, li => {
  if (!li.includes('microtopic-plain')) return li;
  const dm = li.match(/aso-cb-d(\d+)-/);
  const day = dm ? Number(dm[1]) : null;
  return li.replace(/<span class="microtopic-link microtopic-plain">([\s\S]*?)<\/span>/g, (m, text) => {
    const label = norm(text);
    if (SKIP_RE.test(label)) { skipped++; return m; }
    const cands = [];
    if (day != null && byDay.has(day)) cands.push(...byDay.get(day).map(t => ({ ...t, s: score(label, t) + 0.25 }))); // day bonus
    for (const t of topics) cands.push({ ...t, s: score(label, t) });
    cands.sort((x, y) => y.s - x.s);
    const best = cands[0];
    if (!best || best.s < 0.5) { unmatched.push(`d${day} :: ${label}`); return m; }
    linked++;
    return `<a href="/upsc-aso/${best.pillar}/${best.slug}/" class="microtopic-link" onclick="event.stopPropagation();">${text}</a>`;
  });
});

fs.writeFileSync(HUB, html);
console.log(`topics in dataset: ${topics.length}`);
console.log(`bullets newly linked: ${linked}`);
console.log(`bullets skipped (practice/revise lines): ${skipped}`);
console.log(`unmatched: ${unmatched.length}`);
unmatched.slice(0, 60).forEach(u => console.log('  UNMATCHED ' + u));
