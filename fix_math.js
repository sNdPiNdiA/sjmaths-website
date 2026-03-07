const fs = require('fs');
let content = fs.readFileSync('class-10-maths/chapter-3-data.json', 'utf8');
const obj = JSON.parse(content);

function replaceMath(o) {
    if (typeof o === 'string') {
        // Find $...$ where the content inside has no $, and it's not immediately preceded by a letter/number to avoid matching inside strings inappropriately, although our markdown math Usually has spaces around or is at start.
        // Even simpler: since I know the exact math expressions, I'll replace $...$ where ... doesn't contain $ or \n.
        // But what about "$17"? It doesn't have a closing $. 
        // We only replace if there's a pair.
        // Let's explicitly NOT replace if the content starts with digits or space, e.g. "$17" or "$ x for adults". Wait, "$17" and "$x for adults" in the text are:
        // "pays $17" and "pays $16" -> The $17 and $16 could match if there's another $ later. 
        // e.g. "$17... $16". Then "17... " is captured.
        // To be safe, look for $<math>$ where <math> starts with a letter, backslash, or number but is meant as math. 
        return o.replace(/\$([^\$\n]+)\$/g, (match, p1) => {
            // If the captured string starts with a number and has no spaces (like '17' or '16'), it's likely a currency overlap.
            // Actually, in our JSON, math is like $a_1x...$ or $x+y=5$. 
            // Currency is "$17". 
            if (p1 === '17' || p1 === '16' || p1 === 'x for adults and ' || p1 === 'y for kids. A family of 2 adults and 3 kids pays ') {
                return match; // don't replace
            }
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

const newObj = replaceMath(obj);
fs.writeFileSync('class-10-maths/chapter-3-data.json', JSON.stringify(newObj, null, 4));
console.log('Math delimiters updated successfully.');
