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
            const pyqsTabStart = content.indexOf('<div id="tab-pyqs"');
            
            let pyqsCount = 0;
            if (pyqsTabStart !== -1) {
                let pyqsSection = content.substring(pyqsTabStart);
                pyqsCount = (pyqsSection.match(/class="practice-question-card/g) || []).length;
            }
            
            if (!results[pyqsCount]) {
                results[pyqsCount] = [];
            }
            results[pyqsCount].push(fullPath.replace(targetDir, ''));
        }
    }
}

scanDir(targetDir);

console.log('=== PYQ COUNT SUMMARY ===');
let totalPyqs = 0;
for (const count of Object.keys(results).sort((a,b) => parseInt(b) - parseInt(a))) {
    console.log(`${String(results[count].length).padStart(3, ' ')} files have exactly ${count} PYQs.`);
    totalPyqs += parseInt(count) * results[count].length;
}
console.log(`\nGrand Total PYQs: ${totalPyqs}`);

let targetFiles = [];
for (const count of Object.keys(results).sort((a,b) => parseInt(b) - parseInt(a))) {
    if (parseInt(count) <= 1) {
        results[count].forEach(p => {
            if (!p.includes('_template')) { // Ignore the template file
                targetFiles.push({ file: path.join(targetDir, p), count: parseInt(count) });
            }
        });
    }
}
fs.writeFileSync('C:\\\\Users\\\\sande\\\\.gemini\\\\antigravity-ide\\\\brain\\\\21b8a75e-f11a-42b8-a02e-46e7af3ba25e\\\\scratch\\\\target_pyqs_files.json', JSON.stringify(targetFiles, null, 2));
console.log(`Saved ${targetFiles.length} files to target_pyqs_files.json`);
