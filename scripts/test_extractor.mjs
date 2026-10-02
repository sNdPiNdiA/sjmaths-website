import fs from 'node:fs';
import path from 'node:path';

function extractTopicData(filePath) {
  const html = fs.readFileSync(filePath, 'utf8');

  // 1. Lead desc
  const leadMatch = html.match(/<p class="lead-desc">([\s\S]*?)<\/p>/);
  const leadDesc = leadMatch ? leadMatch[1].trim() : '';

  // 2. Syllabus focus
  const focusMatch = html.match(/<strong>Syllabus Focus &amp; High-Yield Strategy:<\/strong>([\s\S]*?)<\/p>/);
  const syllabusFocus = focusMatch ? focusMatch[1].trim() : '';

  // 3. Concepts
  const concepts = [];
  const conceptRegex = /<div class="prep-card">\s*<h2>\s*<i class="fas fa-bookmark"[^>]*><\/i>\s*<span>([^<]+)<\/span>\s*<\/h2>\s*<div class="topic-content-body">([\s\S]*?)<\/div>\s*<\/div>/g;
  let cMatch;
  while ((cMatch = conceptRegex.exec(html)) !== null) {
    concepts.push({
      heading: cMatch[1].trim(),
      html_content: cMatch[2].trim()
    });
  }

  // 4. Comparative table
  let comparativeTable = null;
  const tableTitleMatch = html.match(/<i class="fas fa-table-columns"[^>]*><\/i>\s*<span>([^<]+)<\/span>/);
  const tableMatch = html.match(/<table class="prep-table">([\s\S]*?)<\/table>/);
  if (tableTitleMatch && tableMatch) {
    const tableHtml = tableMatch[1];
    const ths = [...tableHtml.matchAll(/<th>([\s\S]*?)<\/th>/g)].map(m => m[1].replace(/<[^>]+>/g, '').trim());
    const rows = [];
    const trRegex = /<tr>([\s\S]*?)<\/tr>/g;
    let trMatch;
    // skip the first tr if it's the header
    let isHeader = true;
    while ((trMatch = trRegex.exec(tableHtml)) !== null) {
      if (trMatch[1].includes('<th')) continue;
      const tds = [...trMatch[1].matchAll(/<td>([\s\S]*?)<\/td>/g)].map(m => m[1].trim());
      if (tds.length) rows.push(tds);
    }
    comparativeTable = {
      title: tableTitleMatch[1].trim(),
      headers: ths,
      rows: rows
    };
  }

  // 5. Test Data (10 MCQs)
  let testData = [];
  const testDataMatch = html.match(/const testData\s*=\s*(\[[\s\S]*?\]);\s*<\/script>/);
  if (testDataMatch) {
    try {
      testData = JSON.parse(testDataMatch[1]);
    } catch (e) {
      console.warn('Failed to parse testData JSON directly:', e.message);
    }
  }

  // 6. Revision Facts
  const facts = [];
  const factRegex = /<div class="revision-fact-row">\s*<span class="fact-num-badge">[^<]+<\/span>\s*<div class="fact-text-col">([\s\S]*?)<\/div>\s*<\/div>/g;
  let fMatch;
  while ((fMatch = factRegex.exec(html)) !== null) {
    facts.push(fMatch[1].trim());
  }

  // 7. Mnemonics
  const mnemonics = [];
  const mnemRegex = /<div class="mnemonic-card">[\s\S]*?<h3[^>]*>[\s\S]*?<i class="fas fa-lightbulb"><\/i>\s*([\s\S]*?)<\/h3>[\s\S]*?<code>([\s\S]*?)<\/code>[\s\S]*?<p[^>]*>([\s\S]*?)<\/p>\s*<\/div>/g;
  let mMatch;
  while ((mMatch = mnemRegex.exec(html)) !== null) {
    mnemonics.push({
      title: mMatch[1].trim(),
      acronym: mMatch[2].trim(),
      expansion: mMatch[3].trim()
    });
  }

  // 8. Exam Traps
  const traps = [];
  const trapRegex = /<div class="trap-card-item">[\s\S]*?<p[^>]*>([\s\S]*?)<\/p>\s*<\/div>\s*<\/div>/g;
  let tMatch;
  while ((tMatch = trapRegex.exec(html)) !== null) {
    traps.push(tMatch[1].trim());
  }

  // 9. Checklist
  const checklist = [];
  const chkRegex = /<label class="mastery-check-item">[\s\S]*?<span>([\s\S]*?)<\/span>\s*<\/label>/g;
  let chkMatch;
  while ((chkMatch = chkRegex.exec(html)) !== null) {
    checklist.push(chkMatch[1].trim());
  }

  return {
    leadDesc,
    syllabusFocus,
    concepts,
    comparativeTable,
    testData,
    facts,
    mnemonics,
    traps,
    checklist
  };
}

const samples = [
  'up-upper-primary-teacher/social-studies/indus-valley-civilisation/index.html',
  'up-upper-primary-teacher/science/daily-life-science/index.html',
  'up-upper-primary-teacher/general-knowledge/indian-freedom-struggle/index.html'
];

for (const s of samples) {
  console.log('Testing sample:', s);
  const res = extractTopicData(s);
  console.log('  Concepts Count:', res.concepts.length);
  console.log('  Comparative Table Rows:', res.comparativeTable?.rows?.length);
  console.log('  MCQs Count:', res.testData.length);
  console.log('  Facts Count:', res.facts.length);
  console.log('  Mnemonics Count:', res.mnemonics.length);
  console.log('  Traps Count:', res.traps.length);
  console.log('  Checklist Count:', res.checklist.length);
}
