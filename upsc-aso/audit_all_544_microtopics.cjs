const fs = require('fs');
const path = require('path');

const manifestPath = path.resolve('upsc-aso/all_544_microtopics.json');
if (!fs.existsSync(manifestPath)) {
  console.error('ERROR: all_544_microtopics.json not found.');
  process.exit(1);
}

const allTopics = JSON.parse(fs.readFileSync(manifestPath, 'utf8'));

// CLI options: e.g. node audit_all_544_microtopics.cjs --day=1 or --id=3 or --all
const args = process.argv.slice(2);
let targetDay = null;
let targetId = null;

for (const a of args) {
  if (a.startsWith('--day=')) targetDay = parseInt(a.split('=')[1], 10);
  else if (a.startsWith('--id=')) targetId = parseInt(a.split('=')[1], 10);
}

let topicsToAudit = allTopics;
if (targetId) topicsToAudit = allTopics.filter(t => t.id === targetId);
else if (targetDay) topicsToAudit = allTopics.filter(t => t.day === targetDay);

console.log(`\nAuditing ${topicsToAudit.length} microtopics...`);

let passed = 0;
let failed = 0;
const defects = [];

for (const t of topicsToAudit) {
  const file = path.resolve(t.filePath);
  if (!fs.existsSync(file)) {
    defects.push({ id: t.id, title: t.title, issue: 'File does not exist' });
    failed++;
    continue;
  }

  const content = fs.readFileSync(file, 'utf8');
  const issues = [];

  if (content.length < 5000) {
    issues.push(`File too small (${content.length} bytes)`);
  }

  // Daylight UI Theme check (stress-free eye-friendly theme)
  if (!content.includes('--bg-void: #f8fafc') || content.includes('#060911')) {
    issues.push('Missing stress-free daylight theme (--bg-void: #f8fafc) or contains legacy dark void #060911');
  }

  // Polyfill check
  if (content.includes('polyfill.io')) {
    issues.push('Contains insecure polyfill.io');
  }

  // MathJax check
  if (!content.includes('window.MathJax =') || !content.includes('tex-mml-chtml.js')) {
    issues.push('Missing standardized MathJax configuration');
  }

  // Breadcrumb position check
  const h1Idx = content.indexOf('<h1');
  const breadcrumbIdx = content.indexOf('breadcrumb-trail');
  if (breadcrumbIdx === -1 || (h1Idx !== -1 && breadcrumbIdx > h1Idx)) {
    issues.push('Breadcrumbs missing or located after <h1>');
  }

  // 8 Pillars check
  const pillars = [
    'Pillar 1:',
    'Pillar 2:',
    'Pillar 3:',
    'Pillar 4:',
    'Pillar 5:',
    'Pillar 6:',
    'Pillar 7:',
    'Pillar 8:'
  ];
  for (const p of pillars) {
    if (!content.includes(p)) {
      issues.push(`Missing ${p}`);
    }
  }

  // 4 Tabs check
  if (!content.includes('tab-concepts') || !content.includes('tab-practice') || !content.includes('tab-minitest') || !content.includes('tab-flashcards')) {
    issues.push('Missing one or more of the 4 standard tabs');
  }

  // Completeness check
  if (!content.includes('</html>')) {
    issues.push('HTML truncated (missing </html>)');
  }

  // Air Safety Officer Section check
  if (!content.includes('aso-mission-banner') || !content.includes('Air Safety Officers')) {
    issues.push('Missing dedicated Air Safety Officers relevance section');
  }

  // Conflict stylesheet check (causing white bleed and squished hero)
  if (content.includes('main.min.css') || content.includes('layout.min.css')) {
    issues.push('Contains conflicting legacy stylesheets (main.min.css/layout.min.css)');
  }

  if (issues.length > 0) {
    failed++;
    defects.push({ id: t.id, title: t.title, filePath: t.filePath, issues });
  } else {
    passed++;
  }
}

console.log(`\n================ AUDIT SUMMARY ================`);
console.log(`Audited: ${topicsToAudit.length}`);
console.log(`Passed:  ${passed} (${((passed/topicsToAudit.length)*100).toFixed(1)}%)`);
console.log(`Failed:  ${failed}`);

if (defects.length > 0) {
  console.log(`\nSample Defects (first 10):`);
  console.log(JSON.stringify(defects.slice(0, 10), null, 2));
}
console.log(`================================================\n`);
