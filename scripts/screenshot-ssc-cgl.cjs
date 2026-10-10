const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const artifactDir = 'C:\\Users\\sande\\.gemini\\antigravity-ide\\brain\\c9266549-0505-4e62-ae71-656bcf6c1e82';
  
  const context = await browser.newContext();
  await context.addInitScript(() => {
    sessionStorage.setItem('sj_auth_gate_skipped', 'true');
    localStorage.setItem('sj_uid', 'verified_tester');
  });

  // Desktop View
  const page = await context.newPage({ viewport: { width: 1280, height: 800 } });
  
  await page.goto('http://localhost:8082/ssc-cgl/', { waitUntil: 'networkidle' });
  await page.screenshot({ path: path.join(artifactDir, 'ssc_cgl_main_desktop.png') });
  console.log('Saved ssc_cgl_main_desktop.png');

  await page.goto('http://localhost:8082/ssc-cgl/quantitative-aptitude/percentage/', { waitUntil: 'networkidle' });
  await page.screenshot({ path: path.join(artifactDir, 'ssc_cgl_quant_percentage.png') });
  console.log('Saved ssc_cgl_quant_percentage.png');

  await page.goto('http://localhost:8082/ssc-cgl/general-awareness/geography/atmosphere-and-weather-parameters/', { waitUntil: 'networkidle' });
  await page.screenshot({ path: path.join(artifactDir, 'ssc_cgl_atmosphere.png') });
  console.log('Saved ssc_cgl_atmosphere.png');

  await page.goto('http://localhost:8082/ssc-cgl/finance-economics/', { waitUntil: 'networkidle' });
  await page.screenshot({ path: path.join(artifactDir, 'ssc_cgl_finance_hub.png') });
  console.log('Saved ssc_cgl_finance_hub.png');

  // Mobile View
  const mobilePage = await context.newPage({ viewport: { width: 390, height: 844 }, isMobile: true });
  await mobilePage.goto('http://localhost:8082/ssc-cgl/', { waitUntil: 'networkidle' });
  await mobilePage.screenshot({ path: path.join(artifactDir, 'ssc_cgl_main_mobile.png') });
  console.log('Saved ssc_cgl_main_mobile.png');

  await browser.close();
})();
