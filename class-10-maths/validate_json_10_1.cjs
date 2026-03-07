const fs = require('fs');
const path = require('path');

const jsonPath = path.join(__dirname, 'chapter-1-data.json');

try {
    const data = fs.readFileSync(jsonPath, 'utf8');
    const json = JSON.parse(data);
    console.log('JSON is valid.');
    console.log('Chapter ID:', json.chapterId);
    console.log('Concepts count:', json.concepts.length);
    json.concepts.forEach((c, i) => {
        console.log(`Concept ${i + 1}: ${c.title}`);
        console.log(`  Practice: ${c.practice.length}`);
        console.log(`  PYQ: ${c.pyq.length}`);
        console.log(`  Test: ${c.test.length}`);
    });
    console.log('Mastery Exam questions:', json.chapterTest.questions.length);
} catch (e) {
    console.error('JSON Error:', e.message);
    process.exit(1);
}
