const fs = require('fs');
const path = require('path');

const ROOT_DIR = process.cwd();
const EXCLUDED_DIRS = new Set([
  '.git', '.firebase', '.vscode', 'assets', 'components', 'dataconnect', 
  'digital-evaluation', 'node_modules', 'questions-module', 'scripts', 'src', 'utils'
]);

function shouldSkipDir(dirName) {
  return EXCLUDED_DIRS.has(dirName) || dirName.startsWith('.');
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
      entries.push(fullPath);
    }
  }
  return entries;
}

const files = collectHtmlFiles(ROOT_DIR);
console.log(`Total HTML files found: ${files.length}`);
const noteFiles = files.filter(f => f.includes('chapter-wise-notes'));
console.log(`Notes files found: ${noteFiles.length}`);
if (noteFiles.length > 0) {
    console.log(`Example: ${noteFiles[0]}`);
}
const practiceFiles = files.filter(f => f.includes('ncert-exercise-practice'));
console.log(`Practice files found: ${practiceFiles.length}`);
