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
        // We look for either href="./subject/topic/" or href="./subject/topic/some-subtopic/"
        // A simple check is if the string `./subject/topic/` is anywhere in the file.
        const relativePath = `./${subject}/${topic}/`;
        if (!indexContent.includes(relativePath)) {
            orphaned.push(path.join(subjectPath, topic));
        }
    });
});

console.log(JSON.stringify(orphaned, null, 2));
