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
console.log('Found ' + dirs.length + ' microtopic pages with theory.json');
dirs.forEach(d => console.log(d));