const fs = require('fs');
const path = 'c:/Users/sande/Documents/GitHub/sjmaths-website/class-12-maths/chapter-10-data.json';

let content = fs.readFileSync(path, 'utf8');

// Protect existing double backslashes, escape single ones
content = content.split('\\\\').map(part => part.replace(/\\/g, '\\\\')).join('\\\\');

fs.writeFileSync(path, content);
console.log('Robustly fixed LaTeX escaping in ' + path);
