const fs = require('fs');
const path = require('path');

const sscCglDir = 'c:/Users/sande/Documents/GitHub/sjmaths-website/ssc-cgl';

function getHtmlFiles(dir) {
    let results = [];
    const list = fs.readdirSync(dir);
    list.forEach(file => {
        const fullPath = path.join(dir, file);
        const stat = fs.statSync(fullPath);
        if (stat && stat.isDirectory()) {
            results = results.concat(getHtmlFiles(fullPath));
        } else if (file === 'index.html') {
            results.push(fullPath);
        }
    });
    return results;
}

const htmlFiles = getHtmlFiles(sscCglDir);
console.log('Total index.html files under ssc-cgl:', htmlFiles.length);

let modifiedCount = 0;
htmlFiles.forEach(file => {
    let content = fs.readFileSync(file, 'utf8');
    
    const navRegex = /<!-- Subject Navigation Menu -->\s*<nav class="subject-nav"[\s\S]*?<\/nav>/gi;
    const navRegex2 = /<nav class="subject-nav"[\s\S]*?<\/nav>/gi;
    
    if (navRegex.test(content) || navRegex2.test(content)) {
        content = content.replace(navRegex, '').replace(navRegex2, '');
        fs.writeFileSync(file, content, 'utf8');
        modifiedCount++;
    }
});

console.log('✅ Removed subject-nav pill bar from ' + modifiedCount + ' files.');
