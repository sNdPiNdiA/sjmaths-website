const { chromium } = require('playwright');
const path = require('path');

async function inspectPage(url, label) {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1280, height: 800 } });
  await page.goto(url, { waitUntil: 'networkidle' });

  const metrics = await page.evaluate(() => {
    const results = [];
    
    // Check main layout containers
    const containers = [
      '.study-layout', '.study-toc', '.study-article',
      '.study-main', '.main-content', '.ib-hero', '.study-guide-layout',
      '.study-tabs', '.study-tab-panel.active'
    ];
    
    for (const sel of containers) {
      const el = document.querySelector(sel);
      if (el) {
        const rect = el.getBoundingClientRect();
        const style = window.getComputedStyle(el);
        results.push({
          selector: sel,
          display: style.display,
          width: rect.width,
          height: rect.height,
          top: rect.top,
          marginTop: style.marginTop,
          marginBottom: style.marginBottom,
          paddingTop: style.paddingTop,
          paddingBottom: style.paddingBottom
        });
      }
    }

    // Check sibling vertical gaps
    const allSections = Array.from(document.querySelectorAll('section, article, nav, header, main, footer'));
    const gaps = [];
    for (let i = 0; i < allSections.length - 1; i++) {
      const a = allSections[i].getBoundingClientRect();
      const b = allSections[i+1].getBoundingClientRect();
      const gap = b.top - a.bottom;
      if (gap > 60) {
        gaps.push({
          from: allSections[i].tagName + '.' + allSections[i].className,
          to: allSections[i+1].tagName + '.' + allSections[i+1].className,
          gap: Math.round(gap)
        });
      }
    }

    return { results, gaps, scrollHeight: document.body.scrollHeight };
  });

  const screenshotPath = path.join(__dirname, `screenshot_${label}.png`);
  await page.screenshot({ path: screenshotPath, fullPage: false });
  await browser.close();

  return { metrics, screenshotPath };
}

async function run() {
  console.log('Inspecting Functions HL Hub:');
  const r1 = await inspectPage('http://localhost:8082/ib/dp-mathematics/analysis-and-approaches-hl/functions/', 'hl_functions');
  console.log('Functions HL Metrics:', JSON.stringify(r1.metrics, null, 2));

  console.log('\nInspecting AA HL Guide:');
  const r2 = await inspectPage('http://localhost:8082/ib/dp-mathematics/analysis-and-approaches-hl/functions/modulus-functions-and-inequalities/', 'hl_modulus');
  console.log('Modulus Guide Metrics:', JSON.stringify(r2.metrics, null, 2));

  console.log('\nInspecting SL Calculus Guide:');
  const r3 = await inspectPage('http://localhost:8082/ib/dp-mathematics/analysis-and-approaches-sl/calculus/limits-and-first-derivatives/', 'sl_limits');
  console.log('SL Limits Guide Metrics:', JSON.stringify(r3.metrics, null, 2));
}

run().catch(console.error);
