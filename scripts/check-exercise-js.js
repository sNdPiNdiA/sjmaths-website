/**
 * Check which Class 10 exercise files have exercise.js included
 */
const fs = require('fs');
const path = require('path');

const baseDir = path.join(__dirname, '..', 'classes', 'class-10', 'ncert-exercise-practice');

const chapters = [
    { folder: 'chapter-1-real-numbers', exercises: [1, 2] },
    { folder: 'chapter-2-polynomials', exercises: [1, 2] },
    { folder: 'chapter-3-pair-of-linear-equations-in-two-variables', exercises: [1, 2, 3] },
    { folder: 'chapter-4-quadratic-equations', exercises: [1, 2, 3] },
    { folder: 'chapter-5-arithmetic-progressions', exercises: [1, 2, 3, 4] },
    { folder: 'chapter-6-triangles', exercises: [1, 2, 3] },
    { folder: 'chapter-7-coordinate-geometry', exercises: [1, 2] },
    { folder: 'chapter-8-introduction-to-trigonometry', exercises: [1, 2, 3] },
    { folder: 'chapter-9-applications-of-trigonometry', exercises: [1] },
    { folder: 'chapter-10-circles', exercises: [1, 2] },
    { folder: 'chapter-11-areas-related-to-circles', exercises: [1] },
    { folder: 'chapter-12-surface-areas-and-volumes', exercises: [1, 2] },
    { folder: 'chapter-13-statistics', exercises: [1, 2, 3] },
    { folder: 'chapter-14-probability', exercises: [1] }
];

console.log('Checking Class 10 exercise files for exercise.js...\n');

let hasExerciseJS = [];
let missingExerciseJS = [];

chapters.forEach((ch, i) => {
    const chNum = i + 1;
    ch.exercises.forEach(ex => {
        const fileName = `exercise-${chNum}-${ex}.html`;
        const filePath = path.join(baseDir, ch.folder, fileName);

        if (fs.existsSync(filePath)) {
            const content = fs.readFileSync(filePath, 'utf8');
            if (content.includes('exercise.js')) {
                hasExerciseJS.push({ chapter: chNum, exercise: ex, file: fileName });
                console.log(`✓ Ch${chNum} Ex${ex}: has exercise.js`);
            } else {
                missingExerciseJS.push({ chapter: chNum, exercise: ex, file: fileName, folder: ch.folder });
                console.log(`✗ Ch${chNum} Ex${ex}: MISSING exercise.js`);
            }
        } else {
            console.log(`? Ch${chNum} Ex${ex}: file not found`);
        }
    });
});

console.log('\n========================================');
console.log(`With exercise.js: ${hasExerciseJS.length}`);
console.log(`Missing exercise.js: ${missingExerciseJS.length}`);

if (missingExerciseJS.length > 0) {
    console.log('\nFiles missing exercise.js:');
    missingExerciseJS.forEach(f => console.log(`  - ${f.folder}/${f.file}`));
}
