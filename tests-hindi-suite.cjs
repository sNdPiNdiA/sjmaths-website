const fs = require('fs');
const path = require('path');
const cheerio = require('cheerio');

console.log('=== STARTING UPPSC RO/ARO GENERAL HINDI INTEGRITY SUITE ===\n');

// 1. Verify ro-aro-topic.js engine normalization logic
const topicJs = fs.readFileSync('assets/js/ro-aro-topic.js', 'utf-8');
const match = topicJs.match(/function normalizeQ\(q\) \{([\s\S]*?)\n      \}/);
if (!match) {
  console.error('FAIL: Could not extract normalizeQ from ro-aro-topic.js');
  process.exit(1);
}
const normalizeQ = new Function('q', match[1]);

// Test letter ans mapping
const testSampleA = normalizeQ({ q: "Q1", options: ["A. 1", "B. 2"], ans: "A", exp: "Exp1" });
const testSampleB = normalizeQ({ q: "Q2", options: ["A. 1", "B. 2"], ans: "B", exp: "Exp2" });
const testSampleC = normalizeQ({ q: "Q3", options: ["A. 1", "B. 2", "C. 3"], ans: "C", exp: "Exp3" });
const testSampleD = normalizeQ({ q: "Q4", options: ["A. 1", "B. 2", "C. 3", "D. 4"], ans: "D", exp: "Exp4" });

if (testSampleA.correct !== 0 || testSampleB.correct !== 1 || testSampleC.correct !== 2 || testSampleD.correct !== 3) {
  console.error('FAIL: normalizeQ letter answer mapping failed!', {
    A: testSampleA.correct,
    B: testSampleB.correct,
    C: testSampleC.correct,
    D: testSampleD.correct
  });
  process.exit(1);
}
if (!testSampleA.qHi || !testSampleA.explanation.hi) {
  console.error('FAIL: normalizeQ failed to map q or exp to qHi/explanation.hi');
  process.exit(1);
}
console.log('PASS: Engine normalizeQ handles both schemas and letter answers perfectly.\n');

// 2. Read syllabus
const syllabusHtml = fs.readFileSync('uppsc-ro-aro/syllabus/index.html', 'utf-8');
const $s = cheerio.load(syllabusHtml);

const phinPanel = $s('#panel-phin');
if (!phinPanel.length) {
  console.error('FAIL: #panel-phin not found in syllabus');
  process.exit(1);
}

const cardIds = [
  'subj-phin-opp',
  'subj-phin-sent',
  'subj-phin-oneword',
  'subj-phin-nature',
  'subj-phin-adj',
  'subj-phin-syn'
];

const hubs = [];
const topics = [];

cardIds.forEach((cid, idx) => {
  const card = phinPanel.find('#' + cid);
  if (!card.length) {
    console.error(`FAIL: Card ${cid} missing in #panel-phin`);
    return;
  }
  const hubHref = card.find('.subject-title a').attr('href');
  hubs.push(hubHref);

  card.find('ul.syllabus-topics a, .syllabus-item a').each((j, a) => {
    topics.push({
      cardIdx: idx + 1,
      cardId: cid,
      topicNum: j + 1,
      href: $s(a).attr('href'),
      title: $s(a).text().trim().replace(/\s+/g, ' ')
    });
  });
});

console.log(`Verified Syllabus structure: ${hubs.length} Hubs, ${topics.length} Micro-topics linked.`);
if (topics.length !== 68) {
  console.error(`FAIL: Expected 68 micro-topics in syllabus, found ${topics.length}`);
  process.exit(1);
}

// 3. Verify each micro-topic page on disk
let totalErrors = 0;
let minNotesLen = Infinity;
let maxNotesLen = 0;
let smallestTopic = '';

const placeholderRegex = /आयोग के उच्च-प्राथमिकता तत्सम-तद्भव शब्द|उत्तर प्रदेश लोक सेवा आयोग की विगत परीक्षाओं में पूछे गए सबसे महत्वपूर्ण तत्सम-तद्भव युग्मों का व्यवस्थित संकलन/;

topics.forEach((t, i) => {
  let cleanPath = t.href.replace(/^https?:\/\/[^\/]+/, '').replace(/^\//, '');
  if (!cleanPath.endsWith('.html')) cleanPath = path.join(cleanPath, 'index.html');
  const fullPath = path.resolve(cleanPath);

  if (!fs.existsSync(fullPath)) {
    console.error(`[ERR] File missing: ${cleanPath}`);
    totalErrors++;
    return;
  }

  const content = fs.readFileSync(fullPath, 'utf-8');
  const $ = cheerio.load(content);

  // Check Tab 1: Notes
  const notesTab = $('#tab-notes');
  if (!notesTab.length) {
    console.error(`[ERR] Missing #tab-notes in ${t.href}`);
    totalErrors++;
    return;
  }

  const notesHtml = notesTab.html() || '';
  const notesLen = notesHtml.length;
  if (notesLen < minNotesLen) {
    minNotesLen = notesLen;
    smallestTopic = t.href;
  }
  if (notesLen > maxNotesLen) maxNotesLen = notesLen;

  if (notesLen < 4500) {
    console.error(`[ERR] Notes length too short (${notesLen} chars) in ${t.href}`);
    totalErrors++;
  }

  if (placeholderRegex.test(content)) {
    console.error(`[ERR] Placeholder text detected in ${t.href}`);
    totalErrors++;
  }

  // Check Tab 2: Practice PYQs
  const practiceCards = $('#tab-practice .ro-pyq-card');
  if (practiceCards.length !== 10) {
    console.error(`[ERR] Expected 10 practice cards, found ${practiceCards.length} in ${t.href}`);
    totalErrors++;
  }

  practiceCards.each((qIdx, pCard) => {
    const qText = $(pCard).find('.ro-pyq-q').text().trim();
    if (!qText || qText.includes('undefined')) {
      console.error(`[ERR] Broken question text ("${qText}") in ${t.href} [Q${qIdx + 1}]`);
      totalErrors++;
    }
    const optCount = $(pCard).find('.ro-pyq-opt').length;
    if (optCount < 4) {
      console.error(`[ERR] Incomplete options (${optCount}) in ${t.href} [Q${qIdx + 1}]`);
      totalErrors++;
    }
    const ansBadge = $(pCard).find('.ro-ans-badge').text().trim();
    if (!/^[A-D]$/.test(ansBadge)) {
      console.error(`[ERR] Invalid answer badge ("${ansBadge}") in ${t.href} [Q${qIdx + 1}]`);
      totalErrors++;
    }
  });

  // Check Tab 3: Mock Test Simulator Script
  const testScript = $('#ro-test-data');
  if (!testScript.length) {
    console.error(`[ERR] Missing #ro-test-data script in ${t.href}`);
    totalErrors++;
  } else {
    try {
      const testJson = JSON.parse(testScript.text() || '{}');
      ['1', '2', '3'].forEach(lvl => {
        const lvlQs = testJson[lvl] || [];
        if (lvlQs.length !== 5) {
          console.error(`[ERR] Level ${lvl} has ${lvlQs.length} questions (expected 5) in ${t.href}`);
          totalErrors++;
        }
        lvlQs.forEach((rawQ, qIdx) => {
          const norm = normalizeQ(rawQ);
          if (!norm.qHi || norm.qHi.trim() === '' || norm.qHi.includes('undefined')) {
            console.error(`[ERR] Test L${lvl} Q${qIdx+1} empty/broken in ${t.href}`);
            totalErrors++;
          }
          if (norm.correct < 0 || norm.correct > 3 || isNaN(norm.correct)) {
            console.error(`[ERR] Test L${lvl} Q${qIdx+1} invalid correct index (${norm.correct}) in ${t.href}`);
            totalErrors++;
          }
        });
      });
    } catch (e) {
      console.error(`[ERR] JSON parse error in ${t.href}: ${e.message}`);
      totalErrors++;
    }
  }

  // Check Tab 4: Mains
  const mainsTab = $('#tab-mains');
  if (!mainsTab.length || mainsTab.text().trim().length < 50) {
    console.error(`[ERR] Mains tab missing or empty in ${t.href}`);
    totalErrors++;
  }

  // Check Tab 5: Revision
  const revTab = $('#tab-revision');
  if (!revTab.length || revTab.text().trim().length < 50) {
    console.error(`[ERR] Revision tab missing or empty in ${t.href}`);
    totalErrors++;
  }
});

console.log('Micro-topics deep verification complete.');
console.log(`Smallest notes length: ${minNotesLen} chars (${smallestTopic})`);
console.log(`Largest notes length: ${maxNotesLen} chars`);

// 4. Verify all 6 category hubs
hubs.forEach(h => {
  let cleanPath = h.replace(/^https?:\/\/[^\/]+/, '').replace(/^\//, '');
  if (!cleanPath.endsWith('.html')) cleanPath = path.join(cleanPath, 'index.html');
  const fullPath = path.resolve(cleanPath);

  if (!fs.existsSync(fullPath)) {
    console.error(`[ERR] Hub missing: ${cleanPath}`);
    totalErrors++;
    return;
  }
  const content = fs.readFileSync(fullPath, 'utf-8');
  const $ = cheerio.load(content);
  const notesLen = ($('#tab-notes').html() || '').length;
  if (notesLen < 4500) {
    console.error(`[ERR] Hub notes too short (${notesLen} chars) in ${h}`);
    totalErrors++;
  }
});

// 5. Verify unlinked ati-bhramak page on disk is also healthy
const extraFile = 'uppsc-ro-aro/hindi/ati-bhramak-tatsam-tadbhav-pairs/index.html';
if (fs.existsSync(extraFile)) {
  const content = fs.readFileSync(extraFile, 'utf-8');
  const $ = cheerio.load(content);
  const extraNotesLen = ($('#tab-notes').html() || '').length;
  console.log(`Verified ati-bhramak-tatsam-tadbhav-pairs notes length: ${extraNotesLen} chars`);
  if (extraNotesLen < 4500) {
    console.error(`[ERR] ati-bhramak notes too short: ${extraNotesLen}`);
    totalErrors++;
  }
}

console.log('\n======================================================');
if (totalErrors === 0) {
  console.log('SUCCESS: ALL 68 MICRO-TOPICS, 6 HUBS, AND ENGINE PASSED 100%!');
} else {
  console.error(`FAILED: Total ${totalErrors} issues found!`);
  process.exit(1);
}
console.log('======================================================');
