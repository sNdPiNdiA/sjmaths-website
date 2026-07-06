const fs = require('fs');
const path = require('path');

const ROOT_DIR = path.join(__dirname, '..');
const UPSC_DIR = path.join(ROOT_DIR, 'upsc');

function getHtmlFiles(dir, fileList = []) {
  if (!fs.existsSync(dir)) return fileList;
  const files = fs.readdirSync(dir);
  for (const file of files) {
    const filePath = path.join(dir, file);
    const stat = fs.statSync(filePath);
    if (stat.isDirectory()) {
      getHtmlFiles(filePath, fileList);
    } else if (file.endsWith('.html')) {
      fileList.push(filePath);
    }
  }
  return fileList;
}

const allFiles = getHtmlFiles(UPSC_DIR);
let fixedCount = 0;

for (const filePath of allFiles) {
  let html = fs.readFileSync(filePath, 'utf8');
  let modified = false;

  const relPath = path.relative(ROOT_DIR, filePath).replace(/\\/g, '/');
  const isHindi = relPath.includes('/hi/');

  // 1. Ensure <!DOCTYPE html>
  if (!/^<!DOCTYPE html>/i.test(html.trim())) {
    html = '<!DOCTYPE html>\n' + html.trim();
    modified = true;
  }

  // 2. Ensure <html lang="...">
  if (!/<html[^>]*lang=/i.test(html)) {
    const langAttr = isHindi ? 'hi' : 'en';
    html = html.replace(/<html(?![^>]*lang=)/i, `<html lang="${langAttr}"`);
    modified = true;
  }

  // 3. Ensure <meta charset="UTF-8"> inside <head>
  if (!/<meta\s+charset=["']UTF-8["']/i.test(html)) {
    if (html.includes('<head>')) {
      html = html.replace('<head>', '<head>\n    <meta charset="UTF-8">');
      modified = true;
    }
  }

  if (modified) {
    fs.writeFileSync(filePath, html, 'utf8');
    fixedCount++;
  }
}

console.log(`🎉 Fixed doctype, html lang, and charset tags across ${fixedCount} UPSC files.`);
