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

let cleaned = 0;

for (const filePath of htmlFiles) {
  let html = fs.readFileSync(filePath, 'utf8');
  let modified = false;

  const relPath = path.relative(ROOT_DIR, filePath).replace(/\\/g, '/');
  const filename = path.basename(filePath, '.html');

  // Fix malformed description tags
  if (/<meta\s+name=["']description["'][\s\S]*?>\s*s\s*Formula/i.test(html) || /<meta\s+name=["']description["'][\s\S]*?>\s*Exemplar/i.test(html)) {
    const pageTitle = html.match(/<title[^>]*>(.*?)<\/title>/i);
    const cleanTitleText = pageTitle ? pageTitle[1].replace(/\s*\|\s*SJMaths/i, '').trim() : filename;
    const cleanDesc = `Practice ${cleanTitleText} for Class 9 CBSE Board exam preparation. Access step-by-step solutions, key formulas, and expert revision notes on SJMaths.`;

    html = html.replace(/<meta\s+name=["']description["'][\s\S]*?>([\s\S]*?>)*/i, `<meta name="description" content="${cleanDesc}">`);
    cleaned++;
    modified = true;
  }

  // Ensure unique meta description for each file based on its relative path
  const descMatch = html.match(/<meta\s+name=["']description["']\s+content=["'](.*?)["']/i);
  if (descMatch) {
    let currentDesc = descMatch[1];
    if (relPath.includes('chapter-10-heron-formula')) {
      const exNum = filename.replace('exemplar-', '').replace('-', '.');
      currentDesc = `Practice Class 9 Maths Heron's Formula Exemplar Exercise ${exNum} NCERT problems with step-by-step solutions on SJMaths.`;
      html = html.replace(/<meta\s+name=["']description["']\s+content=["'](.*?)["']/i, `<meta name="description" content="${currentDesc}">`);
      modified = true;
    } else if (relPath.includes('chapter-5-introduction-to-euclids-geometry')) {
      const type = filename.replace(/-/g, ' ').toUpperCase();
      const parentDir = relPath.includes('tests') ? 'Online Test' : 'Worksheet';
      currentDesc = `Practice Class 9 Euclid's Geometry ${type} ${parentDir} with step-by-step solutions, key axioms, and revision notes on SJMaths.`;
      html = html.replace(/<meta\s+name=["']description["']\s+content=["'](.*?)["']/i, `<meta name="description" content="${currentDesc}">`);
      modified = true;
    }
  }

  if (modified) {
    fs.writeFileSync(filePath, html, 'utf8');
  }
}

console.log(`🎉 Cleaned malformed & duplicate meta description tags in ${cleaned} Class 9 files.`);
