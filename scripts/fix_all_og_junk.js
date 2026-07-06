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

  // Clean up any line containing >s Geometry or duplicate closing quotes/brackets in og/twitter tags
  html = html.replace(/">s Geometry[\s\S]*?>/gi, '">');
  html = html.replace(/">s Formula[\s\S]*?>/gi, '">');
  html = html.replace(/">>/g, '">');

  if (html !== original) {
    fs.writeFileSync(filePath, html, 'utf8');
    fixed++;
  }
}

console.log(`🎉 Cleaned up og/twitter tag line junk in ${fixed} Class 9 files.`);
