const fs = require('fs');
const path = require('path');

function walk(dir) {
    let results = [];
    const list = fs.readdirSync(dir);
    list.forEach(function(file) {
        file = path.join(dir, file);
        const stat = fs.statSync(file);
        if (stat && stat.isDirectory()) { 
            results = results.concat(walk(file));
        } else { 
            if(file.endsWith('index.html')) results.push(file);
        }
    });
    return results;
}

const files = walk('upsssc-lower-mains');
let modifiedCount = 0;

for (const file of files) {
    let content = fs.readFileSync(file, 'utf8');
    
    // Regular expression to match two adjacent summary tags and combine them into one with spans inside
    // Match <summary class="lang-en">Text</summary> <summary class="lang-hi">Text</summary>
    const regex = /<summary\s+class="lang-en">([\s\S]*?)<\/summary>\s*<summary\s+class="lang-hi">([\s\S]*?)<\/summary>/g;
    
    if (regex.test(content)) {
        content = content.replace(regex, '<summary>\n    <span class="lang-en">$1</span>\n    <span class="lang-hi">$2</span>\n</summary>');
        fs.writeFileSync(file, content, 'utf8');
        modifiedCount++;
    }
}

console.log(`Successfully fixed <summary> tags in ${modifiedCount} files.`);
