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

const files = walk('upsc');
let checks = {
    total: files.length,
    title: 0,
    desc: 0,
    canonical: 0,
    og: 0,
    robots: 0,
    lang: 0
};

files.forEach(f => {
    const c = fs.readFileSync(f, 'utf8');
    if (c.includes('<title>')) checks.title++;
    if (c.includes('<meta name="description"')) checks.desc++;
    if (c.includes('<link rel="canonical"')) checks.canonical++;
    if (c.includes('property="og:')) checks.og++;
    if (c.includes('<meta name="robots"')) checks.robots++;
    if (c.includes('lang="en"') || c.includes('lang="hi"')) checks.lang++;
});

console.log(JSON.stringify(checks, null, 2));
