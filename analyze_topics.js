const fs = require('fs');
let content = fs.readFileSync('class-11-applied-mathematics/index.html', 'utf8');

// Extract all microtopics with their chapter association
// Pattern: data-grp-idx="X-cY" followed by syllabus-text links
const topicPattern = /data-grp-idx="(\d+-c\d+)"[\s\S]*?<ul class="syllabus-list">[\s\S]*?<li class="syllabus-item">[\s\S]*?<a href="[^"]*" class="topic-link syllabus-text">([^<]+)<\/a>/g;

let match;
const chaptersWithTopics = {};

while ((match = topicPattern.exec(content)) !== null) {
    const chapterKey = match[1];
    const topic = match[2].trim();

    if (!chaptersWithTopics[chapterKey]) {
        chaptersWithTopics[chapterKey] = [];
    }
    chaptersWithTopics[chapterKey].push(topic);
}

console.log('Microtopics per chapter:\n');
for (const [key, topics] of Object.entries(chaptersWithTopics)) {
    console.log(`\n${key}:`);
    topics.forEach(t => console.log(`  - ${t}`));
}

fs.writeFileSync('topics_per_chapter.json', JSON.stringify(chaptersWithTopics, null, 2));
console.log('\n\nSaved to topics_per_chapter.json');