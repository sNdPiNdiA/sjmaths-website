const fs = require('fs');
const path = require('path');

const RESPONSIVE_DAYLIGHT_SNIPPET = `
/* ==========================================================================
   MOBILE-FIRST RESPONSIVE ENHANCEMENT (SJMaths ASO Study Hub)
   ========================================================================== */
html, body {
    max-width: 100vw !important;
    overflow-x: hidden !important;
    position: relative;
    background-color: #f8fafc !important;
    background: #f8fafc !important;
    color: #1e293b !important;
    -webkit-text-size-adjust: 100%;
    text-size-adjust: 100%;
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important;
}
* {
    box-sizing: border-box;
}

/* Fluid Responsive Typography */
h1, .hero-title {
    font-size: clamp(1.45rem, 4.5vw, 2.5rem) !important;
    line-height: 1.25 !important;
    word-break: break-word;
    overflow-wrap: break-word;
    color: #0f172a !important;
}
h2 {
    font-size: clamp(1.2rem, 3.5vw, 1.75rem) !important;
    line-height: 1.3 !important;
    word-break: break-word;
    color: #0f172a !important;
}
h3 {
    font-size: clamp(1.05rem, 3vw, 1.35rem) !important;
    line-height: 1.35 !important;
    word-break: break-word;
    color: #0f172a !important;
}

/* Touch-Optimized Segmented Tab Strip */
nav [role="tablist"],
nav.sticky div.flex,
nav div.flex,
.tab-strip,
#tab-nav,
.tabs-container,
.tab-nav {
    display: flex !important;
    flex-direction: row !important;
    flex-wrap: nowrap !important;
    align-items: center !important;
    gap: 0.35rem !important;
    overflow-x: auto !important;
    -webkit-overflow-scrolling: touch !important;
    scrollbar-width: none !important;
    -ms-overflow-style: none !important;
    max-width: 100% !important;
}
nav [role="tablist"]::-webkit-scrollbar,
nav.sticky div.flex::-webkit-scrollbar,
nav div.flex::-webkit-scrollbar,
.tab-strip::-webkit-scrollbar,
#tab-nav::-webkit-scrollbar,
.tabs-container::-webkit-scrollbar,
.tab-nav::-webkit-scrollbar,
.no-scrollbar::-webkit-scrollbar {
    display: none !important;
}
.tab-btn,
nav [role="tablist"] button,
nav.sticky button {
    display: inline-flex !important;
    flex-direction: row !important;
    align-items: center !important;
    justify-content: center !important;
    flex-shrink: 0 !important;
    white-space: nowrap !important;
    touch-action: manipulation;
    -webkit-tap-highlight-color: transparent;
    user-select: none;
    min-height: 38px;
    color: #475569 !important;
}
.tab-btn:hover {
    background-color: #f1f5f9 !important;
    color: #0f172a !important;
}
.tab-btn.bg-blue-600, .tab-btn.active {
    background-color: #1e40af !important;
    color: #ffffff !important;
}

/* Responsive Tables & Containers */
table {
    max-width: 100% !important;
    width: 100% !important;
    border-collapse: collapse;
    background-color: #ffffff !important;
    border: 1px solid #e2e8f0 !important;
}
th {
    background-color: #f1f5f9 !important;
    color: #0f172a !important;
    border-bottom: 2px solid #cbd5e1 !important;
    padding: 10px 14px;
}
td {
    color: #334155 !important;
    border-bottom: 1px solid #e2e8f0 !important;
    padding: 10px 14px;
}
tr:hover td {
    background-color: #eff6ff !important;
}
.data-table, .concept-card table, table.table-custom {
    display: block !important;
    overflow-x: auto !important;
    -webkit-overflow-scrolling: touch !important;
    scrollbar-width: thin;
}
.overflow-x-auto {
    overflow-x: auto !important;
    -webkit-overflow-scrolling: touch !important;
    max-width: 100% !important;
}

/* Prevent MathJax Display Formulas from Blowing Out Screen Width */
mjx-container[jax="CHTML"][display="true"] {
    overflow-x: auto !important;
    overflow-y: hidden !important;
    max-width: 100% !important;
    padding: 0.5rem 0.25rem !important;
    margin: 0.75rem 0 !important;
    -webkit-overflow-scrolling: touch !important;
    scrollbar-width: thin;
}
mjx-container {
    max-width: 100% !important;
}

/* Mobile Viewport Refinements (< 640px) */
@media (max-width: 640px) {
    body {
        font-size: 14px !important;
    }
    main, .max-w-7xl, .container, .module-container {
        padding-left: 0.75rem !important;
        padding-right: 0.75rem !important;
        padding-top: 1rem !important;
        padding-bottom: 2rem !important;
    }
    .concept-card {
        padding: 1.15rem 0.75rem !important;
        margin-bottom: 1.25rem !important;
        border-radius: 0.75rem !important;
    }
    .definition-callout, .callout-def, .trap-box, .numerical-box, .math-box, .derivation-box {
        padding: 0.85rem 0.75rem !important;
        margin: 0.85rem 0 !important;
        font-size: 0.875rem !important;
    }
    .tab-btn {
        padding: 0.4rem 0.75rem !important;
        font-size: 0.75rem !important;
    }
    table th, table td, .data-table th, .data-table td {
        padding: 0.45rem 0.6rem !important;
        font-size: 0.75rem !important;
        white-space: nowrap;
    }
    .quiz-card, .quiz-item, .mcq-card, .question-card {
        padding: 1rem 0.75rem !important;
        margin-bottom: 1rem !important;
    }
    .quiz-option, .option-item, .option-label, label.block {
        padding: 0.65rem 0.75rem !important;
        font-size: 0.85rem !important;
        min-height: 44px;
        display: flex;
        align-items: center;
    }
    .grid-cols-2, .grid-cols-3, .grid-cols-4, .sm\\:grid-cols-2, .md\\:grid-cols-2, .sm\\:grid-cols-3, .md\\:grid-cols-3 {
        grid-template-columns: 1fr !important;
    }
    .hero-badge, .badge-exam {
        font-size: 0.7rem !important;
        padding: 0.25rem 0.5rem !important;
    }
    .checklist-item {
        padding: 0.6rem 0.75rem !important;
        font-size: 0.85rem !important;
    }
    .page-footer-nav, .page-nav-footer {
        flex-direction: column !important;
        gap: 0.75rem !important;
        align-items: stretch !important;
        text-align: center;
    }
    .page-footer-nav a, .page-nav-footer a, .nav-btn-link {
        width: 100% !important;
        justify-content: center !important;
        display: flex !important;
    }
}

/* Tablet Refinements (641px - 1024px) */
@media (min-width: 641px) and (max-width: 1024px) {
    main, .max-w-7xl {
        padding-left: 1.25rem !important;
        padding-right: 1.25rem !important;
    }
    .concept-card {
        padding: 1.5rem !important;
    }
}

/* Daylight Surface & Text Palette */
header.sticky, .sj-header, .sj-topbar {
    background-color: rgba(255, 255, 255, 0.96) !important;
    border-bottom: 1px solid #e2e8f0 !important;
    box-shadow: 0 1px 3px rgba(15, 23, 42, 0.04) !important;
}
.text-white {
    color: #0f172a !important;
}
.text-slate-100, .text-slate-200 {
    color: #1e293b !important;
}
.text-slate-300, .text-slate-400 {
    color: #475569 !important;
}
.text-slate-500 {
    color: #64748b !important;
}
.bg-dark-surface, .concept-card, .hero-card {
    background-color: #ffffff !important;
    border-color: #e2e8f0 !important;
    color: #1e293b !important;
}
.border-slate-800, .border-slate-700, .border-slate-900 {
    border-color: #e2e8f0 !important;
}
.concept-card, .hero-card, .quiz-card, .question-card {
    background-color: #ffffff !important;
    border: 1px solid #e2e8f0 !important;
    box-shadow: 0 2px 10px rgba(15, 23, 42, 0.04) !important;
}
pre, code, .font-mono, .code-font {
    background-color: #f8fafc !important;
    color: #0f172a !important;
    border: 1px solid #e2e8f0 !important;
}
.bg-slate-900\\/80, .bg-slate-900\\/60, .bg-slate-900\\/50, .bg-slate-900\\/40, .bg-slate-900 {
    background-color: #f0f9ff !important;
    border-color: #bae6fd !important;
}
.bg-slate-950 {
    background-color: #f8fafc !important;
    border-color: #e2e8f0 !important;
    color: #0f172a !important;
}

/* High-Contrast Calm Quiz States */
.quiz-opt-correct,
.option-item.correct,
.quiz-option.correct,
.quiz-opt-btn.correct,
label.quiz-opt-correct {
    border-color: #10b981 !important;
    background-color: #dcfce7 !important;
    color: #065f46 !important;
}
.quiz-opt-incorrect,
.option-item.incorrect,
.quiz-option.incorrect,
.quiz-opt-btn.incorrect,
label.quiz-opt-incorrect {
    border-color: #ef4444 !important;
    background-color: #fee2e2 !important;
    color: #991b1b !important;
}
`;

function convertDayContent(filePath, html) {
  const isDay1 = filePath.includes('fluid-properties');
  const isDay2 = filePath.includes('fluid-statics');

  // Replace dark gradients
  html = html.replace(/to-\[#060911\]/g, 'to-slate-50');
  html = html.replace(/from-\[#0c1222\]/g, 'from-white');
  html = html.replace(/from-\[#111a30\]/g, 'from-white');

  // Replace #060911 in text and configs
  html = html.replace(/'#060911'/g, "'#f8fafc'");
  html = html.replace(/"#060911"/g, '"#f8fafc"');
  html = html.replace(/#060911/g, '#f8fafc');

  // Replace background-color and color
  html = html.replace(/background-color:\s*#060911\s*!important/gi, 'background-color: #f8fafc !important');
  html = html.replace(/background:\s*#060911/gi, 'background: #f8fafc');
  html = html.replace(/background-color:\s*#1e293b\s*!important/gi, 'background-color: #f8fafc !important');
  html = html.replace(/(?<!background-)color:\s*#f8fafc\s*!important/gi, 'color: #1e293b !important');
  html = html.replace(/(?<!background-)color:\s*#060911\s*!important/gi, 'color: #0f172a !important');
  html = html.replace(/(?<!background-)color:\s*#060911/gi, 'color: #0f172a');

  // Clean up inline dark table headers & borders
  html = html.replace(/background-color:\s*#1e293b;\s*color:\s*#38bdf8;/gi, 'background-color: #f1f5f9; color: #0f172a;');
  html = html.replace(/border:\s*1px\s+solid\s+#334155;/gi, 'border: 1px solid #e2e8f0;');
  html = html.replace(/border:\s*1px\s+solid\s+#475569;/gi, 'border: 1px solid #e2e8f0;');
  html = html.replace(/border-bottom:\s*1px\s+solid\s+#334155;/gi, 'border-bottom: 1px solid #e2e8f0;');
  html = html.replace(/border-bottom:\s*1px\s+solid\s+#475569;/gi, 'border-bottom: 1px solid #e2e8f0;');

  // Clean up low contrast quiz colors in scripts
  html = html.replace(/['"]#6ee7b7['"]/g, "'#065f46'");
  html = html.replace(/['"]#fca5a5['"]/g, "'#991b1b'");
  html = html.replace(/rgba\(16,\s*185,\s*129,\s*0\.22\)/g, '#dcfce7');
  html = html.replace(/rgba\(239,\s*68,\s*68,\s*0\.22\)/g, '#fee2e2');

  if (isDay1) {
    // ── DAY 1 SPECIFIC CONVERSIONS ── //
    html = html.replace(/--bg-base:\s*#[0-9a-fA-F]+;/, '--bg-base: #f8fafc;');
    html = html.replace(/--bg-surface:\s*#[0-9a-fA-F]+;/, '--bg-surface: #ffffff;');
    html = html.replace(/--bg-card:\s*#[0-9a-fA-F]+;/, '--bg-card: #ffffff;');
    html = html.replace(/--bg-card-hover:\s*#[0-9a-fA-F]+;/, '--bg-card-hover: #f1f5f9;');
    html = html.replace(/--border-subtle:\s*[^;]+;/, '--border-subtle: #e2e8f0;');
    html = html.replace(/--border-glow:\s*[^;]+;/, '--border-glow: rgba(37, 99, 235, 0.2);');
    html = html.replace(/--text-primary:\s*#[0-9a-fA-F]+;/, '--text-primary: #0f172a;');
    html = html.replace(/--text-secondary:\s*#[0-9a-fA-F]+;/, '--text-secondary: #475569;');
    html = html.replace(/--cyan-500:\s*#[0-9a-fA-F]+;/, '--cyan-500: #0284c7;');
    html = html.replace(/--cyan-400:\s*#[0-9a-fA-F]+;/, '--cyan-400: #0369a1;');
    html = html.replace(/--cyan-glow:\s*[^;]+;/, '--cyan-glow: rgba(2, 132, 199, 0.12);');
    html = html.replace(/--accent-grad:\s*[^;]+;/, '--accent-grad: linear-gradient(135deg, #1e3a8a 0%, #2563eb 50%, #3b82f6 100%);');

    html = html.replace(/\.hero-title\s*\{([\s\S]*?)color:\s*#[0-9a-fA-F]+;/, `.hero-title {$1color: #0f172a;`);
    html = html.replace(/\.safety-card-header\s+h2\s*\{([\s\S]*?)color:\s*[^;]+;/, `.safety-card-header h2 {$1color: #be123c;`);
    html = html.replace(/\.chain-title\s*\{([\s\S]*?)color:\s*#[0-9a-fA-F]+;/, `.chain-title {$1color: #0f172a;`);
    html = html.replace(/\.concept-heading\s*\{([\s\S]*?)color:\s*#[0-9a-fA-F]+;/, `.concept-heading {$1color: #0f172a;`);
    html = html.replace(/\.concept-body-section\s+h4\s*\{([\s\S]*?)color:\s*#[0-9a-fA-F]+;/, `.concept-body-section h4 {$1color: #0f172a;`);
    html = html.replace(/\.concept-body-section\s+p\s*\{([\s\S]*?)color:\s*#[0-9a-fA-F]+;/, `.concept-body-section p {$1color: #334155;`);

    // Remove any duplicate unclosed orphan responsive snippet chunk in Day 1
    html = html.replace(/\s*\.grid-cols-2,\s*\.grid-cols-3[\s\S]*?@media\s*\(min-width:\s*641px\s*\)\s*and\s*\(max-width:\s*1024px\)\s*\{[\s\S]*?\}\s*\}/gi, '');

    // Ensure table has overflow-x-auto
    if (!html.includes('overflow-x-auto') && html.includes('<table')) {
      html = html.replace('<table', '<div class="overflow-x-auto"><table');
      html = html.replace('</table>', '</table></div>');
    }

  } else if (isDay2) {
    // ── DAY 2 SPECIFIC CONVERSIONS ── //
    html = html.replace(/--accent-gradient:\s*[^;]+;/, '--accent-gradient: linear-gradient(135deg, #1e3a8a 0%, #2563eb 100%);');
    html = html.replace(/--glass-bg:\s*[^;]+;/, '--glass-bg: #ffffff;');
    html = html.replace(/--glass-border:\s*[^;]+;/, '--glass-border: #e2e8f0;');
    html = html.replace(/--card-bg:\s*[^;]+;/, '--card-bg: #ffffff;');
    html = html.replace(/--bg-main:\s*[^;]+;/, '--bg-main: #f8fafc;');
    html = html.replace(/--text-main:\s*[^;]+;/, '--text-main: #1e293b;');
    html = html.replace(/--text-muted:\s*[^;]+;/, '--text-muted: #64748b;');

    html = html.replace(
      /body\s*\{[\s\S]*?overflow-x:\s*hidden;\s*\}/,
      `html, body {
            font-family: 'Inter', sans-serif;
            background-color: #f8fafc !important;
            background: #f8fafc !important;
            color: #1e293b !important;
            line-height: 1.65;
            overflow-x: hidden;
        }`
    );

    html = html.replace(
      /\.hero-card\s*\{[\s\S]*?overflow:\s*hidden;\s*\}/,
      `.hero-card {
            background: linear-gradient(135deg, #ffffff 0%, #eff6ff 100%);
            border: 1px solid var(--glass-border);
            border-radius: 1rem;
            padding: 2.25rem 2rem;
            box-shadow: 0 4px 16px rgba(15, 23, 42, 0.04);
            margin-bottom: 2rem;
            position: relative;
            overflow: hidden;
        }`
    );

    // Remove any duplicate unclosed orphan responsive snippet chunk in Day 2
    html = html.replace(/\s*\.grid-cols-2,\s*\.grid-cols-3[\s\S]*?@media\s*\(min-width:\s*641px\s*\)\s*and\s*\(max-width:\s*1024px\)\s*\{[\s\S]*?\}\s*\}/gi, '');

  } else {
    // ── DAYS 3 TO 97 (Tailwind Type C) ── //
    html = html.replace(/<html([^>]*)\s+class="dark"([^>]*)>/i, '<html$1$2>');
    html = html.replace(/<html([^>]*)\s+class='dark'([^>]*)>/i, '<html$1$2>');

    html = html.replace(/darkBg:\s*'#[0-9a-fA-F]+'/, "darkBg: '#f8fafc'");
    html = html.replace(/bg:\s*'#[0-9a-fA-F]+'/, "bg: '#f8fafc'");
    html = html.replace(/surface:\s*'#[0-9a-fA-F]+'/, "surface: '#ffffff'");
    html = html.replace(/cardBg:\s*'#[0-9a-fA-F]+'/, "cardBg: '#ffffff'");
    html = html.replace(/cardHover:\s*'#[0-9a-fA-F]+'/, "cardHover: '#f1f5f9'");
    html = html.replace(/accentBlue:\s*'#[0-9a-fA-F]+'/, "accentBlue: '#1e40af'");
    html = html.replace(/accentIndigo:\s*'#[0-9a-fA-F]+'/, "accentIndigo: '#4338ca'");
    html = html.replace(/accentEmerald:\s*'#[0-9a-fA-F]+'/, "accentEmerald: '#059669'");
    html = html.replace(/accentAmber:\s*'#[0-9a-fA-F]+'/, "accentAmber: '#d97706'");
    html = html.replace(/accentRose:\s*'#[0-9a-fA-F]+'/, "accentRose: '#e11d48'");

    html = html.replace(/class="bg-darkBg text-slate-100/, 'class="bg-[#f8fafc] text-[#1e293b]');
    html = html.replace(/class='bg-darkBg text-slate-100/, "class='bg-[#f8fafc] text-[#1e293b]");

    html = html.replace(/bg-\[#0c1222\]\/80/g, 'bg-white/95');
    html = html.replace(/bg-\[#0c1222\]/g, 'bg-white');
    html = html.replace(/bg-\[#111a30\]/g, 'bg-white');
    html = html.replace(/bg-\[#090e1a\]/g, 'bg-slate-50');
    html = html.replace(/bg-\[#090d16\]/g, 'bg-[#f8fafc]');
  }

  // Ensure ALL pages have the responsive snippet
  if (!html.includes('MOBILE-FIRST RESPONSIVE ENHANCEMENT')) {
    html = html.replace('</style>', `${RESPONSIVE_DAYLIGHT_SNIPPET}\n</style>`);
  } else {
    // Replace old responsive snippet with daylight version
    html = html.replace(
      /\/\* ==========================================================================\s*MOBILE-FIRST RESPONSIVE ENHANCEMENT[\s\S]*?<\/style>/,
      `${RESPONSIVE_DAYLIGHT_SNIPPET}\n</style>`
    );
  }

  return html;
}

module.exports = { convertDayContent };
