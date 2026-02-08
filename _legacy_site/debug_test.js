const fs = require('fs');
const path = require('path');
const file = path.join('classes', 'class-9', 'worksheets', 'chapter-1-number-system', 'hots.html');

try {
    const content = fs.readFileSync(file, 'utf8');

    const checks = [
        { test: /<html[^>]*lang=/i, msg: 'Has lang attribute' },
        { test: /<meta[^>]*charset=/i, msg: 'Has charset meta' },
        { test: /<meta[^>]*name=["']viewport["']/i, msg: 'Has viewport meta' },
        { test: /<title>/i, msg: 'Has title tag' }
    ];

    console.log(`Checking ${file}...`);
    checks.forEach(({ test, msg }) => {
        if (test.test(content)) {
            console.log(`✅ ${msg}`);
        } else {
            console.log(`❌ ${msg}`);
            console.log(`Failed Regex: ${test}`);
        }
    });
} catch (error) {
    console.error('Error reading file:', error.message);
}
