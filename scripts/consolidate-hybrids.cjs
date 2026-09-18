const fs = require('fs');
const path = require('path');

const config = JSON.parse(fs.readFileSync('scripts/geography_hybrids_config.json', 'utf8'));

console.log(`Starting consolidation for ${config.length} hybrid clusters...`);

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

for (const group of config) {
  const targetRel = group.target.replace(/^\//, '').replace(/\/$/, '');
  const targetDir = path.join(process.cwd(), targetRel);
  const targetIndexPath = path.join(targetDir, 'index.html');

  console.log(`\nProcessing target: ${group.target}`);

  let combinedStudyNotes = [];
  let combinedQuiz = [];
  let combinedPYQ = [];
  let combinedTopicTest = [];
  let baseHtmlTemplate = readIfExists(targetIndexPath);

  for (const src of group.sources) {
    const srcRel = src.replace(/^\//, '').replace(/\/$/, '');
    const srcDir = path.join(process.cwd(), srcRel);
    const srcIndexPath = path.join(srcDir, 'index.html');

    const html = readIfExists(srcIndexPath);
    if (html) {
      if (!baseHtmlTemplate) baseHtmlTemplate = html;
      
      const notesMatch = html.match(/<section[^>]*id="study-notes"[^>]*>([\s\S]*?)<\/section>/i) ||
                         html.match(/<article[^>]*id="notes"[^>]*>([\s\S]*?)<\/article>/i) ||
                         html.match(/<div[^>]*class="notes-content"[^>]*>([\s\S]*?)<\/div>/i);
      if (notesMatch) {
        combinedStudyNotes.push(notesMatch[1].trim());
      }
    }

    const quizData = readJsonIfExists(path.join(srcDir, 'quiz.json'));
    if (quizData) combinedQuiz = combinedQuiz.concat(Array.isArray(quizData) ? quizData : (quizData.questions || []));

    const pyqData = readJsonIfExists(path.join(srcDir, 'pyq.json'));
    if (pyqData) combinedPYQ = combinedPYQ.concat(Array.isArray(pyqData) ? pyqData : (pyqData.questions || []));

    const testData = readJsonIfExists(path.join(srcDir, 'topic-test.json'));
    if (testData) combinedTopicTest = combinedTopicTest.concat(Array.isArray(testData) ? testData : (testData.questions || []));
  }

  const finalQuiz = deduplicateArray(combinedQuiz);
  const finalPYQ = deduplicateArray(combinedPYQ);
  const finalTopicTest = deduplicateArray(combinedTopicTest);

  if (!fs.existsSync(targetDir)) {
    fs.mkdirSync(targetDir, { recursive: true });
  }

  if (finalQuiz.length > 0) writeJson(path.join(targetDir, 'quiz.json'), finalQuiz);
  if (finalPYQ.length > 0) writeJson(path.join(targetDir, 'pyq.json'), finalPYQ);
  if (finalTopicTest.length > 0) writeJson(path.join(targetDir, 'topic-test.json'), finalTopicTest);

  let finalHtml = baseHtmlTemplate;
  if (finalHtml) {
    finalHtml = finalHtml.replace(/<title>[\s\S]*?<\/title>/i, `<title>${group.title} | UP TGT &amp; PGT Geography</title>`);
    if (/<h1[^>]*>[\s\S]*?<\/h1>/i.test(finalHtml)) {
      finalHtml = finalHtml.replace(/<h1[^>]*>[\s\S]*?<\/h1>/i, `<h1>${group.title}</h1>`);
    }
    const canonicalUrl = `https://sjmaths.com${group.target}`;
    if (/<link rel="canonical"[^>]*>/i.test(finalHtml)) {
      finalHtml = finalHtml.replace(/<link rel="canonical"[^>]*>/i, `<link rel="canonical" href="${canonicalUrl}" />`);
    } else if (/<\/head>/i.test(finalHtml)) {
      finalHtml = finalHtml.replace(/<\/head>/i, `  <link rel="canonical" href="${canonicalUrl}" />\n</head>`);
    }

    fs.writeFileSync(targetIndexPath, finalHtml, 'utf8');
    console.log(`✓ Target written: ${targetIndexPath}`);
  }

  // Delete superseded child folders (sources !== target)
  for (const src of group.sources) {
    if (src === group.target) continue;
    const srcRel = src.replace(/^\//, '').replace(/\/$/, '');
    const srcDir = path.join(process.cwd(), srcRel);
    if (fs.existsSync(srcDir)) {
      fs.rmSync(srcDir, { recursive: true, force: true });
      console.log(`  - Deleted superseded subtopic folder: ${srcRel}`);
    }
  }
}
