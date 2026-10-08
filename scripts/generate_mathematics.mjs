#!/usr/bin/env node
/**
 * ============================================================================
 * SJ Maths — Master Mathematics Study Notes & 10-MCQ Generator Pipeline
 * Powered by Google Gemini API via @google/genai SDK
 * Generates authoritative, 7-Pillar Self-Study Notes with KaTeX Math Rendering
 * for all 299 Mathematics topics across 17 branches.
 *
 * Configured to use GEMINI_API_KEY_2 (isolated from active translation tasks).
 * Model: gemini-3.5-flash-lite
 * ============================================================================
 */

import fs from 'node:fs';
import path from 'node:path';
import 'dotenv/config';
import { GoogleGenAI } from '@google/genai';
import { jsonrepair } from 'jsonrepair';
import { formatMathematicsOption, normalizeMathematicsMarkup } from './lib/mathematics-option-markup.mjs';
import { mathematicsTopicStyleLink } from './lib/mathematics-styles.mjs';

const ROOT = process.cwd();
const DOMAIN = 'https://sjmaths.com';
const STATUS_FILE = path.join(ROOT, 'content-generation-status-mathematics.json');
const MATH_ROOT = path.join(ROOT, 'mathematics');

// 1. Parse command line arguments
const args = process.argv.slice(2);
const DRY_RUN = args.includes('--dry-run');
const FORCE = args.includes('--force');
const LIMIT = (() => {
  const idx = args.indexOf('--limit');
  return idx !== -1 && args[idx + 1] ? parseInt(args[idx + 1], 10) : null;
})();
const TARGET_TOPIC = (() => {
  const idx = args.indexOf('--topic');
  return idx !== -1 && args[idx + 1] ? args[idx + 1] : null;
})();
const TARGET_BRANCH = (() => {
  const idx = args.indexOf('--branch');
  return idx !== -1 && args[idx + 1] ? args[idx + 1] : null;
})();
const MODEL_NAME = (() => {
  const idx = args.indexOf('--model');
  return idx !== -1 && args[idx + 1] ? args[idx + 1] : 'gemini-3.5-flash-lite';
})();

// Key selection: Defaults to GEMINI_API_KEY_1 as requested
const KEY_NAME = (() => {
  const idx = args.indexOf('--key');
  return idx !== -1 && args[idx + 1] ? args[idx + 1] : 'GEMINI_API_KEY_1';
})();
const apiKey = process.env[KEY_NAME] || process.env.GEMINI_API_KEY_1 || process.env.GEMINI_API_KEY_2 || process.env.GEMINI_API_KEY;

if (!DRY_RUN && !apiKey) {
  console.error(`ERROR: No API key found for ${KEY_NAME} in .env. Please configure GEMINI_API_KEY_1.`);
  process.exit(1);
}

const ai = apiKey ? new GoogleGenAI({ apiKey }) : null;

// 2. Load generation status tracking
let statusMap = {};
if (fs.existsSync(STATUS_FILE)) {
  try {
    statusMap = JSON.parse(fs.readFileSync(STATUS_FILE, 'utf8'));
  } catch (e) {
    statusMap = {};
  }
}

function saveStatus() {
  fs.writeFileSync(STATUS_FILE, JSON.stringify(statusMap, null, 2), 'utf8');
}

// 3. Discover all 299 Mathematics topic pages
function discoverAllMathTopics(dir) {
  let list = [];
  const entries = fs.readdirSync(dir, { withFileTypes: true });
  for (const entry of entries) {
    const fullPath = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      list.push(...discoverAllMathTopics(fullPath));
    } else if (entry.name === 'index.html' && dir !== MATH_ROOT) {
      list.push(fullPath);
    }
  }
  return list;
}

const allHtmlFiles = discoverAllMathTopics(MATH_ROOT);

function parseTopicFile(filePath) {
  const rawHtml = fs.readFileSync(filePath, 'utf8');
  const relDir = path.relative(ROOT, path.dirname(filePath)).replace(/\\/g, '/');
  const url = `/${relDir}/`;
  
  // Extract title
  const titleMatch = rawHtml.match(/<title>([^<]+)<\/title>/i);
  let title = 'Mathematics Topic';
  if (titleMatch) {
    title = titleMatch[1].replace(/ — Mathematics.*$/i, '').trim();
  } else {
    const h1Match = rawHtml.match(/<h1>([^<]+)<\/h1>/i);
    if (h1Match) title = h1Match[1].trim();
  }

  // Extract kicker / branch info
  const kickerMatch = rawHtml.match(/<div class="kicker">([^<]+)<\/div>/i);
  const kicker = kickerMatch ? kickerMatch[1].trim() : 'Mathematics Study Guide';

  // Extract parts from path: e.g. mathematics/calculus/differential-calculus/rolles-theorem
  const parts = relDir.split('/'); // ['mathematics', 'calculus', 'differential-calculus', 'rolles-theorem']
  const branchSlug = parts[1] || 'general';
  const subBranchSlug = parts[2] || branchSlug;

  const branchTitle = branchSlug
    .split('-')
    .map(w => w.charAt(0).toUpperCase() + w.slice(1))
    .join(' ');

  return {
    filePath,
    relDir,
    url,
    title,
    kicker,
    branchSlug,
    subBranchSlug,
    branchTitle
  };
}

const allTopics = allHtmlFiles.map(parseTopicFile).sort((a, b) => a.url.localeCompare(b.url));

// 4. Build prompt for Gemini 3.5 Flash Lite
function buildPrompt(topic, prevTopic, nextTopic) {
  return `You are an expert Senior Professor of Mathematics and author for competitive teacher recruitment examinations in India (UP PGT Mathematics, UP TGT Mathematics, DSSSB PGT/TGT, KVS PGT, NVS, and LT Grade).

Prepare clear, mathematically rigorous self-study notes for the following topic. Use natural, direct language. Avoid promotional claims, unsupported exam-frequency or weightage estimates, and unrealistic claims about solving problems in a fixed number of seconds.
Topic: "${topic.title}"
Syllabus Kicker: "${topic.kicker}"
Branch: "${topic.branchTitle}"
URL: "${topic.url}"

- CRITICAL MATHEMATICAL TYPESETTING REQUIREMENT:
- Use standard LaTeX math formatting enclosed in $ ... $ for inline formulas and $$ ... $$ for display formulas.
- Before returning the JSON, verify that every LaTeX expression has balanced braces and matching delimiters; never add extra dollars such as $$$.
- In MCQ option strings, provide answer content only (do not repeat the (A)/(B)/(C)/(D) label; the page adds it). Enclose mathematical content in valid $...$ delimiters, and use \\text{...} for words inside a formula.
- Example: $f'(c) = 0$, $c \\in (a, b)$, $$\\lim_{x \\to 0} \\frac{\\sin x}{x} = 1$$, $$\\int_a^b f(x)\\,dx$$.
- KaTeX will automatically render all LaTeX notation in the browser.
- Ensure all Greek letters (\\alpha, \\beta, \\theta, \\lambda, \\pi), sets (\\mathbb{R}, \\mathbb{Z}, \\mathbb{C}), quantifiers (\\forall, \\exists), and symbols (\\in, \\subset, \\le, \\ge, \\neq, \\to, \\implies) are valid LaTeX.
- CRITICAL JSON ESCAPING: In the JSON output, all LaTeX backslashes MUST be escaped with double backslashes (e.g. \\\\to, \\\\in, \\\\frac{a}{b}, \\\\theta, \\\\mathbb{R}, \\\\subset, \\\\sum, \\\\int).

Return a SINGLE, VALID JSON object with EXACTLY this structure (no markdown fences, no explanation outside JSON):
{
  "title": "${topic.title}",
  "short_intro": "2 or 3 concise, mathematically exact sentences introducing the concept and its geometric or algebraic meaning. Keep the introduction about the mathematics; avoid exam-frequency claims and promotional language.",
  "pillar1_statement": {
    "theorem_name": "Full Formal Name / Principle",
    "statement_latex": "The rigorous mathematical statement with all exact hypotheses and conditions.",
    "geometric_interpretation": "Detailed geometric intuition, visualization, slope/tangent/area meaning.",
    "algebraic_significance": "Algebraic structure, analytical foundation, or algebraic consequences."
  },
  "pillar2_hypotheses": [
    {
      "condition": "Condition 1 name (e.g., Continuity on [a, b])",
      "interval_type": "[a, b] (Closed interval)",
      "necessity": "Strictly Mandatory / Necessary",
      "failure_consequence": "Explicit failure if dropped: e.g. Step function or removable discontinuity violates conclusion."
    },
    {
      "condition": "Condition 2 name (e.g., Differentiability on (a, b))",
      "interval_type": "(a, b) (Open interval)",
      "necessity": "Strictly Mandatory",
      "failure_consequence": "Corner/sharp points (like |x|) lead to non-existence of tangent."
    },
    {
      "condition": "Condition 3 (or boundary equality)",
      "interval_type": "Boundary values",
      "necessity": "Essential for conclusion",
      "failure_consequence": "If f(a) != f(b), horizontal tangent is not guaranteed (leads instead to LMVT)."
    }
  ],
  "pillar3_high_yield_shortcuts": [
    {
      "title": "Shortcut 1: Root Isolation & Polynomial Derivatives",
      "formula_latex": "$$ ... $$",
      "shortcut_rule": "A concise way to apply this result, with its conditions stated.",
      "pyq_relevance": "A topic-specific application or example. Do not claim a question is frequent or cite an exam unless supported by a verified source."
    },
    {
      "title": "Shortcut 2: Symmetric Intervals & Parity",
      "formula_latex": "$$ ... $$",
      "shortcut_rule": "Direct deduction rule for even/odd or symmetric cases.",
      "pyq_relevance": "Standard PYQ appearance."
    },
    {
      "title": "Shortcut 3: Algebraic Derivative Roots",
      "formula_latex": "$$ ... $$",
      "shortcut_rule": "Direct formula/relation.",
      "pyq_relevance": "Direct result tested in examination."
    },
    {
      "title": "Shortcut 4: Trigonometric & Exponential Bounds",
      "formula_latex": "$$ ... $$",
      "shortcut_rule": "Direct bound or interval shortcut.",
      "pyq_relevance": "Direct exam application."
    },
    {
      "title": "Shortcut 5: Determinant / Wronskian / Matrix Shortcut",
      "formula_latex": "$$ ... $$",
      "shortcut_rule": "Direct calculation trick.",
      "pyq_relevance": "Standard question format."
    },
    {
      "title": "Shortcut 6: Rapid Elimination Trick",
      "formula_latex": "$$ ... $$",
      "shortcut_rule": "How to eliminate 2 wrong options instantly without full calculation.",
      "pyq_relevance": "Time management in 125-question exams."
    }
  ],
  "pillar4_exam_traps": [
    {
      "trap_title": "Trap 1: The Sharp Corner / Modulus Fallacy",
      "common_mistake": "Candidates apply the theorem to piecewise or absolute value functions without verifying differentiability at interior points.",
      "counterexample_latex": "$f(x) = |x|$ on $[-1, 1]$",
      "why_it_fails": "Continuous everywhere and $f(-1) = f(1) = 1$, but $f'(0)$ does not exist, so no $c \\in (-1, 1)$ satisfies $f'(c) = 0$.",
      "exam_defense_rule": "Always test derivative from left and right ($f'_-(x_0) = f'_+(x_0)$) at points where argument changes sign."
    },
    {
      "trap_title": "Trap 2: Open vs. Closed Interval Confusion",
      "common_mistake": "Confusing where continuity vs differentiability is required, or asserting that $c$ can be an endpoint $a$ or $b$.",
      "counterexample_latex": "$c \\in (a, b)$ strictly, never $c = a$ or $c = b$",
      "why_it_fails": "If $f'(x) = 0$ only at endpoints, the theorem is violated because $c$ must be in the open interior $(a, b)$.",
      "exam_defense_rule": "Instantly discard any option that offers $c = a$ or $c = b$."
    }
  ],
  "pillar5_comparison_matrix": {
    "title": "Comparative Hierarchy Matrix",
    "headers": ["Concept / Theorem", "Hypotheses / Assumptions", "Key Formula / Outcome", "Geometric Meaning", "Exam Identification Clue"],
    "rows": [
      ["Row 1 Name", "Conditions", "Formula", "Geometric Meaning", "When to apply in exam"],
      ["Row 2 Name", "Conditions", "Formula", "Geometric Meaning", "When to apply in exam"],
      ["Row 3 Name", "Conditions", "Formula", "Geometric Meaning", "When to apply in exam"],
      ["Row 4 Name", "Conditions", "Formula", "Geometric Meaning", "When to apply in exam"]
    ]
  },
  "pillar6_canonical_problems": [
    {
      "problem_statement": "Representative worked problem 1 with clear numerical values.",
      "options": ["(A) ...", "(B) ...", "(C) ...", "(D) ..."],
      "correct_option": "(A)",
      "method_textbook": "Step 1: Verify conditions. Step 2: Differentiate. Step 3: Solve equation. Step 4: Confirm $c \\in (a, b)$.",
      "method_shortcut": "The 25-second option elimination or geometric shortcut method.",
      "exam_tip": "A useful check or observation for this problem."
    },
    {
      "problem_statement": "Representative worked problem 2 (for example, parameter determination or root count).",
      "options": ["(A) ...", "(B) ...", "(C) ...", "(D) ..."],
      "correct_option": "(B)",
      "method_textbook": "Detailed algebraic derivation.",
      "method_shortcut": "Fast speed shortcut.",
      "exam_tip": "A useful check or observation for this problem."
    }
  ],
  "pillar7_practice_mcqs": [
    {
      "q": "MCQ 1: Direct definition / hypothesis test with math $...$",
      "options": ["...", "...", "...", "..."],
      "correct": 0,
      "explanation": "Detailed step-by-step mathematical explanation."
    },
    {
      "q": "MCQ 2: Direct calculation / value of parameter with math $...$",
      "options": ["...", "...", "...", "..."],
      "correct": 1,
      "explanation": "Detailed step-by-step mathematical explanation."
    },
    {
      "q": "MCQ 3: Standard UP PGT/TGT PYQ pattern with math $...$",
      "options": ["...", "...", "...", "..."],
      "correct": 2,
      "explanation": "Detailed step-by-step mathematical explanation."
    },
    {
      "q": "MCQ 4: Root isolation / interval identification with math $...$",
      "options": ["...", "...", "...", "..."],
      "correct": 0,
      "explanation": "Detailed step-by-step mathematical explanation."
    },
    {
      "q": "MCQ 5: Counterexample / condition failure with math $...$",
      "options": ["...", "...", "...", "..."],
      "correct": 3,
      "explanation": "Detailed step-by-step mathematical explanation."
    },
    {
      "q": "MCQ 6: Intermediate value / derivative property with math $...$",
      "options": ["...", "...", "...", "..."],
      "correct": 1,
      "explanation": "Detailed step-by-step mathematical explanation."
    },
    {
      "q": "MCQ 7: Advanced application / algebraic geometry link with math $...$",
      "options": ["...", "...", "...", "..."],
      "correct": 2,
      "explanation": "Detailed step-by-step mathematical explanation."
    },
    {
      "q": "MCQ 8: Assertion-Reason or statement analysis with math $...$",
      "options": ["...", "...", "...", "..."],
      "correct": 0,
      "explanation": "Detailed step-by-step mathematical explanation."
    },
    {
      "q": "MCQ 9: Trigonometric / Exponential / Special function with math $...$",
      "options": ["...", "...", "...", "..."],
      "correct": 3,
      "explanation": "Detailed step-by-step mathematical explanation."
    },
    {
      "q": "MCQ 10: Calculation or application with math $...$",
      "options": ["...", "...", "...", "..."],
      "correct": 1,
      "explanation": "Detailed step-by-step mathematical explanation."
    }
  ],
  "faqs": [
    {
      "q": "FAQ 1: A frequent conceptual dilemma students face in this topic",
      "a": "Direct, authoritative mathematical clarification."
    },
    {
      "q": "FAQ 2: What is the most common reason students lose marks on this topic?",
      "a": "Specific guidance on boundary conditions, intervals, or sign errors."
    },
    {
      "q": "FAQ 3: A topic-specific question about an important condition, result, or application.",
      "a": "A concise mathematical explanation with the relevant conditions."
    },
    {
      "q": "FAQ 4: A topic-specific question about interpreting a result or choosing a method.",
      "a": "A concise explanation with the relevant mathematical steps."
    }
  ]
}`;
}

// 5. Build HTML Page with KaTeX, Rich Aesthetics, and Interactive MCQs
function buildHtmlPage(topic, data, prevTopic, nextTopic) {
  const canonicalUrl = `${DOMAIN}${topic.url}`;

  // Clean title
  const pageTitle = `${topic.title} — Mathematics Study Notes | SJ Maths`;
  const metaDesc = `Mathematics notes on ${topic.title}: definitions, conditions, key results, solved examples, common errors and practice questions for UP PGT and TGT.`;

  // Render Hypotheses Checklist
  const hypothesesRows = (data.pillar2_hypotheses || []).map((h, idx) => `
    <tr>
      <td class="font-semibold">${h.condition}</td>
      <td><code class="px-2 py-1 bg-slate-100 rounded text-xs font-mono">${h.interval_type || 'N/A'}</code></td>
      <td><span class="badge-status ${h.necessity && h.necessity.toLowerCase().includes('mandatory') ? 'badge-mandatory' : 'badge-essential'}">${h.necessity}</span></td>
      <td class="text-sm text-slate-600">${h.failure_consequence}</td>
    </tr>
  `).join('');

  // Render Shortcuts Cards
  const shortcutsCards = (data.pillar3_high_yield_shortcuts || []).map((s, idx) => `
    <div class="shortcut-card">
      <div class="shortcut-header">
        <span class="shortcut-num">0${idx + 1}</span>
        <h4 class="shortcut-title">${s.title}</h4>
      </div>
      <div class="shortcut-formula">${s.formula_latex}</div>
      <p class="shortcut-rule"><strong>Rule:</strong> ${s.shortcut_rule}</p>
      <div class="shortcut-pyq"><strong>Application:</strong> ${s.pyq_relevance}</div>
    </div>
  `).join('');

  // Render Traps Cards
  const trapsCards = (data.pillar4_exam_traps || []).map((t, idx) => `
    <div class="trap-card">
      <div class="trap-badge">⚠️ COMMON ERROR #0${idx + 1}</div>
      <h3 class="trap-title">${t.trap_title}</h3>
      <p class="trap-mistake"><strong>Common Pitfall:</strong> ${t.common_mistake}</p>
      <div class="trap-example"><strong>Counterexample:</strong> ${t.counterexample_latex}</div>
      <p class="trap-why"><strong>Why it fails:</strong> ${t.why_it_fails}</p>
      <div class="trap-rule">🛡️ <strong>Exam Defense:</strong> ${t.exam_defense_rule}</div>
    </div>
  `).join('');

  // Render Comparison Matrix
  const compHeaders = (data.pillar5_comparison_matrix?.headers || []).map(h => `<th>${h}</th>`).join('');
  const compRows = (data.pillar5_comparison_matrix?.rows || []).map(row => `
    <tr>
      ${row.map((cell, cidx) => `<td ${cidx === 0 ? 'class="font-semibold text-brand"' : ''}>${cell}</td>`).join('')}
    </tr>
  `).join('');

  // Render Canonical Problems
  const canonicalProblems = (data.pillar6_canonical_problems || []).map((p, idx) => `
    <div class="canonical-card">
      <div class="canonical-header">
        <span class="canonical-badge">CANONICAL PROBLEM 0${idx + 1}</span>
        <span class="canonical-tag">Dual-Method Breakdown</span>
      </div>
      <p class="problem-stmt">${p.problem_statement}</p>
      <div class="problem-options">
        ${(p.options || []).map(opt => `<span class="opt-pill">${opt}</span>`).join('')}
      </div>
      <div class="correct-banner">✓ Correct Answer: <strong>${p.correct_option}</strong></div>
      <div class="methods-grid">
        <div class="method-box textbook">
          <div class="method-title">📚 Method A: Formal Textbook Derivation</div>
          <div class="method-body">${p.method_textbook}</div>
        </div>
        <div class="method-box shortcut">
          <div class="method-title">⚡ Method B: 25-Second Exam Shortcut</div>
          <div class="method-body">${p.method_shortcut}</div>
        </div>
      </div>
      <div class="exam-takeaway">💡 <strong>Key Takeaway:</strong> ${p.exam_tip}</div>
    </div>
  `).join('');

  // Render 10 Practice MCQs
  const mcqsHtml = (data.pillar7_practice_mcqs || []).map((mcq, idx) => {
    const letters = ['A', 'B', 'C', 'D'];
    const rawCorrect = mcq.correct;
    const correctIdx = typeof rawCorrect === 'string' && /^[A-D]$/i.test(rawCorrect.trim())
      ? rawCorrect.trim().toUpperCase().charCodeAt(0) - 65
      : rawCorrect === null || rawCorrect === undefined || (typeof rawCorrect === 'string' && !rawCorrect.trim())
        ? Number.NaN
        : Number(rawCorrect);
    if (!Array.isArray(mcq.options) || mcq.options.length < 2 ||
        !Number.isInteger(correctIdx) || correctIdx < 0 || correctIdx >= mcq.options.length) {
      throw new Error(`MCQ ${idx + 1} has an invalid answer key or options array.`);
    }
    const optionsHtml = (mcq.options || []).map((opt, oIdx) => {
      const optionText = formatMathematicsOption(opt, letters[oIdx]);
      return `
      <div class="mcq-option" data-idx="${oIdx}" onclick="handleOptionClick(this, ${correctIdx}, ${idx})">
        <span class="opt-label">${letters[oIdx]}</span>
        <span class="opt-text">${optionText}</span>
      </div>
    `;
    }).join('');

    return `
      <div class="mcq-box" id="mcq-${idx}" data-correct="${correctIdx}">
        <div class="mcq-header">
          <span class="mcq-qnum">Q${idx + 1}</span>
          <div class="mcq-question">${mcq.q}</div>
        </div>
        <div class="mcq-options-grid">
          ${optionsHtml}
        </div>
        <div class="mcq-feedback" id="feedback-${idx}"></div>
        <button type="button" class="btn-toggle-sol" onclick="toggleExplanation(${idx})">
          <span>Show Step-by-Step Derivation</span> ▾
        </button>
        <div class="mcq-sol-body" id="sol-${idx}">
          <strong>Derivation &amp; Analysis:</strong>
          <p>${mcq.explanation}</p>
        </div>
      </div>
    `;
  }).join('');

  // Render FAQs
  const faqsHtml = (data.faqs || []).map((faq, idx) => `
    <div class="faq-item">
      <button class="faq-btn" onclick="toggleFaq(this)">
        <span>${faq.q}</span>
        <span class="faq-icon">+</span>
      </button>
      <div class="faq-answer">
        <p>${faq.a}</p>
      </div>
    </div>
  `).join('');

  // FAQ Schema JSON-LD
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

  return normalizeMathematicsMarkup(`<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>${pageTitle}</title>
  <meta name="description" content="${metaDesc}">
  <meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large,max-video-preview:-1">
  <meta name="author" content="SJ Maths">
  <meta name="theme-color" content="#0f172a">
  <link rel="canonical" href="${canonicalUrl}">
  <link rel="icon" type="image/png" href="/favicon.png">

  <!-- Open Graph -->
  <meta property="og:type" content="article">
  <meta property="og:site_name" content="SJ Maths">
  <meta property="og:title" content="${pageTitle}">
  <meta property="og:description" content="${metaDesc}">
  <meta property="og:url" content="${canonicalUrl}">
  <meta property="og:image" content="https://sjmaths.com/assets/images/og-maths.jpg">

  <!-- KaTeX for High-Fidelity Mathematical Typesetting -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" onload="renderMathInElement(document.body,{delimiters:[{left:'$$',right:'$$',display:true},{left:'$',right:'$',display:false}],ignoredTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'option'],throwOnError:false})"></script>

  <!-- Schema Markup -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "LearningResource",
        "name": ${JSON.stringify(data.title)},
        "headline": ${JSON.stringify(`${data.title} — Mathematics Study Notes`)},
        "description": ${JSON.stringify(metaDesc)},
        "url": ${JSON.stringify(canonicalUrl)},
        "educationalLevel": "Higher Secondary / Competitive Teacher Exam",
        "learningResourceType": "Study Module",
        "isPartOf": {
          "@type": "WebSite",
          "name": "SJ Maths",
          "url": "https://sjmaths.com/"
        },
        "breadcrumb": {
          "@type": "BreadcrumbList",
          "itemListElement": [
            { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://sjmaths.com/" },
            { "@type": "ListItem", "position": 2, "name": "Mathematics", "item": "https://sjmaths.com/mathematics/" },
            { "@type": "ListItem", "position": 3, "name": ${JSON.stringify(topic.branchTitle)}, "item": ${JSON.stringify(`https://sjmaths.com/mathematics/${topic.branchSlug}/`)} },
            { "@type": "ListItem", "position": 4, "name": ${JSON.stringify(topic.title)}, "item": ${JSON.stringify(canonicalUrl)} }
          ]
        }
      }
      ${faqSchema ? ',' + JSON.stringify(faqSchema) : ''}
    ]
  }
  </script>

  ${mathematicsTopicStyleLink}
</head>
<body>

<header class="site-header">
  <div class="wrap header-inner">
    <a class="brand" href="https://sjmaths.com/">
      <span class="brand-mark">&int;</span>
      <span>
        <span class="brand-name">SJ Maths</span>
        <span class="brand-sub">Mathematics • ${topic.branchTitle}</span>
      </span>
    </a>
    <div class="header-actions">
      <a class="nav-btn" href="/up-pgt-mathematics/">UP PGT Tracker</a>
      <a class="nav-btn" href="/up-tgt-mathematics/">UP TGT Tracker</a>
    </div>
  </div>
</header>

<main class="wrap">
  <section class="hero">
    <nav class="breadcrumb" aria-label="Breadcrumb">
      <a href="https://sjmaths.com/">Home</a>
      <span>›</span>
      <a href="/mathematics/">Mathematics</a>
      <span>›</span>
      <a href="/mathematics/${topic.branchSlug}/">${topic.branchTitle}</a>
      <span>›</span>
      <span>${topic.title}</span>
    </nav>
    <div class="kicker-badge">${topic.kicker}</div>
    <h1>${data.title || topic.title}</h1>
    <p class="lead-p">${data.short_intro}</p>

    <div class="exam-chips">
      <span style="font-size: 0.74rem; font-weight: 800; color: var(--ink-muted);">For:</span>
      <a class="chip primary" href="/up-pgt-mathematics/">UP PGT Mathematics</a>
      <a class="chip" href="/up-tgt-mathematics/">UP TGT Mathematics</a>
      <span class="chip">DSSSB PGT / TGT</span>
      <span class="chip">KVS / NVS PGT</span>
      <span class="chip">LT Grade</span>
    </div>

    <div class="tracker-strip">
      <div class="tracker-info">
        <span>📖 Topic progress</span>
      </div>
      <div class="toggle-mastery" id="masteryBtn" onclick="toggleMastery()">
        <span id="masteryIcon">○</span>
        <span id="masteryText">Mark as complete</span>
      </div>
    </div>
  </section>

  <!-- Definition and statement -->
  <article class="card">
    <h2>Definition and statement</h2>
    <div class="theorem-box">
      <div class="theorem-title">${data.pillar1_statement?.theorem_name || topic.title}</div>
      <div class="theorem-statement">${data.pillar1_statement?.statement_latex || ''}</div>
    </div>
    <div class="interp-grid">
      <div class="interp-box">
        <h4>📐 Geometric meaning</h4>
        <p>${data.pillar1_statement?.geometric_interpretation || ''}</p>
      </div>
      <div class="interp-box">
        <h4>⚙️ Algebraic meaning</h4>
        <p>${data.pillar1_statement?.algebraic_significance || ''}</p>
      </div>
    </div>
  </article>

  <!-- Conditions -->
  <article class="card">
    <h2>Conditions and hypotheses</h2>
    <p style="font-size:0.9rem; color:#475569; margin-top:0;">Check each condition and what changes when it is omitted:</p>
    <div class="table-wrap">
      <table>
        <thead>
          <tr>
            <th>Hypothesis / Condition</th>
            <th>Domain / Interval</th>
            <th>Necessity</th>
            <th>What Fails If Condition Dropped</th>
          </tr>
        </thead>
        <tbody>
          ${hypothesesRows}
        </tbody>
      </table>
    </div>
  </article>

  <!-- Results and shortcuts -->
  <article class="card">
    <h2>Useful results and shortcuts</h2>
    <p style="font-size:0.9rem; color:#475569; margin-top:0;">Use these identities and results when their conditions apply:</p>
    <div class="shortcuts-grid">
      ${shortcutsCards}
    </div>
  </article>

  <!-- Common errors and counterexamples -->
  <article class="card">
    <h2>Common errors and counterexamples</h2>
    <p style="font-size:0.9rem; color:#475569; margin-top:0;">These examples show how a conclusion can fail when a condition is missing:</p>
    <div class="traps-grid">
      ${trapsCards}
    </div>
  </article>

  <!-- Comparison -->
  <article class="card">
    <h2>${data.pillar5_comparison_matrix?.title || 'Comparison'}</h2>
    <div class="table-wrap">
      <table>
        <thead>
          <tr>
            ${compHeaders}
          </tr>
        </thead>
        <tbody>
          ${compRows}
        </tbody>
      </table>
    </div>
  </article>

  <!-- Solved examples -->
  <article class="card">
    <h2>Solved examples</h2>
    <p style="font-size:0.9rem; color:#475569; margin-top:0;">Each problem includes a full solution and a shorter method:</p>
    ${canonicalProblems}
  </article>

  <!-- Practice questions -->
  <article class="card">
    <h2>Practice questions</h2>
    <p style="font-size:0.9rem; color:#475569; margin-top:0;">Choose an answer to check it and see the solution:</p>
    ${mcqsHtml}
  </article>

  <!-- Questions -->
  <article class="card">
    <h2>Common questions</h2>
    <div class="faqs-list">
      ${faqsHtml}
    </div>
  </article>

  <!-- Cross Navigation -->
  <div class="cross-nav">
    ${prevTopic ? `
      <a class="nav-card" href="${prevTopic.url}">
        <div class="nav-card-label">← Previous Topic</div>
        <div class="nav-card-title">${prevTopic.title}</div>
      </a>
    ` : `<div></div>`}
    ${nextTopic ? `
      <a class="nav-card" style="text-align: right;" href="${nextTopic.url}">
        <div class="nav-card-label">Next Topic →</div>
        <div class="nav-card-title">${nextTopic.title}</div>
      </a>
    ` : `<div></div>`}
  </div>
</main>

<footer class="site-footer">
  <div class="wrap footer-inner">
    <div>
      <strong>SJ Maths</strong> • ${topic.branchTitle} • Mathematics
    </div>
    <div class="footer-links">
      <a href="https://sjmaths.com/">Home</a>
      <a href="/up-pgt-mathematics/">UP PGT Tracker</a>
      <a href="/up-tgt-mathematics/">UP TGT Tracker</a>
      <a href="/mathematics/">Mathematics Hub</a>
    </div>
  </div>
</footer>

<script>
  // Topic Mastery Tracker (localStorage)
  const TOPIC_KEY = 'sjmaths_mastery_${topic.url.replace(/[^a-zA-Z0-9]/g, '_')}';
  function initMastery() {
    const isDone = localStorage.getItem(TOPIC_KEY) === 'true';
    const btn = document.getElementById('masteryBtn');
    const icon = document.getElementById('masteryIcon');
    const text = document.getElementById('masteryText');
    if (isDone) {
      btn.classList.add('completed');
      icon.textContent = '✓';
      text.textContent = 'Completed';
    } else {
      btn.classList.remove('completed');
      icon.textContent = '○';
      text.textContent = 'Mark as complete';
    }
  }
  function toggleMastery() {
    const current = localStorage.getItem(TOPIC_KEY) === 'true';
    localStorage.setItem(TOPIC_KEY, (!current).toString());
    initMastery();
  }
  initMastery();

  // MCQ Selection Handler
  function handleOptionClick(optEl, correctIdx, qIdx) {
    const parent = optEl.closest('.mcq-options-grid');
    if (parent.dataset.answered === 'true') return; // Prevent multiple clicks
    parent.dataset.answered = 'true';

    const selectedIdx = parseInt(optEl.getAttribute('data-idx'), 10);
    const options = parent.querySelectorAll('.mcq-option');
    const feedback = document.getElementById('feedback-' + qIdx);

    if (selectedIdx === correctIdx) {
      optEl.classList.add('correct');
      feedback.textContent = '✓ Correct Answer!';
      feedback.className = 'mcq-feedback correct';
    } else {
      optEl.classList.add('incorrect');
      if (options[correctIdx]) options[correctIdx].classList.add('correct');
      feedback.textContent = '✗ Incorrect. Check the correct option highlighted in green.';
      feedback.className = 'mcq-feedback incorrect';
    }

    // Auto open explanation
    const sol = document.getElementById('sol-' + qIdx);
    if (sol) sol.classList.add('open');
  }

  // Toggle Explanation Button
  function toggleExplanation(qIdx) {
    const sol = document.getElementById('sol-' + qIdx);
    if (sol) sol.classList.toggle('open');
  }

  // FAQ Accordion Toggle
  function toggleFaq(btn) {
    const ans = btn.nextElementSibling;
    const icon = btn.querySelector('.faq-icon');
    if (ans.classList.contains('open')) {
      ans.classList.remove('open');
      icon.textContent = '+';
    } else {
      ans.classList.add('open');
      icon.textContent = '−';
    }
  }
</script>
</body>
</html>`);
}

function sanitizeRawGeminiJson(raw) {
  return raw.replace(/(?<!\\)\\([a-zA-Z]+)/g, '\\\\$1');
}

function repairLatexControls(val) {
  if (typeof val === 'string') {
    return val
      .replace(/\u0009o\b/g, '\\to ')
      .replace(/\u0009heta/g, '\\theta')
      .replace(/\u0009imes/g, '\\times')
      .replace(/\u0009au/g, '\\tau')
      .replace(/\u0009(?=[a-zA-Z])/g, '\\t')
      .replace(/\u0008(?=[a-zA-Z])/g, '\\b')
      .replace(/\u000C(?=[a-zA-Z])/g, '\\f')
      .replace(/\u000B(?=[a-zA-Z])/g, '\\v')
      .replace(/\u000D(?=[a-zA-Z])/g, '\\r')
      .replace(/\n(?=(?:eq|abla|u|ot)\b)/g, '\\n');
  }
  if (Array.isArray(val)) return val.map(repairLatexControls);
  if (val && typeof val === 'object') {
    return Object.fromEntries(Object.entries(val).map(([k, v]) => [k, repairLatexControls(v)]));
  }
  return val;
}

// 6. Main Pipeline Runner
async function run() {
  console.log('================================================================');
  console.log('SJ Maths — Master Mathematics Study Notes Generator Pipeline');
  console.log(`Model: ${MODEL_NAME}`);
  console.log(`Key:   ${KEY_NAME} (${apiKey ? apiKey.substring(0, 8) + '...' + apiKey.slice(-4) : 'NONE'})`);
  console.log(`Total Discovered Topics: ${allTopics.length}`);
  console.log('================================================================');

  let eligibleTopics = allTopics;

  if (TARGET_TOPIC) {
    const clean = TARGET_TOPIC.endsWith('/') ? TARGET_TOPIC : TARGET_TOPIC + '/';
    eligibleTopics = eligibleTopics.filter(t => t.url === clean || t.relDir === TARGET_TOPIC || t.filePath.includes(TARGET_TOPIC));
    console.log(`Targeting single topic: ${TARGET_TOPIC} (${eligibleTopics.length} found)`);
  } else if (TARGET_BRANCH) {
    eligibleTopics = eligibleTopics.filter(t => t.branchSlug === TARGET_BRANCH);
    console.log(`Targeting branch: ${TARGET_BRANCH} (${eligibleTopics.length} topics)`);
  }

  if (LIMIT) {
    eligibleTopics = eligibleTopics.slice(0, LIMIT);
    console.log(`Applying limit: ${LIMIT} topics.`);
  }

  let generatedCount = 0;
  let skippedCount = 0;
  let errorCount = 0;

  for (let i = 0; i < eligibleTopics.length; i++) {
    const topic = eligibleTopics[i];
    const targetFile = topic.filePath;

    // Check if already completed
    if (statusMap[topic.url]?.aiCompleted === true && !FORCE && fs.existsSync(targetFile)) {
      skippedCount++;
      continue;
    }

    const prevTopic = i > 0 ? eligibleTopics[i - 1] : null;
    const nextTopic = i < eligibleTopics.length - 1 ? eligibleTopics[i + 1] : null;

    console.log(`\n[${i + 1}/${eligibleTopics.length}] Generating notes for: ${topic.title}`);
    console.log(`  Path: ${topic.url} (${topic.kicker})`);

    let data;
    let isAiCompleted = false;

    if (DRY_RUN) {
      console.log(`  [DRY RUN] Prompt would be generated for ${topic.title}`);
      continue;
    }

    const prompt = buildPrompt(topic, prevTopic, nextTopic);

    for (let attempt = 0; attempt < 5 && !isAiCompleted; attempt++) {
      try {
        console.log(`  Calling Gemini (${MODEL_NAME}) using ${KEY_NAME} [Attempt ${attempt + 1}]...`);
        const response = await ai.models.generateContent({
          model: MODEL_NAME,
          contents: prompt,
          config: {
            temperature: 0.25,
            responseMimeType: 'application/json'
          }
        });

        const rawText = response.text ? response.text.trim() : '';
        const sanitized = sanitizeRawGeminiJson(rawText);
        const repaired = jsonrepair(sanitized);
        data = repairLatexControls(JSON.parse(repaired));
        console.log(`  Received: ${data.pillar3_high_yield_shortcuts?.length || 0} shortcuts, ${data.pillar7_practice_mcqs?.length || 0} MCQs.`);
        isAiCompleted = true;
      } catch (err) {
        console.warn(`  Attempt ${attempt + 1} warning: ${err.message}`);
        if (attempt < 4) {
          let delayMs = 3000 * Math.pow(1.8, attempt);
          const retryMatch = err.message.match(/retry in ([0-9.]+)s/i) || err.message.match(/retryDelay":"([0-9]+)s"/i);
          if (retryMatch) {
            const sec = parseFloat(retryMatch[1]);
            delayMs = Math.ceil(sec * 1000) + 2000;
            console.log(`  ⏳ Quota throttle detected: waiting ${Math.round(delayMs / 1000)}s before retry...`);
          }
          await new Promise(r => setTimeout(r, delayMs));
        }
      }
    }

    if (!isAiCompleted || !data) {
      console.error(`  ERROR: Failed to generate valid content for ${topic.title} after 5 attempts.`);
      errorCount++;
      continue;
    }

    // Generate HTML
    const html = buildHtmlPage(topic, data, prevTopic, nextTopic);
    fs.writeFileSync(targetFile, html, 'utf8');
    console.log(`  ✓ Written updated 7-pillar master notes to: ${topic.relDir}/index.html`);

    // Update status
    statusMap[topic.url] = {
      title: topic.title,
      branch: topic.branchTitle,
      aiCompleted: true,
      model: MODEL_NAME,
      keyUsed: KEY_NAME,
      timestamp: new Date().toISOString(),
      mcqCount: data.pillar7_practice_mcqs?.length || 0
    };
    saveStatus();
    generatedCount++;

    // Friendly pacing delay
    await new Promise(r => setTimeout(r, 1500));
  }

  console.log('\n================================================================');
  console.log(`Pipeline complete!`);
  console.log(`Generated: ${generatedCount}`);
  console.log(`Skipped:   ${skippedCount}`);
  console.log(`Errors:    ${errorCount}`);
  console.log('================================================================');
}

run().catch(err => {
  console.error('Fatal generator error:', err);
  process.exit(1);
});
