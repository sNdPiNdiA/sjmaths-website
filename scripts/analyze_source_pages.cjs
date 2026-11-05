const fs = require('fs');
const path = require('path');
const cheerio = require('cheerio');

const IGNORE_DIRS = new Set([
  'node_modules',
  '.git',
  '.vscode',
  '.firebase',
  '.pages-dist',
  'dist',
  'build',
  'scripts',
  'dataconnect',
  'scratch',
  'reports',
  'outputs'
]);

function walkDir(dir) {
  let files = [];
  try {
    const entries = fs.readdirSync(dir, { withFileTypes: true });
    for (const entry of entries) {
      if (IGNORE_DIRS.has(entry.name)) continue;
      const fullPath = path.join(dir, entry.name);
      if (entry.isDirectory()) {
        files = files.concat(walkDir(fullPath));
      } else if (entry.name.endsWith('.html')) {
        files.push(fullPath);
      }
    }
  } catch (err) {}
  return files;
}

const sourceHtmlFiles = walkDir('.');
console.log(`Source HTML files (excluding .pages-dist): ${sourceHtmlFiles.length}`);

const findings = {
  missingTitle: [],
  missingDescription: [],
  truncatedDescription: [],
  missingCanonical: [],
  hasComingSoon: [],
  hasBoilerplate: [],
  categoryCounts: {}
};

sourceHtmlFiles.forEach(file => {
  const relPath = file.replace(/\\/g, '/');
  const topDir = relPath.includes('/') ? relPath.split('/')[0] : 'root';
  findings.categoryCounts[topDir] = (findings.categoryCounts[topDir] || 0) + 1;

  // Skip component partials like components/header.html, footer.html
  if (relPath.startsWith('components/') || relPath.includes('/components/')) return;

  try {
    const html = fs.readFileSync(file, 'utf8');
    const $ = cheerio.load(html);

    // Title
    const title = $('title').text().trim();
    if (!title) {
      findings.missingTitle.push(relPath);
    }

    // Description
    const desc = $('meta[name="description"]').attr('content');
    if (!desc || !desc.trim()) {
      findings.missingDescription.push(relPath);
    } else {
      const trimmed = desc.trim();
      if (trimmed.endsWith('...') || trimmed.endsWith(' and') || trimmed.endsWith(',') || trimmed.length < 30) {
        findings.truncatedDescription.push({ file: relPath, desc: trimmed });
      }
    }

    // Canonical
    const canonical = $('link[rel="canonical"]').attr('href');
    if (!canonical) {
      findings.missingCanonical.push(relPath);
    }

    // Coming soon in content body (excluding navigation menus or links mentioning coming-soon)
    // Check main or article or container
    const mainText = ($('main').length ? $('main').text() : $('body').text()).toLowerCase();
    if (mainText.includes('coming soon') || mainText.includes('under construction') || mainText.includes('content will be added soon')) {
      findings.hasComingSoon.push(relPath);
    }

    // Check boilerplate
    if (html.includes('By fundamental definition, the parameter satisfies the required identity constraint') ||
        html.includes('Applied Mathematics analytical principles establish standard domain constraints')) {
      findings.hasBoilerplate.push(relPath);
    }

  } catch (e) {
    console.error('Error on', relPath, e.message);
  }
});

console.log('\n=== SOURCE AUDIT SUMMARY ===');
console.log(`Total Source Pages (excluding components): ${sourceHtmlFiles.length - 12}`);
console.log(`Missing <title>: ${findings.missingTitle.length}`);
console.log(`Missing meta description: ${findings.missingDescription.length}`);
console.log(`Truncated meta description: ${findings.truncatedDescription.length}`);
console.log(`Missing canonical: ${findings.missingCanonical.length}`);
console.log(`Pages with Coming Soon / Stubs: ${findings.hasComingSoon.length}`);
console.log(`Pages with synthetic boilerplate: ${findings.hasBoilerplate.length}`);

console.log('\nTop-level source directories:');
Object.entries(findings.categoryCounts)
  .sort((a, b) => b[1] - a[1])
  .slice(0, 25)
  .forEach(([dir, count]) => {
    console.log(`  ${dir}: ${count} pages`);
  });

if (findings.missingTitle.length > 0) {
  console.log('\nMissing Titles:', findings.missingTitle);
}
if (findings.missingDescription.length > 0) {
  console.log('\nMissing Descriptions (first 15):', findings.missingDescription.slice(0, 15));
}
if (findings.truncatedDescription.length > 0) {
  console.log('\nTruncated Descriptions (first 15):', findings.truncatedDescription.slice(0, 15));
}
if (findings.hasComingSoon.length > 0) {
  console.log('\nComing Soon pages (first 25):', findings.hasComingSoon.slice(0, 25));
}
if (findings.hasBoilerplate.length > 0) {
  console.log('\nBoilerplate pages:', findings.hasBoilerplate);
}

fs.writeFileSync('scripts/source_audit_findings.json', JSON.stringify(findings, null, 2), 'utf8');

