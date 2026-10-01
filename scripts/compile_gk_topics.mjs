import fs from 'node:fs';
import path from 'node:path';

const base = 'up-tgt-pgt-gk';
const mods = [
  { id: 'indian-history', title: 'Indian History', icon: '🏛️', color: '#c2410c', bg: '#fff7ed', meta: '20 Topics' },
  { id: 'general-science', title: 'General Science', icon: '🔬', color: '#2563eb', bg: '#eff6ff', meta: '16 Topics' },
  { id: 'indian-polity', title: 'Indian Polity & Constitution', icon: '⚖️', color: '#15803d', bg: '#f0fdf4', meta: '12 Topics' },
  { id: 'geography', title: 'Geography of India & UP', icon: '🌍', color: '#0e7490', bg: '#ecfeff', meta: '10 Topics' },
  { id: 'art-culture', title: 'Art, Culture & Heritage', icon: '🎨', color: '#be123c', bg: '#fff1f2', meta: '10 Topics' },
  { id: 'current-affairs', title: 'Current Affairs 2026', icon: '📰', color: '#a21caf', bg: '#fdf4ff', meta: '9 Topics' }
];

const fullData = [];

for (const mod of mods) {
  const p = path.join(base, mod.id, 'index.html');
  const html = fs.readFileSync(p, 'utf8');

  const secRegex = /<article class="section-card[^"]*" id="([^"]+)"[\s\S]*?<span class="section-title">([^<]+)<\/span>([\s\S]*?)<\/article>/g;
  let sMatch;
  const sections = [];

  while ((sMatch = secRegex.exec(html)) !== null) {
    const sId = sMatch[1];
    const sTitle = sMatch[2].trim();
    const sBody = sMatch[3];

    const tRegex = /<div class="topic" data-key="([^"]+)"[\s\S]*?<span class="topic-title">([^<]+)<\/span>[\s\S]*?<span class="topic-desc">([^<]+)<\/span>/g;
    let tMatch;
    const topics = [];
    while ((tMatch = tRegex.exec(sBody)) !== null) {
      const key = tMatch[1];
      const title = tMatch[2].trim();
      const desc = tMatch[3].trim();
      const slug = key.split('/').pop();
      const topicDir = path.join(base, mod.id, slug);
      const exists = fs.existsSync(path.join(topicDir, 'index.html'));
      const url = exists 
        ? `/up-tgt-pgt-gk/${mod.id}/${slug}/` 
        : `/up-tgt-pgt-gk/${mod.id}/#${sId}`;

      topics.push({ slug, title, desc, url, exists });
    }
    sections.push({ sectionId: sId, sectionTitle: sTitle, topics });
  }

  fullData.push({ ...mod, sections });
}

fs.writeFileSync('scripts/gk_full_data.json', JSON.stringify(fullData, null, 2), 'utf8');
console.log('Successfully written scripts/gk_full_data.json');
let totalTopics = 0;
fullData.forEach(m => {
  const count = m.sections.reduce((acc, s) => acc + s.topics.length, 0);
  totalTopics += count;
  console.log(`${m.title}: ${count} topics across ${m.sections.length} sections`);
});
console.log(`Total: ${totalTopics} topics across all modules.`);
