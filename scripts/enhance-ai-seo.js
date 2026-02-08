const fs = require('fs');
const path = require('path');
const { promisify } = require('util');

const readdir = promisify(fs.readdir);
const stat = promisify(fs.stat);
const readFile = promisify(fs.readFile);
const writeFile = promisify(fs.writeFile);

const ROOT_DIR = path.resolve(__dirname, '../');
const CLASSES_DIR = path.join(ROOT_DIR, 'classes');

// Helper: Get all files
async function getFiles(dir) {
    const subdirs = await readdir(dir);
    const files = await Promise.all(subdirs.map(async (subdir) => {
        const res = path.resolve(dir, subdir);
        return (await stat(res)).isDirectory() ? getFiles(res) : res;
    }));
    return files.flat();
}

// Helper: Generate Content for Summary
function generateSummaryContent(content, filename) {
    let parts = filename.split(path.sep);
    let classPart = parts.find(p => p.includes('class-'));
    let chapterPart = parts.find(p => p.includes('chapter-'));

    let className = classPart ? classPart.replace('class-', 'Class ') : 'Class 10';
    let chapterName = chapterPart ? chapterPart.replace('chapter-', 'Chapter ').replace(/-/g, ' ') : 'Mathematics';
    chapterName = chapterName.replace(/\b\w/g, l => l.toUpperCase()); // Title Case

    // Custom fix for "Chapter 1 Real Numbers" -> "Real Numbers"
    if (chapterName.toLowerCase().startsWith('chapter')) {
        // keep it as is, or strip number? Usually "Chapter 1 Real Numbers" is fine.
    }

    // Extract Topics from "Cards"
    // Strategies:
    // 1. .step-card h3 (Chapter Notes)
    // 2. .feature-card h2 (Class Index)
    // 3. .card h3 (Generic)
    // 4. h2 (Fall back)

    let topics = [];

    // Regex for specific card headers
    const cardRegex = /<(?:div|a)[^>]*class=["'](?:.*?)?(?:step-card|feature-card|card)(?:.*?)?["'][^>]*>[\s\S]*?<h[23][^>]*>(.*?)<\/h[23]>/gi;
    let match;
    while ((match = cardRegex.exec(content)) !== null) {
        let text = match[1].replace(/<[^>]*>/g, '').trim();
        if (text && !topics.includes(text)) topics.push(text);
    }

    // Fallback if no cards found (e.g. exercise pages might just have H2s)
    if (topics.length === 0) {
        const h2Regex = /<h2>(?!<i)(.*?)<\/h2>/gi; // Avoid icons if possible, though strip tags handles it
        while ((match = h2Regex.exec(content)) !== null) {
            let text = match[1].replace(/<[^>]*>/g, '').trim();
            // Filter keywords
            if (text && !text.match(/Question|Exam|Overview|Summary|Menu|Quick Nav/i) && !topics.includes(text)) {
                topics.push(text);
            }
        }
    }

    // Limit to top 5-6 topics to keep it concise but comprehensive
    const maxTopics = 8;
    let topicString = '';
    if (topics.length > 0) {
        const selectedTopics = topics.slice(0, maxTopics);
        topicString = `Key topics covered: <strong>${selectedTopics.join(', ')}</strong>.`;
    } else {
        topicString = 'Topics covered include key concepts, formulas, and problem-solving techniques.';
    }

    return `This page provides an <strong>Overview</strong> of <strong>${chapterName}</strong> for CBSE <strong>${className}</strong>. ${topicString} All content is aligned with the NCERT syllabus for Board Exam preparation.`;
}

async function enhanceAISEO() {
    console.log('Starting AI SEO Refinement (Overview)...');
    const allFiles = await getFiles(CLASSES_DIR);
    const htmlFiles = allFiles.filter(f => f.endsWith('.html'));

    let updatedCount = 0;

    for (const file of htmlFiles) {
        let content = await readFile(file, 'utf8');
        let modified = false;

        const summaryText = generateSummaryContent(content, file);
        const newSummaryBlock = `
    <!-- AI Summary Block -->
    <section class="ai-summary">
        <h2><i class="fas fa-list-ul"></i> Overview</h2>
        <p>${summaryText}</p>
    </section>
`;

        // Check if .ai-summary exists
        if (content.includes('class="ai-summary"')) {
            // Replace existing block
            // Regex to match the entire section
            const blockRegex = /<section class="ai-summary">[\s\S]*?<\/section>/;
            if (blockRegex.test(content)) {
                content = content.replace(blockRegex, newSummaryBlock.trim());
                modified = true;
                updatedCount++;
            }
        } else {
            // Inject new if missing (fallback)
            if (content.match(/<h1>.*?<\/h1>/i)) {
                content = content.replace(/(<h1>.*?<\/h1>)/i, `$1\n${newSummaryBlock}`);
                modified = true;
                updatedCount++;
            }
        }

        if (modified) {
            await writeFile(file, content, 'utf8');
        }
    }

    console.log(`Refinement Complete. Updated ${updatedCount} pages with 'Chapter Overview'.`);
}

enhanceAISEO().catch(console.error);
