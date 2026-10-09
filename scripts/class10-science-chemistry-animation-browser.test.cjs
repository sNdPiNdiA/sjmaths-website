const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const { chromium } = require('playwright');

test('Retained Chemistry engine has one RAF per scene and supports reduced motion and teardown', { timeout: 180000 }, async () => {
  const browser = await chromium.launch({ headless: true });
  try {
    for (const reducedMotion of ['reduce', 'no-preference']) {
      const context = await browser.newContext({ viewport: { width: 390, height: 900 }, reducedMotion });
      const page = await context.newPage();
      const errors = [];
      page.on('pageerror', error => errors.push(error.message));
      await page.setContent('<main id="fixture"></main>');
      await page.addScriptTag({ url: 'https://unpkg.com/three@0.160.0/build/three.min.js' });
      await page.evaluate(() => {
        const pending = new Set();
        const request = window.requestAnimationFrame.bind(window);
        const cancel = window.cancelAnimationFrame.bind(window);
        window.requestAnimationFrame = callback => {
          const id = request(time => { pending.delete(id); callback(time); });
          pending.add(id);
          return id;
        };
        window.cancelAnimationFrame = id => { pending.delete(id); cancel(id); };
        window.pendingSceneFrames = pending;
        for (const type of ['reaction', 'balance', 'combination', 'decomposition', 'displacement', 'double', 'energy', 'redox', 'corrosion', 'rancidity']) {
          const mount = document.createElement('div');
          mount.dataset.threeAnimation = type;
          mount.style.cssText = 'width:350px;height:300px;position:relative';
          document.getElementById('fixture').appendChild(mount);
        }
      });
      await page.addScriptTag({ content: fs.readFileSync(path.join(__dirname, '../class-10-science/chapter-1-chemical-reactions-and-equations/three-animations.js'), 'utf8') });
      assert.equal(await page.locator('#fixture canvas').count(), 10);
      const state = await page.evaluate(() => {
        const scenes = [...document.querySelectorAll('[data-three-animation]')].map(el => el._sjScienceLab);
        scenes.forEach(scene => { scene.nextStep(); scene.previousStep(); scene.togglePlay(); scene.animate(); scene.animate(); });
        return { pending: window.pendingSceneFrames.size, scenes: scenes.length };
      });
      assert.ok(state.pending <= state.scenes, 'Repeated resume must not create competing animation loops');
      if (reducedMotion === 'reduce') assert.equal(state.pending, 0);
      await page.evaluate(() => {
        document.querySelectorAll('[data-three-animation]').forEach(el => el._sjScienceLab.destroy());
      });
      assert.equal(await page.locator('#fixture canvas').count(), 0);
      assert.equal(await page.evaluate(() => window.pendingSceneFrames.size), 0);
      assert.deepEqual(errors, []);
      await context.close();
    }
  } finally { await browser.close(); }
});
