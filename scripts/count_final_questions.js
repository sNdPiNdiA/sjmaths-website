const fs = require('fs');
const path = require('path');

const targetDir = 'C:\\Users\\sande\\Documents\\GitHub\\sjmaths-website\\upsssc-lower-mains';
let results = {};

function scanDir(dir) {
    const files = fs.readdirSync(dir);
    for (const file of files) {
        const fullPath = path.join(dir, file);
        const stat = fs.statSync(fullPath);
        if (stat.isDirectory()) {
            scanDir(fullPath);
        } else if (file === 'index.html') {
            const content = fs.readFileSync(fullPath, 'utf8');
            const practiceTabStart = content.indexOf('<div id="tab-practice"');
            
            let count = 0;
            if (practiceTabStart !== -1) {
                const practiceTabEnd = content.indexOf('<div id="tab-pyqs"', practiceTabStart);
                if (practiceTabEnd !== -1) {
                    const practiceSection = content.substring(practiceTabStart, practiceTabEnd);
                    count = (practiceSection.match(/class="practice-question-card"/g) || []).length;
                } else {
                    const practiceSection = content.substring(practiceTabStart);
                    count = (practiceSection.match(/class="practice-question-card"/g) || []).length;
                }
            }
            
            const sizeKB = (stat.size / 1024).toFixed(2);
            
            if (!results[count]) {
                results[count] = [];
            }
            results[count].push({ path: fullPath.replace(targetDir, ''), size: sizeKB });
        }
    }
}

scanDir(targetDir);

let totalFiles = 0;
console.log('--- Summary ---');
for (const count of Object.keys(results).sort((a,b) => parseInt(a) - parseInt(b))) {
    console.log(`${results[count].length} files have exactly ${count} practice questions.`);
    totalFiles += results[count].length;
}
console.log(`\nTotal index.html files found: ${totalFiles}`);

console.log('\n--- Details ---');
for (const count of Object.keys(results).sort((a,b) => parseInt(a) - parseInt(b))) {
    console.log(`\n[ Files with ${count} questions ]:`);
    results[count].forEach(f => {
        console.log(`  - ${f.path} (${f.size} KB)`);
    });
}
