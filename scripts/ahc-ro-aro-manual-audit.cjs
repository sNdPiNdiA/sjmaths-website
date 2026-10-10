const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const { chromium } = require(require.resolve('playwright', { paths: [process.cwd()] }));
const root = process.cwd();
const url = 'https://sjmaths.com/ahc-ro-aro/';
const mime = { '.html': 'text/html', '.js': 'text/javascript', '.css': 'text/css', '.json': 'application/json', '.png': 'image/png', '.jpg': 'image/jpeg', '.svg': 'image/svg+xml', '.woff2': 'font/woff2', '.ico': 'image/x-icon' };

async function routeFixtures(page) {
  const evidence = { errors: [], missing: [] };
  page.on('pageerror', error => evidence.errors.push(error.message));
  page.on('console', message => { if (message.type() === 'error') evidence.errors.push(message.text()); });
  await page.route('**/*', async route => {
    const requestUrl = new URL(route.request().url());
    if (['sjmaths.com', 'www.sjmaths.com'].includes(requestUrl.hostname)) {
      const relative = decodeURIComponent(requestUrl.pathname).replace(/^\/+/, '');
      let file = path.resolve(root, relative || 'index.html');
      if (fs.existsSync(file) && fs.statSync(file).isDirectory()) file = path.join(file, 'index.html');
      if (!fs.existsSync(file) && !path.extname(file)) file = path.join(file, 'index.html');
      if (!file.startsWith(path.resolve(root) + path.sep) || !fs.existsSync(file) || !fs.statSync(file).isFile()) {
        evidence.missing.push(requestUrl.pathname);
        return route.fulfill({ status: 404, body: 'Not found' });
      }
      return route.fulfill({ contentType: mime[path.extname(file)] || 'application/octet-stream', body: fs.readFileSync(file) });
    }
    if (requestUrl.hostname === 'firestore.googleapis.com') return route.fulfill({ status: 200, contentType: 'application/json', body: '{}' });
    if (/\.m?js$/i.test(requestUrl.pathname)) return route.fulfill({ status: 200, contentType: 'text/javascript', body: '' });
    if (/\.css$/i.test(requestUrl.pathname)) return route.fulfill({ status: 200, contentType: 'text/css', body: '' });
    return route.fulfill({ status: 204, body: '' });
  });
  return evidence;
}

(async () => {
  const browser = await chromium.launch({ headless: true });
  const results = [];
  try {
    for (const width of [390, 1280]) {
      const context = await browser.newContext({ viewport: { width, height: 900 }, reducedMotion: 'reduce', serviceWorkers: 'block' });
      await context.addInitScript(() => {
        sessionStorage.setItem('sj_auth_gate_skipped', 'true');
        localStorage.removeItem('sjmaths_preferred_language');
        localStorage.removeItem('sj_pref_lang');
        if (localStorage.getItem('ahc-ro-aro-syllabus-progress') === null) {
          localStorage.setItem('ahc-ro-aro-syllabus-progress', '{malformed');
        }
      });
      const page = await context.newPage();
      const evidence = await routeFixtures(page);
      const res = await page.goto(url, { waitUntil: 'domcontentloaded' });
      assert.equal(res.status(), 200);
      await page.locator('#headerLangToggleBtn').waitFor({ state: 'visible' });
      await page.waitForFunction(() => document.body.classList.contains('lang-hi'));
      const state = await page.evaluate(() => ({
        lang: document.documentElement.lang,
        htmlClasses: [...document.documentElement.classList],
        bodyClasses: [...document.body.classList],
        headerLangText: document.querySelector('#headerLangText')?.textContent,
        href: document.querySelector('a.syllabus-link')?.getAttribute('href'),
        hindiVisible: [...document.querySelectorAll('.lang-hi')].filter(e => getComputedStyle(e).display !== 'none').length,
        englishVisible: [...document.querySelectorAll('.lang-en')].filter(e => getComputedStyle(e).display !== 'none').length,
        overflow: Math.max(0, document.documentElement.scrollWidth - innerWidth),
      }));
      console.log('Initial state', width, JSON.stringify(state));
      console.log('First topic visibility', JSON.stringify(await page.locator('a.syllabus-link .lang-hi').first().evaluate(el => ({
        inline: el.style.display,
        display: getComputedStyle(el).display,
        rect: el.getBoundingClientRect().toJSON(),
        ancestors: [...function* () { for (let node = el.parentElement; node; node = node.parentElement) yield node; }()].slice(0, 7).map(node => ({ tag: node.tagName, className: node.className, display: getComputedStyle(node).display, hidden: node.hidden, open: node.open })),
      }))));
      assert.equal(state.lang, 'hi');
      assert.equal(state.headerLangText, 'English');
      assert.ok(state.hindiVisible > 0);
      assert.equal(state.englishVisible, 0);
      assert.ok(!state.href.includes('/hi/'));
      assert.equal(state.overflow, 0);

      await page.locator('a.syllabus-link').first().evaluate(el => { const details = el.closest('details'); if (details) details.open = true; });
      await page.locator('a.syllabus-link .lang-hi').first().evaluate(el => el.click());
      await page.waitForURL('**/ahc-ro-aro/general-science/units-measurements/');
      const progressAfterLinkClick = await page.evaluate(() => localStorage.getItem('ahc-ro-aro-syllabus-progress'));
      assert.equal(progressAfterLinkClick, '{malformed', 'opening a lesson link must not toggle its progress checkbox');
      await page.goBack({ waitUntil: 'domcontentloaded' });
      await page.waitForFunction(() => document.body.classList.contains('lang-hi'));
      await page.waitForFunction(() => document.querySelectorAll('.syllabus-checkbox').length > 0);

      await page.locator('#headerLangToggleBtn').click();
      await page.waitForFunction(() => document.documentElement.lang === 'en');
      const englishState = await page.evaluate(() => ({
        hindiVisible: [...document.querySelectorAll('.lang-hi')].filter(e => getComputedStyle(e).display !== 'none').length,
        englishVisible: [...document.querySelectorAll('.lang-en')].filter(e => getComputedStyle(e).display !== 'none').length,
        href: document.querySelector('a.syllabus-link')?.getAttribute('href'),
      }));
      assert.equal(englishState.hindiVisible, 0);
      assert.ok(englishState.englishVisible > 0);
      assert.ok(!englishState.href.includes('/hi/'));
      await page.locator('#headerLangToggleBtn').click();
      await page.waitForFunction(() => document.documentElement.lang === 'hi');

      await page.locator('.tab-btn[data-tab="stage2"]').click();
      assert.equal(await page.locator('#activeProgressTitle').textContent(), 'Stage II (Mains)');
      assert.equal(await page.locator('#panel-stage2').evaluate(el => el.classList.contains('active')), true);
      await page.locator('.tab-btn[data-tab="stage1"]').click();
      await page.locator('#panel-stage1 .syllabus-checkbox').first().check();
      const secondPage = await context.newPage();
      const secondEvidence = await routeFixtures(secondPage);
      await secondPage.goto(url, { waitUntil: 'domcontentloaded' });
      await secondPage.waitForFunction(() => document.querySelectorAll('.syllabus-checkbox').length > 0);
      assert.equal(await secondPage.locator('#panel-stage1 .syllabus-checkbox').first().isChecked(), true);
      await secondPage.locator('#panel-stage1 .syllabus-checkbox').nth(1).check();
      await page.waitForFunction(() => document.querySelectorAll('.syllabus-checkbox')[1].checked);
      const multiTab = await page.evaluate(() => ({
        checks: [...document.querySelectorAll('.syllabus-checkbox')].slice(0, 2).map(cb => cb.checked),
        value: JSON.parse(localStorage.getItem('ahc-ro-aro-syllabus-progress')),
      }));
      assert.deepEqual(multiTab.checks, [true, true]);
      assert.equal(Object.values(multiTab.value).filter(Boolean).length, 2);
      results.push({ width, ...state, multiTab, runtimeErrors: evidence.errors, missing: evidence.missing, secondTabErrors: secondEvidence.errors, secondTabMissing: secondEvidence.missing });

      const secondaryUrl = 'https://sjmaths.com/ahc-ro-aro/syllabus/';
      const secondaryPage = await context.newPage();
      const secondaryEvidence = await routeFixtures(secondaryPage);
      await secondaryPage.goto(secondaryUrl, { waitUntil: 'domcontentloaded' });
      await secondaryPage.locator('#headerLangToggleBtn').waitFor({ state: 'visible' });
      const secondaryState = await secondaryPage.evaluate(() => ({
        lang: document.documentElement.lang,
        href: document.querySelector('a.syllabus-link')?.getAttribute('href'),
        hindiVisible: [...document.querySelectorAll('.lang-hi')].filter(e => getComputedStyle(e).display !== 'none').length,
        englishVisible: [...document.querySelectorAll('.lang-en')].filter(e => getComputedStyle(e).display !== 'none').length,
        overflow: Math.max(0, document.documentElement.scrollWidth - innerWidth),
        progress: localStorage.getItem('ahc-ro-aro-syllabus-progress'),
      }));
      assert.equal(secondaryState.lang, 'hi');
      assert.ok(secondaryState.hindiVisible > 0);
      assert.equal(secondaryState.englishVisible, 0);
      assert.ok(!secondaryState.href.includes('/hi/'));
      assert.equal(secondaryState.overflow, 0);
      await secondaryPage.locator('a.syllabus-link').first().evaluate(el => { const details = el.closest('details'); if (details) details.open = true; });
      await secondaryPage.locator('a.syllabus-link .lang-hi').first().evaluate(el => el.click());
      await secondaryPage.waitForURL(url => url.pathname !== '/ahc-ro-aro/syllabus/');
      assert.equal(await secondaryPage.evaluate(() => localStorage.getItem('ahc-ro-aro-syllabus-progress')), secondaryState.progress);
      await secondaryPage.goBack({ waitUntil: 'domcontentloaded' });
      await secondaryPage.waitForFunction(() => document.querySelectorAll('.syllabus-checkbox').length > 0);
      const secondaryCheckbox = secondaryPage.locator('#panel-stage1 .syllabus-checkbox').nth(2);
      const secondaryCheckboxId = await secondaryCheckbox.getAttribute('id');
      await secondaryCheckbox.evaluate(el => { const details = el.closest('details'); if (details) details.open = true; });
      await secondaryCheckbox.check();
      const secondaryProgress = await secondaryPage.evaluate(() => JSON.parse(localStorage.getItem('ahc-ro-aro-syllabus-progress')));
      assert.equal(secondaryProgress[secondaryCheckboxId], true);
      results[results.length - 1].secondaryHub = { ...secondaryState, runtimeErrors: secondaryEvidence.errors, missing: secondaryEvidence.missing };
      await context.close();
    }
    const topicContext = await browser.newContext({ viewport: { width: 1280, height: 900 }, reducedMotion: 'reduce', serviceWorkers: 'block' });
    await topicContext.addInitScript(() => {
      sessionStorage.setItem('sj_auth_gate_skipped', 'true');
      localStorage.removeItem('sjmaths_preferred_language');
      localStorage.setItem('sj_pref_lang', 'hi');
    });
    const topicPage = await topicContext.newPage();
    const topicEvidence = await routeFixtures(topicPage);
    await topicPage.goto('https://sjmaths.com/ahc-ro-aro/general-science/atomic-structure/', { waitUntil: 'domcontentloaded' });
    await topicPage.waitForFunction(() => window.currentGuideLanguage === 'hi');
    await topicPage.locator('.tab-btn[data-tab="practice-panel"]').click();
    const firstPracticeCard = topicPage.locator('#practiceQuestionsContainer .practice-card').first();
    await firstPracticeCard.locator('.opt-item').first().click();
    const practiceSubmit = firstPracticeCard.locator('.submit-mult-btn');
    if (await practiceSubmit.isVisible()) await practiceSubmit.click();
    const practiceBeforeToggle = await firstPracticeCard.evaluate(card => ({
      optionClasses: [...card.querySelectorAll('.opt-item')].map(option => option.className),
      pointerEvents: [...card.querySelectorAll('.opt-item')].map(option => option.style.pointerEvents),
      explanationDisplay: card.querySelector('.explanation-box').style.display,
    }));
    const topicHindi = await topicPage.evaluate(() => ({
      documentLanguage: document.documentElement.lang,
      guideLanguage: window.currentGuideLanguage,
      deepDiveTitle: document.querySelector('#deep-dive-section h2')?.textContent.trim(),
      languagePreference: localStorage.getItem('sjmaths_preferred_language'),
      overflow: Math.max(0, document.documentElement.scrollWidth - innerWidth),
    }));
    assert.equal(topicHindi.documentLanguage, 'hi');
    assert.equal(topicHindi.guideLanguage, 'hi');
    await topicPage.locator('#headerLangToggleBtn').click();
    await topicPage.waitForFunction(() => document.documentElement.lang === 'en' && window.currentGuideLanguage === 'en');
    const practiceAfterToggle = await firstPracticeCard.evaluate(card => ({
      optionClasses: [...card.querySelectorAll('.opt-item')].map(option => option.className),
      pointerEvents: [...card.querySelectorAll('.opt-item')].map(option => option.style.pointerEvents),
      explanationDisplay: card.querySelector('.explanation-box').style.display,
    }));
    assert.deepEqual(practiceAfterToggle, practiceBeforeToggle, 'practice answer state must survive the language switch');

    await topicPage.locator('.tab-btn[data-tab="test-panel"]').click();
    await topicPage.evaluate(() => window.startTest());
    await topicPage.locator('#testQuestionArea .test-opt').first().click();
    const selectedTestAnswer = await topicPage.locator('#testQuestionArea .test-opt.selected').count();
    assert.equal(selectedTestAnswer, 1);
    await topicPage.locator('#headerLangToggleBtn').click();
    await topicPage.waitForFunction(() => document.documentElement.lang === 'hi' && window.currentGuideLanguage === 'hi');
    assert.equal(await topicPage.locator('#testPlayCard').evaluate(el => getComputedStyle(el).display !== 'none'), true);
    assert.equal(await topicPage.locator('#testQuestionArea .test-opt.selected').count(), 1, 'mock test answer must survive the language switch');
    await topicPage.evaluate(() => window.submitTest());
    await topicPage.locator('#headerLangToggleBtn').click();
    await topicPage.waitForFunction(() => document.documentElement.lang === 'en' && window.currentGuideLanguage === 'en');
    assert.equal(await topicPage.locator('#testResultsCard').evaluate(el => getComputedStyle(el).display !== 'none'), true, 'completed test results must survive the language switch');
    const topicAfterToggle = await topicPage.evaluate(() => ({
      documentLanguage: document.documentElement.lang,
      guideLanguage: window.currentGuideLanguage,
      deepDiveTitle: document.querySelector('#deep-dive-section h2')?.textContent.trim(),
      languagePreference: localStorage.getItem('sjmaths_preferred_language'),
      hindiVisible: [...document.querySelectorAll('.lang-hi')].filter(element => getComputedStyle(element).display !== 'none').length,
      englishVisible: [...document.querySelectorAll('.lang-en')].filter(element => getComputedStyle(element).display !== 'none').length,
      englishInlineHidden: [...document.querySelectorAll('.lang-en')].filter(element => element.style.display === 'none').length,
    }));
    console.log('Topic language toggle state', JSON.stringify({ topicHindi, topicAfterToggle, runtimeErrors: topicEvidence.errors }));
    assert.equal(topicAfterToggle.documentLanguage, 'en');
    assert.equal(topicAfterToggle.languagePreference, 'en');
    assert.equal(topicAfterToggle.guideLanguage, 'en');
    assert.equal(topicAfterToggle.hindiVisible, 0);
    assert.ok(topicAfterToggle.englishVisible > 2);
    assert.equal(topicAfterToggle.englishInlineHidden, 0);
    await topicContext.close();
    console.log(JSON.stringify(results, null, 2));
  } finally { await browser.close(); }
})().catch(error => { console.error(error); process.exitCode = 1; });
