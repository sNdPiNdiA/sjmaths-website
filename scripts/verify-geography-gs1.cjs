/**
 * scripts/verify-geography-gs1.cjs
 *
 * Comprehensive verification script checking that:
 * 1. Zero files in upsc/geography/ contain GS-3 or GS 3 (case-insensitive or in Hindi).
 * 2. All JSON files under upsc/geography/ parse without error.
 * 3. All embedded JSON-LD and page-data scripts in upsc/geography/ HTML parse without error.
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
    } else if (entry.isFile()) {
      fileList.push(fullPath);
    }
  }
  return fileList;
}

function verify() {
  const files = getAllFiles(TARGET_DIR);
  console.log(`Scanning ${files.length} files under ${TARGET_DIR} for GS-3 / GS 3 and syntax validity...`);

  let failingFiles = [];
  let jsonErrors = [];

  for (const file of files) {
    const content = fs.readFileSync(file, 'utf8');

    // 1. Check for any GS-3 / GS 3 occurrences
    if (/gs[-\s]?3/i.test(content) || /जीएस[-\s]?3/i.test(content)) {
      failingFiles.push(file);
    }

    // 2. Validate standalone JSON files
    if (file.endsWith('.json')) {
      try {
        JSON.parse(content);
      } catch (e) {
        jsonErrors.push({ file, err: e.message });
      }
    }

    // 3. Validate embedded JSONs in HTML files
    if (file.endsWith('.html')) {
      const pageDataMatches = content.matchAll(/<script[^>]*id=["']upsc-page-data["'][^>]*>([\s\S]*?)<\/script>/gi);
      for (const m of pageDataMatches) {
        try {
          JSON.parse(m[1]);
        } catch (e) {
          jsonErrors.push({ file, type: 'upsc-page-data', err: e.message });
        }
      }

      const schemaMatches = content.matchAll(/<script[^>]*type=["']application\/ld\+json["'][^>]*>([\s\S]*?)<\/script>/gi);
      for (const m of schemaMatches) {
        try {
          JSON.parse(m[1]);
        } catch (e) {
          jsonErrors.push({ file, type: 'ld+json', err: e.message });
        }
      }
    }
  }

  if (failingFiles.length > 0) {
    console.error(`❌ Verification failed! ${failingFiles.length} file(s) still contain GS-3:`);
    failingFiles.slice(0, 10).forEach(f => console.error(`  - ${f}`));
    process.exit(1);
  }

  if (jsonErrors.length > 0) {
    console.error(`❌ Verification failed! ${jsonErrors.length} JSON syntax error(s):`);
    jsonErrors.forEach(e => console.error(`  - ${e.file}: ${e.err}`));
    process.exit(1);
  }

  console.log(`✅ Verification passed! Exactly 0 files in upsc/geography/ contain GS-3.`);
  console.log(`✅ All JSON and embedded schema scripts are 100% syntactically valid.`);
}

verify();
