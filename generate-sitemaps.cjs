const fs = require('fs');
const path = require('path');
const { siteFiles } = require('./scripts/seo-html.cjs');
const { createResolver } = require('./scripts/seo-routes.cjs');
const {
  DOMAIN,
  SITEMAP_ORDER,
  shouldSkipDir,
  normalizePath,
  toUrl,
  getSitemapName,
  getPriority,
  getChangefreq,
  isSitemapEligibleHtml,
} = require('./scripts/seo-policy.cjs');

const ROOT_DIR = __dirname;
const files = siteFiles();
const resolveUrl = createResolver(files);

// Weekly current affairs detail pages should advertise the publication week
// (from their JSON dataset) as lastmod instead of the file modification time.
function resolveLastmod(relativePath) {
  const match = relativePath.match(/^current-affairs\/weekly\/(\d{4})\/(\d{2})\/(\d{4}-\d{2}-\d{2})\/index\.html$/);
  if (!match) return null;
  const dataFile = path.join(ROOT_DIR, 'current-affairs', 'data', 'weekly', match[1], match[2], `${match[3]}.json`);
  try {
    const data = JSON.parse(fs.readFileSync(dataFile, 'utf8'));
    const lastmod = String(data.end || data.start || '');
    return /^\d{4}-\d{2}-\d{2}$/.test(lastmod) ? lastmod : null;
  } catch {
    return null;
  }
}

function collectHtmlFiles(dirPath, entries = []) {
  const dirents = fs.readdirSync(dirPath, { withFileTypes: true });

  for (const dirent of dirents) {
    if (dirent.isDirectory()) {
      if (!shouldSkipDir(dirent.name)) {
        collectHtmlFiles(path.join(dirPath, dirent.name), entries);
      }
      continue;
    }

    if (!dirent.isFile() || !dirent.name.endsWith('.html')) {
      continue;
    }

    const fullPath = path.join(dirPath, dirent.name);
    const relativePath = normalizePath(fullPath, ROOT_DIR);
    const content = fs.readFileSync(fullPath, 'utf8');

    if (!isSitemapEligibleHtml(relativePath, content)) {
      continue;
    }

    const url = toUrl(relativePath);
    const served = resolveUrl(url);
    if (served.file !== relativePath || served.redirect || served.loop) continue;
    // lastmod is optional. Only publish a known content date; checkout times
    // and mass formatting/metadata commits are not reliable update dates.
    const lastmod = resolveLastmod(relativePath);
    entries.push({
      relativePath,
      url,
      lastmod: lastmod && lastmod <= new Date().toISOString().slice(0, 10) ? lastmod : null,
      sitemap: getSitemapName(relativePath),
    });
  }

  return entries;
}

function renderSitemap(entries) {
  const sortedEntries = [...entries].sort((a, b) => a.url.localeCompare(b.url));

  const body = sortedEntries
    .map(
      (entry) => `  <url>
    <loc>${entry.url}</loc>${entry.lastmod ? `\n    <lastmod>${entry.lastmod}</lastmod>` : ''}
    <changefreq>${getChangefreq(entry.url)}</changefreq>
    <priority>${getPriority(entry.url)}</priority>
  </url>`
    )
    .join('\n\n');

  return `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">

${body}
</urlset>
`;
}

function renderSitemapIndex() {
  const body = SITEMAP_ORDER.map(
    (fileName) => `  <sitemap>
    <loc>${DOMAIN}/${fileName}</loc>
  </sitemap>`
  ).join('\n');

  return `<?xml version="1.0" encoding="UTF-8"?>
<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${body}
</sitemapindex>
`;
}

function writeFile(fileName, content) {
  if (fs.existsSync(path.join(ROOT_DIR, fileName)) && fs.readFileSync(path.join(ROOT_DIR, fileName), 'utf8') === content) return;
  fs.writeFileSync(path.join(ROOT_DIR, fileName), content, 'utf8');
  console.log(`Updated ${fileName}`);
}

function main() {
  const class9Only = process.argv.includes('--scope=class-9');
  const entries = class9Only
    ? ['class-9-maths', 'class-9-ganita-manjari-part-2'].flatMap(dir => collectHtmlFiles(path.join(ROOT_DIR, dir)))
    : collectHtmlFiles(ROOT_DIR);
  const groupedEntries = Object.fromEntries(SITEMAP_ORDER.map((fileName) => [fileName, []]));

  for (const entry of entries) {
    groupedEntries[entry.sitemap].push(entry);
  }

  for (const fileName of SITEMAP_ORDER) {
    if (class9Only && fileName !== 'sitemap-class-9.xml') continue;
    let content = renderSitemap(groupedEntries[fileName]);
    if (class9Only) {
      const existingPath = path.join(ROOT_DIR, fileName);
      if (!fs.existsSync(existingPath)) throw new Error('A scoped sitemap update requires an existing sitemap. Run the full generator first.');
      const existing = fs.readFileSync(existingPath, 'utf8');
      const isScoped = block => /<loc>https:\/\/sjmaths\.com\/class-9-(?:maths|ganita-manjari-part-2)\//.test(block);
      const retained = [...existing.matchAll(/  <url>[\s\S]*?<\/url>/g)].map(match => match[0]).filter(block => !isScoped(block));
      const updated = [...content.matchAll(/  <url>[\s\S]*?<\/url>/g)].map(match => match[0]);
      const blocks = [...retained, ...updated].sort((a, b) => a.match(/<loc>(.*?)<\/loc>/)[1].localeCompare(b.match(/<loc>(.*?)<\/loc>/)[1]));
      content = content.replace(/  <url>[\s\S]*?<\/url>\s*(?=<\/urlset>)/, blocks.join('\n\n') + '\n');
    }
    writeFile(fileName, content);
  }

  if (!class9Only) writeFile('sitemap.xml', renderSitemapIndex());
  console.log(`${class9Only ? 'Class 9 sitemap' : 'Sitemap index'} now submits ${entries.length} high-confidence URLs.`);
}

main();
