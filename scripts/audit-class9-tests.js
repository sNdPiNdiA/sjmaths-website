const fs = require('fs');
const path = require('path');

const baseDir = 'c:/Users/sande/Documents/GitHub/sjmaths-website/classes/class-9/tests/chapter-wise';
const chapters = fs.readdirSync(baseDir).filter(f => fs.statSync(path.join(baseDir, f)).isDirectory());

const levels = ['basic', 'standard', 'hard'];

let results = '--- Class 9 Test Audit ---\n';

chapters.forEach(chapter => {
    results += `\nChapter: ${chapter}\n`;
    levels.forEach(level => {
        const htmlPath = path.join(baseDir, chapter, `${level}.html`);
        const jsonPath = path.join(baseDir, chapter, `${level}.json`);

        // Check HTML
        if (!fs.existsSync(htmlPath)) {
            results += `  [MISSING HTML] ${level}.html\n`;
        } else {
            const htmlContent = fs.readFileSync(htmlPath, 'utf8');
            if (htmlContent.length < 100) {
                results += `  [EMPTY HTML] ${level}.html\n`;
            }
            if (!htmlContent.includes('new TestEngine')) {
                results += `  [INVALID HTML] ${level}.html (No TestEngine init)\n`;
            }
        }

        // Check JSON
        if (!fs.existsSync(jsonPath)) {
            results += `  [MISSING JSON] ${level}.json\n`;
        } else {
            try {
                const jsonContent = fs.readFileSync(jsonPath, 'utf8');
                const data = JSON.parse(jsonContent);
                if (!data.questions || !Array.isArray(data.questions) || data.questions.length === 0) {
                    results += `  [INVALID JSON] ${level}.json (No questions)\n`;
                } else {
                    results += `  [OK] ${level} (${data.questions.length} questions)\n`;
                }
            } catch (e) {
                results += `  [SYNTAX ERROR] ${level}.json: ${e.message}\n`;
            }
        }
    });
});

fs.writeFileSync('c:/Users/sande/Documents/GitHub/sjmaths-website/audit_results.log', results, 'utf8');
console.log('Audit complete. Results saved to audit_results.log');
