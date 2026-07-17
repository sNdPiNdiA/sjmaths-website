const fs = require('fs');
const path = require('path');

const upscDir = path.join(__dirname, '..', 'upsc');

function aggressiveCleanup(filePath) {
    let content = fs.readFileSync(filePath, 'utf8');
    let modified = false;

    // Remove ALL mindmap-card div blocks (English and Hindi) - handle various formats
    content = content.replace(/<div class="card-premium" id="mindmap-card(-hi)?">[\s\S]*?<\/div>\n/g, '');

    // Remove any remaining renderMindmap script blocks (English and Hindi)
    content = content.replace(/<script>\s*renderMindmap\([^<]+\);\s*<\/script>\n?/g, '');
    content = content.replace(/<script>\s*renderMindmap\([^<]+\);\s*\n\s*<\/script>\n?/g, '');

    // Remove mindmap-engine script tags
    content = content.replace(/<script src="\/assets\/js\/mindmap-engine\.min\.js\?v=[^"]*"><\/script>\n?/g, '');

    // Remove mindmap CSS links
    content = content.replace(/<link rel="stylesheet" href="\/assets\/css\/mindmap\.min\.css\?v=[^"]*">\n?/g, '');

    // Remove noscript mindmap fallback blocks
    content = content.replace(/<noscript class="noscript-mindmap">[\s\S]*?<\/noscript>\n?/g, '');

    // Remove "Interactive Mindmap" text from titles and headings (various formats)
    content = content.replace(/ — Interactive Mindmap/g, '');
    content = content.replace(/ &mdash; Interactive Mindmap/g, '');
    content = content.replace(/ — इंटरैक्टिव माइंडमैप/g, '');
    content = content.replace(/ &mdash; इंटरैक्टिव माइंडमैप/g, '');

    // Remove "Interactive Mindmap" comments
    content = content.replace(/\s*<!-- Interactive Mindmap -->\s*/g, '\n');

    // Remove empty mindmap container divs
    content = content.replace(/<div id="prehistory-mindmap-container(-hi)?">\s*<\/div>\n?/g, '');

    // Remove any remaining empty card-premium divs with mindmap in id
    content = content.replace(/<div class="card-premium" id="mindmap-card(-hi)?">\s*<\/div>\n?/g, '');

    // Clean up multiple consecutive blank lines
    content = content.replace(/\n{3,}/g, '\n\n');

    // Remove trailing whitespace
    content = content.replace(/[ \t]+$/gm, '');

    if (content !== fs.readFileSync(filePath, 'utf8')) {
        fs.writeFileSync(filePath, content, 'utf8');
        modified = true;
    }

    return modified;
}

function processDirectory(dir) {
    let filesProcessed = 0;
    let filesModified = 0;

    const items = fs.readdirSync(dir);

    for (const item of items) {
        const itemPath = path.join(dir, item);
        const stat = fs.statSync(itemPath);

        if (stat.isDirectory()) {
            const subResults = processDirectory(itemPath);
            filesProcessed += subResults.processed;
            filesModified += subResults.modified;
        } else if (item.endsWith('.html')) {
            filesProcessed++;
            if (aggressiveCleanup(itemPath)) {
                filesModified++;
                console.log(`Removed: ${itemPath}`);
            }
        }
    }

    return { processed: filesProcessed, modified: filesModified };
}

console.log('Starting AGGRESSIVE removal of ALL mindmap elements from UPSC files...');
const results = processDirectory(upscDir);
console.log(`\nComplete!`);
console.log(`Files processed: ${results.processed}`);
console.log(`Files modified: ${results.modified}`);