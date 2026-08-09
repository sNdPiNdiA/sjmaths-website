const fs = require('fs');
const path = require('path');
const cheerio = require('cheerio');
const {
  shouldSkipDir,
  normalizePath,
  toLocalUrl,
  isSitemapEligibleHtml,
} = require('./scripts/seo-policy.cjs');

const ROOT_DIR = __dirname;

function getCategoryFromPath(relativePath) {
  if (relativePath.startsWith('class-9-maths/')) return 'Class 9';
  if (relativePath.startsWith('class-10-maths/')) return 'Class 10';
  if (relativePath.startsWith('class-11-maths/')) return 'Class 11';
  if (relativePath.startsWith('class-12-maths/')) return 'Class 12';
  if (relativePath.startsWith('maths-mastery/')) return 'Maths Mastery';
  if (relativePath.startsWith('ssc-cgl/')) return 'SSC CGL';
  if (relativePath.startsWith('current-affairs/')) return 'Current Affairs';
  return 'General';
}

function collectSearchableData(dirPath, entries = []) {
  const dirents = fs.readdirSync(dirPath, { withFileTypes: true });

  for (const dirent of dirents) {
    if (dirent.isDirectory()) {
      if (!shouldSkipDir(dirent.name)) {
        collectSearchableData(path.join(dirPath, dirent.name), entries);
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

    const $ = cheerio.load(content);
    const title = $('title').first().text().replace(/\s+\|\s*SJMaths$/i, '').trim();
    const keywords = $('meta[name="keywords"]').attr('content') || '';
    const category = getCategoryFromPath(relativePath);
    const tags = keywords
      .split(',')
      .map((keyword) => keyword.trim().toLowerCase())
      .filter(Boolean);

    if (category) {
      tags.push(category.toLowerCase());
    }

    if (title) {
      entries.push({
        url: toLocalUrl(relativePath),
        title,
        category,
        tags: [...new Set(tags)],
      });
    }
  }

  return entries;
}

function writeFile(filePath, content) {
  fs.writeFileSync(filePath, content, 'utf8');
  console.log(`Updated ${filePath}`);
}

function main() {
  console.log('Starting search index generation...');
  const searchData = collectSearchableData(ROOT_DIR);
  const outputPath = path.join(ROOT_DIR, 'assets', 'js', 'search-index.json');

  fs.mkdirSync(path.dirname(outputPath), { recursive: true });
  writeFile(outputPath, JSON.stringify(searchData, null, 2));
  console.log(`Successfully generated search index with ${searchData.length} public entries.`);
}

main();
