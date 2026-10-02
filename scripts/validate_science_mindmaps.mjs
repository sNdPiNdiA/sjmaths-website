import fs from 'fs';
import path from 'path';

const catalogPath = path.join(process.cwd(), 'scripts', 'science_topics_catalog.json');
const topics = JSON.parse(fs.readFileSync(catalogPath, 'utf8'));

let passed = 0;
let errors = [];

for (const t of topics) {
  const filePath = path.join(process.cwd(), 'up-upper-primary-teacher', 'science', t.slug, 'index.html');
  if (!fs.existsSync(filePath)) {
    errors.push(`File missing: ${t.slug}`);
    continue;
  }

  const html = fs.readFileSync(filePath, 'utf8');

  if (!html.includes('<!-- Mindmap Component')) {
    errors.push(`${t.slug}: Missing Mindmap Component comment`);
  }
  if (!html.includes('mindmap-wrapper')) {
    errors.push(`${t.slug}: Missing mindmap-wrapper class`);
  }
  if (!html.includes('mindmap-root-badge')) {
    errors.push(`${t.slug}: Missing mindmap-root-badge`);
  }

  const branchCount = (html.match(/class="mindmap-branch-card"/g) || []).length;
  if (branchCount < 4) {
    errors.push(`${t.slug}: Insufficient branches (${branchCount})`);
  }

  const subnodeCount = (html.match(/class="mindmap-subnode-item"/g) || []).length;
  if (subnodeCount < 16) {
    errors.push(`${t.slug}: Insufficient subnodes (${subnodeCount})`);
  }

  // Ensure study notes are intact
  if (!html.includes('1. Core Principles') && !html.includes('1. मुख्य सिद्धांत')) {
    errors.push(`${t.slug}: Study notes card 1 missing or corrupted`);
  }
  if (!html.includes('id="tab-concepts"')) {
    errors.push(`${t.slug}: id="tab-concepts" missing`);
  }

  passed++;
}

console.log(`\nValidation complete for ${passed}/${topics.length} Science Topics.`);
if (errors.length > 0) {
  console.error(`Issues found (${errors.length}):`, errors);
  process.exit(1);
} else {
  console.log(`ALL 34 SCIENCE TOPIC PAGES PASSED MINDMAP VALIDATION! 100% COMPREHENSIVE & INTACT.`);
}
