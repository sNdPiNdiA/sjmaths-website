/**
 * Verify Exercise Pages - Check if old headers/footers are removed
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

// Patterns that should NOT exist (old elements)
const oldPatterns = [
    { name: 'Breadcrumb div', regex: /<div class="breadcrumb">/i },
    { name: 'Hero section', regex: /<section class="hero">/i },
    { name: 'Page footer', regex: /<footer class="page-footer">/i },
    { name: 'Floating controls', regex: /<div class="floating-controls">/i },
    { name: 'Quick nav', regex: /<div class="quick-nav">/i },
];

// Patterns that SHOULD exist (new elements)
const newPatterns = [
    { name: 'exercise-header.js', regex: /exercise-header\.js/i },
    { name: 'exercise-footer.js', regex: /exercise-footer\.js/i },
    { name: 'data-class attribute', regex: /data-class="/i },
];

let totalFiles = 0;
let filesWithOldPatterns = [];
let filesMissingNewPatterns = [];

function checkFile(filePath) {
    const content = fs.readFileSync(filePath, 'utf8');
    const relPath = path.relative(BASE_DIR, filePath);
    totalFiles++;

    // Check for OLD patterns (should NOT exist)
    const foundOld = [];
    oldPatterns.forEach(p => {
        if (p.regex.test(content)) {
            foundOld.push(p.name);
        }
    });

    if (foundOld.length > 0) {
        filesWithOldPatterns.push({ file: relPath, patterns: foundOld });
    }

    // Check for NEW patterns (should exist)
    const missingNew = [];
    newPatterns.forEach(p => {
        if (!p.regex.test(content)) {
            missingNew.push(p.name);
        }
    });

    if (missingNew.length > 0) {
        filesMissingNewPatterns.push({ file: relPath, missing: missingNew });
    }
}

function processDirectory(dir) {
    const fullPath = path.join(BASE_DIR, dir);

    if (!fs.existsSync(fullPath)) {
        return;
    }

    const chapters = fs.readdirSync(fullPath).filter(f =>
        f.startsWith('chapter-') && fs.statSync(path.join(fullPath, f)).isDirectory()
    );

    chapters.forEach(chapter => {
        const chapterPath = path.join(fullPath, chapter);
        const files = fs.readdirSync(chapterPath).filter(f =>
            f.startsWith('exercise-') && f.endsWith('.html')
        );

        files.forEach(file => {
            checkFile(path.join(chapterPath, file));
        });
    });
}

console.log('🔍 Verifying Exercise Page Refactoring...\n');

exerciseDirs.forEach(dir => processDirectory(dir));

console.log(`📊 Total files checked: ${totalFiles}\n`);

if (filesWithOldPatterns.length === 0) {
    console.log('✅ No OLD patterns found (all removed successfully)');
} else {
    console.log(`❌ Files still containing OLD patterns: ${filesWithOldPatterns.length}`);
    filesWithOldPatterns.forEach(f => {
        console.log(`  - ${f.file}: ${f.patterns.join(', ')}`);
    });
}

console.log('');

if (filesMissingNewPatterns.length === 0) {
    console.log('✅ All files have NEW components');
} else {
    console.log(`⚠️ Files missing NEW patterns: ${filesMissingNewPatterns.length}`);
    filesMissingNewPatterns.slice(0, 10).forEach(f => {
        console.log(`  - ${f.file}: missing ${f.missing.join(', ')}`);
    });
    if (filesMissingNewPatterns.length > 10) {
        console.log(`  ... and ${filesMissingNewPatterns.length - 10} more`);
    }
}

console.log('\n========================================');
console.log('SUMMARY:');
console.log(`  Old patterns remaining: ${filesWithOldPatterns.length} files`);
console.log(`  Missing new patterns: ${filesMissingNewPatterns.length} files`);
