const fs = require('fs');
const path = require('path');

const ROOT_DIR = path.join(__dirname, '..');
const CLASS12_DIR = path.join(ROOT_DIR, 'class-12-maths');

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

const htmlFiles = getHtmlFiles(CLASS12_DIR);

let fixedBrackets = 0;
let setNoindexStubs = 0;

for (const filePath of htmlFiles) {
  let html = fs.readFileSync(filePath, 'utf8');
  let modified = false;

  // 1. Fix stray double angle brackets (e.g. .html">>, content="...">>)
  if (html.includes('">>')) {
    html = html.replace(/">>/g, '">');
    fixedBrackets++;
    modified = true;
  }

  // 2. Check for stub / placeholder text
  const isStub = /is being updated|intentionally excluded from search indexing|Updating/i.test(html);
  if (isStub) {
    if (/<meta\s+name=["']robots["']\s+content=["'][^"']*index/i.test(html) && !/<meta\s+name=["']robots["']\s+content=["'][^"']*noindex/i.test(html)) {
      html = html.replace(
        /<meta\s+name=["']robots["']\s+content=["'][^"']*index[^"']*["']/i,
        '<meta name="robots" content="noindex, follow">'
      );
      setNoindexStubs++;
      modified = true;
    }
  }

  if (modified) {
    fs.writeFileSync(filePath, html, 'utf8');
  }
}

console.log(`🎉 Fixed stray double brackets in ${fixedBrackets} files.`);
console.log(`📌 Properly set noindex on ${setNoindexStubs} stub/placeholder files to protect domain SEO quality.`);
