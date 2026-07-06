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

let count = 0;

for (const filePath of htmlFiles) {
  let html = fs.readFileSync(filePath, 'utf8');

  if (html.includes('">>')) {
    html = html.replaceAll('">>', '">');
    fs.writeFileSync(filePath, html, 'utf8');
    count++;
  }
}

console.log(`🎉 Fixed double angle brackets in ${count} Class 9 files.`);
