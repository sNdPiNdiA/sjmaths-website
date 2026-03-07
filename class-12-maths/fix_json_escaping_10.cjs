const fs = require('fs');
const path = 'c:/Users/sande/Documents/GitHub/sjmaths-website/class-12-maths/chapter-10-data.json';

let content = fs.readFileSync(path, 'utf8');

// First, find all single backslashes that are not part of an escaped character
// This is tricky because some are already escaped (\\).
// We want to replace \ with \\ in LaTeX but not break valid JSON escapes like \n, \", etc.

// Better approach: Since we know the LaTeX contexts ($ or \(\)), 
// but in JSON we just have strings.
// Let's replace any \ that is NOT followed by another \ OR a valid JSON escape char (", \, /, b, f, n, r, t, u)

content = content.replace(/\\(?![\\\/bfnrtu"'])/g, '\\\\');

fs.writeFileSync(path, content);
console.log('Fixed LaTeX escaping in ' + path);
