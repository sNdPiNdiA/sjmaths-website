const fs = require('fs');
const path = require('path');

const dataJson = fs.readFileSync('csir-net/mathematics/topics-data.json', 'utf8');

const html = `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>CSIR-UGC NET Mathematics · Official Topic Tracker & Study Hub | SJMaths</title>
<meta name="description" content="Interactive CSIR-UGC NET Mathematics curriculum checklist & topic hub. Track progress across Real Analysis, Linear Algebra, Complex Analysis, Modern Algebra, Topology, ODE, PDE, Applied Maths & Statistics with persistent tick boxes.">
<meta name="robots" content="index, follow">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
<style>
  :root {
    --bg-primary: #080E18;
    --bg-secondary: #0E1A2C;
    --bg-card: rgba(16, 29, 49, 0.72);
    --bg-card-hover: rgba(22, 38, 64, 0.85);
    --border-color: rgba(43, 72, 112, 0.45);
    --border-highlight: rgba(88, 140, 206, 0.55);
    --text-main: #F1F5F9;
    --text-muted: #94A3B8;
    --text-subtle: #64748B;
    --accent-teal: #14B8A6;
    --accent-emerald: #10B981;
    --accent-blue: #38BDF8;
    --accent-indigo: #818CF8;
    --accent-purple: #A78BFA;
    --accent-pink: #F472B6;
    --accent-amber: #F59E0B;
    --radius-sm: 8px;
    --radius-md: 12px;
    --radius-lg: 16px;
    --radius-full: 9999px;
    --shadow-soft: 0 10px 25px -5px rgba(0, 0, 0, 0.4), 0 8px 10px -6px rgba(0, 0, 0, 0.4);
    --shadow-glow: 0 0 20px -3px rgba(56, 189, 248, 0.25);
  }

  [data-theme="light"] {
    --bg-primary: #F1F5F9;
    --bg-secondary: #E2E8F0;
    --bg-card: #FFFFFF;
    --bg-card-hover: #F8FAFC;
    --border-color: #CBD5E1;
    --border-highlight: #94A3B8;
    --text-main: #0F172A;
    --text-muted: #334155;
    --text-subtle: #475569;
    --shadow-soft: 0 4px 6px -1px rgba(0, 0, 0, 0.07), 0 2px 4px -2px rgba(0, 0, 0, 0.05);
  }

  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    background: var(--bg-primary);
    color: var(--text-main);
    min-height: 100vh;
    line-height: 1.5;
    transition: background 0.3s ease, color 0.3s ease;
  }

  /* Sticky Top Header */
  .header {
    background: rgba(14, 26, 44, 0.9);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    border-bottom: 1px solid var(--border-color);
    position: sticky;
    top: 0;
    z-index: 100;
    padding: 14px 20px;
  }
  [data-theme="light"] .header {
    background: rgba(248, 250, 252, 0.92);
  }
  .header-inner {
    max-width: 1140px;
    margin: 0 auto;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 16px;
    flex-wrap: wrap;
  }
  .brand-area {
    display: flex;
    align-items: center;
    gap: 12px;
  }
  .brand-logo-pill {
    background: linear-gradient(135deg, #2563EB, #06B6D4);
    color: #fff;
    font-weight: 800;
    font-size: 13px;
    letter-spacing: 0.5px;
    padding: 5px 12px;
    border-radius: var(--radius-full);
    text-decoration: none;
    box-shadow: 0 2px 10px rgba(37, 99, 235, 0.3);
  }
  .header-titles h1 {
    font-size: 17px;
    font-weight: 800;
    color: var(--text-main);
    line-height: 1.2;
  }
  .header-titles p {
    font-size: 11.5px;
    color: var(--text-muted);
  }

  /* Progress Display */
  .top-progress-box {
    display: flex;
    align-items: center;
    gap: 14px;
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid var(--border-color);
    padding: 6px 14px;
    border-radius: var(--radius-full);
  }
  .progress-bar-wrap {
    width: 130px;
    height: 7px;
    background: rgba(255, 255, 255, 0.1);
    border-radius: var(--radius-full);
    overflow: hidden;
  }
  .progress-bar-fill {
    height: 100%;
    width: 0%;
    background: linear-gradient(90deg, var(--accent-blue), var(--accent-emerald));
    border-radius: var(--radius-full);
    transition: width 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  }
  .progress-stat {
    display: flex;
    flex-direction: column;
    align-items: flex-end;
  }
  .progress-stat .val {
    font-size: 13px;
    font-weight: 800;
    font-family: 'JetBrains Mono', monospace;
    color: var(--accent-emerald);
    line-height: 1;
  }
  .progress-stat .lbl {
    font-size: 9.5px;
    color: var(--text-subtle);
    margin-top: 2px;
  }

  /* Header Controls */
  .header-controls {
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .btn-action {
    background: rgba(255, 255, 255, 0.04);
    border: 1px solid var(--border-color);
    color: var(--text-main);
    padding: 6px 12px;
    border-radius: var(--radius-md);
    font-size: 12px;
    font-weight: 600;
    cursor: pointer;
    display: inline-flex;
    align-items: center;
    gap: 6px;
    transition: all 0.2s;
    text-decoration: none;
  }
  .btn-action:hover {
    background: rgba(255, 255, 255, 0.09);
    border-color: var(--border-highlight);
    transform: translateY(-1px);
  }

  /* Main Container */
  .main-container {
    max-width: 1140px;
    margin: 0 auto;
    padding: 24px 20px 60px;
  }

  /* Hero Section */
  .hero-banner {
    background: linear-gradient(135deg, rgba(30, 58, 102, 0.4) 0%, rgba(14, 26, 44, 0.7) 100%);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-lg);
    padding: 24px 28px;
    margin-bottom: 24px;
    position: relative;
    overflow: hidden;
    box-shadow: var(--shadow-soft);
  }
  [data-theme="light"] .hero-banner {
    background: #FFFFFF;
    border: 1.5px solid #CBD5E1;
    box-shadow: 0 4px 12px -2px rgba(0, 0, 0, 0.06);
  }
  .hero-banner::after {
    content: '';
    position: absolute;
    top: -50px;
    right: -50px;
    width: 220px;
    height: 220px;
    background: radial-gradient(circle, rgba(56, 189, 248, 0.15) 0%, transparent 70%);
    pointer-events: none;
  }
  [data-theme="light"] .hero-banner::after {
    background: radial-gradient(circle, rgba(2, 132, 199, 0.08) 0%, transparent 70%);
  }
  .hero-badge {
    display: inline-block;
    font-size: 10.5px;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    color: #38BDF8;
    background: rgba(56, 189, 248, 0.12);
    border: 1px solid rgba(56, 189, 248, 0.3);
    padding: 3px 10px;
    border-radius: var(--radius-full);
    margin-bottom: 10px;
  }
  [data-theme="light"] .hero-badge {
    color: #0369A1;
    background: #E0F2FE;
    border-color: #BAE6FD;
  }
  .hero-title {
    font-size: 26px;
    font-weight: 800;
    color: var(--text-main);
    letter-spacing: -0.5px;
    margin-bottom: 8px;
  }
  .hero-desc {
    font-size: 13.5px;
    color: var(--text-muted);
    max-width: 760px;
    line-height: 1.6;
    margin-bottom: 18px;
  }
  .hero-stats-row {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
  }
  .hero-stat-pill {
    background: rgba(0, 0, 0, 0.25);
    border: 1px solid var(--border-color);
    padding: 6px 14px;
    border-radius: var(--radius-full);
    font-size: 12px;
    display: flex;
    align-items: center;
    gap: 8px;
  }
  [data-theme="light"] .hero-stat-pill {
    background: #F8FAFC;
    border-color: #CBD5E1;
    color: #334155;
  }
  .hero-stat-pill strong {
    color: var(--text-main);
    font-weight: 700;
  }

  /* Control Toolbar */
  .toolbar-card {
    background: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-md);
    padding: 14px 18px;
    margin-bottom: 24px;
    display: flex;
    flex-direction: column;
    gap: 14px;
    box-shadow: var(--shadow-soft);
  }
  .toolbar-top {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
    align-items: center;
    justify-content: space-between;
  }
  .search-wrapper {
    flex: 1;
    min-width: 260px;
    position: relative;
  }
  .search-icon {
    position: absolute;
    left: 14px;
    top: 50%;
    transform: translateY(-50%);
    color: var(--text-subtle);
    font-size: 14px;
  }
  .search-input {
    width: 100%;
    background: rgba(255, 255, 255, 0.04);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-full);
    padding: 9px 16px 9px 38px;
    font-size: 13px;
    color: var(--text-main);
    outline: none;
    transition: all 0.2s ease;
    font-family: inherit;
  }
  [data-theme="light"] .search-input {
    background: #fff;
  }
  .search-input:focus {
    border-color: var(--accent-blue);
    background: rgba(255, 255, 255, 0.07);
    box-shadow: 0 0 0 3px rgba(56, 189, 248, 0.15);
  }
  .status-filters {
    display: flex;
    gap: 6px;
    flex-wrap: wrap;
  }
  .filter-btn {
    background: rgba(255, 255, 255, 0.04);
    border: 1px solid var(--border-color);
    color: var(--text-muted);
    font-size: 12px;
    font-weight: 600;
    padding: 7px 14px;
    border-radius: var(--radius-full);
    cursor: pointer;
    transition: all 0.15s;
    font-family: inherit;
  }
  .filter-btn:hover {
    color: var(--text-main);
    background: rgba(255, 255, 255, 0.08);
  }
  .filter-btn.active {
    background: #2563EB;
    border-color: #2563EB;
    color: #fff;
    box-shadow: 0 2px 8px rgba(37, 99, 235, 0.4);
  }

  /* Unit Navigation Tabs / Strip */
  .unit-nav-strip {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    align-items: center;
    padding-top: 6px;
    border-top: 1px solid rgba(255, 255, 255, 0.06);
  }
  .unit-chip {
    font-size: 12.5px;
    font-weight: 700;
    padding: 8px 16px;
    border-radius: var(--radius-full);
    text-decoration: none;
    cursor: pointer;
    border: 1.5px solid;
    background: transparent;
    transition: all 0.2s ease;
    display: inline-flex;
    align-items: center;
    gap: 8px;
  }
  .unit-chip:hover {
    transform: translateY(-1px);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
  }
  .unit-chip.active {
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.4);
    transform: translateY(-1px);
  }

  /* Unit Container Section */
  .unit-section {
    margin-bottom: 24px;
    display: none; /* Only active unit is shown */
  }
  .unit-section.active-unit {
    display: block;
    animation: fadeInUnit 0.25s ease forwards;
  }
  @keyframes fadeInUnit {
    from { opacity: 0; transform: translateY(6px); }
    to { opacity: 1; transform: translateY(0); }
  }

  .unit-header-card {
    background: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-md) var(--radius-md) 0 0;
    padding: 16px 20px;
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: space-between;
    gap: 12px;
    position: sticky;
    top: 72px;
    z-index: 10;
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
  }
  .unit-title-group {
    display: flex;
    align-items: center;
    gap: 12px;
  }
  .unit-tag {
    font-size: 11px;
    font-weight: 800;
    padding: 3px 8px;
    border-radius: var(--radius-sm);
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }
  .unit-title-text {
    font-size: 17px;
    font-weight: 800;
    color: var(--text-main);
  }
  .unit-progress-display {
    display: flex;
    align-items: center;
    gap: 12px;
  }
  .unit-progress-text {
    font-size: 12px;
    font-weight: 700;
    color: var(--text-muted);
  }

  /* Subject Cards Grid */
  .subjects-container {
    display: flex;
    flex-direction: column;
    gap: 18px;
    margin-top: 14px;
  }
  .subject-card {
    background: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-md);
    overflow: hidden;
    box-shadow: var(--shadow-soft);
    transition: border-color 0.2s ease;
  }
  .subject-card:hover {
    border-color: var(--border-highlight);
  }
  .subject-card-hdr {
    padding: 12px 18px;
    background: rgba(255, 255, 255, 0.02);
    border-bottom: 1px solid var(--border-color);
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: space-between;
    gap: 12px;
  }
  .subject-name-area {
    display: flex;
    align-items: center;
    gap: 10px;
  }
  .subject-color-bar {
    width: 4px;
    height: 18px;
    border-radius: 2px;
  }
  .subject-name {
    font-size: 15px;
    font-weight: 700;
    color: var(--text-main);
  }
  .subject-badge-count {
    font-size: 11px;
    color: var(--text-muted);
    background: rgba(255, 255, 255, 0.06);
    padding: 2px 8px;
    border-radius: var(--radius-full);
    font-weight: 600;
  }
  .subject-actions {
    display: flex;
    align-items: center;
    gap: 10px;
  }
  .btn-mark-all {
    background: transparent;
    border: none;
    color: var(--accent-blue);
    font-size: 11.5px;
    font-weight: 600;
    cursor: pointer;
    padding: 3px 8px;
    border-radius: var(--radius-sm);
    transition: background 0.15s;
  }
  .btn-mark-all:hover {
    background: rgba(56, 189, 248, 0.12);
  }
  .subject-progress-mini {
    font-size: 12px;
    font-weight: 700;
    color: var(--text-muted);
    font-family: 'JetBrains Mono', monospace;
  }

  /* Topics Checklist List */
  .topics-list {
    padding: 10px 12px;
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
    gap: 8px;
  }
  .topic-item {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 10px 14px;
    border-radius: var(--radius-sm);
    background: rgba(255, 255, 255, 0.02);
    border: 1px solid rgba(255, 255, 255, 0.04);
    transition: all 0.15s ease;
    position: relative;
    cursor: pointer;
  }
  [data-theme="light"] .topic-item {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
  }
  [data-theme="light"] .topic-item:hover {
    background: #F8FAFC;
    border-color: #CBD5E1;
  }
  [data-theme="light"] .topic-item.completed {
    background: #F0FDF4;
    border-color: #86EFAC;
  }
  .topic-item:hover {
    background: var(--bg-card-hover);
    border-color: rgba(255, 255, 255, 0.1);
  }
  .topic-item.completed {
    background: rgba(16, 185, 129, 0.06);
    border-color: rgba(16, 185, 129, 0.2);
  }

  /* Custom Tick Box Checkbox */
  .custom-checkbox {
    position: relative;
    width: 20px;
    height: 20px;
    flex-shrink: 0;
  }
  .custom-checkbox input {
    opacity: 0;
    width: 100%;
    height: 100%;
    cursor: pointer;
    position: absolute;
    z-index: 2;
  }
  .checkmark {
    position: absolute;
    top: 0;
    left: 0;
    width: 20px;
    height: 20px;
    background: rgba(0, 0, 0, 0.35);
    border: 1.5px solid var(--border-color);
    border-radius: 5px;
    transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
    display: flex;
    align-items: center;
    justify-content: center;
  }
  [data-theme="light"] .checkmark {
    background: #FFFFFF;
    border: 1.5px solid #94A3B8;
  }
  [data-theme="light"] .custom-checkbox input:checked ~ .checkmark {
    background: #059669;
    border-color: #059669;
    box-shadow: 0 0 8px rgba(5, 150, 105, 0.25);
  }
  .custom-checkbox input:checked ~ .checkmark {
    background: var(--accent-emerald);
    border-color: var(--accent-emerald);
    box-shadow: 0 0 10px rgba(16, 185, 129, 0.4);
  }
  .checkmark::after {
    content: '';
    display: none;
    width: 5px;
    height: 9px;
    border: solid #fff;
    border-width: 0 2px 2px 0;
    transform: rotate(45deg);
    margin-bottom: 2px;
  }
  .custom-checkbox input:checked ~ .checkmark::after {
    display: block;
  }

  /* Topic Label & Path */
  .topic-info {
    flex: 1;
    min-width: 0;
  }
  .topic-title {
    font-size: 13px;
    font-weight: 600;
    color: var(--text-main);
    line-height: 1.4;
    transition: color 0.15s;
    word-break: break-word;
  }
  .topic-item.completed .topic-title {
    color: var(--text-muted);
    text-decoration: line-through;
    opacity: 0.85;
  }
  .topic-meta-row {
    display: flex;
    align-items: center;
    gap: 8px;
    margin-top: 3px;
  }
  .topic-folder-tag {
    font-family: 'JetBrains Mono', monospace;
    font-size: 10.5px;
    font-weight: 600;
    color: var(--text-subtle);
    background: rgba(255, 255, 255, 0.04);
    padding: 2px 7px;
    border-radius: 4px;
    max-width: 260px;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }
  [data-theme="light"] .topic-folder-tag {
    color: #475569;
    background: #F1F5F9;
    border: 1px solid #E2E8F0;
  }

  /* Bottom Unit Switcher Bar */
  .unit-bottom-nav {
    margin-top: 32px;
    background: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-lg);
    padding: 16px 20px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 16px;
    box-shadow: var(--shadow-soft);
  }
  .nav-unit-btn {
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid var(--border-color);
    color: var(--text-main);
    padding: 10px 20px;
    border-radius: var(--radius-full);
    font-size: 13px;
    font-weight: 700;
    cursor: pointer;
    display: inline-flex;
    align-items: center;
    gap: 8px;
    transition: all 0.2s ease;
    font-family: inherit;
    text-decoration: none;
  }
  .nav-unit-btn:hover {
    background: var(--border-highlight);
    color: #fff;
    transform: translateY(-1px);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.25);
  }
  .nav-unit-btn.next {
    background: linear-gradient(135deg, #2563EB, #06B6D4);
    border-color: transparent;
    color: #fff;
    margin-left: auto;
  }
  .nav-unit-btn.next:hover {
    box-shadow: 0 4px 16px rgba(37, 99, 235, 0.4);
  }
  .nav-unit-btn.disabled {
    opacity: 0.4;
    pointer-events: none;
  }

  /* No Results Message */
  .no-results-card {
    display: none;
    text-align: center;
    padding: 60px 20px;
    background: var(--bg-card);
    border: 1px dashed var(--border-color);
    border-radius: var(--radius-lg);
    margin: 30px 0;
  }
  .no-results-card h3 {
    font-size: 18px;
    color: var(--text-main);
    margin-bottom: 6px;
  }
  .no-results-card p {
    font-size: 13px;
    color: var(--text-muted);
  }

  /* Toast Notification */
  .toast {
    position: fixed;
    bottom: 24px;
    right: 24px;
    background: rgba(16, 29, 49, 0.95);
    border: 1px solid var(--border-highlight);
    color: #fff;
    padding: 12px 20px;
    border-radius: var(--radius-md);
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
    font-size: 13px;
    font-weight: 600;
    display: flex;
    align-items: center;
    gap: 10px;
    z-index: 1000;
    transform: translateY(100px);
    opacity: 0;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    pointer-events: none;
  }
  .toast.show {
    transform: translateY(0);
    opacity: 1;
    pointer-events: auto;
  }

  /* Footer */
  .site-footer {
    border-top: 1px solid var(--border-color);
    padding: 30px 20px 50px;
    text-align: center;
    font-size: 12px;
    color: var(--text-subtle);
    max-width: 1140px;
    margin: 0 auto;
  }
  .site-footer a {
    color: var(--accent-blue);
    text-decoration: none;
  }
  .site-footer a:hover {
    text-decoration: underline;
  }

  .hidden { display: none !important; }

  @media (max-width: 768px) {
    .header-inner { flex-direction: column; align-items: stretch; }
    .top-progress-box { justify-content: space-between; }
    .hero-title { font-size: 22px; }
    .topics-list { grid-template-columns: 1fr; }
    .unit-header-card { top: 120px; }
    .unit-bottom-nav { flex-direction: column; }
    .nav-unit-btn { width: 100%; justify-content: center; }
  }
</style>
</head>
<body>

<!-- Header -->
<header class="header">
  <div class="header-inner">
    <div class="brand-area">
      <a href="/" class="brand-logo-pill">SJMaths</a>
      <div class="header-titles">
        <h1>CSIR-NET Mathematics Hub</h1>
        <p>Curriculum topic tracker &amp; progress checklist · 333 core topics</p>
      </div>
    </div>

    <!-- Progress Indicator -->
    <div class="top-progress-box" id="top-progress-box">
      <div class="progress-bar-wrap">
        <div class="progress-bar-fill" id="global-progress-bar"></div>
      </div>
      <div class="progress-stat">
        <div class="val"><span id="completed-count">0</span> / <span id="total-count">332</span></div>
        <div class="lbl"><span id="percent-label">0%</span> Completed</div>
      </div>
    </div>

    <!-- Header Actions -->
    <div class="header-controls">
      <button class="btn-action" id="btn-theme-toggle" title="Toggle Dark/Light Mode">
        <span id="theme-icon">🌓</span> Theme
      </button>
      <button class="btn-action" id="btn-reset-progress" title="Reset Progress Checklist">
        <span>↺</span> Reset
      </button>
      <a href="/" class="btn-action">
        <span>←</span> Home
      </a>
    </div>
  </div>
</header>

<main class="main-container">

  <!-- Hero Section -->
  <section class="hero-banner">
    <div class="hero-content">
      <div class="hero-badge">Official Syllabus Tracker</div>
      <h2 class="hero-title">CSIR-UGC NET Mathematical Sciences</h2>
      <p class="hero-desc">
        Comprehensive subject-wise checklist mapping every curriculum module to its dedicated subject branch. Use the tick boxes to keep track of topics you have revised, solved previous year questions (PYQs) for, or mastered.
      </p>
      <div class="hero-stats-row">
        <div class="hero-stat-pill">
          <span>📚 Total Topics:</span> <strong id="stat-total">332</strong>
        </div>
        <div class="hero-stat-pill">
          <span>🏛 Units:</span> <strong>4 Units (12 Subject Disciplines)</strong>
        </div>
        <div class="hero-stat-pill">
          <span>✅ Completed:</span> <strong id="stat-completed" style="color: var(--accent-emerald);">0</strong>
        </div>
        <div class="hero-stat-pill">
          <span>⏳ Remaining:</span> <strong id="stat-remaining" style="color: var(--accent-amber);">332</strong>
        </div>
      </div>
    </div>
  </section>

  <!-- Control Toolbar -->
  <div class="toolbar-card">
    <div class="toolbar-top">
      <div class="search-wrapper">
        <span class="search-icon">🔍</span>
        <input type="search" id="search-input" class="search-input" placeholder="Search topics (e.g., Cauchy, Sylow, Lebesgue, Wave, Simplex, Green)..." autocomplete="off">
      </div>
      <div class="status-filters">
        <button class="filter-btn active" data-status="all">All (<span id="btn-count-all">332</span>)</button>
        <button class="filter-btn" data-status="completed">Done (<span id="btn-count-done">0</span>)</button>
        <button class="filter-btn" data-status="remaining">Pending (<span id="btn-count-rem">332</span>)</button>
      </div>
    </div>

    <!-- Unit Jump Tabs -->
    <div class="unit-nav-strip" id="unit-nav-strip">
      <!-- Generated dynamically -->
    </div>
  </div>

  <!-- Content Container for Units & Subject Cards -->
  <div id="units-content"></div>

  <!-- Empty Search Result Card -->
  <div class="no-results-card" id="no-results-card">
    <h3>No matching topics found</h3>
    <p>Try searching for a different keyword or clear the active filter.</p>
  </div>

</main>

<div class="toast" id="toast-msg">Notification message</div>

<footer class="site-footer">
  <p>CSIR-UGC NET Mathematics Subject Hub · All 332 curriculum modules mapped to subject repositories.</p>
  <p style="margin-top: 6px;"><a href="javascript:void(0)" id="back-to-top">Back to Top ↑</a> · <a href="/">SJMaths Home</a></p>
</footer>

<script>
// Load Dataset
const DATA = ${dataJson};

const UNITS_META = {
  'I': {
    name: 'Unit I — Analysis & Linear Algebra',
    colorDark: '#38BDF8',
    colorLight: '#0369A1',
    bgBadgeDark: 'rgba(56, 189, 248, 0.15)',
    bgBadgeLight: '#E0F2FE',
    subjects: ['Real Analysis', 'Linear Algebra']
  },
  'II': {
    name: 'Unit II — Complex Analysis, Algebra & Topology',
    colorDark: '#A78BFA',
    colorLight: '#6D28D9',
    bgBadgeDark: 'rgba(167, 139, 250, 0.15)',
    bgBadgeLight: '#EDE9FE',
    subjects: ['Complex Analysis', 'Algebra (Abstract & Number Theory)', 'Topology']
  },
  'III': {
    name: 'Unit III — ODE, PDE, Numerical & Applied',
    colorDark: '#34D399',
    colorLight: '#047857',
    bgBadgeDark: 'rgba(52, 211, 153, 0.15)',
    bgBadgeLight: '#D1FAE5',
    subjects: [
      'Ordinary Differential Equations (ODE)',
      'Partial Differential Equations (PDE)',
      'Numerical Analysis',
      'Calculus of Variations',
      'Linear Integral Equations',
      'Classical Mechanics'
    ]
  },
  'IV': {
    name: 'Unit IV — Statistics & Operations Research',
    colorDark: '#F472B6',
    colorLight: '#BE185D',
    bgBadgeDark: 'rgba(244, 114, 182, 0.15)',
    bgBadgeLight: '#FCE7F3',
    subjects: ['Mathematical Statistics & OR']
  }
};

const SUBJECT_COLORS = {
  'Real Analysis': { dark: '#38BDF8', light: '#0369A1' },
  'Linear Algebra': { dark: '#60A5FA', light: '#1D4ED8' },
  'Complex Analysis': { dark: '#C084FC', light: '#7E22CE' },
  'Algebra (Abstract & Number Theory)': { dark: '#A78BFA', light: '#6D28D9' },
  'Topology': { dark: '#818CF8', light: '#4338CA' },
  'Ordinary Differential Equations (ODE)': { dark: '#34D399', light: '#047857' },
  'Partial Differential Equations (PDE)': { dark: '#2DD4BF', light: '#0F766E' },
  'Numerical Analysis': { dark: '#FBBF24', light: '#B45309' },
  'Calculus of Variations': { dark: '#FB923C', light: '#C2410C' },
  'Linear Integral Equations': { dark: '#A3E635', light: '#4D7C0F' },
  'Classical Mechanics': { dark: '#F472B6', light: '#BE185D' },
  'Mathematical Statistics & OR': { dark: '#EC4899', light: '#9D174D' }
};

function getUnitColor(uKey) {
  const isLight = document.documentElement.getAttribute('data-theme') === 'light';
  return isLight ? UNITS_META[uKey].colorLight : UNITS_META[uKey].colorDark;
}
function getUnitBadge(uKey) {
  const isLight = document.documentElement.getAttribute('data-theme') === 'light';
  return isLight ? UNITS_META[uKey].bgBadgeLight : UNITS_META[uKey].bgBadgeDark;
}
function getSubjectColor(subjName) {
  const isLight = document.documentElement.getAttribute('data-theme') === 'light';
  const sc = SUBJECT_COLORS[subjName];
  if (!sc) return getUnitColor(activeUnitKey);
  return isLight ? sc.light : sc.dark;
}

const UNIT_KEYS = ['I', 'II', 'III', 'IV'];
let activeUnitKey = 'I';

// Storage Key
const STORAGE_KEY = 'sj_csir_net_math_progress_v2';
let completedIds = new Set();

try {
  const saved = localStorage.getItem(STORAGE_KEY);
  if (saved) {
    completedIds = new Set(JSON.parse(saved));
  }
} catch (e) {
  console.error('Error loading progress:', e);
}

function saveProgress() {
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(Array.from(completedIds)));
  } catch (e) {
    console.error('Error saving progress:', e);
  }
}

// Toast Helper
function showToast(msg) {
  const toast = document.getElementById('toast-msg');
  toast.textContent = msg;
  toast.classList.add('show');
  setTimeout(() => toast.classList.remove('show'), 2600);
}

// Group Data by Unit -> Subject
const grouped = {};
Object.keys(UNITS_META).forEach(u => {
  grouped[u] = {};
  UNITS_META[u].subjects.forEach(subj => {
    grouped[u][subj] = [];
  });
});

DATA.forEach(item => {
  if (grouped[item.u] && grouped[item.u][item.c]) {
    grouped[item.u][item.c].push(item);
  }
});

// Render DOM
const unitsContent = document.getElementById('units-content');
const unitNavStrip = document.getElementById('unit-nav-strip');

UNIT_KEYS.forEach((uKey, idx) => {
  const uMeta = UNITS_META[uKey];
  const uSubjects = grouped[uKey];
  const uTopics = DATA.filter(d => d.u === uKey);

  // Top Nav Tab
  const navChip = document.createElement('button');
  navChip.type = 'button';
  navChip.className = 'unit-chip' + (uKey === activeUnitKey ? ' active' : '');
  navChip.id = 'chip-unit-' + uKey;
  navChip.style.borderColor = getUnitColor(uKey);
  navChip.style.color = (uKey === activeUnitKey) ? '#fff' : getUnitColor(uKey);
  if (uKey === activeUnitKey) {
    navChip.style.background = getUnitColor(uKey);
  }
  navChip.innerHTML = '<span>●</span> Unit ' + uKey + ' (' + uTopics.length + ')';
  navChip.addEventListener('click', () => {
    switchUnit(uKey);
  });
  unitNavStrip.appendChild(navChip);

  // Unit Section
  const section = document.createElement('section');
  section.className = 'unit-section' + (uKey === activeUnitKey ? ' active-unit' : '');
  section.id = 'unit-' + uKey;

  // Unit Header Card
  const uHeader = document.createElement('div');
  uHeader.className = 'unit-header-card';
  uHeader.style.borderLeft = '4px solid ' + getUnitColor(uKey);
  uHeader.innerHTML = \`
    <div class="unit-title-group">
      <span class="unit-tag" id="tag-unit-\${uKey}" style="background:\${getUnitBadge(uKey)}; color:\${getUnitColor(uKey)};">Unit \${uKey}</span>
      <h3 class="unit-title-text">\${uMeta.name}</h3>
    </div>
    <div class="unit-progress-display">
      <span class="unit-progress-text" id="unit-\${uKey}-progress">0 / \${uTopics.length} completed</span>
    </div>
  \`;
  section.appendChild(uHeader);

  // Subjects Container
  const subjectsContainer = document.createElement('div');
  subjectsContainer.className = 'subjects-container';

  Object.keys(uSubjects).forEach(subjName => {
    const topics = uSubjects[subjName];
    if (!topics || topics.length === 0) return;

    const subjCard = document.createElement('div');
    subjCard.className = 'subject-card';
    subjCard.dataset.subject = subjName;

    // Subject Card Header
    const subjHdr = document.createElement('div');
    subjHdr.className = 'subject-card-hdr';
    subjHdr.innerHTML = \`
      <div class="subject-name-area">
        <div class="subject-color-bar" style="background:\${getSubjectColor(subjName)};"></div>
        <div class="subject-name">\${subjName}</div>
        <span class="subject-badge-count">\${topics.length} topics</span>
      </div>
      <div class="subject-actions">
        <span class="subject-progress-mini" id="subj-\${slugify(subjName)}-prog">0/\${topics.length}</span>
        <button type="button" class="btn-mark-all" data-action="toggle-subj" data-subj="\${subjName}">Check All</button>
      </div>
    \`;

    // Topics Checklist
    const topicsList = document.createElement('div');
    topicsList.className = 'topics-list';

    topics.forEach(t => {
      const isChecked = completedIds.has(t.id);
      const itemEl = document.createElement('div');
      itemEl.className = 'topic-item' + (isChecked ? ' completed' : '');
      itemEl.id = 'topic-item-' + t.id;
      itemEl.dataset.id = t.id;
      itemEl.dataset.unit = t.u;
      itemEl.dataset.subject = t.c;

      itemEl.innerHTML = \`
        <label class="custom-checkbox" title="Mark completed">
          <input type="checkbox" id="chk-\${t.id}" \${isChecked ? 'checked' : ''}>
          <span class="checkmark"></span>
        </label>
        <div class="topic-info">
          <div class="topic-title">\${escapeHtml(t.t)}</div>
          <div class="topic-meta-row">
            <span class="topic-folder-tag">\${t.slug}</span>
          </div>
        </div>
      \`;

      // Event listener
      const checkbox = itemEl.querySelector('input[type="checkbox"]');
      checkbox.addEventListener('change', (e) => {
        e.stopPropagation();
        toggleTopic(t.id, checkbox.checked);
      });

      itemEl.addEventListener('click', (e) => {
        if (e.target.tagName.toLowerCase() === 'input') return;
        checkbox.checked = !checkbox.checked;
        toggleTopic(t.id, checkbox.checked);
      });

      topicsList.appendChild(itemEl);
    });

    subjCard.appendChild(subjHdr);
    subjCard.appendChild(topicsList);
    subjectsContainer.appendChild(subjCard);
  });

  section.appendChild(subjectsContainer);

  // Bottom Navigation Bar to Switch Units
  const bottomNav = document.createElement('div');
  bottomNav.className = 'unit-bottom-nav';

  const prevKey = idx > 0 ? UNIT_KEYS[idx - 1] : null;
  const nextKey = idx < UNIT_KEYS.length - 1 ? UNIT_KEYS[idx + 1] : null;

  let bottomNavHtml = '';
  if (prevKey) {
    bottomNavHtml += \`<button type="button" class="nav-unit-btn prev" onclick="switchUnit('\${prevKey}')">← Previous: Unit \${prevKey}</button>\`;
  } else {
    bottomNavHtml += \`<div></div>\`;
  }

  if (nextKey) {
    bottomNavHtml += \`<button type="button" class="nav-unit-btn next" onclick="switchUnit('\${nextKey}')">Proceed to Unit \${nextKey} →</button>\`;
  } else {
    bottomNavHtml += \`<button type="button" class="nav-unit-btn next" onclick="window.scrollTo({top:0, behavior:'smooth'})">Back to Top ↑</button>\`;
  }

  bottomNav.innerHTML = bottomNavHtml;
  section.appendChild(bottomNav);

  unitsContent.appendChild(section);
});

// Unit Switching Logic
function switchUnit(uKey) {
  activeUnitKey = uKey;

  // Update tabs
  UNIT_KEYS.forEach(k => {
    const chip = document.getElementById('chip-unit-' + k);
    const sec = document.getElementById('unit-' + k);
    const meta = UNITS_META[k];
    const isCur = (k === uKey);

    const uCol = getUnitColor(k);
    if (chip) {
      chip.classList.toggle('active', isCur);
      chip.style.borderColor = uCol;
      chip.style.color = isCur ? '#fff' : uCol;
      chip.style.background = isCur ? uCol : 'transparent';
    }
    const tag = document.getElementById('tag-unit-' + k);
    if (tag) {
      tag.style.background = getUnitBadge(k);
      tag.style.color = uCol;
    }
    if (sec) {
      sec.classList.toggle('active-unit', isCur);
    }
  });

  // Update URL hash without harsh reload
  if (history.replaceState) {
    history.replaceState(null, null, '#unit-' + uKey);
  }

  // Scroll smoothly to toolbar
  const toolbar = document.querySelector('.toolbar-card');
  if (toolbar) {
    const y = toolbar.getBoundingClientRect().top + window.pageYOffset - 80;
    window.scrollTo({ top: y, behavior: 'smooth' });
  }
}

// Check initial hash in URL
if (window.location.hash) {
  const hashKey = window.location.hash.replace('#unit-', '').toUpperCase();
  if (UNIT_KEYS.includes(hashKey)) {
    activeUnitKey = hashKey;
  }
}

function slugify(s) {
  return s.toLowerCase().replace(/[^a-z0-9]+/g, '-');
}

function escapeHtml(s) {
  return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
}

// Toggle Topic Status
function toggleTopic(id, isDone) {
  if (isDone) {
    completedIds.add(id);
  } else {
    completedIds.delete(id);
  }
  const itemEl = document.getElementById('topic-item-' + id);
  if (itemEl) {
    itemEl.classList.toggle('completed', isDone);
    const chk = itemEl.querySelector('input');
    if (chk) chk.checked = isDone;
  }
  saveProgress();
  updateMetrics();
  filterVisibleTopics();
}

// Update All Progress Meters
function updateMetrics() {
  const total = DATA.length;
  const done = completedIds.size;
  const rem = total - done;
  const pct = Math.round((done / total) * 100);

  // Global Header
  document.getElementById('completed-count').textContent = done;
  document.getElementById('total-count').textContent = total;
  document.getElementById('percent-label').textContent = pct + '%';
  document.getElementById('global-progress-bar').style.width = pct + '%';

  // Hero Stats
  document.getElementById('stat-total').textContent = total;
  document.getElementById('stat-completed').textContent = done;
  document.getElementById('stat-remaining').textContent = rem;

  // Filter Button Counts
  document.getElementById('btn-count-all').textContent = total;
  document.getElementById('btn-count-done').textContent = done;
  document.getElementById('btn-count-rem').textContent = rem;

  // Per-Unit Progress
  Object.keys(UNITS_META).forEach(uKey => {
    const uTopics = DATA.filter(d => d.u === uKey);
    const uDone = uTopics.filter(d => completedIds.has(d.id)).length;
    const el = document.getElementById('unit-' + uKey + '-progress');
    if (el) {
      el.textContent = uDone + ' / ' + uTopics.length + ' completed (' + Math.round((uDone / uTopics.length) * 100) + '%)';
    }
  });

  // Per-Subject Progress
  Object.keys(UNITS_META).forEach(uKey => {
    UNITS_META[uKey].subjects.forEach(subj => {
      const sTopics = DATA.filter(d => d.c === subj);
      const sDone = sTopics.filter(d => completedIds.has(d.id)).length;
      const el = document.getElementById('subj-' + slugify(subj) + '-prog');
      if (el) {
        el.textContent = sDone + '/' + sTopics.length;
      }
      // Update check all button label
      const btn = document.querySelector('[data-action="toggle-subj"][data-subj="' + subj + '"]');
      if (btn) {
        btn.textContent = (sDone === sTopics.length && sTopics.length > 0) ? 'Uncheck All' : 'Check All';
      }
    });
  });
}

// Batch Subject Toggle
document.querySelectorAll('[data-action="toggle-subj"]').forEach(btn => {
  btn.addEventListener('click', (e) => {
    e.stopPropagation();
    const subj = btn.dataset.subj;
    const sTopics = DATA.filter(d => d.c === subj);
    const allDone = sTopics.every(d => completedIds.has(d.id));

    sTopics.forEach(t => {
      if (allDone) {
        completedIds.delete(t.id);
      } else {
        completedIds.add(t.id);
      }
      const el = document.getElementById('topic-item-' + t.id);
      if (el) {
        el.classList.toggle('completed', !allDone);
        el.querySelector('input').checked = !allDone;
      }
    });

    saveProgress();
    updateMetrics();
    filterVisibleTopics();
    showToast((allDone ? 'Unchecked all in ' : 'Marked all completed in ') + subj);
  });
});

// Search & Status Filters
const searchInput = document.getElementById('search-input');
const statusButtons = document.querySelectorAll('.filter-btn');
const noResultsCard = document.getElementById('no-results-card');

let currentStatusFilter = 'all';

statusButtons.forEach(btn => {
  btn.addEventListener('click', () => {
    statusButtons.forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    currentStatusFilter = btn.dataset.status;
    filterVisibleTopics();
  });
});

searchInput.addEventListener('input', () => {
  filterVisibleTopics();
});

function filterVisibleTopics() {
  const query = searchInput.value.trim().toLowerCase();
  let totalVisible = 0;

  // If user searches, allow matching topics across units, or restrict to active unit if no query
  document.querySelectorAll('.topic-item').forEach(item => {
    const id = item.dataset.id;
    const isDone = completedIds.has(id);
    const text = item.textContent.toLowerCase();

    // Check status filter
    let statusMatch = true;
    if (currentStatusFilter === 'completed') statusMatch = isDone;
    if (currentStatusFilter === 'remaining') statusMatch = !isDone;

    // Check search query
    const queryMatch = !query || text.indexOf(query) > -1;

    const visible = statusMatch && queryMatch;
    item.classList.toggle('hidden', !visible);
    if (visible) totalVisible++;
  });

  // If searching across all units, show matching unit sections
  if (query) {
    document.querySelectorAll('.unit-section').forEach(sec => {
      const hasVisible = !!sec.querySelector('.topic-item:not(.hidden)');
      sec.style.display = hasVisible ? 'block' : 'none';
    });
  } else {
    // Revert to showing only active unit
    UNIT_KEYS.forEach(k => {
      const sec = document.getElementById('unit-' + k);
      if (sec) sec.style.display = (k === activeUnitKey) ? 'block' : 'none';
    });
  }

  // Hide empty subjects
  document.querySelectorAll('.subject-card').forEach(card => {
    const hasVisible = !!card.querySelector('.topic-item:not(.hidden)');
    card.classList.toggle('hidden', !hasVisible);
  });

  noResultsCard.style.display = (totalVisible === 0) ? 'block' : 'none';
}

// Reset Progress Button
document.getElementById('btn-reset-progress').addEventListener('click', () => {
  if (completedIds.size === 0) {
    showToast('No progress to reset.');
    return;
  }
  if (confirm('Are you sure you want to reset all completed topics?')) {
    completedIds.clear();
    saveProgress();
    document.querySelectorAll('.topic-item').forEach(el => {
      el.classList.remove('completed');
      el.querySelector('input').checked = false;
    });
    updateMetrics();
    filterVisibleTopics();
    showToast('Progress has been reset.');
  }
});

// Theme Toggle
const themeBtn = document.getElementById('btn-theme-toggle');
const themeIcon = document.getElementById('theme-icon');

function setTheme(theme) {
  if (theme === 'light') {
    document.documentElement.setAttribute('data-theme', 'light');
    themeIcon.textContent = '☀️';
  } else {
    document.documentElement.removeAttribute('data-theme');
    themeIcon.textContent = '🌙';
  }
  localStorage.setItem('sj_theme_pref', theme);
  // Re-apply theme-adjusted color accents
  if (typeof switchUnit === 'function') {
    switchUnit(activeUnitKey);
  }
  // Update subject color bars
  document.querySelectorAll('.subject-card').forEach(card => {
    const sName = card.dataset.subject;
    const bar = card.querySelector('.subject-color-bar');
    if (bar && sName) bar.style.background = getSubjectColor(sName);
  });
}

const savedTheme = localStorage.getItem('sj_theme_pref') || 'dark';
setTheme(savedTheme);

themeBtn.addEventListener('click', () => {
  const current = document.documentElement.getAttribute('data-theme') === 'light' ? 'light' : 'dark';
  setTheme(current === 'light' ? 'dark' : 'light');
});

// Back to Top
document.getElementById('back-to-top').addEventListener('click', () => {
  window.scrollTo({ top: 0, behavior: 'smooth' });
});

// Set initial unit display
switchUnit(activeUnitKey);

// Initial Metrics Calculation
updateMetrics();
</script>
</body>
</html>`;

fs.writeFileSync('csir-net/mathematics/index.html', html, 'utf8');
console.log('Successfully updated csir-net/mathematics/index.html with single-unit view & bottom navigation, size:', html.length);
