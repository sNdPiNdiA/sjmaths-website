const fs = require('fs');
const path = require('path');

const ROOT_DIR = __dirname;
const DOMAIN = 'https://sjmaths.com';

const SITEMAP_GROUPS = {
  'class-9-maths/': 'sitemap-class-9.xml',
  'class-10-maths/': 'sitemap-class-10.xml',
  'class-11-maths/': 'sitemap-class-11.xml',
  'class-12-maths/': 'sitemap-class-12.xml',
};

const SITEMAP_ORDER = [
  'sitemap-main.xml',
  'sitemap-class-9.xml',
  'sitemap-class-10.xml',
  'sitemap-class-11.xml',
  'sitemap-class-12.xml',
];

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

function encodeUrlPath(relativePath) {
  return relativePath
    .split('/')
    .map((segment) => encodeURIComponent(segment))
    .join('/');
}

function toUrl(relativePath) {
  let urlPath = relativePath;
  
  // Map legacy classes/class-N/ paths to pretty class-N-maths/ paths
  urlPath = urlPath.replace(/^classes\/class-(9|10|11|12)\//, 'class-$1-maths/');

  if (urlPath === 'index.html') {
    return `${DOMAIN}/`;
  }

  if (urlPath.endsWith('/index.html')) {
    const dirPath = urlPath.slice(0, -'index.html'.length);
    return `${DOMAIN}/${encodeUrlPath(dirPath)}`;
  }

  return `${DOMAIN}/${encodeUrlPath(urlPath)}`;
}

function getSitemapName(relativePath) {
  for (const [prefix, fileName] of Object.entries(SITEMAP_GROUPS)) {
    if (relativePath.startsWith(prefix)) {
      return fileName;
    }
  }

  return 'sitemap-main.xml';
}

function getPriority(url) {
  if (url === `${DOMAIN}/`) {
    return '1.0';
  }

  if (
    /^https:\/\/sjmaths\.com\/(?:classes|class-(?:9|10|11|12)-maths|ebooks|maths-mastery)\/$/.test(
      url
    )
  ) {
    return '0.9';
  }

  return '0.8';
}

function getChangefreq(url) {
  if (url === `${DOMAIN}/`) {
    return 'weekly';
  }

  if (
    /^https:\/\/sjmaths\.com\/(?:classes|class-(?:9|10|11|12)-maths|ebooks|maths-mastery)\/$/.test(
      url
    )
  ) {
    return 'weekly';
  }

  return 'monthly';
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

function collectHtmlFiles(dirPath, entries = []) {
  const dirents = fs.readdirSync(dirPath, { withFileTypes: true });

  for (const dirent of dirents) {
    if (shouldSkipDir(dirent.name)) {
      continue;
    }

    const fullPath = path.join(dirPath, dirent.name);

    if (dirent.isDirectory()) {
      collectHtmlFiles(fullPath, entries);
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
}

main();
