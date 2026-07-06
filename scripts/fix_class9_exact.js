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

  // Fix any remaining double brackets >>
  if (html.includes('">>')) {
    html = html.replace(/">>/g, '">');
    modified = true;
  }
  if (html.includes('.">')) {
    html = html.replace(/\.">\s*>/g, '." >');
    modified = true;
  }

  // Check for short stubs (under 15 lines or less than 50 words)
  const lines = html.split('\n').length;
  if (lines <= 15 && !html.includes('noindex')) {
    html = html.replace(
      /<meta\s+name=["']robots["']\s+content=["'][^"']*index[^"']*["']/i,
      '<meta name="robots" content="noindex, follow">'
    );
    modified = true;
  }

  // Ensure unique description on every indexable file
  if (!html.includes('noindex')) {
    const filename = path.basename(filePath, '.html');
    const pageTitleM = html.match(/<title[^>]*>(.*?)<\/title>/i);
    const pageTitle = pageTitleM ? pageTitleM[1].replace(/\s*\|\s*SJMaths/i, '').trim() : filename;

    const uniqueDesc = `Practice ${pageTitle} (${relPath}) for Class 9 CBSE Board exam preparation. Access step-by-step solutions, key formulas, and expert revision notes on SJMaths.`;

    if (/<meta\s+name=["']description["']/i.test(html)) {
      html = html.replace(/<meta\s+name=["']description["']\s+content=["'](.*?)["']/i, `<meta name="description" content="${uniqueDesc}">`);
      modified = true;
    }
  }

  if (modified) {
    fs.writeFileSync(filePath, html, 'utf8');
  }
}

console.log('🎉 Class 9 exact metadata & stub cleanup complete.');
