const fs = require('node:fs');
const path = require('node:path');
const { ROOT, siteFiles } = require('./seo-html.cjs');
const { BASE, rowsFor, applyPage } = require('./lib/up-upper-primary-seo.cjs');

const files = siteFiles().filter(file => file.startsWith(`${BASE}/`) && /\/index\.html$/i.test(file));
const rows = rowsFor(files);
if (rows.length !== 418) throw new Error(`Expected 418 indexable upper-primary pages; found ${rows.length}. Review scope before applying.`);

let changed = 0;
for (const row of rows) {
  const filePath = path.join(ROOT, row.file);
  const before = fs.readFileSync(filePath, 'utf8');
  let after = applyPage(before, row);
  if (row.file === `${BASE}/index.html`) {
    after = after.replace(/\s+id=(['"])sub-prog-\d+\1/gi, '');
  }
  if (row.file === `${BASE}/general-knowledge/current-events-national-international/index.html`) {
    after = after.replace(/<script\s+src=["']\/assets\/js\/common\.min\.js(?:\?[^"']*)?["']\s*>\s*<\/script>\s*/i, '');
  }
  if (after !== before) {
    fs.writeFileSync(filePath, after, 'utf8');
    changed += 1;
  }
}

const sitemapPath = path.join(ROOT, 'sitemap-up-upper-primary-teacher.xml');
let sitemap = fs.readFileSync(sitemapPath, 'utf8');
const missingSitemapRows = rows.filter(row => {
  const canonical = `https://sjmaths.com${row.route}`;
  return row.file.includes('/mathematics/') && !sitemap.includes(`<loc>${canonical}</loc>`);
});
if (missingSitemapRows.length) {
  const closeIndex = sitemap.lastIndexOf('</urlset>');
  if (closeIndex < 0) throw new Error('Could not find </urlset> in upper-primary sitemap');
  const entries = missingSitemapRows.map(row => `  <url>\n    <loc>https://sjmaths.com${row.route}</loc>\n    <changefreq>monthly</changefreq>\n    <priority>0.7</priority>\n  </url>\n`).join('\n');
  sitemap = `${sitemap.slice(0, closeIndex)}${entries}${sitemap.slice(closeIndex)}`;
  fs.writeFileSync(sitemapPath, sitemap, 'utf8');
}

console.log(`Updated SEO metadata on ${changed}/${rows.length} UP Upper Primary Teacher pages.`);
console.log(`Added ${missingSitemapRows.length} missing indexable mathematics routes to sitemap-up-upper-primary-teacher.xml.`);
