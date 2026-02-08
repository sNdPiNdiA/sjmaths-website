/**
 * Batch update script for exercise HTML files
 * Updates:
 * 1. Adds meta description if missing
 * 2. Fixes breadcrumb schema typo ("Exercise X Y.html" -> "Exercise X.Y")
 * 3. Adds datePublished and dateModified to Article schema
 * 4. Removes timer-box elements
 */

const fs = require('fs');
const path = require('path');

const classesDir = path.join(__dirname, '..', 'classes');
const TODAY = '2026-02-05';

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

function extractMetaFromPath(filePath) {
    // Extract class number, chapter name, and exercise number from path
    const match = filePath.match(/class-(\d+).*?chapter-\d+-([^\\\/]+).*?exercise-(\d+)-(\d+)/i);
    if (match) {
        return {
            classNum: match[1],
            chapterName: match[2].split('-').map(w => w.charAt(0).toUpperCase() + w.slice(1)).join(' '),
            exerciseNum: `${match[3]}.${match[4]}`
        };
    }
    return null;
}

function updateFile(filePath) {
    let content = fs.readFileSync(filePath, 'utf8');
    let modified = false;
    const meta = extractMetaFromPath(filePath);

    // 1. Add meta description if missing
    if (!content.includes('<meta name="description"')) {
        const descContent = meta
            ? `Class ${meta.classNum} NCERT Exercise ${meta.exerciseNum} Practice - ${meta.chapterName} chapter. Practice questions with step-by-step solutions.`
            : 'NCERT Exercise Practice questions with detailed step-by-step solutions.';

        // Insert after viewport meta
        const viewportPattern = /(<meta name="viewport"[^>]*>)/;
        if (viewportPattern.test(content)) {
            content = content.replace(viewportPattern, `$1\n    <meta name="description" content="${descContent}">`);
            modified = true;
        }
    }

    // 2. Fix breadcrumb schema typo: "Exercise X Y.html" -> "Exercise X.Y"
    const breadcrumbPattern = /"name":\s*"Exercise (\d+) (\d+)\.html"/g;
    if (breadcrumbPattern.test(content)) {
        content = content.replace(breadcrumbPattern, '"name": "Exercise $1.$2"');
        modified = true;
    }

    // 3. Add datePublished and dateModified to Article schema if missing
    if (content.includes('"learningResourceType"') && !content.includes('"datePublished"')) {
        content = content.replace(
            /("url":\s*"https:\/\/www\.sjmaths\.com\/favicon\.png"\s*\n\s*}\s*\n\s*},?)\s*\n(\s*"learningResourceType")/,
            `$1\n  "datePublished": "${TODAY}",\n  "dateModified": "${TODAY}",\n$2`
        );
        modified = true;
    }

    // 4. Remove timer-box elements
    const timerPattern = /<div class="timer-box"[^>]*>[\s\S]*?<\/div>\s*/g;
    if (timerPattern.test(content)) {
        content = content.replace(timerPattern, '');
        modified = true;
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
        if (updateFile(file)) {
            console.log(`✓ Updated: ${relativePath}`);
            updatedCount++;
        } else {
            console.log(`- Skipped (already up to date): ${relativePath}`);
        }
    } catch (error) {
        console.error(`✗ Error updating ${relativePath}: ${error.message}`);
    }
}

console.log(`\n========================================`);
console.log(`Done! Updated ${updatedCount} of ${files.length} files.`);
