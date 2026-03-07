const fs = require('fs');
const path = require('path');

const filePath = path.join(__dirname, 'chapter-12-data.json');

try {
    const data = fs.readFileSync(filePath, 'utf8');
    const json = JSON.parse(data);
    console.log('JSON is valid!');
    console.log('Concepts:', json.concepts.length);
    json.concepts.forEach((c, idx) => {
        console.log(`Concept ${idx + 1}: ${c.title} (${c.practice.length} Practice, ${c.pyq.length} PYQ, ${c.test.length} Test)`);
    });
} catch (err) {
    console.error('JSON Error:', err.message);
    const match = err.message.match(/at position (\d+)/);
    if (match) {
        const pos = parseInt(match[1]);
        const content = fs.readFileSync(filePath, 'utf8');
        const start = Math.max(0, pos - 50);
        const end = Math.min(content.length, pos + 50);
        console.error('Context:', content.substring(start, end));
        console.error(' '.repeat(pos - start + 8) + '^');
    }
    process.exit(1);
}
