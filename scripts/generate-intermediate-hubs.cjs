/**
 * generate-intermediate-hubs.cjs
 * ─────────────────────────────────────────────────────────────────────
 * Creates index.html hub pages for intermediate directories that are
 * linked from existing pages but have no page of their own (they 404).
 *
 * Targets are derived from the newest scripts/reports/audit-*.json:
 * only directories that appear as broken-internal-link targets AND have
 * HTML descendants are generated, so we never inflate the site with
 * unlinked listing pages.
 *
 * Uses the same template/style as scripts/repair-broken-links.cjs.
 * Run:  node scripts/generate-intermediate-hubs.cjs [--dry-run]
 */
const fs = require('fs');
const path = require('path');
const { createResolver } = require('./seo-routes.cjs');
const { siteFiles } = require('./seo-html.cjs');
const ROOT = path.resolve(__dirname, '..');
const DRY_RUN = process.argv.includes('--dry-run');

/* ── locate newest audit report ───────────────────────────────────── */
function newestAuditReport() {
  const dir = path.join(ROOT, 'scripts', 'reports');
  if (!fs.existsSync(dir)) return null;
  const reports = fs.readdirSync(dir)
    .filter(f => /^audit-.*\.json$/.test(f))
    .map(f => ({ name: f, mtime: fs.statSync(path.join(dir, f)).mtimeMs }))
    .sort((a, b) => b.mtime - a.mtime);
  return reports[0]?.name || null;
}

/* ── helpers (same semantics as repair-broken-links.cjs) ──────────── */
const slugToTitle = slug =>
  slug.replace(/-/g, ' ').replace(/\b\w/g, c => c.toUpperCase());

function getSubdirs(dir) {
  const abs = path.join(ROOT, dir);
  if (!fs.existsSync(abs)) return [];
  return fs.readdirSync(abs, { withFileTypes: true })
    .filter(d => d.isDirectory())
    .map(d => d.name)
    .sort();
}

function getChapterCount(dir) {
  const abs = path.join(ROOT, dir);
  if (!fs.existsSync(abs)) return 0;
  let count = 0;
  const walk = d => {
    for (const ent of fs.readdirSync(d, { withFileTypes: true })) {
      if (ent.isFile() && ent.name === 'index.html') count++;
      else if (ent.isDirectory()) walk(path.join(d, ent.name));
    }
  };
  walk(abs);
  return count;
}

function getChildName(childDir, slug) {
  const childIndex = path.join(ROOT, childDir, 'index.html');
  try {
    const src = fs.readFileSync(childIndex, 'utf8');
    const m = src.match(/<title[^>]*>([\s\S]*?)<\/title>/i);
    if (m) {
      let name = m[1].replace(/\s+/g, ' ').trim();
      name = name.split(/\s*[|—:]\s*/)[0].trim();
      if (name) return name;
    }
  } catch { /* fall through to slug title */ }
  return slugToTitle(slug);
}

/* ── page template (same as repair-broken-links.cjs) ──────────────── */
function buildDirectoryPage({ route, title, description, breadcrumbs, children, heroSubtitle, themeColor, lang, h1 }) {
  const pageLang = lang || 'en';
  const canonicalUrl = `https://sjmaths.com${route}`;
  const bc = breadcrumbs.map((b, i) => {
    const item = i < breadcrumbs.length - 1 ? `,"item":"${b.url}"` : '';
    return `{"@type":"ListItem","position":${i + 1},"name":"${b.name}"${item}}`;
  }).join(',');

  const childCards = children.map(c => {
    const chapCount = getChapterCount(c.dir);
    const badge = chapCount > 0 ? `<span class="topic-badge">${chapCount} chapters</span>` : '';
    return `<a href="${c.href}" class="topic-card"><span class="topic-name">${c.name}</span>${badge}</a>`;
  }).join('\n      ');

  return `<!doctype html>
<html lang="${pageLang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>${title}</title>
<meta name="description" content="${description}">
<meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large,max-video-preview:-1">
<meta name="author" content="SJ Maths">
<meta name="theme-color" content="${themeColor || '#12324a'}">
<link rel="canonical" href="${canonicalUrl}">

<meta property="og:type" content="website">
<meta property="og:site_name" content="SJ Maths">
<meta property="og:title" content="${title}">
<meta property="og:description" content="${description}">
<meta property="og:url" content="${canonicalUrl}">
<meta property="og:image" content="https://sjmaths.com/assets/icons/icon-512x512.png">

<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="${title}">
<meta name="twitter:description" content="${description}">
<meta name="twitter:image" content="https://sjmaths.com/assets/icons/icon-512x512.png">

<script type="application/ld+json">{"@context":"https://schema.org","@type":"CollectionPage","name":"${title}","headline":"${title}","description":"${description}","url":"${canonicalUrl}","isPartOf":{"@type":"WebSite","name":"SJ Maths","url":"https://sjmaths.com/"},"breadcrumb":{"@type":"BreadcrumbList","itemListElement":[${bc}]}}</script>

<style>
:root {
  --bg:#f5f7fa; --paper:#fff; --ink:#172033; --ink2:#4a5568; --muted:#7a8597;
  --line:#e2e7ee; --brand:${themeColor || '#12324a'}; --brand2:#1b5875;
  --shadow:0 16px 38px rgba(20,35,50,.07);
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:
  radial-gradient(circle at 95% 0,rgba(37,99,235,.055),transparent 28rem),
  radial-gradient(circle at 0 30rem,rgba(15,118,110,.05),transparent 28rem),
  var(--bg);color:var(--ink);font-family:Inter,ui-sans-serif,-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Arial,sans-serif;line-height:1.5;-webkit-font-smoothing:antialiased}
a{color:inherit;text-decoration:none}
.wrap{width:min(1200px,calc(100% - 32px));margin:auto}

.site-header{height:66px;position:sticky;top:0;z-index:90;background:rgba(255,255,255,.96);backdrop-filter:blur(12px);border-bottom:1px solid var(--line)}
.header-inner{height:100%;display:flex;align-items:center;gap:16px}
.brand{display:flex;gap:11px;align-items:center;text-decoration:none}
.brand-mark{width:39px;height:39px;border-radius:11px;background:linear-gradient(145deg,#12324a,#1f6a87);display:grid;place-items:center;color:#fff;font-weight:900;font-family:'Times New Roman','Cambria Math',serif;font-size:1.65rem;font-style:italic;line-height:1}
.brand-name{display:block;font-weight:850}
.brand-sub{display:block;color:var(--muted);font-size:.68rem}

.hero{padding:48px 0 16px;text-align:center}
.hero h1{font-size:clamp(1.6rem,4vw,2.4rem);font-weight:900;margin:0 0 8px;letter-spacing:-.02em}
.hero p{color:var(--ink2);font-size:1.05rem;max-width:640px;margin:0 auto}

.topics{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:16px;padding:32px 0 64px}
.topic-card{display:flex;align-items:center;justify-content:space-between;padding:18px 22px;background:var(--paper);border:1px solid var(--line);border-radius:14px;transition:all .18s ease;box-shadow:0 2px 6px rgba(0,0,0,.04)}
.topic-card:hover{border-color:var(--brand);box-shadow:var(--shadow);transform:translateY(-2px)}
.topic-name{font-weight:700;font-size:.95rem}
.topic-badge{background:#edf2f7;color:var(--muted);font-size:.72rem;font-weight:700;padding:4px 10px;border-radius:999px;white-space:nowrap}

.breadcrumbs{padding:16px 0 0;font-size:.82rem;color:var(--muted)}
.breadcrumbs a{text-decoration:underline;text-underline-offset:2px}
.breadcrumbs span{margin:0 6px}

footer{padding:32px 0;text-align:center;font-size:.78rem;color:var(--muted);border-top:1px solid var(--line)}
footer a{text-decoration:underline;text-underline-offset:2px}
</style>
</head>
<body>

<header class="site-header">
<div class="wrap header-inner">
  <a href="/" class="brand">
    <div class="brand-mark">S</div>
    <div><span class="brand-name">SJ Maths</span><span class="brand-sub">Smart Learning</span></div>
  </a>
</div>
</header>

<main class="wrap">
  <nav class="breadcrumbs">${breadcrumbs.map((b, i) => {
    if (i === breadcrumbs.length - 1) return b.name;
    return `<a href="${b.url}">${b.name}</a><span>›</span>`;
  }).join('')}</nav>

  <section class="hero">
    <h1>${h1 || title}</h1>
    <p>${heroSubtitle || description}</p>
  </section>

  <section class="topics">
      ${childCards}
  </section>
</main>

<footer>
  <div class="wrap">© 2024–2026 SJ Maths · <a href="/privacy-policy/">Privacy Policy</a></div>
</footer>

</body>
</html>
`;
}

/* ── per-section presentation ─────────────────────────────────────── */
const SECTION_STYLE = {
  commerce: { themeColor: '#0f766e', label: 'Commerce' },
  geography: { themeColor: '#1d7874', label: 'Geography' },
  hindi: { themeColor: '#7f1d1d', label: 'हिंदी', lang: 'hi' },
  sanskrit: { themeColor: '#9a3412', label: 'संस्कृतम्', lang: 'sa' },
  economics: { themeColor: '#1d4ed8', label: 'Economics' },
  civics: { themeColor: '#7c3aed', label: 'Civics' },
  english: { themeColor: '#b45309', label: 'English' },
  'csir-net': { themeColor: '#0e7490', label: 'CSIR NET' },
};

function sectionStyle(dirPath) {
  const first = dirPath.split('/')[0];
  return SECTION_STYLE[first] || { themeColor: '#12324a', label: slugToTitle(first) };
}

/* ── collect linked-but-missing directories ───────────────────────── */
// Scan current pages for internal links that do not resolve, so the set
// reflects today's site (audit reports can lag behind fresh edits).
const resolve = createResolver(siteFiles());
const files = siteFiles().filter(f => f.endsWith('.html'));
const HREF_RE = /\bhref="([^"#]+)"/g;
const JSONLD_URL_RE = /"(?:url|item)":"(https:\/\/sjmaths\.com\/[^"{}]+)"/g;

function collectCandidates() {
  const candidates = new Set();
  const addPath = (pathname) => {
    const clean = decodeURIComponent(pathname.split(/[?#]/)[0]).replace(/^\/+|\/+$/g, '');
    if (!clean || clean.includes('//')) return;
    const abs = path.join(ROOT, clean);
    if (!fs.existsSync(abs) || !fs.statSync(abs).isDirectory()) return;
    if (fs.existsSync(path.join(abs, 'index.html'))) return; // has page now
    if (getChapterCount(clean) === 0) return; // nothing to list
    candidates.add(clean);
  };
  for (const file of files) {
    const src = fs.readFileSync(path.join(ROOT, file), 'utf8');
    for (const match of src.matchAll(HREF_RE)) {
      const href = match[1];
      if (/^(https?:)?\/\//i.test(href) && !/^https:\/\/(?:www\.)?sjmaths\.com\//i.test(href)) continue;
      const result = resolve(href, `https://sjmaths.com/${file}`);
      if (result.external || result.invalid) continue;
      if (result.file && !result.redirect) continue; // resolves fine now
      if (result.loop) continue;
      const pathname = (result.redirect || new URL(href, `https://sjmaths.com/${file}`).pathname);
      if (!pathname.endsWith('/')) continue; // only directory-style targets
      addPath(pathname);
    }
    for (const match of src.matchAll(JSONLD_URL_RE)) {
      const result = resolve(match[1]);
      if (result.external || result.invalid) continue;
      if (result.file && !result.redirect) continue;
      if (result.loop) continue;
      const pathname = result.redirect || new URL(match[1]).pathname;
      if (!pathname.endsWith('/')) continue;
      addPath(pathname);
    }
  }
  return candidates;
}

const candidates = collectCandidates();
const sorted = [...candidates].sort();
console.log(`Scanned ${files.length} pages → ${sorted.length} linked missing hubs to create\n`);

/* ── generate ─────────────────────────────────────────────────────── */
let created = 0;
// Within one run a generic leaf name can repeat across parents
// (e.g. three geography "agriculture" hubs). Qualify the display name
// with the immediate parent whenever the leaf repeats in *this batch*.
const leafCounts = {};
for (const dirPath of sorted) {
  const leaf = dirPath.split('/').pop();
  leafCounts[leaf] = (leafCounts[leaf] || 0) + 1;
}
for (const dirPath of sorted) {
  const segments = dirPath.split('/');
  const style = sectionStyle(dirPath);
  const leafTitle = slugToTitle(segments[segments.length - 1]);
  const name = leafCounts[segments[segments.length - 1]] > 1
    ? `${leafTitle} (${slugToTitle(segments[segments.length - 2])})`
    : leafTitle;

  const breadcrumbs = [{ name: 'Home', url: 'https://sjmaths.com/' }];
  for (let i = 0; i < segments.length - 1; i++) {
    const ancestor = segments.slice(0, i + 1).join('/');
    if (fs.existsSync(path.join(ROOT, ancestor, 'index.html'))) {
      breadcrumbs.push({ name: getChildName(ancestor, segments[i]), url: `https://sjmaths.com/${ancestor}/` });
    }
  }
  breadcrumbs.push({ name });

  const children = getSubdirs(dirPath)
    .filter(d => getChapterCount(`${dirPath}/${d}`) > 0)
    .map(d => ({
      name: getChildName(`${dirPath}/${d}`, d),
      href: `/${dirPath}/${d}/`,
      dir: `${dirPath}/${d}`
    }));

  const title = `${name} — ${style.label} Study Material | SJ Maths`;
  const description = `Free ${style.label.toLowerCase()} study notes on ${name} — chapter-wise topics, revision material and practice questions.`;
  const heroSubtitle = `Explore chapters and topics under ${name}.`;
  const html = buildDirectoryPage({ route: `/${dirPath}/`, title, description, breadcrumbs, children, heroSubtitle, themeColor: style.themeColor, lang: style.lang, h1: name });

  const dest = path.join(ROOT, dirPath, 'index.html');
  if (DRY_RUN) {
    console.log(`🔍 DRY-RUN: would create ${dirPath}/index.html (${children.length} topics)`);
  } else {
    fs.writeFileSync(dest, html, 'utf8');
    console.log(`✅ Created ${dirPath}/index.html (${children.length} topics listed)`);
  }
  created++;
}

console.log(`\n${DRY_RUN ? 'DRY-RUN' : 'DONE'}: ${created} intermediate hubs ${DRY_RUN ? 'planned' : 'created'}`);
process.exitCode = 0;
