import fs from 'fs';
import path from 'path';

function getMicrotopicDirs(dir, list = []) {
  const files = fs.readdirSync(dir);
  if (files.includes('index.html') && (files.includes('tabs') || files.includes('content.json'))) {
    list.push(dir);
  }
  for (const f of files) {
    const full = path.join(dir, f);
    if (fs.statSync(full).isDirectory() && f !== 'tabs' && f !== 'assets') {
      getMicrotopicDirs(full, list);
    }
  }
  return list;
}

const topics = getMicrotopicDirs('upsc');
console.log(`Found ${topics.length} microtopic directories in upsc.`);

let hasTabsDir = 0;
let hasOverview = 0;
let hasConcepts = 0;
let hasPractice = 0;
let hasRevision = 0;
let hasMains = 0;
let hasTest = 0;
let hasManifest = 0;

for (const t of topics) {
  const tabsPath = path.join(t, 'tabs');
  if (fs.existsSync(tabsPath)) {
    hasTabsDir++;
    if (fs.existsSync(path.join(tabsPath, 'overview.json'))) hasOverview++;
    if (fs.existsSync(path.join(tabsPath, 'concepts.json'))) hasConcepts++;
    if (fs.existsSync(path.join(tabsPath, 'practice.json'))) hasPractice++;
    if (fs.existsSync(path.join(tabsPath, 'revision.json'))) hasRevision++;
    if (fs.existsSync(path.join(tabsPath, 'mains.json'))) hasMains++;
    if (fs.existsSync(path.join(tabsPath, 'test.json'))) hasTest++;
  }
  if (fs.existsSync(path.join(t, 'page.manifest.json'))) hasManifest++;
}

console.log({
  totalTopics: topics.length,
  hasTabsDir,
  hasOverview,
  hasConcepts,
  hasPractice,
  hasRevision,
  hasMains,
  hasTest,
  hasManifest
});

