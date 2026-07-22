const fs = require('fs');
const path = require('path');

const baseDir = 'c:/Users/sande/Documents/GitHub/sjmaths-website/ssc-cgl/reasoning';

function cleanFile(filePath) {
    let content = fs.readFileSync(filePath, 'utf8');
    const orig = content;

    // Remove any trailing slash and 2nd language text in MCQ options
    content = content.replace(/(<span class="lang-en">\([A-D]\)\s*[^<\n\/]+?)\s*\/[^\n<]+/g, '$1');
    content = content.replace(/(<span class="lang-hi">\([A-D]\)\s*[^<\n\/]+?)\s*\/[^\n<]+/g, '$1');
    content = content.replace(/<\/span><\/span>/g, '</span>');

    if (content !== orig) {
        fs.writeFileSync(filePath, content, 'utf8');
        console.log('✅ Cleaned options in:', filePath);
    }
}

function scan(dir) {
    if (!fs.existsSync(dir)) return;
    const list = fs.readdirSync(dir);
    list.forEach(file => {
        const full = path.join(dir, file);
        if (fs.statSync(full).isDirectory()) {
            scan(full);
        } else if (file === 'index.html') {
            cleanFile(full);
        }
    });
}

scan(baseDir);
console.log('🎉 Finished cleaning existing Reasoning index.html files');
