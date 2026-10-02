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

const files = findHtmlFiles('up-upper-primary-teacher');
console.log('Total files found:', files.length);

let stats = {
  redirectStubs: 0,
  legacyTopicStylesReplaced: 0,
  topicCssUpdatedVersion: 0,
  subjectHubsUpdated: 0,
  rootHubUpdated: 0,
  alreadyClean: 0,
  other: 0
};

for (const file of files) {
  const content = fs.readFileSync(file, 'utf8');

  // Check redirect stub
  if (content.includes('http-equiv="refresh"') || content.includes('window.location.replace')) {
    stats.redirectStubs++;
    continue;
  }

  // Check root hub
  const normalizedPath = file.replace(/\\/g, '/');
  if (normalizedPath === 'up-upper-primary-teacher/index.html') {
    stats.rootHubUpdated++;
    continue;
  }

  // Check subject hubs
  if (/^up-upper-primary-teacher\/[^\/]+\/index\.html$/.test(normalizedPath)) {
    stats.subjectHubsUpdated++;
    continue;
  }

  // Check topic files with large legacy styles
  const styleMatch = content.match(/<style[^>]*>([\s\S]*?)<\/style>/i);
  if (styleMatch && styleMatch[1].length > 500 && styleMatch[1].includes('.topic-page-container')) {
    stats.legacyTopicStylesReplaced++;
    continue;
  }

  // Check topic files that link to topic CSS
  if (content.includes('up-upper-primary-topic.min.css') || content.includes('up-upper-primary-topic.css')) {
    stats.topicCssUpdatedVersion++;
    continue;
  }

  stats.other++;
  console.log('Other file:', file);
}

console.log('Dry Run Classification Stats:', stats);
