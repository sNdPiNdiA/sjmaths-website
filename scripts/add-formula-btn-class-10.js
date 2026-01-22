const fs = require('fs');
const path = require('path');

// Path to Class 10 exercises
const directoryPath = path.join(__dirname, '../classes/class-10/ncert-exercise-practice');

function updateFiles(dir) {
    if (!fs.existsSync(dir)) {
        console.error(`Directory not found: ${dir}`);
        return;
    }

    const files = fs.readdirSync(dir);

    files.forEach(file => {
        const filePath = path.join(dir, file);
        const stat = fs.statSync(filePath);

        if (stat.isDirectory()) {
            updateFiles(filePath);
        } else if (file.endsWith('.html')) {
            let content = fs.readFileSync(filePath, 'utf8');
            let modified = false;

            // 1. Add Button if missing
            if (!content.includes('class="formula-btn"')) {
                const floatingControlsRegex = /(<div class="floating-controls">[\s\S]*?)(<button class="theme-toggle-btn")/i;
                if (floatingControlsRegex.test(content)) {
                    const buttonHtml = `  <button class="formula-btn" aria-label="Formulas">\n    <i class="fas fa-book-open"></i>\n  </button>\n  `;
                    content = content.replace(floatingControlsRegex, `$1${buttonHtml}$2`);
                    modified = true;
                }
            }

            // 2. Add Script if missing
            if (!content.includes('src="/assets/js/exercise.js"')) {
                // Try to insert before </body>
                if (content.includes('</body>')) {
                    content = content.replace('</body>', '<script src="/assets/js/exercise.js"></script>\n</body>');
                    modified = true;
                }
            }

            if (modified) {
                fs.writeFileSync(filePath, content, 'utf8');
                console.log(`Updated ${file}`);
            } else {
                console.log(`Skipping ${file} (Already up to date)`);
            }
        }
    });
}

console.log('Starting batch update for Class 10...');
updateFiles(directoryPath);
console.log('Batch update complete.');