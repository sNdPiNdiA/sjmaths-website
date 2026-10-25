import fs from 'fs';
import path from 'path';

const testDir = 'upsc/economy/Agriculture-Sector-in-Indian-Economy/Agricultural-System';
const tabsDir = path.join(testDir, 'tabs');

console.log('Original files in tabsDir:');
console.log(fs.readdirSync(tabsDir));

// Read the 4 study notes components
const readJson = (name) => {
  const p = path.join(tabsDir, name);
  return fs.existsSync(p) ? JSON.parse(fs.readFileSync(p, 'utf8')) : null;
};

const overview = readJson('overview.json');
const concepts = readJson('concepts.json');
const visual = readJson('visual.json');
const comparisons = readJson('comparisons.json');

const notes = {
  overview,
  concepts,
  visual,
  comparisons
};

console.log('Consolidated notes.json keys:', Object.keys(notes).filter(k => notes[k] !== null));

