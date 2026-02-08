const fs = require('fs');
const path = require('path');

// Configuration
const CLASSES_DIR = path.join(__dirname, '../classes');
const CSS_PATH = '/assets/css/exercise.css';

// HTML Snippet for the Floating Button (Class 9 specific)
const FLOATING_BTN_HTML = `        <a href="/classes/class-9/index.html" class="btn-floating-index" title="Class 9 Index">
            <i class="fas fa-th-large"></i> <span>Class 9 Index</span>
        </a>`;

// Main function
function processDirectory(directory) {
    const files = fs.readdirSync(directory);

    files.forEach(file => {
        const fullPath = path.join(directory, file);
        const stat = fs.statSync(fullPath);

        if (stat.isDirectory()) {
            processDirectory(fullPath);
        } else if (file.endsWith('.html') && file.includes('exercise')) {
            updateExercisePage(fullPath);
        }
    });
}

function updateExercisePage(filePath) {
    let content = fs.readFileSync(filePath, 'utf8');
    let modified = false;

    // 1. Remove Inline Styles (The specific block added recently)
    // Matches <style> tags containing root variables or specific classes we added
    const styleRegex = /<style>[\s\S]*?(:root|btn-floating-index)[\s\S]*?<\/style>/gi;
    if (styleRegex.test(content)) {
        content = content.replace(styleRegex, '');
        modified = true;
    }

    // 2. Ensure exercise.css is linked
    if (!content.includes('assets/css/exercise.css')) {
        content = content.replace('</head>', `    <link rel="stylesheet" href="${CSS_PATH}">\n</head>`);
        modified = true;
    }

    // 3. Add Floating Button (Only for Class 9 pages if missing)
    if (filePath.includes('class-9') && !content.includes('btn-floating-index')) {
        // Insert before </main>
        if (content.includes('</main>')) {
            content = content.replace('</main>', `\n${FLOATING_BTN_HTML}\n    </main>`);
            modified = true;
        }
    }

    if (modified) {
        fs.writeFileSync(filePath, content, 'utf8');
        console.log(`✅ Updated: ${path.relative(process.cwd(), filePath)}`);
    }
}

console.log('🚀 Starting Exercise Page Update...');
processDirectory(CLASSES_DIR);
console.log('✨ Update Complete!');