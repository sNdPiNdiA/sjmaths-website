const fs = require('fs');
const path = require('path');

const baseDir = 'c:/Users/sande/Documents/GitHub/sjmaths-website/ssc-cgl/reasoning';
const htmlFiles = [];

function getFiles(dir) {
    const files = fs.readdirSync(dir);
    for (const f of files) {
        const fullPath = path.join(dir, f);
        if (fs.statSync(fullPath).isDirectory()) {
            getFiles(fullPath);
        } else if (f === 'index.html') {
            htmlFiles.push(fullPath);
        }
    }
}
getFiles(baseDir);

let fixedCount = 0;
htmlFiles.forEach(file => {
    let content = fs.readFileSync(file, 'utf8');
    // Remove redundant <svg...><text...>...</text></svg> inside questions
    const regex = /<svg[^>]*>\s*<text[^>]*>[^<]*<\/text>\s*<\/svg>/gi;
    if (regex.test(content)) {
        content = content.replace(regex, '');
        fs.writeFileSync(file, content, 'utf8');
        fixedCount++;
        console.log('Cleaned redundant text SVG from:', file);
    }
});

console.log('Total files cleaned:', fixedCount);
