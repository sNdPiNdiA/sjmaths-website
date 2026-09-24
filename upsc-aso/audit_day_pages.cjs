const fs = require('fs');
const path = require('path');

async function main() {
  const genModule = await import('./generate_gemini_study_page.mjs');
  const allDays = genModule.parseAllDays();
  const existingDays = allDays.filter(d => fs.existsSync(d.outputPath));

  console.log(`Auditing Math, UI, and UX for all ${existingDays.length} Day Study Modules...\n`);

  let totalPages = existingDays.length;
  let missingMathScript = 0;
  let missingInlineConfig = 0;
  let hasPolyfill = 0;
  let missingTypesetInSwitchTab = 0;
  let missingDarkBody = 0;
  let delimiterMismatchCount = 0;
  let tableOverflowIssues = 0;

  const defectList = [];

  existingDays.forEach(d => {
    const html = fs.readFileSync(d.outputPath, 'utf8');
    const rel = path.relative(path.resolve('.'), d.outputPath).replace(/\\/g, '/');
    const issues = [];

    // 1. MathJax
    const hasMathJax = html.includes('mathjax');
    const hasInlineConfig = html.includes("['$', '$']") || html.includes('["$", "$"]');
    const polyfillPresent = html.includes('polyfill.io');

    if (!hasMathJax) {
      missingMathScript++;
      issues.push('Missing MathJax script');
    } else if (!hasInlineConfig) {
      missingInlineConfig++;
      issues.push('Missing inline dollar ($...$) MathJax configuration');
    }

    if (polyfillPresent) {
      hasPolyfill++;
      issues.push('Contains deprecated/compromised polyfill.io script');
    }

    // 2. Tab switching & Math re-typeset
    const hasSwitchTab = html.includes('function switchTab');
    const hasTypeset = html.includes('MathJax.typesetPromise') || html.includes('MathJax.typeset');
    if (hasSwitchTab && !hasTypeset) {
      missingTypesetInSwitchTab++;
      issues.push('switchTab() does not call MathJax.typesetPromise() for hidden tabs');
    }

    // 3. UI Dark Theme
    const hasDaylightOverride = (html.includes('background-color: #f8fafc !important') || html.includes('background-color:#f8fafc!important') || html.includes('--bg-base: #f8fafc')) && !html.includes('#060911');
    if (!hasDaylightOverride) {
      missingDarkBody++;
      issues.push('Missing stress-free daylight theme #f8fafc override or contains legacy dark void #060911');
    }

    // 4. Tables responsiveness
    const hasTable = html.includes('<table');
    const hasTableOverflow = html.includes('overflow-x-auto') || html.includes('overflow-x: auto') || html.includes('overflow-x:auto');
    if (hasTable && !hasTableOverflow) {
      tableOverflowIssues++;
      issues.push('Contains tables without overflow-x-auto wrapper/CSS (mobile overflow risk)');
    }

    // 5. Delimiter Balance Check (Single $, Double $$, \(...\))
    const codeFree = html.replace(/<script[\s\S]*?<\/script>/gi, '').replace(/<style[\s\S]*?<\/style>/gi, '');
    
    // Count \( and \)
    const openParens = (codeFree.match(/\\\(/g) || []).length;
    const closeParens = (codeFree.match(/\\\)/g) || []).length;
    if (openParens !== closeParens) {
      delimiterMismatchCount++;
      issues.push(`Unbalanced LaTeX parenthesis delimiters: \\( count (${openParens}) != \\) count (${closeParens})`);
    }

    // Count $$
    const doubleDollars = (codeFree.match(/\$\$/g) || []).length;
    if (doubleDollars % 2 !== 0) {
      delimiterMismatchCount++;
      issues.push(`Unbalanced block math delimiters: $$ count is odd (${doubleDollars})`);
    }

    // Count single $
    const totalDollars = (codeFree.match(/\$/g) || []).length;
    const singleDollars = totalDollars - (doubleDollars * 2);
    if (singleDollars % 2 !== 0) {
      delimiterMismatchCount++;
      issues.push(`Unbalanced inline dollar delimiters: $ count is odd (${singleDollars})`);
    }

    // 6. Mobile Responsiveness Checks
    const hasViewport = html.includes('name="viewport"');
    const hasResponsiveCss = html.includes('MOBILE-FIRST RESPONSIVE ENHANCEMENT');
    const hasMathOverflowGuard = html.includes('mjx-container[jax="CHTML"][display="true"]') || html.includes('mjx-container');

    if (!hasViewport) {
      issues.push('Missing <meta name="viewport"> tag');
    }
    if (!hasResponsiveCss) {
      issues.push('Missing MOBILE-FIRST RESPONSIVE ENHANCEMENT styles');
    }
    if (!hasMathOverflowGuard) {
      issues.push('Missing MathJax horizontal overflow guard');
    }

    if (issues.length > 0) {
      defectList.push({
        day: d.day,
        topic: d.topic,
        file: rel,
        issues
      });
    }
  });

  console.log('========================================================================');
  console.log(`               AUDIT SUMMARY OF ${totalPages} GENERATED DAY PAGES`);
  console.log('========================================================================');
  console.log(`- Pages missing inline dollar ($...$) MathJax config: ${missingInlineConfig} / ${totalPages}`);
  console.log(`- Pages with compromised polyfill.io: ${hasPolyfill} / ${totalPages}`);
  console.log(`- Pages where switchTab() misses MathJax.typesetPromise(): ${missingTypesetInSwitchTab} / ${totalPages}`);
  console.log(`- Pages missing stress-free daylight theme override: ${missingDarkBody} / ${totalPages}`);
  console.log(`- Pages with table mobile overflow risk: ${tableOverflowIssues} / ${totalPages}`);
  console.log(`- Pages with LaTeX delimiter balance errors: ${delimiterMismatchCount} / ${totalPages}`);
  console.log(`- Pages with mobile-first responsive architecture: ${totalPages - defectList.filter(d => d.issues.some(i => i.includes('MOBILE-FIRST'))).length} / ${totalPages}`);
  console.log('========================================================================\n');

  if (defectList.length === 0) {
    console.log(`🎉 PERFECT SCORE! All ${totalPages} Day pages passed MathJax, UI, and UX checks with ZERO defects!`);
  } else {
    console.log(`Total pages with 1 or more defects: ${defectList.length} / ${totalPages}\n`);
    defectList.slice(0, 15).forEach(item => {
      console.log(`Day ${item.day}: ${item.topic} (${item.file})`);
      item.issues.forEach(iss => console.log(`   - ${iss}`));
    });
  }
}

main().catch(console.error);
