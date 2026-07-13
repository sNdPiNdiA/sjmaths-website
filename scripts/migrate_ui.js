const fs = require('fs');
const path = require('path');

function walk(dir) {
    let results = [];
    const list = fs.readdirSync(dir);
    list.forEach(function(file) {
        file = path.join(dir, file);
        const stat = fs.statSync(file);
        if (stat && stat.isDirectory()) {
            // skip polity folder since it's already using the new structure
            if (!file.includes('polity')) {
                results = results.concat(walk(file));
            }
        } else {
            if(file.endsWith('index.html')) results.push(file);
        }
    });
    return results;
}

const dirsToProcess = ['upsssc-lower-mains'];
let files = walk('upsssc-lower-mains');

let modifiedCount = 0;

for (const file of files) {
    let content = fs.readFileSync(file, 'utf8');
    let originalContent = content;

    // 1. Remove old CSS
    content = content.replace(/<link rel="stylesheet" href="\/assets\/css\/layout\.min\.css[^>]*>\s*/g, '');
    content = content.replace(/<link rel="stylesheet" href="\/assets\/css\/component\.min\.css[^>]*>\s*/g, '');
    content = content.replace(/<link rel="stylesheet" href="\/assets\/css\/pages\.min\.css[^>]*>\s*/g, '');

    // Add topic-details.min.css if missing
    if (!content.includes('topic-details.min.css')) {
        content = content.replace(/(<link rel="stylesheet" href="\/assets\/css\/upsssc-lower\.min\.css)/, '<link rel="stylesheet" href="/assets/css/topic-details.min.css">\n    $1');
    }

    // 2. Update Breadcrumbs (Move top-controls if needed, but for now just fix classes)
    content = content.replace(/<div class="breadcrumb(?:s)?">\s*([\s\S]*?)\s*<\/div>/g, '<div class="breadcrumbs">\n            <div class="breadcrumbs-path">\n                $1\n            </div>\n        </div>');
    
    // Fix lang-toggle-btn
    if (content.includes('<button class="lang-toggle-btn"')) {
        content = content.replace(/<button class="lang-toggle-btn"[^>]*>A\/अ<\/button>/, '');
        content = content.replace(/<div class="page-container">/g, '<div class="container">\n        <div class="top-controls">\n            <button class="lang-toggle-btn" onclick="toggleLang()">A/अ</button>\n        </div>');
    }

    // 3. Update Header
    content = content.replace(/<div class="(?:page|topic)-header">/g, '<div class="topic-header">');
    content = content.replace(/<h1 class="page-title">/g, '<h1>');
    content = content.replace(/<p class="page-subtitle">/g, '<p>');

    // 4. Update Navigation
    content = content.replace(/<div class="(?:sub|subject)-nav">/g, '<div class="subject-nav">');

    if (content !== originalContent) {
        fs.writeFileSync(file, content, 'utf8');
        modifiedCount++;
    }
}

console.log(`Successfully migrated ${modifiedCount} files to the polity UI structure.`);
