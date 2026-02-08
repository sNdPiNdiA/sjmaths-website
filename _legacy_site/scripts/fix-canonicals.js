const fs = require('fs');
const path = require('path');

const rootDir = '.';
const DOMAIN = 'https://www.sjmaths.com';

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

function generateExpectedCanonical(filePath) {
    // Normalize path separators to forward slash
    let relativePath = filePath.replace(/\\/g, '/');
    if (relativePath.startsWith('./')) relativePath = relativePath.substring(2);

    // Handle root index.html
    if (relativePath === 'index.html') return `${DOMAIN}/`;

    // Handle directory indexes
    if (relativePath.endsWith('/index.html')) {
        return `${DOMAIN}/${relativePath.replace('index.html', '')}`;
    }

    return `${DOMAIN}/${relativePath}`;
}

const htmlFiles = findFiles(rootDir, '.html');
let fixedCount = 0;

htmlFiles.forEach(file => {
    let content = fs.readFileSync(file, 'utf8');

    if (content.includes('<link rel="canonical"')) {
        const correctUrl = generateExpectedCanonical(file);
        const newTag = `<link rel="canonical" href="${correctUrl}">`;

        // Regex replace existing tag
        const newContent = content.replace(/<link rel="canonical" href="[^"]+">/, newTag);

        if (newContent !== content) {
            fs.writeFileSync(file, newContent, 'utf8');
            console.log(`Fixed: ${file}`);
            fixedCount++;
        }
    }
});

console.log(`Total canonicals fixed: ${fixedCount}`);
