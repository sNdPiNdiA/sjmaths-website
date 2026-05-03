const fs = require('fs');
const path = require('path');

const ROOT_DIR = process.cwd();
const CLASSES = ['class-10-maths', 'class-11-maths', 'class-12-maths'];

function getChapterNumber(dirName) {
  const match = dirName.match(/chapter-(\d+)/i);
  return match ? match[1] : null;
}

function findFirstExercise(exerciseDir, chapterNum) {
  if (!fs.existsSync(exerciseDir)) return null;
  const files = fs.readdirSync(exerciseDir);
  let match = files.find(f => f.toLowerCase() === `exercise-${chapterNum}-1.html`);
  if (!match) match = files.find(f => f.toLowerCase() === `exercise-1.html`);
  if (!match) match = files.find(f => f.toLowerCase() === `exercise-${chapterNum}-01.html`);
  if (!match) match = files.find(f => /exercise-.*-1\.html/i.test(f));
  return match || null;
}

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
    
    // If it already has "PRACTICE THIS CHAPTER", skip
    if (content.includes('PRACTICE THIS CHAPTER')) {
      console.log(`Skipping (already has standardized CTA): ${indexPath}`);
      return;
    }

    const chapterNum = getChapterNumber(chap);
    const exerciseDir = path.join(ROOT_DIR, cls, 'ncert-exercise-practice', chap);
    const firstEx = findFirstExercise(exerciseDir, chapterNum);

    if (firstEx) {
      const exLink = `../../ncert-exercise-practice/${chap}/${firstEx}`;
      
      const ctaHtml = `
        <div class="practice-link-box" style="text-align: center; margin-bottom: 40px; margin-top: 20px;">
            <a href="${exLink}" class="slide-btn"
                style="background: var(--primary); color: white; text-decoration: none; display: inline-block; padding: 12px 24px; border-radius: 50px; font-weight: 600; box-shadow: 0 4px 15px rgba(0,0,0,0.2); transition: transform 0.2s;">
                <i class="fas fa-pen-fancy"></i> PRACTICE THIS CHAPTER
            </a>
        </div>
      `;

      // If there's an existing practice-link-box, we might want to replace it or add near it.
      // For simplicity, if </main> exists, put it before that.
      if (content.includes('</main>')) {
        content = content.replace('</main>', `${ctaHtml}\n    </main>`);
      } else if (content.includes('</body>')) {
        content = content.replace('</body>', `${ctaHtml}\n</body>`);
      }

      fs.writeFileSync(indexPath, content, 'utf8');
      console.log(`Standardized CTA: ${indexPath}`);
    } else {
      console.log(`No exercise found for: ${indexPath}`);
    }
  });
});
