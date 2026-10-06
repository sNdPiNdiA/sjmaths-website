import fs from 'fs';
import path from 'path';

const cssPath = path.join(process.cwd(), 'assets', 'css', 'up-upper-primary-topic.css');

const modernCss = `/* =========================================================
   UP Upper Primary Teacher - Unified Modern Responsive Stylesheet
   Engineered for Optimal Readability, Fluid Spacing & Zero Mobile Bloat
   ========================================================= */

:root {
    --brand-emerald: #059669;
    --brand-emerald-dark: #047857;
    --brand-emerald-light: #10b981;
    --brand-emerald-subtle: rgba(5, 150, 105, 0.08);
    --brand-emerald-border: rgba(5, 150, 105, 0.2);

    --brand-indigo: #4f46e5;
    --brand-indigo-light: #6366f1;
    --brand-indigo-subtle: rgba(79, 70, 229, 0.08);

    --bg-canvas: #f8fafc;
    --bg-surface: #ffffff;
    --border-subtle: #e2e8f0;
    --border-medium: #cbd5e1;

    --text-headline: #0f172a;
    --text-sub: #475569;
    --text-muted: #64748b;

    --shadow-xs: 0 1px 2px rgba(15, 23, 42, 0.04);
    --shadow-sm: 0 2px 6px -1px rgba(15, 23, 42, 0.06), 0 2px 4px -2px rgba(15, 23, 42, 0.04);
    --shadow-md: 0 8px 24px -4px rgba(15, 23, 42, 0.08), 0 4px 12px -2px rgba(15, 23, 42, 0.04);

    --gradient-subject: linear-gradient(135deg, #059669 0%, #0d9488 50%, #4f46e5 100%);
}

/* Bilingual Language Display Engine */
body:not(.lang-mode-hi) .lang-hi { display: none !important; }
body.lang-mode-hi .lang-en { display: none !important; }

/* Language Toggle Pill */
.lang-toggle-btn {
    background: var(--bg-surface);
    border: 1px solid var(--border-medium);
    padding: 0.42rem 0.9rem;
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 0.84rem;
    font-weight: 700;
    color: var(--text-headline);
    border-radius: 999px;
    cursor: pointer;
    display: inline-flex;
    align-items: center;
    gap: 0.45rem;
    transition: all 0.2s ease;
}

.lang-toggle-btn:hover {
    border-color: var(--brand-emerald);
    color: var(--brand-emerald-dark);
}

body {
    background-color: var(--bg-canvas);
    color: var(--text-headline);
    font-family: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;
    line-height: 1.6;
}

/* Unified Layout Container - Fluid Responsive Padding */
.topic-page-container,
.subject-page-container,
.syllabus-container {
    max-width: 1040px;
    margin: clamp(0.75rem, 2vw, 1.35rem) auto;
    padding: 0.75rem clamp(0.75rem, 2.5vw, 1.25rem) 2.5rem;
    animation: fadeIn 0.35s ease-out;
}

/* Top Action & Breadcrumb Bar */
.top-action-bar,
.hub-navigation-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 0.85rem;
    flex-wrap: wrap;
    gap: 0.65rem;
}

.breadcrumb-trail {
    display: flex;
    align-items: center;
    gap: 0.4rem;
    font-size: 0.82rem;
    color: var(--text-muted);
    font-weight: 500;
    flex-wrap: wrap;
}

.breadcrumb-trail a {
    color: var(--text-sub);
    text-decoration: none;
    transition: color 0.2s ease;
}

.breadcrumb-trail a:hover {
    color: var(--brand-emerald);
}

.back-hub-btn {
    display: inline-flex;
    align-items: center;
    gap: 0.45rem;
    color: var(--brand-emerald-dark);
    text-decoration: none;
    font-weight: 700;
    font-size: 0.86rem;
    padding: 0.42rem 0.85rem;
    border-radius: 8px;
    background: var(--brand-emerald-subtle);
    transition: all 0.2s ease;
}

.back-hub-btn:hover {
    background: var(--brand-emerald);
    color: #ffffff;
    transform: translateX(-2px);
}

/* Topic & Subject Hero Header */
.topic-hero-panel,
.subject-hero-card,
.hero-panel {
    background: radial-gradient(circle at 10% 20%, rgba(5, 150, 105, 0.06) 0%, rgba(79, 70, 229, 0.05) 90%), var(--bg-surface);
    border: 1px solid var(--border-subtle);
    border-radius: 14px;
    padding: clamp(1rem, 2.5vw, 1.45rem) clamp(0.9rem, 2.5vw, 1.35rem);
    margin-bottom: 1rem;
    box-shadow: var(--shadow-sm);
    position: relative;
    overflow: hidden;
}

.topic-hero-panel::before,
.subject-hero-card::before,
.hero-panel::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 3px;
    background: var(--gradient-subject);
}

.topic-meta-row,
.hero-meta-row {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    margin-bottom: 0.65rem;
    flex-wrap: wrap;
}

.topic-badge-pill,
.part-badge {
    font-family: 'Outfit', sans-serif;
    font-size: 0.78rem;
    font-weight: 800;
    padding: 0.2rem 0.65rem;
    border-radius: 999px;
    background: var(--brand-emerald-subtle);
    color: var(--brand-emerald-dark);
    border: 1px solid var(--brand-emerald-border);
}

.subject-tag-pill,
.marks-badge,
.hero-pill {
    font-family: 'Outfit', sans-serif;
    font-size: 0.78rem;
    font-weight: 700;
    padding: 0.2rem 0.65rem;
    border-radius: 999px;
    background: rgba(79, 70, 229, 0.08);
    color: var(--brand-indigo);
}

.topic-hero-panel h1,
.subject-hero-card h1,
.hero-panel h1 {
    font-family: 'Outfit', sans-serif;
    font-size: clamp(1.35rem, 2.5vw, 1.8rem);
    font-weight: 800;
    color: var(--text-headline);
    margin: 0 0 0.35rem 0;
    line-height: 1.25;
}

.topic-hero-subtitle {
    font-size: clamp(0.92rem, 1.5vw, 1.02rem);
    font-weight: 600;
    color: var(--brand-emerald-dark);
    margin-bottom: 0.45rem;
}

.lead-desc,
.subject-hero-card p,
.hero-panel p {
    font-size: 0.92rem;
    color: var(--text-sub);
    line-height: 1.55;
    margin: 0;
}

/* Subject Hub Specific Components */
.subject-title-box {
    display: flex;
    align-items: center;
    gap: 1rem;
    margin-bottom: 0.75rem;
}

.subject-icon-box {
    width: 52px;
    height: 52px;
    border-radius: 12px;
    background: var(--gradient-subject);
    color: #ffffff;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.5rem;
    flex-shrink: 0;
    box-shadow: 0 4px 14px rgba(5, 150, 105, 0.2);
}

.sticky-subject-tracker {
    background: var(--bg-surface);
    border: 1px solid var(--border-subtle);
    border-radius: 12px;
    padding: 0.85rem 1.15rem;
    margin-bottom: 1rem;
    box-shadow: var(--shadow-sm);
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 1rem;
    flex-wrap: wrap;
    position: sticky;
    top: 66px;
    z-index: 100;
    backdrop-filter: blur(12px);
}

.tracker-left h2 {
    font-family: 'Outfit', sans-serif;
    font-size: 1.05rem;
    font-weight: 800;
    color: var(--text-headline);
    margin: 0 0 0.15rem 0;
}

.tracker-left p {
    font-size: 0.82rem;
    color: var(--text-muted);
    margin: 0;
}

.tracker-right {
    display: flex;
    align-items: center;
    gap: 0.85rem;
    flex-grow: 1;
    max-width: 320px;
    justify-content: flex-end;
}

.meter-rail {
    background: #e2e8f0;
    border-radius: 999px;
    height: 8px;
    width: 100%;
    overflow: hidden;
}

.meter-bar {
    background: var(--gradient-subject);
    height: 100%;
    width: 0%;
    transition: width 0.35s ease-out;
    border-radius: 999px;
}

.meter-label {
    font-family: 'Outfit', sans-serif;
    font-weight: 800;
    font-size: 1.05rem;
    color: var(--brand-emerald-dark);
    min-width: 44px;
    text-align: right;
}

details.module-accordion {
    background: var(--bg-surface);
    border: 1px solid var(--border-subtle);
    border-radius: 12px;
    margin-bottom: 0.85rem;
    transition: all 0.2s ease;
    overflow: hidden;
    box-shadow: var(--shadow-xs);
}

details.module-accordion[open] {
    border-color: var(--brand-emerald-border);
    box-shadow: var(--shadow-sm);
}

summary.module-summary {
    padding: 0.85rem 1.15rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
    cursor: pointer;
    list-style: none;
    user-select: none;
    background: #f8fafc;
    border-bottom: 1px solid transparent;
    transition: background-color 0.2s ease;
}

details.module-accordion[open] summary.module-summary {
    background: #ffffff;
    border-bottom-color: var(--border-subtle);
}

summary.module-summary::-webkit-details-marker {
    display: none;
}

.module-title {
    font-family: 'Outfit', sans-serif;
    font-size: 0.98rem;
    font-weight: 700;
    color: var(--text-headline);
    margin: 0;
    flex-grow: 1;
    padding-right: 0.75rem;
}

/* Study Tabs Strip - Fluid Non-Blocking Sticky Pill Strip */
.study-tabs-strip {
    display: flex;
    gap: 0.35rem;
    padding: 0.3rem 0.4rem;
    background: var(--bg-surface);
    border: 1px solid var(--border-subtle);
    border-radius: 12px;
    margin-bottom: 1rem;
    position: sticky;
    top: 66px;
    z-index: 100;
    backdrop-filter: blur(12px);
    box-shadow: var(--shadow-sm);
    flex-wrap: nowrap;
    overflow-x: auto;
    scrollbar-width: none;
    -webkit-overflow-scrolling: touch;
}

.study-tabs-strip::-webkit-scrollbar {
    display: none;
}

.study-tab-btn {
    flex: 1 1 auto;
    min-width: 105px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 0.4rem;
    padding: 0.5rem 0.85rem;
    border: none;
    background: transparent;
    border-radius: 8px;
    font-family: 'Outfit', sans-serif;
    font-size: 0.88rem;
    font-weight: 700;
    color: var(--text-sub);
    cursor: pointer;
    transition: all 0.2s ease;
    white-space: nowrap;
}

.study-tab-btn:hover {
    background: var(--brand-emerald-subtle);
    color: var(--brand-emerald-dark);
}

.study-tab-btn.active {
    background: #047857;
    color: #ffffff;
    box-shadow: 0 3px 10px rgba(5, 150, 105, 0.25);
}

.study-tab-pane {
    display: none;
}

.study-tab-pane.active {
    display: block;
    animation: fadeIn 0.3s ease-out;
}

/* Prep Cards & Content Body */
.prep-card {
    background: var(--bg-surface);
    border: 1px solid var(--border-subtle);
    border-radius: 14px;
    padding: clamp(0.95rem, 2vw, 1.35rem) clamp(0.85rem, 2vw, 1.35rem);
    margin-bottom: 1rem;
    box-shadow: var(--shadow-xs);
}

.prep-card h2 {
    font-family: 'Outfit', sans-serif;
    font-size: clamp(1.05rem, 2vw, 1.22rem);
    font-weight: 800;
    color: var(--text-headline);
    margin: 0 0 0.75rem 0;
    display: flex;
    align-items: center;
    gap: 0.55rem;
    padding-bottom: 0.5rem;
    border-bottom: 1px solid var(--border-subtle);
}

.topic-content-body {
    font-size: 0.95rem;
    line-height: 1.65;
    color: var(--text-sub);
}

.topic-content-body p {
    margin: 0 0 0.75rem 0;
}

.topic-content-body ul,
.topic-content-body ol {
    margin: 0 0 0.75rem 1.15rem;
    padding: 0;
}

.topic-content-body li {
    margin-bottom: 0.35rem;
}

.topic-content-body strong {
    color: var(--text-headline);
}

/* Pointwise Notes & Concept Cards */
.point-grid {
    display: flex;
    flex-direction: column;
    gap: 0.55rem;
    margin: 0.65rem 0 0.85rem 0;
}

.point-card {
    background: #f8fafc;
    border: 1px solid var(--border-subtle);
    border-left: 4px solid var(--brand-emerald);
    border-radius: 8px;
    padding: 0.65rem 0.95rem;
    font-size: 0.91rem;
    line-height: 1.58;
    color: var(--text-sub);
    transition: transform 0.15s ease, border-color 0.15s ease;
}

.point-card:hover {
    transform: translateX(2px);
    border-color: var(--brand-emerald-border);
    background: #ffffff;
}

.point-card strong {
    color: var(--text-headline);
    font-weight: 700;
}

/* Callout Highlights */
.tip-box {
    background: rgba(245, 158, 11, 0.08);
    border: 1px solid rgba(245, 158, 11, 0.3);
    border-left: 4px solid #f59e0b;
    border-radius: 8px;
    padding: 0.65rem 0.95rem;
    margin: 0.75rem 0;
    font-size: 0.89rem;
    color: #92400e;
    line-height: 1.55;
}

.tip-box strong {
    color: #78350f;
}

.trick-box {
    background: rgba(99, 102, 241, 0.08);
    border: 1px solid rgba(99, 102, 241, 0.3);
    border-left: 4px solid #6366f1;
    border-radius: 8px;
    padding: 0.65rem 0.95rem;
    margin: 0.75rem 0;
    font-size: 0.89rem;
    color: #3730a3;
    line-height: 1.55;
}

.trick-box strong {
    color: #312e81;
}

.mnemonic-inline-box {
    background: rgba(16, 185, 129, 0.08);
    border: 1px solid rgba(16, 185, 129, 0.3);
    border-left: 4px solid #10b981;
    border-radius: 8px;
    padding: 0.65rem 0.95rem;
    margin: 0.75rem 0;
    font-size: 0.89rem;
    color: #065f46;
    line-height: 1.55;
}

.mnemonic-inline-box code {
    background: #ecfdf5;
    padding: 0.15rem 0.45rem;
    border-radius: 5px;
    font-weight: 800;
    color: #047857;
    border: 1px solid rgba(16, 185, 129, 0.3);
    font-family: 'Outfit', monospace;
}

.strategy-banner-box {
    background: var(--brand-emerald-subtle);
    border: 1px solid var(--brand-emerald-border);
    border-left: 4px solid var(--brand-emerald);
    padding: 0.75rem 1rem;
    border-radius: 8px;
    margin-bottom: 1rem;
    font-size: 0.9rem;
    line-height: 1.55;
}

/* Concept Sub-tables & Data Tables */
.topic-subtable-wrapper,
.table-scroll-wrapper {
    margin: 0.85rem 0;
    overflow-x: auto;
    border-radius: 10px;
    border: 1px solid var(--border-subtle);
}

.topic-subtable,
.prep-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.88rem;
    text-align: left;
}

.topic-subtable th,
.prep-table th {
    background: #f1f5f9;
    padding: 0.55rem 0.75rem;
    font-weight: 700;
    color: var(--text-headline);
    border-bottom: 2px solid var(--border-medium);
    white-space: nowrap;
}

.topic-subtable td,
.prep-table td {
    padding: 0.55rem 0.75rem;
    border-bottom: 1px solid var(--border-subtle);
    color: var(--text-sub);
}

.topic-subtable tr:hover td,
.prep-table tr:hover td {
    background: #f8fafc;
}

.prep-table tr:last-child td {
    border-bottom: none;
}

/* Mathematics & Worked Example Enhancements */
.worked-example-box {
    background: #f0fdf4;
    border: 1px solid #bbf7d0;
    border-left: 4px solid var(--brand-emerald);
    border-radius: 10px;
    padding: 0.85rem 1.15rem;
    margin: 0.85rem 0;
}

.worked-example-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 0.55rem;
    flex-wrap: wrap;
    gap: 0.5rem;
}

.worked-example-title {
    font-size: 0.95rem;
    font-weight: 800;
    color: #166534;
    display: flex;
    align-items: center;
    gap: 0.45rem;
}

.speed-badge {
    background: #dcfce7;
    color: #15803d;
    border: 1px solid #86efac;
    font-size: 0.72rem;
    font-weight: 800;
    padding: 0.15rem 0.55rem;
    border-radius: 999px;
    text-transform: uppercase;
}

.method-compare-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 0.85rem;
    margin-top: 0.65rem;
}

.method-col {
    background: var(--bg-surface);
    border-radius: 8px;
    padding: 0.75rem 0.95rem;
    border: 1px solid var(--border-subtle);
}

.method-col.standard {
    border-left: 3px solid #94a3b8;
}

.method-col.topper {
    border-left: 3px solid #10b981;
    background: rgba(16, 185, 129, 0.05);
}

.method-label {
    font-size: 0.76rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 0.35rem;
}

.method-label.standard { color: #64748b; }
.method-label.topper { color: #15803d; }

.formula-table-wrap {
    overflow-x: auto;
    margin: 0.85rem 0;
    border-radius: 10px;
    border: 1px solid var(--border-subtle);
}

.formula-table {
    width: 100%;
    border-collapse: collapse;
    text-align: left;
    font-size: 0.88rem;
}

.formula-table th {
    background: #f1f5f9;
    color: var(--text-headline);
    font-weight: 700;
    padding: 0.55rem 0.75rem;
    border-bottom: 2px solid var(--border-medium);
}

.formula-table td {
    padding: 0.55rem 0.75rem;
    border-bottom: 1px solid var(--border-subtle);
    color: var(--text-sub);
}

.formula-table tr:hover td {
    background: #f8fafc;
}

.traps-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 0.85rem;
    margin-top: 0.85rem;
}

/* Live Completion Toggle Card */
.completion-card {
    background: var(--bg-surface);
    border: 1px solid var(--border-subtle);
    border-radius: 12px;
    padding: 0.75rem 1.15rem;
    margin-bottom: 1rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 1rem;
    flex-wrap: wrap;
}

.completion-card-left {
    display: flex;
    align-items: center;
    gap: 0.75rem;
}

.toggle-topic-btn {
    background: var(--brand-emerald);
    color: #ffffff;
    border: none;
    padding: 0.55rem 1.15rem;
    border-radius: 8px;
    font-family: 'Outfit', sans-serif;
    font-weight: 700;
    font-size: 0.88rem;
    cursor: pointer;
    transition: all 0.2s ease;
    display: inline-flex;
    align-items: center;
    gap: 0.45rem;
}

.toggle-topic-btn:hover {
    background: var(--brand-emerald-dark);
    transform: translateY(-1px);
    box-shadow: 0 3px 10px rgba(5, 150, 105, 0.25);
}

.toggle-topic-btn.completed {
    background: #10b981;
}

/* MCQs Styles */
.practice-summary-bar {
    background: var(--bg-surface);
    border: 1px solid var(--border-subtle);
    border-radius: 10px;
    padding: 0.75rem 1.15rem;
    margin-bottom: 1rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 0.75rem;
}

.practice-score-badge {
    font-family: 'Outfit', sans-serif;
    font-weight: 800;
    font-size: 0.95rem;
    color: var(--brand-emerald-dark);
    background: var(--brand-emerald-subtle);
    padding: 0.25rem 0.85rem;
    border-radius: 999px;
    border: 1px solid var(--brand-emerald-border);
}

.mcq-item-card {
    background: var(--bg-surface);
    border: 1px solid var(--border-subtle);
    border-radius: 12px;
    padding: clamp(0.95rem, 2vw, 1.25rem);
    margin-bottom: 1rem;
    box-shadow: var(--shadow-sm);
    transition: border-color 0.2s ease;
}

.mcq-header-meta {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 0.65rem;
    gap: 0.5rem;
}

.mcq-q-pill {
    font-family: 'Outfit', sans-serif;
    font-size: 0.76rem;
    font-weight: 700;
    padding: 0.18rem 0.55rem;
    background: #e2e8f0;
    border-radius: 5px;
    color: var(--text-headline);
}

.mcq-exam-pill {
    font-size: 0.78rem;
    font-weight: 600;
    color: var(--brand-emerald-dark);
}

.mcq-question-text {
    font-size: 0.98rem;
    font-weight: 600;
    color: var(--text-headline);
    line-height: 1.55;
    margin-bottom: 0.85rem;
}

.mcq-options-group {
    display: grid;
    gap: 0.55rem;
}

.mcq-option-btn {
    width: 100%;
    text-align: left;
    display: flex;
    align-items: flex-start;
    gap: 0.75rem;
    padding: 0.65rem 0.85rem;
    border-radius: 8px;
    background: #f8fafc;
    border: 1px solid var(--border-subtle);
    color: var(--text-headline);
    font-family: inherit;
    font-size: 0.9rem;
    cursor: pointer;
    transition: all 0.18s ease;
    line-height: 1.45;
}

.mcq-option-btn:hover:not(:disabled) {
    background: #f1f5f9;
    border-color: var(--border-medium);
    transform: translateX(2px);
}

.mcq-option-btn .opt-label {
    font-family: 'Outfit', sans-serif;
    font-weight: 700;
    min-width: 24px;
    height: 24px;
    border-radius: 5px;
    background: #e2e8f0;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    font-size: 0.8rem;
    flex-shrink: 0;
    margin-top: 1px;
}

.mcq-option-btn.opt-correct {
    background: #ecfdf5 !important;
    border-color: #10b981 !important;
    color: #065f46 !important;
}

.mcq-option-btn.opt-correct .opt-label {
    background: #10b981 !important;
    color: #ffffff !important;
}

.mcq-option-btn.opt-wrong {
    background: #fef2f2 !important;
    border-color: #ef4444 !important;
    color: #991b1b !important;
}

.mcq-option-btn.opt-wrong .opt-label {
    background: #ef4444 !important;
    color: #ffffff !important;
}

.mcq-explanation-box {
    display: none;
    margin-top: 0.85rem;
    padding: 0.75rem 1rem;
    border-radius: 8px;
    background: #f8fafc;
    border-left: 4px solid var(--brand-emerald);
    font-size: 0.89rem;
    animation: fadeIn 0.3s ease-out;
}

.exp-badge {
    font-weight: 700;
    font-family: 'Outfit', sans-serif;
    margin-bottom: 0.3rem;
}

/* Timed Mini Test Styles */
.mini-test-intro {
    text-align: center;
    padding: 1.1rem 0.75rem;
}

.test-desc {
    max-width: 600px;
    margin: 0 auto 1.1rem;
    font-size: 0.92rem;
    color: var(--text-sub);
}

.test-stats-row {
    display: flex;
    justify-content: center;
    gap: 0.75rem;
    margin-bottom: 1.25rem;
    flex-wrap: wrap;
}

.test-stat-chip {
    background: #f8fafc;
    border: 1px solid var(--border-subtle);
    padding: 0.35rem 0.85rem;
    border-radius: 999px;
    font-size: 0.82rem;
    font-weight: 600;
    color: var(--text-sub);
}

.start-test-btn,
.test-submit-btn,
.retry-test-btn {
    background: var(--gradient-subject);
    color: #ffffff;
    border: none;
    padding: 0.65rem 1.6rem;
    font-family: 'Outfit', sans-serif;
    font-size: 0.95rem;
    font-weight: 700;
    border-radius: 10px;
    cursor: pointer;
    box-shadow: 0 3px 12px rgba(5, 150, 105, 0.25);
    transition: transform 0.2s ease;
}

.start-test-btn:hover,
.test-submit-btn:hover,
.retry-test-btn:hover {
    transform: translateY(-2px);
}

.test-timer-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding-bottom: 0.75rem;
    border-bottom: 1px solid var(--border-subtle);
    margin-bottom: 1rem;
}

.test-countdown {
    font-family: 'Outfit', sans-serif;
    font-size: 1.1rem;
    font-weight: 800;
    color: #dc2626;
    display: flex;
    align-items: center;
    gap: 0.4rem;
}

.test-nav-controls {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 1.1rem;
    gap: 0.75rem;
}

.test-btn-nav {
    background: #f1f5f9;
    border: 1px solid var(--border-subtle);
    padding: 0.5rem 1rem;
    border-radius: 6px;
    font-weight: 600;
    font-size: 0.86rem;
    cursor: pointer;
    transition: all 0.2s ease;
}

.test-btn-nav:hover:not(:disabled) {
    background: #e2e8f0;
}

/* Revision Tab Styles */
.revision-facts-grid {
    display: grid;
    gap: 0.65rem;
    margin-bottom: 1.25rem;
}

.revision-fact-row {
    display: flex;
    align-items: flex-start;
    gap: 0.65rem;
    padding: 0.65rem 0.85rem;
    background: #f8fafc;
    border-radius: 8px;
    border: 1px solid var(--border-subtle);
    font-size: 0.91rem;
    line-height: 1.55;
}

.fact-num-badge {
    font-family: 'Outfit', sans-serif;
    font-weight: 800;
    font-size: 0.75rem;
    padding: 0.15rem 0.45rem;
    background: var(--brand-emerald-subtle);
    color: var(--brand-emerald-dark);
    border-radius: 5px;
    flex-shrink: 0;
    margin-top: 2px;
}

.mnemonic-card {
    background: var(--bg-surface);
    border: 1px solid var(--border-subtle);
    border-radius: 12px;
    padding: 0.95rem 1.15rem;
    margin-bottom: 1rem;
}

.mnemonic-quote-box {
    background: linear-gradient(135deg, rgba(99, 102, 241, 0.08), rgba(5, 150, 105, 0.08));
    border-left: 4px solid var(--brand-indigo);
    border-radius: 8px;
    padding: 0.85rem 1.1rem;
    font-size: 0.95rem;
    line-height: 1.55;
    color: var(--text-headline);
    margin-bottom: 0.6rem;
}

.traps-container {
    display: grid;
    gap: 0.75rem;
}

.trap-card-item {
    display: flex;
    align-items: flex-start;
    gap: 0.75rem;
    background: #fff5f5;
    border: 1px solid #fed7d7;
    border-left: 4px solid #dc2626;
    border-radius: 8px;
    padding: 0.75rem 1rem;
    font-size: 0.91rem;
    line-height: 1.55;
    color: #7f1d1d;
}

.topic-mastery-checklist {
    display: grid;
    gap: 0.55rem;
}

.mastery-check-item {
    display: flex;
    align-items: center;
    gap: 0.65rem;
    padding: 0.6rem 0.85rem;
    background: #f8fafc;
    border-radius: 8px;
    border: 1px solid var(--border-subtle);
    cursor: pointer;
    font-size: 0.91rem;
}

/* Coming Soon Blueprint */
.coming-soon-card {
    background: var(--bg-surface);
    border: 2px dashed var(--brand-emerald);
    border-radius: 14px;
    margin-bottom: 1.25rem;
    padding: 2rem 1.25rem;
    text-align: center;
}

.coming-soon-icon {
    font-size: 2.8rem;
    color: var(--brand-emerald);
    margin-bottom: 0.75rem;
}

.coming-soon-title {
    font-family: 'Outfit', sans-serif;
    font-size: 1.5rem;
    font-weight: 900;
    color: var(--text-headline);
    margin-bottom: 0.5rem;
}

.coming-soon-desc {
    max-width: 600px;
    margin: 0 auto 1.1rem;
    font-size: 0.95rem;
    color: var(--text-sub);
    line-height: 1.6;
}

.status-badge-live {
    display: inline-flex;
    align-items: center;
    gap: 0.45rem;
    padding: 0.35rem 0.95rem;
    border-radius: 999px;
    font-family: 'Outfit', sans-serif;
    font-size: 0.85rem;
    font-weight: 800;
    background: #ecfdf5;
    color: #065f46;
    border: 1px solid #a7f3d0;
}

/* Bottom Sequential Navigation */
.bottom-topic-nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 2rem;
    padding-top: 1rem;
    border-top: 1px solid var(--border-subtle);
    gap: 0.75rem;
    flex-wrap: wrap;
}

.topic-nav-btn {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.6rem 1rem;
    border-radius: 10px;
    text-decoration: none;
    font-family: 'Outfit', sans-serif;
    font-weight: 700;
    font-size: 0.9rem;
    border: 1px solid var(--border-subtle);
    background: var(--bg-surface);
    color: var(--text-headline);
    transition: all 0.2s ease;
}

.topic-nav-btn:hover:not(.disabled) {
    border-color: var(--brand-emerald-border);
    color: var(--brand-emerald-dark);
    transform: translateY(-2px);
    box-shadow: var(--shadow-sm);
}

.topic-nav-btn.disabled {
    opacity: 0.5;
    cursor: not-allowed;
}

/* Floating Actions */
.floating-action-strip {
    position: fixed;
    bottom: 1.5rem;
    right: 1.5rem;
    z-index: 999;
}

.back-to-top-btn {
    position: fixed;
    bottom: 20px;
    right: 20px;
    z-index: 1000;
    width: 42px;
    height: 42px;
    border-radius: 50%;
    background: var(--bg-surface);
    color: var(--brand-emerald-dark);
    border: 1px solid var(--border-subtle);
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.1);
    display: none;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    font-size: 1.05rem;
    transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
}

.back-to-top-btn:hover {
    background: var(--brand-emerald);
    color: #ffffff;
    box-shadow: 0 6px 18px rgba(5, 150, 105, 0.35);
    transform: translateY(-2px);
}

/* Animations */
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(5px); }
    to { opacity: 1; transform: translateY(0); }
}

/* Concept Mindmap Visual Hierarchy */
.mindmap-wrapper {
    background: radial-gradient(circle at 50% 50%, rgba(5, 150, 105, 0.05) 0%, rgba(79, 70, 229, 0.04) 100%), var(--bg-surface);
    border: 1px solid var(--brand-emerald-border);
    border-radius: 12px;
    padding: clamp(0.85rem, 2vw, 1.15rem);
    margin: 0.85rem 0;
    overflow-x: auto;
}

.mindmap-root-node {
    text-align: center;
    margin-bottom: 0.85rem;
}

.mindmap-root-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.45rem;
    background: var(--gradient-subject);
    color: #ffffff;
    font-family: 'Outfit', sans-serif;
    font-size: 0.95rem;
    font-weight: 800;
    padding: 0.45rem 1.15rem;
    border-radius: 999px;
    box-shadow: 0 3px 10px rgba(5, 150, 105, 0.25);
}

.mindmap-branches {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 0.85rem;
}

.mindmap-branch-card {
    background: var(--bg-surface);
    border: 1px solid var(--border-subtle);
    border-top: 4px solid var(--brand-emerald);
    border-radius: 10px;
    padding: 0.75rem 0.85rem;
    box-shadow: var(--shadow-xs);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.mindmap-branch-card:hover {
    transform: translateY(-2px);
    box-shadow: var(--shadow-sm);
    border-color: var(--brand-emerald-border);
}

.mindmap-branch-card:nth-child(2) { border-top-color: #4f46e5; }
.mindmap-branch-card:nth-child(3) { border-top-color: #0891b2; }
.mindmap-branch-card:nth-child(4) { border-top-color: #d97706; }
.mindmap-branch-card:nth-child(5) { border-top-color: #9333ea; }
.mindmap-branch-card:nth-child(6) { border-top-color: #059669; }

.mindmap-branch-title {
    font-family: 'Outfit', sans-serif;
    font-weight: 800;
    font-size: 0.92rem;
    color: var(--text-headline);
    margin-bottom: 0.55rem;
    display: flex;
    align-items: center;
    gap: 0.4rem;
}

.mindmap-subnodes {
    list-style: none;
    padding: 0;
    margin: 0;
    display: flex;
    flex-direction: column;
    gap: 0.35rem;
}

.mindmap-subnode-item {
    font-size: 0.85rem;
    color: var(--text-sub);
    background: #f8fafc;
    border: 1px solid var(--border-subtle);
    border-radius: 6px;
    padding: 0.35rem 0.55rem;
    line-height: 1.45;
}

/* =========================================================
   Responsive Media Queries: Mobile & Tablet Optimization
   ========================================================= */

@media (max-width: 768px) {
    .topic-page-container,
    .subject-page-container,
    .syllabus-container {
        padding: 0.5rem 0.75rem 2.25rem;
        margin: 0.5rem auto;
    }

    .top-action-bar,
    .hub-navigation-bar {
        margin-bottom: 0.65rem;
        gap: 0.5rem;
    }

    .topic-hero-panel,
    .subject-hero-card,
    .hero-panel {
        padding: 0.95rem 0.9rem;
        margin-bottom: 0.85rem;
        border-radius: 12px;
    }

    .topic-hero-panel h1,
    .subject-hero-card h1,
    .hero-panel h1 {
        font-size: 1.35rem;
        margin-bottom: 0.3rem;
    }

    .topic-hero-subtitle {
        font-size: 0.92rem;
        margin-bottom: 0.35rem;
    }

    .lead-desc,
    .subject-hero-card p,
    .hero-panel p {
        font-size: 0.88rem;
        line-height: 1.5;
    }

    .prep-card {
        padding: 0.85rem 0.9rem;
        margin-bottom: 0.85rem;
        border-radius: 12px;
    }

    .prep-card h2 {
        font-size: 1.05rem;
        margin-bottom: 0.6rem;
        padding-bottom: 0.4rem;
    }

    /* Fixed Sticky Strip on Mobile: Sleek single row, no wrapping, zero vertical blockage */
    .study-tabs-strip {
        top: 56px;
        margin-bottom: 0.85rem;
        padding: 0.25rem 0.35rem;
        gap: 0.3rem;
        flex-wrap: nowrap;
        overflow-x: auto;
        -webkit-overflow-scrolling: touch;
        scrollbar-width: none;
    }

    .study-tabs-strip::-webkit-scrollbar {
        display: none;
    }

    .study-tab-btn {
        flex: 0 0 auto;
        min-width: auto;
        white-space: nowrap;
        padding: 0.45rem 0.75rem;
        font-size: 0.84rem;
        border-radius: 6px;
    }

    .point-card {
        padding: 0.55rem 0.75rem;
        font-size: 0.88rem;
    }

    .tip-box,
    .trick-box,
    .mnemonic-inline-box,
    .strategy-banner-box {
        padding: 0.55rem 0.75rem;
        margin: 0.6rem 0;
        font-size: 0.86rem;
    }

    .mindmap-wrapper {
        padding: 0.75rem;
        margin: 0.75rem 0;
        border-radius: 10px;
    }

    .mindmap-branches {
        grid-template-columns: 1fr;
        gap: 0.65rem;
    }

    .mindmap-branch-card {
        padding: 0.65rem 0.75rem;
    }

    .method-compare-grid,
    .traps-grid {
        grid-template-columns: 1fr;
        gap: 0.65rem;
    }

    .completion-card {
        flex-direction: column;
        align-items: stretch;
        padding: 0.75rem 0.85rem;
        gap: 0.75rem;
    }

    .toggle-topic-btn {
        width: 100%;
        justify-content: center;
        padding: 0.55rem 1rem;
    }

    .bottom-topic-nav {
        flex-direction: column;
        margin-top: 1.5rem;
        padding-top: 0.85rem;
        gap: 0.6rem;
    }

    .topic-nav-btn {
        width: 100%;
        justify-content: center;
        padding: 0.55rem 0.9rem;
    }

    .table-scroll-wrapper,
    .topic-subtable-wrapper,
    .formula-table-wrap {
        margin: 0.65rem 0;
    }

    .prep-table th,
    .prep-table td,
    .topic-subtable th,
    .topic-subtable td,
    .formula-table th,
    .formula-table td {
        padding: 0.45rem 0.6rem;
        font-size: 0.82rem;
    }

    .mcq-item-card {
        padding: 0.85rem 0.9rem;
        margin-bottom: 0.85rem;
    }

    .mcq-question-text {
        font-size: 0.94rem;
        margin-bottom: 0.75rem;
    }

    .mcq-option-btn {
        padding: 0.55rem 0.75rem;
        font-size: 0.86rem;
    }
}

@media (max-width: 480px) {
    .topic-hero-panel h1,
    .subject-hero-card h1,
    .hero-panel h1 {
        font-size: 1.22rem;
    }

    .study-tabs-strip {
        top: 52px;
    }

    .study-tab-btn {
        font-size: 0.8rem;
        padding: 0.4rem 0.65rem;
    }

    .subject-title-box {
        gap: 0.75rem;
    }

    .subject-icon-box {
        width: 44px;
        height: 44px;
        font-size: 1.25rem;
    }
}

/* =========================================================
   Unified Comprehensive Dark Mode Engine
   ========================================================= */

body.dark-mode,
html.dark-mode,
html[data-theme="dark"],
body[data-theme="dark"],
.dark-mode {
    --bg-canvas: #090d16;
    --bg-surface: #111827;
    --bg-surface-elevated: #162032;
    --border-subtle: #1f2937;
    --border-medium: #374151;
    --text-headline: #f8fafc;
    --text-sub: #cbd5e1;
    --text-muted: #94a3b8;
    --brand-emerald-subtle: rgba(5, 150, 105, 0.16);
    --brand-emerald-border: rgba(5, 150, 105, 0.35);
    background-color: #090d16 !important;
    color: #cbd5e1 !important;
}

/* Hero Panel Dark Mode */
.dark-mode .topic-hero-panel,
.dark-mode .subject-hero-card,
.dark-mode .hero-panel,
body.dark-mode .topic-hero-panel,
body.dark-mode .subject-hero-card,
body.dark-mode .hero-panel,
html[data-theme="dark"] .topic-hero-panel,
html[data-theme="dark"] .subject-hero-card,
html[data-theme="dark"] .hero-panel {
    background: radial-gradient(circle at 10% 20%, rgba(5, 150, 105, 0.16) 0%, rgba(79, 70, 229, 0.1) 90%), #111827 !important;
    border: 1px solid #1f2937 !important;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.5) !important;
}

.dark-mode .topic-hero-panel h1,
.dark-mode .subject-hero-card h1,
.dark-mode .hero-panel h1,
body.dark-mode .topic-hero-panel h1,
body.dark-mode .subject-hero-card h1,
body.dark-mode .hero-panel h1,
html[data-theme="dark"] .topic-hero-panel h1,
html[data-theme="dark"] .subject-hero-card h1,
html[data-theme="dark"] .hero-panel h1 {
    color: #f8fafc !important;
}

.dark-mode .topic-hero-subtitle,
body.dark-mode .topic-hero-subtitle,
html[data-theme="dark"] .topic-hero-subtitle {
    color: #34d399 !important;
}

.dark-mode .lead-desc,
.dark-mode .subject-hero-card p,
.dark-mode .hero-panel p,
body.dark-mode .lead-desc,
body.dark-mode .subject-hero-card p,
body.dark-mode .hero-panel p,
html[data-theme="dark"] .lead-desc,
html[data-theme="dark"] .subject-hero-card p,
html[data-theme="dark"] .hero-panel p {
    color: #cbd5e1 !important;
}

/* Action Bar & Buttons Dark Mode */
.dark-mode .back-hub-btn,
body.dark-mode .back-hub-btn,
html[data-theme="dark"] .back-hub-btn {
    background: rgba(5, 150, 105, 0.15) !important;
    color: #34d399 !important;
    border: 1px solid rgba(5, 150, 105, 0.3) !important;
}

.dark-mode .back-hub-btn:hover,
body.dark-mode .back-hub-btn:hover,
html[data-theme="dark"] .back-hub-btn:hover {
    background: var(--brand-emerald) !important;
    color: #ffffff !important;
    border-color: var(--brand-emerald) !important;
}

.dark-mode .breadcrumb-trail,
body.dark-mode .breadcrumb-trail,
html[data-theme="dark"] .breadcrumb-trail {
    color: #94a3b8 !important;
}

.dark-mode .breadcrumb-trail a,
body.dark-mode .breadcrumb-trail a,
html[data-theme="dark"] .breadcrumb-trail a {
    color: #cbd5e1 !important;
}

.dark-mode .breadcrumb-trail a:hover,
body.dark-mode .breadcrumb-trail a:hover,
html[data-theme="dark"] .breadcrumb-trail a:hover {
    color: #34d399 !important;
}

/* Study Tabs Strip Dark Mode */
.dark-mode .study-tabs-strip,
body.dark-mode .study-tabs-strip,
html[data-theme="dark"] .study-tabs-strip {
    background: rgba(17, 24, 39, 0.95) !important;
    border: 1px solid #1f2937 !important;
    box-shadow: 0 4px 24px rgba(0, 0, 0, 0.6) !important;
}

.dark-mode .study-tab-btn,
body.dark-mode .study-tab-btn,
html[data-theme="dark"] .study-tab-btn {
    color: #94a3b8 !important;
    background: transparent !important;
    border: none !important;
}

.dark-mode .study-tab-btn:hover,
body.dark-mode .study-tab-btn:hover,
html[data-theme="dark"] .study-tab-btn:hover {
    background: rgba(5, 150, 105, 0.15) !important;
    color: #34d399 !important;
}

.dark-mode .study-tab-btn.active,
body.dark-mode .study-tab-btn.active,
html[data-theme="dark"] .study-tab-btn.active {
    background: #047857 !important;
    color: #ffffff !important;
    box-shadow: 0 4px 14px rgba(5, 150, 105, 0.35) !important;
}

/* Subject Hub Elements Dark Mode */
.dark-mode .sticky-subject-tracker,
body.dark-mode .sticky-subject-tracker,
html[data-theme="dark"] .sticky-subject-tracker {
    background: rgba(17, 24, 39, 0.95) !important;
    border-color: #1f2937 !important;
}

.dark-mode .tracker-left h2,
body.dark-mode .tracker-left h2,
html[data-theme="dark"] .tracker-left h2 {
    color: #f8fafc !important;
}

.dark-mode .tracker-left p,
body.dark-mode .tracker-left p,
html[data-theme="dark"] .tracker-left p {
    color: #94a3b8 !important;
}

.dark-mode .meter-rail,
body.dark-mode .meter-rail,
html[data-theme="dark"] .meter-rail {
    background: #1e293b !important;
}

.dark-mode details.module-accordion,
body.dark-mode details.module-accordion,
html[data-theme="dark"] details.module-accordion {
    background: #111827 !important;
    border-color: #1f2937 !important;
}

.dark-mode summary.module-summary,
body.dark-mode summary.module-summary,
html[data-theme="dark"] summary.module-summary {
    background: #151f30 !important;
}

.dark-mode details.module-accordion[open] summary.module-summary,
body.dark-mode details.module-accordion[open] summary.module-summary,
html[data-theme="dark"] details.module-accordion[open] summary.module-summary {
    background: #111827 !important;
    border-bottom-color: #1f2937 !important;
}

.dark-mode .module-title,
body.dark-mode .module-title,
html[data-theme="dark"] .module-title {
    color: #f8fafc !important;
}

/* Prep Cards & Content Dark Mode */
.dark-mode .prep-card,
body.dark-mode .prep-card,
html[data-theme="dark"] .prep-card {
    background: #111827 !important;
    border: 1px solid #1f2937 !important;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.35) !important;
}

.dark-mode .prep-card h2,
body.dark-mode .prep-card h2,
html[data-theme="dark"] .prep-card h2 {
    color: #f8fafc !important;
    border-bottom: 1px solid #1f2937 !important;
}

.dark-mode .topic-content-body,
body.dark-mode .topic-content-body,
html[data-theme="dark"] .topic-content-body {
    color: #cbd5e1 !important;
}

.dark-mode .topic-content-body strong,
body.dark-mode .topic-content-body strong,
html[data-theme="dark"] .topic-content-body strong {
    color: #f8fafc !important;
}

/* Point Cards & Notes Dark Mode */
.dark-mode .point-card,
body.dark-mode .point-card,
html[data-theme="dark"] .point-card {
    background: #151f30 !important;
    border: 1px solid #1f2937 !important;
    border-left: 4px solid var(--brand-emerald) !important;
    color: #cbd5e1 !important;
}

.dark-mode .point-card:hover,
body.dark-mode .point-card:hover,
html[data-theme="dark"] .point-card:hover {
    background: #1e2d42 !important;
    border-color: var(--brand-emerald-border) !important;
}

.dark-mode .point-card strong,
body.dark-mode .point-card strong,
html[data-theme="dark"] .point-card strong {
    color: #f8fafc !important;
}

/* Callout Boxes Dark Mode */
.dark-mode .strategy-banner-box,
body.dark-mode .strategy-banner-box,
html[data-theme="dark"] .strategy-banner-box {
    background: rgba(5, 150, 105, 0.14) !important;
    border-color: rgba(5, 150, 105, 0.35) !important;
    border-left-color: #10b981 !important;
    color: #e2e8f0 !important;
}

.dark-mode .tip-box,
body.dark-mode .tip-box,
html[data-theme="dark"] .tip-box {
    background: rgba(245, 158, 11, 0.12) !important;
    border-color: rgba(245, 158, 11, 0.3) !important;
    border-left-color: #f59e0b !important;
    color: #fde68a !important;
}

.dark-mode .tip-box strong,
body.dark-mode .tip-box strong,
html[data-theme="dark"] .tip-box strong {
    color: #fef3c7 !important;
}

.dark-mode .trick-box,
body.dark-mode .trick-box,
html[data-theme="dark"] .trick-box {
    background: rgba(99, 102, 241, 0.14) !important;
    border-color: rgba(99, 102, 241, 0.3) !important;
    border-left-color: #6366f1 !important;
    color: #c7d2fe !important;
}

.dark-mode .trick-box strong,
body.dark-mode .trick-box strong,
html[data-theme="dark"] .trick-box strong {
    color: #e0e7ff !important;
}

.dark-mode .mnemonic-inline-box,
body.dark-mode .mnemonic-inline-box,
html[data-theme="dark"] .mnemonic-inline-box {
    background: rgba(16, 185, 129, 0.12) !important;
    border-color: rgba(16, 185, 129, 0.3) !important;
    border-left-color: #10b981 !important;
    color: #a7f3d0 !important;
}

.dark-mode .mnemonic-inline-box code,
body.dark-mode .mnemonic-inline-box code,
html[data-theme="dark"] .mnemonic-inline-box code {
    background: #064e3b !important;
    color: #6ee7b7 !important;
    border-color: #059669 !important;
}

/* Mathematics & Worked Examples Dark Mode */
.dark-mode .worked-example-box,
body.dark-mode .worked-example-box,
html[data-theme="dark"] .worked-example-box {
    background: rgba(16, 185, 129, 0.08) !important;
    border-color: rgba(16, 185, 129, 0.25) !important;
}

.dark-mode .worked-example-title,
body.dark-mode .worked-example-title,
html[data-theme="dark"] .worked-example-title {
    color: #34d399 !important;
}

.dark-mode .method-col,
body.dark-mode .method-col,
html[data-theme="dark"] .method-col {
    background: #151f30 !important;
    border-color: #1f2937 !important;
}

.dark-mode .method-col.topper,
body.dark-mode .method-col.topper,
html[data-theme="dark"] .method-col.topper {
    background: rgba(16, 185, 129, 0.12) !important;
}

.dark-mode .formula-table th,
body.dark-mode .formula-table th,
html[data-theme="dark"] .formula-table th {
    background: #151f30 !important;
    color: #f8fafc !important;
    border-bottom: 2px solid #374151 !important;
}

.dark-mode .formula-table td,
body.dark-mode .formula-table td,
html[data-theme="dark"] .formula-table td {
    background: #111827 !important;
    border-bottom: 1px solid #1f2937 !important;
    color: #cbd5e1 !important;
}

.dark-mode .formula-table tr:hover td,
body.dark-mode .formula-table tr:hover td,
html[data-theme="dark"] .formula-table tr:hover td {
    background: #1e293b !important;
}

/* Tables Dark Mode */
.dark-mode .table-scroll-wrapper,
.dark-mode .topic-subtable-wrapper,
.dark-mode .formula-table-wrap,
body.dark-mode .table-scroll-wrapper,
body.dark-mode .topic-subtable-wrapper,
body.dark-mode .formula-table-wrap,
html[data-theme="dark"] .table-scroll-wrapper,
html[data-theme="dark"] .topic-subtable-wrapper,
html[data-theme="dark"] .formula-table-wrap {
    border-color: #1f2937 !important;
}

.dark-mode .prep-table th,
.dark-mode .topic-subtable th,
body.dark-mode .prep-table th,
body.dark-mode .topic-subtable th,
html[data-theme="dark"] .prep-table th,
html[data-theme="dark"] .topic-subtable th {
    background: #151f30 !important;
    color: #f8fafc !important;
    border-bottom: 2px solid #374151 !important;
}

.dark-mode .prep-table td,
.dark-mode .topic-subtable td,
body.dark-mode .prep-table td,
body.dark-mode .topic-subtable td,
html[data-theme="dark"] .prep-table td,
html[data-theme="dark"] .topic-subtable td {
    background: #111827 !important;
    border-bottom: 1px solid #1f2937 !important;
    color: #cbd5e1 !important;
}

.dark-mode .prep-table tr:hover td,
.dark-mode .topic-subtable tr:hover td,
body.dark-mode .prep-table tr:hover td,
body.dark-mode .topic-subtable tr:hover td,
html[data-theme="dark"] .prep-table tr:hover td,
html[data-theme="dark"] .topic-subtable tr:hover td {
    background: #1e293b !important;
}

/* Completion Card Dark Mode */
.dark-mode .completion-card,
body.dark-mode .completion-card,
html[data-theme="dark"] .completion-card {
    background: #111827 !important;
    border: 1px solid #1f2937 !important;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.35) !important;
}

.dark-mode .completion-card strong,
body.dark-mode .completion-card strong,
html[data-theme="dark"] .completion-card strong {
    color: #f8fafc !important;
}

.dark-mode .completion-card p,
body.dark-mode .completion-card p,
html[data-theme="dark"] .completion-card p {
    color: #94a3b8 !important;
}

/* MCQs Dark Mode */
.dark-mode .practice-summary-bar,
body.dark-mode .practice-summary-bar,
html[data-theme="dark"] .practice-summary-bar {
    background: #111827 !important;
    border: 1px solid #1f2937 !important;
}

.dark-mode .practice-score-badge,
body.dark-mode .practice-score-badge,
html[data-theme="dark"] .practice-score-badge {
    background: rgba(5, 150, 105, 0.16) !important;
    color: #34d399 !important;
    border-color: rgba(5, 150, 105, 0.35) !important;
}

.dark-mode .mcq-item-card,
body.dark-mode .mcq-item-card,
html[data-theme="dark"] .mcq-item-card {
    background: #111827 !important;
    border: 1px solid #1f2937 !important;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.35) !important;
}

.dark-mode .mcq-q-pill,
body.dark-mode .mcq-q-pill,
html[data-theme="dark"] .mcq-q-pill {
    background: #1e293b !important;
    color: #e2e8f0 !important;
}

.dark-mode .mcq-exam-pill,
body.dark-mode .mcq-exam-pill,
html[data-theme="dark"] .mcq-exam-pill {
    color: #34d399 !important;
}

.dark-mode .mcq-question-text,
body.dark-mode .mcq-question-text,
html[data-theme="dark"] .mcq-question-text {
    color: #f8fafc !important;
}

.dark-mode .mcq-option-btn,
body.dark-mode .mcq-option-btn,
html[data-theme="dark"] .mcq-option-btn {
    background: #151f30 !important;
    border: 1px solid #1f2937 !important;
    color: #cbd5e1 !important;
}

.dark-mode .mcq-option-btn:hover:not(:disabled),
body.dark-mode .mcq-option-btn:hover:not(:disabled),
html[data-theme="dark"] .mcq-option-btn:hover:not(:disabled) {
    background: #1e2d42 !important;
    border-color: #374151 !important;
}

.dark-mode .mcq-option-btn .opt-label,
body.dark-mode .mcq-option-btn .opt-label,
html[data-theme="dark"] .mcq-option-btn .opt-label {
    background: #1e293b !important;
    color: #cbd5e1 !important;
}

.dark-mode .mcq-explanation-box,
body.dark-mode .mcq-explanation-box,
html[data-theme="dark"] .mcq-explanation-box {
    background: #0f172a !important;
    border: 1px solid #1f2937 !important;
    border-left: 4px solid var(--brand-emerald) !important;
    color: #cbd5e1 !important;
}

/* Timed Mini Test Dark Mode */
.dark-mode .test-timer-bar,
body.dark-mode .test-timer-bar,
html[data-theme="dark"] .test-timer-bar {
    border-color: #1f2937 !important;
}

.dark-mode .test-stat-chip,
body.dark-mode .test-stat-chip,
html[data-theme="dark"] .test-stat-chip {
    background: #151f30 !important;
    border-color: #1f2937 !important;
    color: #cbd5e1 !important;
}

.dark-mode .test-desc,
body.dark-mode .test-desc,
html[data-theme="dark"] .test-desc {
    color: #94a3b8 !important;
}

.dark-mode .test-btn-nav,
body.dark-mode .test-btn-nav,
html[data-theme="dark"] .test-btn-nav {
    background: #1e293b !important;
    border-color: #334155 !important;
    color: #f1f5f9 !important;
}

.dark-mode .test-btn-nav:hover:not(:disabled),
body.dark-mode .test-btn-nav:hover:not(:disabled),
html[data-theme="dark"] .test-btn-nav:hover:not(:disabled) {
    background: #334155 !important;
}

/* Quick Revision & Exam Traps Dark Mode */
.dark-mode .revision-fact-row,
body.dark-mode .revision-fact-row,
html[data-theme="dark"] .revision-fact-row {
    background: #151f30 !important;
    border-color: #1f2937 !important;
    color: #cbd5e1 !important;
}

.dark-mode .mnemonic-card,
body.dark-mode .mnemonic-card,
html[data-theme="dark"] .mnemonic-card {
    background: #111827 !important;
    border-color: #1f2937 !important;
}

.dark-mode .mnemonic-quote-box,
body.dark-mode .mnemonic-quote-box,
html[data-theme="dark"] .mnemonic-quote-box {
    background: linear-gradient(135deg, rgba(99, 102, 241, 0.15), rgba(5, 150, 105, 0.15)) !important;
    border-color: var(--brand-indigo-light) !important;
    color: #e2e8f0 !important;
}

.dark-mode .trap-card-item,
body.dark-mode .trap-card-item,
html[data-theme="dark"] .trap-card-item {
    background: rgba(153, 27, 27, 0.16) !important;
    border-color: rgba(239, 68, 68, 0.35) !important;
    color: #fca5a5 !important;
}

.dark-mode .mastery-check-item,
body.dark-mode .mastery-check-item,
html[data-theme="dark"] .mastery-check-item {
    background: #151f30 !important;
    border-color: #1f2937 !important;
    color: #cbd5e1 !important;
}

/* Mindmap Dark Mode */
.dark-mode .mindmap-wrapper,
body.dark-mode .mindmap-wrapper,
html[data-theme="dark"] .mindmap-wrapper {
    background: radial-gradient(circle at 50% 50%, rgba(5, 150, 105, 0.12) 0%, rgba(79, 70, 229, 0.08) 100%), #111827 !important;
    border-color: rgba(5, 150, 105, 0.3) !important;
}

.dark-mode .mindmap-branch-card,
body.dark-mode .mindmap-branch-card,
html[data-theme="dark"] .mindmap-branch-card {
    background: #151f30 !important;
    border-color: #1f2937 !important;
}

.dark-mode .mindmap-branch-title,
body.dark-mode .mindmap-branch-title,
html[data-theme="dark"] .mindmap-branch-title {
    color: #f8fafc !important;
}

.dark-mode .mindmap-subnode-item,
body.dark-mode .mindmap-subnode-item,
html[data-theme="dark"] .mindmap-subnode-item {
    background: #111827 !important;
    border-color: #1f2937 !important;
    color: #cbd5e1 !important;
}

/* Bottom Navigation & Floating Buttons Dark Mode */
.dark-mode .bottom-topic-nav,
body.dark-mode .bottom-topic-nav,
html[data-theme="dark"] .bottom-topic-nav {
    border-top-color: #1f2937 !important;
}

.dark-mode .topic-nav-btn,
body.dark-mode .topic-nav-btn,
html[data-theme="dark"] .topic-nav-btn {
    background: #111827 !important;
    border-color: #1f2937 !important;
    color: #f8fafc !important;
}

.dark-mode .topic-nav-btn:hover:not(.disabled),
body.dark-mode .topic-nav-btn:hover:not(.disabled),
html[data-theme="dark"] .topic-nav-btn:hover:not(.disabled) {
    border-color: var(--brand-emerald-border) !important;
    color: #34d399 !important;
}

.dark-mode .back-to-top-btn,
body.dark-mode .back-to-top-btn,
html[data-theme="dark"] .back-to-top-btn {
    background: #111827 !important;
    border-color: #374151 !important;
    color: #34d399 !important;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.6) !important;
}

.dark-mode .back-to-top-btn:hover,
body.dark-mode .back-to-top-btn:hover,
html[data-theme="dark"] .back-to-top-btn:hover {
    background: var(--brand-emerald) !important;
    color: #ffffff !important;
}
`;

fs.writeFileSync(cssPath, modernCss, 'utf8');
console.log('Successfully wrote updated up-upper-primary-topic.css with math & hub enhancements');
