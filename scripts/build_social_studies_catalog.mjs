import fs from 'fs';
import path from 'path';

const dir = 'up-upper-primary-teacher/social-studies';
const slugs = fs.readdirSync(dir, { withFileTypes: true })
  .filter(d => d.isDirectory())
  .map(d => d.name);

const topics = [];

for (const slug of slugs) {
  const filePath = path.join(dir, slug, 'index.html');
  if (!fs.existsSync(filePath)) continue;
  const html = fs.readFileSync(filePath, 'utf8');

  // Extract English and Hindi titles independently
  let enTitle = '';
  let hiTitle = '';

  const h1Match = html.match(/<h1[^>]*>([\s\S]*?)<\/h1>/i);
  if (h1Match) {
    const h1Content = h1Match[1];
    const enM = h1Content.match(/<span class="lang-en"[^>]*>([\s\S]*?)<\/span>/i);
    const hiM = h1Content.match(/<span class="lang-hi"[^>]*>([\s\S]*?)<\/span>/i);
    if (enM) enTitle = enM[1].replace(/<[^>]+>/g, '').trim();
    if (hiM) hiTitle = hiM[1].replace(/<[^>]+>/g, '').trim();
  }

  if (!enTitle) {
    const titleMatch = html.match(/<title[^>]*>([\s\S]*?)<\/title>/i);
    if (titleMatch) {
      const parts = titleMatch[1].split('|').map(p => p.trim());
      enTitle = parts[0] || slug;
      if (!hiTitle && parts[1]) hiTitle = parts[1];
    }
  }

  if (!enTitle) enTitle = slug.replace(/-/g, ' ').replace(/\b\w/g, c => c.toUpperCase());
  if (!hiTitle) hiTitle = enTitle;

  // Extract prep card headings
  const cardHeadings = [];
  const cardMatches = [...html.matchAll(/<div class="prep-card">[\s\S]*?<h2>[\s\S]*?<span class="lang-en">([\s\S]*?)<\/span>[\s\S]*?<span class="lang-hi">([\s\S]*?)<\/span>/g)];
  for (const cm of cardMatches) {
    cardHeadings.push({ en: cm[1].trim(), hi: cm[2].trim() });
  }

  // Extract lead description if available
  let leadEn = '';
  let leadHi = '';
  const leadMatch = html.match(/<p class="lead-desc">[\s\S]*?<span class="lang-en">([\s\S]*?)<\/span>[\s\S]*?<span class="lang-hi">([\s\S]*?)<\/span>[\s\S]*?<\/p>/);
  if (leadMatch) {
    leadEn = leadMatch[1].trim();
    leadHi = leadMatch[2].trim();
  }

  // Extract key points from the content
  const pointsEn = [];
  const pointsHi = [];
  const pointCardMatches = [...html.matchAll(/<div class="point-card">([\s\S]*?)<\/div>/g)];
  for (const pm of pointCardMatches) {
    const raw = pm[1].replace(/<[^>]+>/g, ' ').replace(/\s+/g, ' ').trim();
    if (raw.length > 15) {
      if (/[\u0900-\u097F]/.test(raw)) {
        pointsHi.push(raw);
      } else {
        pointsEn.push(raw);
      }
    }
  }

  topics.push({
    slug,
    enTitle,
    hiTitle,
    leadEn,
    leadHi,
    cardHeadings,
    samplePointsEn: pointsEn.slice(0, 10),
    samplePointsHi: pointsHi.slice(0, 10)
  });
}

console.log('Parsed topics count:', topics.length);
fs.writeFileSync('scripts/social_studies_topics_catalog.json', JSON.stringify(topics, null, 2), 'utf8');
console.log('Wrote scripts/social_studies_topics_catalog.json');
