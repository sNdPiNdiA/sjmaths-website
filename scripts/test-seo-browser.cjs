// Browser checks against local files or a deployed preview/production origin.
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');
const { ROOT, siteFiles } = require('./seo-html.cjs');
const { createResolver } = require('./seo-routes.cjs');
const liveBase = process.env.SEO_TEST_BASE?.replace(/\/$/, '');
const targetBase = liveBase || 'https://sjmaths.com';
const targetHost = new URL(targetBase).hostname;
const mime = { '.html': 'text/html', '.js': 'application/javascript', '.css': 'text/css', '.json': 'application/json', '.svg': 'image/svg+xml', '.png': 'image/png', '.webp': 'image/webp', '.woff2': 'font/woff2', '.xml': 'application/xml' };
const routes = [
  '/upsc/polity/',
  '/class-12-physics/chapter-1-electric-fields-and-charges/',
  '/class-10-maths/previous-year-questions/chapter-1-real-numbers/fundamental-theorem-of-arithmetic',
  '/class-10-maths/chapter-wise-notes/chapter-8-introduction-to-trigonometry/',
  '/class-9-maths/ncert-exercise-practice/chapter-3-coordinate-geometry/exercise-3-2',
  '/class-11-maths/ncert-exemplar-practice/chapter-1-sets/exemplar-1-1',
];
const physicsRoutes = siteFiles()
  .filter(file => /^class-12-physics\/chapter-[^/]+\/index\.html$/.test(file))
  .map(file => '/' + file.replace(/index\.html$/, ''))
  .sort((a, b) => a.localeCompare(b, undefined, { numeric: true }));
const viewports = [
  { width: 390, height: 844 },
  { width: 1280, height: 900 },
];
async function main() {
  const resolve = createResolver(siteFiles());
  const browser = await chromium.launch({ headless: true });
  const results = [];
  const activeRoutes = process.env.SEO_TEST_PHYSICS_SWEEP ? physicsRoutes : routes;
  const activeViewports = process.env.SEO_TEST_PHYSICS_SWEEP ? [viewports[0]] : viewports;
  fs.mkdirSync(path.join(ROOT, 'scratch/seo-browser'), { recursive: true });
  try {
    for (const viewport of activeViewports) {
      for (const pathname of activeRoutes.filter(value => !process.env.SEO_TEST_FILTER || value.includes(process.env.SEO_TEST_FILTER))) {
        const { width } = viewport;
        const context = await browser.newContext({ viewport, reducedMotion: 'reduce' });
        const page = await context.newPage();
        const errors = new Set(), missing = [], excludedExternal = new Set(), externalFailures = new Set();
        const sourceResult = resolve('https://sjmaths.com' + pathname);
        const source = sourceResult.file ? fs.readFileSync(path.join(ROOT, sourceResult.file), 'utf8') : '';
        const authExpected = /require-auth(?:\.min)?\.js/.test(source);
        const mathExpected = /katex(?:\.min)?\.js/.test(source);
        const closingHtmlCount = (source.match(/<\/html>/gi) || []).length;
        const trailingSource = source.slice(source.toLowerCase().indexOf('</html>') + 7).trim();
        page.on('pageerror', error => errors.add(error.stack || error.message));
        page.on('console', message => {
          if (message.type() === 'error') errors.add(`console: ${message.text()}`);
        });
        page.on('requestfailed', request => {
          const url = new URL(request.url());
          const detail = `${url.hostname}${url.pathname}: ${request.failure()?.errorText || 'request failed'}`;
          if (url.hostname === targetHost) missing.push(detail);
          else externalFailures.add(detail);
        });
        await page.route('**/*', async route => {
          const url = new URL(route.request().url());
          if (liveBase) {
            if (/googlesyndication|google-analytics|googletagmanager|doubleclick/.test(url.hostname)) {
              excludedExternal.add(url.hostname);
              return route.fulfill({ status: 204, body: '' });
            }
            return route.continue();
          }
          if (!['sjmaths.com', 'www.sjmaths.com'].includes(url.hostname)) {
            // Ads/analytics are outside this local, anonymous functional check.
            if (/googlesyndication|google-analytics|googletagmanager|doubleclick/.test(url.hostname)) {
              excludedExternal.add(url.hostname);
              return route.fulfill({ status: 204, body: '' });
            }
            return route.continue();
          }
          const result = resolve(url.href);
          if (result.redirect) return route.fulfill({ status: 301, headers: { location: result.redirect } });
          if (!result.file) { missing.push(url.pathname); return route.fulfill({ status: 404, body: 'Not found' }); }
          return route.fulfill({ contentType: (mime[path.extname(result.file)] || 'application/octet-stream') + (['.html', '.js', '.json', '.css', '.xml'].includes(path.extname(result.file)) ? '; charset=utf-8' : ''), body: fs.readFileSync(path.join(ROOT, result.file)) });
        });
        try {
          await page.goto(targetBase + pathname + '?seo-test=1#verification', { waitUntil: 'load', timeout: 45000 });
          await page.waitForTimeout(1000);
          // Exercise the existing public "Skip for now" flow, not an auth bypass.
          const skip = page.locator('#sj-skip-gate-btn');
          const firebaseBlocked = [...externalFailures].some(value => /gstatic\.com\/firebase|firestore\.googleapis\.com/.test(value));
          const mathCdnBlocked = [...externalFailures].some(value => /cdn\.jsdelivr\.net\/(?:npm\/)?(?:katex|mathjax)/.test(value));
          if (authExpected && !firebaseBlocked) {
            await skip.waitFor({ state: 'visible', timeout: 7000 }).catch(() => {});
          }
          const guestGate = Boolean(await skip.count() && await skip.isVisible());
          if (guestGate) {
            await skip.click({ timeout: 5000 });
            await page.locator('#sj-auth-overlay').waitFor({ state: 'detached', timeout: 5000 });
          }
          if (mathExpected && !mathCdnBlocked) {
            await page.locator('.katex').first().waitFor({ state: 'attached', timeout: 8000 }).catch(() => {});
          }
          const state = await page.evaluate(() => {
            const allIds = [...document.querySelectorAll('[id]')].map(el => el.id);
            return {
              canonical: [...document.querySelectorAll('link[rel="canonical"]')].map(el => el.href),
              descriptions: document.querySelectorAll('meta[name="description"]').length,
              ogUrls: [...document.querySelectorAll('meta[property="og:url"]')].map(el => el.content),
              h1: document.querySelectorAll('h1').length,
              duplicateIds: [...new Set(allIds.filter((id, i) => allIds.indexOf(id) !== i))],
              overflow: document.documentElement.scrollWidth - innerWidth,
              title: document.title,
              renderedMath: document.querySelectorAll('.katex').length,
              mathErrors: document.querySelectorAll('.katex-error').length,
              mathErrorDetails: [...document.querySelectorAll('.katex-error')].slice(0, 10).map(el => ({
                source: el.textContent.trim().slice(0, 240),
                error: el.getAttribute('title') || '',
              })),
              overflowElements: [...document.body.querySelectorAll('*')]
                .map(el => {
                  const rect = el.getBoundingClientRect();
                  return { el, rect };
                })
                .filter(({ rect }) => rect.right > innerWidth + 2 || rect.left < -2)
                .sort((a, b) => b.rect.width - a.rect.width)
                .slice(0, 12)
                .map(({ el, rect }) => ({
                  tag: el.tagName.toLowerCase(),
                  id: el.id,
                  className: typeof el.className === 'string' ? el.className.slice(0, 160) : '',
                  left: Math.round(rect.left),
                  right: Math.round(rect.right),
                  width: Math.round(rect.width),
                  text: (el.innerText || '').trim().replace(/\s+/g, ' ').slice(0, 180),
                })),
            };
          });
          state.sourceClosingHtml = closingHtmlCount;
          state.sourceTrailingMarkup = Boolean(trailingSource);
          state.authExpected = authExpected;
          state.guestGate = Boolean(guestGate);
          state.guestGateDismissed = !guestGate || await page.locator('#sj-auth-overlay').count() === 0;
          state.mathExpected = mathExpected;
          const button = page.locator('button.solution-toggle-btn, button.solution-btn, button.sol-toggle-btn').first();
          if (await button.count() && await button.isVisible()) {
            await button.click({ timeout: 5000 });
            state.solutionToggleText = (await button.innerText()).trim();
            state.solutionToggle = await button.evaluate(btn => {
              const target = btn.nextElementSibling;
              return /Hide (?:Step-by-Step )?Solution/.test(btn.innerText) || btn.classList.contains('active') || Boolean(target?.classList.contains('open'));
            });
          }
          const previewFirebaseBlocked = Boolean(liveBase && targetHost.includes('--') && [...errors].some(message => /FirebaseError: Installations:.*referer .* are blocked/i.test(message)));
          const relevantExternalFailures = [...externalFailures].filter(message => !/pagead2\.googlesyndication\.com/.test(message));
          const externalBlocked = relevantExternalFailures.length > 0 || previewFirebaseBlocked;
          const actionableErrors = [...errors].filter(message =>
            !/net::ERR_NETWORK_ACCESS_DENIED|Service Worker registration failed|unknown error occurred when fetching the script/i.test(message) &&
            !(previewFirebaseBlocked && /403|FirebaseError: Installations:/i.test(message)) &&
            !/pagead2\.googlesyndication\.com.*Content Security Policy/i.test(message)
          );
          state.structuralPassed = state.canonical.length === 1 && state.canonical[0] === 'https://sjmaths.com' + pathname && state.descriptions === 1 && state.ogUrls.length === 1 && state.ogUrls[0] === state.canonical[0] && state.h1 === 1 && !state.duplicateIds.length && state.overflow <= 2 && state.solutionToggle !== false && state.sourceClosingHtml === 1 && !state.sourceTrailingMarkup && !actionableErrors.length && !missing.length;
          state.integrationBlocked = externalBlocked && (state.mathExpected || state.authExpected);
          state.passed = state.structuralPassed && !state.integrationBlocked && (!state.mathExpected || state.renderedMath > 0 && state.mathErrors === 0) && (!state.authExpected || state.guestGate && state.guestGateDismissed) && !actionableErrors.length;
          results.push({ targetBase, pathname, width, height: viewport.height, ...state, errors: [...errors], actionableErrors, missing: [...new Set(missing)], excludedExternal: [...excludedExternal], externalFailures: [...externalFailures] });
          if (pathname === routes[0] || pathname === routes[4]) await page.screenshot({ path: path.join(ROOT, `scratch/seo-browser/${pathname === routes[0] ? 'directory' : 'exercise'}-${width}.png`), fullPage: true });
        } catch (error) { results.push({ pathname, width, height: viewport.height, passed: false, error: error.message, errors: [...errors], missing: [...new Set(missing)], externalFailures: [...externalFailures] }); }
        finally { await context.close(); }
        console.log(JSON.stringify(results.at(-1)));
      }
    }
  } finally { await browser.close(); }
  const resultName = process.env.SEO_TEST_RESULT || (process.env.SEO_TEST_PHYSICS_SWEEP ? 'physics-results.json' : 'results.json');
  fs.writeFileSync(path.join(ROOT, 'scratch/seo-browser', resultName), JSON.stringify(results, null, 2) + '\n');
  const actionableFailed = results.filter(row => !row.structuralPassed || (!row.integrationBlocked && !row.passed));
  console.log(JSON.stringify({ checks: results.length, passed: results.filter(row => row.passed).length, structuralPassed: results.filter(row => row.structuralPassed).length, integrationBlocked: results.filter(row => row.integrationBlocked).length, actionableFailed }, null, 2));
  if (actionableFailed.length) process.exitCode = 1;
}
main().catch(error => { console.error(error); process.exitCode = 1; });
