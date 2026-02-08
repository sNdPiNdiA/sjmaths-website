/**
 * Check for broken exercise links in Class 10 index
 */
const fs = require('fs');
const path = require('path');

const baseDir = path.join(__dirname, '..', 'classes', 'class-10', 'ncert-exercise-practice');

const chapters = [
    { name: 'Real Numbers', folder: 'chapter-1-real-numbers', exercises: [1, 2] },
    { name: 'Polynomials', folder: 'chapter-2-polynomials', exercises: [1, 2] },
    { name: 'Pair of Linear Equations', folder: 'chapter-3-pair-of-linear-equations-in-two-variables', exercises: [1, 2, 3] },
    { name: 'Quadratic Equations', folder: 'chapter-4-quadratic-equations', exercises: [1, 2, 3] },
    { name: 'Arithmetic Progressions', folder: 'chapter-5-arithmetic-progressions', exercises: [1, 2, 3, 4] },
    { name: 'Triangles', folder: 'chapter-6-triangles', exercises: [1, 2, 3] },
    { name: 'Coordinate Geometry', folder: 'chapter-7-coordinate-geometry', exercises: [1, 2] },
    { name: 'Introduction to Trigonometry', folder: 'chapter-8-introduction-to-trigonometry', exercises: [1, 2, 3] },
    { name: 'Applications of Trigonometry', folder: 'chapter-9-applications-of-trigonometry', exercises: [1] },
    { name: 'Circles', folder: 'chapter-10-circles', exercises: [1, 2] },
    { name: 'Areas Related to Circles', folder: 'chapter-11-areas-related-to-circles', exercises: [1] },
    { name: 'Surface Areas and Volumes', folder: 'chapter-12-surface-areas-and-volumes', exercises: [1, 2] },
    { name: 'Statistics', folder: 'chapter-13-statistics', exercises: [1, 2, 3] },
    { name: 'Probability', folder: 'chapter-14-probability', exercises: [1] }
];

console.log('Checking Class 10 exercise links...\n');

let broken = [];
let valid = 0;

chapters.forEach((ch, i) => {
    const chNum = i + 1;
    ch.exercises.forEach(ex => {
        const fileName = `exercise-${chNum}-${ex}.html`;
        const filePath = path.join(baseDir, ch.folder, fileName);
        if (fs.existsSync(filePath)) {
            valid++;
            console.log(`✓ Ch${chNum} Ex${ex}: ${fileName}`);
        } else {
            broken.push({ chapter: chNum, name: ch.name, expected: fileName, folder: ch.folder });
            console.log(`✗ Ch${chNum} Ex${ex}: ${fileName} - MISSING!`);
        }
    });
});

console.log('\n========================================');
console.log(`Valid: ${valid} | Broken: ${broken.length}`);

if (broken.length > 0) {
    console.log('\nBROKEN LINKS:');
    broken.forEach(b => console.log(`  - ${b.folder}/${b.expected}`));
}
