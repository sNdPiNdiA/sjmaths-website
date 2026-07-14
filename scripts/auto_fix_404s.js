const fs = require('fs');
const data = require('../404_summary.json');
const path = require('path');

const sources = {};
Object.entries(data.missingLinks).forEach(([link, arr]) => {
    arr.forEach(src => {
        if (!sources[src]) sources[src] = [];
        sources[src].push(link);
    });
});

let totalFixed = 0;

for (const [file, brokenLinks] of Object.entries(sources)) {
    const filePath = path.join(__dirname, '..', file);
    if (!fs.existsSync(filePath)) continue;

    let content = fs.readFileSync(filePath, 'utf8');
    let fixed = 0;

    for (let badLink of brokenLinks) {
        // Escape special regex chars in badLink
        const escapedLink = badLink.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
        
        const hrefRegex = new RegExp(`href=["']${escapedLink}["']`, 'g');
        if (hrefRegex.test(content)) {
            content = content.replace(hrefRegex, 'href="#"');
            fixed++;
        }
        
        const srcRegex = new RegExp(`src=["']${escapedLink}["']`, 'g');
        if (srcRegex.test(content)) {
            // For scripts/images, use a tiny data URI to prevent actual network requests
            content = content.replace(srcRegex, 'src="data:,"');
            fixed++;
        }
    }

    if (fixed > 0) {
        fs.writeFileSync(filePath, content, 'utf8');
        console.log(`Fixed ${fixed} links in ${file}`);
        totalFixed += fixed;
    }
}

console.log(`Total automatically fixed: ${totalFixed}`);
