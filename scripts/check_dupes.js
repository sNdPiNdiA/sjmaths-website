const fs = require('fs');
const path = require('path');

function walk(dir) {
    let results = [];
    const list = fs.readdirSync(dir);
    list.forEach(function(file) {
        file = path.join(dir, file);
        const stat = fs.statSync(file);
        if (stat && stat.isDirectory()) {
            results = results.concat(walk(file));
        } else if (file.endsWith('.html')) {
            results.push(file);
        }
    });
    return results;
}

let bad = 0;
walk('upsssc-lower-mains').forEach(f => {
    const c = fs.readFileSync(f, 'utf8');
    const m = c.match(/<meta[^>]+name=["']description["']/gi);
    if (m && m.length > 1) {
        bad++;
        console.log(f, m.length);
    }
});
console.log('Duplicate description files:', bad);
