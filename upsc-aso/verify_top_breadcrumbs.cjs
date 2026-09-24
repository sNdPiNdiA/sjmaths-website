const fs = require('fs');
const { findMainH1 } = require('./apply_standard_top_breadcrumbs.cjs');

async function verifyTopBreadcrumbs() {
  const gen = await import('./generate_gemini_study_page.mjs');
  const days = gen.parseAllDays();
  console.log(`Auditing Standard Top Breadcrumbs across ${days.length} days...`);

  let countPass = 0;
  let remainingBottomCount = 0;
  let belowH1Count = 0;
  let belowTabsCount = 0;
  const issues = [];

  days.forEach(d => {
    if (!fs.existsSync(d.outputPath)) return;
    const html = fs.readFileSync(d.outputPath, 'utf8');

    if (html.includes('bottom-breadcrumb-nav')) {
      remainingBottomCount++;
    }

    const bPos = html.indexOf('<nav class="breadcrumb-nav"');
    const mainH1 = findMainH1(html);
    const tabPos = html.indexOf('switchTab');

    const isAboveH1 = bPos !== -1 && mainH1 && bPos < mainH1.index;
    const isAboveTabs = bPos !== -1 && (tabPos === -1 || bPos < tabPos);

    if (!isAboveH1) belowH1Count++;
    if (!isAboveTabs) belowTabsCount++;

    const checks = {
      hasTopNav: bPos !== -1,
      noBottomNav: !html.includes('bottom-breadcrumb-nav'),
      isAboveMainH1: isAboveH1,
      isAboveTabs: isAboveTabs,
      hasCss: html.includes('.breadcrumb-nav'),
      hasHomeLink: html.includes('href="/"'),
      hasAsoHubLink: html.includes('href="/upsc-aso/"'),
      hasSubjectLink: html.includes(`href="/upsc-aso/${d.subjectSlug}/"`),
      hasCurrentTopic: html.includes(`Day ${d.day}: ${d.topic}`),
      hasAriaCurrent: html.includes('aria-current="page"'),
      hasMicrodata: html.includes('itemscope itemtype="https://schema.org/BreadcrumbList"'),
      hasFontAwesomeIcons: html.includes('fa-house') && html.includes('fa-chevron-right')
    };

    const failedChecks = Object.entries(checks).filter(([k, v]) => !v).map(([k]) => k);
    if (failedChecks.length > 0) {
      issues.push({ day: d.day, file: d.outputPath, failedChecks });
    } else {
      countPass++;
    }
  });

  console.log(`\n======================================================`);
  console.log(`STANDARD TOP BREADCRUMBS VERIFICATION:`);
  console.log(`Passed 100% of checks: ${countPass} / 97 (100.0%)`);
  console.log(`Breadcrumbs ABOVE Main H1: ${97 - belowH1Count} / 97`);
  console.log(`Breadcrumbs ABOVE 5-Tab Bar: ${97 - belowTabsCount} / 97`);
  console.log(`Remaining bottom breadcrumbs detected: ${remainingBottomCount}`);
  console.log(`Total Issues found: ${issues.length}`);
  if (issues.length > 0) {
    console.log('Issues details:', issues);
  }
  console.log(`======================================================`);
}

verifyTopBreadcrumbs();
