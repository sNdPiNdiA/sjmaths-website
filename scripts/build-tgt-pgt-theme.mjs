import fs from 'fs';
import path from 'path';
import esbuild from 'esbuild';

const FONT_LINK_SNIPPET = `<!-- Fonts (UPSSSC PET Aesthetic) -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,400..700;1,9..40,400..700&family=Source+Serif+4:ital,opsz,wght@0,8..60,400..700;1,8..60,400..700&display=swap" rel="stylesheet">`;

// Master UPSSSC PET design system for standard tracker pages
const TRACKER_CSS = `/* =============================================================
   SJMaths UP TGT & PGT Unified Tracker Design System
   Matches UPSSSC PET Visual System & Tokens Exactly
   ============================================================= */

@import url('https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,400..700;1,9..40,400..700&family=Source+Serif+4:ital,opsz,wght@0,8..60,400..700;1,8..60,400..700&display=swap');

:root {
  /* Brand (forest green & teal - matches UPSSSC PET) */
  --planner-primary:        #0d9488;
  --planner-primary-dark:   #0f766e;
  --planner-primary-light:  #f0fdfa;
  --planner-primary-glow:   rgba(13, 148, 136, 0.18);
  --planner-primary-soft:   rgba(13, 148, 136, 0.10);
  --planner-brand:          #16634b;
  --planner-brand-light:    #eaf0e7;
  --planner-accent-gradient: linear-gradient(135deg, #16634b, #0d9488);

  /* Page surfaces (warm paper editorial style) */
  --bg:                     #f7f5ef;
  --paper:                  #ffffff;
  --surface:                #fffdf8;
  --softline:               #eeeee5;

  /* Typography */
  --ink:                    #182e26;
  --ink2:                   #3e5047;
  --muted:                  #5d6d63;
  --light:                  #8a9e92;

  /* Borders */
  --line:                   #d9ddd1;
  --line-medium:            #c5cec1;

  /* Exam Overlap Tags & Accents */
  --brand:                  #16634b;
  --brand2:                 #0f766e;
  --primary:                #0d9488;
  --done:                   #0d9488;
  --donebg:                 #f0fdfa;
  --shared:                 #0f766e;
  --sharedbg:               #eaf0e7;
  --only:                   #7c3aed;
  --onlybg:                 #f5f0ff;
  --tgt:                    #b45309;
  --tgtbg:                  #fffbeb;

  /* Shadows & Radii */
  --shadow:                 0 1px 4px rgba(10, 20, 15, 0.06), 0 0 0 1px rgba(13, 148, 136, 0.06);
  --shadow-hover:           0 4px 16px rgba(13, 148, 136, 0.12);
  --card-radius:            10px;
  --r-full:                 9999px;
  --header:                 66px;
}

* {
  box-sizing: border-box;
}

html {
  scroll-behavior: smooth;
}

body {
  margin: 0;
  background: var(--bg);
  color: var(--ink2);
  font-family: 'DM Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  line-height: 1.55;
  -webkit-font-smoothing: antialiased;
}

a {
  color: inherit;
  text-decoration: none;
}

button, input {
  font: inherit;
}

button {
  color: inherit;
}

.wrap {
  width: min(1440px, calc(100% - 32px));
  margin: auto;
}

/* Site Header */
.site-header {
  height: var(--header);
  position: sticky;
  top: 0;
  z-index: 90;
  background: rgba(255, 253, 248, 0.96);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border-bottom: 1px solid var(--line);
}

.header-inner {
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
}

.brand {
  display: flex;
  gap: 11px;
  align-items: center;
  text-decoration: none;
}

.brand-mark {
  width: 38px;
  height: 38px;
  border-radius: 10px;
  background: var(--planner-accent-gradient);
  display: grid;
  place-items: center;
  color: #fff;
  font-weight: 900;
  font-family: 'Times New Roman', 'Cambria Math', serif;
  font-size: 1.65rem;
  font-style: italic;
  line-height: 1;
}

.brand-name {
  display: block;
  font-weight: 750;
  color: var(--ink);
  font-size: 1.05rem;
}

.brand-sub {
  display: block;
  color: var(--muted);
  font-size: 0.68rem;
}

.exam-chip {
  padding: 6px 13px;
  border: 1px solid rgba(22, 99, 75, 0.22);
  border-radius: var(--r-full);
  background: var(--planner-brand-light);
  color: var(--planner-brand);
  font-size: 0.74rem;
  font-weight: 700;
}

/* Hero Section */
.hero {
  padding: 34px 0 22px;
}

.breadcrumb {
  display: flex;
  gap: 7px;
  align-items: center;
  font-size: 0.76rem;
  color: var(--muted);
  margin-bottom: 14px;
}

.breadcrumb a {
  color: var(--planner-primary-dark);
  text-decoration: none;
  font-weight: 500;
}

.breadcrumb a:hover {
  color: var(--primary);
  text-decoration: underline;
}

.hero-grid {
  display: grid;
  grid-template-columns: minmax(0, 1fr) 390px;
  gap: 28px;
  align-items: center;
}

.kicker {
  display: inline-flex;
  align-items: center;
  gap: 9px;
  color: var(--brand);
  font-size: 0.74rem;
  text-transform: uppercase;
  font-weight: 800;
  letter-spacing: 0.08em;
}

.kicker:before {
  content: "";
  width: 26px;
  height: 2px;
  background: currentColor;
  border-radius: var(--r-full);
}

h1 {
  margin: 10px 0 12px;
  font-family: 'Source Serif 4', Georgia, serif;
  font-size: clamp(1.9rem, 3.8vw, 2.9rem);
  font-weight: 600;
  line-height: 1.15;
  letter-spacing: -0.015em;
  color: var(--ink);
  max-width: 980px;
}

.lead {
  margin: 0;
  color: var(--ink2);
  max-width: 950px;
  font-size: 1rem;
  line-height: 1.65;
}

.hero-tags, .hero-stats-row {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
  margin-top: 18px;
}

.tag, .hero-stat-item {
  padding: 6px 12px;
  border: 1px solid var(--line);
  border-radius: var(--r-full);
  background: var(--paper);
  font-size: 0.73rem;
  font-weight: 600;
  color: var(--ink2);
  box-shadow: 0 1px 2px rgba(10, 20, 15, 0.03);
}

.hero-stat-item strong {
  color: var(--planner-primary-dark);
  font-weight: 800;
}

/* Progress Card (UPSSSC PET Aesthetic) */
.progress-card {
  background: var(--paper);
  color: var(--ink);
  border: 1px solid var(--line);
  border-radius: 12px;
  padding: 22px;
  box-shadow: var(--shadow);
  position: relative;
  overflow: hidden;
  transition: box-shadow 0.22s ease;
}

.progress-card:hover {
  box-shadow: var(--shadow-hover);
}

.progress-card:before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 4px;
  height: 100%;
  background: var(--planner-accent-gradient);
}

.progress-label {
  color: var(--muted);
  font-size: 0.72rem;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  font-weight: 700;
}

.progress-row, .progress-top {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  gap: 10px;
  margin: 8px 0 12px;
}

.progress-pct {
  font-family: 'DM Sans', sans-serif;
  font-size: 2.35rem;
  line-height: 1;
  font-weight: 800;
  color: var(--primary);
}

.progress-copy {
  text-align: right;
  color: var(--muted);
  font-size: 0.78rem;
  line-height: 1.4;
}

.progress-track, .progress-bar {
  height: 10px;
  background: var(--softline);
  border-radius: var(--r-full);
  overflow: hidden;
}

.progress-track span, .progress-bar span {
  display: block;
  height: 100%;
  width: 0;
  background: var(--planner-accent-gradient);
  border-radius: var(--r-full);
  transition: width 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}

.progress-stats, .stats {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 8px;
  margin-top: 15px;
}

.pstat, .stat {
  padding: 9px 10px;
  border-radius: 8px;
  background: var(--surface);
  border: 1px solid var(--line);
  text-align: center;
}

.pstat strong, .stat strong {
  display: block;
  font-size: 1.05rem;
  font-weight: 800;
  color: var(--ink);
}

.pstat span, .stat span {
  font-size: 0.68rem;
  color: var(--muted);
  font-weight: 600;
}

/* Summary Strip & Overview */
.summary-strip, .overview, .relevance-strip {
  margin-bottom: 22px;
  background: var(--paper);
  border: 1px solid var(--line);
  border-radius: 12px;
  padding: 18px 20px;
  display: grid;
  grid-template-columns: 1.3fr repeat(3, 0.55fr);
  gap: 12px;
  box-shadow: var(--shadow);
}

.summary-intro h2, .overview h2, .relevance-title {
  font-family: 'Source Serif 4', Georgia, serif;
  font-size: 1.1rem;
  font-weight: 600;
  color: var(--ink);
  margin: 0 0 4px;
}

.summary-intro p, .overview p, .relevance-desc {
  margin: 0;
  color: var(--muted);
  font-size: 0.82rem;
  line-height: 1.5;
}

.metric, .relevance-chip {
  padding: 12px 14px;
  border-radius: 8px;
  border: 1px solid var(--line);
  background: var(--surface);
  text-align: center;
}

.metric strong, .relevance-chip strong {
  display: block;
  font-size: 1.25rem;
  font-weight: 800;
  color: var(--planner-primary-dark);
}

.metric span, .relevance-chip span {
  font-size: 0.68rem;
  color: var(--muted);
  font-weight: 600;
}

/* Layout & Sidebar */
.layout {
  display: grid;
  grid-template-columns: 280px minmax(0, 1fr);
  gap: 24px;
  padding-bottom: 64px;
}

.sidebar {
  position: sticky;
  top: 86px;
  align-self: start;
  max-height: calc(100vh - 106px);
  overflow: auto;
  scrollbar-width: thin;
}

.side-card {
  background: var(--paper);
  border: 1px solid var(--line);
  border-radius: 12px;
  padding: 12px;
  box-shadow: var(--shadow);
}

.side-title {
  padding: 6px 8px 8px;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  font-size: 0.68rem;
  font-weight: 700;
  color: var(--muted);
}

.nav-list {
  display: grid;
  gap: 4px;
}

.nav-list a {
  display: grid;
  grid-template-columns: 30px minmax(0, 1fr) auto;
  gap: 9px;
  align-items: center;
  padding: 7px 9px;
  border-radius: 8px;
  text-decoration: none;
  color: var(--ink2);
  font-size: 0.75rem;
  font-weight: 600;
  transition: all 0.16s ease;
}

.nav-list a:hover {
  background: var(--planner-primary-light);
  color: var(--primary);
}

.nav-no, .nav-chip {
  width: 28px;
  height: 28px;
  border-radius: 6px;
  display: grid;
  place-items: center;
  background: var(--softline);
  color: var(--brand);
  font-size: 0.66rem;
  font-weight: 800;
  transition: all 0.16s ease;
}

.nav-list a:hover .nav-no, .nav-list a:hover .nav-chip {
  background: var(--primary);
  color: #fff;
}

.nav-list small, .nav-pct {
  font-size: 0.68rem;
  color: var(--muted);
  font-weight: 600;
}

/* Toolbar & Filters (UPSSSC PET Style Tab Pills) */
.content {
  min-width: 0;
}

.toolbar {
  position: sticky;
  top: 76px;
  z-index: 50;
  margin-bottom: 16px;
  padding: 10px 12px;
  border: 1px solid var(--line);
  border-radius: 12px;
  background: rgba(255, 253, 248, 0.95);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  display: grid;
  grid-template-columns: minmax(0, 1fr) auto auto auto;
  gap: 10px;
  box-shadow: var(--shadow);
}

.search-wrap {
  position: relative;
}

.search-icon {
  position: absolute;
  left: 14px;
  top: 50%;
  transform: translateY(-50%);
  width: 16px;
  height: 16px;
  color: var(--muted);
  pointer-events: none;
}

.search {
  width: 100%;
  height: 42px;
  border: 1.5px solid var(--line-medium);
  border-radius: var(--r-full);
  padding: 0 14px 0 40px;
  background: var(--paper);
  outline: none;
  font-size: 0.85rem;
  font-family: 'DM Sans', sans-serif;
  color: var(--ink);
  transition: all 0.18s ease;
}

.search:focus {
  border-color: var(--primary);
  box-shadow: 0 0 0 3px var(--planner-primary-glow);
}

.filters {
  display: flex;
  gap: 3px;
  padding: 3px;
  border-radius: var(--r-full);
  background: var(--softline);
}

/* Long syllabus point filters occupy their own row instead of widening the page. */
#pointFilters {
  grid-column: 1 / -1;
  order: 1;
  flex-wrap: wrap;
  border-radius: 12px;
}

.filters button {
  height: 36px;
  padding: 0 12px;
  border: 0;
  border-radius: var(--r-full);
  background: transparent;
  color: var(--muted);
  font-family: 'DM Sans', sans-serif;
  font-size: 0.74rem;
  font-weight: 600;
  cursor: pointer;
  white-space: nowrap;
  transition: all 0.18s ease;
}

.filters button:hover {
  color: var(--primary);
  background: var(--planner-primary-light);
}

.filters button.active {
  background: var(--primary);
  color: #fff;
  box-shadow: 0 2px 8px var(--planner-primary-glow);
  font-weight: 700;
}

.toolbar-btn {
  height: 42px;
  padding: 0 14px;
  border: 1px solid var(--line);
  border-radius: var(--r-full);
  background: var(--paper);
  color: var(--ink2);
  font-family: 'DM Sans', sans-serif;
  font-size: 0.75rem;
  font-weight: 600;
  cursor: pointer;
  white-space: nowrap;
  transition: all 0.18s ease;
}

.toolbar-btn:hover {
  background: var(--planner-primary-light);
  color: var(--primary);
  border-color: rgba(13, 148, 136, 0.3);
}

/* Section Cards & Accordions */
.section-card {
  --accent: #0d9488;
  --soft: #f0fdfa;
  background: var(--paper);
  border: 1px solid var(--line);
  border-radius: 10px;
  overflow: hidden;
  scroll-margin-top: 145px;
  box-shadow: var(--shadow);
  transition: box-shadow 0.22s ease, border-color 0.22s ease;
  position: relative;
}

.section-card + .section-card {
  margin-top: 14px;
}

.section-card:hover {
  box-shadow: var(--shadow-hover);
  border-color: rgba(13, 148, 136, 0.25);
}

.section-card:before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 4px;
  height: 100%;
  background: var(--planner-accent-gradient);
  border-radius: 4px 0 0 4px;
}

.section-head {
  position: relative;
  width: 100%;
  border: 0;
  background: transparent;
  display: grid;
  grid-template-columns: 50px minmax(0, 1fr) 190px 22px;
  gap: 13px;
  align-items: center;
  text-align: left;
  padding: 16px 18px 16px 20px;
  cursor: pointer;
}

.section-index, .section-no {
  width: 44px;
  height: 44px;
  border-radius: 8px;
  display: grid;
  place-items: center;
  background: var(--planner-brand-light);
  color: var(--brand);
  font-size: 0.78rem;
  font-weight: 800;
}

.section-title {
  display: block;
  font-family: 'DM Sans', sans-serif;
  font-size: 1.05rem;
  font-weight: 700;
  color: var(--ink);
  line-height: 1.35;
}

.section-meta, .section-desc {
  display: block;
  color: var(--muted);
  font-size: 0.74rem;
  margin-top: 2px;
}

.section-hindi {
  display: block;
  font-size: 0.78rem;
  color: var(--muted);
  margin-top: 2px;
}

.mini-progress, .section-progress {
  display: grid;
  grid-template-columns: 1fr auto;
  gap: 8px;
  align-items: center;
}

.mini-track, .section-progress-bar {
  height: 6px;
  background: var(--softline);
  border-radius: var(--r-full);
  overflow: hidden;
}

.mini-track span, .section-progress-bar span {
  display: block;
  height: 100%;
  width: 0;
  background: var(--planner-accent-gradient);
  border-radius: var(--r-full);
  transition: width 0.3s ease;
}

.mini-progress small, .section-progress small {
  font-size: 0.7rem;
  color: var(--muted);
  min-width: 55px;
  text-align: right;
  font-weight: 600;
}

.chev {
  font-size: 1.15rem;
  color: var(--primary);
  opacity: 0.8;
  transition: transform 0.2s ease;
  line-height: 1;
}

.section-card.open .chev {
  transform: rotate(180deg);
}

.section-body {
  display: none;
  border-top: 1px solid var(--softline);
  background: var(--surface);
  padding: 16px;
}

.section-card.open .section-body {
  display: block;
}

/* Topic Grid & Items (UPSSSC PET Checkbox UX) */
.topic-grid, .topic-list {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  border: 1px solid var(--line);
  border-radius: 8px;
  overflow: hidden;
  background: var(--paper);
}

.topic {
  display: grid;
  grid-template-columns: 42px minmax(0, 1fr) 36px;
  align-items: center;
  min-height: 56px;
  border-bottom: 1px solid var(--softline);
  background: var(--paper);
  transition: background 0.15s ease;
  padding: 2px 0;
}

.topic:nth-child(odd) {
  border-right: 1px solid var(--softline);
}

.topic:hover {
  background: var(--planner-primary-light);
}

.topic.done {
  background: rgba(13, 148, 136, 0.04);
}

.check, .check-wrap {
  display: grid;
  place-items: center;
  height: 100%;
  min-width: 42px;
  cursor: pointer;
}

.topic-check {
  appearance: none;
  -webkit-appearance: none;
  width: 17px;
  height: 17px;
  min-width: 17px;
  border: 1.5px solid var(--line-medium);
  border-radius: 4px;
  outline: none;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  transition: all 0.18s ease;
  background: var(--paper);
  position: relative;
}

.topic-check:hover {
  border-color: var(--primary);
}

.topic-check:checked {
  background: var(--primary);
  border-color: var(--primary);
}

.topic-check:checked:before {
  content: "";
  display: block;
  width: 4px;
  height: 8px;
  border: solid #fff;
  border-width: 0 2px 2px 0;
  transform: rotate(45deg);
  margin-bottom: 2px;
}

.topic-copy, .topic-main {
  min-width: 0;
  padding: 8px 4px 8px 0;
}

.topic-link {
  display: block;
  text-decoration: none;
  font-size: 0.88rem;
  font-weight: 600;
  color: var(--ink);
  line-height: 1.45;
  transition: color 0.15s ease;
}

.topic-link:hover {
  color: var(--primary);
  text-decoration: none;
}

.topic.done .topic-link {
  color: var(--light);
  text-decoration: line-through;
}

.topic-tags {
  display: flex;
  gap: 5px;
  flex-wrap: wrap;
  margin-top: 4px;
}

.exam-tag {
  padding: 2px 8px;
  border-radius: var(--r-full);
  font-size: 0.62rem;
  font-weight: 700;
  letter-spacing: 0.02em;
  border: 1px solid transparent;
}

.exam-tag.shared {
  background: var(--planner-brand-light);
  color: var(--planner-brand);
  border-color: rgba(22, 99, 75, 0.2);
}

.exam-tag.only {
  background: var(--onlybg);
  color: var(--only);
  border-color: rgba(124, 58, 237, 0.2);
}

.exam-tag.tgt-only {
  background: var(--tgtbg);
  color: var(--tgt);
  border-color: rgba(180, 83, 9, 0.2);
}

.library-tag, .family-tag {
  padding: 2px 7px;
  border-radius: var(--r-full);
  font-size: 0.6rem;
  font-weight: 700;
  background: var(--softline);
  color: var(--muted);
  border: 1px solid var(--line);
}

.topic-path {
  display: block;
  margin-top: 2px;
  color: var(--light);
  font-size: 0.72rem;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.open-topic, .open-link {
  width: 28px;
  height: 28px;
  display: grid;
  place-items: center;
  text-decoration: none;
  border-radius: 6px;
  color: var(--light);
  transition: all 0.15s ease;
}

.open-topic:hover, .open-link:hover {
  background: var(--planner-primary-light);
  color: var(--primary);
}

/* Group heads, tables & additional modules */
.topic-group + .topic-group {
  margin-top: 20px;
}

.group-head {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 8px;
}

.group-head h3 {
  margin: 0;
  font-size: 0.8rem;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--brand);
  font-weight: 800;
}

.group-head span {
  font-size: 0.7rem;
  color: var(--muted);
}

.index-table {
  margin-top: 28px;
  background: var(--paper);
  border: 1px solid var(--line);
  border-radius: 12px;
  padding: 20px;
  box-shadow: var(--shadow);
}

.index-table h2 {
  margin: 0;
  font-size: 1.15rem;
}

.index-table p {
  margin: 4px 0 14px;
  color: var(--muted);
  font-size: 0.8rem;
}

.table-wrap {
  overflow: auto;
  border: 1px solid var(--line);
  border-radius: 8px;
}

table {
  width: 100%;
  border-collapse: collapse;
  min-width: 820px;
}

th, td {
  padding: 11px 13px;
  border-bottom: 1px solid var(--softline);
  text-align: left;
  vertical-align: middle;
}

th {
  background: var(--surface);
  font-size: 0.72rem;
  text-transform: uppercase;
  letter-spacing: 0.07em;
  color: var(--ink);
  font-weight: 700;
}

td {
  font-size: 0.82rem;
}

td a {
  color: var(--ink);
  font-weight: 600;
  text-decoration: none;
}

td a:hover {
  color: var(--primary);
  text-decoration: underline;
}

/* Empty State, Cross Card & Note Card */
.empty {
  display: none;
  padding: 44px 18px;
  border: 1.5px dashed var(--line-medium);
  border-radius: 12px;
  background: var(--paper);
  color: var(--muted);
  text-align: center;
  font-size: 0.9rem;
}

.cross-card, .cross-exam {
  margin-top: 16px;
  padding: 16px 20px;
  border: 1px solid var(--line);
  border-radius: 12px;
  background: var(--paper);
  display: flex;
  justify-content: space-between;
  gap: 16px;
  align-items: center;
  box-shadow: var(--shadow);
}

.cross-card strong, .cross-exam strong {
  display: block;
  font-size: 0.92rem;
  color: var(--ink);
}

.cross-card span, .cross-exam span {
  display: block;
  color: var(--muted);
  font-size: 0.76rem;
  margin-top: 2px;
}

.cross-card a, .cross-exam a {
  padding: 8px 14px;
  border: 1px solid var(--line);
  border-radius: var(--r-full);
  background: var(--surface);
  color: var(--planner-primary-dark);
  font-size: 0.76rem;
  font-weight: 700;
  text-decoration: none;
  white-space: nowrap;
  transition: all 0.16s ease;
}

.cross-card a:hover, .cross-exam a:hover {
  background: var(--planner-primary-light);
  border-color: rgba(13, 148, 136, 0.3);
  color: var(--primary);
}

.note-card {
  margin-top: 16px;
  padding: 14px 18px;
  border: 1px solid var(--line);
  border-radius: 12px;
  background: var(--paper);
  font-size: 0.8rem;
  color: var(--ink2);
}

.note-card strong {
  display: block;
  color: var(--ink);
  font-size: 0.88rem;
  margin-bottom: 3px;
}

/* Footer */
.footer {
  padding: 28px 0;
  background: var(--paper);
  border-top: 1px solid var(--line);
  color: var(--muted);
  font-size: 0.77rem;
}

.footer-inner {
  display: flex;
  justify-content: space-between;
  gap: 14px;
  flex-wrap: wrap;
}

.footer a {
  color: var(--planner-primary-dark);
  text-decoration: none;
  font-weight: 700;
}

.footer a:hover {
  color: var(--primary);
}

.section-card[hidden], .topic[hidden] {
  display: none !important;
}

/* Responsive Media Queries */
@media (max-width: 1160px) {
  .hero-grid {
    grid-template-columns: 1fr;
  }
  .progress-card {
    max-width: 560px;
  }
  .summary-strip, .overview, .relevance-strip {
    grid-template-columns: 1fr 1fr 1fr;
  }
  .summary-intro, .overview > div:first-child {
    grid-column: 1 / -1;
  }
  .layout {
    grid-template-columns: 235px minmax(0, 1fr);
  }
  .section-head {
    grid-template-columns: 50px minmax(0, 1fr) 145px 20px;
  }
  .toolbar {
    grid-template-columns: 1fr auto auto;
  }
  .search-wrap {
    grid-column: 1 / -1;
  }
}

@media (max-width: 880px) {
  .layout {
    display: block;
  }
  .sidebar {
    display: none;
  }
  .topic-grid, .topic-list {
    grid-template-columns: 1fr;
  }
  .topic:nth-child(odd) {
    border-right: 0;
  }
}

@media (max-width: 650px) {
  .wrap {
    width: min(100% - 20px, 1440px);
  }
  .exam-chip {
    display: none;
  }
  .hero {
    padding-top: 26px;
  }
  .summary-strip, .overview, .relevance-strip {
    grid-template-columns: 1fr;
  }
  .summary-intro, .overview > div:first-child {
    grid-column: auto;
  }
  .toolbar {
    display: flex;
    flex-wrap: wrap;
    top: 72px;
  }
  .search-wrap {
    flex: 1 0 100%;
  }
  .filters {
    max-width: 100%;
    overflow: auto;
  }
  .toolbar-btn {
    margin-left: auto;
  }
  .section-head {
    grid-template-columns: 46px minmax(0, 1fr) 20px;
    gap: 10px;
    padding: 14px 14px 14px 16px;
  }
  .mini-progress, .section-progress {
    grid-column: 2 / 3;
    margin-top: 4px;
  }
  .section-head .chev {
    grid-column: 3;
    grid-row: 1 / 3;
  }
  .section-body {
    padding: 12px;
  }
  .progress-stats, .stats {
    grid-template-columns: 1fr;
  }
  .cross-card, .cross-exam {
    display: block;
  }
  .cross-card a, .cross-exam a {
    display: inline-block;
    margin-top: 10px;
  }
}
`;

async function main() {
  console.log('Writing master tracker CSS...');
  fs.writeFileSync('assets/css/up-tgt-pgt-tracker.css', TRACKER_CSS, 'utf8');

  // List of all specialized CSS files to harmonize with the UPSSSC PET design system
  const specializedCssFiles = [
    'assets/css/up-tgt-pgt-english.css',
    'assets/css/up-tgt-pgt-commerce.css',
    'assets/css/up-tgt-pgt-sanskrit.css',
    'assets/css/up-tgt-pgt-physical-education.css',
    'assets/css/up-tgt-pgt-gk.css',
    'assets/css/up-tgt-art.css',
    'assets/css/up-pgt-art.css',
    'assets/css/up-pgt-biology.css',
    'assets/css/up-pgt-civics.css',
    'assets/css/up-pgt-education.css',
    'assets/css/up-pgt-sociology.css'
  ];

  for (const cssFile of specializedCssFiles) {
    if (fs.existsSync(cssFile)) {
      // Harmonize root tokens and fonts
      let content = fs.readFileSync(cssFile, 'utf8');
      
      // Ensure Google Fonts import is at top
      if (!content.includes('fonts.googleapis.com')) {
        content = `@import url('https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,400..700;1,9..40,400..700&family=Source+Serif+4:ital,opsz,wght@0,8..60,400..700;1,8..60,400..700&display=swap');\n` + content;
      }
      
      // Replace backgrounds, borders, inks to PET warm editorial system
      content = content.replace(/--bg:\s*#[a-fA-F0-9]+/g, '--bg: #f7f5ef');
      content = content.replace(/--paper:\s*#[a-fA-F0-9]+/g, '--paper: #ffffff');
      content = content.replace(/--ink:\s*#[a-fA-F0-9]+/g, '--ink: #182e26');
      content = content.replace(/--ink2:\s*#[a-fA-F0-9]+/g, '--ink2: #3e5047');
      content = content.replace(/--muted:\s*#[a-fA-F0-9]+/g, '--muted: #5d6d63');
      content = content.replace(/--line:\s*#[a-fA-F0-9]+/g, '--line: #d9ddd1');
      content = content.replace(/--softline:\s*#[a-fA-F0-9]+/g, '--softline: #eeeee5');
      content = content.replace(/--soft:\s*#[a-fA-F0-9]+/g, '--soft: #eeeee5');
      content = content.replace(/--brand:\s*#[a-fA-F0-9]+/g, '--brand: #16634b');
      content = content.replace(/--brand2:\s*#[a-fA-F0-9]+/g, '--brand2: #0f766e');
      content = content.replace(/--success:\s*#[a-fA-F0-9]+/g, '--success: #0d9488');
      content = content.replace(/--success-bg:\s*#[a-fA-F0-9]+/g, '--success-bg: #f0fdfa');
      content = content.replace(/font-family:\s*Inter[^;]+/g, `font-family: 'DM Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif`);
      
      // Update h1 font
      if (!content.includes(`font-family:'Source Serif 4'`)) {
        content += `\nh1, h2, .section-title { font-family: 'Source Serif 4', Georgia, serif; }\n`;
      }

      fs.writeFileSync(cssFile, content, 'utf8');
      console.log(`Updated ${cssFile}`);
    }
  }

  // Minify all files with esbuild
  const allCss = ['assets/css/up-tgt-pgt-tracker.css', ...specializedCssFiles];
  for (const f of allCss) {
    const minPath = f.replace('.css', '.min.css');
    const raw = fs.readFileSync(f, 'utf8');
    const result = await esbuild.transform(raw, { loader: 'css', minify: true });
    fs.writeFileSync(minPath, result.code, 'utf8');
    console.log(`Minified ${f} -> ${minPath} (${result.code.length} bytes)`);
  }

  // Now ensure all 37 root index.html pages have the fonts snippet
  const files = fs.readdirSync('.').filter(d => (d.startsWith('up-tgt-') || d.startsWith('up-pgt-')) && fs.statSync(d).isDirectory());
  console.log(`Found ${files.length} subject directories`);

  let updatedPages = 0;
  for (const dir of files) {
    const indexPath = path.join(dir, 'index.html');
    if (fs.existsSync(indexPath)) {
      let html = fs.readFileSync(indexPath, 'utf8');
      if (!html.includes('family=Source+Serif+4')) {
        // Insert fonts right before the stylesheet link or before </head>
        if (html.includes('<link rel="stylesheet"')) {
          html = html.replace('<link rel="stylesheet"', `${FONT_LINK_SNIPPET}\n<link rel="stylesheet"`);
        } else {
          html = html.replace('</head>', `${FONT_LINK_SNIPPET}\n</head>`);
        }
        fs.writeFileSync(indexPath, html, 'utf8');
        updatedPages++;
      }
    }
  }
  console.log(`Updated ${updatedPages} pages with Google Fonts snippet.`);
}

main().catch(err => {
  console.error(err);
  process.exit(1);
});
