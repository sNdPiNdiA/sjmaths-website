const fs = require('fs');
const path = require('path');

const RESPONSIVE_CSS = `
/* ==========================================================================
   MOBILE-FIRST RESPONSIVE ENHANCEMENT (SJMaths ASO Study Hub)
   ========================================================================== */
html, body {
    max-width: 100vw !important;
    overflow-x: hidden !important;
    position: relative;
    background-color: #060911 !important;
    color: #f8fafc !important;
    -webkit-text-size-adjust: 100%;
    text-size-adjust: 100%;
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
}
h2 {
    font-size: clamp(1.2rem, 3.5vw, 1.75rem) !important;
    line-height: 1.3 !important;
    word-break: break-word;
}
h3 {
    font-size: clamp(1.05rem, 3vw, 1.35rem) !important;
    line-height: 1.35 !important;
    word-break: break-word;
}

/* Touch-Optimized Segmented Tab Strip (GUARANTEED HORIZONTAL) */
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
}

/* Responsive Tables & Containers - NEVER override display on .overflow-x-auto */
table {
    max-width: 100% !important;
    width: 100% !important;
    border-collapse: collapse;
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
`;

async function apply() {
  const genModule = await import('./generate_gemini_study_page.mjs');
  const allDays = genModule.parseAllDays();
  const existingDays = allDays.filter(d => fs.existsSync(d.outputPath));

  console.log(`Applying mobile-first responsive enhancements across ${existingDays.length} Day study modules...\n`);

  let modifiedCount = 0;

  for (const d of existingDays) {
    let html = fs.readFileSync(d.outputPath, 'utf8');
    const original = html;

    // 1. Ensure proper viewport meta tag
    if (!html.includes('name="viewport"')) {
      html = html.replace('<head>', '<head>\n    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">');
    }

    // 2. Ensure switchTab has MathJax typesetPromise
    if (html.includes('function switchTab') && !html.includes('MathJax.typesetPromise')) {
      if (html.includes('window.scrollTo')) {
        html = html.replace(/(function\s+switchTab\s*\([^)]*\)\s*\{[\s\S]*?)(window\.scrollTo)/, (match, p1, p2) => {
          return `${p1}if (window.MathJax && window.MathJax.typesetPromise) { window.MathJax.typesetPromise(); }\n            ${p2}`;
        });
      } else {
        html = html.replace(/(function\s+switchTab\s*\([^)]*\)\s*\{[\s\S]*?)(\n\s*\})/, (match, p1, p2) => {
          return `${p1}\n            if (window.MathJax && window.MathJax.typesetPromise) { window.MathJax.typesetPromise(); }${p2}`;
        });
      }
    }

    // 3. Inject or Update RESPONSIVE_CSS
    if (html.includes('MOBILE-FIRST RESPONSIVE ENHANCEMENT')) {
      // Replace existing block
      html = html.replace(/\/\* ==========================================================================[\s\S]*?MOBILE-FIRST RESPONSIVE ENHANCEMENT[\s\S]*?(?=\n\s*<\/style>)/, RESPONSIVE_CSS.trim());
    } else {
      if (html.includes('</style>')) {
        html = html.replace('</style>', `${RESPONSIVE_CSS}\n    </style>`);
      } else if (html.includes('</head>')) {
        html = html.replace('</head>', `    <style>${RESPONSIVE_CSS}</style>\n</head>`);
      }
    }

    if (html !== original) {
      fs.writeFileSync(d.outputPath, html, 'utf8');
      modifiedCount++;
      console.log(`✓ Enhanced Day ${d.day}: ${d.topic}`);
    }
  }

  console.log(`\nSuccessfully applied mobile-first responsive enhancements to ${modifiedCount} / ${existingDays.length} pages.`);
}

apply().catch(console.error);
