const fs = require('fs');
const path = require('path');

const quantDir = 'c:/Users/sande/Documents/GitHub/sjmaths-website/ssc-cgl/quantitative-aptitude';
let cleanedCount = 0;

function cleanDir(dir) {
    const list = fs.readdirSync(dir);
    list.forEach(file => {
        const fullPath = path.join(dir, file);
        const stat = fs.statSync(fullPath);
        if (stat.isDirectory()) {
            const indexFile = path.join(fullPath, 'index.html');
            if (fs.existsSync(indexFile)) {
                let content = fs.readFileSync(indexFile, 'utf8');
                const orig = content;

                content = content.replace(/<div class="meta-info">[\s\S]*?<\/div>/gi, '');
                content = content.replace(/<p>\s*<strong>Author:[\s\S]*?<\/p>/gi, '');
                content = content.replace(/<p>\s*<strong>Target Exam:[\s\S]*?<\/p>/gi, '');
                content = content.replace(/<p>\s*<strong>Target Audience:[\s\S]*?<\/p>/gi, '');
                content = content.replace(/<p>\s*<strong>Estimated Reading Time:[\s\S]*?<\/p>/gi, '');

                if (content !== orig) {
                    fs.writeFileSync(indexFile, content, 'utf8');
                    cleanedCount++;
                }
            }
            cleanDir(fullPath);
        }
    });
}

cleanDir(quantDir);
console.log('✅ Cleaned meta-info from total files:', cleanedCount);
