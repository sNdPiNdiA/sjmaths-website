const fs = require('fs');
const path = require('path');
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

    const stats = fs.statSync(fullPath);
    entries.push({
      relativePath,
      url: toUrl(relativePath),
      lastmod: stats.mtime.toISOString().slice(0, 10),
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
    <loc>${entry.url}</loc>
    <lastmod>${entry.lastmod}</lastmod>
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
  const today = new Date().toISOString().slice(0, 10);
  const body = SITEMAP_ORDER.map(
    (fileName) => `  <sitemap>
    <loc>${DOMAIN}/${fileName}</loc>
    <lastmod>${today}</lastmod>
  </sitemap>`
  ).join('\n');

  return `<?xml version="1.0" encoding="UTF-8"?>
<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${body}
</sitemapindex>
`;
}

function writeFile(fileName, content) {
  fs.writeFileSync(path.join(ROOT_DIR, fileName), content, 'utf8');
  console.log(`Updated ${fileName}`);
}

function main() {
  const entries = collectHtmlFiles(ROOT_DIR);
  const groupedEntries = Object.fromEntries(SITEMAP_ORDER.map((fileName) => [fileName, []]));

  for (const entry of entries) {
    groupedEntries[entry.sitemap].push(entry);
  }

  for (const fileName of SITEMAP_ORDER) {
    writeFile(fileName, renderSitemap(groupedEntries[fileName]));
  }

  writeFile('sitemap.xml', renderSitemapIndex());
  console.log(`Sitemap index now submits ${entries.length} high-confidence URLs.`);
}

main();
