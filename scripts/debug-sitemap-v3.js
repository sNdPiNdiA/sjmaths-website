const fs = require('fs');
const path = require('path');

// COPY OF ORIGINAL generate-sitemaps.js BUT WITH LOGGING
const ROOT_DIR = process.cwd();
const DOMAIN = 'https://sjmaths.com';

const SITEMAP_GROUPS = {
  'class-9-maths/': 'sitemap-class-9.xml',
  'class-10-maths/': 'sitemap-class-10.xml',
  'class-11-maths/': 'sitemap-class-11.xml',
  'class-12-maths/': 'sitemap-class-12.xml',
};

const EXCLUDED_DIRS = new Set([
  '.git', '.firebase', '.vscode', 'assets', 'components', 'dataconnect', 
  'digital-evaluation', 'node_modules', 'questions-module', 'scripts', 'src', 'utils'
]);

function shouldSkipDir(dirName) {
  return EXCLUDED_DIRS.has(dirName) || dirName.startsWith('.');
}

function normalizePath(filePath) {
  return path.relative(ROOT_DIR, filePath).split(path.sep).join('/');
}

function collectHtmlFiles(dirPath, entries = []) {
  const dirents = fs.readdirSync(dirPath, { withFileTypes: true });
  for (const dirent of dirents) {
    if (shouldSkipDir(dirent.name)) continue;
    const fullPath = path.join(dirPath, dirent.name);
    if (dirent.isDirectory()) {
      collectHtmlFiles(fullPath, entries);
      continue;
    }
    if (dirent.name.endsWith('.html')) {
        const rel = normalizePath(fullPath);
        entries.push({ relativePath: rel });
    }
  }
  return entries;
}

function getSitemapName(relativePath) {
  for (const [prefix, fileName] of Object.entries(SITEMAP_GROUPS)) {
    if (relativePath.startsWith(prefix)) {
      return fileName;
    }
  }
  return 'sitemap-main.xml';
}

const entries = collectHtmlFiles(ROOT_DIR);
console.log(`Total HTML files: ${entries.length}`);

const grouped = {};
entries.forEach(e => {
    const s = getSitemapName(e.relativePath);
    grouped[s] = (grouped[s] || 0) + 1;
});

console.log('Groups:', grouped);
