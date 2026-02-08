/**
 * Refactor Exercise Pages
 * Removes old headers/footers and adds new component scripts
 */
const fs = require('fs');
const path = require('path');

const BASE_DIR = path.join(__dirname, '..');

// All class exercise directories
const exerciseDirs = [
    'classes/class-9/ncert-exercise-practice',
    'classes/class-10/ncert-exercise-practice',
    'classes/class-11/ncert-exercise-practice',
    'classes/class-12/ncert-exercise-practice'
];

let updated = 0;
let skipped = 0;
let errors = [];

function processFile(filePath) {
    try {
        let content = fs.readFileSync(filePath, 'utf8');
        const originalContent = content;

        // Skip if already has exercise-header.js
        if (content.includes('exercise-header.js')) {
            console.log(`⏭ Skipped (already updated): ${filePath}`);
            skipped++;
            return;
        }

        // === REMOVALS ===

        // 1. Remove breadcrumb div (Class 9 style)
        content = content.replace(/<div class="breadcrumb">[\s\S]*?<\/div>\s*/gi, '');

        // 2. Remove hero section (Class 10 style)
        content = content.replace(/<section class="hero">[\s\S]*?<\/section>\s*/gi, '');

        // 3. Remove quick-nav section
        content = content.replace(/<div class="quick-nav">[\s\S]*?<\/div>\s*/gi, '');
        content = content.replace(/<nav class="quick-nav">[\s\S]*?<\/nav>\s*/gi, '');

        // 4. Remove old footer (page-footer class)
        content = content.replace(/<footer class="page-footer">[\s\S]*?<\/footer>\s*/gi, '');

        // 5. Remove floating controls div (Class 10 has this)
        content = content.replace(/<div class="floating-controls">[\s\S]*?<\/div>\s*/gi, '');

        // 6. Remove inline toggleTheme function (we'll use the header one)
        content = content.replace(/<!-- Redundant inline script purged by standardizer -->\n`;
                }
            }
            return match;
        });

        // === ADDITIONS ===

        // Add exercise-header.js and exercise-footer.js before </body>

        if (content.includes('</body>') && !content.includes('exercise-header.js')) {
            content = content.replace('</body>', `${newScripts}\n
    <script src="../../../../assets/js/exercise-seo.js"></script>
    <script src="../../../../assets/js/main.min.js" defer></script>
    <script src="../../../../assets/js/exercise.js"></script>
    <script src="../../../../assets/js/exercise-header.js"></script>
    <script src="../../../../assets/js/exercise-footer.js"></script>
</body>`);
        }

        // Only write if content changed
        if (content !== originalContent) {
            fs.writeFileSync(filePath, content, 'utf8');
            console.log(`✅ Updated: ${filePath}`);
            updated++;
        } else {
            console.log(`⏭ No changes needed: ${filePath}`);
            skipped++;
        }

    } catch (err) {
        console.log(`❌ Error: ${filePath} - ${err.message}`);
        errors.push({ file: filePath, error: err.message });
    }
}

function processDirectory(dir) {
    const fullPath = path.join(BASE_DIR, dir);

    if (!fs.existsSync(fullPath)) {
        console.log(`⚠ Directory not found: ${dir}`);
        return;
    }

    console.log(`\n📁 Processing: ${dir}`);

    // Get all chapter folders
    const chapters = fs.readdirSync(fullPath).filter(f =>
        f.startsWith('chapter-') && fs.statSync(path.join(fullPath, f)).isDirectory()
    );

    chapters.forEach(chapter => {
        const chapterPath = path.join(fullPath, chapter);
        const files = fs.readdirSync(chapterPath).filter(f =>
            f.startsWith('exercise-') && f.endsWith('.html')
        );

        files.forEach(file => {
            processFile(path.join(chapterPath, file));
        });
    });
}

console.log('🚀 Starting Exercise Page Refactoring...\n');

exerciseDirs.forEach(dir => processDirectory(dir));

console.log('\n========================================');
console.log(`✅ Updated: ${updated} files`);
console.log(`⏭ Skipped: ${skipped} files`);
console.log(`❌ Errors: ${errors.length} files`);

if (errors.length > 0) {
    console.log('\nErrors:');
    errors.forEach(e => console.log(`  - ${e.file}: ${e.error}`));
}
