const fs = require('fs');

const s1 = fs.readFileSync('class-10-social-science/economics/index.html', 'utf8').match(/<style[\s\S]*?<\/style>/i)[0];
const s2 = fs.readFileSync('class-10-social-science/geography/index.html', 'utf8').match(/<style[\s\S]*?<\/style>/i)[0];

const c1 = s1.replace(/<\/?style>/gi, '');
const c2 = s2.replace(/<\/?style>/gi, '');

const lines1 = c1.split(/\r?\n/);
const lines2 = c2.split(/\r?\n/);

console.log('lines1 count:', lines1.length, 'lines2 count:', lines2.length);
lines1.forEach((l, i) => {
  if (l !== lines2[i]) {
    console.log('Diff at line ' + i + ':\n  1: ' + l + '\n  2: ' + (lines2[i] || 'EOF'));
  }
});
