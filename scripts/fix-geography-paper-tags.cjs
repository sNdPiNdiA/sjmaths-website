/**
 * scripts/fix-geography-paper-tags.cjs
 *
 * Sitewide remediation script to retag UPSC Geography pages from GS-3 to GS-1.
 * In the UPSC Civil Services Examination, Geography is General Studies Paper 1 (GS-1),
 * whereas GS-3 is Economy, Sci-Tech, and Environment.
 */

const fs = require('fs');
const path = require('path');

const TARGET_DIR = path.join(__dirname, '..', 'upsc', 'geography');

function getAllHtmlFiles(dir, fileList = []) {
  if (!fs.existsSync(dir)) return fileList;
  const entries = fs.readdirSync(dir, { withFileTypes: true });
  for (const entry of entries) {
    const fullPath = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      getAllHtmlFiles(fullPath, fileList);
    } else if (entry.isFile() && entry.name.endsWith('.html')) {
      fileList.push(fullPath);
    }
  }
  return fileList;
}

function remediateGeographyFile(filePath) {
  let content = fs.readFileSync(filePath, 'utf8');
  let original = content;

  // 1. Replace title / og:title / twitter:title tags
  content = content.replace(/\|\s*UPSC\s+GS-3\s*\|/g, '| UPSC GS-1 |');
  content = content.replace(/-\s*UPSC\s+GS-3\s*\|/g, '- UPSC GS-1 |');

  // 2. Replace keywords and schema mentions of UPSC GS-3 in Geography context
  content = content.replace(/UPSC\s+GS-3\b/g, (match, offset) => {
    // Check surrounding context: do not change if part of an explicit cross-syllabus comparison like "GS-1/GS-3"
    const prevText = content.slice(Math.max(0, offset - 10), offset);
    if (prevText.includes('GS-1/')) {
      return match;
    }
    return 'UPSC GS-1';
  });

  // 3. Replace Hindi topic description
  content = content.replace(/UPSC\s+GS-3\s+की\s+विस्तृत\s+गाइड/g, 'UPSC GS-1 की विस्तृत गाइड');

  if (content !== original) {
    fs.writeFileSync(filePath, content, 'utf8');
    return true;
  }
  return false;
}

function run() {
  const files = getAllHtmlFiles(TARGET_DIR);
  console.log(`Found ${files.length} HTML files under ${TARGET_DIR}`);
  let modifiedCount = 0;

  for (const file of files) {
    if (remediateGeographyFile(file)) {
      modifiedCount++;
    }
  }

  console.log(`Successfully retagged ${modifiedCount} files from GS-3 to GS-1.`);
}

run();

