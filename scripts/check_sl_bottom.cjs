const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1280, height: 900 } });
  await page.goto('http://localhost:8082/ib/dp-mathematics/analysis-and-approaches-sl/calculus/limits-and-first-derivatives/', { waitUntil: 'networkidle' });

  const btns = await page.$$('button');
  for (const b of btns) {
    const text = await b.innerText();
    if (text.includes('Practice')) {
      await b.click();
      break;
    }
  }
  await page.waitForTimeout(300);

  const data = await page.evaluate(() => {
    const q15 = document.querySelector('ol.practice-list li:last-child');
    const panel = document.querySelector('#tab-practice');
    const moreLessons = document.querySelector('#more-lessons');
    const related = document.querySelector('.related-guides');
    const footer = document.querySelector('.ib-footer');

    const getBox = (el) => {
      if (!el) return null;
      const r = el.getBoundingClientRect();
      const s = window.getComputedStyle(el);
      return {
        top: r.top + window.scrollY,
        bottom: r.bottom + window.scrollY,
        height: r.height,
        display: s.display,
        visibility: s.visibility,
        marginBottom: s.marginBottom,
        paddingBottom: s.paddingBottom
      };
    };

    return {
      q15: getBox(q15),
      panel: getBox(panel),
      moreLessons: getBox(moreLessons),
      related: getBox(related),
      footer: getBox(footer),
      bodyHeight: document.body.scrollHeight
    };
  });

  console.log('Layout evaluation:', JSON.stringify(data, null, 2));
  await browser.close();
})();
