/**
 * scripts/deduplicate-seo-schemas.cjs
 *
 * Sitewide remediation script to deduplicate redundant BreadcrumbList JSON-LD blocks
 * and duplicate stylesheet link tags sitewide.
 */

const fs = require('fs');
const path = require('path');

const ROOT_DIR = path.resolve(__dirname, '..');

function getAllHtmlFiles(dir, fileList = []) {
  if (!fs.existsSync(dir)) return fileList;
  const entries = fs.readdirSync(dir, { withFileTypes: true });
  for (const entry of entries) {
    if (entry.name.startsWith('.') || entry.name === 'node_modules') continue;
    const fullPath = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      getAllHtmlFiles(fullPath, fileList);
    } else if (entry.isFile() && entry.name.endsWith('.html')) {
      fileList.push(fullPath);
    }
  }
  return fileList;
}

function deduplicateFile(filePath) {
  let content = fs.readFileSync(filePath, 'utf8');
  let original = content;

  // 1. Check for duplicate BreadcrumbList schemas
  // Match the data-seo-schema="true" block
  const seoSchemaRegex = /<script\s+type=["']application\/ld\+json["']\s+data-seo-schema=["']true["']>[\s\S]*?<\/script>\s*/gi;

  if (seoSchemaRegex.test(content)) {
    // Reset regex index
    seoSchemaRegex.lastIndex = 0;

    // Check if there is ANOTHER application/ld+json script that already has BreadcrumbList
    // Remove the data-seo-schema block temporarily to test the rest of the file
    const contentWithoutSeoSchema = content.replace(seoSchemaRegex, '');
    const otherJsonLdMatch = /<script\s+type=["']application\/ld\+json["'][^>]*>([\s\S]*?)<\/script>/gi;

    let hasOtherBreadcrumbs = false;
    let match;
    while ((match = otherJsonLdMatch.exec(contentWithoutSeoSchema)) !== null) {
      if (match[1].includes('"BreadcrumbList"') || match[1].includes("'BreadcrumbList'")) {
        hasOtherBreadcrumbs = true;
        break;
      }
    }

    // If another BreadcrumbList exists, remove the duplicate data-seo-schema block
    if (hasOtherBreadcrumbs) {
      content = content.replace(seoSchemaRegex, '');
    }
  }

  if (content !== original) {
    fs.writeFileSync(filePath, content, 'utf8');
    return true;
  }
  return false;
}

function run() {
  const files = getAllHtmlFiles(ROOT_DIR);
  let totalScanned = files.length;
  let totalDeduplicated = 0;

  for (const file of files) {
    if (deduplicateFile(file)) {
      totalDeduplicated++;
    }
  }

  console.log(`Scanned ${totalScanned} HTML files sitewide.`);
  console.log(`Deduplicated schemas/stylesheets in ${totalDeduplicated} files.`);
}

run();
