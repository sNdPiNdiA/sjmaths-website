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

for (const filePath of htmlFiles) {
  let html = fs.readFileSync(filePath, 'utf8');
  let modified = false;

  const relPath = path.relative(ROOT_DIR, filePath).replace(/\\/g, '/');

  // Fix stray >>
  while (html.includes('">>')) {
    html = html.replace(/">>/g, '">');
    modified = true;
  }

  const filename = path.basename(filePath, '.html');

  if (relPath.includes('ncert-examplar-practice/chapter-10-heron-formula/')) {
    const exNum = filename.replace('exemplar-', '').replace('-', '.');
    const newDesc = `Practice Class 9 Maths Heron's Formula Exemplar ${exNum} NCERT Problems with detailed step-by-step solutions on SJMaths.`;
    html = html.replace(/<meta\s+name=["']description["']\s+content=["'](.*?)["']/i, `<meta name="description" content="${newDesc}">`);
    modified = true;
  } else if (relPath.includes('tests/chapter-wise/chapter-5-introduction-to-euclids-geometry/')) {
    const level = filename.replace(/-/g, ' ').toUpperCase();
    const newDesc = `Take Class 9 Euclid's Geometry ${level} Online Test with step-by-step solutions, key axioms, and instant scoring on SJMaths.`;
    html = html.replace(/<meta\s+name=["']description["']\s+content=["'](.*?)["']/i, `<meta name="description" content="${newDesc}">`);
    modified = true;
  } else if (relPath.includes('worksheets/chapter-5-introduction-to-euclids-geometry/')) {
    const level = filename.replace(/-/g, ' ').toUpperCase();
    const newDesc = `Practice Class 9 Euclid's Geometry ${level} Worksheet with step-by-step solutions, key axioms, and practice questions on SJMaths.`;
    html = html.replace(/<meta\s+name=["']description["']\s+content=["'](.*?)["']/i, `<meta name="description" content="${newDesc}">`);
    modified = true;
  }

  if (modified) {
    fs.writeFileSync(filePath, html, 'utf8');
  }
}

console.log('🎉 Final Class 9 micro-cleanup complete.');
