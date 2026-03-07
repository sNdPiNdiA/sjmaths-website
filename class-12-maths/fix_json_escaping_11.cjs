const fs = require('fs');
const path = require('path');

const filePath = path.join(__dirname, 'chapter-11-data.json');
let content = fs.readFileSync(filePath, 'utf8');

// Safeguard against double-escaping: 
// Replace single backslashes that are NOT followed by [u, n, r, t, b, f, ", \, /]
// with double backslashes.
content = content.replace(/\\(?![unrtbf"\\/])/g, '\\\\');

fs.writeFileSync(filePath, content);
console.log('Fixed escaping in chapter-11-data.json');
