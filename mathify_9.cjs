const fs = require('fs');
const path = require('path');

const files = [
    'chapter-1-data.json', 'chapter-2-data.json', 'chapter-3-data.json', 'chapter-4-data.json',
    'chapter-5-data.json', 'chapter-6-data.json', 'chapter-7-data.json', 'chapter-8-data.json',
    'chapter-9-data.json', 'chapter-10-data.json', 'chapter-11-data.json', 'chapter-12-data.json'
];

const mathKeywords = [
    '\\\\angle', '\\\\cong', '\\\\Delta', '\\\\pi', '\\\\sqrt', '\\\\frac', '\\\\text{', '\\\\iff', '\\\\implies',
    '\\\\angle', '\\\\theta', '\\\\rho', '\\\\sigma', '\\\\mu', '\\\\lambda', '\\\\alpha', '\\\\beta', '\\\\gamma'
];

files.forEach(file => {
    const filePath = path.join(__dirname, 'class-9-maths', file);
    if (!fs.existsSync(filePath)) return;

    let content = fs.readFileSync(filePath, 'utf8');
    let data = JSON.parse(content);

    function processObject(obj) {
        for (let key in obj) {
            if (typeof obj[key] === 'string') {
                let s = obj[key];
                // Check if string contains math keywords and is NOT already wrapped in $
                let hasMath = mathKeywords.some(k => s.includes(k.replace(/\\\\/g, '\\')));
                let isWrapped = s.trim().startsWith('$') && s.trim().endsWith('$');

                if (hasMath && !isWrapped) {
                    // Primitive check to avoid wrapping already wrapped interior math
                    if (!s.includes('$')) {
                        obj[key] = `$${s}$`;
                    }
                }
            } else if (typeof obj[key] === 'object' && obj[key] !== null) {
                processObject(obj[key]);
            }
        }
    }

    processObject(data);
    fs.writeFileSync(filePath, JSON.stringify(data, null, 4), 'utf8');
    console.log(`Mathified ${file}`);
});
