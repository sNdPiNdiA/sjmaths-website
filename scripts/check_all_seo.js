const fs = require('fs');
const path = require('path');

const SKIPPED_DIRS = new Set([
  '.git', '.firebase', '.vscode', 'assets', 'components', 'dataconnect',
  'digital-evaluation', 'node_modules', 'questions-module', 'scripts',
  'src', 'utils', 'scratch'
]);

function walk(dir) {
    let results = [];
    const list = fs.readdirSync(dir);
    list.forEach(function(file) {
        if (SKIPPED_DIRS.has(file)) return;
        const filePath = path.join(dir, file);
        const stat = fs.statSync(filePath);
        if (stat && stat.isDirectory()) {
            results = results.concat(walk(filePath));
        } else if (file.endsWith('.html')) {
            results.push(filePath);
        }
    });
    return results;
}

const files = walk('.');
let issues = {
    missingCanonical: [],
    missingDesc: [],
    missingTitle: [],
    multipleH1: [],
    noViewport: []
};

files.forEach(f => {
    const c = fs.readFileSync(f, 'utf8');
    
    // Ignore small fragments or redirects
    if (c.includes('http-equiv="refresh"')) return;
    if (!c.includes('<html')) return; // skip partials

    if (!c.includes('<link rel="canonical"')) issues.missingCanonical.push(f);
    if (!c.match(/<meta[^>]+name=["']description["']/i)) issues.missingDesc.push(f);
    if (!c.includes('<title>')) issues.missingTitle.push(f);
    if (!c.includes('name="viewport"')) issues.noViewport.push(f);
    
    const h1s = c.match(/<h1/gi);
    if (h1s && h1s.length > 2) { 
        // >2 because language toggle uses 2
        issues.multipleH1.push(f);
    }
});

console.log(`Checked ${files.length} HTML files.`);
console.log(`Missing Canonical URLs: ${issues.missingCanonical.length} files`);
console.log(`Missing Meta Descriptions: ${issues.missingDesc.length} files`);
console.log(`Missing Title Tags: ${issues.missingTitle.length} files`);
console.log(`Missing Viewport (Mobile-Friendly): ${issues.noViewport.length} files`);
console.log(`More than 2 H1 tags (Dilutes SEO): ${issues.multipleH1.length} files`);

// Give a breakdown by directory for missing Canonical
const getTopLevelDir = (filePath) => filePath.split(path.sep)[0] || 'root';

const canonicalDirs = {};
issues.missingCanonical.forEach(f => {
    const d = getTopLevelDir(f);
    canonicalDirs[d] = (canonicalDirs[d] || 0) + 1;
});

const descDirs = {};
issues.missingDesc.forEach(f => {
    const d = getTopLevelDir(f);
    descDirs[d] = (descDirs[d] || 0) + 1;
});

console.log('\n--- Missing Canonical Breakdown ---');
console.log(canonicalDirs);
console.log('\n--- Missing Description Breakdown ---');
console.log('\n--- Missing Viewport Files (Sample) ---');
console.log(issues.noViewport.slice(0, 5));

console.log('\n--- Files with >2 H1 Tags ---');
console.log(issues.multipleH1);
