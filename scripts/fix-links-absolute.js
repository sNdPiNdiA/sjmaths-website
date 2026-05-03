const fs = require('fs');
const path = require('path');

const ROOT_DIR = process.cwd();
const CLASSES = ['class-9-maths', 'class-10-maths', 'class-11-maths', 'class-12-maths'];

CLASSES.forEach(cls => {
  const notesDir = path.join(ROOT_DIR, cls, 'chapter-wise-notes');
  if (fs.existsSync(notesDir)) {
    const chapters = fs.readdirSync(notesDir, { withFileTypes: true })
      .filter(d => d.isDirectory())
      .map(d => d.name);

    chapters.forEach(chap => {
      const indexPath = path.join(notesDir, chap, 'index.html');
      if (!fs.existsSync(indexPath)) return;

      let content = fs.readFileSync(indexPath, 'utf8');
      
      // Look for practice link
      // Match href="../../ncert-exercise-practice/ or href="../../../ncert-exercise-practice/
      const regex = /href="(\.\.\/)+ncert-exercise-practice\/([^"]+)"/g;
      
      const newContent = content.replace(regex, (match, p1, p2) => {
        return `href="/${cls}/ncert-exercise-practice/${p2}"`;
      });
      
      if (content !== newContent) {
        console.log(`Fixing paths in: ${indexPath} to absolute`);
        fs.writeFileSync(indexPath, newContent, 'utf8');
      }
    });
  }
});
