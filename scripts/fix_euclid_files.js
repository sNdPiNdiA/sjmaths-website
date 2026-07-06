const fs = require('fs');
const path = require('path');

const ROOT_DIR = path.join(__dirname, '..');

const files = [
  'class-9-maths/tests/chapter-wise/chapter-5-introduction-to-euclids-geometry/basic.html',
  'class-9-maths/tests/chapter-wise/chapter-5-introduction-to-euclids-geometry/standard.html',
  'class-9-maths/tests/chapter-wise/chapter-5-introduction-to-euclids-geometry/hard.html',
  'class-9-maths/worksheets/chapter-5-introduction-to-euclids-geometry/basic.html',
  'class-9-maths/worksheets/chapter-5-introduction-to-euclids-geometry/standard.html'
];

for (const relPath of files) {
  const filePath = path.join(ROOT_DIR, relPath);
  if (!fs.existsSync(filePath)) continue;

  let html = fs.readFileSync(filePath, 'utf8');

  const filename = path.basename(filePath, '.html');
  const dirName = relPath.includes('tests') ? 'Online Test' : 'Worksheet';
  const cleanDesc = `Practice Class 9 Euclid's Geometry ${filename.toUpperCase()} ${dirName} with step-by-step solutions, key axioms, and revision notes on SJMaths.`;

  // Replace entire description tag line cleanly
  html = html.replace(/<meta\s+name=["']description["'][\s\S]*?\n/i, `<meta name="description" content="${cleanDesc}">\n`);

  fs.writeFileSync(filePath, html, 'utf8');
}

console.log('🎉 Cleaned Euclid geometry test and worksheet files.');
