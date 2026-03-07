const fs = require('fs');

let data = fs.readFileSync('chapter-3-data.json', 'utf8');

// Robust fix for LaTeX backslashes in JSON strings
data = data.replace(/\\/g, '\\\\');
data = data.replace(/\\\\\\\\/g, '\\\\');
data = data.replace(/\\\\"/g, '\\"');

fs.writeFileSync('chapter-3-data.json', data);
console.log('Fixed LaTeX escaping in chapter-3-data.json');
