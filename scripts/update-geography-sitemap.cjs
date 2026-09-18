const fs = require('fs');

const sitemapPath = 'sitemap-main.xml';
let sitemap = fs.readFileSync(sitemapPath, 'utf8');

function getFiles(dir) {
  let results = [];
  const list = fs.readdirSync(dir, { withFileTypes: true });
  for (const item of list) {
    const full = dir + '/' + item.name;
    if (item.isDirectory()) {
      results = results.concat(getFiles(full));
    } else if (item.name === 'index.html') {
      results.push(full);
    }
  }
  return results;
}

const geoFiles = getFiles('geography');
const activeUrls = new Set(geoFiles.map(f => {
  let rel = f.replace(/\\/g, '/').replace(/index\.html$/, '');
  if (!rel.startsWith('/')) rel = '/' + rel;
  return 'https://sjmaths.com' + rel;
}));

console.log('Active Geography URLs count on disk:', activeUrls.size);

// Extract all <url> blocks
const urlBlockRegex = /<url>[\s\S]*?<\/url>/g;
let removedCount = 0;
let updatedSitemap = sitemap.replace(urlBlockRegex, (match) => {
  const locMatch = match.match(/<loc>(https:\/\/sjmaths\.com\/geography\/[^<]+)<\/loc>/);
  if (locMatch) {
    const url = locMatch[1];
    if (!activeUrls.has(url)) {
      removedCount++;
      return ''; // remove deleted URL
    }
  }
  return match;
});

// Check if any active Geography URLs are missing from sitemap
let addedCount = 0;
for (const url of activeUrls) {
  if (!updatedSitemap.includes('<loc>' + url + '</loc>')) {
    addedCount++;
    const newEntry = `  <url>\n    <loc>${url}</loc>\n    <lastmod>2026-09-18</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.7</priority>\n  </url>\n`;
    updatedSitemap = updatedSitemap.replace('</urlset>', newEntry + '</urlset>');
  }
}

// Clean up extra blank lines
updatedSitemap = updatedSitemap.replace(/\n\s*\n\s*\n/g, '\n\n');

fs.writeFileSync(sitemapPath, updatedSitemap, 'utf8');
console.log(`Sitemap updated: removed ${removedCount} obsolete Geography URLs, added ${addedCount} missing Geography URLs.`);
