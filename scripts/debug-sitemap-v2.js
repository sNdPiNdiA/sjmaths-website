const fs = require('fs');
const path = require('path');

const ROOT_DIR = process.cwd();
const EXCLUDED_DIRS = new Set([
  '.git', '.firebase', '.vscode', 'assets', 'components', 'dataconnect', 
  'digital-evaluation', 'node_modules', 'questions-module', 'scripts', 'src', 'utils'
]);

const EXCLUDED_PATHS = new Set([
  '404.html', 'dashboard.html', 'login.html', 'my-submissions.html', 
  'notifications.html', 'offline.html', 'pages/admin.html', 'pages/coming-soon.html',
  'pages/manage-content.html', 'pages/settings.html', 'profile.html', 'search.html', 'settings.html'
]);

const EXCLUDED_BASENAMES = new Set([
  'final-evaluation.html', 'free-evaluation.html', 'paid-evaluation.html', 'performance-dashboard.html',
]);

const HIDDEN_PATH_PATTERN = /(^|\/)[._][^/]+/;
const NOINDEX_PATTERN = /<meta[^>]+name=["']robots["'][^>]+content=["'][^"']*\bnoindex\b/i;
const TITLE_PATTERN = /<title>\s*[^<]+\s*<\/title>/i;

function shouldSkipDir(dirName) {
  return EXCLUDED_DIRS.has(dirName) || dirName.startsWith('.');
}

function normalizePath(filePath) {
  return path.relative(ROOT_DIR, filePath).split(path.sep).join('/');
}

function isIndexableHtml(relativePath, content) {
  if (!relativePath.endsWith('.html')) return "not html";
  if (!content.trim()) return "empty";
  if (HIDDEN_PATH_PATTERN.test(relativePath)) return "hidden path";
  if (EXCLUDED_PATHS.has(relativePath)) return "excluded path";
  if (EXCLUDED_BASENAMES.has(path.posix.basename(relativePath))) return "excluded basename";
  if (NOINDEX_PATTERN.test(content)) return "noindex";
  if (!TITLE_PATTERN.test(content)) return "no title";
  return true;
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
        const content = fs.readFileSync(fullPath, 'utf8');
        const res = isIndexableHtml(rel, content);
        if (res === true) {
            entries.push(rel);
        } else if (rel.includes('chapter-wise-notes') || rel.includes('ncert-exercise-practice')) {
            console.log(`Skipped ${rel}: ${res}`);
        }
    }
  }
  return entries;
}

const files = collectHtmlFiles(ROOT_DIR);
console.log(`Final indexable files: ${files.length}`);
