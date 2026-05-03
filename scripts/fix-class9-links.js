const fs = require('fs');
const path = require('path');

const ROOT_DIR = process.cwd();
const CLASS = 'class-9-maths';

const notesDir = path.join(ROOT_DIR, CLASS, 'chapter-wise-notes');
if (fs.existsSync(notesDir)) {
  const chapters = fs.readdirSync(notesDir, { withFileTypes: true })
    .filter(d => d.isDirectory())
    .map(d => d.name);

  chapters.forEach(chap => {
    const indexPath = path.join(notesDir, chap, 'index.html');
    if (!fs.existsSync(indexPath)) return;

    let content = fs.readFileSync(indexPath, 'utf8');
    
    // Replace ../../../ncert-exercise-practice/ with ../../ncert-exercise-practice/
    const oldPath = '../../../ncert-exercise-practice/';
    const newPath = '../../ncert-exercise-practice/';
    
    if (content.includes(oldPath)) {
      console.log(`Fixing paths in: ${indexPath}`);
      content = content.split(oldPath).join(newPath);
      fs.writeFileSync(indexPath, content, 'utf8');
    }
  });
}
