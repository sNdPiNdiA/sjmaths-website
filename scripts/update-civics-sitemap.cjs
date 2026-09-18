const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
const sitemapFile = path.join(ROOT, 'sitemap-main.xml');
let xml = fs.readFileSync(sitemapFile, 'utf8');

function getValidCivicsPages(dir) {
  let pages = [];
  const entries = fs.readdirSync(dir, { withFileTypes: true });
  for (const ent of entries) {
    const full = path.join(dir, ent.name);
    if (ent.isDirectory()) {
      pages = pages.concat(getValidCivicsPages(full));
    } else if (ent.name === 'index.html') {
      const content = fs.readFileSync(full, 'utf8');
      if (!content.includes('http-equiv="refresh"')) {
        const rel = path.relative(ROOT, path.dirname(full)).replace(/\\/g, '/');
        pages.push(`https://sjmaths.com/${rel}/`);
      }
    }
  }
  return pages;
}

const validCivicsUrls = getValidCivicsPages(path.join(ROOT, 'civics'));
console.log('Valid canonical Civics URLs:', validCivicsUrls.length);

// Regex to remove all existing civics <url> entries from sitemap-main.xml
const civicsUrlRegex = /\s*<url>\s*<loc>https:\/\/sjmaths\.com\/civics\/[^<]+<\/loc>[\s\S]*?<\/url>/g;
xml = xml.replace(civicsUrlRegex, '');

// Format new civics url blocks
const newUrlBlocks = validCivicsUrls.sort().map(u => `  <url>
    <loc>${u}</loc>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>`).join('\n\n');

// Insert newUrlBlocks right after <urlset ...>
const urlsetMatch = xml.match(/<urlset[^>]*>/);
if (urlsetMatch) {
  const insertPos = urlsetMatch.index + urlsetMatch[0].length;
  xml = xml.slice(0, insertPos) + '\n\n' + newUrlBlocks + xml.slice(insertPos);
  fs.writeFileSync(sitemapFile, xml, 'utf8');
  console.log(`sitemap-main.xml successfully updated with ${validCivicsUrls.length} Civics URLs.`);
} else {
  console.error('Could not find urlset tag in sitemap-main.xml');
}
