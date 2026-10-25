import { chromium } from 'playwright';
import path from 'node:path';
import { pathToFileURL } from 'node:url';

async function checkFooter() {
  const browser = await chromium.launch({ headless: true });
  
  for (const isMobile of [false, true]) {
    const page = await browser.newPage({
      viewport: isMobile ? { width: 375, height: 667 } : { width: 1280, height: 800 },
      isMobile
    });

    const errors = [];
    page.on('console', msg => {
      if (msg.type() === 'error') errors.push(msg.text());
    });
    page.on('pageerror', err => errors.push(err.message));

    const fileUrl = pathToFileURL(path.resolve('index.html')).href;
    await page.goto(fileUrl, { waitUntil: 'load' });
    await page.waitForTimeout(1000);

    const footerData = await page.evaluate(() => {
      const footer = document.getElementById('site-footer');
      if (!footer) return { exists: false };
      const rect = footer.getBoundingClientRect();
      const style = window.getComputedStyle(footer);
      const grid = footer.querySelector('.sf-grid');
      const gridStyle = grid ? window.getComputedStyle(grid) : null;
      const mobileLegal = footer.querySelector('.sf-mobile-legal');
      const mobileLegalStyle = mobileLegal ? window.getComputedStyle(mobileLegal) : null;
      const bottomNav = document.querySelector('.mobile-bottom-nav');
      const bottomNavStyle = bottomNav ? window.getComputedStyle(bottomNav) : null;

      // Check horizontal overflow
      const docWidth = document.documentElement.offsetWidth;
      const scrollWidth = document.documentElement.scrollWidth;

      return {
        exists: true,
        classes: footer.className,
        rect: { top: rect.top, height: rect.height, width: rect.width },
        gridColumns: gridStyle ? gridStyle.gridTemplateColumns : null,
        mobileLegalDisplay: mobileLegalStyle ? mobileLegalStyle.display : null,
        bottomNavDisplay: bottomNavStyle ? bottomNavStyle.display : null,
        hasHorizontalOverflow: scrollWidth > docWidth,
        docWidth,
        scrollWidth
      };
    });

    console.log(`\n--- Viewport: ${isMobile ? 'MOBILE (375px)' : 'DESKTOP (1280px)'} ---`);
    console.log('Console errors:', errors);
    console.log('Footer data:', footerData);
  }

  await browser.close();
}

checkFooter().catch(console.error);

