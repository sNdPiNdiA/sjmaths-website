import fs from 'fs';
import path from 'path';

const INVENTORY_FILE = 'scratch/agriculture_inventory.json';
const inventory = JSON.parse(fs.readFileSync(INVENTORY_FILE, 'utf8'));

console.log('=== Agriculture Content Audit & Verification ===\n');

let total = inventory.length;
let completed = 0;
let missingHtml = 0;
let missingQuiz = 0;
let missingTest = 0;
let hindiFoundHtml = 0;
let hindiFoundQuiz = 0;
let hindiFoundTest = 0;
let smallHtmlCount = 0;
const devanagariRegex = /[\u0900-\u097F]/;

for (const item of inventory) {
  const dir = path.resolve(item.dir);
  const htmlPath = path.join(dir, 'index.html');
  const quizPath = path.join(dir, 'quiz.json');
  const testPath = path.join(dir, 'topic-test.json');

  let itemOk = true;

  if (!fs.existsSync(htmlPath)) {
    missingHtml++;
    itemOk = false;
  } else {
    const html = fs.readFileSync(htmlPath, 'utf8');
    if (html.length < 20000) {
      // Could be stub
      smallHtmlCount++;
      itemOk = false;
    }
    if (devanagariRegex.test(html)) {
      hindiFoundHtml++;
      itemOk = false;
    }
  }

  if (!fs.existsSync(quizPath)) {
    missingQuiz++;
    itemOk = false;
  } else {
    try {
      const quiz = JSON.parse(fs.readFileSync(quizPath, 'utf8'));
      if (devanagariRegex.test(JSON.stringify(quiz))) {
        hindiFoundQuiz++;
        itemOk = false;
      }
    } catch (e) {
      missingQuiz++;
      itemOk = false;
    }
  }

  if (!fs.existsSync(testPath)) {
    missingTest++;
    itemOk = false;
  } else {
    try {
      const test = JSON.parse(fs.readFileSync(testPath, 'utf8'));
      if (devanagariRegex.test(JSON.stringify(test))) {
        hindiFoundTest++;
        itemOk = false;
      }
    } catch (e) {
      missingTest++;
      itemOk = false;
    }
  }

  if (itemOk) {
    completed++;
  }
}

// Check for empty directories inside agriculture
function findEmptyDirs(dir, list = []) {
  const entries = fs.readdirSync(dir, { withFileTypes: true });
  if (entries.length === 0) {
    list.push(dir);
    return list;
  }
  for (const entry of entries) {
    if (entry.isDirectory()) {
      const sub = path.join(dir, entry.name);
      findEmptyDirs(sub, list);
    }
  }
  return list;
}

const emptyDirs = findEmptyDirs(path.resolve('agriculture'));

console.log(`Total Target Topics: ${total}`);
console.log(`Fully Generated & Validated Topics: ${completed}/${total} (${((completed / total) * 100).toFixed(1)}%)`);
console.log(`Missing/Stub HTML (<20KB): ${missingHtml + smallHtmlCount}`);
console.log(`Missing Quiz JSON: ${missingQuiz}`);
console.log(`Missing Topic Test JSON: ${missingTest}`);
console.log(`Devanagari Hindi in HTML: ${hindiFoundHtml}`);
console.log(`Devanagari Hindi in Quiz: ${hindiFoundQuiz}`);
console.log(`Devanagari Hindi in Tests: ${hindiFoundTest}`);
console.log(`Empty Directories in agriculture/: ${emptyDirs.length}`);
if (emptyDirs.length > 0) {
  console.log('Empty dirs sample:', emptyDirs.slice(0, 5));
}
