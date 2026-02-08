const fs = require('fs');
const path = require('path');

const TARGET_DIRS = [
    path.join(__dirname, '../classes/class-9/ncert-exercise-practice'),
    path.join(__dirname, '../classes/class-10/ncert-exercise-practice'),
    path.join(__dirname, '../classes/class-11/ncert-exercise-practice'),
    path.join(__dirname, '../classes/class-12/ncert-exercise-practice')
];

// SVG Definitions
const SVGS = {
    'clock': `<svg class="icon-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="16" height="16" fill="currentColor"><path d="M256,8C119,8,8,119,8,256S119,504,256,504,504,393,504,256,393,8,256,8Zm0,448c-110.5,0-200-89.5-200-200S145.5,56,256,56s200,89.5,200,200S366.5,456,256,456ZM369.1,343.9,278,252.8V128a24,24,0,0,0-48,0V264a24,24,0,0,0,7,17l96,96a24,24,0,0,0,33.9-33.9Z"/></svg>`,
    'eye': `<svg class="icon-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512" width="16" height="16" fill="currentColor"><path d="M288 32c-80.8 0-145.5 36.8-192.6 80.6C48.6 156 17.3 208 2.5 243.7c-3.3 7.9-3.3 16.7 0 24.6C17.3 304 48.6 356 95.4 399.4C142.5 443.2 207.2 480 288 480s145.5-36.8 192.6-80.6c46.8-43.5 78.1-95.4 93-131.1c3.3-7.9 3.3-16.7 0-24.6c-14.9-35.7-46.2-87.7-93-131.1C433.5 68.8 368.8 32 288 32zM144 256a144 144 0 1 1 288 0 144 144 0 1 1 -288 0zm144-64c0 35.3-28.7 64-64 64c-7.1 0-13.9-1.2-20.3-3.3c-5.5-1.8-11.9 1.6-11.7 7.4c.3 6.9 1.3 13.8 3.2 20.7c13.7 51.2 66.4 81.6 117.6 67.9s81.6-66.4 67.9-117.6c-11.1-41.5-47.8-69.4-88.6-71.1c-5.8-.2-9.2 6.1-7.4 11.7c2.1 6.4 3.3 13.2 3.3 20.3z"/></svg>`,
    'arrow-right': `<svg class="icon-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" width="16" height="16" fill="currentColor"><path d="M438.6 278.6c12.5-12.5 12.5-32.8 0-45.3l-160-160c-12.5-12.5-32.8-12.5-45.3 0s-12.5 32.8 0 45.3L338.8 224 32 224c-17.7 0-32 14.3-32 32s14.3 32 32 32l306.7 0L233.4 393.4c-12.5 12.5-12.5 32.8 0 45.3s32.8 12.5 45.3 0l160-160z"/></svg>`,
    'arrow-left': `<svg class="icon-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" width="16" height="16" fill="currentColor"><path d="M9.4 233.4c-12.5 12.5-12.5 32.8 0 45.3l160 160c12.5 12.5 32.8 12.5 45.3 0s12.5 32.8 0-45.3L109.2 288 416 288c17.7 0 32-14.3 32-32s-14.3-32-32-32l-306.7 0L214.6 118.6c12.5-12.5 12.5-32.8 0-45.3s-32.8-12.5-45.3 0l-160 160z"/></svg>`,
    'book': `<svg class="icon-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" width="16" height="16" fill="currentColor"><path d="M96 0C43 0 0 43 0 96V416c0 53 43 96 96 96H384h32c17.7 0 32-14.3 32-32s-14.3-32-32-32V384c17.7 0 32-14.3 32-32V32c0-17.7-14.3-32-32-32H384 96zm0 384H352v64H96c-17.7 0-32-14.3-32-32s14.3-32 32-32zm32-240c0-8.8 7.2-16 16-16H336c8.8 0 16 7.2 16 16s-7.2 16-16 16H144c-8.8 0-16-7.2-16-16zm0 64c0-8.8 7.2-16 16-16H336c8.8 0 16 7.2 16 16s-7.2 16-16 16H144c-8.8 0-16-7.2-16-16zm0 64c0-8.8 7.2-16 16-16H336c8.8 0 16 7.2 16 16s-7.2 16-16 16H144c-8.8 0-16-7.2-16-16z"/></svg>`,
    'th-large': `<svg class="icon-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="16" height="16" fill="currentColor"><path d="M448 32H64C28.65 32 0 60.65 0 96v320c0 35.35 28.65 64 64 64h384c35.35 0 64-28.65 64-64V96c0-35.35-28.65-64-64-64zm-304 96c0-8.84 7.16-16 16-16h80c8.84 0 16 7.16 16 16v80c0 8.84-7.16 16-16 16h-80c-8.84 0-16-7.16-16-16v-80zm0 192c0-8.84 7.16-16 16-16h80c8.84 0 16 7.16 16 16v80c0 8.84-7.16 16-16 16h-80c-8.84 0-16-7.16-16-16v-80zm192 16h-80c-8.84 0-16-7.16-16-16v-80c0-8.84 7.16-16 16-16h80c8.84 0 16 7.16 16 16v80c0 8.84-7.16 16-16 16zm0-192h-80c-8.84 0-16-7.16-16-16v-80c0-8.84 7.16-16 16-16h80c8.84 0 16 7.16 16 16v80c0 8.84-7.16 16-16 16z"/></svg>`
};

const KATEX_BLOCK = `    <!-- KaTeX: Faster Math Rendering -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css" integrity="sha384-n8MVd4RsNIU0tAv4ct0nTaAbDJwPJzDEaqSD1odI+WdtXRGWt2kTvGFasHpSy3SV" crossorigin="anonymous">
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js" integrity="sha384-XjKyFAMyFwxDDclqDNZR/hdUsw1WmvFiW58NVKtq9gu9XL1s1bUhv/0607fWE4W4" crossorigin="anonymous"></script>
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" integrity="sha384-+VBxd3r6XgURycqtZ117nYw44OOcIax56Z4dCRWbxyPt0Koah1uHoK0o4+/RRE05" crossorigin="anonymous"
        onload="renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '$', right: '$', display: false}]});"></script>`;

function getAllFiles(dirPath, arrayOfFiles) {
    const files = fs.readdirSync(dirPath);
    arrayOfFiles = arrayOfFiles || [];

    files.forEach(function (file) {
        if (fs.statSync(path.join(dirPath, file)).isDirectory()) {
            arrayOfFiles = getAllFiles(path.join(dirPath, file), arrayOfFiles);
        } else {
            if (file.endsWith(".html")) {
                arrayOfFiles.push(path.join(dirPath, file));
            }
        }
    });

    return arrayOfFiles;
}

function processFile(filePath) {
    let content = fs.readFileSync(filePath, 'utf8');
    let original = content;

    // 1. Remove FontAwesome Links (Force remove even if duplicates exist)
    content = content.replace(/<link[^>]*href="[^"]*font-awesome[^"]*"[^>]*>/gi, '');
    content = content.replace(/<noscript>[\s\S]*?font-awesome[\s\S]*?<\/noscript>/gi, '');

    // 2. Remove MathJax (Force remove independent of KaTeX existence)
    // Remove specific script src tags even if multiline
    content = content.replace(/<script[^>]*MathJax[^>]*>[\s\S]*?<\/script>/gi, '');
    // Remove inline config blocks
    content = content.replace(/<script>[\s\S]*?window\.MathJax[\s\S]*?<\/script>/gi, '');
    content = content.replace(/window\.MathJax\s*=\s*{[\s\S]*?};/g, '');

    // 3. Add KaTeX if missing
    if (!content.includes('katex.min.css')) {
        content = content.replace('</head>', () => `${KATEX_BLOCK}\n</head>`);
    }

    // 4. Replace Icons (Force replace remaining icons)
    content = content.replace(/<i class="fas fa-clock"><\/i>/g, SVGS['clock']);
    content = content.replace(/<i class="fas fa-eye"><\/i>/g, SVGS['eye']);
    content = content.replace(/<i class="fas fa-arrow-right"><\/i>/g, SVGS['arrow-right']);
    content = content.replace(/<i class="fas fa-arrow-left"><\/i>/g, SVGS['arrow-left']);
    content = content.replace(/<i class="fas fa-book"><\/i>/g, SVGS['book']);
    content = content.replace(/<i class="fas fa-th-large"><\/i>/g, SVGS['th-large']);

    // Cleanup empty lines
    content = content.replace(/^\s*[\r\n]/gm, '');

    if (content !== original) {
        fs.writeFileSync(filePath, content, 'utf8');
        console.log(`Fixed: ${path.basename(filePath)}`);
    } else {
        // console.log(`Clean: ${path.basename(filePath)}`);
    }
}

// Run
TARGET_DIRS.forEach(dir => {
    if (fs.existsSync(dir)) {
        console.log(`Processing Directory: ${dir}`);
        const files = getAllFiles(dir);
        console.log(`Found ${files.length} HTML files.`);
        files.forEach(processFile);
        console.log(`Finished ${path.basename(path.dirname(dir))}\n`);
    } else {
        console.warn(`Directory not found: ${dir}`);
    }
});
console.log('All classes optimized.');
