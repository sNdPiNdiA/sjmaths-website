const fs = require('fs');
let content = fs.readFileSync('class-10-maths/chapter-3-data.json', 'utf8');
const obj = JSON.parse(content);

function replaceMath(o) {
    if (typeof o === 'string') {
        return o.replace(/\$([^\$\n]+)\$/g, (match, p1) => {
            if (p1 === '17' || p1 === '16' || p1 === 'x for adults and ' || p1 === 'y for kids. A family of 2 adults and 3 kids pays ') {
                return match;
            }
            // THIS is the correct replacement for KaTeX to work.
            // When stringified, '\\(' becomes '"\\\\("' which is parsed as '\\(' by JSON.parse
            return '\\\\(' + p1 + '\\\\)';
        });
    }
    if (Array.isArray(o)) return o.map(replaceMath);
    if (o !== null && typeof o === 'object') {
        const res = {};
        for (let k in o) res[k] = replaceMath(o[k]);
        return res;
    }
    return o;
}

// I previously screwed up the file, so I will just do a direct string replace of "\\\\(" to "\\(".
let newContent = content.replace(/\\\\\\\\\\\(/g, '\\\\\\(').replace(/\\\\\\\\\\\)/g, '\\\\\\)');

fs.writeFileSync('class-10-maths/chapter-3-data.json', newContent);
console.log('Math delimiters fixed to single escaped backslash.');
