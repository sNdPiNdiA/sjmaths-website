/**
 * scripts/fix-truncated-descriptions.cjs
 *
 * Sitewide remediation script to fix severed/truncated meta descriptions
 * and JSON-LD structured data descriptions across ssc-cgl/ and ahc-ro-aro/ directories.
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

function repairDescription(desc, isAhc) {
  let d = desc.trim();

  // Pattern 1: AHC RO/ARO severed ending in ", and a live" or ", and a" or ", and"
  if (isAhc) {
    if (/, and\s*(?:a\s*(?:live)?)?\s*$/i.test(d)) {
      return d.replace(/, and\s*(?:a\s*(?:live)?)?\s*$/i, ', and full exam test series.');
    }
    if (/practice questions,\s*and\s*$/i.test(d)) {
      return d.replace(/practice questions,\s*and\s*$/i, 'practice questions, and full exam test series.');
    }
    return desc;
  }

  // Pattern 2: SSC CGL severed ending in ", and" or "interactive practice" without questions
  if (/, and\s*$/i.test(d)) {
    return d.replace(/, and\s*$/i, ', and solved previous year questions.');
  }

  if (/interactive practice questions\s*$/i.test(d)) {
    return d + ', and solved previous year questions.';
  }

  if (/interactive practice\s*$/i.test(d)) {
    return d + ' questions, and solved previous year questions.';
  }

  if (/under SSC CGL General\s*$/i.test(d)) {
    return d + ' Intelligence & Reasoning.';
  }

  return desc;
}

function remediateFile(filePath) {
  let content = fs.readFileSync(filePath, 'utf8');
  let original = content;
  const isAhc = filePath.includes('ahc-ro-aro');

  // 1. Match meta description, og:description, twitter:description tags
  const metaDescRegex = /<meta\s+([^>]*?(?:name|property)=["'](?:description|og:description|twitter:description)["'][^>]*?)>/gi;

  content = content.replace(metaDescRegex, (tag) => {
    const contentMatch = tag.match(/content=["']([^"']*)["']/i);
    if (!contentMatch) return tag;

    const oldDesc = contentMatch[1];
    const newDesc = repairDescription(oldDesc, isAhc);

    if (newDesc !== oldDesc) {
      return tag.replace(contentMatch[0], `content="${newDesc}"`);
    }
    return tag;
  });

  // 2. Match JSON-LD script blocks
  const jsonLdRegex = /<script\s+type=["']application\/ld\+json["'][^>]*>([\s\S]*?)<\/script>/gi;

  content = content.replace(jsonLdRegex, (scriptBlock, jsonText) => {
    // Check if jsonText has severed description
    if (/"description":\s*"[^"]*, and(?:\s+a(?:\s+live)?)?"/i.test(jsonText)) {
      const repairedJsonText = jsonText.replace(/"description":\s*"([^"]*)"/gi, (match, desc) => {
        const repaired = repairDescription(desc, isAhc);
        return `"description": "${repaired}"`;
      });
      return scriptBlock.replace(jsonText, repairedJsonText);
    }
    return scriptBlock;
  });

  if (content !== original) {
    fs.writeFileSync(filePath, content, 'utf8');
    return true;
  }
  return false;
}

function run() {
  const allFiles = getAllHtmlFiles(ROOT_DIR);
  let totalFiles = allFiles.length;
  let modifiedFiles = 0;

  for (const file of allFiles) {
    if (remediateFile(file)) {
      modifiedFiles++;
    }
  }

  console.log(`Scanned ${totalFiles} HTML files.`);
  console.log(`Repaired severed descriptions in ${modifiedFiles} files.`);
}

run();
