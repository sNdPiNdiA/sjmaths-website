const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
const sitemapPath = path.join(ROOT, 'sitemap-main.xml');

function getPages(dir) {
  let res = [];
  if (!fs.existsSync(dir)) return res;
  for (const f of fs.readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, f.name);
    if (f.isDirectory()) res.push(...getPages(full));
    else if (f.name === 'index.html') res.push(path.normalize(full));
  }
  return res;
}

const econPages = getPages(path.join(ROOT, 'economics'));
console.log(`Current valid Economics URLs on disk: ${econPages.length}`);

let sitemap = fs.readFileSync(sitemapPath, 'utf8');

// Remove all existing /economics/ url blocks
const econBlockRegex = /\s*<url>\s*<loc>https:\/\/sjmaths\.com\/economics\/[^<]*<\/loc>[\s\S]*?<\/url>/g;
sitemap = sitemap.replace(econBlockRegex, '');

// Generate new XML blocks for active economics pages
const today = new Date().toISOString().split('T')[0];
const newBlocks = econPages.map(p => {
  const rel = path.relative(ROOT, path.dirname(p)).replace(/\\/g, '/');
  const loc = `https://sjmaths.com/${rel}/`;
  return `  <url>
    <loc>${loc}</loc>
    <lastmod>${today}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>`;
}).join('\n');

// Insert newBlocks before </urlset>
sitemap = sitemap.replace('</urlset>', `${newBlocks}\n</urlset>`);

fs.writeFileSync(sitemapPath, sitemap, 'utf8');
console.log(`sitemap-main.xml successfully updated with ${econPages.length} Economics URLs.`);
