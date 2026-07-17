const fs = require('fs');
const path = require('path');

const upscDir = path.join(__dirname, '..', 'upsc');

function finalCleanup(filePath) {
    let content = fs.readFileSync(filePath, 'utf8');
    let modified = false;

    // Remove entire mindmap-card div blocks (English and Hindi variants) - more aggressive pattern
    content = content.replace(/<div class="card-premium" id="mindmap-card(-hi)?">[\s\S]*?<\/div>\n/g, '');

    // Remove renderMindmap script blocks (English and Hindi)
    content = content.replace(/<script>\s*renderMindmap\([^<]+\);\s*<\/script>\n?/g, '');

    // Remove mindmap-engine script tags
    content = content.replace(/<script src="\/assets\/js\/mindmap-engine\.min\.js\?v=[^"]*"><\/script>\n?/g, '');

    // Remove mindmap CSS links
    content = content.replace(/<link rel="stylesheet" href="\/assets\/css\/mindmap\.min\.css\?v=[^"]*">\n?/g, '');

    // Remove noscript mindmap fallback blocks
    content = content.replace(/<noscript class="noscript-mindmap">[\s\S]*?<\/noscript>\n?/g, '');

    // Remove "Interactive Mindmap" text from titles and headings
    content = content.replace(/ &mdash; Interactive Mindmap/g, '');
    content = content.replace(/ — Interactive Mindmap/g, '');

    // Remove standalone "Interactive Mindmap" comments
    content = content.replace(/\s*<!-- Interactive Mindmap -->\s*/g, '\n');

    // Remove empty mindmap container divs
    content = content.replace(/<div id="prehistory-mindmap-container(-hi)?">\s*<\/div>\n?/g, '');

    // Clean up multiple consecutive blank lines
    content = content.replace(/\n{3,}/g, '\n\n');

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
            if (finalCleanup(itemPath)) {
                filesModified++;
                console.log(`Final cleanup: ${itemPath}`);
            }
        }
    }

    return { processed: filesProcessed, modified: filesModified };
}

console.log('Starting FINAL cleanup of all mindmap elements in UPSC files...');
const results = processDirectory(upscDir);
console.log(`\nComplete!`);
console.log(`Files processed: ${results.processed}`);
console.log(`Files cleaned: ${results.modified}`);