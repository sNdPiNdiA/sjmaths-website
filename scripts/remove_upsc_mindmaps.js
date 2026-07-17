const fs = require('fs');
const path = require('path');

const upscDir = path.join(__dirname, '..', 'upsc');

function removeMindmaps(filePath) {
    let content = fs.readFileSync(filePath, 'utf8');
    let modified = false;

    // Remove mindmap CSS link (with various query string versions)
    content = content.replace(/<link rel="stylesheet" href="\/assets\/css\/mindmap\.min\.css\?v=[^"]*">\n?/g, '');

    // Remove mindmap-engine script tag
    content = content.replace(/<script src="\/assets\/js\/mindmap-engine\.min\.js\?v=[^"]*"><\/script>\n?/g, '');

    // Remove renderMindmap script block
    content = content.replace(/<script>\s*renderMindmap\([^<]+\);?\s*<\/script>\n?/g, '');

    // Remove noscript mindmap fallback
    content = content.replace(/<noscript class="noscript-mindmap">[\s\S]*?<\/noscript>\n?/g, '');

    // Remove the entire Interactive Mindmap section (including <!-- Interactive Mindmap --> comment and surrounding divs)
    content = content.replace(/<!-- Interactive Mindmap -->\n\s*<div class="card-premium" id="mindmap-card">[\s\S]*?<\/div>\n\s*<div id="prehistory-mindmap-container">[\s\S]*?<\/div>\n/g, '');

    // Clean up any remaining mindmap-container divs that might be orphaned
    content = content.replace(/<div id="prehistory-mindmap-container">\n<\/div>\n/g, '');

    // Update meta descriptions removing "interactive mindmaps, " prefix
    content = content.replace(/content="Explore interactive mindmaps, /g, 'content="Explore ');
    content = content.replace(/content="Explore interactive mindmaps, revision notes, and /g, 'content="Explore revision notes, and ');

    // Update JSON-LD learningResourceType
    content = content.replace(/"learningResourceType": "Mindmap \/ Revision Notes"/g, '"learningResourceType": "Study Notes"');

    // Update body text references
    content = content.replace(/interactive mindmaps/g, 'study notes');

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
            if (removeMindmaps(itemPath)) {
                filesModified++;
                console.log(`Modified: ${itemPath}`);
            }
        }
    }

    return { processed: filesProcessed, modified: filesModified };
}

console.log('Starting mindmap removal from UPSC files...');
const results = processDirectory(upscDir);
console.log(`\nComplete!`);
console.log(`Files processed: ${results.processed}`);
console.log(`Files modified: ${results.modified}`);