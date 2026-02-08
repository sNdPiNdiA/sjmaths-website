/**
 * Remove floating index button from all exercise files
 */

const fs = require('fs');
const path = require('path');

const classesDir = path.join(__dirname, '..', 'classes');

function findExerciseFiles(dir, files = []) {
    const items = fs.readdirSync(dir);
    for (const item of items) {
        const fullPath = path.join(dir, item);
        const stat = fs.statSync(fullPath);
        if (stat.isDirectory()) {
            findExerciseFiles(fullPath, files);
        } else if (item.match(/^exercise-\d+-\d+\.html$/)) {
            files.push(fullPath);
        }
    }
    return files;
}

function removeFloatingIndexButton(filePath) {
    let content = fs.readFileSync(filePath, 'utf8');

    // Pattern to match the floating index button - handles various formats
    const patterns = [
        // Multi-line format
        /<a href="[^"]*" class="btn-floating-index"[^>]*>[\s\S]*?<\/a>\s*/g,
        // Single line format
        /<a [^>]*class="btn-floating-index"[^>]*>[^<]*(?:<[^>]*>[^<]*)*<\/a>\s*/g
    ];

    let modified = false;
    for (const pattern of patterns) {
        if (pattern.test(content)) {
            content = content.replace(pattern, '');
            modified = true;
        }
    }

    if (modified) {
        fs.writeFileSync(filePath, content, 'utf8');
        return true;
    }
    return false;
}

// Main execution
console.log('Finding exercise files...');
const files = findExerciseFiles(classesDir);
console.log(`Found ${files.length} exercise files.\n`);

let updatedCount = 0;
for (const file of files) {
    const relativePath = path.relative(classesDir, file);
    try {
        if (removeFloatingIndexButton(file)) {
            console.log(`✓ Removed button: ${relativePath}`);
            updatedCount++;
        } else {
            console.log(`- No button found: ${relativePath}`);
        }
    } catch (error) {
        console.error(`✗ Error: ${relativePath}: ${error.message}`);
    }
}

console.log(`\n========================================`);
console.log(`Done! Removed from ${updatedCount} of ${files.length} files.`);
