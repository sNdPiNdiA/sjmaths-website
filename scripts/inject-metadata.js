const fs = require('fs');
const path = require('path');
const { promisify } = require('util');

const readdir = promisify(fs.readdir);
const stat = promisify(fs.stat);
const readFile = promisify(fs.readFile);
const writeFile = promisify(fs.writeFile);

const ROOT_DIR = path.resolve(__dirname, '../');
const CLASSES_DIR = path.join(ROOT_DIR, 'classes');

async function getFiles(dir) {
    const subdirs = await readdir(dir);
    const files = await Promise.all(subdirs.map(async (subdir) => {
        const res = path.resolve(dir, subdir);
        return (await stat(res)).isDirectory() ? getFiles(res) : res;
    }));
    return files.flat();
}

function generateDescription(content, filename) {
    // Extract H1
    const h1Match = content.match(/<h1>(.*?)<\/h1>/i);
    const h1 = h1Match ? h1Match[1].replace(/<[^>]*>/g, '').trim() : '';

    // Extract Title
    const titleMatch = content.match(/<title>(.*?)<\/title>/i);
    const title = titleMatch ? titleMatch[1].replace(/<[^>]*>/g, '').trim() : '';

    // Determine Class and Chapter from path
    // path: .../classes/class-10/chapter-wise-notes/chapter-1-real-numbers/...
    // path: .../classes/class-10/ncert-exercise-practice/chapter-1-real-numbers/exercise-1-1.html

    let parts = filename.split(path.sep);
    let classPart = parts.find(p => p.includes('class-'));
    let chapterPart = parts.find(p => p.includes('chapter-'));
    let exercisePart = parts.find(p => p.includes('exercise-') && p.endsWith('.html'));

    let className = classPart ? classPart.replace('class-', 'Class ') : 'Class 10';
    let chapterName = chapterPart ? chapterPart.replace('chapter-', 'Chapter ').replace(/-/g, ' ') : '';
    // Capitalize chapter name
    chapterName = chapterName.replace(/\b\w/g, l => l.toUpperCase());

    if (filename.includes('exercise')) {
        let exerciseName = exercisePart ? exercisePart.replace('exercise-', 'Exercise ').replace('.html', '') : 'Exercise';
        return `Free NCERT Solutions for ${className} Maths ${chapterName} ${exerciseName}. Step-by-step explained answers for CBSE Board exams. Download PDF and practice now.`;
    } else if (filename.includes('notes')) {
        return `${className} Maths ${chapterName} Notes. Comprehensive revision notes, formulas, and key concepts for CBSE Board Exams.`;
    } else {
        // generic
        return `${h1 || title} - Free study material for ${className} Maths. NCERT Solutions, Notes, and PYQs.`;
    }
}

async function injectMetadata() {
    console.log('Starting Metadata Injection...');
    const allFiles = await getFiles(CLASSES_DIR);
    const htmlFiles = allFiles.filter(f => f.endsWith('.html'));

    let updatedCount = 0;
    let skippedCount = 0;

    for (const file of htmlFiles) {
        let content = await readFile(file, 'utf8');

        // Check for existing description
        const metaDescRegex = /<meta\s+name=["']description["']\s+content=["'](.*?)["']\s*\/?>/i;
        const match = content.match(metaDescRegex);

        if (match && match[1] && match[1].length > 10) {
            console.log(`Skipping (Existing SEO): ${path.basename(file)}`);
            skippedCount++;
            continue;
        }

        const newDesc = generateDescription(content, file);
        const metaTag = `<meta name="description" content="${newDesc}">`;

        // Inject into <head>
        // Try to insert after <meta charset> or <title> or <head>

        if (content.includes('<meta charset')) {
            content = content.replace(/(<meta charset[^>]*>)/i, `$1\n    ${metaTag}`);
        } else if (content.includes('<title>')) {
            content = content.replace(/(<title>.*?<\/title>)/i, `$1\n    ${metaTag}`);
        } else if (content.includes('<head>')) {
            content = content.replace('<head>', `<head>\n    ${metaTag}`);
        } else {
            console.warn(`Could not find <head> in ${file}`);
            continue;
        }

        await writeFile(file, content, 'utf8');
        console.log(`Updated: ${path.basename(file)}`);
        updatedCount++;
    }

    console.log(`Metadata Injection Complete. Updated: ${updatedCount}, Skipped: ${skippedCount}`);
}

injectMetadata().catch(console.error);
