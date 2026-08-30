#!/usr/bin/env node
/**
 * generate-weekly-pages.cjs
 *
 * Generates static, crawlable `index.html` pages for every weekly current
 * affairs dataset under `current-affairs/data/weekly/**`. Each generated page:
 *   - has unique title / meta description / canonical URL
 *   - embeds all topic content as static HTML (no JS required to read)
 *   - includes Article + BreadcrumbList + ItemList JSON-LD with real dates
 *   - links to prev/next week, the weekly hub (?period= deep link) and the hub
 *
 * It also maintains two marked blocks inside `current-affairs/weekly/index.html`:
 *   <!--CA_WEEKLY_ARCHIVE_LINKS:START--> ... END  (visible, crawlable archive list)
 *   <!--CA_WEEKLY_ITEMLIST:START--> ... END       (ItemList JSON-LD in <head>)
 *
 * Usage: node current-affairs/generate-weekly-pages.cjs
 */
const fs = require('fs');
const path = require('path');

const CA_ROOT = __dirname;
const DATA_ROOT = path.join(CA_ROOT, 'data');
const WEEKLY_ROOT = path.join(CA_ROOT, 'weekly');
const WEEKLY_INDEX = path.join(WEEKLY_ROOT, 'index.html');
const DOMAIN = 'https://sjmaths.com';
const BASE_URL = `${DOMAIN}/current-affairs/weekly`;

function escapeHtml(value) {
  return String(value == null ? '' : value)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}

function escapeJsonLd(value) {
  return JSON.stringify(value)
    .replace(/</g, '\\u003c')
    .replace(/>/g, '\\u003e')
    .replace(/&/g, '\\u0026');
}

function detailUrl(start) {
  const parts = String(start).split('-');
  return `${BASE_URL}/${parts[0]}/${parts[1]}/${start}/`;
}

function prettyRange(label) {
  return escapeHtml(String(label || '').replace(' - ', '–'));
}

function groupByCategory(topics) {
  const groups = [];
  const index = new Map();
  for (const topic of topics) {
    const category = topic.category || 'General';
    if (!index.has(category)) {
      index.set(category, []);
      groups.push([category, index.get(category)]);
    }
    index.get(category).push(topic);
  }
  return groups;
}

function renderTopic(topic, index) {
  const facts = Array.isArray(topic.facts) ? topic.facts : [];
  const topicId = topic.id || `topic-${index + 1}`;
  return `        <article class="topic" id="${escapeHtml(topicId)}">
          <h2 class="topic-title">${escapeHtml(topic.title)}</h2>
          <p class="topic-meta"><span class="pill">${escapeHtml(topic.category)}</span>${topic.importance ? `<span class="pill pill-imp">${escapeHtml(topic.importance)} importance</span>` : ''}<span class="topic-date">${escapeHtml(topic.date || '')}</span></p>
          ${facts.length ? `<div class="facts"><h3>Key Facts &amp; Highlights</h3><ul>${facts.map((f) => `<li>${escapeHtml(f)}</li>`).join('')}</ul></div>` : ''}
          ${topic.detail ? `<p class="detail">${escapeHtml(topic.detail)}</p>` : ''}
          ${topic.exam ? `<p class="exam"><strong>Exam angle:</strong> ${escapeHtml(topic.exam)}</p>` : ''}
          ${topic.remember ? `<p class="remember"><strong>Remember:</strong> ${escapeHtml(topic.remember)}</p>` : ''}
        </article>`;
}

function renderPage(week, prevWeek, nextWeek) {
  const data = week.data;
  const url = detailUrl(data.start);
  const range = prettyRange(data.label);
  const rangeTitle = escapeHtml(data.label || '');
  const title = `Weekly Current Affairs ${rangeTitle} | Notes &amp; MCQs | SJMaths`;
  const topicCount = data.topics.length;
  const description = `${topicCount} exam-ready current affairs topics for ${rangeTitle} — key facts, details, exam angles and revision points for SSC, Banking, Railway, UPSC and State PCS exams.`;
  const hubLink = `${DOMAIN}/current-affairs/weekly/?period=${encodeURIComponent(data.start)}`;
  const published = data.end || data.start;
  const categories = groupByCategory(data.topics);

  const articleLd = {
    '@context': 'https://schema.org',
    '@type': 'Article',
    '@id': `${url}#article`,
    headline: `Weekly Current Affairs ${data.label || data.start}`,
    description,
    inLanguage: 'en',
    datePublished: published,
    dateModified: published,
    mainEntityOfPage: url,
    author: { '@type': 'Organization', name: 'SJMaths', url: `${DOMAIN}/` },
    publisher: {
      '@type': 'Organization',
      name: 'SJMaths',
      url: `${DOMAIN}/`,
      logo: { '@type': 'ImageObject', url: `${DOMAIN}/assets/icons/icon-512x512.png` },
    },
    isPartOf: { '@type': 'WebSite', name: 'SJMaths', url: `${DOMAIN}/` },
  };

  const breadcrumbLd = {
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    itemListElement: [
      { '@type': 'ListItem', position: 1, name: 'Home', item: `${DOMAIN}/` },
      { '@type': 'ListItem', position: 2, name: 'Current Affairs', item: `${DOMAIN}/current-affairs/` },
      { '@type': 'ListItem', position: 3, name: 'Weekly', item: `${DOMAIN}/current-affairs/weekly/` },
      { '@type': 'ListItem', position: 4, name: `Weekly Current Affairs ${data.label || data.start}`, item: url },
    ],
  };

  const itemListLd = {
    '@context': 'https://schema.org',
    '@type': 'ItemList',
    name: `Weekly Current Affairs Topics — ${data.label || data.start}`,
    numberOfItems: topicCount,
    itemListElement: data.topics.map((t, i) => ({
      '@type': 'ListItem',
      position: i + 1,
      name: t.title,
      url: `${url}#${escapeHtml(t.id || `topic-${i + 1}`)}`,
    })),
  };

  const nav = [];
  nav.push(prevWeek
    ? `<a class="nav-link" href="${escapeHtml(detailUrl(prevWeek.data.start))}">&larr; ${escapeHtml(prevWeek.data.label)}</a>`
    : '<span></span>');
  nav.push(`<a class="nav-link nav-hub" href="${escapeHtml(hubLink)}">Practice this week &rarr;</a>`);
  nav.push(nextWeek
    ? `<a class="nav-link" href="${escapeHtml(detailUrl(nextWeek.data.start))}">${escapeHtml(nextWeek.data.label)} &rarr;</a>`
    : '<span></span>');


  return `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>${title}</title>
  <meta name="description" content="${escapeHtml(description)}">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <link rel="canonical" href="${url}">
  <link rel="icon" type="image/png" href="/favicon.png">
  <meta name="theme-color" content="#e11d48">
  <meta property="og:type" content="article">
  <meta property="og:title" content="${title}">
  <meta property="og:description" content="${escapeHtml(description)}">
  <meta property="og:url" content="${url}">
  <meta property="og:image" content="${DOMAIN}/assets/icons/icon-512x512.png">
  <meta property="article:published_time" content="${published}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="${title}">
  <meta name="twitter:description" content="${escapeHtml(description)}">
  <meta name="twitter:image" content="${DOMAIN}/assets/icons/icon-512x512.png">
  <script type="application/ld+json">${escapeJsonLd(articleLd)}</script>
  <script type="application/ld+json">${escapeJsonLd(breadcrumbLd)}</script>
  <script type="application/ld+json">${escapeJsonLd(itemListLd)}</script>
  <style>
    :root { --primary:#e11d48; --ink:#0f172a; --muted:#64748b; --line:#e2e8f0; --bg:#f8fafc; }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: 'Inter', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif; color: var(--ink); background: var(--bg); line-height: 1.65; }
    .wrap { max-width: 860px; margin: 0 auto; padding: 1.5rem 1.25rem 3rem; }
    header.hero { background: linear-gradient(135deg, #e11d48 0%, #ea580c 100%); color: #fff; padding: 2.25rem 1.25rem; }
    header.hero .wrap { padding: 0; }
    h1 { font-size: clamp(1.6rem, 4vw, 2.2rem); font-weight: 800; line-height: 1.25; }
    .hero p { margin-top: .5rem; opacity: .92; max-width: 640px; }
    .week-nav { display: flex; justify-content: space-between; gap: .75rem; flex-wrap: wrap; margin: 1.25rem 0 2rem; }
    .nav-link { display: inline-block; padding: .5rem .9rem; border: 1px solid var(--line); border-radius: 10px; background: #fff; color: var(--ink); text-decoration: none; font-size: .9rem; font-weight: 600; }
    .nav-link:hover { border-color: var(--primary); color: var(--primary); }
    .nav-hub { background: var(--primary); border-color: var(--primary); color: #fff; }
    .cat-section { margin: 2rem 0; }
    .cat-title { font-size: 1.15rem; font-weight: 800; color: var(--primary); border-bottom: 2px solid var(--line); padding-bottom: .4rem; margin-bottom: 1rem; }
    .topic { background: #fff; border: 1px solid var(--line); border-radius: 14px; padding: 1.25rem 1.35rem; margin-bottom: 1rem; box-shadow: 0 4px 12px rgba(15, 23, 42, .05); }
    .topic-title { font-size: 1.15rem; font-weight: 700; margin-bottom: .5rem; }
    .topic-meta { display: flex; gap: .5rem; align-items: center; flex-wrap: wrap; font-size: .82rem; color: var(--muted); margin-bottom: .75rem; }
    .pill { background: #fff1f2; color: #be123c; border-radius: 999px; padding: .15rem .7rem; font-weight: 600; }
    .pill-imp { background: #fef3c7; color: #92400e; }
    .facts h3 { font-size: .95rem; margin-bottom: .4rem; color: #0f766e; }
    .facts ul { padding-left: 1.2rem; margin-bottom: .75rem; }
    .facts li { margin-bottom: .3rem; }
    .detail { margin-bottom: .6rem; }
    .exam, .remember { font-size: .95rem; background: var(--bg); border-left: 3px solid var(--primary); padding: .5rem .8rem; border-radius: 0 8px 8px 0; margin-top: .5rem; }
    .remember { border-left-color: #0f766e; }
    .cta { background: #fff; border: 1px solid var(--line); border-radius: 14px; padding: 1.25rem 1.35rem; margin-top: 2rem; }
    .cta h2 { font-size: 1.1rem; margin-bottom: .4rem; }
    .cta p { color: var(--muted); font-size: .95rem; }
    .cta a { color: var(--primary); font-weight: 600; }
    footer { margin-top: 2rem; font-size: .8rem; color: var(--muted); text-align: center; }
    footer a { color: var(--primary); }
  </style>
</head>
<body>
  <header class="hero">
    <div class="wrap">
      <nav class="crumbs" style="color:rgba(255,255,255,.85); font-size:.85rem;"><a style="color:#fff" href="/">Home</a> › <a style="color:#fff" href="/current-affairs/">Current Affairs</a> › <a style="color:#fff" href="/current-affairs/weekly/">Weekly</a> › ${range}</nav>
      <h1>Weekly Current Affairs: ${range}</h1>
      <p>${topicCount} curated, exam-ready current affairs topics with key facts, exam angles and revision points for SSC, Banking, Railway, UPSC, UPPSC and other competitive exams.</p>
    </div>
  </header>
  <div class="wrap">
    <nav class="week-nav" aria-label="Week navigation">
      ${nav.join('\n      ')}
    </nav>
${categories.map(([category, items]) => `    <section class="cat-section" id="${escapeHtml(String(category).toLowerCase().replace(/[^a-z0-9]+/g, '-'))}">
      <h2 class="cat-title">${escapeHtml(category)}</h2>
${items.map((t) => renderTopic(t, data.topics.indexOf(t))).join('\n')}
    </section>`).join('\n')}
    <div class="cta">
      <h2>Practice this week's current affairs</h2>
      <p>Revise these topics with MCQs, one-liners, audio summaries and a live mock in the interactive weekly dashboard: <a href="${escapeHtml(hubLink)}">open the ${range} practice set</a>. Browse all sets in the <a href="/current-affairs/weekly/">weekly current affairs index</a> or visit the <a href="/current-affairs/">Current Affairs Hub</a>.</p>
    </div>
    <footer>${escapeHtml(data.sourceNote || 'Weekly Current Affairs Compilation by sjmaths.com')} &bull; <a href="${DOMAIN}/">SJMaths</a></footer>
  </div>
</body>
</html>
`;
}


function collectDataFiles() {
  const manifestPath = path.join(DATA_ROOT, 'manifest.json');
  let relPaths = [];

  if (fs.existsSync(manifestPath)) {
    try {
      const manifest = JSON.parse(fs.readFileSync(manifestPath, 'utf8'));
      relPaths = (manifest.weekly || []).map((p) => p.replace(/^weekly\//, ''));
    } catch (error) {
      console.warn(`Could not parse manifest.json (${error.message}); falling back to directory scan.`);
    }
  }

  if (!relPaths.length) {
    const scan = (dir) => {
      for (const dirent of fs.readdirSync(dir, { withFileTypes: true })) {
        const full = path.join(dir, dirent.name);
        if (dirent.isDirectory()) scan(full);
        else if (dirent.isFile() && dirent.name.endsWith('.json')) {
          relPaths.push(path.relative(path.join(DATA_ROOT, 'weekly'), full).split(path.sep).join('/'));
        }
      }
    };
    scan(path.join(DATA_ROOT, 'weekly'));
  }

  const seen = new Set();
  const weeks = [];
  for (const rel of relPaths) {
    const full = path.join(DATA_ROOT, 'weekly', rel);
    if (!fs.existsSync(full)) {
      console.warn(`Skipping missing data file: ${rel}`);
      continue;
    }
    let data;
    try {
      data = JSON.parse(fs.readFileSync(full, 'utf8'));
    } catch (error) {
      console.warn(`Skipping unparseable data file ${rel}: ${error.message}`);
      continue;
    }
    if (!data || !data.start || !Array.isArray(data.topics) || data.topics.length === 0) continue;
    if (seen.has(data.start)) continue;
    seen.add(data.start);
    weeks.push({ rel, data });
  }

  weeks.sort((a, b) => a.data.start.localeCompare(b.data.start));
  return weeks;
}

function upsertMarkerBlock(html, startMarker, endMarker, block, anchor) {
  const startIdx = html.indexOf(startMarker);
  if (startIdx >= 0) {
    const endIdx = html.indexOf(endMarker, startIdx);
    if (endIdx < 0) throw new Error(`Found ${startMarker} but not ${endMarker}`);
    return html.slice(0, startIdx) + block + html.slice(endIdx + endMarker.length);
  }
  const anchorIdx = html.indexOf(anchor);
  if (anchorIdx < 0) throw new Error(`Anchor not found in weekly/index.html: ${anchor.slice(0, 60)}...`);
  const insertAt = anchorIdx + anchor.length;
  return html.slice(0, insertAt) + '\n\n' + block + html.slice(insertAt);
}


function updateWeeklyIndex(weeks) {
  let html = fs.readFileSync(WEEKLY_INDEX, 'utf8');

  const archiveItems = weeks
    .map(({ data }) => `        <li><a href="${escapeHtml(detailUrl(data.start))}">Weekly Current Affairs ${escapeHtml(data.label || data.start)}</a> <span>(${data.topics.length} topics)</span></li>`)
    .join('\n');

  const archiveBlock = `<!--CA_WEEKLY_ARCHIVE_LINKS:START-->
      <section class="ca-weekly-archive" aria-labelledby="weeklyArchiveTitle" style="margin:2rem 0; padding:1.25rem 1.35rem; background:#fff; border:1px solid var(--ca-line, #e2e8f0); border-radius:14px;">
        <h2 id="weeklyArchiveTitle" style="font-size:1.1rem; margin-bottom:.6rem;">Weekly Current Affairs Archive</h2>
        <p style="font-size:.9rem; color:var(--ca-muted, #64748b); margin-bottom:.75rem;">Static, print-ready weekly compilations — ideal for quick reading and revision.</p>
        <ul style="padding-left:1.2rem; font-size:.95rem; line-height:1.9;">
${archiveItems}
        </ul>
      </section>
      <!--CA_WEEKLY_ARCHIVE_LINKS:END-->`;

  const itemListLd = {
    '@context': 'https://schema.org',
    '@type': 'ItemList',
    name: 'Weekly Current Affairs Archives',
    itemListElement: weeks.map(({ data }, i) => ({
      '@type': 'ListItem',
      position: i + 1,
      name: `Weekly Current Affairs ${data.label || data.start}`,
      url: detailUrl(data.start),
    })),
  };

  const itemListBlock = `<!--CA_WEEKLY_ITEMLIST:START-->
  <script type="application/ld+json">${escapeJsonLd(itemListLd)}</script>
  <!--CA_WEEKLY_ITEMLIST:END-->`;

  html = upsertMarkerBlock(
    html,
    '<!--CA_WEEKLY_ARCHIVE_LINKS:START-->',
    '<!--CA_WEEKLY_ARCHIVE_LINKS:END-->',
    archiveBlock,
    '<section class="selector-grid" id="periodSelector" aria-label="Select weekly date range"></section>'
  );

  html = upsertMarkerBlock(
    html,
    '<!--CA_WEEKLY_ITEMLIST:START-->',
    '<!--CA_WEEKLY_ITEMLIST:END-->',
    itemListBlock,
    '<link rel="icon" type="image/png" href="/favicon.png">'
  );

  fs.writeFileSync(WEEKLY_INDEX, html, 'utf8');
}

function main() {
  const weeks = collectDataFiles();
  if (!weeks.length) {
    console.error('No weekly datasets found — nothing generated.');
    process.exit(1);
  }

  let created = 0;
  let updated = 0;
  weeks.forEach((week, i) => {
    const data = week.data;
    const parts = String(data.start).split('-');
    const outDir = path.join(WEEKLY_ROOT, parts[0], parts[1], data.start);
    const outFile = path.join(outDir, 'index.html');
    const html = renderPage(week, weeks[i - 1] || null, weeks[i + 1] || null);

    if (fs.existsSync(outFile)) updated++;
    else created++;
    fs.mkdirSync(outDir, { recursive: true });
    fs.writeFileSync(outFile, html, 'utf8');
  });

  updateWeeklyIndex(weeks);

  console.log(`Generated ${created} new and updated ${updated} existing weekly pages (total ${weeks.length}).`);
  console.log('Updated current-affairs/weekly/index.html (archive links + ItemList JSON-LD).');
  console.log('Next step: run `npm run generate:sitemaps` to publish the new URLs.');
}

main();

