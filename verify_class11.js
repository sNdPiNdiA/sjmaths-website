
const fs = require('fs');
const path = require('path');

const indexFile = path.join(__dirname, 'classes/class-11/ncert-exercise-practice/index.html');
const content = fs.readFileSync(indexFile, 'utf8');

// Regex to find hrefs starting with /classes/class-11/ncert-exercise-practice/
// Example: href="/classes/class-11/ncert-exercise-practice/chapter-1-sets/exercise-1-1.html"
const regex = /href="\/classes\/class-11\/ncert-exercise-practice\/([^"]+)"/g;
let match;
let errors = 0;
let count = 0;

console.log("Checking links in Class 11 index...");

// Clear previous log if exists
if (fs.existsSync('broken_links_11.txt')) {
    fs.unlinkSync('broken_links_11.txt');
}

while ((match = regex.exec(content)) !== null) {
    const relativePath = match[1];
    if (!relativePath) continue;

    // Skip self-reference or directory links if they end in / (though index.html usually implies a file check)
    if (relativePath === '' || relativePath.endsWith('/')) continue;

    const absolutePath = path.join(__dirname, 'classes/class-11/ncert-exercise-practice', relativePath);

    if (!fs.existsSync(absolutePath)) {
        // console.error(`[BROKEN LINK] ${relativePath}`);
        fs.appendFileSync('broken_links_11.txt', `[BROKEN] ${relativePath}\n`);
        errors++;
    } else {
        // console.log(`[OK] ${relativePath}`);
    }
    count++;
}

console.log(`Checked ${count} links.`);
if (errors === 0) {
    console.log("All links verified successfully!");
} else {
    console.log(`Found ${errors} broken links. Check broken_links_11.txt`);
}
