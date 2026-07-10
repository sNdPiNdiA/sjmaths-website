const fs = require('fs');
let fileContent = fs.readFileSync('upsssc-lower-mains/index.html', 'utf8');

// Replace all instances of 'syllabus-link syllabus-text' with 'topic-link syllabus-text'
let updatedContent = fileContent.replace(/class="syllabus-link syllabus-text"/g, 'class="topic-link syllabus-text"');

fs.writeFileSync('upsssc-lower-mains/index.html', updatedContent, 'utf8');
console.log('Replaced syllabus-link with topic-link');
