const fs = require('fs');
const path = require('path');

function processDirRegex(dir) {
    if (!fs.existsSync(dir)) return 0;
    const files = fs.readdirSync(dir);
    let count = 0;
    for (const file of files) {
        if (file === '.git' || file === 'node_modules' || file === 'scripts' || file === 'assets') continue;
        const fullPath = path.join(dir, file);
        if (fs.statSync(fullPath).isDirectory()) {
            count += processDirRegex(fullPath);
        } else if (file === 'index.html' || file.endsWith('.html')) {
            let content = fs.readFileSync(fullPath, 'utf8');
            let originalContent = content;
            
            // Bump the cache buster string
            content = content.replace(/global-header\.min\.js\?v=4d1d595f/g, "global-header.min.js?v=4d1d595g");
            
            if (content !== originalContent) {
                fs.writeFileSync(fullPath, content, 'utf8');
                count++;
            }
        }
    }
    return count;
}

const totalFixed = processDirRegex('.');
console.log('Total files cache-busted (global):', totalFixed);
