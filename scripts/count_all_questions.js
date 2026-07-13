const fs = require('fs');
const path = require('path');

const targetDir = 'C:\\Users\\sande\\Documents\\GitHub\\sjmaths-website\\upsssc-lower-mains';
let fileBreakdown = [];

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
            const pyqsTabStart = content.indexOf('<div id="tab-pyqs"');
            
            let practiceCount = 0;
            let pyqsCount = 0;

            if (practiceTabStart !== -1) {
                const end = pyqsTabStart !== -1 ? pyqsTabStart : content.length;
                let practiceSection = content.substring(practiceTabStart, end);
                practiceCount = (practiceSection.match(/class="practice-question-card/g) || []).length;
            }

            if (pyqsTabStart !== -1) {
                let pyqsSection = content.substring(pyqsTabStart);
                pyqsCount = (pyqsSection.match(/class="practice-question-card/g) || []).length;
            }
            
            const totalCount = practiceCount + pyqsCount;
            
            fileBreakdown.push({
                path: fullPath.replace(targetDir, ''),
                practice: practiceCount,
                pyqs: pyqsCount,
                total: totalCount
            });
        }
    }
}

scanDir(targetDir);

// Sort by total questions descending
fileBreakdown.sort((a,b) => b.total - a.total);

let totalPractice = 0;
let totalPyqs = 0;
let totalAll = 0;

fileBreakdown.forEach(f => {
    totalPractice += f.practice;
    totalPyqs += f.pyqs;
    totalAll += f.total;
});

// Write strictly to stdout
console.log('=== OVERALL DATABASE STATISTICS ===');
console.log(`Total Test (Practice) Questions: ${totalPractice}`);
console.log(`Total PYQs:                      ${totalPyqs}`);
console.log(`GRAND TOTAL QUESTIONS:           ${totalAll}`);
console.log(`Total HTML files scanned:        ${fileBreakdown.length}`);
console.log('\n===================================\n');

console.log('=== DETAILED BREAKDOWN BY FILE ===');
fileBreakdown.forEach(f => {
    console.log(`[Total: ${String(f.total).padStart(2, ' ')}] (Practice: ${String(f.practice).padStart(2, ' ')} | PYQs: ${String(f.pyqs).padStart(2, ' ')}) -> ${f.path}`);
});
