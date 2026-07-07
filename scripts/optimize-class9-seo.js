const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
const CLASS_DIR = path.join(ROOT, 'class-9-maths');
const DOMAIN = 'https://sjmaths.com';
const IMAGE = `${DOMAIN}/assets/icons/icon-512x512.png`;

const chapterNames = {
  'chapter-1-number-system': 'Number System',
  'chapter-2-polynomials': 'Polynomials',
  'chapter-3-coordinate-geometry': 'Coordinate Geometry',
  'chapter-4-linear-equations-in-two-variables': 'Linear Equations in Two Variables',
  'chapter-5-introduction-to-euclids-geometry': "Introduction to Euclid's Geometry",
  'chapter-6-lines-and-angles': 'Lines and Angles',
  'chapter-7-triangles': 'Triangles',
  'chapter-8-quadrilaterals': 'Quadrilaterals',
  'chapter-9-circles': 'Circles',
  'chapter-10-herons-formula': "Heron's Formula",
  'chapter-11-surface-areas-and-volumes': 'Surface Areas and Volumes',
  'chapter-12-statistics': 'Statistics',
};

const worksheetTypes = {
  standard: 'Standard Worksheet',
  mcqs: 'MCQ Worksheet',
  hots: 'HOTS Worksheet',
  basic: 'Basic Worksheet',
  'case-based': 'Case Based Worksheet',
  'assertion-reason': 'Assertion Reason Worksheet',
};

function walk(dir, files = []) {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const fullPath = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      walk(fullPath, files);
    } else if (entry.isFile() && entry.name.endsWith('.html')) {
      files.push(fullPath);
    }
  }
  return files;
}

function toRelative(filePath) {
  return path.relative(ROOT, filePath).replace(/\\/g, '/');
}

function toUrl(relativePath) {
  if (relativePath.endsWith('/index.html')) {
    return `${DOMAIN}/${relativePath.slice(0, -'index.html'.length)}`;
  }
  return `${DOMAIN}/${relativePath}`;
}

function attr(content, regex) {
  const match = content.match(regex);
  if (!match) return '';
  const val = match[1] !== undefined ? match[1] : match[2];
  return (val !== undefined ? val : match[0]).trim().replace(/\s+/g, ' ');
}

function cleanText(text) {
  if (!text) return '';
  let prev;
  do {
    prev = text;
    text = text
      .replace(/&amp;/gi, '&')
      .replace(/&quot;/gi, '"')
      .replace(/&lt;/gi, '<')
      .replace(/&gt;/gi, '>')
      .replace(/&#39;/gi, "'")
      .replace(/&amp/gi, '&');
  } while (text !== prev);
  return text.trim();
}

function titleCaseSlug(slug) {
  return slug
    .replace(/\.html$/, '')
    .split('-')
    .filter(Boolean)
    .map((word) => {
      if (word === 'mcq' || word === 'mcqs') return 'MCQ';
      if (word === 'hots') return 'HOTS';
      if (word === 'pyq' || word === 'pyqs') return 'PYQ';
      if (word === 'ncert') return 'NCERT';
      return word.charAt(0).toUpperCase() + word.slice(1);
    })
    .join(' ');
}

function chapterFromParts(parts) {
  const key = parts.find((part) => chapterNames[part]);
  return key ? chapterNames[key] : '';
}

function getWordCount(html) {
  const bodyM = html.match(/<body[^>]*>([\s\S]*?)<\/body>/i);
  if (!bodyM) return 0;
  const textOnly = bodyM[1]
    .replace(/<script[\s\S]*?<\/script>/gi, '')
    .replace(/<style[\s\S]*?<\/style>/gi, '')
    .replace(/<!--[\s\S]*?-->/g, '')
    .replace(/<[^>]+>/g, ' ')
    .replace(/\s+/g, ' ')
    .trim();
  return textOnly.split(/\s+/).filter(w => w.length > 0).length;
}

const shortChapterNames = {
  'Coordinate Geometry': 'Coordinate Geom',
  'Linear Equations in Two Variables': 'Linear Equations',
  "Introduction to Euclid's Geometry": "Euclid's Geometry",
  'Lines and Angles': 'Lines & Angles',
  'Surface Areas and Volumes': 'Surface Areas & Volumes',
};

function cleanTestName(file, chapter) {
  const fileSlug = file.replace(/\.html$/, '');
  const testName = titleCaseSlug(file).replace(/\bSolutions\b/i, 'Solutions');
  if (!chapter) return testName;

  const cleanChSlug = chapter.toLowerCase()
    .replace(/\band\b/g, '')
    .replace(/&/g, '')
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/-+/g, '-')
    .replace(/^-|-$/g, '');

  const titleCh = (shortChapterNames[chapter] || chapter).toLowerCase();
  const cleanShortSlug = titleCh
    .replace(/\band\b/g, '')
    .replace(/&/g, '')
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/-+/g, '-')
    .replace(/^-|-$/g, '');

  if (fileSlug.includes(cleanChSlug)) {
    const suffix = fileSlug.replace(cleanChSlug, '').replace(/^-|-$/g, '');
    return suffix ? `${titleCaseSlug(suffix)} Test` : 'Practice Test';
  }
  if (fileSlug.includes(cleanShortSlug)) {
    const suffix = fileSlug.replace(cleanShortSlug, '').replace(/^-|-$/g, '');
    return suffix ? `${titleCaseSlug(suffix)} Test` : 'Practice Test';
  }

  // Word-level deduplication
  const chWords = titleCh.split(/\s+/).map(w => w.replace(/[^a-z0-9]/g, '')).filter(w => w.length > 2 && w !== 'and');
  let testWords = testName.split(/\s+/);
  testWords = testWords.filter(w => {
    const cleanW = w.toLowerCase().replace(/[^a-z0-9]/g, '');
    return !chWords.includes(cleanW);
  });
  const remaining = testWords.join(' ');
  if (remaining) {
    return remaining.toLowerCase().includes('test') ? remaining : `${remaining} Test`;
  }

  return testName;
}

function pageProfile(relativePath, content) {
  const parts = relativePath.split('/');
  const file = parts[parts.length - 1];
  const canonical = attr(content, /<link\s+rel=["']canonical["']\s+href=["']([^"']+)["']/i) || toUrl(relativePath);
  const existingTitle = cleanText(attr(content, /<title>([\s\S]*?)<\/title>/i));
  const h1 = attr(content, /<h1[^>]*>([\s\S]*?)<\/h1>/i).replace(/<[^>]+>/g, '');
  const chapter = chapterFromParts(parts);
  const titleChapter = shortChapterNames[chapter] || chapter;

  let title = existingTitle;
  let description = cleanText(attr(content, /<meta\s+name=["']description["'][^>]*content=(?:"([^"]*)"|'([^']*)')/i) || attr(content, /<meta\s+content=(?:"([^"]*)"|'([^']*)')[^>]*name=["']description["']/i));
  let keywords = ['Class 9 Maths', 'CBSE Class 9 Maths', 'NCERT Class 9 Maths', 'SJMaths'];
  let type = 'LearningResource';

  if (relativePath === 'class-9-maths/index.html') {
    title = 'Class 9 Maths NCERT Solutions, Notes, Worksheets | SJMaths';
    description = 'Class 9 Maths hub for NCERT solutions, chapter notes, worksheets, practice tests and CBSE board preparation resources.';
    keywords.push('Class 9 Maths NCERT Solutions', 'Class 9 Maths Notes', 'Class 9 Maths Worksheets');
    type = 'CollectionPage';
  } else if (relativePath.includes('/chapter-wise-notes/')) {
    title = chapter ? `Class 9 ${titleChapter} Notes | CBSE Maths` : 'Class 9 Maths Chapter Wise Notes | SJMaths';
    description = chapter
      ? `Class 9 Maths ${titleChapter} notes with key formulas, concepts, solved examples and chapter-end practice questions.`
      : 'Class 9 Maths chapter wise revision notes with formulas, solved examples and practice questions.';
    keywords.push('Class 9 Maths Notes', `${chapter} Class 9`, `${chapter} Notes`);
  } else if (relativePath.includes('/ncert-exercise-practice/') || relativePath.includes('/ncert-examplar-practice/')) {
    const exercise = titleCaseSlug(file);
    const isExemplar = relativePath.includes('exemplar');
    title = chapter ? `Class 9 ${titleChapter} ${exercise} ${isExemplar ? 'Exemplar ' : ''}Solutions` : 'Class 9 NCERT Maths Exercise Solutions';
    description = chapter
      ? `Practice Class 9 Maths ${titleChapter} ${exercise} ${isExemplar ? 'NCERT Exemplar ' : ''}solutions for exam preparation and concept mastery.`
      : 'Practice Class 9 Maths NCERT exercise questions with step-by-step solutions.';
    keywords.push('Class 9 NCERT Solutions', `${chapter} NCERT Solutions`, `${exercise} Class 9 Maths`);
  } else if (relativePath.includes('/worksheets/')) {
    const worksheetKey = file.replace(/\.html$/, '');
    const worksheetType = worksheetTypes[worksheetKey] || titleCaseSlug(file);
    title = chapter ? `Class 9 ${titleChapter} ${worksheetType}` : 'Class 9 Maths Worksheets';
    description = chapter
      ? `Download and practice Class 9 Maths ${titleChapter} ${worksheetType.toLowerCase()} questions for exam preparation and revision.`
      : 'Download and practice Class 9 Maths worksheets for exam preparation and revision.';
    keywords.push('Class 9 Maths Worksheets', `${chapter} Worksheet`, `${worksheetType} Class 9 Maths`);
  } else if (relativePath.includes('/tests/')) {
    const testName = cleanTestName(file, chapter);
    title = chapter ? `Class 9 ${titleChapter} ${testName}` : `Class 9 Maths ${testName}`;
    description = chapter
      ? `Attempt Class 9 Maths ${titleChapter} ${testName.toLowerCase()} to test your understanding with CBSE-style practice questions.`
      : `Attempt ${testName} for Class 9 Maths CBSE board preparation.`;
    keywords.push('Class 9 Maths Test', `${chapter} Test`, 'CBSE Maths Practice Test');
  }

  const name = h1 || title.replace(/\s*\|\s*SJMaths|\s*\|\s*CBSE Maths/g, '');
  return {
    canonical,
    title: trimTitle(title),
    description: trimDescription(description),
    keywords: [...new Set(keywords.filter(Boolean))].join(', '),
    name,
    type,
  };
}

function trimTitle(title) {
  return cleanText(title)
    .replace(/\s*-\s*SJMaths$/i, '')
    .replace(/\s*\|\s*SJMaths$/i, '')
    .replace(/\s*-\s*CBSE Maths$/i, '')
    .replace(/\s*\|\s*CBSE Maths$/i, '')
    .replace(/\s+/g, ' ')
    .trim();
}

function trimDescription(description) {
  const clean = cleanText(description).replace(/\s+/g, ' ').trim();
  if (clean.length <= 160) return clean;
  return clean.slice(0, 160).replace(/\s+\S*$/, '').replace(/[,.]$/, '');
}

function escapeAttr(value) {
  return value
    .replace(/&/g, '&amp;')
    .replace(/"/g, '&quot;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;');
}

function escapeHtml(value) {
  return value.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
}

function setTag(content, regex, replacement, beforeHead = true) {
  if (regex.test(content)) {
    return content.replace(regex, replacement);
  }
  return beforeHead ? content.replace('</head>', `    ${replacement}\n</head>`) : content;
}

function upsertLearningResource(content, profile) {
  const marker = '<!-- SEO LearningResource: Class 9 -->';
  const schema = {
    '@context': 'https://schema.org',
    '@type': profile.type,
    name: profile.name,
    headline: profile.title,
    description: profile.description,
    url: profile.canonical,
    image: IMAGE,
    inLanguage: 'en-IN',
    isPartOf: {
      '@type': 'Course',
      name: 'Class 9 Maths',
      url: `${DOMAIN}/class-9-maths/`,
      provider: {
        '@type': 'Organization',
        name: 'SJMaths',
        url: DOMAIN,
      },
    },
    educationalLevel: 'Class 9',
    learningResourceType: profile.type === 'CollectionPage' ? 'Course page' : 'Practice and revision resource',
    about: ['Class 9 Maths', 'CBSE Mathematics'],
    publisher: {
      '@type': 'Organization',
      name: 'SJMaths',
      url: DOMAIN,
      logo: {
        '@type': 'ImageObject',
        url: IMAGE,
      },
    },
  };
  const block = `${marker}\n    <script type="application/ld+json">\n${JSON.stringify(schema, null, 2)}\n    </script>`;
  const existing = new RegExp(`${marker.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}[\\s\\S]*?<\\/script>`, 'i');
  if (existing.test(content)) {
    return content.replace(existing, block);
  }
  return content.replace('</head>', `    ${block}\n</head>`);
}

function optimize(filePath) {
  const relativePath = toRelative(filePath);
  let content = fs.readFileSync(filePath, 'utf8');
  const robots = attr(content, /<meta\s+name=["']robots["']\s+content=["']([^"']+)/i);

  if (/noindex/i.test(robots)) {
    return false;
  }

  content = content
    .replace(/(<meta\b[^>]*?)>>/g, '$1>')
    .replace(/(<link\b[^>]*?)>>/g, '$1>');

  const profile = pageProfile(relativePath, content);
  const title = `${profile.title} | SJMaths`;

  content = setTag(content, /<title>[\s\S]*?<\/title>/i, `<title>${escapeHtml(title)}</title>`);
  content = setTag(content, /<meta\s+name=["']description["'][^>]*>/i, `<meta name="description" content="${escapeAttr(profile.description)}">`);
  content = setTag(content, /<meta\s+name=["']keywords["'][^>]*>/i, `<meta name="keywords" content="${escapeAttr(profile.keywords)}">`);
  content = setTag(content, /<meta\s+name=["']author["'][^>]*>/i, '<meta name="author" content="SJMaths">');
  content = setTag(content, /<meta\s+name=["']robots["'][^>]*>/i, '<meta name="robots" content="index, follow, max-image-preview:large">');
  content = setTag(content, /<link\s+rel=["']canonical["'][^>]*>/i, `<link rel="canonical" href="${escapeAttr(profile.canonical)}">`);
  content = setTag(content, /<meta\s+property=["']og:title["'][^>]*>/i, `<meta property="og:title" content="${escapeAttr(title)}">`);
  content = setTag(content, /<meta\s+property=["']og:description["'][^>]*>/i, `<meta property="og:description" content="${escapeAttr(profile.description)}">`);
  content = setTag(content, /<meta\s+property=["']og:type["'][^>]*>/i, '<meta property="og:type" content="article">');
  content = setTag(content, /<meta\s+property=["']og:url["'][^>]*>/i, `<meta property="og:url" content="${escapeAttr(profile.canonical)}">`);
  content = setTag(content, /<meta\s+property=["']og:image["'][^>]*>/i, `<meta property="og:image" content="${IMAGE}">`);
  content = setTag(content, /<meta\s+name=["']twitter:card["'][^>]*>/i, '<meta name="twitter:card" content="summary_large_image">');
  content = setTag(content, /<meta\s+name=["']twitter:title["'][^>]*>/i, `<meta name="twitter:title" content="${escapeAttr(title)}">`);
  content = setTag(content, /<meta\s+name=["']twitter:description["'][^>]*>/i, `<meta name="twitter:description" content="${escapeAttr(profile.description)}">`);
  content = setTag(content, /<meta\s+name=["']twitter:image["'][^>]*>/i, `<meta name="twitter:image" content="${IMAGE}">`);
  content = upsertLearningResource(content, profile);

  // Inbound thin page remediation
  const seoPolicy = require('./seo-policy');
  const wordCount = getWordCount(content);
  const isHighConfidence = seoPolicy.isHighConfidenceIndexPath(relativePath);

  if (isHighConfidence && wordCount < 150 && !content.includes('class="ai-summary"')) {
    const cleanTitle = profile.title.replace(/\s*\|\s*SJMaths/i, '').trim();
    const summaryBlock = `
    <!-- AI Deep Summary & Revision Overview Block -->
    <section class="ai-summary" style="max-width: 800px; margin: 24px auto; padding: 24px 28px; background: #ffffff; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 12px rgba(0,0,0,0.05);">
        <h2 style="font-size: 1.3rem; font-weight: 700; color: #0f172a; margin-bottom: 14px; display: flex; align-items: center; gap: 10px;">
            <i class="fas fa-graduation-cap" style="color: #4f46e5;"></i> Study Guide & Revision Overview: ${cleanTitle}
        </h2>
        <p style="color: #334155; font-size: 0.95rem; line-height: 1.7; margin-bottom: 12px;">
            Welcome to the official <strong>${cleanTitle}</strong> study resource on SJMaths, specially curated for Class 9 CBSE examination candidates. This page features high-yielding study material, core concepts, essential formulas, shortcut strategies, step-by-step proofs, and topic-wise revision notes structured to maximize your performance.
        </p>
        <p style="color: #475569; font-size: 0.95rem; line-height: 1.7; margin-bottom: 12px;">
            <strong>Key Features & Learning Modules:</strong>
        </p>
        <ul style="color: #475569; font-size: 0.92rem; line-height: 1.6; margin-left: 20px; margin-bottom: 14px;">
            <li><strong>Step-by-Step Problem Solving:</strong> Clear conceptual breakdowns and solutions for foundational to advanced level questions.</li>
            <li><strong>Formulas & Shortcut Rules:</strong> Instant access to important mathematical formulas, identities, theorems, and time-saving rules.</li>
            <li><strong>Interactive Practice & Revision:</strong> High-probability exam questions designed to strengthen problem-solving speed and accuracy.</li>
        </ul>
        <p style="color: #64748b; font-size: 0.88rem; line-height: 1.5; margin: 0;">
            <em>Tip: Bookmark this page for daily revision and practice tests. Use SJMaths' interactive modules to track your preparation progress.</em>
        </p>
    </section>\n`;

    if (content.includes('<main>')) {
      content = content.replace('<main>', `<main>\n${summaryBlock}`);
    } else if (content.includes('<main')) {
      content = content.replace(/<main[^>]*>/i, `$&${summaryBlock}`);
    } else if (content.includes('<body')) {
      content = content.replace(/<body[^>]*>/i, `$&${summaryBlock}`);
    }
  }

  const before = fs.readFileSync(filePath, 'utf8');
  if (content !== before) {
    fs.writeFileSync(filePath, content, 'utf8');
    return true;
  }
  return false;
}

let changed = 0;
let indexable = 0;
for (const file of walk(CLASS_DIR)) {
  const content = fs.readFileSync(file, 'utf8');
  const robots = attr(content, /<meta\s+name=["']robots["']\s+content=["']([^"']+)/i);
  if (!/noindex/i.test(robots)) indexable += 1;
  if (optimize(file)) changed += 1;
}

console.log(`Optimized ${changed} files across ${indexable} indexable Class 9 pages.`);
