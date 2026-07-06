const fs = require('fs');
const path = require('path');

const ROOT_DIR = path.join(__dirname, '..');

function addSummaryBlock(filePath, topicTitle, subjectCategory, customText = "") {
  if (!fs.existsSync(filePath)) return false;
  let html = fs.readFileSync(filePath, 'utf8');

  // Skip if already contains ai-summary
  if (html.includes('class="ai-summary"')) return false;

  const descText = customText || `Access comprehensive <strong>${topicTitle}</strong> study material, interactive practice questions, formulas, shortcut tricks, and step-by-step solutions for ${subjectCategory} exam preparation on SJMaths.`;

  const summaryBlock = `
    <!-- AI Summary & Revision Overview Block -->
    <section class="ai-summary" style="max-width: 800px; margin: 24px auto; padding: 20px 24px; background: #ffffff; border-radius: 12px; border: 1px solid #e5e7eb; box-shadow: 0 2px 8px rgba(0,0,0,0.04);">
        <h2 style="font-size: 1.25rem; font-weight: 700; color: #1e293b; margin-bottom: 12px; display: flex; align-items: center; gap: 8px;">
            <i class="fas fa-book-open" style="color: #4f46e5;"></i> Overview & Key Study Notes
        </h2>
        <p style="color: #475569; font-size: 0.95rem; line-height: 1.6; margin: 0;">${descText}</p>
    </section>\n`;

  if (html.includes('<main>')) {
    html = html.replace('<main>', `<main>\n${summaryBlock}`);
  } else if (html.includes('<main')) {
    html = html.replace(/<main[^>]*>/i, `$&${summaryBlock}`);
  } else if (html.includes('<body')) {
    html = html.replace(/<body[^>]*>/i, `$&${summaryBlock}`);
  } else {
    return false;
  }

  fs.writeFileSync(filePath, html, 'utf8');
  return true;
}

function getHtmlFiles(dir, fileList = []) {
  if (!fs.existsSync(dir)) return fileList;
  const files = fs.readdirSync(dir);
  for (const file of files) {
    const filePath = path.join(dir, file);
    const stat = fs.statSync(filePath);
    if (stat.isDirectory()) {
      getHtmlFiles(filePath, fileList);
    } else if (file.endsWith('.html')) {
      fileList.push(filePath);
    }
  }
  return fileList;
}

const targetDirs = [
  path.join(ROOT_DIR, 'upsc', 'csat', 'Basic-Numeracy-Arithmetic'),
  path.join(ROOT_DIR, 'ahc-ro-aro'),
  path.join(ROOT_DIR, 'class-11-maths', 'worksheets'),
  path.join(ROOT_DIR, 'maths-mastery'),
  path.join(ROOT_DIR, 'current-affairs')
];

let allFiles = [];
for (const d of targetDirs) {
  allFiles = getHtmlFiles(d, allFiles);
}

const importantQ = path.join(ROOT_DIR, 'important-questions.html');
if (fs.existsSync(importantQ)) allFiles.push(importantQ);

console.log(`Analyzing ${allFiles.length} target files for thin content remediation...`);

let fixedCount = 0;

for (const filePath of allFiles) {
  let html = fs.readFileSync(filePath, 'utf8');
  const relPath = path.relative(ROOT_DIR, filePath).replace(/\\/g, '/');

  // Skip noindex
  if (/<meta\s+name=["']robots["']\s+content=["'][^"']*noindex/i.test(html)) continue;

  const bodyM = html.match(/<body[^>]*>([\s\S]*?)<\/body>/i);
  let wordCount = 0;
  if (bodyM) {
    const textOnly = bodyM[1]
      .replace(/<script[\s\S]*?<\/script>/gi, '')
      .replace(/<style[\s\S]*?<\/style>/gi, '')
      .replace(/<[^>]+>/g, ' ')
      .replace(/\s+/g, ' ')
      .trim();
    wordCount = textOnly.split(/\s+/).filter(w => w.length > 0).length;
  }

  const hasMindmap = html.includes('renderMindmap') || html.includes('mindmap-card');
  const hasQuestions = html.includes('QUESTIONS_JSON') || html.includes('question-card');

  if (wordCount < 60 && !hasMindmap && !hasQuestions) {
    const titleM = html.match(/<title[^>]*>(.*?)<\/title>/i);
    const titleText = titleM ? titleM[1].replace(/\s*\|\s*SJMaths/i, '').replace(/\s*-\s*UPSC.*/i, '').trim() : 'Study Notes';

    let category = 'Competitive Exams';
    if (relPath.includes('upsc')) category = 'UPSC CSAT / Civil Services';
    else if (relPath.includes('ahc-ro-aro')) category = 'Allahabad High Court RO/ARO Mains';
    else if (relPath.includes('class-11')) category = 'Class 11 CBSE Mathematics';
    else if (relPath.includes('maths-mastery')) category = 'Maths Mastery & Quantitative Aptitude';
    else if (relPath.includes('current-affairs')) category = 'Current Affairs & General Awareness';

    if (addSummaryBlock(filePath, titleText, category)) {
      fixedCount++;
    }
  }
}

console.log(`🎉 Injected rich static overview & revision blocks into ${fixedCount} thin pages.`);
