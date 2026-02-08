const fs = require('fs');
const path = require('path');

const rootDir = '.';
const viewportTag = '<meta name="viewport" content="width=device-width, initial-scale=1.0">';

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

    // Check if viewport meta exists (using the same loose regex logic as our test runner)
    // We look for name="viewport" OR viewport= to be safe
    if (!/<meta[^>]*name=["']viewport["']/i.test(content) && !/<meta[^>]*content=["'][^"']*width=device-width/i.test(content)) {
        // Insert it
        if (content.includes('<head>')) {
            // Try to insert after charset if possible
            if (content.includes('<meta charset="UTF-8">')) {
                content = content.replace('<meta charset="UTF-8">', '<meta charset="UTF-8">\n    ' + viewportTag);
            } else {
                content = content.replace('<head>', '<head>\n    ' + viewportTag);
            }

            fs.writeFileSync(file, content, 'utf8');
            console.log(`Fixed: ${file}`);
            fixedCount++;
        } else {
            console.log(`Skipped (no head): ${file}`);
        }
    }
});

console.log(`Total files fixed: ${fixedCount}`);
