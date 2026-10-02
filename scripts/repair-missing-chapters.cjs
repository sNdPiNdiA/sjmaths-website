/**
 * repair-missing-chapters.cjs
 * ─────────────────────────────────────────────────────────────────────
 * Creates lightweight "coming soon" placeholder pages for all chapters
 * linked from subject index pages that don't yet have content.
 *
 * These placeholders are marked noindex so they don't pollute search
 * results, but they resolve the broken-internal-link audit errors.
 *
 * Run:  node scripts/repair-missing-chapters.cjs [--dry-run]
 */
const fs = require('fs');
const path = require('path');
const ROOT = path.resolve(__dirname, '..');

const DRY_RUN = process.argv.includes('--dry-run');

/* Load the audit report to find broken targets */
const reportPath = path.join(ROOT, 'scripts/reports/audit-detail2.json');
if (!fs.existsSync(reportPath)) {
  console.error('❌ Run audit first: node scripts/audit-seo.cjs --output=scripts/reports/audit-detail2.json');
  process.exit(1);
}

const report = JSON.parse(fs.readFileSync(reportPath, 'utf8'));
const brokenLinks = report.issues.filter(i => i.code === 'broken-internal-link');

const slugToTitle = slug =>
  slug.replace(/-/g, ' ').replace(/\b\w/g, c => c.toUpperCase());

function buildBreadcrumbs(route) {
  const parts = route.split('/').filter(Boolean);
  const crumbs = [{ name: 'Home', url: 'https://sjmaths.com/' }];
  let accumulated = '';
  for (let i = 0; i < parts.length; i++) {
    accumulated += '/' + parts[i];
    const name = slugToTitle(parts[i]);
    if (i < parts.length - 1) {
      crumbs.push({ name, url: `https://sjmaths.com${accumulated}/` });
    } else {
      crumbs.push({ name }); // last item, no URL
    }
  }
  return crumbs;
}

function buildPlaceholderPage(route) {
  const parts = route.split('/').filter(Boolean);
  const topicName = slugToTitle(parts[parts.length - 1]);
  const subjectName = slugToTitle(parts[0]);
  const canonicalUrl = `https://sjmaths.com${route}`;
  const breadcrumbs = buildBreadcrumbs(route);

  const bcJson = breadcrumbs.map((b, i) => {
    const item = i < breadcrumbs.length - 1 ? `,"item":"${b.url}"` : '';
    return `{"@type":"ListItem","position":${i + 1},"name":"${b.name}"${item}}`;
  }).join(',');

  const bcHtml = breadcrumbs.map((b, i) => {
    if (i === breadcrumbs.length - 1) return b.name;
    return `<a href="${b.url}">${b.name}</a><span>›</span>`;
  }).join('');

  const title = `${topicName} — ${subjectName} | SJ Maths`;
  const description = `${topicName} study notes for ${subjectName} — detailed content coming soon on SJ Maths.`;

  return `<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>${title}</title>
<meta name="description" content="${description}">
<meta name="robots" content="noindex,follow">
<meta name="author" content="SJ Maths">
<meta name="theme-color" content="#12324a">
<link rel="canonical" href="${canonicalUrl}">

<meta property="og:type" content="website">
<meta property="og:site_name" content="SJ Maths">
<meta property="og:title" content="${title}">
<meta property="og:description" content="${description}">
<meta property="og:url" content="${canonicalUrl}">

<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="${title}">
<meta name="twitter:description" content="${description}">

<script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","name":"${topicName}","url":"${canonicalUrl}","isPartOf":{"@type":"WebSite","name":"SJ Maths","url":"https://sjmaths.com/"},"breadcrumb":{"@type":"BreadcrumbList","itemListElement":[${bcJson}]}}</script>

<link rel="stylesheet" href="/assets/css/coming-soon-page.css">
</head>
<body>

<header class="site-header">
<div class="wrap header-inner">
  <a href="/" class="brand">
    <div class="brand-mark">&int;</div>
    <div><span class="brand-name">SJ Maths</span><span class="brand-sub">Smart Learning</span></div>
  </a>
</div>
</header>

<main class="wrap">
  <nav class="breadcrumbs">${bcHtml}</nav>
  <section class="coming-soon">
    <div class="icon">📝</div>
    <h1>${topicName}</h1>
    <p>We're preparing detailed study notes for this topic. Check back soon for comprehensive content, practice questions and revision material.</p>
    <a href="/${parts[0]}/" class="back-btn">← Back to ${subjectName}</a>
  </section>
</main>

<footer>
  <div class="wrap">© 2024–2026 SJ Maths · <a href="/privacy-policy/">Privacy Policy</a></div>
</footer>

</body>
</html>
`;
}

/* ── create pages ─────────────────────────────────────────────────── */
let created = 0;
let skipped = 0;

// Deduplicate targets
const targets = [...new Set(brokenLinks.map(i => i.detail))].sort();

for (const route of targets) {
  // Convert route to file path: /foo/bar/ -> foo/bar/index.html
  const relPath = route.replace(/^\//, '').replace(/\/$/, '') + '/index.html';
  const absPath = path.join(ROOT, relPath);

  if (fs.existsSync(absPath)) {
    skipped++;
    continue;
  }

  if (DRY_RUN) {
    console.log(`🔍 DRY-RUN: would create ${relPath}`);
  } else {
    fs.mkdirSync(path.dirname(absPath), { recursive: true });
    fs.writeFileSync(absPath, buildPlaceholderPage(route), 'utf8');
  }
  created++;
}

console.log(`\n${DRY_RUN ? 'DRY-RUN' : 'DONE'}: ${created} placeholder pages created, ${skipped} skipped`);
