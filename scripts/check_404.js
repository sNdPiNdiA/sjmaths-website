const fs = require('fs');
const path = require('path');

const ROOT_DIR = path.resolve(__dirname, '..');

function findHtmlFiles(dir, fileList = []) {
  try {
    const dirents = fs.readdirSync(dir, { withFileTypes: true });
    for (const dirent of dirents) {
      if (['node_modules', '.git', '.firebase', '.codex', 'dataconnect', '.github', '.well-known', 'src'].includes(dirent.name)) continue;
      
      const filePath = path.join(dir, dirent.name);
      if (dirent.isDirectory()) {
        findHtmlFiles(filePath, fileList);
      } else if (dirent.name.endsWith('.html')) {
        fileList.push(filePath);
      }
    }
  } catch (e) {
    // ignore
  }
  return fileList;
}

const htmlFiles = findHtmlFiles(ROOT_DIR);
let total404 = 0;
const missingLinks = {};

for (const file of htmlFiles) {
  let content = '';
  try {
    content = fs.readFileSync(file, 'utf8');
  } catch (e) { continue; }
  
  const linkRegex = /(?:href|src)=["']([^"']+)["']/g;
  let match;
  while ((match = linkRegex.exec(content)) !== null) {
    let link = match[1];
    
    if (link.startsWith('http') || link.startsWith('mailto:') || link.startsWith('tel:') || link.startsWith('#') || link.trim() === '') {
      continue;
    }
    if (link.startsWith('data:')) continue;
    if (link.includes('${')) continue; // Ignore JS template literals
    
    link = link.split('?')[0].split('#')[0];
    if (link === '') continue;

    let targetPath;
    if (link.startsWith('/')) {
      targetPath = path.join(ROOT_DIR, link.substring(1));
    } else {
      targetPath = path.join(path.dirname(file), link);
    }
    
    let isDir = false;
    try {
      if (fs.existsSync(targetPath) && fs.statSync(targetPath).isDirectory()) {
        isDir = true;
        targetPath = path.join(targetPath, 'index.html');
      }
    } catch (e) {}

    if (!fs.existsSync(targetPath)) {
      if (!isDir && fs.existsSync(targetPath + '.html')) {
        continue;
      }
      
      const displayLink = link;
      if (!missingLinks[displayLink]) missingLinks[displayLink] = [];
      missingLinks[displayLink].push(path.relative(ROOT_DIR, file));
      total404++;
    }
  }
}

const summaryPath = path.join(ROOT_DIR, '404_summary.json');
fs.writeFileSync(summaryPath, JSON.stringify({
  total404,
  uniqueMissingLinks: Object.keys(missingLinks).length,
  missingLinks
}, null, 2));

console.log(`Finished. Found ${total404} broken links across ${Object.keys(missingLinks).length} unique URLs. Summary written to 404_summary.json`);
