const fs = require('fs');
const path = require('path');

const baseDir = 'c:\\Users\\sande\\Documents\\GitHub\\sjmaths-website\\classes\\class-9\\tests\\full-length-tests';
const files = [
    { name: 'model-test-1.json', targetMarks: 80, targetCount: 38 },
    { name: 'model-test-2.json', targetMarks: 80, targetCount: 38 },
    { name: 'test-1.json', targetMarks: 40, targetCount: 19 },
    { name: 'test-2.json', targetMarks: 40, targetCount: 19 },
    { name: 'test-3.json', targetMarks: 40, targetCount: 19 }
];

files.forEach(fileObj => {
    const file = fileObj.name;
    const content = JSON.parse(fs.readFileSync(path.join(baseDir, file), 'utf8'));
    let totalMarks = 0;
    content.questions.forEach(q => { totalMarks += q.marks; });

    const countMatch = content.questions.length === fileObj.targetCount;
    const marksMatch = totalMarks === fileObj.targetMarks;

    if (countMatch && marksMatch) {
        console.log(`[PASS] ${file}: ${totalMarks} Marks, ${content.questions.length} Qs`);
    } else {
        console.log(`[FAIL] ${file}: Marks=${totalMarks}/${fileObj.targetMarks}, Qs=${content.questions.length}/${fileObj.targetCount}`);
    }
});
