const fs = require('fs');
const path = require('path');

const BREADCRUMB_CSS = `
/* ==========================================================================
   BOTTOM BREADCRUMB NAVIGATION (AERONAUTICAL DARK THEME & MOBILE RESPONSIVE)
   ========================================================================== */
.bottom-breadcrumb-nav {
    width: 100% !important;
    max-width: 1200px !important;
    margin: 2.5rem auto 1.5rem auto !important;
    padding: 0 1rem !important;
    box-sizing: border-box !important;
}
.bottom-breadcrumb-container {
    background: rgba(12, 18, 34, 0.85) !important;
    backdrop-filter: blur(12px) !important;
    -webkit-backdrop-filter: blur(12px) !important;
    border: 1px solid rgba(255, 255, 255, 0.08) !important;
    border-radius: 0.85rem !important;
    padding: 0.75rem 1.15rem !important;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.35) !important;
}
.bottom-breadcrumb-list {
    display: flex !important;
    align-items: center !important;
    flex-wrap: wrap !important;
    gap: 0.35rem 0.5rem !important;
    margin: 0 !important;
    padding: 0 !important;
    list-style: none !important;
    font-family: 'Inter', system-ui, -apple-system, sans-serif !important;
    font-size: 0.8125rem !important;
    line-height: 1.4 !important;
}
.bottom-breadcrumb-item {
    display: inline-flex !important;
    align-items: center !important;
}
.bottom-breadcrumb-link {
    display: inline-flex !important;
    align-items: center !important;
    gap: 0.35rem !important;
    color: #94a3b8 !important;
    text-decoration: none !important;
    padding: 0.25rem 0.5rem !important;
    border-radius: 0.375rem !important;
    font-weight: 500 !important;
    transition: color 0.15s ease, background-color 0.15s ease !important;
}
.bottom-breadcrumb-link:hover,
.bottom-breadcrumb-link:focus {
    color: #38bdf8 !important;
    background-color: rgba(56, 189, 248, 0.1) !important;
    text-decoration: none !important;
}
.bottom-breadcrumb-sep {
    display: inline-flex !important;
    align-items: center !important;
    color: #475569 !important;
    font-size: 0.625rem !important;
    user-select: none !important;
    padding: 0 0.1rem !important;
}
.bottom-breadcrumb-current {
    display: inline-flex !important;
    align-items: center !important;
    color: #38bdf8 !important;
    font-weight: 600 !important;
    padding: 0.25rem 0.55rem !important;
    background-color: rgba(56, 189, 248, 0.12) !important;
    border-radius: 0.375rem !important;
    border: 1px solid rgba(56, 189, 248, 0.25) !important;
    max-width: 100% !important;
    word-break: break-word !important;
}
@media (max-width: 640px) {
    .bottom-breadcrumb-nav {
        margin: 1.75rem auto 1rem auto !important;
        padding: 0 0.5rem !important;
    }
    .bottom-breadcrumb-container {
        padding: 0.6rem 0.75rem !important;
        border-radius: 0.65rem !important;
    }
    .bottom-breadcrumb-list {
        font-size: 0.75rem !important;
        gap: 0.25rem 0.35rem !important;
    }
    .bottom-breadcrumb-link,
    .bottom-breadcrumb-current {
        padding: 0.15rem 0.35rem !important;
    }
}
`;

function generateBottomBreadcrumbsHtml(dayInfo) {
  const { day, subject, subjectSlug, topic } = dayInfo;
  return `
<!-- BOTTOM BREADCRUMB NAVIGATION -->
<nav class="bottom-breadcrumb-nav" aria-label="Breadcrumb">
    <div class="bottom-breadcrumb-container">
        <ol class="bottom-breadcrumb-list" itemscope itemtype="https://schema.org/BreadcrumbList">
            <li class="bottom-breadcrumb-item" itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
                <a href="/" class="bottom-breadcrumb-link" itemprop="item">
                    <i class="fa-solid fa-house"></i>
                    <span itemprop="name">Home</span>
                </a>
                <meta itemprop="position" content="1">
            </li>
            <li class="bottom-breadcrumb-sep" aria-hidden="true"><i class="fa-solid fa-chevron-right"></i></li>
            <li class="bottom-breadcrumb-item" itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
                <a href="/upsc-aso/" class="bottom-breadcrumb-link" itemprop="item">
                    <i class="fa-solid fa-plane"></i>
                    <span itemprop="name">UPSC ASO</span>
                </a>
                <meta itemprop="position" content="2">
            </li>
            <li class="bottom-breadcrumb-sep" aria-hidden="true"><i class="fa-solid fa-chevron-right"></i></li>
            <li class="bottom-breadcrumb-item" itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
                <a href="/upsc-aso/${subjectSlug}/" class="bottom-breadcrumb-link" itemprop="item">
                    <span itemprop="name">${subject}</span>
                </a>
                <meta itemprop="position" content="3">
            </li>
            <li class="bottom-breadcrumb-sep" aria-hidden="true"><i class="fa-solid fa-chevron-right"></i></li>
            <li class="bottom-breadcrumb-item bottom-breadcrumb-current" itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem" aria-current="page">
                <span itemprop="name">Day ${day}: ${topic}</span>
                <meta itemprop="position" content="4">
            </li>
        </ol>
    </div>
</nav>
`;
}

function applyBottomBreadcrumbsToHtml(html, dayInfo) {
  const breadcrumbHtml = generateBottomBreadcrumbsHtml(dayInfo);

  // 1. Inject CSS if not present
  if (!html.includes('.bottom-breadcrumb-nav')) {
    if (html.includes('</style>')) {
      const lastStyleIdx = html.lastIndexOf('</style>');
      html = html.substring(0, lastStyleIdx) + `${BREADCRUMB_CSS}\n</style>` + html.substring(lastStyleIdx + 8);
    } else if (html.includes('</head>')) {
      html = html.replace('</head>', () => `<style>${BREADCRUMB_CSS}</style>\n</head>`);
    }
  }

  // 2. If already has bottom-breadcrumb-nav markup, replace it cleanly (idempotent)
  if (html.includes('<nav class="bottom-breadcrumb-nav"') || html.includes("class='bottom-breadcrumb-nav'")) {
    html = html.replace(/<!--\s*BOTTOM BREADCRUMB NAVIGATION\s*-->[\s\S]*?<\/nav>/i, () => breadcrumbHtml.trim());
    return html;
  }

  // 3. Find optimal insertion point
  // Priority 1: Right before footer navigation comment (78 pages)
  const commentMatch = html.match(/<!--\s*(?:=================\s*)?(?:page\s+navigation\s+footer|footer\s+navigation)(?:\s*=================)?\s*-->/i);
  if (commentMatch) {
    const idx = commentMatch.index;
    return html.substring(0, idx) + breadcrumbHtml + '\n' + html.substring(idx);
  }

  // Priority 2: Right before <footer tag
  if (html.includes('<footer')) {
    const fIdx = html.indexOf('<footer');
    return html.substring(0, fIdx) + breadcrumbHtml + '\n' + html.substring(fIdx);
  }

  // Priority 3: Right before page-footer-nav / page-nav-footer / page-footer / footer-nav
  const navContainerMatch = html.match(/<(?:div|nav)[^>]*(?:page-footer-nav|page-nav-footer|page-footer|footer-nav)[^>]*>/i);
  if (navContainerMatch) {
    const idx = navContainerMatch.index;
    return html.substring(0, idx) + breadcrumbHtml + '\n' + html.substring(idx);
  }

  // Priority 4: Look for nav button strip in main before </main>
  if (html.includes('</main>')) {
    const mIdx = html.indexOf('</main>');
    const beforeMain = html.substring(0, mIdx);
    const subSnippet = beforeMain.substring(Math.max(0, mIdx - 1200));
    const navMatch = subSnippet.match(/<div[^>]*class="[^"]*(?:flex[^"]*(?:justify-between|items-center)|border-t|mt-12)[^"]*"[^>]*>[\s\S]*?(?:Day\s+\d+|Previous|Next)[\s\S]*?<\/div>/i);
    
    if (navMatch) {
      const matchPos = Math.max(0, mIdx - 1200) + navMatch.index;
      return html.substring(0, matchPos) + breadcrumbHtml + '\n' + html.substring(matchPos);
    } else {
      return html.substring(0, mIdx) + breadcrumbHtml + '\n' + html.substring(mIdx);
    }
  }

  // Fallback: before </body>
  if (html.includes('</body>')) {
    const bIdx = html.indexOf('</body>');
    return html.substring(0, bIdx) + breadcrumbHtml + '\n' + html.substring(bIdx);
  }

  return html + breadcrumbHtml;
}

// Batch apply to all days
async function applyToAllDays() {
  const gen = await import('./generate_gemini_study_page.mjs');
  const days = gen.parseAllDays();
  console.log(`Processing ${days.length} days for Bottom Breadcrumb Navigation...`);

  let updatedCount = 0;
  let alreadyHasCount = 0;
  let missingFiles = 0;

  days.forEach(d => {
    if (!fs.existsSync(d.outputPath)) {
      missingFiles++;
      return;
    }

    const originalHtml = fs.readFileSync(d.outputPath, 'utf8');
    const updatedHtml = applyBottomBreadcrumbsToHtml(originalHtml, d);

    if (originalHtml !== updatedHtml) {
      fs.writeFileSync(d.outputPath, updatedHtml, 'utf8');
      updatedCount++;
    } else {
      alreadyHasCount++;
    }
  });

  console.log(`\n================ SUMMARY ================`);
  console.log(`Updated Files: ${updatedCount}`);
  console.log(`Unchanged / Already Current: ${alreadyHasCount}`);
  console.log(`Missing Files (e.g. Days 98-100 not generated yet): ${missingFiles}`);
  console.log(`Total Study Days Processed: ${updatedCount + alreadyHasCount}`);
}

if (require.main === module) {
  applyToAllDays().catch(err => {
    console.error('Error applying bottom breadcrumbs:', err);
    process.exit(1);
  });
}

module.exports = {
  BREADCRUMB_CSS,
  generateBottomBreadcrumbsHtml,
  applyBottomBreadcrumbsToHtml,
  applyToAllDays
};
