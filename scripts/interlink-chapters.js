const fs = require('fs');
const path = require('path');
const { promisify } = require('util');

const readdir = promisify(fs.readdir);
const readFile = promisify(fs.readFile);
const writeFile = promisify(fs.writeFile);
const stat = promisify(fs.stat);

const ROOT_DIR = path.resolve(__dirname, '../');
const CLASSES_DIR = path.join(ROOT_DIR, 'classes');

// Helper: Recursive file scanner
async function getFiles(dir) {
    const subdirs = await readdir(dir);
    const files = await Promise.all(subdirs.map(async (subdir) => {
        const res = path.resolve(dir, subdir);
        return (await stat(res)).isDirectory() ? getFiles(res) : res;
    }));
    return files.flat();
}

async function interlinkChapters() {
    console.log('Starting Internal Linking Injection...');
    const allFiles = await getFiles(CLASSES_DIR);
    const htmlFiles = allFiles.filter(f => f.endsWith('.html'));

    let notesUpdated = 0;
    let exercisesUpdated = 0;

    for (const file of htmlFiles) {
        let content = await readFile(file, 'utf8');
        let modified = false;

        // DETERMINE CONTEXT
        const isNotePage = file.includes('chapter-wise-notes') && file.endsWith('index.html');
        // Exercise pages are usually exercise-1-1.html etc inside ncert-exercise-practice
        const isExercisePage = file.includes('ncert-exercise-practice') && file.includes('exercise-');

        if (isNotePage) {
            // Logic: Link to Practice Exercises
            // Path: classes/class-X/chapter-wise-notes/chapter-Y/index.html
            // Target: classes/class-X/ncert-exercise-practice/chapter-Y/index.html

            // Check duplications
            if (content.includes('id="related-exercises"')) continue;

            const currentChapterDir = path.basename(path.dirname(file)); // chapter-1-real-numbers
            const classDir = path.dirname(path.dirname(path.dirname(file))); // classes/class-10

            // Construct target path
            const targetRelPath = `../../ncert-exercise-practice/${currentChapterDir}/index.html`;
            const targetAbsPath = path.resolve(path.dirname(file), targetRelPath);

            if (fs.existsSync(targetAbsPath)) {
                console.log(`Linking Note -> Exercise: ${currentChapterDir}`);

                const linkBlock = `
    <!-- Related Content Link -->
    <section id="related-exercises" class="box-pyq" style="text-align: center; margin-top: 40px;">
        <h3><i class="fas fa-pen-nib"></i> Ready to Practice?</h3>
        <p>Apply these concepts by solving NCERT Exercises.</p>
        <a href="${targetRelPath}" class="nav-btn">Go to NCERT Solutions <i class="fas fa-arrow-right"></i></a>
    </section>
`;
                // Inject before the main closing tag or before footer
                if (content.includes('</main>')) {
                    content = content.replace('</main>', `${linkBlock}\n</main>`);
                    modified = true;
                    notesUpdated++;
                }
            }
        }



        const isExemplarPage = file.includes('ncert-exemplar-practice') && file.endsWith('.html') && !file.endsWith('index.html');

        if (isExercisePage || isExemplarPage) {
            // Logic: Link BACK to Notes (Concept Revision)
            // Path: classes/class-X/ncert-exercise-practice/chapter-Y/exercise-1-1.html
            // Target: classes/class-X/chapter-wise-notes/chapter-Y/index.html

            // Check duplications
            if (content.includes('class="floating-notes-link"')) continue;

            const currentChapterDir = path.basename(path.dirname(file));
            const targetRelPath = `../../chapter-wise-notes/${currentChapterDir}/index.html`;
            const targetAbsPath = path.resolve(path.dirname(file), targetRelPath);

            if (fs.existsSync(targetAbsPath)) {
                // We want this unobtrusive, maybe near the top title or floating
                // Let's add it right after the H1 title for visibility
                console.log(`Linking Exercise/Exemplar -> Note: ${path.basename(file)}`);

                const noteLink = `
    <div class="floating-notes-link" style="margin-bottom: 20px; text-align: center;">
        <a href="${targetRelPath}" style="color: var(--primary); font-weight: 600; text-decoration: none;">
            <i class="fas fa-book-open"></i> Revise Chapter Notes
        </a>
    </div>
`;
                // Inject after H1
                if (content.match(/<h1>.*?<\/h1>/i)) {
                    content = content.replace(/(<h1>.*?<\/h1>)/i, `$1\n${noteLink}`);
                    modified = true;
                    exercisesUpdated++;
                }
            }
        }

        if (modified) {
            await writeFile(file, content, 'utf8');
        }
    }

    console.log(`\nExternal Linking Complete.`);
    console.log(`Notes Updated: ${notesUpdated}`);
    console.log(`Exercises Updated: ${exercisesUpdated}`);
}

interlinkChapters().catch(console.error);
