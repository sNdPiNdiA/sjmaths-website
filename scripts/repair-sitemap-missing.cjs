/**
 * repair-sitemap-missing.cjs
 * ─────────────────────────────────────────────────────────────────────
 * Adds newly created indexable pages to their corresponding sitemaps.
 *
 * Run:  node scripts/repair-sitemap-missing.cjs [--dry-run]
 */
const fs = require('fs');
const path = require('path');
const ROOT = path.resolve(__dirname, '..');
const DRY_RUN = process.argv.includes('--dry-run');

const today = new Date().toISOString().slice(0, 10);

// Map of subject -> sitemap file
const sitemapMap = {
  'agriculture': 'sitemap-agriculture.xml',
  'art':         'sitemap-art.xml',
  'chemistry':   'sitemap-chemistry.xml',
  'home-science':'sitemap-home-science.xml',
};

// Pages that need to be added
const newPages = [
  'agriculture/index.html',
  'art/index.html',
  'art/aesthetics/index.html',
  'art/art-techniques-and-media/index.html',
  'art/bengal-school/index.html',
  'art/colour-theory/index.html',
  'art/company-school/index.html',
  'art/contemporary-indian-art/index.html',
  'art/drawing-and-composition/index.html',
  'art/elements-of-art/index.html',
  'art/important-artists/index.html',
  'art/important-paintings-and-artworks/index.html',
  'art/indian-miniature-painting/index.html',
  'art/indian-mural-painting/index.html',
  'art/indian-painting-foundations/index.html',
  'art/indus-valley-art/index.html',
  'art/modern-indian-art/index.html',
  'art/mughal-painting/index.html',
  'art/pahari-painting/index.html',
  'art/prehistoric-art/index.html',
  'art/principles-of-art-and-composition/index.html',
  'art/rajasthani-painting/index.html',
  'art/western-art-history/index.html',
  'art/western-art-movements/index.html',
  'chemistry/index.html',
  'home-science/index.html',
];

function fileToUrl(file) {
  // agriculture/index.html -> https://sjmaths.com/agriculture/
  return 'https://sjmaths.com/' + file.replace(/index\.html$/, '');
}

function fileToSubject(file) {
  const parts = file.split('/');
  if (parts[0] === 'home-science') return 'home-science';
  return parts[0];
}

// Group pages by sitemap
const groups = {};
for (const file of newPages) {
  const subject = fileToSubject(file);
  const sitemapFile = sitemapMap[subject];
  if (!sitemapFile) {
    console.log(`⚠️  No sitemap mapping for ${subject}`);
    continue;
  }
  if (!groups[sitemapFile]) groups[sitemapFile] = [];
  groups[sitemapFile].push(file);
}

let totalAdded = 0;

for (const [sitemapFile, pages] of Object.entries(groups)) {
  const absPath = path.join(ROOT, sitemapFile);
  let xml = fs.readFileSync(absPath, 'utf8');

  const toAdd = [];
  for (const page of pages) {
    const url = fileToUrl(page);
    if (xml.includes(url)) {
      console.log(`⏭️  Already in ${sitemapFile}: ${url}`);
      continue;
    }
    toAdd.push(url);
  }

  if (toAdd.length === 0) continue;

  // Build URL entries
  const entries = toAdd.map(url => {
    // Index pages get higher priority
    const isRoot = url.split('/').filter(Boolean).length <= 3; // e.g. /art/ or /art/aesthetics/
    const priority = isRoot ? '0.9' : '0.8';
    return `  <url>
    <loc>${url}</loc>
    <lastmod>${today}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>${priority}</priority>
  </url>`;
  }).join('\n\n');

  // Insert before </urlset>
  xml = xml.replace('</urlset>', entries + '\n\n</urlset>');

  if (DRY_RUN) {
    console.log(`🔍 Would add ${toAdd.length} URLs to ${sitemapFile}`);
    toAdd.forEach(u => console.log(`   + ${u}`));
  } else {
    fs.writeFileSync(absPath, xml, 'utf8');
    console.log(`✅ Added ${toAdd.length} URLs to ${sitemapFile}`);
  }
  totalAdded += toAdd.length;
}

console.log(`\n${DRY_RUN ? 'DRY-RUN' : 'DONE'}: ${totalAdded} URLs added to sitemaps`);
