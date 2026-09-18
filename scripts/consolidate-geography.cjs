const fs = require('fs');
const path = require('path');

const config = JSON.parse(fs.readFileSync('scripts/geography_consolidation_config.json', 'utf8'));

console.log(`Starting consolidation for ${config.length} natural clusters...`);

function readIfExists(filePath) {
  if (fs.existsSync(filePath)) {
    return fs.readFileSync(filePath, 'utf8');
  }
  return null;
}

function readJsonIfExists(filePath) {
  if (fs.existsSync(filePath)) {
    try {
      return JSON.parse(fs.readFileSync(filePath, 'utf8'));
    } catch (e) {
      console.error(`Error parsing JSON from ${filePath}:`, e.message);
      return null;
    }
  }
  return null;
}

function writeJson(filePath, data) {
  const dir = path.dirname(filePath);
  if (!fs.existsSync(dir)) fs.mkdirSync(dir, { recursive: true });
  fs.writeFileSync(filePath, JSON.stringify(data, null, 2), 'utf8');
}

function deduplicateArray(arr, keyProp = 'question') {
  if (!Array.isArray(arr)) return [];
  const seen = new Set();
  const result = [];
  for (const item of arr) {
    const key = item[keyProp] ? item[keyProp].toLowerCase().trim() : JSON.stringify(item);
    if (!seen.has(key)) {
      seen.add(key);
      result.push(item);
    }
  }
  return result;
}

let totalSourcesRemoved = 0;
let totalTargetsCreated = 0;

for (const group of config) {
  const targetRel = group.target.replace(/^\//, '').replace(/\/$/, ''); // e.g. geography/physical-geography/...
  const targetDir = path.join(process.cwd(), targetRel);
  const targetIndexPath = path.join(targetDir, 'index.html');

  console.log(`\nProcessing target: ${group.target}`);
  console.log(`Sources: ${group.sources.join(', ')}`);

  // 1. Gather all data from existing source pages
  let combinedStudyNotes = [];
  let combinedQuickRevision = [];
  let combinedQuiz = [];
  let combinedPYQ = [];
  let combinedTopicTest = [];
  let baseHtmlTemplate = null;

  for (const src of group.sources) {
    const srcRel = src.replace(/^\//, '').replace(/\/$/, '');
    const srcDir = path.join(process.cwd(), srcRel);
    const srcIndexPath = path.join(srcDir, 'index.html');

    const html = readIfExists(srcIndexPath);
    if (html) {
      if (!baseHtmlTemplate) baseHtmlTemplate = html;
      
      // Extract study notes content if present
      const notesMatch = html.match(/<section[^>]*id="study-notes"[^>]*>([\s\S]*?)<\/section>/i) ||
                         html.match(/<article[^>]*id="notes"[^>]*>([\s\S]*?)<\/article>/i) ||
                         html.match(/<div[^>]*class="notes-content"[^>]*>([\s\S]*?)<\/div>/i);
      if (notesMatch) {
        combinedStudyNotes.push(notesMatch[1].trim());
      }

      // Extract quick revision content if present
      const revMatch = html.match(/<section[^>]*id="quick-revision"[^>]*>([\s\S]*?)<\/section>/i) ||
                       html.match(/<div[^>]*id="revision"[^>]*>([\s\S]*?)<\/div>/i);
      if (revMatch) {
        combinedQuickRevision.push(revMatch[1].trim());
      }
    }

    const quizData = readJsonIfExists(path.join(srcDir, 'quiz.json'));
    if (quizData) combinedQuiz = combinedQuiz.concat(Array.isArray(quizData) ? quizData : (quizData.questions || []));

    const pyqData = readJsonIfExists(path.join(srcDir, 'pyq.json'));
    if (pyqData) combinedPYQ = combinedPYQ.concat(Array.isArray(pyqData) ? pyqData : (pyqData.questions || []));

    const testData = readJsonIfExists(path.join(srcDir, 'topic-test.json'));
    if (testData) combinedTopicTest = combinedTopicTest.concat(Array.isArray(testData) ? testData : (testData.questions || []));
  }

  // Deduplicate quizzes, pyqs, and topic tests
  const finalQuiz = deduplicateArray(combinedQuiz);
  const finalPYQ = deduplicateArray(combinedPYQ);
  const finalTopicTest = deduplicateArray(combinedTopicTest);

  // If target directory doesn't exist, create it
  if (!fs.existsSync(targetDir)) {
    fs.mkdirSync(targetDir, { recursive: true });
  }

  // Save unified JSON files
  if (finalQuiz.length > 0) writeJson(path.join(targetDir, 'quiz.json'), finalQuiz);
  if (finalPYQ.length > 0) writeJson(path.join(targetDir, 'pyq.json'), finalPYQ);
  if (finalTopicTest.length > 0) writeJson(path.join(targetDir, 'topic-test.json'), finalTopicTest);

  // 2. Build or Update target index.html
  let existingTargetHtml = readIfExists(targetIndexPath);
  let finalHtml = existingTargetHtml || baseHtmlTemplate;

  if (finalHtml) {
    // Update Title & Meta Tags
    finalHtml = finalHtml.replace(/<title>[\s\S]*?<\/title>/i, `<title>${group.title} | UP TGT &amp; PGT Geography</title>`);
    
    // Update H1 header
    if (/<h1[^>]*>[\s\S]*?<\/h1>/i.test(finalHtml)) {
      finalHtml = finalHtml.replace(/<h1[^>]*>[\s\S]*?<\/h1>/i, `<h1>${group.title}</h1>`);
    }

    // Update canonical link
    const canonicalUrl = `https://sjmaths.com${group.target}`;
    if (/<link rel="canonical"[^>]*>/i.test(finalHtml)) {
      finalHtml = finalHtml.replace(/<link rel="canonical"[^>]*>/i, `<link rel="canonical" href="${canonicalUrl}" />`);
    } else if (/<\/head>/i.test(finalHtml)) {
      finalHtml = finalHtml.replace(/<\/head>/i, `  <link rel="canonical" href="${canonicalUrl}" />\n</head>`);
    }

    // If we combined study notes from multiple sub-sources and creating new target, inject combined notes
    if (!existingTargetHtml && combinedStudyNotes.length > 1) {
      const mergedNotesHtml = combinedStudyNotes.join('\n<hr class="section-divider" style="margin:2.5rem 0;border:0;border-top:1px dashed #cbd5e1;" />\n');
      if (/<section[^>]*id="study-notes"[^>]*>([\s\S]*?)<\/section>/i.test(finalHtml)) {
        finalHtml = finalHtml.replace(/(<section[^>]*id="study-notes"[^>]*>)([\s\S]*?)(<\/section>)/i, `$1\n${mergedNotesHtml}\n$3`);
      }
    }

    fs.writeFileSync(targetIndexPath, finalHtml, 'utf8');
    totalTargetsCreated++;
    console.log(`✓ Target written: ${targetIndexPath}`);
  } else {
    console.warn(`! No HTML found for target: ${targetIndexPath}`);
  }

  // 3. Remove superseded source folders (if source !== target)
  for (const src of group.sources) {
    if (src === group.target) continue; // Keep target if it was one of the sources
    const srcRel = src.replace(/^\//, '').replace(/\/$/, '');
    const srcDir = path.join(process.cwd(), srcRel);
    if (fs.existsSync(srcDir)) {
      fs.rmSync(srcDir, { recursive: true, force: true });
      totalSourcesRemoved++;
      console.log(`  - Deleted superseded source folder: ${srcRel}`);
    }
  }
}

console.log(`\nConsolidation complete! Targets created/updated: ${totalTargetsCreated}, Source folders cleaned up: ${totalSourcesRemoved}`);
