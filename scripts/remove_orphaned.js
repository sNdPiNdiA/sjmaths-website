const fs = require('fs');
const path = require('path');

const indexContent = fs.readFileSync('upsc/index.html', 'utf8');
const upscDir = 'upsc';
const subjects = fs.readdirSync(upscDir).filter(f => fs.statSync(path.join(upscDir, f)).isDirectory());
const orphaned = [];

subjects.forEach(subject => {
    const subjectPath = path.join(upscDir, subject);
    const topics = fs.readdirSync(subjectPath).filter(f => fs.statSync(path.join(subjectPath, f)).isDirectory());
    
    topics.forEach(topic => {
        const relativePath = `./${subject}/${topic}/`;
        if (!indexContent.includes(relativePath)) {
            orphaned.push(path.join(subjectPath, topic));
        }
    });
});

console.log(`Found ${orphaned.length} orphaned directories. Deleting...`);

orphaned.forEach(dir => {
    try {
        fs.rmSync(dir, { recursive: true, force: true });
        console.log(`Deleted: ${dir}`);
    } catch (err) {
        console.error(`Error deleting ${dir}:`, err.message);
    }
});

console.log("Cleanup complete!");
