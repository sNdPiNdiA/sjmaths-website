const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');
const { ROOT, setMetadata, parse, compact } = require('../seo-html.cjs');

const BASE = 'up-upper-primary-teacher';
const DOMAIN = 'https://sjmaths.com';
const SECTION_NAMES = {
  english: 'English',
  'general-knowledge': 'General Knowledge',
  mathematics: 'Mathematics',
  science: 'Science',
  'social-studies': 'Social Studies',
  sanskrit: 'Sanskrit',
  hindi: 'Hindi'
};

function cleanText(value) {
  return compact(String(value || '').replace(/\u00a0/g, ' '));
}

function routeFor(file) {
  return `/${file.replace(/\\/g, '/').replace(/\/index\.html$/i, '/')}`;
}

function sectionFor(file) {
  const parts = file.replace(/\\/g, '/').split('/');
  return parts.length > 2 ? (SECTION_NAMES[parts[1]] || parts[1].replace(/-/g, ' ')) : 'UP Teacher Exam';
}

function topicFrom(source, file) {
  const $ = parse(source);
  const h1 = $('h1').first();
  const englishLabel = cleanText(h1.find('.lang-en').first().text());
  let topic = englishLabel || cleanText(h1.text());
  if (file === `${BASE}/index.html`) return 'UP Upper Primary Teacher Syllabus 2026';
  if (topic) {
    const devanagari = topic.search(/[\u0900-\u097f]/u);
    if (devanagari >= 0) topic = topic.slice(0, devanagari).replace(/[|—–:;,\s-]+$/u, '').trim();
  }
  if (!topic) {
    const title = cleanText($('title').first().text());
    topic = title.split(/\s+(?:\||—|–)\s+/u)[0].replace(/\s+(?:Notes|Study Notes|Mindmap|MCQs).*$/iu, '').trim();
  }
  if (!topic) topic = file.replace(/\\/g, '/').replace(/\/index\.html$/i, '').split('/').at(-1).replace(/-/g, ' ').replace(/\b\w/g, letter => letter.toUpperCase());
  return topic;
}

function shorten(text, max) {
  const normalized = cleanText(text);
  if (normalized.length <= max) return normalized;
  const clipped = normalized.slice(0, max + 1);
  const wordEnd = clipped.lastIndexOf(' ');
  return (wordEnd > Math.floor(max * 0.65) ? clipped.slice(0, wordEnd) : clipped.slice(0, max)).replace(/[\s,:;|—–-]+$/u, '');
}

function labelFor(file) {
  const relative = file.replace(/\\/g, '/').replace(`${BASE}/`, '').replace(/\/index\.html$/i, '');
  const parts = relative.split('/');
  if (parts.length === 1) return SECTION_NAMES[parts[0]] || 'UP Teacher';
  const discriminator = parts.length > 2
    ? parts.at(-2).replace(/-/g, ' ')
    : parts.at(-1).split('-').slice(-2).join(' ');
  return `${SECTION_NAMES[parts[0]] || parts[0].replace(/-/g, ' ')} · ${discriminator}`;
}

function rowsFor(files) {
  const rows = files.filter(file => file.startsWith(`${BASE}/`) && /\/index\.html$/i.test(file))
    .map(file => {
      const source = fs.readFileSync(path.join(ROOT, file), 'utf8');
      if (/<meta\b[^>]*http-equiv\s*=\s*["']?refresh\b/i.test(source)) return null;
      const topic = topicFrom(source, file);
      return { file, topic, context: sectionFor(file), route: routeFor(file) };
    }).filter(Boolean);
  const titleCounts = new Map();
  for (const row of rows) {
    const root = row.file === `${BASE}/index.html`;
    const categoryHub = row.file.split('/').length === 3;
    const topic = shorten(row.topic, 78);
    const baseTitle = root
      ? 'UP Upper Primary Teacher Syllabus 2026'
      : categoryHub
        ? `${topic} Syllabus & Notes`
        : topic;
    const title = `${baseTitle} | UP Teacher | SJMaths`;
    titleCounts.set(title, (titleCounts.get(title) || 0) + 1);
    row.title = title;
    row.isHub = root || categoryHub;
  }
  for (const row of rows) {
    row.duplicateTitle = titleCounts.get(row.title) > 1;
    if (row.duplicateTitle) {
      const base = row.title.replace(/\s+\|\s+UP Teacher\s+\|\s+SJMaths$/u, '');
      row.title = `${shorten(base, 58)} · ${shorten(labelFor(row.file), 34)} | UP Teacher | SJMaths`;
    }
    if (row.file === `${BASE}/index.html`) {
      row.description = 'Browse the UP Upper Primary Assistant Teacher syllabus for Classes 6–8, exam pattern and subject-wise study tracker.';
    } else if (row.file.split('/').length === 3) {
      row.description = `Explore ${row.context} notes and topic-wise practice for the UP Upper Primary Teacher exam (Classes 6–8).`;
    } else {
      const topic = shorten(row.topic, 82);
      row.description = `Study ${topic} for the UP Upper Primary Teacher exam with concise notes and practice questions.`;
      if (row.duplicateTitle) row.description = `Review ${shorten(row.topic, 62)} in ${shorten(labelFor(row.file), 42)} for UP Upper Primary Teacher exam practice.`;
    }
    row.description = shorten(row.description, 190);
    row.image = imagePath(row.file);
  }
  const duplicateFinalTitles = new Map();
  for (const row of rows) duplicateFinalTitles.set(row.title, (duplicateFinalTitles.get(row.title) || 0) + 1);
  for (const row of rows) {
    if (duplicateFinalTitles.get(row.title) > 1) {
      const hash = crypto.createHash('sha1').update(row.file).digest('hex').slice(0, 5);
      const base = row.title.replace(/\s+\|\s+UP Teacher\s+\|\s+SJMaths$/u, '');
      row.title = `${shorten(base, 85)} · ${hash} | UP Teacher | SJMaths`;
    }
  }
  const descriptions = new Map();
  for (const row of rows) descriptions.set(row.description, (descriptions.get(row.description) || 0) + 1);
  for (const row of rows) {
    if (descriptions.get(row.description) > 1) {
      row.description = `Review ${shorten(row.topic, 56)} in ${shorten(labelFor(row.file), 34)} for UP Upper Primary Teacher exam practice.`;
    }
  }
  const repeatedDescriptions = new Map();
  for (const row of rows) repeatedDescriptions.set(row.description, (repeatedDescriptions.get(row.description) || 0) + 1);
  for (const row of rows) {
    if (repeatedDescriptions.get(row.description) > 1) {
      const slug = row.file.replace(/\\/g, '/').split('/').at(-2).replace(/-/g, ' ');
      const hash = crypto.createHash('sha1').update(row.file).digest('hex').slice(0, 5);
      row.description = shorten(`Study ${shorten(row.topic, 54)} (${shorten(slug, 30)} ${hash}) for UP Upper Primary Teacher exam practice.`, 170);
    }
  }
  return rows;
}

function imagePath(file) {
  const slug = file.replace(/\\/g, '/').replace(`${BASE}/`, '').replace(/\/index\.html$/i, '') || 'home';
  return `/assets/images/og/up-upper-primary-teacher/${slug.replace(/\//g, '--')}.png`;
}

function applyPage(source, row) {
  const canonical = `${DOMAIN}${row.route}`;
  const image = `${DOMAIN}${row.image}`;
  const imageAlt = `SJMaths ${row.topic} study guide for UP Upper Primary Teacher exam`;
  return setMetadata(source, {
    title: row.title,
    description: row.description,
    canonical,
    'og:title': row.title,
    'og:description': row.description,
    'og:type': row.isHub ? 'website' : 'article',
    'og:url': canonical,
    'og:image': image,
    'og:image:type': 'image/png',
    'og:image:width': '1200',
    'og:image:height': '630',
    'og:image:alt': imageAlt,
    'twitter:card': 'summary_large_image',
    'twitter:title': row.title,
    'twitter:description': row.description,
    'twitter:image': image,
    'twitter:image:alt': imageAlt
  });
}

module.exports = { BASE, ROOT, rowsFor, routeFor, sectionFor, topicFrom, imagePath, applyPage };
