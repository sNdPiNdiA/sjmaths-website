const fs = require('fs');
const path = require('path');

const indexPath = path.resolve('upsc/index.html');
const upscDir = path.resolve('upsc');
const html = fs.readFileSync(indexPath, 'utf8');

const linkRegex = /<a\s+[^>]*href="([^"]+)"/g;
let match;
let totalLinks = 0;
let brokenLinks = [];

while ((match = linkRegex.exec(html)) !== null) {
  const href = match[1];
  if (href.startsWith('#') || href.startsWith('http')) continue;
  totalLinks++;

  // Resolve relative to upscDir or repo root
  let targetPath;
  if (href.startsWith('/upsc/')) {
    targetPath = path.resolve(href.slice(1));
  } else if (href.startsWith('./')) {
    targetPath = path.resolve(upscDir, href.slice(2));
  } else {
    targetPath = path.resolve(upscDir, href);
  }

  // targetPath can be a directory with index.html, or an html file
  let exists = false;
  if (fs.existsSync(targetPath)) {
    if (fs.statSync(targetPath).isDirectory()) {
      exists = fs.existsSync(path.join(targetPath, 'index.html'));
    } else {
      exists = true;
    }
  }

  if (!exists) {
    brokenLinks.push({ href, targetPath });
  }
}

console.log(`Tested ${totalLinks} internal links from upsc/index.html`);
console.log(`Broken links found: ${brokenLinks.length}`);
if (brokenLinks.length > 0) {
  console.log('Sample broken links:', brokenLinks.slice(0, 10));
}
