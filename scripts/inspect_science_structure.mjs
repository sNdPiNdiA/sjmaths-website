import fs from 'fs';
import path from 'path';

const htmlHub = fs.readFileSync(path.join(process.cwd(), 'up-upper-primary-teacher', 'science', 'index.html'), 'utf8');
const regex = /href="\/up-upper-primary-teacher\/science\/([a-zA-Z0-9\-_]+)\/?"/g;
const linkedSlugs = new Set();
let m;
while ((m = regex.exec(htmlHub)) !== null) {
    if (m[1]) linkedSlugs.add(m[1]);
}

const officialTopics = Array.from(linkedSlugs);
console.log(`\n=== OFFICIAL 34 TOPICS (Linked in science/index.html) ===`);
officialTopics.forEach((slug, idx) => {
    const fPath = path.join(process.cwd(), 'up-upper-primary-teacher', 'science', slug, 'index.html');
    const exists = fs.existsSync(fPath);
    let title = 'N/A';
    let size = 0;
    if (exists) {
        const c = fs.readFileSync(fPath, 'utf8');
        size = c.length;
        const tm = c.match(/<title>(.*?)<\/title>/);
        if (tm) title = tm[1];
    }
    console.log(`${idx + 1}. [${slug}] (${(size / 1024).toFixed(1)} KB) -> ${title.substring(0, 70)}...`);
});

const baseDir = path.join(process.cwd(), 'up-upper-primary-teacher', 'science');
const entries = fs.readdirSync(baseDir, { withFileTypes: true }).filter(e => e.isDirectory()).map(e => e.name);
const otherTopics = entries.filter(s => !linkedSlugs.has(s));

console.log(`\n=== OTHER ${otherTopics.length} TOPIC DIRECTORIES ON DISK ===`);
otherTopics.forEach((slug, idx) => {
    const fPath = path.join(process.cwd(), 'up-upper-primary-teacher', 'science', slug, 'index.html');
    const exists = fs.existsSync(fPath);
    let size = 0;
    if (exists) {
        size = fs.readFileSync(fPath, 'utf8').length;
    }
    console.log(`${idx + 1}. [${slug}] (${(size / 1024).toFixed(1)} KB)`);
});
