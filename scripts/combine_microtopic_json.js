/**
 * Combine split JSON files (theory.json, practice.json, mastery.json) into unified content.json
 * and embed them into microtopic index.html files
 */

const fs = require('fs');
const path = require('path');

function findDirs(dir, results = []) {
    if (!fs.existsSync(dir)) return results;
    const items = fs.readdirSync(dir);
    items.forEach(item => {
        const full = path.join(dir, item);
        const stat = fs.statSync(full);
        if (stat.isDirectory()) {
            findDirs(full, results);
        } else if (item === 'theory.json') {
            results.push(path.dirname(full));
        }
    });
    return results;
}

const dirs = findDirs('upsc');
console.log(`Found ${dirs.length} microtopic pages\n`);

dirs.forEach(dir => {
    try {
        const theoryPath = path.join(dir, 'theory.json');
        const practicePath = path.join(dir, 'practice.json');
        const masteryPath = path.join(dir, 'mastery.json');
        const mockPath = path.join(dir, 'mock.json');
        const htmlPath = path.join(dir, 'index.html');

        if (!fs.existsSync(theoryPath) || !fs.existsSync(htmlPath)) {
            console.log(`⚠ Skipping ${dir} - missing theory.json or index.html`);
            return;
        }

        const theory = JSON.parse(fs.readFileSync(theoryPath, 'utf8'));
        const practice = fs.existsSync(practicePath) ? JSON.parse(fs.readFileSync(practicePath, 'utf8')) : null;
        const mastery = fs.existsSync(masteryPath) ? JSON.parse(fs.readFileSync(masteryPath, 'utf8')) : null;
        const mock = fs.existsSync(mockPath) ? JSON.parse(fs.readFileSync(mockPath, 'utf8')) : null;

        // Build unified content structure
        const content = {
            breadcrumbs: theory.breadcrumbs || {},
            hero: theory.hero || {},
            labels: theory.labels || {},
            timeline: theory.timeline || { cards: [] },
            mnemonics: theory.mnemonics || { items: [] },
            flashcards: theory.flashcards || { items: [] },
            traps: theory.traps || { items: [] },
            deepDive: {
                title: theory.deepDive?.title || 'Study Notes',
                description: theory.deepDive?.description || '',
                sections: (theory.deepDive?.sections || []).map((sec, idx) => {
                    // Merge mastery zone from mastery.json if available
                    let masteryZone = [];
                    if (sec && Array.isArray(sec.masteryZone)) {
                        masteryZone = sec.masteryZone;
                    }

                    const secTitle = typeof sec?.title === 'string' ? sec.title : '';
                    const secNum = secTitle.includes('. ') ? secTitle.split('. ')[1] : '';

                    if (mastery && mastery.sections && Array.isArray(mastery.sections) && secNum) {
                        try {
                            const masterySection = mastery.sections.find(ms => {
                                const msTitle = typeof ms?.title === 'string' ? ms.title : '';
                                return msTitle === secTitle || msTitle.includes(secNum);
                            });
                            if (masterySection && Array.isArray(masterySection.masteryZone)) {
                                masteryZone = masterySection.masteryZone;
                            }
                        } catch (e) {
                            // Ignore mastery merge errors
                        }
                    }

                    return {
                        title: secTitle,
                        content: typeof sec?.content === 'string' ? sec.content : '',
                        masteryZone: masteryZone
                    };
                })
            },
            practiceQuestions: practice?.practiceQuestions || [],
            mockTestQuestions: mock?.mockTestQuestions || []
        };

        const embeddedScript = `<script type="application/json" id="embedded-study-guide-data">\n${JSON.stringify(content, null, 2)}\n</script>`;

        const html = fs.readFileSync(htmlPath, 'utf8');
        const pattern = 'competitive-exam-guide.min.js';
        const scriptIndex = html.indexOf(pattern);

        if (scriptIndex === -1) {
            console.log(`⚠ Skipping ${dir} - competitive-exam-guide script not found`);
            return;
        }

        const tagStart = html.lastIndexOf('<script', scriptIndex);
        const tagEnd = html.indexOf('>', scriptIndex) + 1;

        const updatedHtml = html.substring(0, tagStart) +
            embeddedScript + '\n' +
            html.substring(tagStart);

        fs.writeFileSync(htmlPath, updatedHtml, 'utf8');
        console.log(`✓ ${dir}`);
    } catch (err) {
        console.error(`✗ Error processing ${dir}:`, err.message);
    }
});

console.log('\nDone!');