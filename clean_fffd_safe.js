const fs = require('fs');

const sscCglDir = 'c:/Users/sande/Documents/GitHub/sjmaths-website/ssc-cgl';

function cleanFFFD(filePath) {
    let content = fs.readFileSync(filePath, 'utf8');
    if (!content.includes('\uFFFD')) return false;

    // Safely remove FFFD replacement characters without inserting extra words
    content = content.replace(/\uFFFD+/g, '');
    fs.writeFileSync(filePath, content, 'utf8');
    return true;
}

function walk(dir) {
    let count = 0;
    const list = fs.readdirSync(dir);
    list.forEach(file => {
        const fullPath = dir + '/' + file;
        const stat = fs.statSync(fullPath);
        if (stat && stat.isDirectory()) {
            count += walk(fullPath);
        } else if (file === 'index.html') {
            if (cleanFFFD(fullPath)) count++;
        }
    });
    return count;
}

const cleaned = walk(sscCglDir);
console.log('Cleaned U+FFFD characters safely from ' + cleaned + ' HTML files.');
