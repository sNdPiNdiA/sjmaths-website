#!/usr/bin/env node
/**
 * Validation Suite for UP Upper Primary Teacher — English Language & Literature Topics
 * Verifies all 24 canonical topics and 16 redirect stubs meet 100% quality standards.
 */

import fs from 'node:fs';
import path from 'node:path';
import { ENGLISH_TOPICS } from './generate_up_upper_primary_english.mjs';

const ROOT = process.cwd();
const BASE_DIR = path.join(ROOT, 'up-upper-primary-teacher', 'english');

let totalChecks = 0;
let passedChecks = 0;
let failedChecks = 0;

function assert(condition, message) {
  totalChecks++;
  if (condition) {
    passedChecks++;
  } else {
    failedChecks++;
    console.error(`  ✗ FAIL: ${message}`);
  }
}

console.log('================================================================');
console.log('SJ Maths — English Topic Quality & Integrity Validation Suite');
console.log(`Checking ${ENGLISH_TOPICS.length} Canonical Topics & Legacy Redirects`);
console.log('================================================================\n');

for (const topic of ENGLISH_TOPICS) {
  const filePath = path.join(BASE_DIR, topic.slug, 'index.html');
  const exists = fs.existsSync(filePath);
  assert(exists, `[${topic.slug}] index.html exists`);
  if (!exists) continue;

  const content = fs.readFileSync(filePath, 'utf8');
  const sizeKb = Math.round(content.length / 1024);

  // 1. File Size check (> 25KB)
  assert(sizeKb >= 25, `[${topic.slug}] File size >= 25KB (Actual: ${sizeKb}KB)`);

  // 2. Mindmap verification
  const hasMindmapWrapper = content.includes('class="mindmap-wrapper"');
  const branchCount = (content.match(/class="mindmap-branch-card"/g) || []).length;
  const subnodeCount = (content.match(/class="mindmap-subnode-item"/g) || []).length;
  assert(hasMindmapWrapper, `[${topic.slug}] Has mindmap-wrapper`);
  assert(branchCount >= 4, `[${topic.slug}] Mindmap has >= 4 branches (Actual: ${branchCount})`);
  assert(subnodeCount >= 16, `[${topic.slug}] Mindmap has >= 16 subnodes (Actual: ${subnodeCount})`);

  // 3. Four Tabs Verification
  assert(content.includes('id="tab-concepts"'), `[${topic.slug}] Tab 1 (Concepts) exists`);
  assert(content.includes('id="tab-practice"'), `[${topic.slug}] Tab 2 (Practice) exists`);
  assert(content.includes('id="tab-test"'), `[${topic.slug}] Tab 3 (Test) exists`);
  assert(content.includes('id="tab-revision"'), `[${topic.slug}] Tab 4 (Revision) exists`);

  // 4. Practice MCQs Verification (10 questions)
  const mcqCount = (content.match(/class="mcq-item-card"/g) || []).length;
  assert(mcqCount >= 10, `[${topic.slug}] Practice MCQs count >= 10 (Actual: ${mcqCount})`);

  // 5. Timed Mini Test Data verification
  const hasTestData = content.includes('const testData = [') && content.includes('"question":');
  assert(hasTestData, `[${topic.slug}] Tab 3 has valid testData payload`);

  // 6. Revision & Exam Traps
  const factCount = (content.match(/class="revision-fact-row"/g) || []).length;
  const mnemonicCount = (content.match(/class="mnemonic-card"/g) || []).length;
  const trapCount = (content.match(/class="trap-card-item"/g) || []).length;
  assert(factCount >= 10, `[${topic.slug}] Tab 4 has >= 10 revision facts (Actual: ${factCount})`);
  assert(mnemonicCount >= 3, `[${topic.slug}] Tab 4 has >= 3 mnemonics (Actual: ${mnemonicCount})`);
  assert(trapCount >= 3, `[${topic.slug}] Tab 4 has >= 3 exam traps (Actual: ${trapCount})`);

  // 7. Comparative Matrix Table
  assert(content.includes('class="prep-table"'), `[${topic.slug}] Comparative prep-table exists`);

  // 8. Strict Constraint: NO FOOTER
  const hasFooterContainer = content.includes('id="footer-container"');
  const hasGlobalFooterScript = content.includes('global-footer.min.js');
  assert(!hasFooterContainer, `[${topic.slug}] STRICT: No id="footer-container"`);
  assert(!hasGlobalFooterScript, `[${topic.slug}] STRICT: No global-footer.min.js`);

  // 9. CSS and JS links
  assert(content.includes('/assets/css/up-upper-primary-topic.min.css?v=20261002_03'), `[${topic.slug}] Uses CSS v20261002_03`);
  assert(content.includes('/assets/js/up-upper-primary-topic.min.js?v=20261002_02'), `[${topic.slug}] Uses JS v20261002_02`);

  // 10. Navigation controls
  assert(content.includes('class="bottom-topic-nav"'), `[${topic.slug}] Bottom navigation present`);
}

// 11. Legacy Redirects Verification
console.log('\nChecking Legacy Redirect Stubs...');
const LEGACY_DIRS = [
  'parts-of-speech',
  'vocabulary',
  'unseen-passage-comprehension',
  path.join('english-grammar-syntax-vocabulary', 'active-and-passive-voice'),
  path.join('english-grammar-syntax-vocabulary', 'articles-and-determiners'),
  path.join('english-grammar-syntax-vocabulary', 'conjunctions-and-clause-analysis'),
  path.join('english-grammar-syntax-vocabulary', 'direct-and-indirect-speech'),
  path.join('english-grammar-syntax-vocabulary', 'error-spotting-sentence-correction'),
  path.join('english-grammar-syntax-vocabulary', 'parts-of-speech-nouns-pronouns-verbs'),
  path.join('english-grammar-syntax-vocabulary', 'prepositions-and-phrasal-verbs'),
  path.join('english-grammar-syntax-vocabulary', 'subject-verb-concord-agreement'),
  path.join('english-grammar-syntax-vocabulary', 'tenses-and-time-aspects'),
  path.join('english-grammar-syntax-vocabulary', 'vocabulary-synonyms-antonyms-idioms'),
  'english-grammar-syntax-vocabulary',
  'history-of-english-literature-language',
  'major-writers-poets-and-works'
];

for (const dir of LEGACY_DIRS) {
  const filePath = path.join(BASE_DIR, dir, 'index.html');
  const exists = fs.existsSync(filePath);
  assert(exists, `[Legacy Redirect] ${dir}/index.html exists`);
  if (exists) {
    const content = fs.readFileSync(filePath, 'utf8');
    assert(content.includes('http-equiv="refresh"'), `[Legacy Redirect] ${dir} has meta refresh`);
  }
}

console.log('\n================================================================');
console.log(`Validation Results:`);
console.log(`  - Total Checks:  ${totalChecks}`);
console.log(`  - Passed:        ${passedChecks}`);
console.log(`  - Failed:        ${failedChecks}`);
console.log(`  - Quality Rate:  ${((passedChecks / totalChecks) * 100).toFixed(1)}%`);
console.log('================================================================\n');

if (failedChecks > 0) {
  process.exit(1);
} else {
  console.log('🎉 ALL ENGLISH TOPICS & REDIRECTS VALIDATED 100% CLEAN!');
}
