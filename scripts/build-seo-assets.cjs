// Rebuild only the SEO-related runtime assets; do not delete unrelated bundles.
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const esbuild = require('esbuild');
const { ROOT, siteFiles } = require('./seo-html.cjs');
const allNames = ['chapter-seo', 'exercise-seo', 'competitive-exam-guide', 'questions-loader'];
const requested = process.argv.find(arg => arg.startsWith('--asset='))?.slice(8);
if (requested && !allNames.includes(requested)) throw new Error(`Unknown asset: ${requested}`);
const names = requested ? [requested] : allNames;
const hashes = new Map();
for (const name of names) {
  const relative = `assets/js/${name}.min.js`;
  const target = path.join(ROOT, relative);
  esbuild.buildSync({ entryPoints: [path.join(ROOT, `assets/js/${name}.js`)], outfile: target, minify: true, sourcemap: false });
  hashes.set(relative, crypto.createHash('md5').update(fs.readFileSync(target)).digest('hex').slice(0, 8));
}
const assetPattern = new RegExp(`assets/js/(?:${names.join('|')})\\.min\\.js(?:\\?v=[\\w-]+)?`, 'g');
let changed = 0;
for (const file of siteFiles().filter(file => file.endsWith('.html'))) {
  const target = path.join(ROOT, file);
  const source = fs.readFileSync(target, 'utf8');
  const next = source.replace(assetPattern, value => {
    const asset = value.split('?')[0];
    return `${asset}?v=${hashes.get(asset)}`;
  });
  if (next !== source) { fs.writeFileSync(target, next); changed++; }
}
console.log(`Rebuilt ${names.length} SEO assets; refreshed ${changed} HTML cache keys.`);
