const fs = require('fs');
const path = require('path');

function processDir(dir) {
    if (!fs.existsSync(dir)) return;
    const files = fs.readdirSync(dir);
    for (const file of files) {
        const fullPath = path.join(dir, file);
        if (fs.statSync(fullPath).isDirectory()) {
            processDir(fullPath);
        } else if (file === 'index.html') {
            let content = fs.readFileSync(fullPath, 'utf8');
            if (content.includes("}, undefined, 'en');")) {
                content = content.replace(/}, undefined, 'en'\);/g, "}, 'prehistory-mindmap-container', 'en');");
                fs.writeFileSync(fullPath, content, 'utf8');
                console.log('Fixed', fullPath);
            } else if (content.includes("} }, undefined, 'en');")) {
                content = content.replace(/} }, undefined, 'en'\);/g, "} }, 'prehistory-mindmap-container', 'en');");
                fs.writeFileSync(fullPath, content, 'utf8');
                console.log('Fixed', fullPath);
            } else if (content.includes("]}, undefined, 'en');")) {
                content = content.replace(/]}, undefined, 'en'\);/g, "]}, 'prehistory-mindmap-container', 'en');");
                fs.writeFileSync(fullPath, content, 'utf8');
                console.log('Fixed', fullPath);
            }
        }
    }
}

// More robust regex approach
function processDirRegex(dir) {
    if (!fs.existsSync(dir)) return;
    const files = fs.readdirSync(dir);
    let count = 0;
    for (const file of files) {
        const fullPath = path.join(dir, file);
        if (fs.statSync(fullPath).isDirectory()) {
            count += processDirRegex(fullPath);
        } else if (file === 'index.html') {
            let content = fs.readFileSync(fullPath, 'utf8');
            let originalContent = content;
            
            // Look for renderMindmap(..., undefined, 'en');
            content = content.replace(/,\s*undefined\s*,\s*'en'\s*\)/g, ", 'prehistory-mindmap-container', 'en')");
            content = content.replace(/,\s*undefined\s*,\s*'hi'\s*\)/g, ", 'prehistory-mindmap-container-hi', 'hi')");
            
            if (content !== originalContent) {
                fs.writeFileSync(fullPath, content, 'utf8');
                console.log('Fixed undefined mindmap container in', fullPath);
                count++;
            }
        }
    }
    return count;
}

const totalFixed = processDirRegex('upsc');
console.log('Total files fixed:', totalFixed);
