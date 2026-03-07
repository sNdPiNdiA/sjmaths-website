const fs = require('fs');

const data = fs.readFileSync('chapter-13-data.json', 'utf8');

// Fix common unescaped backslashes in LaTeX strings for JSON
// Specifically looking for things like \cdot, \cap, \cup, \dots, \frac that aren't already escaped with \\
// We should replace any \ that is not followed by another \ with \\
// However, in the JS string 'data', the actual backslashes are represented as \.
// If the JSON is invalid, it means there are single \ characters in it.

const fixedData = data.replace(/\\(?!\\)/g, '\\\\');

fs.writeFileSync('chapter-13-data.json', fixedData);
console.log('Fixed LaTeX escaping in chapter-13-data.json');
