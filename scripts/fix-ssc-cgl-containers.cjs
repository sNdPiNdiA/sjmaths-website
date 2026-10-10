const fs = require('fs');
const path = require('path');

const repoRoot = path.resolve(__dirname, '..');
const sscRoot = path.join(repoRoot, 'ssc-cgl');

function walk(dir) {
  let files = [];
  for (const item of fs.readdirSync(dir)) {
    const full = path.join(dir, item);
    if (fs.statSync(full).isDirectory()) files = files.concat(walk(full));
    else if (item.endsWith('.html')) files.push(full);
  }
  return files;
}

const all = walk(sscRoot);
let footerFixed = 0;
let mainFixed = 0;

for (const filePath of all) {
  let content = fs.readFileSync(filePath, 'utf8');
  let modified = false;

  // 1. Missing footer container & unclosed divs in 37 legacy topic files
  if (!content.includes('footer-container')) {
    if (content.includes('<div class="container">')) {
      content = content.replace('<div class="container">', '<main class="container" id="main-content">');
      modified = true;
    }
    // Replace the trailing 4 divs with 3 divs + </main> + <div id="footer-container"></div>
    const pattern = /<\/div>\s*<\/div>\s*<\/div>\s*<\/div>\s*(<script)/;
    if (pattern.test(content)) {
      content = content.replace(pattern, '</div>\n</div>\n</div>\n</main>\n<div id="footer-container"></div>\n$1');
      modified = true;
      footerFixed++;
    }
  }

  // 2. Missing id="main-content" in topic-container (e.g., economy files)
  if (!content.includes('id="main-content"') && !content.includes("id='main-content'")) {
    if (content.includes('<main class="topic-container">')) {
      content = content.replace('<main class="topic-container">', '<main class="topic-container" id="main-content">');
      modified = true;
      mainFixed++;
    } else if (content.includes('<main class="subject-container">')) {
      content = content.replace('<main class="subject-container">', '<main class="subject-container" id="main-content">');
      modified = true;
      mainFixed++;
    }
  }

  if (modified) {
    fs.writeFileSync(filePath, content, 'utf8');
  }
}

console.log(`Successfully fixed footer-container in ${footerFixed} files.`);
console.log(`Successfully fixed missing id="main-content" in ${mainFixed} files.`);
