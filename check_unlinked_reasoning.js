const fs = require('fs');
const path = require('path');

const baseDir = 'c:/Users/sande/Documents/GitHub/sjmaths-website/ssc-cgl/reasoning';
const allFilesDirs = [];

function scanDir(dir) {
    const items = fs.readdirSync(dir);
    for (const item of items) {
        const fullPath = path.join(dir, item);
        if (fs.statSync(fullPath).isDirectory()) {
            const indexPath = path.join(fullPath, 'index.html');
            if (fs.existsSync(indexPath)) {
                const rel = path.relative(baseDir, fullPath).replace(/\\/g, '/');
                allFilesDirs.push({ relPath: rel, indexPath: indexPath });
            }
            scanDir(fullPath);
        }
    }
}
scanDir(baseDir);

let trackedTopics;
try {
    trackedTopics = JSON.parse(fs.readFileSync('reasoning_topics.json', 'utf8'));
} catch (error) {
    console.error("Error reading or parsing reasoning_topics.json. Make sure the file exists and is valid JSON.", error.message);
    process.exit(1);
}

console.log('Total index.html directories found in ssc-cgl/reasoning:', allFilesDirs.length);
console.log('Total topics in syllabus tracker (reasoning_topics.json):', trackedTopics.length);

const unlinkedDirs = [];
allFilesDirs.forEach(d => {
    if (!trackedTopics.includes(d.relPath)) {
        const content = fs.readFileSync(d.indexPath, 'utf8');
        unlinkedDirs.push({ relPath: d.relPath, size: content.length });
    }
});

console.log('\n=== DIRECTORIES IN ssc-cgl/reasoning NOT IN SYLLABUS TRACKER (' + unlinkedDirs.length + ') ===');
unlinkedDirs.forEach((u, i) => console.log((i+1) + '. ' + u.relPath + ' (Size: ' + u.size + ' bytes)'));
