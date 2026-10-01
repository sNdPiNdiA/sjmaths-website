#!/usr/bin/env node
/**
 * ============================================================================
 * SJ Maths — UP PGT Sociology Study Notes & Practice MCQs Generator Pipeline
 * Powered by Google Gemini API via @google/genai SDK
 * Generates authoritative, master-level study notes, sociological theories,
 * comparison tables, mnemonics, and practice MCQs for all 88 UP PGT Sociology topics.
 *
 * Configured to use GEMINI_API_KEY_1 (isolated from Psychology generator on KEY_2).
 * Model: gemini-3.5-flash-lite
 * ============================================================================
 */

import fs from 'node:fs';
import path from 'node:path';
import 'dotenv/config';
import { GoogleGenAI } from '@google/genai';
import { jsonrepair } from 'jsonrepair';

const ROOT = process.cwd();
const DOMAIN = 'https://sjmaths.com';
const STATUS_FILE = path.join(ROOT, 'content-generation-status-sociology.json');

// 1. Parse command line arguments
const args = process.argv.slice(2);
const DRY_RUN = args.includes('--dry-run');
const FORCE = args.includes('--force');
const TEMPLATE_ONLY = args.includes('--template-only');
const LIMIT = (() => {
  const idx = args.indexOf('--limit');
  return idx !== -1 && args[idx + 1] ? parseInt(args[idx + 1], 10) : null;
})();
const TARGET_TOPIC = (() => {
  const idx = args.indexOf('--topic');
  return idx !== -1 && args[idx + 1] ? args[idx + 1] : null;
})();
const TARGET_SECTION = (() => {
  const idx = args.indexOf('--section');
  return idx !== -1 && args[idx + 1] ? args[idx + 1] : null;
})();
const MODEL_NAME = (() => {
  const idx = args.indexOf('--model');
  return idx !== -1 && args[idx + 1] ? args[idx + 1] : 'gemini-3.5-flash-lite';
})();

// Key selection: Exclusively uses GEMINI_API_KEY_1 (the dedicated key separate from Psychology generator)
const KEY_NAME = (() => {
  const idx = args.indexOf('--key');
  return idx !== -1 && args[idx + 1] ? args[idx + 1] : 'GEMINI_API_KEY_1';
})();
const apiKey = process.env[KEY_NAME] || process.env.GEMINI_API_KEY_1 || process.env.GEMINI_API_KEY;

if (!TEMPLATE_ONLY && !apiKey) {
  console.error(`ERROR: No API key found for ${KEY_NAME} in .env. Please configure GEMINI_API_KEY_1.`);
  process.exit(1);
}

const ai = apiKey ? new GoogleGenAI({ apiKey }) : null;

// 2. Load generation status tracking
let statusMap = {};
if (fs.existsSync(STATUS_FILE)) {
  try {
    statusMap = JSON.parse(fs.readFileSync(STATUS_FILE, 'utf8'));
  } catch {
    statusMap = {};
  }
}
function saveStatus() {
  fs.writeFileSync(STATUS_FILE, JSON.stringify(statusMap, null, 2), 'utf8');
}

// 3. Extract syllabus definitions from UP PGT Sociology tracker
function decodeHtml(str) {
  return str
    .replace(/&amp;/g, '&')
    .replace(/&lt;/g, '<')
    .replace(/&gt;/g, '>')
    .replace(/&quot;/g, '"')
    .replace(/&#39;/g, "'");
}

function extractSyllabus() {
  const trackerPath = path.join(ROOT, 'up-pgt-sociology', 'index.html');
  if (!fs.existsSync(trackerPath)) {
    console.error(`Tracker file not found: ${trackerPath}`);
    return [];
  }
  const html = fs.readFileSync(trackerPath, 'utf8');

  const sectionRegex = /<article class="section-card[^"]*" id="([^"]+)"[\s\S]*?>([\s\S]*?)<\/article>/g;
  let sMatch;
  const topicList = [];

  while ((sMatch = sectionRegex.exec(html)) !== null) {
    const [_, sId, sBody] = sMatch;
    const titleMatch = sBody.match(/<span class="section-title">([^<]+)<\/span>/);
    const rawTitle = titleMatch ? titleMatch[1].trim() : sId;
    const sTitle = decodeHtml(rawTitle);
    
    const numMatch = sBody.match(/<span class="section-no">[^<]*<strong>([^<]+)<\/strong><\/span>/);
    const sNum = numMatch ? numMatch[1].trim() : '';

    const topicRegex = /<a class="topic-link" href="([^"]+)">([^<]+)<\/a>/g;
    let tMatch;
    while ((tMatch = topicRegex.exec(sBody)) !== null) {
      const href = tMatch[1].startsWith('/') ? tMatch[1] : '/' + tMatch[1];
      topicList.push({
        href: href.endsWith('/') ? href : href + '/',
        name: decodeHtml(tMatch[2].trim()),
        sectionTitle: sTitle,
        sectionId: sId,
        sectionNo: sNum
      });
    }
  }

  return topicList;
}

const allTopics = extractSyllabus();

// 4. Gemini AI Prompt Builder for Sociology
function buildPrompt(topic) {
  return `You are a distinguished Professor of Sociology, Classical Sociological Theorist, and Senior Examination Authority for Uttar Pradesh Secondary Education Service Selection Board (UPSESSB / UPESSC) PGT Sociology (Post Graduate Teacher, Subject Code 16) and UGC NET Sociology examinations.

Generate exhaustive, master-level academic study notes and practice questions for this exact curriculum topic:
- Discipline: Sociology (Samajshastra)
- Examination: UP PGT Sociology (Subject Code 16)
- Section ${topic.sectionNo}: ${topic.sectionTitle}
- Topic: ${topic.name}
- Canonical URL: ${topic.href}

ACADEMIC DEPTH & PEDAGOGICAL REQUIREMENTS:
1. Adhere strictly to master's level (M.A. Sociology) standards referenced in standard Indian university curricula and UP PGT examinations:
   - Foundational thinkers and classical paradigms: Auguste Comte (Law of 3 Stages, Positivism), Herbert Spencer (Social Darwinism, Organic Analogy), Émile Durkheim (Social Facts, Suicide, Division of Labour, Religion & Totemism), Max Weber (Social Action typology, Ideal Types, Bureaucracy, Protestant Ethic & Capitalism), Karl Marx (Historical Materialism, Class Struggle, Alienation, Base & Superstructure), Vilfredo Pareto (Circulation of Elites, Residues & Derivations), Pitirim Sorokin (Social & Cultural Dynamics, Sensate/Ideational/Idealistic culture).
   - Indian Sociological Pioneers & Empirical Studies: G.S. Ghurye (Indological approach, Caste & Race in India), M.N. Srinivas (Sanskritization, Westernization, Dominant Caste, Rampura village study), D.P. Mukerji (Marxian-Indological synthesis, Dialectics of Traditions), Radhakamal Mukerjee (Theory of Social Values), Irawati Karve (Kinship Organization in India), Andre Beteille (Caste, Class, and Power in Sripuram), S.C. Dube (Indian Village, Shamirpet study), B.R. Ambedkar (Annihilation of Caste, Critique of Hindu Social Order), Yogendra Singh (Modernization of Indian Tradition).
   - Core Concepts & Institutions: Hindu Social Organization (Ashrama system, Purusharthas, Varna vs. Jati, Rina, Samskaras, Gotra/Pravara exogamy), Muslim Marriage & Family (Nikah, Mahr, Talaq, Iddat, Polygyny), Kinship systems (Descent, Lineage, Kinship Usages - Avoidance, Joking, Teknonymy, Avunculate, Amitate), Social Stratification (Davis-Moore functional theory, Tumin critique, Weberian class-status-party), Social Change (Evolutionary, Cyclical, Linear models), Rural & Urban Sociology (Peasant studies, Community Development Programme 1952, Panchayati Raj 73rd/74th Amendments), and Indian Social Problems (Poverty, Unemployment, Dowry, Juvenile Delinquency, Corruption, Communalism).
   - Explicitly cite major publications, publication years, Latin/Greek etymological roots, and exact theoretical formulations commonly tested in UP PGT exams.
2. Structure your response with:
   - In-depth, readable notes sections using semantic HTML (<p>, <ul>, <li>, <strong>, <em>, <code>).
   - Comparative analysis table contrasting related sociological concepts, schools of thought (e.g. Functionalism vs. Conflict, Primary vs. Secondary groups, Varna vs. Jati, Sanskritization vs. Westernization, Organic vs. Mechanical solidarity, etc.).
   - Memory tricks / mnemonics for memorizing thinker chronologies, stages, books, or typologies.
   - 6 High-yield direct factual takeaways for quick last-minute exam revision (e.g. who coined which term, seminal book years, classic definitions).
   - 2 Common exam traps and misconceptions.
   - Exactly 10 practice multiple-choice questions (MCQs) with 4 options each, correct answer index (0 to 3), and comprehensive rationale explaining why the answer is correct and why other options are incorrect.
   - 4 FAQs addressing top search queries.

OUTPUT FORMAT:
Respond with ONLY a valid, raw JSON object (no markdown \`\`\`json wrappers, no chat preamble) adhering strictly to this schema:
{
  "title": "${topic.name}",
  "short_intro": "2 to 3 sentences introducing the core sociological concept, its historical/theoretical significance, and why it is critical for UP PGT Sociology.",
  "notes_sections": [
    {
      "heading": "1. Definitional Framework, Etymology & Classical Foundations",
      "content_html": "<p>Deep, academic explanation with authoritative definitions by classical theorists (e.g. Comte, Durkheim, Weber, MacIver & Page, Ginsberg)...</p><ul><li><strong>Key Theoretical Postulate:</strong> Detail...</li></ul>"
    },
    {
      "heading": "2. Structural Concepts, Empirical Processes & Indian Sociological Context",
      "content_html": "<p>Detailed breakdown of underlying sociological processes, structural dynamics, empirical village/field studies, and Indian sociological perspectives (Ghurye, Srinivas, Mukerji, Karve, etc.)...</p>"
    },
    {
      "heading": "3. Contemporary Dynamics, Social Policy & Applied Dimensions",
      "content_html": "<p>Application to modern Indian society, constitutional provisions, social legislation, contemporary debates, and policy implications...</p>"
    }
  ],
  "comparison_tables": [
    {
      "title": "Comparative Analysis Table",
      "headers": ["Dimension / Parameter", "Category / Concept A", "Category / Concept B"],
      "rows": [
        ["Criterion 1", "Detail A", "Detail B"],
        ["Criterion 2", "Detail A", "Detail B"]
      ]
    }
  ],
  "mnemonics": [
    {
      "title": "Memory Shortcut / Mnemonic",
      "trick": "ACRONYM / Memory phrase",
      "explanation": "Detailed breakdown of the shortcut to remember stages, types, or key works during the exam."
    }
  ],
  "exam_points": [
    "High-yield factual point 1 (Theorist name, seminal book title & year, concept coinage, or classical definition)",
    "High-yield factual point 2",
    "High-yield factual point 3",
    "High-yield factual point 4",
    "High-yield factual point 5",
    "High-yield factual point 6"
  ],
  "common_errors": [
    "Misconception 1: What students commonly confuse vs. the scientifically accurate sociological principle.",
    "Misconception 2: Classic examination trap and how to answer accurately."
  ],
  "practice_questions": [
    {
      "question": "Clear UP PGT examination-style MCQ question text?",
      "options": ["Option A", "Option B", "Option C", "Option D"],
      "correct_index": 0,
      "explanation": "Thorough explanation of the correct answer with sociological context, book references, and exam guidance."
    }
  ],
  "faqs": [
    {
      "q": "Common question about this topic in Sociology?",
      "a": "Authoritative, clear answer summarizing key sociological facts and theories."
    }
  ]
}`;
}

// 5. Render Study Notes HTML Page for Sociology
function renderFullStudyPage(topic, data) {
  const canonicalUrl = `${DOMAIN}${topic.href}`;
  const pageTitle = `${data.title} — UP PGT Sociology Notes, Theories & MCQs | SJ Maths`;
  const metaDesc = `Comprehensive UP PGT Sociology study notes on ${data.title} (Subject Code 16). Classical and Indian sociological thinkers, theories, comparison tables, mnemonics, and 10 practice MCQs with detailed explanations.`;

  // Render notes sections defensively
  let notesHtml = '';
  (data.notes_sections || []).forEach((sec, idx) => {
    notesHtml += `
      <section class="card content-card" id="section-${idx + 1}">
        <h2>${sec.heading}</h2>
        <div class="prose-content">
          ${sec.content_html}
        </div>
      </section>
    `;
  });

  // Render comparison tables defensively
  let tablesHtml = '';
  if (data.comparison_tables && Array.isArray(data.comparison_tables) && data.comparison_tables.length > 0) {
    data.comparison_tables.forEach(table => {
      const headers = (table.headers || []).map(h => `<th>${h}</th>`).join('');
      const rows = (table.rows || []).map(r => `<tr>${(r || []).map(c => `<td>${c}</td>`).join('')}</tr>`).join('');
      tablesHtml += `
        <div class="comparison-card">
          <div class="table-title">${table.title || 'Comparative Sociological Analysis'}</div>
          <div class="table-responsive">
            <table class="styled-table">
              <thead><tr>${headers}</tr></thead>
              <tbody>${rows}</tbody>
            </table>
          </div>
        </div>
      `;
    });
  }

  // Render mnemonics defensively
  let mnemonicsHtml = '';
  if (data.mnemonics && Array.isArray(data.mnemonics) && data.mnemonics.length > 0) {
    data.mnemonics.forEach(m => {
      mnemonicsHtml += `
        <div class="mnemonic-card">
          <div class="mnemonic-badge">Memory Shortcut / Mnemonic</div>
          <div class="mnemonic-title">${m.title || 'Sociological Mnemonic'}</div>
          <div class="mnemonic-formula">${m.trick || ''}</div>
          <p class="mnemonic-desc">${m.explanation || ''}</p>
        </div>
      `;
    });
  }

  // Render high-yield points defensively
  let pointsHtml = '';
  if (data.exam_points && Array.isArray(data.exam_points) && data.exam_points.length > 0) {
    pointsHtml = `
      <section class="card points-card" id="exam-points">
        <h2>High-Yield Exam Points for UP PGT Sociology</h2>
        <ul class="points-list">
          ${data.exam_points.map(pt => `<li>${pt}</li>`).join('\n          ')}
        </ul>
      </section>
    `;
  }

  // Render common errors defensively
  let errorsHtml = '';
  if (data.common_errors && Array.isArray(data.common_errors) && data.common_errors.length > 0) {
    errorsHtml = `
      <section class="card errors-card" id="common-traps">
        <h2>Common Misconceptions &amp; Exam Traps</h2>
        <ul class="errors-list">
          ${data.common_errors.map(err => `<li>${err}</li>`).join('\n          ')}
        </ul>
      </section>
    `;
  }

  // Render practice questions defensively
  let questionsHtml = '';
  if (data.practice_questions && Array.isArray(data.practice_questions) && data.practice_questions.length > 0) {
    const letters = ['A', 'B', 'C', 'D'];
    const validQuestions = data.practice_questions.filter(q => q && q.question);
    const qList = validQuestions.map((q, i) => {
      const opts = Array.isArray(q.options) ? q.options : (Array.isArray(q.choices) ? q.choices : []);
      const optionsHtml = opts.map((opt, oIdx) => `
        <li class="mcq-option" data-idx="${oIdx}">
          <span class="opt-letter">${letters[oIdx] || String.fromCharCode(65 + oIdx)}</span>
          <span class="opt-text">${opt}</span>
        </li>
      `).join('');

      const correctIdx = typeof q.correct_index === 'number' && q.correct_index >= 0 ? q.correct_index : 0;
      const correctLetter = letters[correctIdx] || 'A';
      const correctText = opts[correctIdx] || '';

      return `
        <div class="mcq-item" id="q-${i + 1}" data-correct="${correctIdx}">
          <div class="mcq-header">
            <span class="q-num">Q${i + 1}</span>
            <span class="q-text">${q.question}</span>
          </div>
          <ul class="mcq-options">
            ${optionsHtml}
          </ul>
          <div class="mcq-reveal">
            <button type="button" class="btn-reveal" onclick="toggleExplanation(${i})">Show Answer &amp; Explanation</button>
            <div class="mcq-explanation" id="exp-${i}" style="display:none;">
              <strong>Correct Option: ${correctLetter}${correctText ? ' (' + correctText + ')' : ''}</strong>
              <p>${q.explanation || 'Refer to theoretical notes above.'}</p>
            </div>
          </div>
        </div>
      `;
    }).join('\n');

    questionsHtml = `
      <section class="card mcq-card" id="practice-mcqs">
        <h2>Practice Examination Questions (${validQuestions.length} MCQs)</h2>
        <p style="color:var(--ink-muted);font-size:.9rem;margin-bottom:20px;">
          Test your conceptual understanding. Select an answer and check the detailed pedagogical rationale.
        </p>
        <div class="mcq-container">
          ${qList}
        </div>
      </section>
    `;
  }

  // Render FAQs defensively
  let faqsHtml = '';
  if (data.faqs && Array.isArray(data.faqs) && data.faqs.length > 0) {
    faqsHtml = `
      <section class="card faq-card" id="faqs">
        <h2>Frequently Asked Questions</h2>
        <div class="faq-list">
          ${data.faqs.map(f => `
            <div class="faq-item">
              <h3 class="faq-q">${f.q}</h3>
              <p class="faq-a">${f.a}</p>
            </div>
          `).join('\n          ')}
        </div>
      </section>
    `;
  }

  // Generate FAQ schema elements
  const faqSchema = (data.faqs && data.faqs.length > 0) ? {
    "@type": "FAQPage",
    "mainEntity": data.faqs.map(f => ({
      "@type": "Question",
      "name": f.q,
      "acceptedAnswer": {
        "@type": "Answer",
        "text": f.a
      }
    }))
  } : null;

  return `<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>${pageTitle}</title>
  <meta name="description" content="${metaDesc}">
  <meta name="robots" content="index,follow,max-image-preview:large">
  <meta name="author" content="SJ Maths">
  <meta name="theme-color" content="#0f766e">
  <link rel="canonical" href="${canonicalUrl}">
  <link rel="icon" type="image/png" href="/favicon.png">

  <!-- Open Graph -->
  <meta property="og:type" content="article">
  <meta property="og:site_name" content="SJ Maths">
  <meta property="og:title" content="${pageTitle}">
  <meta property="og:description" content="${metaDesc}">
  <meta property="og:url" content="${canonicalUrl}">
  <meta property="og:image" content="https://sjmaths.com/assets/images/og-default.jpg">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="${pageTitle}">
  <meta name="twitter:description" content="${metaDesc}">
  <meta name="twitter:image" content="https://sjmaths.com/assets/images/og-default.jpg">

  <!-- Structured Data (JSON-LD) -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "LearningResource",
    "name": "${data.title}",
    "headline": "${data.title} — UP PGT Sociology Study Notes & MCQs",
    "description": "${metaDesc}",
    "url": "${canonicalUrl}",
    "inLanguage": "en",
    "learningResourceType": "Study Guide / Quiz",
    "educationalLevel": "Post Graduate Teacher (UP PGT Subject Code 16)",
    "isPartOf": {
      "@type": "WebSite",
      "name": "SJ Maths",
      "url": "https://sjmaths.com/"
    },
    "breadcrumb": {
      "@type": "BreadcrumbList",
      "itemListElement": [
        { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://sjmaths.com/" },
        { "@type": "ListItem", "position": 2, "name": "UP PGT Sociology", "item": "https://sjmaths.com/up-pgt-sociology/" },
        { "@type": "ListItem", "position": 3, "name": "${topic.sectionTitle}", "item": "${canonicalUrl}" },
        { "@type": "ListItem", "position": 4, "name": "${data.title}", "item": "${canonicalUrl}" }
      ]
    }
  }
  </script>
  ${faqSchema ? `<script type="application/ld+json">\n  ${JSON.stringify(faqSchema, null, 2)}\n  </script>` : ''}

  <style>
    :root {
      --bg: #f6f8fb;
      --card-bg: #ffffff;
      --ink: #18212f;
      --ink-muted: #536174;
      --line: #e1e6ed;
      --soft-line: #eff3f7;
      --brand: #0f766e;
      --brand-dark: #115e59;
      --brand-soft: #eaf8f5;
      --accent: #0d9488;
      --accent-soft: #f0fdfa;
      --success: #15803d;
      --success-soft: #f0fdf4;
      --shadow: 0 12px 34px rgba(15,118,110,.07);
      --radius: 16px;
      --header-h: 66px;
    }
    * { box-sizing: border-box; }
    html { scroll-behavior: smooth; }
    body {
      margin: 0; color: var(--ink);
      background: radial-gradient(circle at 100% 0,rgba(15,118,110,.05),transparent 28rem), var(--bg);
      font-family: Inter, ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
      line-height: 1.65; -webkit-font-smoothing: antialiased;
    }
    a { color: var(--brand); text-decoration: none; }
    a:hover { text-decoration: underline; }
    .wrap { width: min(1080px, calc(100% - 32px)); margin: auto; }
    
    /* Header */
    .site-header {
      height: var(--header-h); position: sticky; top: 0; z-index: 60;
      background: rgba(255,255,255,.96); backdrop-filter: blur(12px); border-bottom: 1px solid var(--line);
    }
    .header-inner { height: 100%; display: flex; align-items: center; justify-content: space-between; gap: 16px; }
    .brand { display: flex; align-items: center; gap: 11px; text-decoration: none; color: inherit; }
    .brand-mark {
      width: 38px; height: 38px; border-radius: 11px; display: grid; place-items: center;
      background: linear-gradient(145deg, #0f766e, #0d9488); color: white;
      font-weight: 900; font-family: 'Times New Roman', serif; font-size: 1.6rem; font-style: italic; line-height: 1;
    }
    .brand-name { font-weight: 850; letter-spacing: -.02em; display: block; }
    .brand-sub { font-size: .7rem; color: var(--ink-muted); display: block; margin-top: 1px; }

    /* Breadcrumbs */
    .breadcrumb {
      display: flex; gap: 8px; align-items: center; font-size: .78rem; color: var(--ink-muted);
      margin: 24px 0 16px; flex-wrap: wrap;
    }
    .breadcrumb a { color: var(--ink-muted); }
    .breadcrumb a:hover { color: var(--brand); }
    .breadcrumb span.sep { color: #94a3b8; }

    /* Topic Hero */
    .topic-hero {
      background: var(--card-bg); border: 1px solid var(--line); border-radius: var(--radius);
      padding: 32px 36px; box-shadow: var(--shadow); position: relative; overflow: hidden; margin-bottom: 24px;
    }
    .topic-hero::before {
      content: ""; position: absolute; left: 0; top: 0; bottom: 0; width: 6px;
      background: linear-gradient(180deg, #0f766e, #115e59);
    }
    .kicker { font-size: .75rem; text-transform: uppercase; font-weight: 800; letter-spacing: .08em; color: var(--brand); margin-bottom: 8px; }
    h1 { margin: 0 0 12px; font-size: clamp(1.6rem, 3.2vw, 2.3rem); line-height: 1.22; color: var(--ink); letter-spacing: -.02em; }
    .lead { margin: 0 0 16px; color: var(--ink-muted); font-size: .98rem; line-height: 1.6; }
    .topic-chips { display: flex; gap: 8px; flex-wrap: wrap; }
    .chip { padding: 4px 11px; border-radius: 999px; font-size: .7rem; font-weight: 750; border: 1px solid transparent; }
    .chip-pgt { background: #eaf8f5; color: #0f766e; border-color: #cce9e4; }
    .chip-unit { background: #f0fdf4; color: #15803d; border-color: #bbf7d0; }

    /* Cards */
    .card {
      background: var(--card-bg); border: 1px solid var(--line); border-radius: var(--radius);
      padding: 28px 34px; box-shadow: var(--shadow); margin-bottom: 24px;
    }
    .card h2 {
      margin: 0 0 16px; font-size: 1.28rem; font-weight: 800; color: var(--ink);
      border-bottom: 2px solid var(--soft-line); padding-bottom: 9px;
    }
    .prose-content p { font-size: .96rem; line-height: 1.75; color: #283542; margin-bottom: 14px; }
    .prose-content ul { margin: 10px 0 18px 22px; padding: 0; }
    .prose-content li { font-size: .94rem; line-height: 1.7; color: #283542; margin-bottom: 8px; }
    .prose-content strong { color: #0f766e; }

    /* Comparison Table */
    .comparison-card {
      background: var(--card-bg); border: 1px solid var(--line); border-radius: var(--radius);
      padding: 24px 28px; box-shadow: var(--shadow); margin-bottom: 24px; overflow: hidden;
    }
    .table-title { font-weight: 800; font-size: 1.08rem; color: var(--ink); margin-bottom: 14px; }
    .table-responsive { overflow-x: auto; -webkit-overflow-scrolling: touch; }
    .styled-table { width: 100%; border-collapse: collapse; font-size: .88rem; text-align: left; }
    .styled-table th { background: var(--brand-soft); color: var(--brand); padding: 11px 14px; font-weight: 750; border: 1px solid var(--line); }
    .styled-table td { padding: 10px 14px; border: 1px solid var(--line); vertical-align: top; }
    .styled-table tr:nth-child(even) { background: #fafbfd; }

    /* Mnemonic Card */
    .mnemonic-card {
      background: linear-gradient(135deg, #f0fdfa, #ccfbf1); border: 1px solid #99f6e4;
      border-radius: var(--radius); padding: 22px 26px; margin-bottom: 24px;
    }
    .mnemonic-badge {
      display: inline-block; background: #0f766e; color: white; font-size: .68rem;
      text-transform: uppercase; font-weight: 800; letter-spacing: .06em; padding: 3px 9px; border-radius: 6px; margin-bottom: 8px;
    }
    .mnemonic-title { font-size: 1.05rem; font-weight: 800; color: #115e59; margin-bottom: 6px; }
    .mnemonic-formula {
      font-size: 1.15rem; font-weight: 900; color: #0f766e; font-family: monospace;
      background: rgba(255,255,255,.9); padding: 6px 12px; border-radius: 8px; display: inline-block; margin-bottom: 8px;
    }
    .mnemonic-desc { font-size: .9rem; color: #134e4a; margin: 0; line-height: 1.55; }

    /* Points & Errors List */
    .points-card h2 { color: #0f766e; }
    .points-list { margin: 0; padding-left: 20px; }
    .points-list li { margin-bottom: 9px; font-size: .92rem; color: #283542; line-height: 1.6; }
    .errors-card { background: #fffbf5; border-color: #fed7aa; }
    .errors-card h2 { color: #9a3412; border-bottom-color: #ffedd5; }
    .errors-list { margin: 0; padding-left: 20px; }
    .errors-list li { margin-bottom: 9px; font-size: .92rem; color: #7c2d12; line-height: 1.6; }

    /* Practice MCQs */
    .mcq-card h2 { color: var(--brand); }
    .mcq-item {
      background: #fafbfd; border: 1px solid var(--line); border-radius: 12px;
      padding: 18px 20px; margin-bottom: 16px;
    }
    .mcq-header { display: flex; gap: 12px; align-items: baseline; margin-bottom: 12px; }
    .q-num {
      background: var(--brand); color: white; font-size: .75rem; font-weight: 850;
      padding: 3px 8px; border-radius: 6px; flex-shrink: 0;
    }
    .q-text { font-size: .95rem; font-weight: 700; color: var(--ink); line-height: 1.5; }
    .mcq-options { list-style: none; margin: 0 0 12px; padding: 0; display: grid; gap: 8px; }
    .mcq-option {
      padding: 9px 14px; border: 1px solid var(--line); border-radius: 8px;
      font-size: .88rem; display: flex; align-items: center; gap: 10px; background: #fff;
    }
    .opt-letter {
      width: 24px; height: 24px; border-radius: 6px; background: var(--soft-line);
      display: grid; place-items: center; font-size: .75rem; font-weight: 800; color: var(--ink-muted);
    }
    .btn-reveal {
      background: var(--brand-soft); border: 1px solid #cce9e4; color: var(--brand);
      padding: 7px 14px; border-radius: 8px; font-size: .8rem; font-weight: 750; cursor: pointer;
    }
    .btn-reveal:hover { background: #daf3ef; }
    .mcq-explanation {
      margin-top: 12px; padding: 12px 16px; background: var(--success-soft);
      border: 1px solid #bbf7d0; border-radius: 8px; font-size: .86rem; color: #166534;
    }
    .mcq-explanation p { margin: 6px 0 0; }

    /* FAQs */
    .faq-item { margin-bottom: 16px; padding-bottom: 14px; border-bottom: 1px solid var(--soft-line); }
    .faq-item:last-child { border-bottom: none; margin-bottom: 0; padding-bottom: 0; }
    .faq-q { font-size: .98rem; font-weight: 750; color: var(--brand); margin: 0 0 6px; }
    .faq-a { font-size: .9rem; color: #334155; margin: 0; line-height: 1.6; }

    /* Cross navigation bar */
    .cross-nav {
      margin: 32px 0 48px;
    }
    .cross-nav-card {
      background: var(--card-bg); border: 1px solid var(--line); border-radius: var(--radius);
      padding: 20px 24px; display: flex; align-items: center; justify-content: space-between;
      gap: 12px; transition: border-color .2s; text-decoration: none;
    }
    .cross-nav-card:hover { border-color: var(--brand); }
    .cross-nav-card strong { display: block; font-size: .98rem; color: var(--ink); }
    .cross-nav-card span { font-size: .8rem; color: var(--ink-muted); }

    /* Footer */
    .site-footer {
      padding: 32px 0; border-top: 1px solid var(--line); background: #ffffff;
      font-size: .8rem; color: var(--ink-muted); text-align: center; margin-top: 48px;
    }
    @media(max-width: 640px) {
      .topic-hero { padding: 22px 20px; }
      .card { padding: 20px 18px; }
    }
  </style>
  <script>
    function toggleExplanation(idx) {
      const exp = document.getElementById('exp-' + idx);
      if (exp) {
        exp.style.display = exp.style.display === 'none' ? 'block' : 'none';
      }
    }
  </script>
</head>
<body>

<header class="site-header">
  <div class="wrap header-inner">
    <a class="brand" href="/" aria-label="SJ Maths Home">
      <span class="brand-mark" aria-hidden="true">&int;</span>
      <span>
        <span class="brand-name">SJ Maths</span>
        <span class="brand-sub">Sociology Study Portal</span>
      </span>
    </a>
    <div class="header-nav">
      <a href="/up-pgt-sociology/" style="font-size:.82rem;font-weight:700;color:var(--brand);">← Back to UP PGT Sociology Tracker</a>
    </div>
  </div>
</header>

<main class="wrap">
  <nav class="breadcrumb" aria-label="Breadcrumb">
    <a href="/">Home</a>
    <span class="sep">›</span>
    <a href="/up-pgt-sociology/">Sociology</a>
    <span class="sep">›</span>
    <span>${topic.sectionTitle}</span>
    <span class="sep">›</span>
    <span>${data.title}</span>
  </nav>

  <article class="topic-hero">
    <div class="kicker">Section ${topic.sectionNo} • ${topic.sectionTitle}</div>
    <h1>${data.title}</h1>
    <p class="lead">${data.short_intro}</p>
    <div class="topic-chips">
      <span class="chip chip-pgt">UP PGT Sociology • Code 16</span>
      <span class="chip chip-unit">Section ${topic.sectionNo}</span>
    </div>
  </article>

  ${notesHtml}
  ${tablesHtml}
  ${mnemonicsHtml}
  ${pointsHtml}
  ${errorsHtml}
  ${questionsHtml}
  ${faqsHtml}

  <section class="cross-nav" aria-label="Syllabus Navigation">
    <a class="cross-nav-card" href="/up-pgt-sociology/">
      <div>
        <strong>UP PGT Sociology Study Tracker</strong>
        <span>Track all 17 sections &amp; 88 curriculum topics</span>
      </div>
      <span aria-hidden="true" style="font-size:1.3rem;font-weight:bold;color:var(--brand);">→</span>
    </a>
  </section>
</main>

<footer class="site-footer">
  <div class="wrap">
    <p>© SJ Maths • Dedicated preparation portal for teacher examinations and sociology education.</p>
    <p><a href="/privacy-policy/">Privacy Policy</a> • <a href="/up-pgt-sociology/">UP PGT Sociology Syllabus Tracker</a> • <a href="/">Home</a></p>
  </div>
</footer>

</body>
</html>`;
}

// 6. Template Fallback Data
function getTemplateData(topic) {
  return {
    title: topic.name,
    short_intro: `${topic.name} is a fundamental curriculum topic in UP PGT Sociology (Subject Code 16), categorized under Section ${topic.sectionNo}: ${topic.sectionTitle}.`,
    notes_sections: [
      {
        heading: '1. Definitional Framework, Etymology & Classical Foundations',
        content_html: `<p><strong>${topic.name}</strong> constitutes an essential area of study within sociology. An academic inquiry into this topic requires understanding classical sociological definitions, institutional origins, and foundational theoretical perspectives.</p><ul><li><strong>Classical Perspectives:</strong> Conceptual frameworks formulated by classical thinkers and sociological authorities.</li><li><strong>Systematic Scope:</strong> Definitional boundaries and subject-matter classifications established in the discipline.</li></ul>`
      },
      {
        heading: '2. Structural Concepts, Empirical Processes & Indian Sociological Context',
        content_html: `<p>This module investigates the structural mechanisms and institutional patterns associated with <strong>${topic.name}</strong>, with specific reference to empirical field studies and Indian sociological traditions.</p>`
      },
      {
        heading: '3. Contemporary Dynamics, Social Policy & Applied Dimensions',
        content_html: `<p>Mastery of <strong>${topic.name}</strong> is vital for analyzing modern social change, constitutional guarantees, welfare interventions, and social policy formulation in contemporary India.</p>`
      }
    ],
    comparison_tables: [],
    mnemonics: [],
    exam_points: [
      `Key curriculum topic under Section ${topic.sectionNo}: ${topic.sectionTitle} for UP PGT Sociology.`,
      `Review standard definitions and conceptual formulations cited in M.A. Sociology syllabi.`,
      `Focus on prominent Indian and Western sociological contributors associated with this theme.`
    ],
    common_errors: [
      `Avoid confusing popular colloquial understandings with formal scientific sociological definitions.`
    ],
    practice_questions: [],
    faqs: [
      {
        q: `What is the significance of ${topic.name} in UP PGT Sociology?`,
        a: `${topic.name} forms an integral component of ${topic.sectionTitle}, frequently featuring in factual and conceptual examination questions.`
      }
    ]
  };
}

// 7. Main Execution Pipeline
async function run() {
  console.log('================================================================');
  console.log('SJ Maths — UP PGT Sociology Study Notes Generator Pipeline');
  console.log(`Model: ${MODEL_NAME}`);
  console.log(`Key:   ${KEY_NAME} (${apiKey ? apiKey.substring(0, 8) + '...' + apiKey.slice(-4) : 'NONE'})`);
  console.log(`Total Topics: ${allTopics.length}`);
  console.log('================================================================');

  let eligibleTopics = allTopics;

  if (TARGET_TOPIC) {
    const clean = TARGET_TOPIC.endsWith('/') ? TARGET_TOPIC : TARGET_TOPIC + '/';
    eligibleTopics = eligibleTopics.filter(t => t.href === clean);
    console.log(`Targeting single topic: ${clean} (${eligibleTopics.length} found)`);
  } else if (TARGET_SECTION) {
    eligibleTopics = eligibleTopics.filter(t => t.sectionId === TARGET_SECTION || t.sectionTitle.toLowerCase().includes(TARGET_SECTION.toLowerCase()));
    console.log(`Targeting Section: ${TARGET_SECTION} (${eligibleTopics.length} topics)`);
  }

  if (LIMIT) {
    eligibleTopics = eligibleTopics.slice(0, LIMIT);
    console.log(`Applying limit of ${LIMIT} topics.`);
  }

  let generatedCount = 0;
  let skippedCount = 0;
  let errorCount = 0;

  for (let i = 0; i < eligibleTopics.length; i++) {
    const topic = eligibleTopics[i];
    const relativePath = topic.href.replace(/^\//, '').replace(/\/$/, '');
    const targetDir = path.join(ROOT, relativePath);
    const targetFile = path.join(targetDir, 'index.html');

    // Skip if already generated with AI in statusMap (unless --force)
    if (statusMap[topic.href]?.aiCompleted === true && !FORCE && fs.existsSync(targetFile)) {
      skippedCount++;
      continue;
    }

    console.log(`\n[${i + 1}/${eligibleTopics.length}] Generating notes for: ${topic.name}`);
    console.log(`  Path: ${topic.href} (Section ${topic.sectionNo}: ${topic.sectionTitle})`);

    let data;
    let isAiCompleted = false;

    if (TEMPLATE_ONLY) {
      data = getTemplateData(topic);
    } else {
      const prompt = buildPrompt(topic);

      for (let attempt = 0; attempt < 3 && !isAiCompleted; attempt++) {
        try {
          console.log(`  Calling Gemini (${MODEL_NAME}) using ${KEY_NAME} [Attempt ${attempt + 1}]...`);
          const response = await ai.models.generateContent({
            model: MODEL_NAME,
            contents: prompt,
            config: {
              temperature: 0.3,
              responseMimeType: 'application/json'
            }
          });

          const rawText = response.text ? response.text.trim() : '';
          const repaired = jsonrepair(rawText);
          data = JSON.parse(repaired);
          console.log(`  Received: ${data.notes_sections?.length || 0} sections, ${data.practice_questions?.length || 0} MCQs.`);
          isAiCompleted = true;
        } catch (err) {
          console.warn(`  Attempt ${attempt + 1} warning: ${err.message}`);
          if (attempt < 2) {
            await new Promise(r => setTimeout(r, 2500));
          }
        }
      }

      if (!isAiCompleted) {
        console.error(`  AI Generation Failed after 3 attempts. Falling back to template.`);
        data = getTemplateData(topic);
        errorCount++;
      }
    }

    let fullHtml;
    try {
      fullHtml = renderFullStudyPage(topic, data);
    } catch (renderErr) {
      console.warn(`  Render warning: ${renderErr.message}. Falling back to clean template.`);
      data = getTemplateData(topic);
      fullHtml = renderFullStudyPage(topic, data);
      isAiCompleted = false;
    }

    if (!DRY_RUN) {
      fs.mkdirSync(targetDir, { recursive: true });
      fs.writeFileSync(targetFile, fullHtml, 'utf8');

      statusMap[topic.href] = {
        status: 'completed',
        aiCompleted: isAiCompleted,
        title: data.title || topic.name,
        sectionsCount: data.notes_sections?.length || 0,
        questionsCount: data.practice_questions?.length || 0,
        generatedAt: new Date().toISOString()
      };
      saveStatus();
    }

    generatedCount++;
    console.log(`  ✓ Written to: ${relativePath}/index.html`);

    // Pacing delay between requests to stay well within rate limits
    if (!TEMPLATE_ONLY && i < eligibleTopics.length - 1) {
      await new Promise(r => setTimeout(r, 1200));
    }
  }

  console.log(`\n========================================`);
  console.log(`Sociology Pipeline Finished!`);
  console.log(`Generated: ${generatedCount} topics`);
  console.log(`Skipped:   ${skippedCount} topics`);
  console.log(`Errors:    ${errorCount}`);
  console.log(`Total:     ${eligibleTopics.length} topics`);
  console.log(`Status saved to: ${STATUS_FILE}`);
  console.log(`========================================`);
}

run().catch(err => {
  console.error('Fatal execution error:', err);
  process.exit(1);
});
