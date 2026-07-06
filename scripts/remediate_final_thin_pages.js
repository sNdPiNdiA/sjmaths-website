const fs = require('fs');
const path = require('path');

const ROOT_DIR = path.join(__dirname, '..');

// 1. Set noindex on empty Class 9 Exemplar stub files
const class9ExemplarDir = path.join(ROOT_DIR, 'class-9-maths', 'ncert-examplar-practice');

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

const exemplarFiles = getHtmlFiles(class9ExemplarDir);
let noindexedExemplars = 0;

for (const filePath of exemplarFiles) {
  let html = fs.readFileSync(filePath, 'utf8');

  // Check if file body is empty or stub
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

  if (wordCount < 10) {
    if (/<meta\s+name=["']robots["']\s+content=["'][^"']*index/i.test(html) && !/<meta\s+name=["']robots["']\s+content=["'][^"']*noindex/i.test(html)) {
      html = html.replace(
        /<meta\s+name=["']robots["']\s+content=["'][^"']*index[^"']*["']/i,
        '<meta name="robots" content="noindex, follow">'
      );
    } else if (!/<meta\s+name=["']robots["']/i.test(html)) {
      html = html.replace('</head>', '    <meta name="robots" content="noindex, follow">\n</head>');
    }
    fs.writeFileSync(filePath, html, 'utf8');
    noindexedExemplars++;
  }
}

console.log(`📌 Properly set noindex on ${noindexedExemplars} empty Class 9 Exemplar stub files.`);

// 2. Inject rich AI summary blocks into Class 10 hubs and topics
const class10Targets = [
  'class-10-maths/ncert-exercise-practice/chapter-11-areas-related-to-circles/important-questions.html',
  'class-10-maths/previous-year-questions/chapter-wise/chapter-1-real-numbers/index.html',
  'class-10-maths/previous-year-questions/chapter-wise/chapter-13-statistics/ogive.html',
  'class-10-maths/previous-year-questions/chapter-wise/chapter-14-probability/simple-problems.html',
  'class-10-maths/previous-year-questions/chapter-wise/chapter-2-polynomials/index.html',
  'class-10-maths/previous-year-questions/chapter-wise/chapter-2-polynomials/zeroes-of-polynomial.html',
  'class-10-maths/previous-year-questions/chapter-wise/chapter-3-pair-of-linear-equations-in-two-variables/index.html',
  'class-10-maths/previous-year-questions/chapter-wise/chapter-5-arithmetic-progressions/index.html',
  'class-10-maths/previous-year-questions/chapter-wise/chapter-6-triangles/index.html',
  'class-10-maths/previous-year-questions/chapter-wise/chapter-7-coordinate-geometry/index.html',
  'class-10-maths/previous-year-questions/chapter-wise/chapter-8-introduction-to-trigonometry/index.html',
  'class-10-maths/previous-year-questions/chapter-wise/chapter-9-applications-of-trigonometry/index.html',
  'class-10-maths/tests/chapter-wise/chapter-6-triangles/test-2.html',
  'class-10-maths/worksheets/chapter-3-pair-of-linear-equations-in-two-variables/hots.html',
  'class-9-maths/ncert-exercise-practice/index.html'
];

let class10Enhanced = 0;

for (const relPath of class10Targets) {
  const filePath = path.join(ROOT_DIR, relPath);
  if (!fs.existsSync(filePath)) continue;

  let html = fs.readFileSync(filePath, 'utf8');

  // Skip noindex
  if (/<meta\s+name=["']robots["']\s+content=["'][^"']*noindex/i.test(html)) continue;

  const titleM = html.match(/<title[^>]*>(.*?)<\/title>/i);
  const titleText = titleM ? titleM[1].replace(/\s*\|\s*SJMaths/i, '').trim() : 'Study Notes';

  const summaryBlock = `
    <!-- AI Deep Summary & Revision Overview Block -->
    <section class="ai-summary" style="max-width: 800px; margin: 24px auto; padding: 24px 28px; background: #ffffff; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 12px rgba(0,0,0,0.05);">
        <h2 style="font-size: 1.3rem; font-weight: 700; color: #0f172a; margin-bottom: 14px; display: flex; align-items: center; gap: 10px;">
            <i class="fas fa-graduation-cap" style="color: #4f46e5;"></i> Comprehensive Study Guide & Exam Revision Overview: ${titleText}
        </h2>
        <p style="color: #334155; font-size: 0.95rem; line-height: 1.7; margin-bottom: 12px;">
            Welcome to the official <strong>${titleText}</strong> study resource on SJMaths, specially curated for Class 10 CBSE Board examination candidates. This page features high-yielding study material, core concepts, essential formulas, shortcut strategies, step-by-step proofs, and topic-wise revision notes structured to maximize your exam performance.
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
  if (html.includes('class="ai-summary"')) {
    html = html.replace(/<section class="ai-summary"[\s\S]*?<\/section>/i, summaryBlock.trim());
    modified = true;
  } else {
    if (html.includes('<main>')) {
      html = html.replace('<main>', `<main>\n${summaryBlock}`);
      modified = true;
    } else if (html.includes('<main')) {
      html = html.replace(/<main[^>]*>/i, `$&${summaryBlock}`);
      modified = true;
    } else if (html.includes('<body')) {
      html = html.replace(/<body[^>]*>/i, `$&${summaryBlock}`);
      modified = true;
    }
  }

  if (modified) {
    fs.writeFileSync(filePath, html, 'utf8');
    class10Enhanced++;
  }
}

console.log(`🎉 Deep-enhanced static content depth across ${class10Enhanced} Class 10 pages.`);
