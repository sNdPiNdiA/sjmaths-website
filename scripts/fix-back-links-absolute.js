const fs = require('fs');
const path = require('path');

const ROOT_DIR = process.cwd();
const CLASSES = ['class-9-maths', 'class-10-maths', 'class-11-maths', 'class-12-maths'];

CLASSES.forEach(cls => {
  const practiceDir = path.join(ROOT_DIR, cls, 'ncert-exercise-practice');
  if (fs.existsSync(practiceDir)) {
    const chapters = fs.readdirSync(practiceDir, { withFileTypes: true })
      .filter(d => d.isDirectory())
      .map(d => d.name);

    chapters.forEach(chap => {
      const chapPath = path.join(practiceDir, chap);
      const files = fs.readdirSync(chapPath).filter(f => f.endsWith('.html'));

      files.forEach(file => {
        const filePath = path.join(chapPath, file);
        let content = fs.readFileSync(filePath, 'utf8');
        
        // Look for back to notes link
        // Match href="../../chapter-wise-notes/
        const regex = /href="\.\.\/\.\.\/chapter-wise-notes\/([^"]+)"/g;
        
        const newContent = content.replace(regex, (match, p1) => {
          return `href="/${cls}/chapter-wise-notes/${p1}"`;
        });
        
        if (content !== newContent) {
          console.log(`Fixing back links in: ${filePath} to absolute`);
          fs.writeFileSync(filePath, newContent, 'utf8');
        }
      });
    });
  }
});
