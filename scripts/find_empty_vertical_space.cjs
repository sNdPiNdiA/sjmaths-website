const { chromium } = require('playwright');

async function testPage(url) {
  const browser = await chromium.launch();
  for (const width of [375, 768, 1280]) {
    const page = await browser.newPage({ viewport: { width, height: 900 } });
    await page.goto(url, { waitUntil: 'networkidle' });

    const issues = await page.evaluate(() => {
      const list = [];
      const els = document.querySelectorAll('*');
      for (const el of els) {
        const style = window.getComputedStyle(el);
        const rect = el.getBoundingClientRect();
        
        // Check for huge margins or paddings
        const mt = parseFloat(style.marginTop) || 0;
        const mb = parseFloat(style.marginBottom) || 0;
        const pt = parseFloat(style.paddingTop) || 0;
        const pb = parseFloat(style.paddingBottom) || 0;
        const minH = parseFloat(style.minHeight) || 0;

        if (mt > 80) list.push({ tag: el.tagName, class: el.className, prop: 'marginTop', val: mt });
        if (mb > 80) list.push({ tag: el.tagName, class: el.className, prop: 'marginBottom', val: mb });
        if (pt > 80) list.push({ tag: el.tagName, class: el.className, prop: 'paddingTop', val: pt });
        if (pb > 80) list.push({ tag: el.tagName, class: el.className, prop: 'paddingBottom', val: pb });
        if (minH > 500 && el.children.length === 0) list.push({ tag: el.tagName, class: el.className, prop: 'emptyMinHeight', val: minH });

        // Check for elements that have height > 150 but no visible content or text
        if (rect.height > 150 && rect.width > 100 && el.innerText.trim() === '' && !el.querySelector('svg, img, canvas, iframe')) {
          list.push({ tag: el.tagName, class: el.className, prop: 'emptyBox', height: rect.height, width: rect.width });
        }
      }
      return list;
    });

    console.log(`[Width ${width}] ${url} issues:`, issues);
    await page.close();
  }
  await browser.close();
}

async function run() {
  await testPage('http://localhost:8082/ib/dp-mathematics/analysis-and-approaches-hl/functions/');
  await testPage('http://localhost:8082/ib/dp-mathematics/analysis-and-approaches-hl/');
  await testPage('http://localhost:8082/ib/dp-mathematics/analysis-and-approaches-hl/functions/modulus-functions-and-inequalities/');
  await testPage('http://localhost:8082/ib/dp-mathematics/analysis-and-approaches-sl/calculus/limits-and-first-derivatives/');
}

run();
