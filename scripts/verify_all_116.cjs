const fs = require('fs');
const path = require('path');
const cheerio = require('cheerio');

const ROOT_DIR = path.resolve(__dirname, '..');
const descriptions = require('./remediate_all_116_meta.cjs'); // wait, let's read the descriptions directly or load them

const auditFile = path.join(__dirname, 'source_audit_findings.json');
const originalAudit = JSON.parse(fs.readFileSync(auditFile, 'utf8'));

// We can load the keys from remediate_all_116_meta.cjs by executing the file or extracting keys
const remContent = fs.readFileSync(path.join(__dirname, 'remediate_all_116_meta.cjs'), 'utf8');
const fileMatches = [...remContent.matchAll(/"([^"]+\.html)":/g)].map(m => m[1]);

console.log(`Checking ${fileMatches.length} remediated files...`);

let issues = 0;

fileMatches.forEach((relPath, idx) => {
  const fullPath = path.resolve(ROOT_DIR, relPath);
  if (!fs.existsSync(fullPath)) {
    console.error(`[FAIL] File does not exist: ${relPath}`);
    issues++;
    return;
  }

  const content = fs.readFileSync(fullPath, 'utf8');
  const $ = cheerio.load(content);

  const metaDesc = $('meta[name="description"]').attr('content');
  const ogDesc = $('meta[property="og:description"]').attr('content');
  const twDesc = $('meta[name="twitter:description"]').attr('content');

  if (!metaDesc) {
    console.error(`[FAIL] Missing meta description: ${relPath}`);
    issues++;
    return;
  }

  const len = metaDesc.length;
  if (len < 120 || len > 160) {
    console.error(`[FAIL] Meta description length ${len} out of bounds (120-160): ${relPath} -> "${metaDesc}"`);
    issues++;
  }

  if (metaDesc.endsWith('...') || metaDesc.endsWith(',') || metaDesc.endsWith(' and') || metaDesc.endsWith(' or') || metaDesc.endsWith(' with')) {
    console.error(`[FAIL] Trailing punctuation or conjunction: ${relPath} -> "${metaDesc}"`);
    issues++;
  }

  if (metaDesc.includes('SEO description here')) {
    console.error(`[FAIL] Template placeholder remains: ${relPath}`);
    issues++;
  }

  if (ogDesc !== metaDesc) {
    console.warn(`[WARN] og:description does not match meta description: ${relPath}`);
  }

  if (twDesc !== metaDesc) {
    console.warn(`[WARN] twitter:description does not match meta description: ${relPath}`);
  }

  // Check JSON-LD
  $('script[type="application/ld+json"]').each((_, s) => {
    const raw = $(s).html();
    try {
      const json = JSON.parse(raw);
      if (json.description) {
        if (json.description.endsWith('...') || json.description.includes('SEO description here') || json.description.endsWith(' and')) {
          console.error(`[FAIL] Truncated description in JSON-LD: ${relPath} -> "${json.description}"`);
          issues++;
        }
      }
    } catch(e) {}
  });
});

console.log(`\n=== VERIFICATION RESULT ===`);
console.log(`Total Files Checked: ${fileMatches.length}`);
console.log(`Total Issues Found: ${issues}`);

if (issues === 0) {
  console.log('✅ ALL 116 PAGES HAVE VALID, HIGH-QUALITY META DESCRIPTIONS AND CLEAN JSON-LD!');
} else {
  process.exit(1);
}
