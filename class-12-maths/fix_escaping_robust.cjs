const fs = require('fs');

// The issue is likely that write_to_file already used some escaping, 
// and my simple regex was too aggressive or not aggressive enough.
// Let's use a safer approach: identify LaTeX patterns and ensure they are double-escaped.

let data = fs.readFileSync('chapter-13-data.json', 'utf8');

// First, let's normalize: if we see \\\, it's a mess. 
// If we see \ followed by a word character (LaTeX command), it MUST be \\.

// Regex to find single backslashes before common LaTeX/MathJax commands
// that are likely causing "Bad escaped character" in JSON.
// In JSON, \n, \r, \t, \", \\ are valid.
// \cap, \cup, \frac, etc. are INVALID if single-escaped.

const commands = [
    'cap', 'cup', 'cap', 'cup', 'frac', 'dots', 'sum', 'mu', 'approx', 'phi',
    'mathbb', 'neq', 'neq', 'times', 'cdot', 'cap', 'cup', 'cup', 'cap',
    'infty', 'dots', 'implies', 'subset', 'dots', 'cup', 'cap', 'dots'
];

// Special case for \n which is valid in JSON strings usually, but not here if intended as LaTeX.
// Actually, in our case, these are all inside JSON strings.

// Let's just escape EVERY backslash that isn't already a double backslash
// and isn't a valid JSON escape (like \")
// Actually, it's safer to just replace all \ with \\ and then fix the cases where we now have \\\\ 
// and then fix the cases where we had \" which is now \\"

data = data.replace(/\\/g, '\\\\'); // All \ becomes \\
data = data.replace(/\\\\\\\\/g, '\\\\'); // Any original \\ was \\\\, now \\\\\\\\, back to \\\\
data = data.replace(/\\\\"/g, '\\"'); // Any original \" was \\", now \\\\", back to \\"

fs.writeFileSync('chapter-13-data.json', data);
console.log('Robustly fixed LaTeX escaping in chapter-13-data.json');
