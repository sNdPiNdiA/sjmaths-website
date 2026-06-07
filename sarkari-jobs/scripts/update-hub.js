'use strict';

const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..', '..');
const DATA_FILE = path.join(ROOT, 'sarkari-jobs', 'data', 'jobs.json');
const HUB_FILE = path.join(ROOT, 'sarkari-jobs', 'index.html');

function loadJson(p, fallback) {
  if (!fs.existsSync(p)) return fallback;
  try { return JSON.parse(fs.readFileSync(p, 'utf8')); }
  catch { return fallback; }
}

function escapeHtml(value) {
  return String(value || '')
    .replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;')
    .replaceAll('"', '&quot;');
}

function renderHub(data) {
  const allJobs = Array.isArray(data.jobs) ? data.jobs : [];
  
  // Filter out non-vacancy reports and generic scraped pages
  const jobs = allJobs.filter(job => {
    const t = (job.title || '').toLowerCase();
    const blocklist = [
      'home', 'report', 'irsp_', 'irass_', 'statistical', 'fact & figure',
      'year book', 'about indian railways', 'revenue frieght', 'efficiency parameters',
      'latest job', 'archive'
    ];
    
    // Explicit exclusions
    if (blocklist.some(w => t.includes(w))) return false;
    
    // Exact match exclusions for short generic titles
    if (t === 'mer') return false;
    
    // Exclude very short generic titles
    if (t.length < 10 && !t.includes('ssc') && !t.includes('rrb') && !t.includes('rrc')) return false;
    
    return true;
  });

  const cards = jobs.slice(0, 50).map(job => `
    <article class="job-card">
      <div class="card-glow"></div>
      <div class="card-content">
        <div class="card-header">
          <span class="portal-badge ${escapeHtml(job.portal || 'default').toLowerCase()}">${escapeHtml(job.portal || 'Portal')}</span>
          ${job.applyEnd && job.applyEnd !== 'Not available' ? `<span class="status-badge pulse">Active</span>` : ''}
        </div>
        
        <h3 class="job-title">${escapeHtml(job.title)}</h3>
        <p class="job-summary">${escapeHtml(job.summary || 'Official notification details and full criteria are available on the linked document.')}</p>
        
        <div class="job-meta">
          <div class="meta-item">
            <div class="meta-icon-wrapper">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M22 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>
            </div>
            <div class="meta-text">
              <span class="meta-label">Vacancy</span>
              <span class="meta-value">${escapeHtml(job.vacancy || 'Not Specified')}</span>
            </div>
          </div>
          
          <div class="meta-item">
            <div class="meta-icon-wrapper">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
            </div>
            <div class="meta-text">
              <span class="meta-label">Deadline</span>
              <span class="meta-value highlight">${escapeHtml(job.applyEnd || 'Until Filled')}</span>
            </div>
          </div>
        </div>

        <div class="card-actions">
          ${job.pageUrl ? `<a href="${escapeHtml(job.pageUrl)}" class="btn btn-outline">
            <span>View Details</span>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
          </a>` : ''}
          ${job.pdfUrl ? `<a href="${escapeHtml(job.pdfUrl)}" target="_blank" rel="noreferrer" class="btn btn-primary">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
            <span>Official PDF</span>
          </a>` : ''}
        </div>
      </div>
    </article>
  `).join('');

  return `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Sarkari Jobs Hub | Premium Government Job Portal</title>
  <meta name="description" content="Latest premium government job notifications auto-generated from official portals." />
  <link rel="canonical" href="https://sjmaths.com/sarkari-jobs/" />
  
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
  
  <style>
    :root {
      --bg-body: #f4f7f9;
      --bg-surface: #ffffff;
      
      --text-hero: #ffffff;
      --text-primary: #0f172a;
      --text-secondary: #475569;
      --text-tertiary: #64748b;
      
      --brand-primary: #2563eb;
      --brand-primary-hover: #1d4ed8;
      --brand-accent: #38bdf8;
      
      --border-light: rgba(226, 232, 240, 0.8);
      --border-dark: rgba(255, 255, 255, 0.1);
      
      --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
      --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
      --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.05), 0 4px 6px -2px rgba(0, 0, 0, 0.025);
      --shadow-hover: 0 20px 25px -5px rgba(0, 0, 0, 0.08), 0 10px 10px -5px rgba(0, 0, 0, 0.03);
      
      --radius-sm: 0.5rem;
      --radius-md: 0.75rem;
      --radius-lg: 1.25rem;
      --radius-xl: 1.5rem;
      
      --transition-spring: cubic-bezier(0.175, 0.885, 0.32, 1.275);
      --transition-smooth: cubic-bezier(0.4, 0, 0.2, 1);
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      background-color: var(--bg-body);
      font-family: 'Inter', sans-serif;
      color: var(--text-primary);
      line-height: 1.6;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
      background-image: 
        radial-gradient(at 0% 0%, hsla(210,100%,96%,1) 0, transparent 50%), 
        radial-gradient(at 100% 0%, hsla(215,100%,94%,1) 0, transparent 50%);
      background-attachment: fixed;
    }

    h1, h2, h3, h4, .brand-font {
      font-family: 'Plus Jakarta Sans', sans-serif;
    }

    /* --- Navbar (Optional minimalist nav) --- */
    nav {
      position: fixed;
      top: 0; left: 0; right: 0;
      height: 64px;
      background: rgba(255, 255, 255, 0.8);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--border-light);
      z-index: 50;
      display: flex;
      align-items: center;
      padding: 0 2rem;
    }
    .nav-brand {
      font-family: 'Plus Jakarta Sans', sans-serif;
      font-weight: 800;
      font-size: 1.25rem;
      color: var(--text-primary);
      text-decoration: none;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }
    .nav-brand-dot {
      width: 8px; height: 8px;
      background: var(--brand-primary);
      border-radius: 50%;
    }

    /* --- Hero Section --- */
    .hero {
      position: relative;
      padding: 10rem 2rem 8rem 2rem;
      background: #0f172a;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
    }

    /* Premium gradient background for Hero */
    .hero-bg {
      position: absolute;
      top: 0; left: 0; right: 0; bottom: 0;
      background: 
        radial-gradient(circle at 15% 50%, rgba(37, 99, 235, 0.15), transparent 25%),
        radial-gradient(circle at 85% 30%, rgba(56, 189, 248, 0.15), transparent 25%);
      z-index: 0;
    }
    
    .hero::after {
      content: '';
      position: absolute;
      bottom: 0; left: 0; right: 0;
      height: 100px;
      background: linear-gradient(to top, var(--bg-body), transparent);
      z-index: 1;
    }

    .hero-content {
      position: relative;
      z-index: 2;
      max-width: 800px;
      animation: fadeUp 0.8s var(--transition-spring) forwards;
    }

    .hero-badge {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      padding: 0.5rem 1rem;
      background: rgba(255, 255, 255, 0.1);
      border: 1px solid rgba(255, 255, 255, 0.15);
      border-radius: 2rem;
      color: rgba(255, 255, 255, 0.9);
      font-size: 0.875rem;
      font-weight: 500;
      margin-bottom: 1.5rem;
      backdrop-filter: blur(8px);
      -webkit-backdrop-filter: blur(8px);
    }

    .hero-badge-pulse {
      width: 6px; height: 6px;
      background: #4ade80;
      border-radius: 50%;
      box-shadow: 0 0 0 0 rgba(74, 222, 128, 0.7);
      animation: pulseGreen 2s infinite;
    }

    .hero h1 {
      font-size: clamp(2.5rem, 5vw, 4rem);
      font-weight: 800;
      color: var(--text-hero);
      line-height: 1.1;
      letter-spacing: -0.03em;
      margin-bottom: 1.25rem;
    }
    
    .hero h1 span {
      background: linear-gradient(135deg, #60a5fa, #a78bfa);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .hero p {
      font-size: 1.125rem;
      color: #94a3b8;
      max-width: 600px;
      margin: 0 auto;
      line-height: 1.6;
    }

    /* --- Main Layout & Grid --- */
    .container {
      max-width: 1280px;
      margin: -3rem auto 4rem auto;
      padding: 0 1.5rem;
      position: relative;
      z-index: 10;
    }

    .section-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 2rem;
    }

    .section-title {
      font-size: 1.5rem;
      font-weight: 700;
      color: var(--text-primary);
    }

    .jobs-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
      gap: 1.5rem;
    }

    /* --- Premium Job Cards --- */
    .job-card {
      position: relative;
      background: var(--bg-surface);
      border-radius: var(--radius-xl);
      border: 1px solid rgba(226, 232, 240, 0.6);
      box-shadow: var(--shadow-md);
      transition: all 0.4s var(--transition-spring);
      display: flex;
      flex-direction: column;
      overflow: hidden;
      z-index: 1;
    }

    .card-glow {
      position: absolute;
      top: 0; left: 0; right: 0; bottom: 0;
      background: radial-gradient(circle at 50% 0%, rgba(37, 99, 235, 0.03), transparent 70%);
      opacity: 0;
      transition: opacity 0.4s ease;
      z-index: -1;
      pointer-events: none;
    }

    .job-card:hover {
      transform: translateY(-6px);
      box-shadow: var(--shadow-hover);
      border-color: rgba(226, 232, 240, 1);
    }

    .job-card:hover .card-glow {
      opacity: 1;
    }

    .card-content {
      padding: 1.75rem;
      display: flex;
      flex-direction: column;
      flex-grow: 1;
    }

    .card-header {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 1.25rem;
    }

    .portal-badge {
      display: inline-flex;
      align-items: center;
      padding: 0.35rem 0.75rem;
      background: #f1f5f9;
      color: #334155;
      border-radius: var(--radius-sm);
      font-size: 0.75rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      font-family: 'Plus Jakarta Sans', sans-serif;
    }

    /* Specific portal colors */
    .portal-badge.ssc { background: #e0e7ff; color: #1e40af; }
    .portal-badge.upsc { background: #fce7f3; color: #86198f; }
    .portal-badge.rrb { background: #ffedd5; color: #be185d; }

    .status-badge {
      font-size: 0.7rem;
      font-weight: 600;
      color: #059669;
      background: #d1fae5;
      padding: 0.25rem 0.6rem;
      border-radius: 1rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    .job-title {
      font-size: 1.25rem;
      font-weight: 700;
      color: var(--text-primary);
      margin-bottom: 0.75rem;
      line-height: 1.4;
      display: -webkit-box;
      -webkit-line-clamp: 2;
      -webkit-box-orient: vertical;
      overflow: hidden;
    }

    .job-summary {
      font-size: 0.95rem;
      color: var(--text-secondary);
      margin-bottom: 1.5rem;
      flex-grow: 1;
      line-height: 1.6;
      display: -webkit-box;
      -webkit-line-clamp: 3;
      -webkit-box-orient: vertical;
      overflow: hidden;
    }

    /* Meta Info Blocks */
    .job-meta {
      display: flex;
      flex-direction: column;
      gap: 0.75rem;
      padding: 1rem;
      background: #f8fafc;
      border-radius: var(--radius-md);
      margin-bottom: 1.5rem;
      border: 1px solid #f1f5f9;
    }

    .meta-item {
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }

    .meta-icon-wrapper {
      display: flex;
      align-items: center;
      justify-content: center;
      width: 32px;
      height: 32px;
      background: #ffffff;
      border-radius: 8px;
      color: var(--brand-primary);
      box-shadow: 0 1px 2px rgba(0,0,0,0.05);
      flex-shrink: 0;
    }

    .meta-text {
      display: flex;
      flex-direction: column;
    }

    .meta-label {
      font-size: 0.75rem;
      font-weight: 500;
      color: var(--text-tertiary);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    .meta-value {
      font-size: 0.9rem;
      font-weight: 600;
      color: var(--text-primary);
    }
    
    .meta-value.highlight {
      color: #b91c1c; /* A subtle red for deadlines */
    }

    /* Actions */
    .card-actions {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 0.75rem;
      margin-top: auto;
    }

    .btn {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 0.5rem;
      padding: 0.75rem 1rem;
      border-radius: var(--radius-md);
      font-size: 0.875rem;
      font-weight: 600;
      text-decoration: none;
      transition: all 0.2s var(--transition-smooth);
      font-family: 'Plus Jakarta Sans', sans-serif;
    }

    .btn-primary {
      background: var(--brand-primary);
      color: white;
      box-shadow: 0 4px 6px -1px rgba(37, 99, 235, 0.2);
    }

    .btn-primary:hover {
      background: var(--brand-primary-hover);
      transform: translateY(-1px);
      box-shadow: 0 6px 8px -1px rgba(37, 99, 235, 0.3);
    }

    .btn-outline {
      background: transparent;
      color: var(--text-primary);
      border: 1px solid #e2e8f0;
    }

    .btn-outline:hover {
      background: #f8fafc;
      border-color: #cbd5e1;
    }

    /* Empty State */
    .empty-state {
      grid-column: 1 / -1;
      text-align: center;
      padding: 5rem 2rem;
      background: white;
      border-radius: var(--radius-xl);
      border: 1px dashed #cbd5e1;
      box-shadow: var(--shadow-sm);
    }
    .empty-icon {
      width: 64px; height: 64px;
      margin: 0 auto 1.5rem;
      color: #cbd5e1;
    }

    /* Animations */
    @keyframes fadeUp {
      from { opacity: 0; transform: translateY(20px); }
      to { opacity: 1; transform: translateY(0); }
    }
    
    @keyframes pulseGreen {
      0% { box-shadow: 0 0 0 0 rgba(74, 222, 128, 0.7); }
      70% { box-shadow: 0 0 0 6px rgba(74, 222, 128, 0); }
      100% { box-shadow: 0 0 0 0 rgba(74, 222, 128, 0); }
    }

    /* Staggered load for cards */
    .jobs-grid > article {
      opacity: 0;
      animation: fadeUp 0.6s var(--transition-spring) forwards;
    }
    
    ${jobs.slice(0,10).map((_, i) => `
    .jobs-grid > article:nth-child(${i+1}) { animation-delay: ${0.1 * i}s; }
    `).join('')}
    
    .jobs-grid > article:nth-child(n+11) { animation-delay: 0.5s; }

    @media (max-width: 768px) {
      .hero { padding: 8rem 1.5rem 6rem 1.5rem; }
      .hero h1 { font-size: 2.5rem; }
      .card-actions { grid-template-columns: 1fr; }
      .container { padding: 0 1rem; margin-top: -2rem; }
      .jobs-grid { grid-template-columns: 1fr; }
    }
  </style>
</head>
<body>
  <nav>
    <a href="/" class="nav-brand">
      <div class="nav-brand-dot"></div>
      SJMaths
    </a>
  </nav>

  <header class="hero">
    <div class="hero-bg"></div>
    <div class="hero-content">
      <div class="hero-badge">
        <div class="hero-badge-pulse"></div>
        ${jobs.length} Opportunities Indexed
      </div>
      <h1>Sarkari Jobs <span>Hub</span></h1>
      <p>Discover the latest premium government opportunities. Auto-curated and intelligently extracted directly from official Indian portals.</p>
    </div>
  </header>

  <main class="container">
    <div class="section-header">
      <h2 class="section-title brand-font">Latest Notifications</h2>
    </div>
    
    <section class="jobs-grid">
      ${cards || `
        <div class="empty-state">
          <svg class="empty-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M20 13V6a2 2 0 00-2-2H6a2 2 0 00-2 2v7m16 0v5a2 2 0 01-2 2H6a2 2 0 01-2-2v-5m16 0h-2.586a1 1 0 00-.707.293l-2.414 2.414a1 1 0 01-.707.293h-3.172a1 1 0 01-.707-.293l-2.414-2.414A1 1 0 006.586 13H4"></path></svg>
          <h3 style="font-size:1.25rem; font-weight:700; color:#0f172a; margin-bottom:0.5rem; font-family:'Plus Jakarta Sans',sans-serif;">No jobs indexed yet</h3>
          <p style="color:#64748b;">The fetch pipeline needs to be run to populate the feed.</p>
        </div>
      `}
    </section>
  </main>
</body>
</html>`;
}

function main() {
  const data = loadJson(DATA_FILE, { version: 1, jobs: [] });
  fs.writeFileSync(HUB_FILE, renderHub(data), 'utf8');
  console.log(`[hub] Wrote ${HUB_FILE} with ${Array.isArray(data.jobs) ? data.jobs.length : 0} jobs`);
}

main();
