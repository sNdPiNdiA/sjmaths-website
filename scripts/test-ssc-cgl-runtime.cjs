const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({
    viewport: { width: 1280, height: 800 }
  });
  const page = await context.newPage();

  const errors = [];
  const warnings = [];
  const failedRequests = [];

  page.on('console', msg => {
    if (msg.type() === 'error') {
      errors.push({ url: page.url(), text: msg.text() });
    } else if (msg.type() === 'warning') {
      warnings.push({ url: page.url(), text: msg.text() });
    }
  });

  page.on('pageerror', err => {
    errors.push({ url: page.url(), text: err.message });
  });

  page.on('requestfailed', req => {
    // Ignore external ads/analytics
    if (req.url().includes('google') || req.url().includes('firestore')) return;
    failedRequests.push({ page: page.url(), url: req.url(), error: req.failure()?.errorText });
  });

  const testUrls = [
    'http://localhost:8082/ssc-cgl/',
    'http://localhost:8082/ssc-cgl/computer-knowledge/',
    'http://localhost:8082/ssc-cgl/english/',
    'http://localhost:8082/ssc-cgl/finance-economics/',
    'http://localhost:8082/ssc-cgl/general-awareness/',
    'http://localhost:8082/ssc-cgl/quantitative-aptitude/',
    'http://localhost:8082/ssc-cgl/reasoning/',
    'http://localhost:8082/ssc-cgl/statistics/',
    // Sample topic pages from each subject
    'http://localhost:8082/ssc-cgl/computer-knowledge/keyboard-shortcuts/',
    'http://localhost:8082/ssc-cgl/quantitative-aptitude/percentage/',
    'http://localhost:8082/ssc-cgl/english/reading-comprehension/',
    'http://localhost:8082/ssc-cgl/reasoning/syllogism/',
    'http://localhost:8082/ssc-cgl/finance-economics/basic-concepts-and-conventions/',
    'http://localhost:8082/ssc-cgl/general-awareness/geography/atmosphere-and-weather-parameters/',
    'http://localhost:8082/ssc-cgl/general-awareness/economy/money-supply-measures-m1-m4-and-inflation-types/',
    'http://localhost:8082/ssc-cgl/general-awareness/history-and-culture/delhi-sultanate/'
  ];

  console.log(`Testing ${testUrls.length} key URLs in Playwright...`);

  for (const url of testUrls) {
    try {
      const resp = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 10000 });
      const status = resp ? resp.status() : 'no response';
      if (status >= 400) {
        errors.push({ url, text: `HTTP Status ${status}` });
      }

      // Check header and footer rendering
      const headerRendered = await page.evaluate(() => {
        const hc = document.getElementById('header-container');
        return hc && hc.children.length > 0;
      });
      const footerRendered = await page.evaluate(() => {
        const fc = document.getElementById('footer-container');
        return fc && fc.children.length > 0;
      });

      // Check for horizontal overflow (bug on mobile or desktop)
      const hasHorizontalScroll = await page.evaluate(() => {
        return document.documentElement.scrollWidth > window.innerWidth;
      });

      console.log(`[${status}] ${url} | header: ${headerRendered} | footer: ${footerRendered} | overflow: ${hasHorizontalScroll}`);

      // If topic page, test tab interaction
      if (url.includes('/keyboard-shortcuts/')) {
        console.log('  Testing tab interaction on keyboard-shortcuts...');
        const tabPractice = await page.$('button[data-tab="practice"], .tab-btn[data-tab="tab-practice"], #tab-practice-btn');
        if (tabPractice) {
          await tabPractice.click();
          await page.waitForTimeout(300);
        }
      }
    } catch (e) {
      errors.push({ url, text: `Navigation exception: ${e.message}` });
    }
  }

  await browser.close();

  console.log('\n=== PLAYWRIGHT AUDIT RESULTS ===');
  console.log(`Errors encountered: ${errors.length}`);
  errors.forEach(e => console.log(`  ERR: [${e.url}] ${e.text}`));

  console.log(`\nFailed Requests: ${failedRequests.length}`);
  failedRequests.forEach(r => console.log(`  FAILED REQ: [${r.page}] ${r.url} (${r.error})`));

  console.log(`\nWarnings: ${warnings.length}`);
  warnings.slice(0, 10).forEach(w => console.log(`  WARN: [${w.url}] ${w.text}`));
})();
