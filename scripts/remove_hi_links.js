const fs = require('fs');
const path = require('path');

const ROOT_DIR = path.resolve(__dirname, '../upsc');

function walkDir(dir, callback) {
    fs.readdirSync(dir).forEach(f => {
        let dirPath = path.join(dir, f);
        let isDirectory = fs.statSync(dirPath).isDirectory();
        isDirectory ? walkDir(dirPath, callback) : callback(path.join(dir, f));
    });
}

const files = [];
walkDir(ROOT_DIR, (filePath) => {
    if (filePath.endsWith('index.html')) {
        files.push(filePath);
    }
});

let fixCount = 0;

for (const file of files) {
  let content = fs.readFileSync(file, 'utf8');
  let changed = false;

  const regex1 = /<a\s+href=["']hi\/["']>\s*Hindi\s+Version\s*<\/a>/g;
  if (regex1.test(content)) {
    content = content.replace(regex1, '');
    changed = true;
  }

  const regex2 = /<a\s+href=["']hi\/["']\s+class=["']mobile-lang-toggle["']>.*?<\/a>/g;
  if (regex2.test(content)) {
    content = content.replace(regex2, '');
    changed = true;
  }

  if (changed) {
    fs.writeFileSync(file, content, 'utf8');
    fixCount++;
  }
}

console.log(`Removed hi/ links from ${fixCount} index.html files.`);
