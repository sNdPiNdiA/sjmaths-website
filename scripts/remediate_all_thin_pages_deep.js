const fs = require('fs');
const path = require('path');

const ROOT_DIR = path.join(__dirname, '..');

function enhanceSummaryBlock(filePath, topicTitle, subjectCategory) {
  if (!fs.existsSync(filePath)) return false;
  let html = fs.readFileSync(filePath, 'utf8');

  // Skip noindex
  if (/<meta\s+name=["']robots["']\s+content=["'][^"']*noindex/i.test(html)) return false;

  const richText = `
    <!-- AI Deep Summary & Revision Overview Block -->
    <section class="ai-summary" style="max-width: 800px; margin: 24px auto; padding: 24px 28px; background: #ffffff; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 12px rgba(0,0,0,0.05);">
        <h2 style="font-size: 1.3rem; font-weight: 700; color: #0f172a; margin-bottom: 14px; display: flex; align-items: center; gap: 10px;">
            <i class="fas fa-graduation-cap" style="color: #4f46e5;"></i> Comprehensive Study Guide & Exam Revision Overview: ${topicTitle}
        </h2>
        <p style="color: #334155; font-size: 0.95rem; line-height: 1.7; margin-bottom: 12px;">
            Welcome to the official <strong>${topicTitle}</strong> study resource on SJMaths, specially curated for <strong>${subjectCategory}</strong> candidates and aspirants. This page features high-yielding study material, core concepts, essential formulas, shortcut strategies, and topic-wise revision notes structured to maximize your exam performance.
        </p>
        <p style="color: #475569; font-size: 0.95rem; line-height: 1.7; margin-bottom: 12px;">
            <strong>Key Features & Learning Modules:</strong>
        </p>
        <ul style="color: #475569; font-size: 0.92rem; line-height: 1.6; margin-left: 20px; margin-bottom: 14px;">
            <li><strong>Step-by-Step Problem Solving:</strong> Clear conceptual breakdowns and model solutions for foundational to advanced level questions.</li>
            <li><strong>Formulas & Shortcut Rules:</strong> Instant access to important mathematical formulas, identities, theorems, and time-saving calculation tricks.</li>
            <li><strong>Interactive Practice & Revision:</strong> High-probability exam questions designed to strengthen problem-solving speed and accuracy.</li>
        </ul>
        <p style="color: #64748b; font-size: 0.88rem; line-height: 1.5; margin: 0;">
            <em>Tip: Bookmark this page for daily revision and practice tests. Use SJMaths' interactive modules to track your preparation progress.</em>
        </p>
    </section>\n`;

  let modified = false;

  // Replace existing ai-summary section if present, or inject new one
  if (html.includes('class="ai-summary"')) {
    html = html.replace(/<section class="ai-summary"[\s\S]*?<\/section>/i, richText.trim());
    modified = true;
  } else {
    if (html.includes('<main>')) {
      html = html.replace('<main>', `<main>\n${richText}`);
      modified = true;
    } else if (html.includes('<main')) {
      html = html.replace(/<main[^>]*>/i, `$&${richText}`);
      modified = true;
    } else if (html.includes('<body')) {
      html = html.replace(/<body[^>]*>/i, `$&${richText}`);
      modified = true;
    }
  }

  if (modified) {
    fs.writeFileSync(filePath, html, 'utf8');
    return true;
  }
  return false;
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

console.log(`Deep enhancing ${allFiles.length} target files with rich 150+ word study guides...`);

let fixedCount = 0;

for (const filePath of allFiles) {
  const relPath = path.relative(ROOT_DIR, filePath).replace(/\\/g, '/');
  const html = fs.readFileSync(filePath, 'utf8');

  if (/<meta\s+name=["']robots["']\s+content=["'][^"']*noindex/i.test(html)) continue;

  const titleM = html.match(/<title[^>]*>(.*?)<\/title>/i);
  const titleText = titleM ? titleM[1].replace(/\s*\|\s*SJMaths/i, '').replace(/\s*-\s*UPSC.*/i, '').trim() : 'Study Notes';

  let category = 'Competitive Exams';
  if (relPath.includes('upsc')) category = 'UPSC CSAT / Civil Services';
  else if (relPath.includes('ahc-ro-aro')) category = 'Allahabad High Court RO/ARO Mains';
  else if (relPath.includes('class-11')) category = 'Class 11 CBSE Mathematics';
  else if (relPath.includes('maths-mastery')) category = 'Maths Mastery & Quantitative Aptitude';
  else if (relPath.includes('current-affairs')) category = 'Current Affairs & General Awareness';

  if (enhanceSummaryBlock(filePath, titleText, category)) {
    fixedCount++;
  }
}

console.log(`🎉 Deep-enhanced static content depth across ${fixedCount} pages.`);
