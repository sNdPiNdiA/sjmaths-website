const fs = require('fs');
const path = require('path');

function processDirRegex(dir) {
    if (!fs.existsSync(dir)) return 0;
    const files = fs.readdirSync(dir);
    let count = 0;
    for (const file of files) {
        const fullPath = path.join(dir, file);
        if (fs.statSync(fullPath).isDirectory()) {
            count += processDirRegex(fullPath);
        } else if (file === 'index.html') {
            let content = fs.readFileSync(fullPath, 'utf8');
            let originalContent = content;
            
            // Bump the cache buster string
            content = content.replace(/mindmap-engine\.min\.js\?v=ea088f0e/g, "mindmap-engine.min.js?v=ea088f0f");
            
            if (content !== originalContent) {
                fs.writeFileSync(fullPath, content, 'utf8');
                count++;
            }
        }
    }
    return count;
}

const totalFixed = processDirRegex('upsc');
console.log('Total files cache-busted:', totalFixed);
