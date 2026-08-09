const fs = require('fs');
const s = fs.readFileSync('generate-microtopics.cjs', 'utf8');
const lines = s.split('\n');
let total = 0;
lines.forEach((l, i) => {
    const c = (l.match(/`/g) || []).length;
    if (c > 0) {
        total += c;
        console.log((i + 1) + ': ' + c + ' backtick(s) -> ' + JSON.stringify(l.slice(0, 100)));
    }
});
console.log('TOTAL BACKTICKS = ' + total);
