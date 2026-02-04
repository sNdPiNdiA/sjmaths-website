const fs = require('fs');
const path = require('path');
const file = path.join('classes', 'class-9', 'tests', 'chapter-wise', 'chapter-1-number-systems', 'test-1.html');

try {
    const content = fs.readFileSync(file, 'utf8');
    console.log(`Size: ${content.length}`);
    console.log('--- Content ---');
    console.log(content);
} catch (e) {
    console.error(e);
}
