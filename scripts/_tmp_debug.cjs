const fs = require('fs');
const path = require('path');
const { siteFiles } = require('./seo-html.cjs');
const ROOT = path.resolve(__dirname, '..');
const targets = ['/geography/cartography/map-projection/', '/sanskrit/laukika-sahitya/gadya/kadambari/', '/geography/india/agriculture/'];
for (const t of targets) {
  const dir = t.replace(/^\//, '').replace(/\/$/, '');
  console.log('\nTARGET', t, '| dir exists:', fs.existsSync(dir));
  // who links to it?
  let from = [];
  for (const f of siteFiles()) {
    if (!f.endsWith('.html')) continue;
    const src = fs.readFileSync(path.join(ROOT, f), 'utf8');
    if (src.includes('href="' + t + '"')) from.push(f);
  }
  console.log('linked from:', from.slice(0, 5), from.length > 5 ? '(+' + (from.length - 5) + ')' : '');
}
