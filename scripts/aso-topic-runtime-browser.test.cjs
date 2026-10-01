const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const { chromium } = require('playwright');
const { ROOT } = require('./seo-html.cjs');
const { fixtureFiles, routeRepositoryFixtures } = require('./lib/browser-fixture.cjs');

test('ASO shared topic controllers preserve five-tab and quiz flows', { timeout: 120000 }, async () => {
  const cases = [
    'upsc-aso/aerodynamics-performance-stability/aeronautics-aerodynamics-mega-test/index.html',
    'upsc-aso/aircraft-structures-materials/wing-structures/index.html',
  ];
  const { hydrateAsoTopicRuntimes } = await import('./lib/aso-topic-runtime.mjs');
  const fixtureRoot = path.resolve(ROOT, process.env.SJ_REFACTOR_FIXTURE_ROOT || '.');
  const files = fixtureFiles(fixtureRoot);
  const browser = await chromium.launch({ headless: true });
  try {
    for (const file of cases) for (const width of [390, 1280]) {
      const url = `https://sjmaths.com/${file.replace(/index\.html$/, '')}`;
      const after = fs.readFileSync(path.join(fixtureRoot, file), 'utf8');
      const before = hydrateAsoTopicRuntimes(after);
      assert.notEqual(before, after, `${file} must exercise both inline controllers`);
      const outcomes = [];
      for (const html of [before, after]) {
        const context = await browser.newContext({ viewport: { width, height: 900 }, reducedMotion: 'reduce', serviceWorkers: 'block' });
        try {
          const page = await context.newPage();
          const evidence = await routeRepositoryFixtures(page, { root: fixtureRoot, files });
          await page.route(url, route => route.fulfill({ contentType: 'text/html', body: html }));
          await page.goto(url);
          const result = await page.evaluate(async standardPage => {
            const buttons = [...document.querySelectorAll('.tab-btn, .tab-button, .nav-tab, .tab-trigger')];
            const tabs = [];
            for (let index = 0; index < buttons.length; index++) {
              window.switchTab(index + 1);
              const panel = [...document.querySelectorAll('.tab-content, .tab-pane, .tab-panel, [id^="tab-content-"], [id^="tabContent"]')].find(node => node.classList.contains('active'));
              tabs.push({ button: buttons[index].textContent.trim(), active: buttons.map(button => button.classList.contains('active')), panel: panel?.innerText.trim() || '' });
            }
            window.switchTab(2);
            const panel = document.querySelector('.tab-content.active, .tab-pane.active, .tab-panel.active, [id^="tab-content-"].active, [id^="tabContent"].active');
            const option = panel?.querySelector('.quiz-option, .quiz-opt-btn, .quiz-opt-label, .quiz-choice, .option-item, label');
            let feedback = '';
            if (standardPage) {
              const radio = panel?.querySelector('input[type="radio"]');
              if (radio) radio.checked = true;
              if (typeof window.gradeQuiz === 'function') window.gradeQuiz();
              feedback = document.querySelector('#quiz-results')?.innerText || '';
            } else {
              option?.click();
              feedback = option?.closest('.quiz-card, .quiz-item, .test-card, .concept-card')?.querySelector('.quiz-exp-revealed')?.innerText || '';
            }
            await new Promise(resolve => setTimeout(resolve, 0));
            return {
              tabCount: buttons.length,
              tabs,
              quiz: option ? {
                selected: option.className,
                feedback,
              } : null,
              overflow: Math.max(0, document.documentElement.scrollWidth - innerWidth),
            };
          }, file.includes('wing-structures'));
          assert.equal(result.tabCount, 5, `${file} at ${width}px tab count`);
          assert.ok(result.tabs.every(tab => tab.active.filter(Boolean).length === 1), `${file} at ${width}px tab activation`);
          assert.ok(result.quiz, `${file} at ${width}px must expose a quiz option`);
          assert.ok(result.quiz.feedback, `${file} at ${width}px must reveal quiz feedback`);
          if (file.includes('wing-structures')) assert.match(result.quiz.feedback, /Your Score:/, `${file} at ${width}px must grade its quiz`);
          else assert.match(result.quiz.selected, /\b(?:correct|incorrect)\b/, `${file} at ${width}px feedback must mark the selected answer`);
          assert.equal(result.overflow, 0, `${file} at ${width}px horizontal overflow`);
          assert.deepEqual(evidence.missing, []);
          outcomes.push({ result, errors: evidence.errors.filter(error => !error.startsWith('Service Worker registration failed')) });
        } finally { await context.close(); }
      }
      assert.deepEqual(outcomes[1], outcomes[0], `${file} at ${width}px inline/external parity`);
    }
  } finally { await browser.close(); }
});
