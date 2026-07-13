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
let fixedCanonical = 0;
let fixedViewport = 0;
let fixedH1 = 0;

files.forEach(f => {
    let c = fs.readFileSync(f, 'utf8');
    let changed = false;

    if (c.includes('http-equiv="refresh"')) return;
    if (!c.includes('<html')) return;

    // 1. Missing Viewport
    if (!c.includes('name="viewport"')) {
        c = c.replace('<head>', '<head>\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">');
        changed = true;
        fixedViewport++;
    }

    // 2. Missing Canonical
    if (!c.includes('<link rel="canonical"')) {
        let urlPath = f.replace(/\\/g, '/');
        if (urlPath.endsWith('index.html')) {
            urlPath = urlPath.replace('index.html', '');
        }
        const canonical = `https://sjmaths.com/${urlPath}`;
        
        // Handle if <title> is missing (it's not based on earlier check, but just in case)
        if (c.includes('</title>')) {
             c = c.replace('</title>', `</title>\n    <link rel="canonical" href="${canonical}">`);
        } else {
             c = c.replace('<head>', `<head>\n    <link rel="canonical" href="${canonical}">`);
        }
        changed = true;
        fixedCanonical++;
    }

    // 3. > 2 H1 tags
    const h1s = c.match(/<h1/gi);
    if (h1s && h1s.length > 2) {
        let matchCount = 0;
        // Replace all H1s after the first 2 with H2s
        c = c.replace(/<h1(.*?)>(.*?)<\/h1>/gi, (match, p1, p2) => {
            matchCount++;
            if (matchCount > 2) {
                return `<h2${p1}>${p2}</h2>`;
            }
            return match;
        });
        changed = true;
        fixedH1++;
    }

    if (changed) {
        fs.writeFileSync(f, c, 'utf8');
    }
});

console.log(`Fixed Viewport: ${fixedViewport}`);
console.log(`Fixed Canonical: ${fixedCanonical}`);
console.log(`Fixed >2 H1s: ${fixedH1}`);
