import fs from 'node:fs';
import path from 'node:path';

const ROOT = process.cwd();
const SST_DIR = path.join(ROOT, 'up-upper-primary-teacher', 'social-studies');
const TRACKER_PATH = path.join(SST_DIR, 'index.html');

function decodeHtml(html) {
  return String(html)
    .replace(/&amp;/g, '&')
    .replace(/&lt;/g, '<')
    .replace(/&gt;/g, '>')
    .replace(/&quot;/g, '"')
    .replace(/&#39;/g, "'");
}

function extractSyllabus() {
  if (!fs.existsSync(TRACKER_PATH)) {
    console.error(`Tracker file not found: ${TRACKER_PATH}`);
    return [];
  }
  const html = fs.readFileSync(TRACKER_PATH, 'utf8');

  const regex = /<details class="module-accordion" data-sec-idx="([^"]+)"[\s\S]*?<h3 class="module-title">[\s\S]*?<span class="lang-hi">([^<]+)<\/span>[\s\S]*?<span class="lang-en">([^<]+)<\/span>[\s\S]*?<ul class="module-list">([\s\S]*?)<\/ul>/g;

  let sMatch;
  const topicList = [];

  while ((sMatch = regex.exec(html)) !== null) {
    const [_, secIdx, secTitleHi, secTitleEn, secBody] = sMatch;
    const topicRegex = /<li class="topic-row">[\s\S]*?<input[^>]*id="([^"]+)"[\s\S]*?<a href="([^"]+)"[\s\S]*?<span class="topic-num">([^<]+)<\/span>[\s\S]*?<span class="lang-hi">([^<]+)<\/span>[\s\S]*?<span class="lang-en">([^<]+)<\/span>[\s\S]*?<span class="topic-tag">([^<]+)<\/span>/g;
    let tMatch;
    while ((tMatch = topicRegex.exec(secBody)) !== null) {
      const href = tMatch[2].startsWith('/') ? tMatch[2] : '/' + tMatch[2];
      const cleanHref = href.endsWith('/') ? href : href + '/';
      const slug = cleanHref.replace('/up-upper-primary-teacher/social-studies/', '').replace(/\//g, '');
      const numRaw = tMatch[3].trim().replace('#', '');
      const num = parseInt(numRaw, 10);

      topicList.push({
        chkId: tMatch[1],
        href: cleanHref,
        slug,
        num,
        numStr: `#${num}`,
        nameHi: decodeHtml(tMatch[4].trim()),
        nameEn: decodeHtml(tMatch[5].trim()),
        tag: tMatch[6].trim(),
        secIdx: parseInt(secIdx, 10),
        secTitleHi: decodeHtml(secTitleHi.trim()),
        secTitleEn: decodeHtml(secTitleEn.trim()),
      });
    }
  }

  return topicList;
}

const topics = extractSyllabus();
console.log(`================================================================`);
console.log(`  Auditing ${topics.length} Social Studies Micro-Topics`);
console.log(`  Directory: ${SST_DIR}`);
console.log(`================================================================\n`);

let passedCount = 0;
let failedCount = 0;
const issues = [];

for (const t of topics) {
  const filePath = path.join(SST_DIR, t.slug, 'index.html');
  if (!fs.existsSync(filePath)) {
    failedCount++;
    issues.push(`[MISSING] Topic #${t.numStr} (${t.slug}) does not exist on disk.`);
    continue;
  }

  const stat = fs.statSync(filePath);
  const sizeKb = (stat.size / 1024).toFixed(1);
  const content = fs.readFileSync(filePath, 'utf-8');

  const checks = [];

  // Common assets check
  if (!content.includes('up-upper-primary-topic.min.css') && !content.includes('up-upper-primary-topic.css')) {
    checks.push('Missing common CSS link (/assets/css/up-upper-primary-topic.min.css)');
  }
  if (!content.includes('up-upper-primary-topic.min.js') && !content.includes('up-upper-primary-topic.js')) {
    checks.push('Missing common JS link (/assets/js/up-upper-primary-topic.min.js)');
  }
  if (content.includes('<style>')) {
    checks.push('Contains obsolete inline <style> block');
  }

  // Check absence of AI-tell artifacts
  if (/Module\s*\d+\s*:\s*Module\s*\d+/i.test(content)) {
    checks.push('Contains duplicated Module pill');
  }
  if (/Pointwise Breakdown/i.test(content)) {
    checks.push('Contains AI title artifact "Pointwise Breakdown"');
  }
  if (/zero narrative/i.test(content)) {
    checks.push('Contains meta prompt leak "zero narrative"');
  }

  // Content depth checks
  if (stat.size < 40 * 1024) checks.push(`Small size (${sizeKb} KB)`);
  if (!content.includes('id="tab-concepts"')) checks.push('Missing tab-concepts');
  if (!content.includes('id="tab-practice"')) checks.push('Missing tab-practice');
  if (!content.includes('id="tab-test"')) checks.push('Missing tab-test');
  if (!content.includes('id="tab-revision"')) checks.push('Missing tab-revision');

  // Pointwise format check
  if (!content.includes('class="point-card"') && !content.includes("class='point-card'")) {
    checks.push('Missing pointwise notes (.point-card)');
  }

  // Mnemonics & Tips check
  if (!content.includes('tip-box') && !content.includes('trick-box') && !content.includes('mnemonic-inline-box')) {
    checks.push('Missing embedded tips/tricks/mnemonics in concepts');
  }

  // Sub-table or comparative table check
  if (!content.includes('prep-table') && !content.includes('topic-subtable')) {
    checks.push('Missing tables');
  }
  
  // Count MCQs
  const mcqMatches = (content.match(/class="mcq-item-card/g) || []).length;
  if (mcqMatches < 10) checks.push(`Only ${mcqMatches} MCQs found`);

  // Error artifacts
  if (content.includes('[object Object]')) checks.push('Contains [object Object]');
  if (content.includes('>undefined<')) checks.push('Contains rendered undefined');

  if (checks.length > 0) {
    failedCount++;
    issues.push(`[FAIL] Topic #${t.numStr} (${t.slug}) - ${checks.join(', ')}`);
  } else {
    passedCount++;
    console.log(`  [OK] Topic #${t.numStr.padEnd(5)} | ${sizeKb.padStart(5)} KB | Pointwise + 10 MCQs | ${t.nameEn.substring(0, 42)}`);
  }
}

console.log(`\n================================================================`);
console.log(`Audit Summary:`);
console.log(`Total Topics: ${topics.length}`);
console.log(`Passed:       ${passedCount} / ${topics.length}`);
console.log(`Failed:       ${failedCount} / ${topics.length}`);
console.log(`================================================================`);

if (issues.length > 0) {
  console.log(`\nIssues detected (${issues.length}):`);
  for (const issue of issues.slice(0, 15)) {
    console.log(`  - ${issue}`);
  }
  if (issues.length > 15) {
    console.log(`  ... and ${issues.length - 15} more topics require regeneration.`);
  }
} else {
  console.log(`\nSUCCESS: All ${topics.length} Social Studies pages are 100% verified, rich, and meet quality standards!`);
}
