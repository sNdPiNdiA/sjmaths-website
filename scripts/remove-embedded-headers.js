/**
 * Remove Embedded Headers and Footers from Exercise Files
 * Second pass to clean up files with embedded header/footer HTML
 */
const fs = require('fs');
const path = require('path');

const BASE_DIR = path.join(__dirname, '..');

const exerciseDirs = [
    'classes/class-9/ncert-exercise-practice',
    'classes/class-10/ncert-exercise-practice',
    'classes/class-11/ncert-exercise-practice',
    'classes/class-12/ncert-exercise-practice'
];

let updated = 0;
let skipped = 0;

function processFile(filePath) {
    try {
        let content = fs.readFileSync(filePath, 'utf8');
        const originalContent = content;

        // Remove <!-- Header removed by standardizer --> tags (non-greedy)
        content = content.replace(/<header[^>]*>[\s\S]*?<\/header>\s*/gi, '');

        // Remove <footer>...</footer> tags (the embedded ones, not page-footer)
        content = content.replace(/<footer[^>]*>[\s\S]*?<\/footer>\s*/gi, '');

        // Remove breadcrumb div
        content = content.replace(/<div class="breadcrumb"[^>]*>[\s\S]*?<\/div>\s*/gi, '');

        // Remove header CSS from <style> blocks (/* --- HEADER --- */ style blocks)
        content = content.replace(/\/\*\s*---\s*HEADER\s*---\s*\*\/[\s\S]*?(?=\/\*\s*---|<\/style>)/gi, '');

        // Remove footer CSS from <style> blocks (/* --- FOOTER --- */ style blocks)  
        content = content.replace(/\/\*\s*---\s*FOOTER\s*---\s*\*\/[\s\S]*?(?=\/\*\s*---|<\/style>)/gi, '');

        // Remove breadcrumb CSS
        content = content.replace(/\/\*\s*---\s*BREADCRUMB\s*---\s*\*\/[\s\S]*?(?=\/\*\s*---|<\/style>)/gi, '');

        // Only write if content changed
        if (content !== originalContent) {
            fs.writeFileSync(filePath, content, 'utf8');
            console.log(`✅ Cleaned: ${path.relative(BASE_DIR, filePath)}`);
            updated++;
        } else {
            skipped++;
        }

    } catch (err) {
        console.log(`❌ Error: ${filePath} - ${err.message}`);
    }
}

function processDirectory(dir) {
    const fullPath = path.join(BASE_DIR, dir);

    if (!fs.existsSync(fullPath)) return;

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

console.log('🧹 Removing embedded headers/footers...\n');

exerciseDirs.forEach(dir => processDirectory(dir));

console.log('\n========================================');
console.log(`✅ Cleaned: ${updated} files`);
console.log(`⏭ No changes: ${skipped} files`);
