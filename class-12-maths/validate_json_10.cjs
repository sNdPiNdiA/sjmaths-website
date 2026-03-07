const fs = require('fs');
const path = 'c:/Users/sande/Documents/GitHub/sjmaths-website/class-12-maths/chapter-10-data.json';

try {
    const data = JSON.parse(fs.readFileSync(path, 'utf8'));
    console.log('JSON is valid!');
    console.log('Concepts:', data.concepts.length);
    data.concepts.forEach((c, i) => {
        console.log(`Concept ${i + 1}: ${c.title} (${c.practice.length} Practice, ${c.pyq.length} PYQ, ${c.test.length} Test)`);
    });
} catch (e) {
    console.error('JSON Error:', e.message);
    process.exit(1);
}
