const fs = require('fs');
const path = require('path');

const upscDir = path.join(__dirname, '..', 'upsc');

function cleanupRemainingMindmaps(filePath) {
    let content = fs.readFileSync(filePath, 'utf8');
    let modified = false;

    // Remove remaining <!-- Interactive Mindmap --> comments (standalone or with extra blank lines)
    content = content.replace(/\s*<!-- Interactive Mindmap -->\s*/g, '\n');

    // Remove remaining empty or near-empty mindmap-container divs
    content = content.replace(/<div id="prehistory-mindmap-container(-hi)?">\s*<\/div>\n?/g, '');

    // Remove mindmap-card divs (English and Hindi variants) - the entire card block
    content = content.replace(/<div class="card-premium" id="mindmap-card(-hi)?">[\s\S]*?<\/div>\n/g, '');

    // Remove any noscript mindmap fallback blocks that might remain
    content = content.replace(/<noscript class="noscript-mindmap">[\s\S]*?<\/noscript>\n?/g, '');

    // Remove standalone renderMindmap script tags that may remain
    content = content.replace(/<script>\s*renderMindmap\([^<]+\);\s*<\/script>\n?/g, '');

    // Remove mindmap-engine script tags that may remain
    content = content.replace(/<script src="\/assets\/js\/mindmap-engine\.min\.js\?v=[^"]*"><\/script>\n?/g, '');

    // Remove mindmap CSS links that may remain
    content = content.replace(/<link rel="stylesheet" href="\/assets\/css\/mindmap\.min\.css\?v=[^"]*">\n?/g, '');

    // Clean up multiple consecutive blank lines that may have been created
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
            if (cleanupRemainingMindmaps(itemPath)) {
                filesModified++;
                console.log(`Cleaned: ${itemPath}`);
            }
        }
    }

    return { processed: filesProcessed, modified: filesModified };
}

console.log('Starting cleanup of remaining mindmap fragments in UPSC files...');
const results = processDirectory(upscDir);
console.log(`\nComplete!`);
console.log(`Files processed: ${results.processed}`);
console.log(`Files cleaned: ${results.modified}`);