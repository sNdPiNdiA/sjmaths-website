import fs from 'fs';
import path from 'path';

const INVENTORY_FILE = 'scratch/chemistry_inventory.json';
const OUTPUT_SITEMAP = 'sitemap-chemistry.xml';

if (!fs.existsSync(INVENTORY_FILE)) {
  console.error(`Inventory file ${INVENTORY_FILE} not found.`);
  process.exit(1);
}

const inventory = JSON.parse(fs.readFileSync(INVENTORY_FILE, 'utf8'));
const today = new Date().toISOString().split('T')[0];

const hubUrls = [
  { loc: 'https://sjmaths.com/chemistry/', priority: '1.0', changefreq: 'weekly' },
  { loc: 'https://sjmaths.com/up-pgt-chemistry/', priority: '0.9', changefreq: 'weekly' },
];

let xml = `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n`;

for (const hub of hubUrls) {
  xml += `  <url>\n    <loc>${hub.loc}</loc>\n    <lastmod>${today}</lastmod>\n    <changefreq>${hub.changefreq}</changefreq>\n    <priority>${hub.priority}</priority>\n  </url>\n`;
}

for (const item of inventory) {
  const loc = `https://sjmaths.com${item.url}`;
  xml += `  <url>\n    <loc>${loc}</loc>\n    <lastmod>${today}</lastmod>\n    <changefreq>weekly</changefreq>\n    <priority>0.8</priority>\n  </url>\n`;
}

xml += `</urlset>\n`;

fs.writeFileSync(OUTPUT_SITEMAP, xml, 'utf8');
console.log(`Generated ${OUTPUT_SITEMAP} with ${hubUrls.length + inventory.length} URLs.`);
