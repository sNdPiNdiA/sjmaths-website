const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
const sitemapPath = path.join(ROOT, 'sitemap-main.xml');
let xml = fs.readFileSync(sitemapPath, 'utf8');

// Find all current valid commerce URLs
function scan(d) {
  let res = [];
  for (const ent of fs.readdirSync(d, { withFileTypes: true })) {
    const full = path.join(d, ent.name);
    if (ent.isDirectory()) res = res.concat(scan(full));
    else if (ent.name === 'index.html') {
      const rel = path.relative(ROOT, path.dirname(full)).replace(/\\/g, '/');
      res.push(`https://sjmaths.com/${rel}/`);
    }
  }
  return res;
}

const currentCommerceUrls = scan(path.join(ROOT, 'commerce'));
console.log(`Current valid Commerce URLs on disk: ${currentCommerceUrls.length}`);

// Remove existing commerce URLs from sitemap-main.xml
const commerceUrlRegex = /\s*<url>\s*<loc>https:\/\/sjmaths\.com\/commerce\/[^<]+<\/loc>[\s\S]*?<\/url>/g;
xml = xml.replace(commerceUrlRegex, '');

// Format new commerce url blocks
const newUrlBlocks = currentCommerceUrls.sort().map(u => `  <url>
    <loc>${u}</loc>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>`).join('\n\n');

// Insert right after urlset
const urlsetMatch = xml.match(/<urlset[^>]*>/);
if (urlsetMatch) {
  const insertPos = urlsetMatch.index + urlsetMatch[0].length;
  xml = xml.slice(0, insertPos) + '\n\n' + newUrlBlocks + xml.slice(insertPos);
  fs.writeFileSync(sitemapPath, xml, 'utf8');
  console.log(`sitemap-main.xml successfully updated with ${currentCommerceUrls.length} Commerce URLs.`);
} else {
  console.error('Could not find urlset in sitemap-main.xml');
}
