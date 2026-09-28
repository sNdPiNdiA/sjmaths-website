// Browser evidence for refactors. Uses repository fixtures; does not test hosting.
const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');
const { chromium } = require('playwright');
const { ROOT, siteFiles } = require('./seo-html.cjs');
const { routeRepositoryFixtures } = require('./lib/browser-fixture.cjs');

const argument = name => process.argv.find(value => value.startsWith(`--${name}=`))?.slice(name.length + 3);
const label = argument('label') || 'before';
if (!/^[a-z0-9-]+$/i.test(label)) throw new Error('Use a simple artifact label.');
const comparisonLabel = argument('compare');
if (comparisonLabel && !/^[a-z0-9-]+$/i.test(comparisonLabel)) throw new Error('Use a simple comparison label.');
const filter = argument('filter');
const fixtureRoot = argument('root') ? path.resolve(ROOT, argument('root')) : ROOT;
const relativeRoot = path.relative(ROOT, fixtureRoot);
if (relativeRoot.startsWith('..') || path.isAbsolute(relativeRoot)) throw new Error('Fixture root must stay inside the repository.');
const cases = [
  { id: 'home', route: '/' },
  { id: 'class10', route: '/class-10-maths/' },
  { id: 'probability', route: '/class-12-maths/chapter-wise-notes/chapter-13-probability/' },
  { id: 'history-art', route: '/history/indus-saraswati-valley-civilization/art/' },
  { id: 'history-bhagvatism', route: '/history/ancient-india/religious-movements/bhagvatism/' },
  { id: 'history-expansion', route: '/history/mauryan-empire/expansion/' },
  { id: 'aso-ceiling', route: '/upsc-aso/aerodynamics-performance-stability/absolute-and-service-ceiling/' },
  { id: 'upsc-agriculture', route: '/upsc/ancient-history/HarappanIndus-Valley-Civilisation/Agriculture/' },
  { id: 'upsc-prehistory', route: '/upsc/ancient-history/Prehistory/Prehistoric-Time-Periods/' },
  { id: 'exercise', route: '/class-9-maths/ncert-exercise-practice/chapter-3-coordinate-geometry/exercise-3-2' },
].filter(item => !filter || item.id.includes(filter));
if (!cases.length) throw new Error('No matching baseline cases.');
const sha = data => crypto.createHash('sha256').update(data).digest('hex');

async function captureState(page) {
  return page.evaluate(() => {
    const visible = element => Boolean(element.getClientRects().length);
    const selectors = ['h1', 'h2', '.tab-btn', '.study-tabs', '.notebook-controls', '.notebook-page', 'main', 'button', 'input'];
    return {
      title: document.title,
      location: location.pathname + location.hash,
      theme: document.documentElement.className + ' ' + document.body.className,
      horizontalOverflow: Math.max(0, document.documentElement.scrollWidth - innerWidth),
      visibleH1: [...document.querySelectorAll('h1')].filter(visible).map(el => el.textContent.trim()),
      controls: selectors.flatMap(selector => [...document.querySelectorAll(selector)].filter(visible).slice(0, 5).map(el => {
        const style = getComputedStyle(el), rect = el.getBoundingClientRect();
        return { selector, text: el.textContent.trim().slice(0, 80), width: Math.round(rect.width), height: Math.round(rect.height), color: style.color, background: style.backgroundColor, font: style.fontFamily, size: style.fontSize, padding: style.padding, radius: style.borderRadius };
      })),
    };
  });
}

async function main() {
  const files = [];
  function collect(directory) {
    for (const entry of fs.readdirSync(directory, { withFileTypes: true })) {
      const absolute = path.join(directory, entry.name);
      if (entry.isDirectory()) {
        if (!['node_modules', '.git', 'scratch', 'scripts'].includes(entry.name)) collect(absolute);
      } else files.push(path.relative(fixtureRoot, absolute).replace(/\\/g, '/'));
    }
  }
  if (fixtureRoot === ROOT) files.push(...siteFiles());
  else collect(fixtureRoot);
  const output = path.join(ROOT, 'scratch/refactor', label);
  fs.mkdirSync(output, { recursive: true });
  const browser = await chromium.launch({ headless: true });
  const results = [];
  try {
    for (const item of cases) for (const width of [390, 1280]) {
      const context = await browser.newContext({ viewport: { width, height: 900 }, reducedMotion: 'reduce', serviceWorkers: 'block' });
      const page = await context.newPage();
      const { errors, missing, externalFailures, exclusions } = await routeRepositoryFixtures(page, { root: fixtureRoot, files });
      const result = { id: item.id, width, route: item.route, screenshots: [], interactions: [] };
      try {
        await page.goto('https://sjmaths.com' + item.route, { waitUntil: 'domcontentloaded', timeout: 30000 });
        await page.waitForLoadState('load', { timeout: 15000 }).catch(() => {});
        await page.evaluate(() => document.fonts.ready);
        const skip = page.locator('#sj-skip-gate-btn');
        const authExpected = await page.locator('script[src*="require-auth"]').count();
        if (authExpected) await skip.waitFor({ state: 'visible', timeout: 15000 });
        if (await skip.isVisible()) { await skip.click(); result.interactions.push('public guest skip'); }
        await page.waitForTimeout(400);
        for (const theme of ['light', 'dark']) {
          if (theme === 'dark') {
            // Use the site's theme API when available; record how it was invoked.
            result.themeMethod = await page.evaluate(() => {
              if (typeof window.toggleDarkMode === 'function') { window.toggleDarkMode(); return 'toggleDarkMode'; }
              return 'no global theme API; system preference';
            });
            if (result.themeMethod.startsWith('no global')) await page.emulateMedia({ colorScheme: 'dark' });
            await page.waitForTimeout(200);
          }
          const name = `${item.id}-${width}-${theme}.png`;
          const buffer = await page.screenshot({ path: path.join(output, name), animations: 'disabled', timeout: 20000 });
          result.screenshots.push({ theme, name, sha256: sha(buffer), state: await captureState(page) });
        }
        if (item.id.startsWith('history-') && await page.locator('#history-quiz-data').count()) {
          await page.locator('[data-tab="tab-quiz"]').click();
          await page.locator('[data-quiz]').first().click();
          result.interactions.push(await page.locator('#quiz-score').innerText());
          await page.locator('[data-tab="tab-test"]').click();
          await page.locator('[data-test]').first().click();
          await page.locator('#btn-submit-test').click();
          result.interactions.push('test result visible: ' + await page.locator('#test-result').isVisible());
        }
        const solution = page.locator('button.solution-toggle-btn, button.solution-btn, button.sol-toggle-btn').first();
        if (await solution.isVisible()) { await solution.click(); result.interactions.push('solution: ' + await solution.innerText()); }
        result.status = 'captured';
      } catch (error) { result.status = 'failed'; result.failure = error.message; process.exitCode = 1; }
      Object.assign(result, { errors: [...new Set(errors)], missing: [...new Set(missing)], externalFailures: [...new Set(externalFailures)], exclusions: [...new Set(exclusions)] });
      results.push(result);
      console.log(`${result.status}: ${item.id} ${width}px; errors=${result.errors.length}; missing=${result.missing.length}`);
      await context.close();
    }
  } finally { await browser.close(); }
  fs.writeFileSync(path.join(output, 'results.json'), JSON.stringify({ fixtureRoot: relativeRoot || '.', mode: 'repository fixtures; third-party advertising excluded; external dependencies attempted; service worker disabled', results }, null, 2) + '\n');
  if (comparisonLabel) {
    const previous = JSON.parse(fs.readFileSync(path.join(ROOT, 'scratch/refactor', comparisonLabel, 'results.json'), 'utf8'));
    const differences = [];
    for (const result of results) {
      const baseline = previous.results.find(item => item.id === result.id && item.width === result.width);
      if (!baseline) { differences.push({ id: result.id, width: result.width, issue: 'missing baseline' }); continue; }
      if (result.status !== 'captured') differences.push({ id: result.id, width: result.width, issue: 'capture failed', value: result.failure });
      for (const error of result.errors.filter(value => !baseline.errors.includes(value))) differences.push({ id: result.id, width: result.width, issue: 'new runtime error', value: error });
      for (const shot of result.screenshots) {
        const before = baseline.screenshots.find(item => item.theme === shot.theme);
        if (!before || before.sha256 !== shot.sha256) differences.push({ id: result.id, width: result.width, theme: shot.theme, issue: 'screenshot differs', computedStateMatches: before && JSON.stringify(before.state) === JSON.stringify(shot.state) });
      }
      for (const missing of result.missing.filter(value => !baseline.missing.includes(value))) differences.push({ id: result.id, width: result.width, issue: 'new missing local request', value: missing });
      if (JSON.stringify(result.interactions) !== JSON.stringify(baseline.interactions)) differences.push({ id: result.id, width: result.width, issue: 'interaction outcome differs', before: baseline.interactions, after: result.interactions });
    }
    fs.writeFileSync(path.join(output, 'comparison.json'), JSON.stringify({ comparedWith: comparisonLabel, differences }, null, 2) + '\n');
    console.log(`Comparison: ${differences.length} differences requiring review.`);
    if (differences.length) process.exitCode = 1;
  }
  console.log(`Evidence: ${path.relative(ROOT, output)}`);
}
main().catch(error => { console.error(error); process.exitCode = 1; });
