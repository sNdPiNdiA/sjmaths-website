const fs = require('fs');
const path = require('path');

const filePath = path.join(__dirname, 'chapter-11-data.json');
let content = fs.readFileSync(filePath, 'utf8');

// Step 1: Normalize all backslash sequences to single backslash
// EXCEPT if followed by a quote (to preserve \" JSON escapes)
content = content.replace(/\\+(?!")/g, '\\');

// Step 2: Escape all single backslashes that are NOT valid JSON escapes
// Valid escapes: \u, \n, \r, \t, \b, \f, \", \\, \/
content = content.replace(/\\(?![unrtbf"\/])/g, '\\\\');

fs.writeFileSync(filePath, content);
console.log('Refined escaping in chapter-11-data.json');
