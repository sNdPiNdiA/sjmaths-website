const fs = require('fs');
const path = require('path');

const upscDir = path.join(__dirname, '..', 'upsc');

function removeMindmapLines(filePath) {
    let lines = fs.readFileSync(filePath, 'utf8').split(/\r?\n/);
    let modified = false;
    let newLines = [];
    let skipBlock = false;

    for (let i = 0; i < lines.length; i++) {
        const line = lines[i];

        // Check if this line starts a mindmap block
        if (line.includes('mindmap-card') ||
            line.includes('renderMindmap') ||
            line.includes('mindmap-engine') ||
            line.includes('mindmap.min.css') ||
            line.includes('prehistory-mindmap-container') ||
            line.includes('noscript-mindmap') ||
            line.includes('Interactive Mindmap') ||
            line.includes('इंटरैक्टिव माइंडमैप')) {

            // If it's a renderMindmap, skip until we find the closing </script>
            if (line.includes('renderMindmap')) {
                skipBlock = true;
                modified = true;
                continue;
            }

            // If it's a noscript block, skip until we find </noscript>
            if (line.includes('noscript-mindmap')) {
                skipBlock = true;
                modified = true;
                continue;
            }

            // Skip this line
            modified = true;
            continue;
        }

        // If we're in a skip block, check if we should end it
        if (skipBlock) {
            if (line.includes('</script>') || line.includes('</noscript>')) {
                skipBlock = false;
                modified = true;
            }
            continue;
        }

        // Keep the line
        newLines.push(line);
    }

    if (modified) {
        const newContent = newLines.join('\n');
        fs.writeFileSync(filePath, newContent, 'utf8');
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
            if (removeMindmapLines(itemPath)) {
                filesModified++;
                console.log(`Cleaned: ${itemPath}`);
            }
        }
    }

    return { processed: filesProcessed, modified: filesModified };
}

console.log('Starting LINE-BASED removal of ALL mindmap elements from UPSC files...');
const results = processDirectory(upscDir);
console.log(`\nComplete!`);
console.log(`Files processed: ${results.processed}`);
console.log(`Files modified: ${results.modified}`);