/**
 * repair-broken-links.cjs
 * ─────────────────────────────────────────────────────────────────────
 * Fixes broken-internal-link errors by creating missing index.html
 * pages for subject root directories (chemistry, agriculture,
 * home-science, art, art/subtopics) and a privacy-policy page.
 *
 * Each generated page follows the existing site template pattern with
 * proper SEO markup (title, meta description, canonical, og tags,
 * twitter card, JSON-LD, breadcrumbs).
 *
 * Run:  node scripts/repair-broken-links.cjs [--dry-run]
 */
const fs = require('fs');
const path = require('path');
const ROOT = path.resolve(__dirname, '..');

const DRY_RUN = process.argv.includes('--dry-run');

/* ── helpers ──────────────────────────────────────────────────────── */
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

/* ── page template ────────────────────────────────────────────────── */
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
    <div class="brand-mark">&int;</div>
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

/* ── privacy policy page ──────────────────────────────────────────── */
function buildPrivacyPage() {
  return `<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Privacy Policy | SJ Maths</title>
<meta name="description" content="Privacy policy for SJ Maths — how we collect, use and protect your data when you use our free educational platform.">
<meta name="robots" content="noindex,follow">
<meta name="author" content="SJ Maths">
<meta name="theme-color" content="#12324a">
<link rel="canonical" href="https://sjmaths.com/privacy-policy/">

<meta property="og:type" content="website">
<meta property="og:site_name" content="SJ Maths">
<meta property="og:title" content="Privacy Policy | SJ Maths">
<meta property="og:description" content="Privacy policy for SJ Maths — how we collect, use and protect your data.">
<meta property="og:url" content="https://sjmaths.com/privacy-policy/">

<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="Privacy Policy | SJ Maths">
<meta name="twitter:description" content="Privacy policy for SJ Maths.">

<script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","name":"Privacy Policy","url":"https://sjmaths.com/privacy-policy/","isPartOf":{"@type":"WebSite","name":"SJ Maths","url":"https://sjmaths.com/"},"breadcrumb":{"@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://sjmaths.com/"},{"@type":"ListItem","position":2,"name":"Privacy Policy"}]}}</script>

<style>
:root{--bg:#f5f7fa;--paper:#fff;--ink:#172033;--ink2:#4a5568;--muted:#7a8597;--line:#e2e7ee;--brand:#12324a}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--ink);font-family:Inter,ui-sans-serif,-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Arial,sans-serif;line-height:1.7;-webkit-font-smoothing:antialiased}
a{color:var(--brand)}
.wrap{width:min(780px,calc(100% - 32px));margin:auto}
.site-header{height:66px;position:sticky;top:0;z-index:90;background:rgba(255,255,255,.96);backdrop-filter:blur(12px);border-bottom:1px solid var(--line)}
.header-inner{height:100%;display:flex;align-items:center;gap:16px}
.brand{display:flex;gap:11px;align-items:center;text-decoration:none;color:inherit}
.brand-mark{width:39px;height:39px;border-radius:11px;background:linear-gradient(145deg,#12324a,#1f6a87);display:grid;place-items:center;color:#fff;font-weight:900;font-family:'Times New Roman','Cambria Math',serif;font-size:1.65rem;font-style:italic;line-height:1}
.brand-name{display:block;font-weight:850}
.brand-sub{display:block;color:var(--muted);font-size:.68rem}
article{background:var(--paper);border:1px solid var(--line);border-radius:18px;padding:48px 40px;margin:32px 0 64px;box-shadow:0 8px 24px rgba(20,35,50,.06)}
article h1{font-size:1.8rem;font-weight:900;margin:0 0 8px;letter-spacing:-.02em}
article h2{font-size:1.15rem;font-weight:800;margin:32px 0 8px;color:var(--brand)}
article p,article li{color:var(--ink2);font-size:.95rem}
article ul{padding-left:20px}
.updated{color:var(--muted);font-size:.82rem;margin-bottom:24px}
footer{padding:32px 0;text-align:center;font-size:.78rem;color:var(--muted);border-top:1px solid var(--line)}
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
<article>
  <h1>Privacy Policy</h1>
  <p class="updated">Last updated: September 2026</p>

  <p>SJ Maths ("we", "us", or "our") operates the website <strong>sjmaths.com</strong>. This page explains what information we collect, how we use it, and your rights.</p>

  <h2>Information We Collect</h2>
  <p>We are a free educational platform. We collect minimal information:</p>
  <ul>
    <li><strong>Usage data:</strong> Pages visited, time spent, browser type and device information — collected automatically via analytics tools.</li>
    <li><strong>Local storage:</strong> Your study progress and preferences are stored locally in your browser and are never sent to our servers.</li>
  </ul>

  <h2>Cookies &amp; Analytics</h2>
  <p>We may use cookies and third-party analytics services (such as Google Analytics) to understand how visitors use our site. These tools may collect anonymised data about your browsing behaviour. You can control cookie preferences through your browser settings.</p>

  <h2>How We Use Information</h2>
  <ul>
    <li>To improve our educational content and user experience.</li>
    <li>To understand which topics are most popular.</li>
    <li>To maintain and operate the website.</li>
  </ul>

  <h2>Third-Party Services</h2>
  <p>Our site may use third-party services for hosting (Cloudflare), analytics, and content delivery. These services have their own privacy policies. We do not sell or share your personal data with third parties for marketing purposes.</p>

  <h2>Children's Privacy</h2>
  <p>Our educational content is designed for students of all ages. We do not knowingly collect personal information from children. If you believe a child has provided us with personal data, please contact us so we can delete it.</p>

  <h2>Your Rights</h2>
  <p>You may request access to, correction of, or deletion of any personal data we hold. Since we store minimal data, in most cases there is nothing to delete beyond clearing your browser's local storage.</p>

  <h2>Changes to This Policy</h2>
  <p>We may update this privacy policy from time to time. Any changes will be posted on this page with an updated revision date.</p>

  <h2>Contact</h2>
  <p>If you have questions about this privacy policy, please reach out to us through the contact information available on our website.</p>
</article>
</main>

<footer>
  <div class="wrap">© 2024–2026 SJ Maths</div>
</footer>

</body>
</html>
`;
}

/* ── subject configurations ───────────────────────────────────────── */
// Prefer the real <title> of each child's own page; fall back to slug casing.
// Titles like "Topic Name — Detail | SJ Maths" reduce to "Topic Name".
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

const subjects = [
  {
    dir: 'chemistry',
    route: '/chemistry/',
    title: 'Chemistry Study Material | SJ Maths',
    description: 'Free chemistry study notes covering Physical, Inorganic and Organic Chemistry — topic-wise chapters, quizzes and revision material.',
    heroSubtitle: 'Explore our comprehensive chemistry study material organised by topic.',
    breadcrumbs: [
      { name: 'Home', url: 'https://sjmaths.com/' },
      { name: 'Chemistry' }
    ],
    themeColor: '#1a5276'
  },
  {
    dir: 'agriculture',
    route: '/agriculture/',
    title: 'Agriculture Study Material | SJ Maths',
    description: 'Free agriculture study notes — Agronomy, Horticulture, Soil Science, Plant Protection and more with topic-wise chapters.',
    heroSubtitle: 'Browse agriculture topics with detailed notes and practice material.',
    breadcrumbs: [
      { name: 'Home', url: 'https://sjmaths.com/' },
      { name: 'Agriculture' }
    ],
    themeColor: '#1e7e34'
  },
  {
    dir: 'home-science',
    route: '/home-science/',
    title: 'Home Science Study Material | SJ Maths',
    description: 'Free home science study notes — Human Development, Nutrition, Textiles, Family Resource Management and more.',
    heroSubtitle: 'Comprehensive home science notes organised by topic for exam preparation.',
    breadcrumbs: [
      { name: 'Home', url: 'https://sjmaths.com/' },
      { name: 'Home Science' }
    ],
    themeColor: '#b7791f'
  },
  {
    dir: 'art',
    route: '/art/',
    title: 'Art Study Material | SJ Maths',
    description: 'Free art study notes — Indian Painting, Western Art, Art History, Drawing, Composition and Aesthetics with topic-wise chapters.',
    heroSubtitle: 'Explore art history, painting traditions and creative techniques.',
    breadcrumbs: [
      { name: 'Home', url: 'https://sjmaths.com/' },
      { name: 'Art' }
    ],
    themeColor: '#8b5cf6'
  },
  {
    dir: 'commerce',
    route: '/commerce/',
    title: 'Commerce Study Material | SJ Maths',
    description: 'Free commerce study notes — Accounting, Business Economics, Cost & Management Accounting, Taxation, Statistics, Trade and more.',
    heroSubtitle: 'Explore commerce chapters with detailed notes and practice material.',
    breadcrumbs: [
      { name: 'Home', url: 'https://sjmaths.com/' },
      { name: 'Commerce' }
    ],
    themeColor: '#0f766e'
  },
  {
    dir: 'geography',
    route: '/geography/',
    title: 'Geography Study Material | SJ Maths',
    description: 'Free geography study notes — Cartography, Physical Geography, Human Geography, Economic Geography and more.',
    heroSubtitle: 'Explore geography chapters with detailed notes and practice material.',
    breadcrumbs: [
      { name: 'Home', url: 'https://sjmaths.com/' },
      { name: 'Geography' }
    ],
    themeColor: '#1d7874'
  },
  {
    dir: 'hindi/bhashavigyan',
    route: '/hindi/bhashavigyan/',
    lang: 'hi',
    title: 'हिंदी भाषाविज्ञान — अध्ययन नोट्स | UP PGT/TGT हिंदी | SJ Maths',
    h1: 'हिंदी भाषाविज्ञान',
    description: 'हिंदी भाषाविज्ञान के सभी अध्याय — भाषाएँ, ध्वनियाँ, देवनागरी लिपि, विभाषाएँ, उपभाषाएँ, त्रुटियाँ एवं विकास विशेषताएँ, विगत प्रश्न (PYQ) सहित।',
    heroSubtitle: 'भाषाविज्ञान के अध्यायों के विस्तृत नोट्स, अभ्यास प्रश्न एवं टेस्ट।',
    breadcrumbs: [
      { name: 'Home', url: 'https://sjmaths.com/' },
      { name: 'हिंदी', url: 'https://sjmaths.com/hindi/' },
      { name: 'भाषाविज्ञान' }
    ],
    themeColor: '#7f1d1d'
  },
  {
    dir: 'hindi/kavyashastra',
    route: '/hindi/kavyashastra/',
    lang: 'hi',
    title: 'हिंदी काव्यशास्त्र — अध्ययन नोट्स | UP PGT/TGT हिंदी | SJ Maths',
    h1: 'हिंदी काव्यशास्त्र',
    description: 'काव्यशास्त्र के सभी अध्याय — रस, अलंकार, छंद, वाक्योक्ति, रीति, ध्वनि एवं काव्य के स्वरूप, विगत प्रश्न (PYQ) सहित।',
    heroSubtitle: 'काव्यशास्त्र के अध्यायों के विस्तृत नोट्स, अभ्यास प्रश्न एवं टेस्ट।',
    breadcrumbs: [
      { name: 'Home', url: 'https://sjmaths.com/' },
      { name: 'हिंदी', url: 'https://sjmaths.com/hindi/' },
      { name: 'काव्यशास्त्र' }
    ],
    themeColor: '#7f1d1d'
  },
  {
    dir: 'hindi/patrakarita',
    route: '/hindi/patrakarita/',
    lang: 'hi',
    title: 'हिंदी पत्रकारिता — अध्ययन नोट्स | UP PGT/TGT हिंदी | SJ Maths',
    h1: 'हिंदी पत्रकारिता',
    description: 'पत्रकारिता के सभी अध्याय — पत्रकारिता की परिभाषा, इतिहास, प्रकार, संपादकीय कौशल एवं विगत प्रश्न (PYQ) सहित।',
    heroSubtitle: 'पत्रकारिता के अध्यायों के विस्तृत नोट्स, अभ्यास प्रश्न एवं टेस्ट।',
    breadcrumbs: [
      { name: 'Home', url: 'https://sjmaths.com/' },
      { name: 'हिंदी', url: 'https://sjmaths.com/hindi/' },
      { name: 'पत्रकारिता' }
    ],
    themeColor: '#7f1d1d'
  },
  {
    dir: 'hindi/sahitya-itihas',
    route: '/hindi/sahitya-itihas/',
    lang: 'hi',
    title: 'हिंदी साहित्य का इतिहास — अध्ययन नोट्स | UP PGT/TGT हिंदी | SJ Maths',
    h1: 'हिंदी साहित्य का इतिहास',
    description: 'हिंदी साहित्य के इतिहास के सभी अध्याय — आदिकाल, भक्तिकाल, रीतिकाल, आधुनिक काल एवं विगत प्रश्न (PYQ) सहित।',
    heroSubtitle: 'साहित्य इतिहास के अध्यायों के विस्तृत नोट्स, अभ्यास प्रश्न एवं टेस्ट।',
    breadcrumbs: [
      { name: 'Home', url: 'https://sjmaths.com/' },
      { name: 'हिंदी', url: 'https://sjmaths.com/hindi/' },
      { name: 'साहित्य का इतिहास' }
    ],
    themeColor: '#7f1d1d'
  },
  {
    dir: 'hindi/vyakaran',
    route: '/hindi/vyakaran/',
    lang: 'hi',
    title: 'हिंदी व्याकरण — अध्ययन नोट्स | UP PGT/TGT हिंदी | SJ Maths',
    h1: 'हिंदी व्याकरण',
    description: 'हिंदी व्याकरण के सभी अध्याय — संज्ञा, सर्वनाम, विशेषण, क्रिया, कारक, रस, समास, संधि एवं विगत प्रश्न (PYQ) सहित।',
    heroSubtitle: 'व्याकरण के अध्यायों के विस्तृत नोट्स, अभ्यास प्रश्न एवं टेस्ट।',
    breadcrumbs: [
      { name: 'Home', url: 'https://sjmaths.com/' },
      { name: 'हिंदी', url: 'https://sjmaths.com/hindi/' },
      { name: 'व्याकरण' }
    ],
    themeColor: '#7f1d1d'
  },
  {
    dir: 'sanskrit/bharatiya-darshana',
    route: '/sanskrit/bharatiya-darshana/',
    lang: 'sa',
    title: 'भारतीय दर्शनम् — अध्ययन नोट्स | UP PGT संस्कृत | SJ Maths',
    h1: 'भारतीय दर्शनम्',
    description: 'भारतीय दर्शनस्य सर्वाध्यायाः — सांख्यः, योगः, न्यायः, वैशेषिकम्, मीमांसा, वेदान्तः एवं विगतप्रश्नाः (PYQ) सहितम्।',
    heroSubtitle: 'दर्शनशास्त्रस्य अध्यायानां विस्तृताः टिप्पण्यः, अभ्यासप्रश्नाश्च।',
    breadcrumbs: [
      { name: 'Home', url: 'https://sjmaths.com/' },
      { name: 'UP PGT संस्कृत', url: 'https://sjmaths.com/up-pgt-sanskrit/' },
      { name: 'भारतीय दर्शनम्' }
    ],
    themeColor: '#9a3412'
  },
  {
    dir: 'sanskrit/bhashavigyana',
    route: '/sanskrit/bhashavigyana/',
    lang: 'sa',
    title: 'भाषाविज्ञानम् — अध्ययन नोट्स | UP PGT संस्कृत | SJ Maths',
    h1: 'भाषाविज्ञानम्',
    description: 'भाषाविज्ञानस्य सर्वाध्यायाः — भाषायाः उद्भवः, वर्गीकरणम्, ध्वनिविज्ञानम् एवं विगतप्रश्नाः (PYQ) सहितम्।',
    heroSubtitle: 'भाषाविज्ञानस्य अध्यायानां विस्तृताः टिप्पण्यः, अभ्यासप्रश्नाश्च।',
    breadcrumbs: [
      { name: 'Home', url: 'https://sjmaths.com/' },
      { name: 'UP PGT संस्कृत', url: 'https://sjmaths.com/up-pgt-sanskrit/' },
      { name: 'भाषाविज्ञानम्' }
    ],
    themeColor: '#9a3412'
  },
  {
    dir: 'sanskrit/laukika-sahitya',
    route: '/sanskrit/laukika-sahitya/',
    lang: 'sa',
    title: 'लौकिक साहित्यम् — अध्ययन नोट्स | UP PGT संस्कृत | SJ Maths',
    h1: 'लौकिक साहित्यम्',
    description: 'लौकिकसाहित्यस्य सर्वाध्यायाः — कथा, काव्यम्, नाटकम्, गद्यम् एवं विगतप्रश्नाः (PYQ) सहितम्।',
    heroSubtitle: 'लौकिकसाहित्यस्य अध्यायानां विस्तृताः टिप्पण्यः, अभ्यासप्रश्नाश्च।',
    breadcrumbs: [
      { name: 'Home', url: 'https://sjmaths.com/' },
      { name: 'UP PGT संस्कृत', url: 'https://sjmaths.com/up-pgt-sanskrit/' },
      { name: 'लौकिक साहित्यम्' }
    ],
    themeColor: '#9a3412'
  },
  {
    dir: 'sanskrit/sanskrit-vyakarana',
    route: '/sanskrit/sanskrit-vyakarana/',
    lang: 'sa',
    title: 'संस्कृत व्याकरणम् — अध्ययन नोट्स | UP PGT संस्कृत | SJ Maths',
    h1: 'संस्कृत व्याकरणम्',
    description: 'संस्कृतव्याकरणस्य सर्वाध्यायाः — सन्धिः, समासः, कारकम्, शब्दरूपाणि, कारकविभक्तयः एवं विगतप्रश्नाः (PYQ) सहितम्।',
    heroSubtitle: 'व्याकरणस्य अध्यायानां विस्तृताः टिप्पण्यः, अभ्यासप्रश्नाश्च।',
    breadcrumbs: [
      { name: 'Home', url: 'https://sjmaths.com/' },
      { name: 'UP PGT संस्कृत', url: 'https://sjmaths.com/up-pgt-sanskrit/' },
      { name: 'संस्कृत व्याकरणम्' }
    ],
    themeColor: '#9a3412'
  }
];

/* ── generate subject root index pages ────────────────────────────── */
let created = 0;
let skipped = 0;

for (const subj of subjects) {
  const dest = path.join(ROOT, subj.dir, 'index.html');
  if (fs.existsSync(dest)) {
    console.log(`⏭️  SKIP  ${subj.dir}/index.html (already exists)`);
    skipped++;
    continue;
  }

  const subdirs = getSubdirs(subj.dir);
  const children = subdirs.map(d => ({
    name: getChildName(`${subj.dir}/${d}`, d),
    href: `/${subj.dir}/${d}/`,
    dir: `${subj.dir}/${d}`
  }));

  const html = buildDirectoryPage({ ...subj, children });

  if (DRY_RUN) {
    console.log(`🔍 DRY-RUN: would create ${subj.dir}/index.html (${children.length} topics)`);
  } else {
    fs.mkdirSync(path.join(ROOT, subj.dir), { recursive: true });
    fs.writeFileSync(dest, html, 'utf8');
    console.log(`✅ Created ${subj.dir}/index.html (${children.length} topics listed)`);
  }
  created++;
}

/* ── generate art subtopic index pages ────────────────────────────── */
const artSubdirs = getSubdirs('art');
for (const sub of artSubdirs) {
  const dest = path.join(ROOT, 'art', sub, 'index.html');
  if (fs.existsSync(dest)) {
    // already has an index page
    continue;
  }

  const subSubdirs = getSubdirs(`art/${sub}`);
  const children = subSubdirs.map(d => ({
    name: slugToTitle(d),
    href: `/art/${sub}/${d}/`,
    dir: `art/${sub}/${d}`
  }));

  const topicName = slugToTitle(sub);
  const html = buildDirectoryPage({
    route: `/art/${sub}/`,
    title: `${topicName} — Art Study Material | SJ Maths`,
    description: `Study notes on ${topicName} — detailed chapters, revision material and practice questions.`,
    heroSubtitle: `Explore chapters and topics under ${topicName}.`,
    breadcrumbs: [
      { name: 'Home', url: 'https://sjmaths.com/' },
      { name: 'Art', url: 'https://sjmaths.com/art/' },
      { name: topicName }
    ],
    children,
    themeColor: '#8b5cf6'
  });

  if (DRY_RUN) {
    console.log(`🔍 DRY-RUN: would create art/${sub}/index.html (${children.length} subtopics)`);
  } else {
    fs.writeFileSync(dest, html, 'utf8');
    console.log(`✅ Created art/${sub}/index.html (${children.length} subtopics listed)`);
  }
  created++;
}

/* ── generate privacy policy page ─────────────────────────────────── */
const ppDir = path.join(ROOT, 'privacy-policy');
const ppDest = path.join(ppDir, 'index.html');
if (fs.existsSync(ppDest)) {
  console.log('⏭️  SKIP  privacy-policy/index.html (already exists)');
  skipped++;
} else {
  if (!DRY_RUN) {
    fs.mkdirSync(ppDir, { recursive: true });
    fs.writeFileSync(ppDest, buildPrivacyPage(), 'utf8');
    console.log('✅ Created privacy-policy/index.html');
  } else {
    console.log('🔍 DRY-RUN: would create privacy-policy/index.html');
  }
  created++;
}

console.log(`\n${DRY_RUN ? 'DRY-RUN' : 'DONE'}: ${created} pages created, ${skipped} skipped`);
