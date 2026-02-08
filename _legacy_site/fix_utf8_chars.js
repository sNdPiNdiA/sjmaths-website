const fs = require('fs');
const path = require('path');

const basePath = 'c:\\Users\\sande\\Documents\\GitHub\\sjmaths-website\\classes\\class-10\\ncert-exercise-practice';

// Using hex escapes to avoid encoding issues
const replacements = [
  { old: '\u00e2\u0080\u0093', new: '\u2013' },  // ”" to –
  { old: '\u00e2\u0080\u00a6', new: '\u2026' }, // ”¦ to …
  { old: '\u00e2\u0088\u0092', new: '\u2212' }, // âˆ' to −
  { old: '\u00e2\u0088\u009a', new: '\u221a' }, // âˆš to √
  { old: '\u00c2\u00a9', new: '\u00a9' },       // Â© to ©
  { old: '\u00e2\u0080\u0099', new: '\u2019' }, // ’ to '
  { old: '\u00e2\u0084\u0080', new: '\u03c0' }, // â„ to π
  { old: '\u00e2\u0086\u0092', new: '\u2192' }, // ←' to →
  { old: 'b\u00e2\u0082\u0081', new: 'b\u2081' }, // bâ‚ to b₁
  { old: 'b\u00e2\u0082\u0082', new: 'b\u2082' }, // bâ‚‚ to b₂
  { old: 'c\u00e2\u0082\u0081', new: 'c\u2081' }, // câ‚ to c₁
  { old: 'c\u00e2\u0082\u0082', new: 'c\u2082' }, // câ‚‚ to c₂
  { old: '\u00e2\u0089\u00a0', new: '\u2260' }, // â‰  to ≠
  { old: '\u00e2\u0089\u00a4', new: '\u2264' }, // â‰¤ to ≤
  { old: '\u00c2', new: '' },                   // Remove stray Â (often appears as artifact)
];

const walkDir = (dir) => {
  let files = [];
  const list = fs.readdirSync(dir);
  list.forEach(file => {
    const filePath = path.join(dir, file);
    const stat = fs.statSync(filePath);
    if (stat.isDirectory()) {
      files = files.concat(walkDir(filePath));
    } else if (file.endsWith('.html') && file.startsWith('exercise-')) {
      files.push(filePath);
    }
  });
  return files;
};

const files = walkDir(basePath);
let fixedCount = 0;
let okCount = 0;

files.forEach(filePath => {
  let content = fs.readFileSync(filePath, 'utf8');
  const original = content;
  
  replacements.forEach(r => {
    content = content.split(r.old).join(r.new);
  });
  
  if (content !== original) {
    fs.writeFileSync(filePath, content, 'utf8');
    console.log('Fixed: ' + path.basename(filePath));
    fixedCount++;
  } else {
    console.log('OK: ' + path.basename(filePath));
    okCount++;
  }
});

console.log('Complete! Fixed: ' + fixedCount + ', OK: ' + okCount);
