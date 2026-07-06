const fs = require('fs');
const path = require('path');

const ROOT_DIR = path.join(__dirname, '..');
const SSC_DIR = path.join(ROOT_DIR, 'ssc-cgl');

function generateHtmlList(node) {
  if (!node) return '';
  let html = `<li><strong>${node.label || ''}</strong>`;
  if (node.date) {
    html += ` (${node.date})`;
  }
  if (node.children && node.children.length > 0) {
    html += '\n<ul>\n';
    for (const child of node.children) {
      html += generateHtmlList(child);
    }
    html += '</ul>\n';
  }
  html += '</li>\n';
  return html;
}

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

const allFiles = getHtmlFiles(SSC_DIR);
console.log(`Found ${allFiles.length} SSC-CGL files to process for noscript pre-rendering.`);

let successCount = 0;
let skippedCount = 0;
let errorCount = 0;

for (const filePath of allFiles) {
  let html = fs.readFileSync(filePath, 'utf8');

  // Skip if already contains noscript list
  if (html.includes('class="noscript-mindmap"')) {
    skippedCount++;
    continue;
  }

  const renderRegex = /renderMindmap\(([\s\S]*?)\s*,\s*(?:undefined|null)/i;
  const match = html.match(renderRegex);
  if (!match) {
    skippedCount++;
    continue;
  }

  try {
    const rawJson = match[1].trim();
    // Parse JSON
    const data = JSON.parse(rawJson);

    // Generate list
    const listHtml = `\n    <noscript class="noscript-mindmap">\n      <p>This is a static text representation of the interactive mindmap. Detailed nodes and hierarchy:</p>\n      <ul>\n        ${generateHtmlList(data)}      </ul>\n    </noscript>\n`;

    if (html.includes('<div id="prehistory-mindmap-container"></div>')) {
      html = html.replace(
        '<div id="prehistory-mindmap-container"></div>',
        `<div id="prehistory-mindmap-container">${listHtml}</div>`
      );
      fs.writeFileSync(filePath, html, 'utf8');
      successCount++;
    } else if (html.includes('<div id="prehistory-mindmap-container">')) {
      skippedCount++;
    } else {
      skippedCount++;
    }
  } catch (e) {
    errorCount++;
  }
}

console.log(`\n================ SSC-CGL PRERENDER REPORT ================`);
console.log(`Processed files: ${allFiles.length}`);
console.log(`Successfully pre-rendered noscript lists: ${successCount}`);
console.log(`Skipped (already pre-rendered or no match): ${skippedCount}`);
console.log(`Errors: ${errorCount}`);
