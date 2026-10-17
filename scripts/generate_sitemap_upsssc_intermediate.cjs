const fs = require('fs');
const path = require('path');
const policy = require('./seo-policy.cjs');
const { siteFiles } = require('./seo-html.cjs');

const htmlFiles = siteFiles().filter(f => f.startsWith('upsssc-intermediate-level/') && f.endsWith('.html'));
const hub = 'https://sjmaths.com/upsssc-intermediate-level/';
const topics = htmlFiles.filter(f => f !== 'upsssc-intermediate-level/index.html').map(f => policy.toUrl(f)).sort();

let xml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">

  <url>
    <loc>${hub}</loc>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>

`;

for (const url of topics) {
  xml += `  <url>
    <loc>${url}</loc>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>

`;
}

xml += `</urlset>
`;

fs.writeFileSync('sitemap-upsssc-intermediate.xml', xml, 'utf8');
console.log(`Generated sitemap-upsssc-intermediate.xml with ${topics.length + 1} URLs.`);
