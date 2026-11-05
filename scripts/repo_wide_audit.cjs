const fs = require('fs');
const path = require('path');
const cheerio = require('cheerio');

const IGNORE_DIRS = new Set([
  'node_modules',
  '.git',
  '.vscode',
  '.firebase',
  'scripts',
  'dataconnect',
  'dist',
  'build'
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
  } catch (err) {
    // ignore
  }
  return files;
}

console.log('Discovering all HTML files across the repository...');
const allHtmlFiles = walkDir('.');
console.log(`Total HTML files found: ${allHtmlFiles.length}`);

const results = {
  missingTitle: [],
  missingDescription: [],
  truncatedDescription: [],
  missingCanonical: [],
  hasPlaceholder: [],
  hasComingSoon: [],
  hasBoilerplate: [],
  categoryCounts: {}
};

const placeholderPhrases = [
  'coming soon',
  'under construction',
  'lorem ipsum',
  'content will be added soon',
  'page under development',
  'By fundamental definition, the parameter satisfies the required identity constraint'
];

allHtmlFiles.forEach(file => {
  const relPath = file.replace(/\\/g, '/');
  
  // Categorize
  const topDir = relPath.includes('/') ? relPath.split('/')[0] : 'root';
  results.categoryCounts[topDir] = (results.categoryCounts[topDir] || 0) + 1;

  try {
    const html = fs.readFileSync(file, 'utf8');
    const $ = cheerio.load(html);

    // Title check
    const title = $('title').text().trim();
    if (!title) {
      results.missingTitle.push(relPath);
    }

    // Description check
    const desc = $('meta[name="description"]').attr('content');
    if (!desc || !desc.trim()) {
      results.missingDescription.push(relPath);
    } else {
      const trimmed = desc.trim();
      if (trimmed.endsWith('...') || trimmed.endsWith(' and') || trimmed.endsWith(',') || trimmed.length < 30) {
        results.truncatedDescription.push({ file: relPath, desc: trimmed });
      }
    }

    // Canonical check
    const canonical = $('link[rel="canonical"]').attr('href');
    if (!canonical) {
      results.missingCanonical.push(relPath);
    }

    // Check placeholder / coming soon
    const bodyText = $('body').text().toLowerCase();
    if (bodyText.includes('coming soon') || bodyText.includes('under construction') || bodyText.includes('content will be added soon')) {
      results.hasComingSoon.push(relPath);
    }

    // Check forbidden boilerplate
    if (html.includes('By fundamental definition, the parameter satisfies the required identity constraint') ||
        html.includes('Applied Mathematics analytical principles establish standard domain constraints')) {
      results.hasBoilerplate.push(relPath);
    }

  } catch (e) {
    console.error(`Error reading ${relPath}:`, e.message);
  }
});

console.log('\n=== AUDIT RESULTS SUMMARY ===');
console.log(`Total HTML files: ${allHtmlFiles.length}`);
console.log(`Missing <title>: ${results.missingTitle.length}`);
console.log(`Missing meta description: ${results.missingDescription.length}`);
console.log(`Truncated/malformed meta description: ${results.truncatedDescription.length}`);
console.log(`Missing canonical link: ${results.missingCanonical.length}`);
console.log(`Contains 'Coming Soon' / placeholder stubs: ${results.hasComingSoon.length}`);
console.log(`Contains synthetic boilerplate phrases: ${results.hasBoilerplate.length}`);

console.log('\nTop-level category file counts:');
Object.entries(results.categoryCounts)
  .sort((a, b) => b[1] - a[1])
  .slice(0, 20)
  .forEach(([dir, count]) => {
    console.log(`  ${dir}: ${count} files`);
  });

if (results.missingTitle.length > 0) {
  console.log('\nSample Missing Titles (first 10):', results.missingTitle.slice(0, 10));
}
if (results.missingDescription.length > 0) {
  console.log('\nSample Missing Descriptions (first 10):', results.missingDescription.slice(0, 10));
}
if (results.truncatedDescription.length > 0) {
  console.log('\nSample Truncated Descriptions (first 10):', results.truncatedDescription.slice(0, 10));
}
if (results.hasComingSoon.length > 0) {
  console.log('\nSample Coming Soon files (first 15):', results.hasComingSoon.slice(0, 15));
}
if (results.hasBoilerplate.length > 0) {
  console.log('\nBoilerplate files:', results.hasBoilerplate);
}

// Write full report to JSON for deep analysis
fs.writeFileSync('scripts/audit_results.json', JSON.stringify(results, null, 2), 'utf8');
console.log('\nDetailed results written to scripts/audit_results.json');

