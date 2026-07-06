const fs = require('fs');
const path = require('path');

const ROOT_DIR = path.join(__dirname, '..');
const CLASS9_DIR = path.join(ROOT_DIR, 'class-9-maths');

function getHtmlFiles(dir, fileList = []) {
  const files = fs.readdirSync(dir);
  for (const file of files) {
    const filePath = path.join(dir, file);
    if (fs.statSync(filePath).isDirectory()) {
      getHtmlFiles(filePath, fileList);
    } else if (file.endsWith('.html')) {
      fileList.push(filePath);
    }
  }
  return fileList;
}

const htmlFiles = getHtmlFiles(CLASS9_DIR);

let fixed = 0;

for (const filePath of htmlFiles) {
  let html = fs.readFileSync(filePath, 'utf8');
  let original = html;

  // Replace single quotes inside meta description content attributes
  html = html.replace(/<meta\s+name=["']description["']\s+content=["'](.*?)["']/gi, (match, desc) => {
    const cleanDesc = desc.replace(/'/g, '’').replace(/"/g, '&quot;');
    return `<meta name="description" content="${cleanDesc}">`;
  });

  html = html.replace(/<meta\s+property=["']og:description["']\s+content=["'](.*?)["']/gi, (match, desc) => {
    const cleanDesc = desc.replace(/'/g, '’').replace(/"/g, '&quot;');
    return `<meta property="og:description" content="${cleanDesc}">`;
  });

  html = html.replace(/<meta\s+name=["']twitter:description["']\s+content=["'](.*?)["']/gi, (match, desc) => {
    const cleanDesc = desc.replace(/'/g, '’').replace(/"/g, '&quot;');
    return `<meta name="twitter:description" content="${cleanDesc}">`;
  });

  if (html !== original) {
    fs.writeFileSync(filePath, html, 'utf8');
    fixed++;
  }
}

console.log(`🎉 Sanitized apostrophes in meta descriptions across ${fixed} Class 9 files.`);
