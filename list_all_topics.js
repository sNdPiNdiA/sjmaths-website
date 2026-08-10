const fs = require('fs');
let content;
try {
    content = fs.readFileSync('class-11-applied-mathematics/index.html', 'utf8');
} catch (error) {
    console.error("Error reading file: class-11-applied-mathematics/index.html. Make sure the file exists.", error.message);
    process.exit(1);
}

// Extract all chapters and their topics - simpler approach
const lines = content.split('\n');
const chaptersData = [];
let currentChapter = null;

for (let i = 0; i < lines.length; i++) {
    const line = lines[i];

    // Check for chapter start
    if (line.includes('subsection-title')) {
        const titleMatch = line.match(/<span class="subsection-title">([^<]+)<\/span>/);
        if (titleMatch) {
            if (currentChapter) {
                chaptersData.push(currentChapter);
            }
            currentChapter = {
                title: titleMatch[1].trim(),
                topics: []
            };
        }
    }

    // Check for topic links within syllabus-list
    if (currentChapter && line.includes('topic-link syllabus-text')) {
        const topicMatch = line.match(/>([^<]+)<\/a>/);
        if (topicMatch) {
            const topicText = topicMatch[1].trim();
            if (topicText) currentChapter.topics.push(topicText);
        }
    }
}

// Don't forget the last chapter
if (currentChapter) {
    chaptersData.push(currentChapter);
}

console.log('All Chapters and Topics:\n');
chaptersData.forEach((c, i) => {
    console.log(`\n${c.title} (${c.topics.length} topics):`);
    c.topics.forEach(t => console.log(`  • ${t}`));
});

fs.writeFileSync('all_topics.json', JSON.stringify(chaptersData, null, 2));
console.log('\n\nSaved to all_topics.json');