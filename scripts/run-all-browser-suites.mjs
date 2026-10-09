import { execSync } from 'node:child_process';

const suites = [
  'scripts/applied-mathematics-browser.test.cjs',
  'scripts/upsc-apfc-browser.test.cjs',
  'scripts/chemistry-browser.test.cjs',
  'scripts/ahc-ro-aro-browser.test.cjs',
  'scripts/sanskrit-browser.test.cjs',
  'scripts/logic-browser.test.cjs',
  'scripts/up-assistant-browser.test.cjs',
  'scripts/up-assistant-language-browser.test.cjs',
  'scripts/music-instrumental-browser.test.cjs',
  'scripts/upsssc-pet-browser.test.cjs',
  'scripts/up-pgt-browser.test.cjs',
  'scripts/civics-browser.test.cjs',
  'scripts/up-tgt-pgt-gk-browser.test.cjs',
  'scripts/agriculture-browser.test.cjs',
  'scripts/emerald-theme-browser.test.cjs',
  'scripts/hindi-theme-browser.test.cjs',
  'scripts/commerce-browser.test.cjs',
  'scripts/military-science-browser.test.cjs',
  'scripts/chapter-nav-dock-browser.test.cjs',
  'scripts/up-assistant-glass-browser.test.cjs'
];

console.log(`Running all ${suites.length} Playwright browser verification suites...\n`);

let passed = 0;
let failed = 0;

for (const suite of suites) {
  process.stdout.write(`Testing ${suite}... `);
  try {
    execSync(`node ${suite}`, { stdio: 'pipe', encoding: 'utf8' });
    console.log('✅ PASSED');
    passed++;
  } catch (err) {
    console.log('❌ FAILED');
    console.error(err.stdout || err.stderr || err.message);
    failed++;
  }
}

console.log(`\n===========================================`);
console.log(`Summary: ${passed}/${suites.length} Suites Passed, ${failed} Failed`);
console.log(`===========================================`);

if (failed > 0) {
  process.exit(1);
}
