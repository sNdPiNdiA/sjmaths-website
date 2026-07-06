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

  // Replace any occurrence of >> in head or meta tags
  html = html.replace(/<meta\s+name=["']description["']\s+content=["'](.*?)["']\s*>/gi, (match, desc) => {
    const cleanDesc = desc.replace(/[">]+/g, '').trim();
    return `<meta name="description" content="${cleanDesc}">`;
  });

  // Clean up any remaining double closing brackets
  html = html.replace(/">>/g, '">').replace(/>>/g, '>');

  if (html !== original) {
    fs.writeFileSync(filePath, html, 'utf8');
    fixed++;
  }
}

console.log(`🎉 Fixed stray >> brackets in ${fixed} Class 9 files.`);
