const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const { chromium } = require('playwright');
const { fixtureFiles, routeRepositoryFixtures } = require('./lib/browser-fixture.cjs');
const root = path.resolve(__dirname,'..');
const route = '/class-11-physics/chapter-8-mechanical-properties-of-solids/';
test('Solids examples, every exercise, quiz, levels and direct links work in Chromium', {timeout:120000}, async () => {
  const browser=await chromium.launch({headless:true});
  try {
    const page=await browser.newPage({viewport:{width:390,height:844},reducedMotion:'reduce'});
    const evidence=await routeRepositoryFixtures(page,{root,files:fixtureFiles(root)});
    await page.route('**/assets/js/require-auth*.js*',r=>r.fulfill({contentType:'text/javascript',body:''}));
    await page.goto('https://sjmaths.com'+route,{waitUntil:'networkidle'});
    assert.equal(await page.locator('.katex-error').count(),0,'Invalid KaTeX');
    assert.ok(await page.locator('.nav-btn svg').evaluateAll(icons=>icons.every(icon=>icon.getBoundingClientRect().width<=24 && icon.getBoundingClientRect().height<=24)),'Navigation icon sizing');
    fs.mkdirSync(path.join(root,'scratch/solids-browser'),{recursive:true});
    await page.screenshot({path:path.join(root,'scratch/solids-browser/mobile-learn.png')});
    for(const example of await page.locator('[data-example]').all()) {
      const button=example.locator('.sol-toggle-btn');
      await button.click();
      assert.equal(await button.getAttribute('aria-expanded'),'true');
      assert.equal(await example.locator('.example-solution-box').isVisible(),true);
      await button.click();
      assert.equal(await button.getAttribute('aria-expanded'),'false');
    }
    await page.locator('.nav-btn[data-tab="exercise"]').click();
    for(const exercise of await page.locator('[data-exercise]').all()) {
      const button=exercise.locator('.sol-toggle-btn');
      await button.click();
      assert.equal(await exercise.locator('.ex-solution-content').isVisible(),true);
      assert.equal(await button.getAttribute('aria-expanded'),'true');
      assert.ok(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1));
      await button.click();
    }
    await page.locator('#exercise .chip').filter({hasText:'Bulk modulus'}).click();
    assert.equal(await page.locator('[data-exercise]:visible').count(),5);
    await page.locator('#exercise .chip').filter({hasText:'All 16'}).click();
    assert.equal(await page.locator('[data-exercise]:visible').count(),16);
    await page.evaluate(()=>location.hash='sec-8-5-5');
    await page.waitForTimeout(80);
    assert.equal(await page.locator('#learn').isVisible(),true);
    assert.ok(await page.locator('#sec-8-5-5').evaluate(e=>Math.abs(e.getBoundingClientRect().top)<50));
    await page.locator('.nav-btn[data-tab="quiz"]').click();
    for(const button of await page.locator('#quiz [data-correct="true"]').all()) await button.click();
    assert.match(await page.locator('#quizProgressCount').textContent(),/18 \/ 18/);
    assert.match(await page.locator('#quizScoreCount').textContent(),/18 \(100%\)/);
    await page.locator('.nav-btn[data-tab="tests"]').click();
    for(let level=0;level<3;level++) {
      await page.locator('.test-tab-btn').nth(level).click();
      const panel=page.locator('#testLevel'+level);
      for(const card of await panel.locator('.test-card').all()) {
        const correct=await card.getAttribute('data-ans');
        await card.locator(`[data-idx="${correct}"]`).click();
      }
      await page.getByRole('button',{name:'Submit Test',exact:true}).click();
      assert.match(await page.locator('#testResultBox').textContent(),/5 \/ 5.*100%/);
      await page.getByRole('button',{name:'Reset',exact:true}).click();
      assert.equal(await panel.locator('[data-selected]').count(),0);
    }
    await page.evaluate(()=>location.hash='exercise-8-12');
    await page.waitForTimeout(80);
    assert.equal(await page.locator('#exercise').isVisible(),true);
    await page.setViewportSize({width:1280,height:900});
    await page.evaluate(()=>switchTab('learn'));
    await page.screenshot({path:path.join(root,'scratch/solids-browser/desktop-learn.png')});
    assert.deepEqual(evidence.errors,[]);
    assert.deepEqual(evidence.missing,[]);
  }finally{await browser.close();}
});
