const fs = require('fs');
const path = require('path');
const cheerio = require('cheerio');

const ROOT_DIR = __dirname;
const DOMAIN = 'https://sjmaths.com';

// --- Reusing constants and functions from generate-sitemaps.js ---

const EXCLUDED_DIRS = new Set([
  '.git',
  '.firebase',
  '.vscode',
  'assets',
  'components',
  'dataconnect',
  'digital-evaluation',
  'node_modules',
  'questions-module',
  'scripts',
  'src',
  'utils',
]);

const EXCLUDED_PATHS = new Set([
  '404.html',
  'dashboard.html',
  'login.html',
  'my-submissions.html',
  'notifications.html',
  'offline.html',
  'pages/admin.html',
  'pages/coming-soon.html',
  'pages/manage-content.html',
  'pages/settings.html',
  'profile.html',
  'search.html',
  'settings.html',
  'signup.html',
  'teacher-dashboard.html',
]);

const EXCLUDED_BASENAMES = new Set([
  'final-evaluation.html',
  'free-evaluation.html',
  'paid-evaluation.html',
  'performance-dashboard.html',
]);

const HIDDEN_PATH_PATTERN = /(^|\/)[._][^/]+/;
const NOINDEX_PATTERN = /<meta[^>]+name=["']robots["'][^>]+content=["'][^"']*\bnoindex\b/i;
const LOGIN_REDIRECT_PATTERN =
  /(?:window\.)?location\.(?:href|replace)\s*=\s*["'][^"']*login\.html["']/i;
const CLIENT_REDIRECT_PATTERN =
  /(?:window\.)?location\.(?:href|replace)\s*=\s*["'][^"']+["']|<meta[^>]+http-equiv=["']refresh["']/i;
const TITLE_PATTERN = /<title>\s*[^<]+\s*<\/title>/i;

function shouldSkipDir(dirName) {
  return EXCLUDED_DIRS.has(dirName) || dirName.startsWith('.');
}

function normalizePath(filePath) {
  return path.relative(ROOT_DIR, filePath).split(path.sep).join('/');
}

function toUrl(relativePath) {
    if (relativePath === 'index.html') {
        return '/';
    }
    if (relativePath.endsWith('/index.html')) {
        const dirPath = relativePath.slice(0, -'index.html'.length);
        return `/${dirPath}`;
    }
    if (relativePath.endsWith('.html')) {
        return `/${relativePath}`;
    }
    return `/${relativePath}`;
}

function isIndexableHtml(relativePath, content) {
  if (!relativePath.endsWith('.html')) {
    return false;
  }
  if (!content.trim()) {
    return false;
  }
  if (HIDDEN_PATH_PATTERN.test(relativePath)) {
    return false;
  }
  if (EXCLUDED_PATHS.has(relativePath) || EXCLUDED_BASENAMES.has(path.posix.basename(relativePath))) {
    return false;
  }
  if (NOINDEX_PATTERN.test(content)) {
    return false;
  }
  if (LOGIN_REDIRECT_PATTERN.test(content)) {
    return false;
  }
  if (CLIENT_REDIRECT_PATTERN.test(content)) {
    return false;
  }
  if (!TITLE_PATTERN.test(content)) {
    return false;
  }
  return true;
}

function getCategoryFromPath(relativePath) {
    if (relativePath.startsWith('class-9-maths/')) return 'Class 9';
    if (relativePath.startsWith('class-10-maths/')) return 'Class 10';
    if (relativePath.startsWith('class-11-maths/')) return 'Class 11';
    if (relativePath.startsWith('class-12-maths/')) return 'Class 12';
    return 'General';
}


function collectSearchableData(dirPath, entries = []) {
  const dirents = fs.readdirSync(dirPath, { withFileTypes: true });

  for (const dirent of dirents) {
    if (shouldSkipDir(dirent.name)) {
      continue;
    }

    const fullPath = path.join(dirPath, dirent.name);

    if (dirent.isDirectory()) {
      collectSearchableData(fullPath, entries);
      continue;
    }

    if (!dirent.isFile() || !dirent.name.endsWith('.html')) {
      continue;
    }

    const relativePath = normalizePath(fullPath);
    const content = fs.readFileSync(fullPath, 'utf8');

    if (!isIndexableHtml(relativePath, content)) {
      continue;
    }

    const $ = cheerio.load(content);
    
    // Extract data
    const title = $('title').text().replace(/ - SJMaths$/, '').trim();
    const description = $('meta[name="description"]').attr('content') || '';
    const keywords = $('meta[name="keywords"]').attr('content') || '';
    const url = toUrl(relativePath);
    const category = getCategoryFromPath(relativePath);

    // For the search result snippet, we prefer the meta description.
    // If it's short or missing, we can create a snippet from the main body text.
    const tags = (keywords || '')
        .split(',')
        .map(k => k.trim().toLowerCase())
        .filter(k => k.length > 0);
    
    if (category) {
        tags.push(category.toLowerCase());
    }

    if (title) {
      entries.push({
        url: url,
        title: title,
        category: category,
        tags: tags
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
  
  // Ensure the directory exists
  fs.mkdirSync(path.dirname(outputPath), { recursive: true });

  writeFile(outputPath, JSON.stringify(searchData, null, 2));
  console.log(`
Successfully generated search index with ${searchData.length} entries.`);
  console.log(`Index file created at: ${outputPath}`);
}

main();
