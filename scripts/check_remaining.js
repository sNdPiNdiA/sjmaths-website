const fs = require('fs');
const path = require('path');

function findDirs(dir, results = []) {
    if (!fs.existsSync(dir)) return results;
    const items = fs.readdirSync(dir);
    items.forEach(item => {
        const full = path.join(dir, item);
        const stat = fs.statSync(full);
        if (stat.isDirectory()) {
            findDirs(full, results);
        } else if (item === 'theory.json') {
            results.push(path.dirname(full));
        }
    });
    return results;
}

const dirs = findDirs('upsc');
console.log(`Checking ${dirs.length} microtopic pages for embedded JSON...\n`);

const missing = [];
const embedded = [];

dirs.forEach(dir => {
    const htmlPath = path.join(dir, 'index.html');
    if (!fs.existsSync(htmlPath)) {
        missing.push(dir + ' (missing index.html)');
        return;
    }

    const html = fs.readFileSync(htmlPath, 'utf8');
    if (html.includes('id="embedded-study-guide-data"')) {
        embedded.push(dir);
    } else {
        missing.push(dir);
    }
});

console.log(`Already embedded: ${embedded.length}`);
console.log(`Missing: ${missing.length}\n`);

if (missing.length > 0) {
    console.log('Pages still needing embedding:');
    missing.forEach(m => console.log('  - ' + m));
}