import fs from 'fs';
import path from 'path';

const dir = 'up-upper-primary-teacher/general-knowledge';
const slugs = fs.readdirSync(dir, { withFileTypes: true })
  .filter(d => d.isDirectory())
  .map(d => d.name);

const topics = [];
const redirectStubs = [];

for (const slug of slugs) {
  const filePath = path.join(dir, slug, 'index.html');
  if (!fs.existsSync(filePath)) {
    console.warn(`File missing for ${slug}`);
    continue;
  }
  const html = fs.readFileSync(filePath, 'utf8');

  // Check if redirect stub
  if (html.includes('refresh') && (html.includes('Redirecting') || html.includes('पुनर्निर्देशित'))) {
    redirectStubs.push(slug);
    continue;
  }

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

  // Extract sample points
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

  const hasTabConcepts = html.includes('id="tab-concepts"');
  const hasTabsStrip = html.includes('class="study-tabs-strip"');

  topics.push({
    slug,
    enTitle,
    hiTitle,
    leadEn,
    leadHi,
    hasTabConcepts,
    hasTabsStrip,
    cardHeadings,
    samplePointsEn: pointsEn.slice(0, 8),
    samplePointsHi: pointsHi.slice(0, 8)
  });
}

console.log(`Total topics in directory: ${slugs.length}`);
console.log(`Active content topics: ${topics.length}`);
console.log(`Redirect stubs: ${redirectStubs.length}`, redirectStubs);

fs.writeFileSync('scripts/gk_topics_catalog.json', JSON.stringify(topics, null, 2), 'utf8');
console.log('Saved scripts/gk_topics_catalog.json');
