const fs = require('fs');
const path = require('path');

const rootDir = '.';

function findFiles(dir, extension) {
    let files = [];
    const items = fs.readdirSync(dir);
    for (const item of items) {
        const fullPath = path.join(dir, item);
        const stat = fs.statSync(fullPath);
        if (stat.isDirectory()) {
            if (item !== 'node_modules' && item !== '.git') {
                files = files.concat(findFiles(fullPath, extension));
            }
        } else if (fullPath.endsWith(extension)) {
            files.push(fullPath);
        }
    }
    return files;
}

const htmlFiles = findFiles(rootDir, '.html');
let fixedCount = 0;

htmlFiles.forEach(file => {
    let content = fs.readFileSync(file, 'utf8');
    let changed = false;

    // Pattern 1: Any favicon.svg reference
    if (content.includes('favicon.svg')) {
        // Replace with root /favicon.png
        content = content.replace(/href=["'][^"']*favicon\.svg["']/g, 'href="/favicon.png"');
        content = content.replace(/type=["']image\/svg\+xml["']/g, 'type="image/png"');
        changed = true;
    }

    // Pattern 2: Old relative favicon.png paths that might be broken in deep subdirs
    // We'll standardization everything to /favicon.png (absolute path from domain root)
    // This assumes the site is hosted at root.

    // Fix broken relative paths specifically mentioned in report (e.g. "../assets/favicon.svg")
    // The global regex above likely caught them, but let's be sure about the image type

    if (changed) {
        fs.writeFileSync(file, content, 'utf8');
        console.log(`Fixed: ${file}`);
        fixedCount++;
    }
});

console.log(`Total files fixed: ${fixedCount}`);
