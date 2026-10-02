import fs from 'fs';
import path from 'path';

function findHtmlFiles(dir) {
  let results = [];
  const entries = fs.readdirSync(dir, { withFileTypes: true });
  for (const entry of entries) {
    const fullPath = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      results.push(...findHtmlFiles(fullPath));
    } else if (entry.isFile() && entry.name.endsWith('.html')) {
      results.push(fullPath);
    }
  }
  return results;
}

const allEnglishFiles = findHtmlFiles('up-upper-primary-teacher/english');
console.log('Total HTML files in english folder:', allEnglishFiles.length);

const hubHtml = fs.readFileSync('up-upper-primary-teacher/english/index.html', 'utf8');
const linkMatches = hubHtml.matchAll(/href=["']([^"']+)["']/g);
const topicLinks = [];
for (const match of linkMatches) {
  const l = match[1];
  if (l.includes('/english/') && l !== '/up-upper-primary-teacher/english/' && l !== '/up-upper-primary-teacher/') {
    topicLinks.push(l);
  }
}
console.log('Topic links in english/index.html:', topicLinks.length);
console.log('Sample links:', topicLinks.slice(0, 15));

// Check each file's size, whether it has mindmaps, tabs, mini-test, etc.
let fileDetails = [];
for (const f of allEnglishFiles) {
  const normalized = f.replace(/\\/g, '/');
  if (normalized === 'up-upper-primary-teacher/english/index.html') continue;
  const content = fs.readFileSync(f, 'utf8');
  fileDetails.push({
    file: normalized,
    size: content.length,
    hasMindmap: content.includes('mindmap-wrapper'),
    hasTabs: content.includes('study-tabs-strip'),
    hasTest: content.includes('testData =') || content.includes('mini-test'),
    hasMcq: content.includes('mcq-item-card'),
    isRedirect: content.includes('http-equiv="refresh"')
  });
}

console.log('Total topic files:', fileDetails.length);
console.log('Summary of features:');
console.log('- With Mindmap:', fileDetails.filter(d => d.hasMindmap).length);
console.log('- With Study Tabs:', fileDetails.filter(d => d.hasTabs).length);
console.log('- With Mini Test:', fileDetails.filter(d => d.hasTest).length);
console.log('- With MCQs:', fileDetails.filter(d => d.hasMcq).length);
console.log('- Redirects:', fileDetails.filter(d => d.isRedirect).length);

console.log('\nFiles without mindmaps:');
fileDetails.filter(d => !d.hasMindmap && !d.isRedirect).forEach(d => console.log(`  ${d.file} (${d.size} bytes)`));

console.log('\nFiles without mini-test:');
fileDetails.filter(d => !d.hasTest && !d.isRedirect).forEach(d => console.log(`  ${d.file} (${d.size} bytes)`));
