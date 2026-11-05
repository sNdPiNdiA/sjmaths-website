const fs = require('fs');
const path = require('path');
const cheerio = require('cheerio');

const baseDir = 'class-11-applied-mathematics';
const forbiddenPhrases = [
  'By fundamental definition, the parameter satisfies the required identity constraint',
  'satisfies the required identity constraint',
  'Applied Mathematics analytical principles establish standard domain constraints',
  'analytical principles establish standard domain constraints',
  'systematic validation confirms correctness'
];

function getAllHtmlFiles(dir) {
  let results = [];
  const list = fs.readdirSync(dir);
  list.forEach(file => {
    const fullPath = path.join(dir, file);
    const stat = fs.statSync(fullPath);
    if (stat && stat.isDirectory()) {
      results = results.concat(getAllHtmlFiles(fullPath));
    } else if (file === 'index.html') {
      results.push(fullPath);
    }
  });
  return results;
}

const allHtmls = getAllHtmlFiles(baseDir);
console.log('Total index.html files discovered:', allHtmls.length);

let totalSubtopics = 0;
let totalChapters = 0;
let syllabusHub = 0;
let boilerplateViolations = 0;
let subtopicsWith10QMock = 0;
let subtopicsWithFewerMockQ = 0;

allHtmls.forEach(file => {
  const relPath = file.replace(/\\/g, '/');
  const content = fs.readFileSync(file, 'utf8');
  
  // Check boilerplate
  let fileViolations = 0;
  forbiddenPhrases.forEach(p => {
    if (content.includes(p)) {
      fileViolations++;
    }
  });
  if (fileViolations > 0) {
    console.error('VIOLATION in', relPath, 'matches:', fileViolations);
    boilerplateViolations += fileViolations;
  }

  // Categorize
  const parts = relPath.split('/');
  if (parts.length === 2) {
    syllabusHub++;
  } else if (parts.length === 3) {
    totalChapters++;
  } else if (parts.length === 4) {
    totalSubtopics++;
    // Check mock questions
    const mockMatch = content.match(/window\.mockObjectiveData\s*=\s*(\[[\s\S]*?\]);\s*(?:window\.grade|function)/);
    if (mockMatch) {
      try {
        const data = eval(mockMatch[1]);
        if (data.length === 10) {
          subtopicsWith10QMock++;
        } else {
          console.warn('Subtopic', relPath, 'has', data.length, 'questions (expected 10)');
          subtopicsWithFewerMockQ++;
        }
      } catch (e) {
        console.error('Eval error in', relPath, e.message);
      }
    } else {
      console.warn('Subtopic', relPath, 'has NO window.mockObjectiveData');
    }
  }
});

console.log('=== AUDIT SUMMARY ===');
console.log('Syllabus Hub count:', syllabusHub, '(expected: 1)');
console.log('Chapter Landing count:', totalChapters, '(expected: 16)');
console.log('Subtopics count:', totalSubtopics, '(expected: 62)');
console.log('Total URLs:', syllabusHub + totalChapters + totalSubtopics, '(expected: 79)');
console.log('Boilerplate Violations:', boilerplateViolations, '(expected: 0)');
console.log('Subtopics with 10-Q Interactive Mock:', subtopicsWith10QMock, '(expected: 62)');
console.log('Subtopics with != 10-Q Mock:', subtopicsWithFewerMockQ, '(expected: 0)');

