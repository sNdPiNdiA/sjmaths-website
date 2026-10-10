const fs = require('fs');
const path = require('path');

const ROOT_DIR = process.cwd();
const AHC_DIR = path.join(ROOT_DIR, 'ahc-ro-aro');

function findHtmlFiles(dir) {
  let results = [];
  const entries = fs.readdirSync(dir, { withFileTypes: true });
  for (const entry of entries) {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      results = results.concat(findHtmlFiles(full));
    } else if (entry.name === 'index.html') {
      results.push(full);
    }
  }
  return results;
}

const allHtml = findHtmlFiles(AHC_DIR);

const topics = [];

for (const file of allHtml) {
  const relPath = path.relative(AHC_DIR, file).replace(/\\/g, '/');
  const dirPath = path.dirname(file);
  const parts = relPath.split('/');
  
  // Hub files: index.html (root) or <subject>/index.html
  if (relPath === 'index.html' || parts.length === 2) {
    continue;
  }

  const content = fs.readFileSync(file, 'utf8');

  let embeddedPracticeCount = 0;
  let embeddedMockCount = 0;
  let jsonPracticeCount = 0;
  let jsonMockCount = 0;

  const matchEn = content.match(/<script id="embedded-study-guide-data"[^>]*>([\s\S]*?)<\/script>/i);
  if (matchEn) {
    try {
      const data = JSON.parse(matchEn[1]);
      if (Array.isArray(data.practiceQuestions)) embeddedPracticeCount = data.practiceQuestions.length;
      if (Array.isArray(data.mockTestQuestions)) embeddedMockCount = data.mockTestQuestions.length;
    } catch (e) {}
  }

  const practiceJsonPath = path.join(dirPath, 'practice.json');
  if (fs.existsSync(practiceJsonPath)) {
    try {
      const pj = JSON.parse(fs.readFileSync(practiceJsonPath, 'utf8'));
      if (Array.isArray(pj.practiceQuestions)) jsonPracticeCount = pj.practiceQuestions.length;
      if (Array.isArray(pj.mockTestQuestions)) jsonMockCount = pj.mockTestQuestions.length;
    } catch (e) {}
  }

  const totalPractice = Math.max(embeddedPracticeCount, jsonPracticeCount);
  const totalMock = Math.max(embeddedMockCount, jsonMockCount);
  const totalMCQs = totalPractice + totalMock; // Check total mcqs vs practice questions

  const subject = parts[0];
  const topicSlug = parts.slice(1, -1).join('/');

  topics.push({
    subject,
    topicSlug,
    relDir: path.dirname(relPath),
    embeddedPracticeCount,
    embeddedMockCount,
    jsonPracticeCount,
    jsonMockCount,
    practiceQuestions: totalPractice,
    mockQuestions: totalMock,
    totalMCQs,
    has50Practice: totalPractice >= 50
  });
}

// Generate report
const bySubject = {};
for (const t of topics) {
  if (!bySubject[t.subject]) {
    bySubject[t.subject] = {
      total: 0,
      has50Practice: 0,
      hasLess50Practice: 0,
      has0Practice: 0,
      topicsMissing50: []
    };
  }
  bySubject[t.subject].total++;
  if (t.practiceQuestions >= 50) {
    bySubject[t.subject].has50Practice++;
  } else {
    bySubject[t.subject].hasLess50Practice++;
    if (t.practiceQuestions === 0) bySubject[t.subject].has0Practice++;
    bySubject[t.subject].topicsMissing50.push({
      topic: t.topicSlug,
      practice: t.practiceQuestions,
      mock: t.mockQuestions,
      totalMCQs: t.totalMCQs
    });
  }
}

const totalTopics = topics.length;
const totalWith50 = topics.filter(t => t.practiceQuestions >= 50).length;
const totalMissing50 = topics.filter(t => t.practiceQuestions < 50).length;
const totalWith0 = topics.filter(t => t.practiceQuestions === 0).length;

console.log('=== AHC RO/ARO MCQ AUDIT SUMMARY ===');
console.log(`Total Topics: ${totalTopics}`);
console.log(`Topics with >= 50 Practice MCQs: ${totalWith50}`);
console.log(`Topics with < 50 Practice MCQs: ${totalMissing50}`);
console.log(`Topics with 0 Practice MCQs: ${totalWith0}`);
console.log('====================================\n');

console.log('SUBJECT-WISE SUMMARY:');
console.log('-------------------------------------------------------------------------------------------------');
console.log('| Subject                         | Total | >=50 Practice | <50 Practice | 0 Practice | Coverage% |');
console.log('-------------------------------------------------------------------------------------------------');

for (const [subj, data] of Object.entries(bySubject)) {
  const pct = ((data.has50Practice / data.total) * 100).toFixed(1) + '%';
  console.log(
    `| ${subj.padEnd(31)} | ${String(data.total).padStart(5)} | ${String(data.has50Practice).padStart(13)} | ${String(data.hasLess50Practice).padStart(12)} | ${String(data.has0Practice).padStart(10)} | ${pct.padStart(9)} |`
  );
}
console.log('-------------------------------------------------------------------------------------------------');

// Write detailed JSON report
fs.writeFileSync(
  path.join(ROOT_DIR, 'scripts', 'ahc-ro-aro-mcq-audit.json'),
  JSON.stringify({ summary: { totalTopics, totalWith50, totalMissing50, totalWith0 }, bySubject, topics }, null, 2),
  'utf8'
);
console.log('\nDetailed audit saved to scripts/ahc-ro-aro-mcq-audit.json');
