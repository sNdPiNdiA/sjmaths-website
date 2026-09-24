const fs = require('fs');

async function verifyBreadcrumbs() {
  const gen = await import('./generate_gemini_study_page.mjs');
  const days = gen.parseAllDays();
  console.log(`Auditing Bottom Breadcrumbs across ${days.length} days...`);

  let countPass = 0;
  const issues = [];

  days.forEach(d => {
    if (!fs.existsSync(d.outputPath)) return;
    const html = fs.readFileSync(d.outputPath, 'utf8');

    const checks = {
      hasNav: html.includes('<nav class="bottom-breadcrumb-nav"'),
      hasCss: html.includes('.bottom-breadcrumb-nav'),
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
  console.log(`BOTTOM BREADCRUMBS VERIFICATION:`);
  console.log(`Passed 100% of checks: ${countPass} / 97`);
  console.log(`Issues found: ${issues.length}`);
  if (issues.length > 0) {
    console.log('Issues details:', issues);
  }
  console.log(`======================================================`);
}

verifyBreadcrumbs();
