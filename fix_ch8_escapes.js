const fs = require('fs');

let text = fs.readFileSync('class-10-maths/chapter-8-data.json', 'utf8');
let res = '';

for (let i = 0; i < text.length; i++) {
    if (text[i] === '\\') {
        if (i + 1 < text.length) {
            const next = text[i + 1];
            if (next === '\\') {
                res += '\\\\'; // Keep double
                i++;
            } else if (['"', 'n', 'r', 't', 'b', 'f', '/'].includes(next)) {
                res += '\\'; // Keep standard JSON escape
            } else {
                res += '\\\\'; // Make single backslash into double
            }
        } else {
            res += '\\\\';
        }
    } else {
        res += text[i];
    }
}

fs.writeFileSync('class-10-maths/chapter-8-data.json', res);
console.log('Fixed backslashes in chapter-8-data.json');

try {
    JSON.parse(res);
    console.log('JSON parsed successfully!');
} catch (e) {
    console.error('JSON Error:', e.message);
}
