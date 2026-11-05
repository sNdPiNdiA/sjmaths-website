/**
 * scripts/fix-geography-paper-tags.cjs
 *
 * Sitewide remediation script to retag UPSC Geography pages from GS-3 to GS-1.
 * In the UPSC Civil Services Examination, Geography is exclusively General Studies Paper 1 (GS-1),
 * whereas GS-3 is Economy, Sci-Tech, and Environment.
 */

const fs = require('fs');
const path = require('path');

const TARGET_DIR = path.join(__dirname, '..', 'upsc', 'geography');

function getAllFiles(dir, fileList = []) {
  if (!fs.existsSync(dir)) return fileList;
  const entries = fs.readdirSync(dir, { withFileTypes: true });
  for (const entry of entries) {
    const fullPath = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      getAllFiles(fullPath, fileList);
    } else if (entry.isFile() && (entry.name.endsWith('.html') || entry.name.endsWith('.json'))) {
      fileList.push(fullPath);
    }
  }
  return fileList;
}

function transformContent(content) {
  let updated = content;

  // 1. Handle combined GS-1 / GS-3 or GS-3 / GS-1 occurrences
  updated = updated.replace(/GS-1\s*\/\s*GS-3/gi, 'GS-1');
  updated = updated.replace(/GS-3\s*\/\s*GS-1/gi, 'GS-1');
  updated = updated.replace(/GS-1\s+and\s+GS-3/gi, 'GS-1');
  updated = updated.replace(/GS-3\s+and\s+GS-1/gi, 'GS-1');
  updated = updated.replace(/GS-1\s*&\s*GS-3/gi, 'GS-1');
  updated = updated.replace(/GS-3\s*&\s*GS-1/gi, 'GS-1');
  updated = updated.replace(/GS-1\s*&amp;\s*GS-3/gi, 'GS-1');
  updated = updated.replace(/GS-3\s*&amp;\s*GS-1/gi, 'GS-1');

  // Hindi combined patterns
  updated = updated.replace(/जीएस-1\s*\/\s*जीएस-3/g, 'जीएस-1');
  updated = updated.replace(/जीएस-3\s*\/\s*जीएस-1/g, 'जीएस-1');
  updated = updated.replace(/जीएस-1\s+और\s+जीएस-3/g, 'जीएस-1');
  updated = updated.replace(/जीएस-3\s+और\s+जीएस-1/g, 'जीएस-1');

  // 2. Titles, meta tags, and headers
  updated = updated.replace(/\|\s*UPSC\s+GS-3\s*\|/gi, '| UPSC GS-1 |');
  updated = updated.replace(/-\s*UPSC\s+GS-3\s*\|/gi, '- UPSC GS-1 |');
  updated = updated.replace(/UPSC\s+GS-3\s+की\s+विस्तृत\s+गाइड/g, 'UPSC GS-1 की विस्तृत गाइड');
  updated = updated.replace(/UPSC\s+GS-3\b/g, 'UPSC GS-1');

  // 3. General GS-3 and GS 3 replacements
  updated = updated.replace(/GS-3\b/g, 'GS-1');
  updated = updated.replace(/GS 3\b/g, 'GS-1');
  updated = updated.replace(/जीएस-3\b/g, 'जीएस-1');
  updated = updated.replace(/जीएस 3\b/g, 'जीएस-1');

  // 4. Leftover variations
  updated = updated.replace(/GS-\s*3\b/g, 'GS-1');
  updated = updated.replace(/जीएस-\s*3\b/g, 'जीएस-1');

  return updated;
}

function remediateGeographyFile(filePath) {
  const content = fs.readFileSync(filePath, 'utf8');
  if (!content.includes('GS-3') && !content.includes('GS 3') && !content.includes('जीएस-3') && !content.includes('जीएस 3')) {
    return false;
  }

  const updated = transformContent(content);

  // Validate JSON integrity
  if (filePath.endsWith('.json')) {
    try {
      JSON.parse(updated);
    } catch (e) {
      throw new Error(`JSON parse error in ${filePath}: ${e.message}`);
    }
  } else if (filePath.endsWith('.html')) {
    const pageDataMatches = updated.matchAll(/<script[^>]*id=["']upsc-page-data["'][^>]*>([\s\S]*?)<\/script>/gi);
    for (const m of pageDataMatches) {
      try {
        JSON.parse(m[1]);
      } catch (e) {
        throw new Error(`Embedded JSON parse error in ${filePath}: ${e.message}`);
      }
    }
    const schemaMatches = updated.matchAll(/<script[^>]*type=["']application\/ld\+json["'][^>]*>([\s\S]*?)<\/script>/gi);
    for (const m of schemaMatches) {
      try {
        JSON.parse(m[1]);
      } catch (e) {
        throw new Error(`LD+JSON parse error in ${filePath}: ${e.message}`);
      }
    }
  }

  if (updated !== content) {
    fs.writeFileSync(filePath, updated, 'utf8');
    return true;
  }
  return false;
}

function run() {
  const files = getAllFiles(TARGET_DIR);
  console.log(`Found ${files.length} candidate files under ${TARGET_DIR}`);
  let htmlCount = 0;
  let jsonCount = 0;

  for (const file of files) {
    if (remediateGeographyFile(file)) {
      if (file.endsWith('.html')) htmlCount++;
      else if (file.endsWith('.json')) jsonCount++;
    }
  }

  console.log(`Successfully retagged:`);
  console.log(`  HTML files: ${htmlCount}`);
  console.log(`  JSON files: ${jsonCount}`);
  console.log(`  Total files: ${htmlCount + jsonCount}`);
}

run();
