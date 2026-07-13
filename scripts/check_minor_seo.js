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
    missingAlt: 0,
    emptyTitle: 0,
    emptyDesc: 0,
    underscoreUrls: new Set()
};

files.forEach(f => {
    const c = fs.readFileSync(f, 'utf8');
    
    if (c.includes('http-equiv="refresh"')) return;
    if (!c.includes('<html')) return;

    // 1. Missing Alt Tags on Images
    const imgs = c.match(/<img[^>]+>/gi);
    if (imgs) {
        imgs.forEach(img => {
            if (!img.includes('alt=')) issues.missingAlt++;
        });
    }

    // 2. Empty Title
    if (c.includes('<title></title>') || c.match(/<title>\s+<\/title>/i)) {
        issues.emptyTitle++;
    }

    // 3. Empty Meta Description
    const descMatch = c.match(/<meta[^>]+name=["']description["'][^>]+content=["'](.*?)["']/i);
    if (descMatch && descMatch[1].trim() === '') {
        issues.emptyDesc++;
    }

    // 4. Underscores in URLs (SEO prefers hyphens)
    // We check the directory path of the file
    if (f.includes('_')) {
        issues.underscoreUrls.add(f);
    }
});

console.log(`Checked ${files.length} HTML files for minor SEO issues.`);
console.log(`Images missing 'alt' attribute: ${issues.missingAlt}`);
console.log(`Files with empty <title>: ${issues.emptyTitle}`);
console.log(`Files with empty description: ${issues.emptyDesc}`);
console.log(`Files/folders with underscores (_) instead of hyphens (-): ${issues.underscoreUrls.size}`);
