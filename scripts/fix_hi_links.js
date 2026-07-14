const fs = require('fs');
const path = require('path');

const ROOT_DIR = path.resolve(__dirname, '..');

function findHiIndexFiles(dir, fileList = []) {
  try {
    const dirents = fs.readdirSync(dir, { withFileTypes: true });
    for (const dirent of dirents) {
      if (['node_modules', '.git', '.firebase', '.codex', 'dataconnect', '.github', '.well-known', 'src'].includes(dirent.name)) continue;
      
      const filePath = path.join(dir, dirent.name);
      if (dirent.isDirectory()) {
        findHiIndexFiles(filePath, fileList);
      } else if (dirent.name === 'index.html' && path.basename(dir) === 'hi') {
        fileList.push(filePath);
      }
    }
  } catch (e) {
    // ignore
  }
  return fileList;
}

const files = findHiIndexFiles(ROOT_DIR);
let fixCount = 0;

for (const file of files) {
  let content = fs.readFileSync(file, 'utf8');
  let changed = false;

  // Replace <a href="hi/">Hindi Version</a>
  const regex1 = /<a\s+href=["']hi\/["']>\s*Hindi\s+Version\s*<\/a>/g;
  if (regex1.test(content)) {
    content = content.replace(regex1, '<a href="../">English Version</a>');
    changed = true;
  }

  // Replace <a href="hi/" class="mobile-lang-toggle"><i class="fas fa-globe"></i> हिन्दी</a>
  const regex2 = /<a\s+href=["']hi\/["']\s+class=["']mobile-lang-toggle["']>\s*<i\s+class=["']fas fa-globe["']><\/i>\s*हिन्दी\s*<\/a>/g;
  if (regex2.test(content)) {
    content = content.replace(regex2, '<a href="../" class="mobile-lang-toggle"><i class="fas fa-globe"></i> English</a>');
    changed = true;
  }
  
  // also handle single quotes or different spacing just in case
  const regex3 = /<a href="hi\/" class="mobile-lang-toggle"><i class="fas fa-globe"><\/i> हिन्दी<\/a>/g;
  if (regex3.test(content)) {
    content = content.replace(regex3, '<a href="../" class="mobile-lang-toggle"><i class="fas fa-globe"></i> English</a>');
    changed = true;
  }

  if (changed) {
    fs.writeFileSync(file, content, 'utf8');
    fixCount++;
  }
}

console.log(`Fixed ${fixCount} Hindi index.html files.`);
