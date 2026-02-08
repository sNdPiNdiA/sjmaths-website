const fs = require('fs');
const path = require('path');

const startDir = path.join(__dirname, '../classes/class-12/ncert-exercise-practice');

// Configuration
const NEW_SCRIPTS = [
];

function getAllFiles(dirPath, arrayOfFiles) {
    const files = fs.readdirSync(dirPath);

    arrayOfFiles = arrayOfFiles || [];

    files.forEach(function (file) {
        if (fs.statSync(dirPath + "/" + file).isDirectory()) {
            arrayOfFiles = getAllFiles(dirPath + "/" + file, arrayOfFiles);
        } else {
            if (file.endsWith('.html')) {
                arrayOfFiles.push(path.join(dirPath, "/", file));
            }
        }
    });

    return arrayOfFiles;
}

function processFile(filePath) {
    let content = fs.readFileSync(filePath, 'utf8');
    let modified = false;

    // 1. Remove Embedded CSS (Teal & Slate Theme)
    // Matches <style> ... /* COLOR THEME: TEAL & SLATE (Class 12) */ ... </style>
    const styleRegex = /<style>[\s\S]*?COLOR THEME: TEAL & SLATE[\s\S]*?<\/style>/i;

    if (styleRegex.test(content)) {
        content = content.replace(styleRegex, '');
        console.log(`[CSS REMOVED] ${path.basename(filePath)}`);
        modified = true;
    }

    // 2. Ensure Scripts are present
    const hasHeaderScript = content.includes('exercise-header.js');
    const hasFooterScript = content.includes('exercise-footer.js');

    if (!hasHeaderScript || !hasFooterScript) {
        // Find closing body tag
        const closingBody = '
    <script src="../../../../assets/js/exercise-seo.js"></script>
    <script src="../../../../assets/js/main.min.js" defer></script>
    <script src="../../../../assets/js/exercise.js"></script>
    <script src="../../../../assets/js/exercise-header.js"></script>
    <script src="../../../../assets/js/exercise-footer.js"></script>
</body>';
        if (content.includes(closingBody)) {
            const scriptsToAdd = [];
            if (!hasHeaderScript) scriptsToAdd.push(NEW_SCRIPTS[0]);
            if (!hasFooterScript) scriptsToAdd.push(NEW_SCRIPTS[1]);

            content = content.replace(closingBody, `${scriptsToAdd.join('\n')}\n${closingBody}`);
            console.log(`[SCRIPTS ADDED] ${path.basename(filePath)}`);
            modified = true;
        }
    }

    if (modified) {
        fs.writeFileSync(filePath, content, 'utf8');
    }
}

// Main Execution
console.log('Starting Class 12 Cleanup...');
if (fs.existsSync(startDir)) {
    const files = getAllFiles(startDir);
    let processedCount = 0;

    files.forEach(file => {
        processFile(file);
        processedCount++;
    });

    console.log(`Cleanup complete. Processed ${processedCount} files.`);
} else {
    console.error(`Directory not found: ${startDir}`);
}
