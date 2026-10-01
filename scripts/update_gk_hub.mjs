import fs from 'node:fs';
import path from 'node:path';

const data = JSON.parse(fs.readFileSync('scripts/gk_full_data.json', 'utf8'));

// Build JSON-LD itemList
let itemPosition = 1;
const schemaItems = [];
data.forEach(m => {
  m.sections.forEach(s => {
    s.topics.forEach(t => {
      schemaItems.push({
        "@type": "ListItem",
        "position": itemPosition++,
        "name": t.title,
        "url": `https://sjmaths.com${t.url}`
      });
    });
  });
});

// Build module cards HTML
const moduleCardsHtml = data.map(m => {
  const sectionTagsHtml = m.sections.map(s => {
    const topicCount = s.topics.length;
    const tagHref = `/up-tgt-pgt-gk/${m.id}/#${s.sectionId}`;
    return `<a class="m-tag m-tag-link" href="${tagHref}" title="View ${s.sectionTitle} (${topicCount} Topics)">${s.sectionTitle} (${topicCount})</a>`;
  }).join('\n          ');

  const totalTopicsInMod = m.sections.reduce((acc, s) => acc + s.topics.length, 0);

  return `
    <div class="module-card" style="--mbg:${m.bg};--mc:${m.color}">
      <div>
        <div class="module-top">
          <div class="module-badge">${m.icon}</div>
          <span class="module-meta">${totalTopicsInMod} Topics</span>
        </div>
        <h3><a class="module-title-link" href="/up-tgt-pgt-gk/${m.id}/">${m.title}</a></h3>
        <p>${m.id === 'indian-history' ? 'Ancient civilizations, medieval dynasties, Mughal administration, British colonial era, and the 1857-1947 freedom movement.' :
             m.id === 'general-science' ? 'Everyday physics, chemical reactions, acids & bases, human physiology, vitamins, diseases, ecology, and scientific developments.' :
             m.id === 'indian-polity' ? 'Constitutional framework, Fundamental Rights, Directive Principles, Parliament, President, Judiciary, and Panchayati Raj.' :
             m.id === 'geography' ? 'Physical features, Himalayan and Peninsular river systems, climate patterns, soil types, natural resources, and UP geography.' :
             m.id === 'art-culture' ? 'Classical dance forms, folk arts of Uttar Pradesh, major fairs and festivals, architectural monuments, and cultural heritage.' :
             'National events, central & UP state government schemes, international summits, sports honours, awards, and appointments.'}</p>
        <div class="module-topics-label">Key Sections &amp; Eras:</div>
        <div class="module-topics">
          ${sectionTagsHtml}
        </div>
      </div>
      <div class="module-footer">
        <a class="module-cta" href="/up-tgt-pgt-gk/${m.id}/">
          <span>Open ${m.title} Tracker</span>
          <span class="arrow-icon">→</span>
        </a>
        <a class="module-browse-btn" href="#module-${m.id}" onclick="filterByModule('${m.id}')">Browse Topics ↓</a>
      </div>
    </div>
  `;
}).join('\n');

// Build the All Topics Directory HTML
const directoryHtml = data.map(m => {
  const sectionsHtml = m.sections.map(s => {
    const topicsListHtml = s.topics.map(t => {
      return `
        <li class="topic-item" data-search="${(t.title + ' ' + t.desc + ' ' + s.sectionTitle + ' ' + m.title).toLowerCase()}">
          <a class="topic-item-link" href="${t.url}" title="Study ${t.title}">
            <span class="topic-indicator">●</span>
            <div class="topic-text-wrap">
              <span class="topic-name">${t.title}</span>
              <span class="topic-sub">${t.desc}</span>
            </div>
            <span class="topic-badge-icon" aria-hidden="true">→</span>
          </a>
        </li>
      `;
    }).join('\n');

    return `
      <div class="section-group" data-section="${s.sectionId}">
        <div class="section-group-head">
          <span class="section-badge">${s.sectionTitle}</span>
          <span class="section-count">${s.topics.length} Topics</span>
        </div>
        <ul class="topic-grid-list">
          ${topicsListHtml}
        </ul>
      </div>
    `;
  }).join('\n');

  const totalInMod = m.sections.reduce((acc, s) => acc + s.topics.length, 0);

  return `
    <article class="directory-module-block" id="module-${m.id}" data-mod="${m.id}" style="--mod-accent:${m.color};--mod-bg:${m.bg}">
      <div class="dir-module-header">
        <div class="dir-module-title-wrap">
          <span class="dir-module-icon">${m.icon}</span>
          <div>
            <h3 class="dir-module-title">${m.title}</h3>
            <span class="dir-module-meta">${m.sections.length} Sections • ${totalInMod} Curriculum Topics</span>
          </div>
        </div>
        <a class="dir-module-link" href="/up-tgt-pgt-gk/${m.id}/">Open Module Study Hub →</a>
      </div>
      <div class="dir-module-body">
        ${sectionsHtml}
      </div>
    </article>
  `;
}).join('\n');

const fullHtml = `<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>UP TGT PGT GK Study Material 2026 | All 77 Topics & Notes Directory | SJ Maths</title>
<meta name="description" content="Complete UP TGT and PGT General Knowledge (GK) & GS syllabus directory. Direct clickable links to all 77 topics across Indian History, General Science, Polity, Geography, Art & Culture and Current Affairs.">
<meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large,max-video-preview:-1">
<meta name="author" content="SJ Maths">
<meta name="theme-color" content="#16324f">
<link rel="canonical" href="https://sjmaths.com/up-tgt-pgt-gk/">
<link rel="icon" type="image/png" href="/favicon.png">

<meta property="og:type" content="website">
<meta property="og:site_name" content="SJ Maths">
<meta property="og:title" content="UP TGT PGT GK Study Material 2026 | All 77 Topics Directory">
<meta property="og:description" content="Direct clickable links to all 77 UP TGT PGT General Knowledge & GS topics across History, Science, Polity, Geography, Art & Culture, and Current Affairs.">
<meta property="og:url" content="https://sjmaths.com/up-tgt-pgt-gk/">
<meta property="og:image" content="https://sjmaths.com/assets/icons/icon-512x512.png">

<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="UP TGT PGT GK Study Material 2026 | SJ Maths">
<meta name="twitter:description" content="Complete clickable topic directory for UP TGT and PGT General Knowledge & GS preparation.">
<meta name="twitter:image" content="https://sjmaths.com/assets/icons/icon-512x512.png">

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "CollectionPage",
  "name": "UP TGT PGT GK Study Material 2026",
  "headline": "UP TGT PGT GK Study Material 2026 | All 77 Topics Directory",
  "description": "Complete UP TGT and PGT General Knowledge (GK) & GS syllabus directory with direct clickable links to all 77 topics.",
  "url": "https://sjmaths.com/up-tgt-pgt-gk/",
  "isPartOf": {
    "@type": "WebSite",
    "name": "SJ Maths",
    "url": "https://sjmaths.com/"
  },
  "breadcrumb": {
    "@type": "BreadcrumbList",
    "itemListElement": [
      {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://sjmaths.com/"},
      {"@type": "ListItem", "position": 2, "name": "UP TGT PGT GK", "item": "https://sjmaths.com/up-tgt-pgt-gk/"}
    ]
  },
  "mainEntity": {
    "@type": "ItemList",
    "numberOfItems": ${schemaItems.length},
    "itemListElement": ${JSON.stringify(schemaItems.slice(0, 30), null, 2)}
  }
}
</script>

<style>
:root{
  --bg:#f6f8fb;
  --paper:#fff;
  --ink:#182238;
  --ink2:#4c576b;
  --muted:#7b8698;
  --line:#e1e7ef;
  --softline:#edf1f5;
  --brand:#16324f;
  --done:#15803d;
  --donebg:#effaf3;
  --accent:#0f766e;
  --shadow:0 16px 38px rgba(28,39,60,.07);
  --header-h:66px;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{
  margin:0;
  background:radial-gradient(circle at 100% 0,rgba(37,99,235,.05),transparent 28rem),radial-gradient(circle at 0 31rem,rgba(15,118,110,.045),transparent 26rem),var(--bg);
  color:var(--ink);
  font-family:Inter,ui-sans-serif,-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Arial,sans-serif;
  line-height:1.5;
  -webkit-font-smoothing:antialiased;
}
a{color:inherit;text-decoration:none}
button,input{font:inherit}
.wrap{width:min(1460px,calc(100% - 32px));margin:auto}

/* Site Header */
.site-header{height:var(--header-h);position:sticky;top:0;z-index:90;background:rgba(255,255,255,.96);backdrop-filter:blur(12px);border-bottom:1px solid var(--line)}
.header-inner{height:100%;display:flex;align-items:center;justify-content:space-between;gap:16px}
.brand{display:flex;gap:11px;align-items:center}
.brand-mark{width:39px;height:39px;border-radius:11px;background:linear-gradient(145deg,#16324f,#2563eb);display:grid;place-items:center;color:#fff;font-weight:900;font-family:'Times New Roman','Cambria Math',serif;font-size:1.65rem;font-style:italic;line-height:1}
.brand-name{display:block;font-weight:850}
.brand-sub{display:block;color:var(--muted);font-size:.68rem}
.exam-chip{padding:8px 12px;border:1px solid #d5deea;border-radius:999px;background:#f4f7fb;color:#274766;font-size:.74rem;font-weight:800}

/* Hero */
.hero{padding:38px 0 22px}
.breadcrumb{display:flex;gap:7px;align-items:center;font-size:.76rem;color:var(--muted);margin-bottom:15px}
.hero-grid{display:grid;grid-template-columns:minmax(0,1fr) 390px;gap:28px;align-items:center}
.kicker{display:inline-flex;align-items:center;gap:9px;color:var(--accent);font-size:.72rem;text-transform:uppercase;font-weight:850;letter-spacing:.1em}
.kicker:before{content:"";width:29px;height:2px;background:var(--accent);border-radius:99px}
h1{margin:9px 0 13px;font-size:clamp(2rem,4vw,3.6rem);line-height:1.04;letter-spacing:-.045em;max-width:980px}
.lead{margin:0;color:var(--ink2);max-width:950px;font-size:1rem}
.hero-tags{display:flex;gap:8px;flex-wrap:wrap;margin-top:18px}
.tag{padding:7px 10px;border:1px solid var(--line);border-radius:999px;background:#fff;font-size:.72rem;font-weight:700;color:var(--ink2)}

.hero-card{background:linear-gradient(145deg,#16324f,#1d4f72);color:#fff;border-radius:22px;padding:24px;box-shadow:0 18px 42px rgba(22,50,79,.18)}
.hero-card-label{color:#c9dfec;font-size:.69rem;text-transform:uppercase;letter-spacing:.1em;font-weight:850}
.hero-card-title{font-size:1.8rem;font-weight:900;margin:6px 0 10px;line-height:1.1}
.hero-card p{margin:0 0 16px;color:#dbe8ef;font-size:.82rem;line-height:1.45}
.hero-card-stats{display:grid;grid-template-columns:repeat(3,1fr);gap:8px}
.hstat{padding:10px;border-radius:11px;background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.08)}
.hstat strong{display:block;font-size:1.15rem}
.hstat span{font-size:.64rem;color:#d8e5ec}

/* Summary Strip */
.summary-strip{margin-bottom:28px;background:#fff;border:1px solid var(--line);border-radius:18px;padding:17px;display:grid;grid-template-columns:1.3fr repeat(3,.55fr);gap:11px}
.summary-intro h2{font-size:1rem;margin:0 0 5px}
.summary-intro p{margin:0;color:var(--muted);font-size:.79rem}
.metric{padding:13px;border-radius:13px;border:1px solid var(--line);background:#fbfcfd}
.metric strong{display:block;font-size:1.25rem}
.metric span{font-size:.68rem;color:var(--muted)}

/* Modules Section */
.modules-section{padding-bottom:32px}
.section-heading{display:flex;justify-content:space-between;align-items:end;margin-bottom:20px;flex-wrap:wrap;gap:12px}
.section-heading h2{margin:0;font-size:1.5rem;font-weight:850;letter-spacing:-.03em}
.section-heading p{margin:4px 0 0;color:var(--muted);font-size:.82rem}

.module-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(330px,1fr));gap:20px}
.module-card{
  background:#fff;border:1px solid var(--line);border-radius:18px;padding:24px;
  box-shadow:0 2px 12px rgba(25,40,55,.035);display:flex;flex-direction:column;justify-content:space-between;
  transition:transform .2s ease,box-shadow .2s ease,border-color .2s ease;
}
.module-card:hover{transform:translateY(-3px);box-shadow:var(--shadow);border-color:#ccd8e6}
.module-top{display:flex;align-items:center;justify-content:space-between;margin-bottom:14px}
.module-badge{width:46px;height:46px;border-radius:13px;background:var(--mbg,#eef4ff);color:var(--mc,#2563eb);display:grid;place-items:center;font-weight:900;font-size:1.15rem}
.module-meta{font-size:.7rem;font-weight:800;color:var(--muted);padding:4px 9px;border-radius:999px;background:#f3f6fa}
.module-card h3{margin:0 0 8px;font-size:1.18rem;font-weight:850}
.module-title-link:hover{color:var(--mc);text-decoration:underline}
.module-card p{margin:0 0 14px;color:var(--ink2);font-size:.84rem;line-height:1.5}
.module-topics-label{font-size:.7rem;font-weight:800;text-transform:uppercase;letter-spacing:.06em;color:var(--muted);margin-bottom:7px}
.module-topics{display:flex;gap:6px;flex-wrap:wrap;margin-bottom:20px}
.m-tag{
  padding:5px 9px;border-radius:7px;background:#f5f7fa;border:1px solid #e5e9f0;
  font-size:.7rem;color:#374151;font-weight:650;transition:all .15s ease;
}
.m-tag-link:hover{background:var(--mbg,#eff6ff);color:var(--mc,#2563eb);border-color:color-mix(in srgb,var(--mc) 30%,transparent)}
.module-footer{display:flex;align-items:center;justify-content:space-between;gap:10px;padding-top:14px;border-top:1px solid var(--softline);margin-top:auto}
.module-cta{display:inline-flex;align-items:center;gap:6px;font-size:.82rem;font-weight:800;color:var(--mc,#2563eb)}
.module-cta .arrow-icon{transition:transform .2s ease}
.module-cta:hover .arrow-icon{transform:translateX(4px)}
.module-browse-btn{font-size:.74rem;font-weight:750;color:var(--muted);padding:4px 8px;border-radius:6px;background:#f8fafc}
.module-browse-btn:hover{color:var(--ink);background:#e2e8f0}

/* Topic Explorer Directory Section */
.directory-section{padding:36px 0 64px}
.dir-toolbar{
  position:sticky;top:var(--header-h);z-index:60;margin-bottom:24px;padding:12px;
  border:1px solid var(--line);border-radius:16px;background:rgba(255,255,255,.96);
  backdrop-filter:blur(12px);box-shadow:0 4px 20px rgba(0,0,0,.03);
  display:flex;flex-direction:column;gap:12px;
}
.search-row{position:relative;width:100%}
.dir-search-icon{position:absolute;left:14px;top:50%;transform:translateY(-50%);width:18px;height:18px;color:#8793a4}
.dir-search{
  width:100%;height:44px;border:1px solid #d4dbe5;border-radius:11px;
  padding:0 14px 0 42px;background:#fff;outline:none;font-size:.88rem;color:var(--ink);
}
.dir-search:focus{border-color:#2563eb;box-shadow:0 0 0 3px rgba(37,99,235,.1)}
.filter-pills{display:flex;gap:6px;overflow-x:auto;padding-bottom:2px;-webkit-overflow-scrolling:touch}
.filter-pill{
  padding:7px 13px;border-radius:999px;border:1px solid var(--line);background:#fbfcfe;
  color:var(--ink2);font-size:.74rem;font-weight:750;cursor:pointer;white-space:nowrap;
  transition:all .15s ease;
}
.filter-pill:hover{background:#f1f5f9;border-color:#cbd5e1}
.filter-pill.active{background:var(--brand);color:#fff;border-color:var(--brand);box-shadow:0 2px 6px rgba(22,50,79,.2)}

/* Directory Module Blocks */
.directory-module-block{
  background:#fff;border:1px solid var(--line);border-radius:18px;overflow:hidden;
  margin-bottom:24px;box-shadow:0 2px 10px rgba(25,40,55,.03);scroll-margin-top:140px;
}
.dir-module-header{
  padding:18px 24px;background:var(--mod-bg,#f8fafc);border-bottom:1px solid var(--line);
  display:flex;align-items:center;justify-content:space-between;gap:16px;flex-wrap:wrap;
  position:relative;
}
.dir-module-header::before{
  content:"";position:absolute;left:0;top:0;bottom:0;width:5px;background:var(--mod-accent,#2563eb);
}
.dir-module-title-wrap{display:flex;align-items:center;gap:14px}
.dir-module-icon{font-size:1.6rem}
.dir-module-title{margin:0;font-size:1.22rem;font-weight:850;color:var(--ink)}
.dir-module-meta{font-size:.74rem;color:var(--muted);display:block;margin-top:2px}
.dir-module-link{
  font-size:.78rem;font-weight:800;color:var(--mod-accent,#2563eb);
  padding:6px 12px;border-radius:8px;background:rgba(255,255,255,.85);border:1px solid var(--line);
}
.dir-module-link:hover{background:#fff;text-decoration:underline}

.dir-module-body{padding:20px 24px}
.section-group{margin-bottom:22px}
.section-group:last-child{margin-bottom:0}
.section-group-head{
  display:flex;align-items:center;justify-content:space-between;gap:10px;
  padding-bottom:8px;margin-bottom:12px;border-bottom:1px dashed var(--line);
}
.section-badge{font-size:.82rem;font-weight:800;color:var(--ink);letter-spacing:-.01em}
.section-count{font-size:.7rem;font-weight:700;color:var(--muted);background:#f1f5f9;padding:2px 8px;border-radius:999px}

/* Topic Grid List */
.topic-grid-list{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(auto-fill,minmax(290px,1fr));gap:10px}
.topic-item{border-radius:11px;transition:all .15s ease}
.topic-item-link{
  display:flex;align-items:center;gap:10px;padding:11px 14px;border:1px solid var(--line);
  border-radius:11px;background:#fbfcfe;color:var(--ink);transition:all .15s ease;height:100%;
}
.topic-item-link:hover{
  background:#fff;border-color:var(--mod-accent,#2563eb);box-shadow:0 3px 10px rgba(0,0,0,.04);
  transform:translateY(-1px);
}
.topic-indicator{font-size:.55rem;color:var(--mod-accent,#2563eb);flex-shrink:0}
.topic-text-wrap{min-width:0;flex:1}
.topic-name{display:block;font-size:.84rem;font-weight:750;line-height:1.35;color:#1e293b}
.topic-sub{display:block;font-size:.69rem;color:var(--muted);margin-top:2px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.topic-badge-icon{font-size:.85rem;color:#94a3b8;transition:transform .15s ease,color .15s ease}
.topic-item-link:hover .topic-badge-icon{transform:translateX(3px);color:var(--mod-accent,#2563eb)}

.no-results{display:none;padding:48px 20px;text-align:center;background:#fff;border:1px dashed var(--line);border-radius:16px;color:var(--muted)}
.no-results strong{display:block;font-size:1.05rem;color:var(--ink);margin-bottom:6px}

/* Quick links strip */
.quick-links-strip{background:#fff;border:1px solid var(--line);border-radius:18px;padding:24px;margin-top:28px}
.quick-links-strip h3{margin:0 0 12px;font-size:1.05rem;font-weight:850}
.quick-tags{display:flex;gap:8px;flex-wrap:wrap}
.quick-tag{padding:8px 13px;border-radius:999px;border:1px solid #dbe3ed;background:#fbfcfe;font-size:.76rem;font-weight:700;color:var(--ink2)}
.quick-tag:hover{border-color:#2563eb;color:#2563eb;background:#eff6ff}

/* Footer */
.footer{padding:28px 0;background:#fff;border-top:1px solid var(--line);color:var(--muted);font-size:.76rem}
.footer-inner{display:flex;justify-content:space-between;gap:14px;flex-wrap:wrap}
.footer a{color:#1d4ed8;font-weight:800}

@media(max-width:1160px){
  .hero-grid{grid-template-columns:1fr}
  .hero-card{max-width:560px}
  .summary-strip{grid-template-columns:1fr 1fr 1fr}
  .summary-intro{grid-column:1/-1}
}
@media(max-width:650px){
  .wrap{width:min(100% - 20px,1460px)}
  .exam-chip{display:none}
  .summary-strip{grid-template-columns:1fr}
  .summary-intro{grid-column:auto}
  .module-grid{grid-template-columns:1fr}
  .topic-grid-list{grid-template-columns:1fr}
  .dir-module-header{padding:14px 16px}
  .dir-module-body{padding:16px 14px}
}
</style>
</head>
<body>
<header class="site-header">
  <div class="wrap header-inner">
    <a class="brand" href="https://sjmaths.com/" aria-label="SJ Maths Home">
      <span class="brand-mark" aria-hidden="true">&int;</span>
      <span>
        <span class="brand-name">SJ Maths</span>
        <span class="brand-sub">Teacher Exam Preparation</span>
      </span>
    </a>
    <span class="exam-chip">UP TGT PGT General Knowledge • 2026 Hub</span>
  </div>
</header>

<main>
<section class="hero">
  <div class="wrap">
    <nav class="breadcrumb" aria-label="Breadcrumb">
      <a href="https://sjmaths.com/">Home</a>
      <span>›</span>
      <span>UP TGT PGT GK</span>
    </nav>
    <div class="hero-grid">
      <div>
        <div class="kicker">UP Teacher Selection • General Studies / GK</div>
        <h1>UP TGT PGT General Knowledge 2026 Study Hub</h1>
        <p class="lead">
          Comprehensive, exam-oriented study modules covering Indian History, General Science, Current Affairs, Indian Polity, Geography, and Culture for Uttar Pradesh TGT &amp; PGT aspirants. Click any topic below to open complete study notes and quizzes.
        </p>
        <div class="hero-tags">
          <span class="tag">6 Core GK Modules</span>
          <span class="tag">77 Clickable Study Topics</span>
          <span class="tag">Concept Quizzes &amp; Tests</span>
          <span class="tag">TGT &amp; PGT Aligned</span>
        </div>
      </div>
      <aside class="hero-card">
        <div class="hero-card-label">General Knowledge Preparation</div>
        <div class="hero-card-title">GS / GK 2026</div>
        <p>Focus on high-scoring general awareness areas with structured notes, factual summaries, and rapid revision pointers.</p>
        <div class="hero-card-stats">
          <div class="hstat"><strong>6</strong><span>Modules</span></div>
          <div class="hstat"><strong>77</strong><span>Core Topics</span></div>
          <div class="hstat"><strong>Free</strong><span>Open Access</span></div>
        </div>
      </aside>
    </div>
  </div>
</section>

<section class="wrap summary-strip">
  <div class="summary-intro">
    <h2>Structured General Studies for UP Teacher Exams</h2>
    <p>Every module is organized into targeted units, allowing you to master historical timelines, scientific principles, constitutional provisions, and current affairs systematically.</p>
  </div>
  <div class="metric"><strong>6</strong><span>Study Modules</span></div>
  <div class="metric"><strong>77</strong><span>Clickable Topics</span></div>
  <div class="metric"><strong>2026</strong><span>Updated Content</span></div>
</section>

<section class="wrap modules-section">
  <div class="section-heading">
    <div>
      <h2>6 Core GK Modules Overview</h2>
      <p>Select any subject module or period tag below to jump directly to detailed study notes and topic-by-topic trackers.</p>
    </div>
  </div>

  <div class="module-grid">
    ${moduleCardsHtml}
  </div>
</section>

<section class="wrap directory-section" id="topic-directory">
  <div class="section-heading">
    <div>
      <h2>Complete Topic-by-Topic GK Directory (77 Topics)</h2>
      <p>Search or filter all individual study topics across History, Science, Polity, Geography, Culture, and Current Affairs. Every topic is directly clickable.</p>
    </div>
  </div>

  <div class="dir-toolbar">
    <div class="search-row">
      <svg class="dir-search-icon" viewBox="0 0 24 24" fill="none" aria-hidden="true">
        <circle cx="11" cy="11" r="6.5" stroke="currentColor" stroke-width="1.8"/>
        <path d="m16 16 4 4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/>
      </svg>
      <input type="search" id="dirSearchInput" class="dir-search" placeholder="Search across all 77 GK topics: Indus Valley, Fundamental Rights, Photosynthesis, 1857 Revolt, Rivers of UP..." autocomplete="off">
    </div>
    <div class="filter-pills" role="tablist" aria-label="Filter GK Topics by Subject">
      <button type="button" class="filter-pill active" onclick="filterByModule('all')">All Modules (77)</button>
      <button type="button" class="filter-pill" onclick="filterByModule('indian-history')">🏛️ Indian History (20)</button>
      <button type="button" class="filter-pill" onclick="filterByModule('general-science')">🔬 General Science (16)</button>
      <button type="button" class="filter-pill" onclick="filterByModule('indian-polity')">⚖️ Indian Polity (12)</button>
      <button type="button" class="filter-pill" onclick="filterByModule('geography')">🌍 Geography (10)</button>
      <button type="button" class="filter-pill" onclick="filterByModule('art-culture')">🎨 Art &amp; Culture (10)</button>
      <button type="button" class="filter-pill" onclick="filterByModule('current-affairs')">📰 Current Affairs (9)</button>
    </div>
  </div>

  <div id="dirContainer">
    ${directoryHtml}
  </div>

  <div class="no-results" id="noResultsMsg">
    <strong>No matching topics found</strong>
    <span>Try searching for another keyword like "Ashoka", "Constitution", "Vitamins", "Rivers", or "Dance".</span>
  </div>

  <div class="quick-links-strip">
    <h3>Jump to Subject Syllabi &amp; Trackers</h3>
    <div class="quick-tags">
      <a class="quick-tag" href="/up-tgt-mathematics/">UP TGT Mathematics</a>
      <a class="quick-tag" href="/up-pgt-physics/">UP PGT Physics</a>
      <a class="quick-tag" href="/up-pgt-sociology/">UP PGT Sociology</a>
      <a class="quick-tag" href="/physical-education/">Physical Education</a>
      <a class="quick-tag" href="/up-tgt-science/">UP TGT Science</a>
      <a class="quick-tag" href="/up-tgt-social-science/">UP TGT Social Science</a>
      <a class="quick-tag" href="/up-tgt-hindi/">UP TGT Hindi</a>
      <a class="quick-tag" href="/up-tgt-english/">UP TGT English</a>
      <a class="quick-tag" href="/up-tgt-sanskrit/">UP TGT Sanskrit</a>
      <a class="quick-tag" href="/up-tgt-physical-education/">UP TGT Physical Education</a>
      <a class="quick-tag" href="/up-tgt-commerce/">UP TGT Commerce</a>
      <a class="quick-tag" href="/up-tgt-agriculture/">UP TGT Agriculture</a>
      <a class="quick-tag" href="/up-tgt-home-science/">UP TGT Home Science</a>
    </div>
  </div>
</section>
</main>

<footer class="footer">
  <div class="wrap footer-inner">
    <span>UP TGT PGT General Knowledge &amp; General Studies 2026 • SJ Maths</span>
    <div>
      <a href="https://sjmaths.com/">Home</a> &nbsp;•&nbsp;
      <a href="/up-tgt-pgt-gk/">UP TGT PGT GK</a> &nbsp;•&nbsp;
      <a href="/up-pgt-sociology/">UP PGT Sociology</a> &nbsp;•&nbsp;
      <a href="/physical-education/">Physical Education</a>
    </div>
  </div>
</footer>

<script>
let currentFilter = 'all';

function filterByModule(modId) {
  currentFilter = modId;
  
  // Update pill active classes
  const pills = document.querySelectorAll('.filter-pill');
  pills.forEach(pill => {
    if (modId === 'all' && pill.textContent.includes('All')) {
      pill.classList.add('active');
    } else if (pill.getAttribute('onclick')?.includes(modId)) {
      pill.classList.add('active');
    } else {
      pill.classList.remove('active');
    }
  });

  applyFilters();
}

function applyFilters() {
  const query = document.getElementById('dirSearchInput').value.trim().toLowerCase();
  const moduleBlocks = document.querySelectorAll('.directory-module-block');
  let totalVisibleTopics = 0;

  moduleBlocks.forEach(block => {
    const mod = block.getAttribute('data-mod');
    const isModuleMatch = (currentFilter === 'all' || currentFilter === mod);

    if (!isModuleMatch) {
      block.style.display = 'none';
      return;
    }

    let moduleHasVisibleTopics = false;
    const sectionGroups = block.querySelectorAll('.section-group');

    sectionGroups.forEach(sec => {
      let secHasVisible = false;
      const topicItems = sec.querySelectorAll('.topic-item');

      topicItems.forEach(item => {
        const searchData = item.getAttribute('data-search') || '';
        const isSearchMatch = !query || searchData.includes(query);

        if (isSearchMatch) {
          item.style.display = '';
          secHasVisible = true;
          moduleHasVisibleTopics = true;
          totalVisibleTopics++;
        } else {
          item.style.display = 'none';
        }
      });

      sec.style.display = secHasVisible ? '' : 'none';
    });

    block.style.display = moduleHasVisibleTopics ? '' : 'none';
  });

  const noResults = document.getElementById('noResultsMsg');
  if (noResults) {
    noResults.style.display = totalVisibleTopics === 0 ? 'block' : 'none';
  }
}

document.getElementById('dirSearchInput').addEventListener('input', applyFilters);
</script>
</body>
</html>
`;

fs.writeFileSync('up-tgt-pgt-gk/index.html', fullHtml, 'utf8');
console.log('✓ Successfully updated up-tgt-pgt-gk/index.html with all 77 clickable topics!');
