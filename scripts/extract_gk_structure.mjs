import fs from 'node:fs';
import path from 'node:path';

const base = 'up-tgt-pgt-gk';
const mods = ['indian-history', 'general-science', 'geography', 'indian-polity', 'art-culture', 'current-affairs'];

const report = {};

for (const m of mods) {
  const p = path.join(base, m, 'index.html');
  const html = fs.readFileSync(p, 'utf8');
  
  // Find sections
  const secRegex = /<article class="section-card[^"]*" id="([^"]+)"[\s\S]*?<span class="section-title">([^<]+)<\/span>([\s\S]*?)<\/article>/g;
  let sMatch;
  report[m] = [];
  
  while ((sMatch = secRegex.exec(html)) !== null) {
    const sId = sMatch[1];
    const sTitle = sMatch[2].trim();
    const sBody = sMatch[3];
    
    const tRegex = /<div class="topic" data-key="([^"]+)"[\s\S]*?<span class="topic-title">([^<]+)<\/span>/g;
    let tMatch;
    const topics = [];
    while ((tMatch = tRegex.exec(sBody)) !== null) {
      const key = tMatch[1];
      const title = tMatch[2].trim();
      const slug = key.split('/').pop();
      const topicDir = path.join(base, m, slug);
      const exists = fs.existsSync(topicDir);
      topics.push({ key, slug, title, exists });
    }
    report[m].push({ sectionId: sId, sectionTitle: sTitle, topics });
  }
}

for (const [m, sections] of Object.entries(report)) {
  console.log(`\n=== ${m} ===`);
  for (const s of sections) {
    console.log(`  Section: ${s.sectionTitle} (#${s.sectionId}) - ${s.topics.length} topics`);
    for (const t of s.topics) {
      console.log(`    - ${t.title} [slug: ${t.slug}, dir exists: ${t.exists}]`);
    }
  }
}
