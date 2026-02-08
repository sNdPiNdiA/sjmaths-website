/**
 * Add exercise.js to Class 10 exercise files that are missing it
 */
const fs = require('fs');
const path = require('path');

const baseDir = path.join(__dirname, '..', 'classes', 'class-10', 'ncert-exercise-practice');

// Get all chapter folders
const folders = fs.readdirSync(baseDir).filter(f =>
    f.startsWith('chapter-') && fs.statSync(path.join(baseDir, f)).isDirectory()
);

let updated = 0;
let skipped = 0;

folders.forEach(folder => {
    const folderPath = path.join(baseDir, folder);
    const files = fs.readdirSync(folderPath).filter(f =>
        f.endsWith('.html') && f.startsWith('exercise-')
    );

    files.forEach(file => {
        const filePath = path.join(folderPath, file);
        let content = fs.readFileSync(filePath, 'utf8');

        if (content.includes('exercise.js')) {
            console.log(`✓ ${folder}/${file} - already has exercise.js`);
            skipped++;
            return;
        }

        // Find the </body> tag and insert the script before it

        if (content.includes('</body>')) {
            content = content.replace('</body>', `${scriptTag}\n</body>`);
            fs.writeFileSync(filePath, content, 'utf8');
            console.log(`✅ ${folder}/${file} - ADDED exercise.js`);
            updated++;
        } else {
            console.log(`⚠ ${folder}/${file} - no 
    <script src="../../../../assets/js/exercise-seo.js"></script>
    <script src="../../../../assets/js/main.min.js" defer></script>
    <script src="../../../../assets/js/exercise.js"></script>
    <script src="../../../../assets/js/exercise-header.js"></script>
    <script src="../../../../assets/js/exercise-footer.js"></script>
</body> tag found`);
        }
    });
});

console.log('\n========================================');
console.log(`Updated: ${updated} files`);
console.log(`Skipped (already had): ${skipped} files`);
