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
    const panel = document.querySelector('#tab-practice');
    const style = window.getComputedStyle(panel);
    const children = Array.from(panel.children).map(c => {
      const r = c.getBoundingClientRect();
      const s = window.getComputedStyle(c);
      return {
        tag: c.tagName,
        id: c.id,
        className: c.className,
        height: r.height,
        top: r.top + window.scrollY,
        bottom: r.bottom + window.scrollY,
        display: s.display,
        minHeight: s.minHeight
      };
    });

    return {
      panelMinHeight: style.minHeight,
      panelHeight: style.height,
      children
    };
  });

  console.log('Panel children info:', JSON.stringify(data, null, 2));
  await browser.close();
})();
