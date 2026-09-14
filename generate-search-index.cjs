const fs = require('fs');
const path = require('path');
const cheerio = require('cheerio');
const { siteFiles } = require('./scripts/seo-html.cjs');
const { createResolver } = require('./scripts/seo-routes.cjs');
const {
  shouldSkipDir,
  normalizePath,
  toLocalUrl,
  isSitemapEligibleHtml,
} = require('./scripts/seo-policy.cjs');

const ROOT_DIR = __dirname;
const resolveUrl = createResolver(siteFiles());

function getCategoryFromPath(relativePath) {
  if (relativePath.startsWith('class-9-science/')) return 'Class 9 Science';
  if (relativePath.startsWith('class-9-advanced-maths/')) return 'Class 9 Advanced Maths';
  if (relativePath.startsWith('class-9-advanced-science/')) return 'Class 9 Advanced Science';
  if (relativePath.startsWith('class-10-science/')) return 'Class 10 Science';
  if (relativePath.startsWith('class-10-social-science/')) return 'Class 10 Social Science';
  if (relativePath.startsWith('class-12-physics/')) return 'Class 12 Physics';
  if (relativePath.startsWith('class-11-applied-mathematics/')) return 'Class 11 Applied Mathematics';
  if (relativePath.startsWith('class-9-maths/')) return 'Class 9';
  if (relativePath.startsWith('class-10-maths/')) return 'Class 10';
  if (relativePath.startsWith('class-11-maths/')) return 'Class 11';
  if (relativePath.startsWith('class-11-physics/')) return 'Class 11 Physics';
  if (relativePath.startsWith('class-11-chemistry/')) return 'Class 11 Chemistry';
  if (relativePath.startsWith('class-12-maths/')) return 'Class 12';
  if (relativePath.startsWith('ssc-cgl/')) return 'SSC CGL';
  if (relativePath.startsWith('up-upper-primary-teacher/')) return 'UP Upper Primary Teacher';
  if (relativePath.startsWith('up-assistant-teacher/')) return 'UP Assistant Teacher';
  if (relativePath.startsWith('upsssc-pet/')) return 'UPSSSC PET';
  if (relativePath.startsWith('upsssc-lower-mains/')) return 'UPSSSC Lower Mains';
  if (relativePath.startsWith('upsc/')) return 'UPSC';
  if (relativePath.startsWith('upsc-apfc/')) return 'UPSC APFC';
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
    const served = resolveUrl(toLocalUrl(relativePath));
    if (served.file !== relativePath || served.redirect || served.loop) continue;

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
