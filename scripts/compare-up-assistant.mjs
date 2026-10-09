import fs from 'fs';

const f1 = 'up-assistant-teacher/child-psychology/creating-conducive-learning-environment/index.html';
const f2 = 'up-assistant-teacher/hindi/alankaara-bhaeda-va-udaaharana/index.html';

const s1 = fs.readFileSync(f1, 'utf8').match(/<style\b[^>]*>([\s\S]*?)<\/style>/i)[1];
const s2 = fs.readFileSync(f2, 'utf8').match(/<style\b[^>]*>([\s\S]*?)<\/style>/i)[1];

console.log('f1 style len:', s1.length, 'f2 style len:', s2.length);

const lines1 = s1.split('\n').map(l => l.trim());
const lines2 = s2.split('\n').map(l => l.trim());

console.log('lines1 count:', lines1.length, 'lines2 count:', lines2.length);

// Compare differences
const diffs = [];
for (let i = 0; i < Math.max(lines1.length, lines2.length); i++) {
  if (lines1[i] !== lines2[i]) {
    diffs.push({ line: i, l1: lines1[i], l2: lines2[i] });
  }
}
console.log('Total diff lines:', diffs.length);
if (diffs.length < 20) {
  console.log(JSON.stringify(diffs, null, 2));
} else {
  console.log('First 10 diffs:');
  console.log(JSON.stringify(diffs.slice(0, 10), null, 2));
}
