const fs = require('fs');

let data = fs.readFileSync('chapter-1-data.json', 'utf8');

// Robust fix for LaTeX backslashes in JSON strings
data = data.replace(/\\/g, '\\\\'); // All \ becomes \\
data = data.replace(/\\\\\\\\/g, '\\\\'); // Any original \\ was \\\\, now \\\\\\\\, back to \\\\
data = data.replace(/\\\\"/g, '\\"'); // Any original \" was \\", now \\\\", back to \\"

fs.writeFileSync('chapter-1-data.json', data);
console.log('Fixed LaTeX escaping in chapter-1-data.json');
