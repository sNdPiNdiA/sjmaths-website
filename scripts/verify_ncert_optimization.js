const fs = require('fs');
const path = require('path');

const TARGET_DIRS = [
    path.join(__dirname, '../classes/class-9/ncert-exercise-practice'),
    path.join(__dirname, '../classes/class-10/ncert-exercise-practice'),
    path.join(__dirname, '../classes/class-11/ncert-exercise-practice'),
    path.join(__dirname, '../classes/class-12/ncert-exercise-practice')
];

function getAllFiles(dirPath, arrayOfFiles) {
    if (!fs.existsSync(dirPath)) return arrayOfFiles || [];

    const files = fs.readdirSync(dirPath);
    arrayOfFiles = arrayOfFiles || [];

    files.forEach(function (file) {
        if (fs.statSync(path.join(dirPath, file)).isDirectory()) {
            arrayOfFiles = getAllFiles(path.join(dirPath, file), arrayOfFiles);
        } else {
            if (file.endsWith(".html")) {
                arrayOfFiles.push(path.join(dirPath, file));
            }
        }
    });

    return arrayOfFiles;
}

let totalFiles = 0;
let issues = [];

TARGET_DIRS.forEach(dir => {
    if (fs.existsSync(dir)) {
        const files = getAllFiles(dir);
        totalFiles += files.length;

        files.forEach(file => {
            const content = fs.readFileSync(file, 'utf8');
            const relativePath = path.relative(path.join(__dirname, '..'), file);

            // Checks
            const hasMathJax = content.includes('MathJax') || content.includes('mathjax');
            const hasFontAwesomeCDN = content.includes('font-awesome') && content.includes('stylesheet');
            // Note: We might keep FA for some icons not yet optimized, but we expect the MAIN CDN to be removed or specific icons replaced.
            // Let's check for the specific replacements we targeted.

            const hasKaTeX = content.includes('katex.min.css');

            // Check for un-replaced icons (if any remnants)
            // The optimization script targeted specific icons. 
            // Let's check if the file uses any of the optimized classes but still as <i> tags
            const hasOldIcons = /<i class="fas fa-(clock|eye|arrow-right|arrow-left|book|th-large)"><\/i>/.test(content);

            if (hasMathJax) {
                issues.push(`[MathJax Found] ${relativePath}`);
            }
            if (!hasKaTeX && (content.includes('$') || content.includes('\\('))) {
                // Only flag missing KaTeX if there looks like math content
                issues.push(`[KaTeX Missing] ${relativePath}`);
            }
            if (hasOldIcons) {
                issues.push(`[Old Icons Found] ${relativePath}`);
            }
        });
    }
});

console.log(`Scanned ${totalFiles} files.`);
if (issues.length === 0) {
    console.log("✅ All files verify clean! No MathJax, KaTeX is present, and target icons are optimized.");
} else {
    console.log(`❌ Found ${issues.length} issues:`);
    issues.forEach(issue => console.log(issue));
}
