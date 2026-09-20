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

<style>
:root{--bg:#f5f7fa;--paper:#fff;--ink:#172033;--ink2:#4a5568;--muted:#7a8597;--line:#e2e7ee;--brand:#12324a}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--ink);font-family:Inter,ui-sans-serif,-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Arial,sans-serif;line-height:1.6;-webkit-font-smoothing:antialiased}
a{color:inherit;text-decoration:none}
.wrap{width:min(800px,calc(100% - 32px));margin:auto}
.site-header{height:66px;position:sticky;top:0;z-index:90;background:rgba(255,255,255,.96);backdrop-filter:blur(12px);border-bottom:1px solid var(--line)}
.header-inner{height:100%;display:flex;align-items:center;gap:16px}
.brand{display:flex;gap:11px;align-items:center}
.brand-mark{width:39px;height:39px;border-radius:11px;background:linear-gradient(145deg,#12324a,#1f6a87);display:grid;place-items:center;color:#fff;font-weight:900;font-family:'Times New Roman','Cambria Math',serif;font-size:1.65rem;font-style:italic;line-height:1}
.brand-name{display:block;font-weight:850}
.brand-sub{display:block;color:var(--muted);font-size:.68rem}
.breadcrumbs{padding:16px 0 0;font-size:.82rem;color:var(--muted)}
.breadcrumbs a{text-decoration:underline;text-underline-offset:2px}
.breadcrumbs span{margin:0 6px}
.coming-soon{text-align:center;padding:80px 20px 120px}
.coming-soon .icon{font-size:3rem;margin-bottom:16px}
.coming-soon h1{font-size:clamp(1.4rem,3.5vw,2rem);font-weight:900;margin:0 0 12px;letter-spacing:-.02em}
.coming-soon p{color:var(--ink2);max-width:480px;margin:0 auto 24px;font-size:.98rem}
.back-btn{display:inline-block;padding:12px 28px;background:var(--brand);color:#fff;border-radius:10px;font-weight:700;font-size:.9rem;transition:opacity .15s}
.back-btn:hover{opacity:.85}
footer{padding:32px 0;text-align:center;font-size:.78rem;color:var(--muted);border-top:1px solid var(--line)}
footer a{text-decoration:underline;text-underline-offset:2px}
</style>
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
