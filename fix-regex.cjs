const fs = require('fs');
const f = 'up-assistant-teacher/hindi/translate-hindi.js';
let c = fs.readFileSync(f, 'utf8');
const lines = c.split('\n');
// Fix the broken regex on line 236 (0-indexed: 235)
lines[235] = String.raw`          const scriptRegex = /(<script id="upsc-page-data" type="application\/json">)([\s\S]*?)(<\/script>)/;`;
fs.writeFileSync(f, lines.join('\n'), 'utf8');
console.log('Fixed line 236!');
console.log('New content:', lines[235]);
