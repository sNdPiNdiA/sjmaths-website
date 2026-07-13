const fs = require('fs');
const path = require('path');

function walk(dir) {
    let results = [];
    const list = fs.readdirSync(dir);
    list.forEach(function(file) {
        file = path.join(dir, file);
        if (fs.statSync(file).isDirectory()) {
            results = results.concat(walk(file));
        } else if (file.endsWith('.html')) {
            results.push(file);
        }
    });
    return results;
}

let bad = 0;
let missing = 0;
walk('upsssc-lower-mains').forEach(f => {
    const c = fs.readFileSync(f, 'utf8');
    const m = c.match(/<h1/gi);
    if (m && m.length > 1) {
        bad++;
        console.log(f, 'has', m.length, 'H1 tags');
    } else if (!m || m.length === 0) {
        missing++;
        console.log(f, 'is MISSING H1 tag');
    }
});
console.log('Multiple H1 files:', bad);
console.log('Missing H1 files:', missing);
