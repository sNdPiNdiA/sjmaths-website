const fs = require('fs');
const path = require('path');

const BREADCRUMB_CSS = `
/* ==========================================================================
   STANDARD TOP BREADCRUMB NAVIGATION (CLEAN INLINE AERO TRAIL)
   ========================================================================== */
.breadcrumb-nav {
    display: inline-flex !important;
    align-items: center !important;
    flex-wrap: wrap !important;
    gap: 0.35rem 0.5rem !important;
    font-size: 0.8125rem !important;
    color: #94a3b8 !important;
    margin: 0 0 1rem 0 !important;
    padding: 0 !important;
    background: transparent !important;
    border: none !important;
    border-radius: 0 !important;
    line-height: 1.4 !important;
    font-family: 'Inter', system-ui, -apple-system, sans-serif !important;
    box-sizing: border-box !important;
    width: auto !important;
}
.breadcrumb-nav a {
    color: #94a3b8 !important;
    text-decoration: none !important;
    display: inline-flex !important;
    align-items: center !important;
    gap: 0.35rem !important;
    font-weight: 500 !important;
    padding: 0.15rem 0.35rem !important;
    border-radius: 0.375rem !important;
    transition: color 0.15s ease, background-color 0.15s ease !important;
}
.breadcrumb-nav a:hover,
.breadcrumb-nav a:focus {
    color: #38bdf8 !important;
    background-color: rgba(56, 189, 248, 0.12) !important;
    text-decoration: none !important;
}
.breadcrumb-nav .breadcrumb-separator {
    color: #475569 !important;
    font-size: 0.625rem !important;
    display: inline-flex !important;
    align-items: center !important;
    user-select: none !important;
    padding: 0 0.05rem !important;
}
.breadcrumb-nav .breadcrumb-current {
    color: #38bdf8 !important;
    font-weight: 600 !important;
    display: inline-flex !important;
    align-items: center !important;
    padding: 0.15rem 0.45rem !important;
    background-color: rgba(56, 189, 248, 0.1) !important;
    border: 1px solid rgba(56, 189, 248, 0.25) !important;
    border-radius: 0.375rem !important;
    max-width: 100% !important;
    word-break: break-word !important;
}
@media (max-width: 640px) {
    .breadcrumb-nav {
        margin: 0 0 0.75rem 0 !important;
        font-size: 0.75rem !important;
        gap: 0.25rem 0.35rem !important;
    }
    .breadcrumb-nav a,
    .breadcrumb-nav .breadcrumb-current {
        padding: 0.1rem 0.25rem !important;
    }
}`;

function findMainH1(html) {
  const allH1 = [...html.matchAll(/<h1[^>]*>/gi)];
  if (allH1.length === 0) return null;
  if (allH1.length === 1) return allH1[0];

  for (const h of allH1) {
    if (/hero-title|text-3xl|text-4xl|text-5xl|text-2xl/i.test(h[0])) {
      return h;
    }
  }
  const tabPos = html.indexOf('switchTab');
  if (tabPos !== -1) {
    const beforeTabH1 = allH1.filter(h => h.index < tabPos);
    if (beforeTabH1.length > 0) return beforeTabH1[beforeTabH1.length - 1];
  }
  return allH1[allH1.length - 1];
}

function moveBreadcrumbsToTop(html, dayInfo) {
  // 1. Remove all old breadcrumb elements, bottom navs, and leftover comments
  html = html.replace(/<!--\s*TOP BREADCRUMB NAVIGATION\s*-->[\s\S]*?<\/nav>/gi, '');
  html = html.replace(/<nav[^>]*class="[^"]*bottom-breadcrumb-nav[^"]*"[^>]*>[\s\S]*?<\/nav>/gi, '');
  html = html.replace(/<nav[^>]*class="[^"]*breadcrumb-nav[^"]*"[^>]*>[\s\S]*?<\/nav>/gi, '');
  html = html.replace(/<div class="sj-breadcrumbs">[\s\S]*?<\/div>/gi, '');
  html = html.replace(/<!--\s*TOP BREADCRUMB NAVIGATION\s*-->/gi, '');

  // 2. Prepare standardized Schema.org breadcrumb HTML
  const homeUrl = '/';
  const asoUrl = '/upsc-aso/';
  const subjectUrl = `/upsc-aso/${dayInfo.subjectSlug}/`;
  const subjectName = dayInfo.subject;
  const topicTitle = `Day ${dayInfo.day}: ${dayInfo.topic}`;

  const topBreadcrumbHtml = `
            <!-- TOP BREADCRUMB NAVIGATION -->
            <nav class="breadcrumb-nav" aria-label="Breadcrumb" itemscope itemtype="https://schema.org/BreadcrumbList">
                <span itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
                    <a href="${homeUrl}" itemprop="item"><i class="fa-solid fa-house"></i> <span itemprop="name">Home</span></a>
                    <meta itemprop="position" content="1">
                </span>
                <i class="fa-solid fa-chevron-right breadcrumb-separator" aria-hidden="true"></i>
                <span itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
                    <a href="${asoUrl}" itemprop="item"><i class="fa-solid fa-plane"></i> <span itemprop="name">UPSC ASO</span></a>
                    <meta itemprop="position" content="2">
                </span>
                <i class="fa-solid fa-chevron-right breadcrumb-separator" aria-hidden="true"></i>
                <span itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
                    <a href="${subjectUrl}" itemprop="item"><span itemprop="name">${subjectName}</span></a>
                    <meta itemprop="position" content="3">
                </span>
                <i class="fa-solid fa-chevron-right breadcrumb-separator" aria-hidden="true"></i>
                <span class="breadcrumb-current" itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem" aria-current="page">
                    <span itemprop="name">${topicTitle}</span>
                    <meta itemprop="position" content="4">
                </span>
            </nav>`;

  // 3. Update CSS: clean old breadcrumb CSS and inject clean inline trail CSS
  html = html.replace(/\/\* ==========================================================================\s+BOTTOM BREADCRUMB NAVIGATION[\s\S]*?@media \(max-width: 640px\) \{[\s\S]*?\}\s*\}\s*/gi, '');
  html = html.replace(/\/\* ==========================================================================\s+STANDARD TOP BREADCRUMB NAVIGATION[\s\S]*?@media \(max-width: 640px\) \{[\s\S]*?\}\s*\}\s*/gi, '');

  if (html.includes('</style>')) {
    const lastStyleIdx = html.lastIndexOf('</style>');
    html = html.substring(0, lastStyleIdx) + `${BREADCRUMB_CSS}\n</style>` + html.substring(lastStyleIdx + 8);
  } else if (html.includes('</head>')) {
    html = html.replace('</head>', () => `<style>${BREADCRUMB_CSS}</style>\n</head>`);
  }

  // 4. Find the primary hero <h1>
  const mainH1 = findMainH1(html);
  if (!mainH1) return html;
  const h1Pos = mainH1.index;
  const beforeH1 = html.substring(0, h1Pos);

  // Look for the enclosing parent container of this H1
  const lastSection = beforeH1.lastIndexOf('<section');
  const lastSectionClose = beforeH1.lastIndexOf('</section>');
  const lastHeader = beforeH1.lastIndexOf('<header');
  const lastHeaderClose = beforeH1.lastIndexOf('</header>');
  const lastMain = beforeH1.lastIndexOf('<main');
  const lastMainClose = beforeH1.lastIndexOf('</main>');

  // Case 1: Inside <section> (and not closed before H1)
  if (lastSection > lastSectionClose && lastSection > lastHeader && lastSection > lastMain) {
    const sectionChunk = beforeH1.substring(lastSection);
    const innerDiv = sectionChunk.match(/(<div[^>]*class="[^"]*(?:max-w-7xl|container|relative\s+z-10|px-)[^"]*"[^>]*>)/i);
    if (innerDiv) {
      const insertPos = lastSection + sectionChunk.indexOf(innerDiv[0]) + innerDiv[0].length;
      html = html.substring(0, insertPos) + '\n' + topBreadcrumbHtml + html.substring(insertPos);
      return html;
    } else {
      const sectionEnd = lastSection + sectionChunk.indexOf('>') + 1;
      html = html.substring(0, sectionEnd) + '\n' + topBreadcrumbHtml + html.substring(sectionEnd);
      return html;
    }
  }

  // Case 2: Inside <header> (and not closed before H1)
  if (lastHeader > lastHeaderClose && lastHeader > lastSection) {
    const headerChunk = beforeH1.substring(lastHeader);
    const innerDiv = headerChunk.match(/(<div[^>]*class="[^"]*(?:max-w-7xl|container|main-container|px-)[^"]*"[^>]*>)/i);
    if (innerDiv) {
      const insertPos = lastHeader + headerChunk.indexOf(innerDiv[0]) + innerDiv[0].length;
      html = html.substring(0, insertPos) + '\n' + topBreadcrumbHtml + html.substring(insertPos);
      return html;
    } else {
      const headerEnd = lastHeader + headerChunk.indexOf('>') + 1;
      html = html.substring(0, headerEnd) + '\n' + topBreadcrumbHtml + html.substring(headerEnd);
      return html;
    }
  }

  // Case 3: Inside <main> (Day 7)
  if (lastMain > lastMainClose) {
    const mainChunk = beforeH1.substring(lastMain);
    const mainEnd = lastMain + mainChunk.indexOf('>') + 1;
    html = html.substring(0, mainEnd) + '\n' + topBreadcrumbHtml + html.substring(mainEnd);
    return html;
  }

  // Case 4: Inside <div class="main-container"> or <div class="container"> (Day 1, 2)
  const lastContainer = Math.max(
    beforeH1.lastIndexOf('class="main-container"'),
    beforeH1.lastIndexOf('class="container"')
  );
  if (lastContainer !== -1) {
    const divOpen = beforeH1.lastIndexOf('<div', lastContainer);
    const divEnd = divOpen + beforeH1.substring(divOpen).indexOf('>') + 1;
    html = html.substring(0, divEnd) + '\n' + topBreadcrumbHtml + html.substring(divEnd);
    return html;
  }

  // Fallback: directly before H1
  html = html.substring(0, h1Pos) + topBreadcrumbHtml + '\n' + html.substring(h1Pos);
  return html;
}

// Batch apply to all days
async function applyToAllDays() {
  const gen = await import('./generate_gemini_study_page.mjs');
  const days = gen.parseAllDays();
  console.log(`Relocating Breadcrumbs to TOP (Above H1 and Above Tabs) across ${days.length} days...`);

  let updatedCount = 0;
  let alreadyHasCount = 0;
  let missingFiles = 0;

  days.forEach(d => {
    if (!fs.existsSync(d.outputPath)) {
      missingFiles++;
      return;
    }

    const originalHtml = fs.readFileSync(d.outputPath, 'utf8');
    const updatedHtml = moveBreadcrumbsToTop(originalHtml, d);

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
  applyToAllDays();
}

module.exports = { moveBreadcrumbsToTop, findMainH1 };
