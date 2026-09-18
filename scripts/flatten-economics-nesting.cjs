const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');

// 1. Unify policies into a single authoritative module
const policiesDir = path.join(ROOT, 'economics/indian-economy/policies-for-poverty-population-and-unemployment');
if (!fs.existsSync(policiesDir)) fs.mkdirSync(policiesDir, { recursive: true });

const policiesHtml = `<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Socio-Economic Policies: Poverty, Population, and Unemployment in India — Economics Study Guide | SJ Maths</title>
<meta name="description" content="Comprehensive analysis of policy interventions in India targeting poverty alleviation, population stabilization, and employment generation for UP PGT & TGT.">
<meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large,max-video-preview:-1">
<meta name="author" content="SJ Maths">
<meta name="theme-color" content="#16324f">
<link rel="canonical" href="https://sjmaths.com/economics/indian-economy/policies-for-poverty-population-and-unemployment/">
<link rel="icon" type="image/png" href="/favicon.png">

<style>
:root {
  --bg: #f5f8fc;
  --surface: #ffffff;
  --ink: #162438;
  --ink2: #465b77;
  --muted: #6f829c;
  --border: #dbe4f0;
  --primary: #1d4ed8;
  --primary-bg: #eff6ff;
  --radius: 14px;
  --shadow: 0 8px 24px rgba(22, 36, 56, 0.08);
}
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background: var(--bg); color: var(--ink); line-height: 1.6; padding-bottom: 60px; }
.site-header { background: #112239; color: #fff; padding: 14px 20px; border-bottom: 1px solid rgba(255,255,255,0.08); }
.header-inner { max-width: 1040px; margin: 0 auto; display: flex; align-items: center; justify-content: space-between; }
.brand-link { color: #fff; text-decoration: none; font-weight: 700; font-size: 1.15rem; }
.back-btn { color: #dbeafe; text-decoration: none; font-size: 0.82rem; border: 1px solid rgba(255,255,255,0.18); padding: 6px 12px; border-radius: 6px; }
.wrap { max-width: 1040px; margin: 0 auto; padding: 24px 20px 0; }
.hero { background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius); padding: 28px 32px; box-shadow: var(--shadow); margin-bottom: 24px; }
.breadcrumb { font-size: 0.8rem; color: var(--muted); margin-bottom: 10px; display: flex; gap: 6px; }
.breadcrumb a { color: var(--primary); text-decoration: none; }
.kicker { color: var(--primary); font-size: 0.76rem; font-weight: 700; text-transform: uppercase; margin-bottom: 6px; }
h1 { font-size: 1.65rem; font-weight: 800; color: #0f172a; margin-bottom: 10px; }
.lead { font-size: 0.95rem; color: var(--ink2); margin-bottom: 16px; }
.main-grid { display: grid; grid-template-columns: 1fr 310px; gap: 24px; }
@media(max-width:840px) { .main-grid { grid-template-columns: 1fr; } }
.card { background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius); padding: 24px 28px; box-shadow: var(--shadow); margin-bottom: 20px; }
.card h2 { font-size: 1.15rem; font-weight: 700; margin-bottom: 12px; color: #0f172a; }
.checklist { display: flex; flex-direction: column; gap: 10px; margin-top: 12px; }
.check-item { display: flex; align-items: flex-start; gap: 10px; font-size: 0.88rem; color: var(--ink2); cursor: pointer; }
.sidebar-card { background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius); padding: 20px 22px; box-shadow: var(--shadow); position: sticky; top: 20px; }
.action-box { background: var(--primary-bg); border: 1px solid #bfdbfe; border-radius: 10px; padding: 14px; margin-top: 10px; }
.action-btn { display: inline-block; background: var(--primary); color: #fff; text-decoration: none; font-size: 0.8rem; font-weight: 600; padding: 6px 14px; border-radius: 6px; }
.footer { border-top: 1px solid var(--border); margin-top: 48px; padding: 24px 20px; font-size: 0.82rem; color: var(--muted); background: var(--surface); text-align: center; }
</style>
</head>
<body>
<header class="site-header">
  <div class="header-inner">
    <a class="brand-link" href="/">SJ Maths <span>• Economics</span></a>
    <a class="back-btn" href="/up-pgt-economics/">← Back to UP PGT Economics</a>
  </div>
</header>

<main class="wrap">
  <section class="hero">
    <nav class="breadcrumb">
      <a href="/">Home</a> <span>›</span> <a href="/up-pgt-economics/">Economics</a> <span>›</span> <span>Indian Economy</span>
    </nav>
    <div class="kicker">Indian Economy</div>
    <h1>Socio-Economic Policies: Poverty, Population, and Unemployment in India</h1>
    <p class="lead">Integrated master module covering government interventions for poverty alleviation, demographic transition policies, and employment generation in India.</p>
  </section>

  <div class="main-grid">
    <div class="content-col">
      <article class="card">
        <h2>1. Key Policy Frameworks &amp; Interventions</h2>
        <div class="checklist">
          <label class="check-item"><input type="checkbox"> <span><strong>Poverty Alleviation Policies:</strong> Tendulkar and Rangarajan poverty line methodologies; PM Garib Kalyan Anna Yojana, DAY-NRLM, and PM Awas Yojana.</span></label>
          <label class="check-item"><input type="checkbox"> <span><strong>Population Policy of India:</strong> National Population Policy (NPP 2000), total fertility rate (TFR) stabilization, maternal-child healthcare missions, and demographic dividend utilization.</span></label>
          <label class="check-item"><input type="checkbox"> <span><strong>Employment Generation Programmes:</strong> MGNREGA legal entitlement, PM Kaushal Vikas Yojana (PMKVY), Mudra Yojana for self-employment, and Atmanirbhar Bharat Rojgar Yojana.</span></label>
          <label class="check-item"><input type="checkbox"> <span><strong>Interconnected Triad:</strong> How population stabilization directly mitigates poverty severity and reduces structural disguised unemployment in rural India.</span></label>
        </div>
      </article>

      <article class="card">
        <h2>2. Study &amp; Self-Assessment Checklist</h2>
        <div class="checklist">
          <label class="check-item"><input type="checkbox"> <span>Read theoretical notes &amp; conceptual summary</span></label>
          <label class="check-item"><input type="checkbox"> <span>Memorized key commission recommendations &amp; policy target dates</span></label>
          <label class="check-item"><input type="checkbox"> <span>Solved minimum 20 previous years' questions (PYQ)</span></label>
          <label class="check-item"><input type="checkbox"> <span>Marked complete on main syllabus tracker</span></label>
        </div>
      </article>
    </div>

    <aside class="sidebar-col">
      <div class="sidebar-card">
        <h3>Exam Trackers</h3>
        <div class="action-box">
          <strong style="color:#1e3a8a;display:block;margin-bottom:4px">UP PGT Economics</strong>
          <p style="font-size:0.78rem;color:#1d4ed8;margin-bottom:10px">Interactive progress tracking &amp; PYQs</p>
          <a class="action-btn" href="/up-pgt-economics/">Open PGT Tracker →</a>
        </div>
        <div class="action-box" style="margin-top:12px;background:#f0fdf4;border-color:#bbf7d0">
          <strong style="color:#166534;display:block;margin-bottom:4px">UP TGT Social Science</strong>
          <p style="font-size:0.78rem;color:#15803d;margin-bottom:10px">Economics section syllabus tracking</p>
          <a class="action-btn" href="/up-tgt-social-science/" style="background:#16a34a">Open TGT Tracker →</a>
        </div>
      </div>
    </aside>
  </div>
</main>

<footer class="footer">
  <span>SJ Maths • Master Subject Library • Socio-Economic Policies</span>
</footer>
</body>
</html>
`;

fs.writeFileSync(path.join(policiesDir, 'index.html'), policiesHtml, 'utf8');
console.log('Created unified policies module.');

// Remove old policies subfolders
fs.rmSync(path.join(ROOT, 'economics/indian-economy/policies'), { recursive: true, force: true });
console.log('Removed old economics/indian-economy/policies directory.');

// 2. Flatten deep folders into clean parent paths
const movePlans = [
  {
    from: 'economics/indian-economy/agriculture-sector/farmers-and-problems',
    to: 'economics/indian-economy/agricultural-problems-and-farmers'
  },
  {
    from: 'economics/indian-economy/agriculture-sector/marketing-and-food-security',
    to: 'economics/indian-economy/agricultural-marketing-and-food-security'
  },
  {
    from: 'economics/indian-economy/agriculture-sector/rural-development-programmes',
    to: 'economics/indian-economy/rural-development-programmes'
  },
  {
    from: 'economics/indian-economy/employment/unemployment-in-india',
    to: 'economics/indian-economy/unemployment-in-india'
  },
  {
    from: 'economics/indian-economy/industrial-sector/policy-and-msme',
    to: 'economics/indian-economy/industrial-policy-and-msme'
  },
  {
    from: 'economics/indian-economy/population/trends',
    to: 'economics/indian-economy/demographic-trends-in-india'
  },
  {
    from: 'economics/macro-economics/trade-cycle/theories',
    to: 'economics/macro-economics/trade-cycle-theories'
  },
  {
    from: 'economics/micro-economics/consumer-behaviour/demand-and-utility',
    to: 'economics/micro-economics/demand-and-utility'
  },
  {
    from: 'economics/micro-economics/consumer-behaviour/indifference-curve-analysis',
    to: 'economics/micro-economics/indifference-curve-analysis'
  },
  {
    from: 'economics/micro-economics/consumer-behaviour/revealed-preference-theory',
    to: 'economics/micro-economics/revealed-preference-theory'
  },
  {
    from: 'economics/micro-economics/distribution-theory/theories-of-interest-and-profit',
    to: 'economics/micro-economics/theories-of-interest-and-profit'
  },
  {
    from: 'economics/micro-economics/distribution-theory/theories-of-rent-and-wages',
    to: 'economics/micro-economics/theories-of-rent-and-wages'
  },
  {
    from: 'economics/micro-economics/production-theory/cost-and-revenue-curves',
    to: 'economics/micro-economics/cost-and-revenue-curves'
  },
  {
    from: 'economics/micro-economics/production-theory/production-functions-and-returns',
    to: 'economics/micro-economics/production-functions-and-returns'
  }
];

for (const m of movePlans) {
  const src = path.join(ROOT, m.from);
  const dst = path.join(ROOT, m.to);
  if (fs.existsSync(src)) {
    if (!fs.existsSync(dst)) fs.mkdirSync(dst, { recursive: true });
    fs.cpSync(src, dst, { recursive: true });
    fs.rmSync(src, { recursive: true, force: true });
    // Update canonical in dst/index.html
    const idx = path.join(dst, 'index.html');
    if (fs.existsSync(idx)) {
      let h = fs.readFileSync(idx, 'utf8');
      h = h.replace(new RegExp(m.from.replace(/\//g, '\\/'), 'g'), m.to);
      fs.writeFileSync(idx, h, 'utf8');
    }
    console.log(`Flattened: ${m.from} -> ${m.to}`);
  }
}

// Clean empty parent directories
function cleanEmptyDirs(dir) {
  let isDir = false;
  try { isDir = fs.statSync(dir).isDirectory(); } catch (e) { return; }
  if (!isDir) return;
  const entries = fs.readdirSync(dir);
  for (const ent of entries) {
    const full = path.join(dir, ent);
    if (fs.statSync(full).isDirectory()) cleanEmptyDirs(full);
  }
  if (dir !== path.join(ROOT, 'economics') && fs.readdirSync(dir).length === 0) {
    fs.rmdirSync(dir);
    console.log(`Removed empty parent directory: ${path.relative(ROOT, dir)}`);
  }
}
cleanEmptyDirs(path.join(ROOT, 'economics'));

console.log('Nesting flattening complete.');
