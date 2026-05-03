const fs = require('fs');
const path = require('path');

const ROOT_DIR = process.cwd();
const CLASSES = ['class-10-maths', 'class-11-maths', 'class-12-maths'];

CLASSES.forEach(cls => {
  const notesDir = path.join(ROOT_DIR, cls, 'chapter-wise-notes');
  if (!fs.existsSync(notesDir)) return;

  const chapters = fs.readdirSync(notesDir, { withFileTypes: true })
    .filter(d => d.isDirectory())
    .map(d => d.name);

  chapters.forEach(chap => {
    const indexPath = path.join(notesDir, chap, 'index.html');
    if (!fs.existsSync(indexPath)) return;

    let content = fs.readFileSync(indexPath, 'utf8');
    
    // 1. Identify all practice-link-box blocks
    // We use a regex to find the blocks. 
    // They usually look like <div class="practice-link-box" ...> ... </div>
    // This can be tricky with multiline.
    
    const blocks = [];
    const blockRegex = /<div class="practice-link-box"[\s\S]*?<\/div>/g;
    let match;
    while ((match = blockRegex.exec(content)) !== null) {
      blocks.push({
        full: match[0],
        index: match.index,
        hasStandardText: match[0].includes('PRACTICE THIS CHAPTER')
      });
    }

    if (blocks.length > 1) {
      console.log(`Cleaning up multiple blocks in: ${indexPath}`);
      
      // If we have a standardized one, remove all NON-standardized ones that point to the SAME exercise
      const standardized = blocks.find(b => b.hasStandardText);
      if (standardized) {
        // Extract the link from the standardized one
        const linkMatch = standardized.full.match(/href="([^"]+)"/);
        if (linkMatch) {
          const standardLink = linkMatch[1];
          
          let newContent = content;
          blocks.forEach(b => {
            if (!b.hasStandardText) {
              const bLinkMatch = b.full.match(/href="([^"]+)"/);
              if (bLinkMatch && bLinkMatch[1] === standardLink) {
                console.log(`  Removing redundant block pointing to ${standardLink}`);
                newContent = newContent.replace(b.full, '');
              }
            }
          });
          
          // Also, if there are multiple standardized ones (unlikely), keep only the last one
          const allStandardized = blocks.filter(b => b.hasStandardText);
          if (allStandardized.length > 1) {
            console.log(`  Removing duplicate standardized blocks`);
            for (let i = 0; i < allStandardized.length - 1; i++) {
              newContent = newContent.replace(allStandardized[i].full, '');
            }
          }

          fs.writeFileSync(indexPath, newContent, 'utf8');
        }
      }
    }
  });
});
