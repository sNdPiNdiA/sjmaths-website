#!/usr/bin/env node
/**
 * ============================================================================
 * SJ Maths — Chemistry Hindi Translation & Bilingual Pipeline
 * Powered by Google Gemini 3.1 Flash Lite via @google/genai SDK
 * Translates and compiles full dual-language (EN / HI) UP PGT/TGT Chemistry Pages
 * Block-based container compiler ensuring 100% tag balance and zero layout leaks
 * ============================================================================
 */

import fs from 'fs';
import path from 'path';
import 'dotenv/config';
import { GoogleGenAI } from '@google/genai';
import { jsonrepair } from 'jsonrepair';

// Multi-key rotation
const rawKeys = [
  process.env.GEMINI_API_KEY_2,
  process.env.GEMINI_API_KEY_1,
  process.env.GEMINI_API_KEY
].filter(Boolean);

const apiKeys = [...new Set(rawKeys)];
if (apiKeys.length === 0) {
  console.error('CRITICAL ERROR: No GEMINI_API_KEY found in environment.');
  process.exit(1);
}

console.log(`Loaded ${apiKeys.length} API keys for round-robin rotation.`);
const clients = apiKeys.map((key, i) => ({
  id: i + 1,
  preview: key.substring(0, 10) + '...' + key.slice(-6),
  client: new GoogleGenAI({ apiKey: key })
}));
let clientIdx = 0;

function getNextClient() {
  const c = clients[clientIdx];
  clientIdx = (clientIdx + 1) % clients.length;
  return c;
}

// CLI Flags
const args = process.argv.slice(2);
function getArg(flag) {
  const idx = args.indexOf(flag);
  return idx !== -1 && args[idx + 1] ? args[idx + 1] : null;
}
const hasFlag = (f) => args.includes(f);

const TARGET_TOPIC = getArg('--topic');
const LIMIT = getArg('--limit') ? parseInt(getArg('--limit'), 10) : null;
const FORCE = hasFlag('--force');

const MODEL_NAME = 'gemini-3.1-flash-lite';
const STATUS_FILE = 'content-generation-status-chemistry-hi.json';
const letters = ['A', 'B', 'C', 'D'];

function fixMissingQuotes(str) {
  return str
    .replace(/^(\s*"[a-zA-Z0-9_]+_hi":\s*)([^"\s][^\n\r]*?)",?$/gm, '$1"$2",')
    .replace(/^(\s*"[a-zA-Z0-9_]+":\s*)([^"\s\[\{0-9\-tfn][^\n\r]*?)",?$/gm, '$1"$2",');
}

// Helper: safe JSON parse with targeted quote repair and jsonrepair fallback
function safeParseJson(raw) {
  let cleaned = raw.trim();
  if (cleaned.startsWith('```json')) cleaned = cleaned.replace(/^```json\s*/, '').replace(/\s*```$/, '');
  else if (cleaned.startsWith('```')) cleaned = cleaned.replace(/^```\s*/, '').replace(/\s*```$/, '');

  // 1. Try standard JSON.parse first
  try {
    return JSON.parse(cleaned);
  } catch (e1) {
    // 2. Targeted line-anchored quote repair on unquoted strings
    const repaired = fixMissingQuotes(cleaned);
    try {
      return JSON.parse(repaired);
    } catch (e2) {
      // 3. Fallback to jsonrepair
      try {
        return JSON.parse(jsonrepair(repaired));
      } catch (e3) {
        return JSON.parse(jsonrepair(cleaned));
      }
    }
  }
}

// Helper: Call Gemini with retries and key rotation
async function callGemini(prompt, systemInstruction, maxRetries = 5) {
  let attempts = 0;
  while (attempts < maxRetries) {
    attempts++;
    const { client, id } = getNextClient();
    try {
      const response = await client.models.generateContent({
        model: MODEL_NAME,
        contents: prompt,
        config: {
          systemInstruction: systemInstruction,
          responseMimeType: 'application/json',
          temperature: 0.2
        }
      });
      return safeParseJson(response.text);
    } catch (err) {
      console.warn(`[Key #${id}] Attempt ${attempts}/${maxRetries} failed: ${err.message}`);
      if (attempts >= maxRetries) throw err;
      const delayMs = Math.min(30000, 2500 * Math.pow(1.5, attempts)) + Math.random() * 1000;
      await new Promise(r => setTimeout(r, delayMs));
    }
  }
}

// SYSTEM INSTRUCTIONS
const SYSTEM_INSTRUCTION_NOTES = `You are a Senior Professor of Chemistry and an expert translator for the UP PGT Chemistry (Subject Code 02) and UP TGT Science competitive exams in India.
Your mission is to translate English Chemistry study notes and summary components into high-standard, academic Hindi (NCERT / UP Madhyamik Education Board standard).

CRITICAL TRANSLATION RULES:
1. Standard Academic Technical Terminology:
   - Translate technical chemistry concepts into standard Devanagari terminology, accompanied by the English term in parentheses on first or principal mention.
   - Examples: "Molarity" -> "मोलरता (Molarity)", "Electronegativity" -> "विद्युत ऋणात्मकता (Electronegativity)", "Homogeneous Mixture" -> "समांगी मिश्रण (Homogeneous Mixture)".
2. Untouched Scientific Elements:
   - KEEP ALL chemical symbols (H2O, NaCl, XeF4, Fe2+), units (mol/L, kJ/mol, g/cm3), mathematical fractions, formulas, and reaction arrows strictly intact in standard scientific Latin/symbolic script.
3. Natural, Formal Tone suitable for postgraduate teacher recruitment candidates.
4. Output must be strict JSON matching the requested schema.`;

const SYSTEM_INSTRUCTION_QUESTIONS = `You are an expert bilingual examiner for UP PGT Chemistry and UP TGT Science exams.
Translate competitive exam questions, options, hints, and explanations into clear, accurate Hindi.
Keep chemical formulas, equations, and math notation intact in standard Latin script.
Output must be strict JSON matching the requested schema.`;

// Extract helper: strip existing bilingual spans to obtain pure English baseline
function getPureEn(str) {
  if (!str) return '';
  const enMatch = str.match(/<span class="lang-en">([\s\S]*?)<\/span>/);
  if (enMatch) return enMatch[1].trim();
  const enDivMatch = str.match(/<div class="lang-en">([\s\S]*?)<\/div>/);
  if (enDivMatch) return enDivMatch[1].replace(/<[^>]+>/g, '').trim();
  return str.replace(/<[^>]+>/g, '').trim();
}

// Clean math HTML helper: standardizes LaTeX tokens into clean semantic HTML
function cleanMathHtml(str) {
  if (!str) return '';
  return str
    .replace(/\\text\{([^{}]+)\}/g, '$1')
    // Greek symbols - negative lookahead ensures no clash with longer words
    .replace(/\\chi(?![a-zA-Z])/g, '&chi;')
    .replace(/\\Delta(?![a-zA-Z])/g, '&Delta;')
    .replace(/\\lambda(?![a-zA-Z])/g, '&lambda;')
    .replace(/\\nu(?![a-zA-Z])/g, '&nu;')
    .replace(/\\mu(?![a-zA-Z])/g, '&mu;')
    .replace(/\\pi(?![a-zA-Z])/g, '&pi;')
    .replace(/\\alpha(?![a-zA-Z])/g, '&alpha;')
    .replace(/\\beta(?![a-zA-Z])/g, '&beta;')
    .replace(/\\gamma(?![a-zA-Z])/g, '&gamma;')
    .replace(/\\theta(?![a-zA-Z])/g, '&theta;')
    .replace(/\\sigma(?![a-zA-Z])/g, '&sigma;')
    .replace(/\\epsilon(?![a-zA-Z])/g, '&epsilon;')
    .replace(/\\omega(?![a-zA-Z])/g, '&omega;')
    .replace(/\\phi(?![a-zA-Z])/g, '&phi;')
    .replace(/\\psi(?![a-zA-Z])/g, '&psi;')
    .replace(/\\rho(?![a-zA-Z])/g, '&rho;')
    .replace(/\\tau(?![a-zA-Z])/g, '&tau;')
    .replace(/\\eta(?![a-zA-Z])/g, '&eta;')
    .replace(/\\kappa(?![a-zA-Z])/g, '&kappa;')
    // Math operators & symbols
    .replace(/\\hbar(?![a-zA-Z])/g, '&#x210f;')
    .replace(/\\times(?![a-zA-Z])/g, '&times;')
    .replace(/\\cdot(?![a-zA-Z])/g, '&middot;')
    .replace(/\\pm(?![a-zA-Z])/g, '&plusmn;')
    .replace(/\\approx(?![a-zA-Z])/g, '&asymp;')
    .replace(/\\propto(?![a-zA-Z])/g, '&prop;')
    .replace(/\\infty(?![a-zA-Z])/g, '&infin;')
    .replace(/\\(?:ge|geq)(?![a-zA-Z])/g, '&ge;')
    .replace(/\\(?:le|leq)(?![a-zA-Z])/g, '&le;')
    .replace(/\\(?:ne|neq)(?![a-zA-Z])/g, '&ne;')
    .replace(/\\partial(?![a-zA-Z])/g, '&part;')
    .replace(/\\sum(?![a-zA-Z])/g, '&sum;')
    .replace(/\\int(?![a-zA-Z])/g, '&int;')
    .replace(/\\(?:to|rightarrow)(?![a-zA-Z])/g, '&rarr;')
    .replace(/\\rightleftharpoons(?![a-zA-Z])/g, '&#8652;')
    .replace(/\\AA(?![a-zA-Z])/g, '&#197;')
    // LaTeX brackets
    .replace(/\\left\(/g, '(')
    .replace(/\\right\)/g, ')')
    .replace(/\\left\[/g, '[')
    .replace(/\\right\]/g, ']')
    // Fractions: standard fractions
    .replace(/(?:&frac|\\frac)\{1\}\{2\}\s*([a-zA-Z])/g, '&frac12; $1')
    .replace(/(?:&frac|\\frac)\{1\}\{2\}/g, '&frac12;')
    .replace(/(?:&frac|\\frac)\{1\}\{4\}/g, '&frac14;')
    .replace(/(?:&frac|\\frac)\{3\}\{4\}/g, '&frac34;')
    .replace(/<span class="math-frac">\s*<span class="math-num">1<\/span>\s*<span class="math-denom">2<\/span>\s*<\/span>\s*([a-zA-Z])/g, '&frac12; $1')
    .replace(/(?:&frac|\\frac)\{([^{}]+)\}\{([^{}]+)\}/g, '<span class="math-frac"><span class="math-num">$1</span><span class="math-denom">$2</span></span>')
    // Square roots
    .replace(/\\sqrt\{([^{}]+)\}/g, '<span class="math-sqrt">&radic;<span class="math-radicand">$1</span></span>')
    // Subscripts & Superscripts (attached to a symbol/char/bracket)
    .replace(/([a-zA-Z0-9\)\]\}\&;\>])_\{([^{}]+)\}/g, '$1<sub>$2</sub>')
    .replace(/([a-zA-Z0-9\)\]\}\&;\>])_([a-zA-Z0-9]+)/g, '$1<sub>$2</sub>')
    .replace(/([a-zA-Z0-9\)\]\}\&;\>])\^\{([^{}]+)\}/g, '$1<sup>$2</sup>')
    .replace(/([a-zA-Z0-9\)\]\}\&;\>])\^([0-9\+\-]+)/g, '$1<sup>$2</sup>');
}

// Extract comprehensive content from index.html
function extractComprehensiveContent(html) {
  const kickerMatch = html.match(/<div class="kicker"[^>]*>([\s\S]*?)<\/div>/);
  const titleMatch = html.match(/<h1>([\s\S]*?)<\/h1>/);
  const leadMatch = html.match(/<p class="lead">([\s\S]*?)<\/p>/);

  const kicker = getPureEn(kickerMatch ? kickerMatch[1] : '');
  const title = getPureEn(titleMatch ? titleMatch[1] : '');
  const lead = getPureEn(leadMatch ? leadMatch[1] : '');

  // Sections
  const sections = [];
  const secRegex = /<section class="notes-section"[^>]*>[\s\S]*?<h2>([\s\S]*?)<\/h2>[\s\S]*?<div class="prose-content">([\s\S]*?)<\/div>\s*<\/section>/g;
  let sMatch;
  while ((sMatch = secRegex.exec(html)) !== null) {
    const heading = getPureEn(sMatch[1]);
    const content = sMatch[2];
    const enBlockMatch = content.match(/<div class="lang-en">([\s\S]*?)<\/div>/);
    const bulletsSource = enBlockMatch ? enBlockMatch[1] : content;
    const bullets = [...bulletsSource.matchAll(/<li>([\s\S]*?)<\/li>/g)].map(m => getPureEn(m[1]));
    sections.push({ heading, bullets });
  }

  // Formulas
  const formulas = [];
  const formRegex = /<div class="formula-card">[\s\S]*?<div class="formula-name">([\s\S]*?)<\/div>[\s\S]*?<div class="formula-eq">([\s\S]*?)<\/div>[\s\S]*?<div class="formula-meta">([\s\S]*?)<\/div>\s*<\/div>/g;
  let fMatch;
  while ((fMatch = formRegex.exec(html)) !== null) {
    const name = getPureEn(fMatch[1]);
    const eq = cleanMathHtml(fMatch[2].trim());
    const metaBlock = fMatch[3];
    const condMatch = metaBlock.match(/Conditions:<\/strong>\s*([\s\S]*?)<\/div>/);
    const unitMatch = metaBlock.match(/Units:<\/strong>\s*([\s\S]*?)<\/div>/);
    formulas.push({
      name,
      eq,
      conditions: condMatch ? cleanMathHtml(getPureEn(condMatch[1])) : '',
      units: unitMatch ? cleanMathHtml(getPureEn(unitMatch[1])) : ''
    });
  }

  // Exceptions
  const exceptions = [];
  const excRegex = /<div class="exception-card">[\s\S]*?<span class="exception-rule">([\s\S]*?)<\/span>[\s\S]*?<p class="exception-detail">([\s\S]*?)<\/p>/g;
  let eMatch;
  while ((eMatch = excRegex.exec(html)) !== null) {
    exceptions.push({
      rule: getPureEn(eMatch[1]),
      observation: getPureEn(eMatch[2].replace(/^<strong>Observation:<\/strong>\s*/, ''))
    });
  }

  // Tricks
  const tricks = [];
  const trkRegex = /<div class="trick-card">[\s\S]*?<div class="trick-title">([\s\S]*?)<\/div>[\s\S]*?<div class="trick-shortcut">([\s\S]*?)<\/div>[\s\S]*?<p class="trick-app">([\s\S]*?)<\/p>/g;
  let tMatch;
  while ((tMatch = trkRegex.exec(html)) !== null) {
    tricks.push({
      title: getPureEn(tMatch[1]),
      shortcut: tMatch[2].trim(),
      application: getPureEn(tMatch[3].replace(/^<strong>Application:<\/strong>\s*/, ''))
    });
  }

  // Comparison Matrix
  let comparison = null;
  const compMatch = html.match(/<div class="comparison-card">[\s\S]*?<div class="comparison-title">([\s\S]*?)<\/div>[\s\S]*?<table class="styled-table">([\s\S]*?)<\/table>/);
  if (compMatch) {
    const cTitle = getPureEn(compMatch[1]);
    const theadMatch = compMatch[2].match(/<thead>[\s\S]*?<tr>([\s\S]*?)<\/tr>[\s\S]*?<\/thead>/);
    const headers = theadMatch ? [...theadMatch[1].matchAll(/<th>([\s\S]*?)<\/th>/g)].map(m => getPureEn(m[1])) : [];
    const tbodyMatch = compMatch[2].match(/<tbody>([\s\S]*?)<\/tbody>/);
    const rows = tbodyMatch ? [...tbodyMatch[1].matchAll(/<tr>([\s\S]*?)<\/tr>/g)].map(tr => {
      return [...tr[1].matchAll(/<td>([\s\S]*?)<\/td>/g)].map(td => getPureEn(td[1]));
    }) : [];
    comparison = { title: cTitle, headers, rows };
  }

  // Exam Points
  let exam_points = [];
  const epMatch = html.match(/<div class="exam-points-card">[\s\S]*?<ul class="exam-points-list">([\s\S]*?)<\/ul>/);
  if (epMatch) {
    exam_points = [...epMatch[1].matchAll(/<li>([\s\S]*?)<\/li>/g)].map(m => getPureEn(m[1]));
  }

  // Common Errors
  let common_errors = [];
  const ceMatch = html.match(/<div class="common-errors-card">[\s\S]*?<ul class="common-errors-list">([\s\S]*?)<\/ul>/);
  if (ceMatch) {
    common_errors = [...ceMatch[1].matchAll(/<li>([\s\S]*?)<\/li>/g)].map(m => getPureEn(m[1]));
  }

  // Tab 2: Summary Concepts
  const summary_concepts = [];
  const conceptRegex = /<div class="summary-concept-card">[\s\S]*?<h3 class="summary-concept-title">([\s\S]*?)<\/h3>[\s\S]*?<div class="summary-concept-body prose-content">([\s\S]*?)<\/div>\s*<\/div>/g;
  let cMatch;
  while ((cMatch = conceptRegex.exec(html)) !== null) {
    summary_concepts.push({
      title: getPureEn(cMatch[1]),
      body: getPureEn(cMatch[2])
    });
  }

  // Tab 2: Glossary
  const glossary = [];
  const gloRegex = /<div class="glossary-item">[\s\S]*?<span class="glossary-term">([\s\S]*?)<\/span>[\s\S]*?<div class="glossary-def">([\s\S]*?)<\/div>/g;
  let gMatch;
  while ((gMatch = gloRegex.exec(html)) !== null) {
    glossary.push({
      term: getPureEn(gMatch[1]),
      definition: getPureEn(gMatch[2])
    });
  }

  // Tab 2: Key Takeaways
  let key_takeaways = [];
  const mustMatch = html.match(/<h2>(?:🎯\s*)?(?:<[^>]+>)?Key Takeaways[\s\S]*?<\/h2>[\s\S]*?<ul[^>]*>([\s\S]*?)<\/ul>/);
  if (mustMatch) {
    key_takeaways = [...mustMatch[1].matchAll(/<li>([\s\S]*?)<\/li>/g)].map(x => getPureEn(x[1]));
  }

  // Tab 2: Quick Recall
  let quick_recall = [];
  const recallMatch = html.match(/<h2>(?:📌\s*)?(?:<[^>]+>)?Quick Recall[\s\S]*?<\/h2>[\s\S]*?<ul[^>]*>([\s\S]*?)<\/ul>/);
  if (recallMatch) {
    quick_recall = [...recallMatch[1].matchAll(/<li>([\s\S]*?)<\/li>/g)].map(x => getPureEn(x[1]));
  }

  // Tab 2: Key Differences
  const key_differences = [];
  const confRegex = /<div class="confusion-item">[\s\S]*?<span class="conf-badge-a">([\s\S]*?)<\/span>[\s\S]*?<span class="conf-badge-b">([\s\S]*?)<\/span>[\s\S]*?<p class="confusion-diff">([\s\S]*?)<\/p>/g;
  let cfMatch;
  while ((cfMatch = confRegex.exec(html)) !== null) {
    key_differences.push({
      term_a: getPureEn(cfMatch[1]),
      term_b: getPureEn(cfMatch[2]),
      difference: getPureEn(cfMatch[3])
    });
  }

  return {
    kicker,
    title,
    lead,
    sections,
    formulas,
    exceptions,
    tricks,
    comparison,
    exam_points,
    common_errors,
    summary_concepts,
    glossary,
    key_takeaways,
    quick_recall,
    key_differences
  };
}

// Translate Study Notes & Theory
async function translateTheory(enData) {
  const prompt = `Translate the following English study notes and revision summary components into academic Hindi according to the rules:

INPUT DATA:
${JSON.stringify(enData, null, 2)}

REQUIRED JSON RESPONSE SCHEMA:
{
  "kicker_hi": "Branch in Hindi (e.g. भौतिक रसायन)",
  "title_hi": "Topic Title in Hindi with English in brackets (e.g. रासायनिक तत्व (Chemical Elements))",
  "lead_hi": "Translated introductory lead paragraph in Hindi",
  "sections_hi": [
    {
      "heading_hi": "Section heading in Hindi",
      "bullets_hi": ["Bullet 1 in Hindi", "Bullet 2 in Hindi"]
    }
  ],
  "formula_meta_hi": [
    {
      "name_hi": "Formula name in Hindi (English in brackets)",
      "conditions_hi": "Translated conditions",
      "units_hi": "Translated units explanation"
    }
  ],
  "exceptions_hi": [
    {
      "rule_hi": "General rule in Hindi",
      "observation_hi": "Observation & explanation in Hindi"
    }
  ],
  "tricks_hi": [
    {
      "title_hi": "Shortcut title in Hindi",
      "shortcut_hi": "Shortcut rule in Hindi",
      "application_hi": "Application tip in Hindi"
    }
  ],
  "comparison_hi": {
    "title_hi": "Comparison table title in Hindi",
    "headers_hi": ["Header 1 in Hindi", "Header 2 in Hindi"],
    "rows_hi": [
      ["Cell 1 in Hindi", "Cell 2 in Hindi"]
    ]
  },
  "exam_points_hi": ["Key point 1 in Hindi", "Key point 2 in Hindi"],
  "common_errors_hi": ["Common error 1 in Hindi", "Common error 2 in Hindi"],
  "summary_concepts_hi": [
    {
      "title_hi": "Core concept title in Hindi",
      "body_hi": "Concise concept explanation in Hindi"
    }
  ],
  "glossary_hi": [
    {
      "term_hi": "Term in Hindi (English in brackets)",
      "definition_hi": "Concise definition in Hindi"
    }
  ],
  "key_takeaways_hi": ["Point 1 in Hindi", "Point 2 in Hindi"],
  "quick_recall_hi": ["Recall point 1 in Hindi", "Recall point 2 in Hindi"],
  "key_differences_hi": [
    {
      "term_a_hi": "Term A in Hindi",
      "term_b_hi": "Term B in Hindi",
      "difference_hi": "Clear distinction in Hindi"
    }
  ]
}`;

  return await callGemini(prompt, SYSTEM_INSTRUCTION_NOTES);
}

// Translate Questions Payload (quiz, topic_test, pyq)
async function translateQuestions(questions) {
  if (!Array.isArray(questions) || questions.length === 0) return [];
  const simplified = questions.map(q => ({
    question: q.question,
    options: q.options,
    hint: q.hint || '',
    explanation: q.explanation || ''
  }));

  const prompt = `Translate the following ${simplified.length} exam questions into Hindi:

INPUT QUESTIONS:
${JSON.stringify(simplified, null, 2)}

REQUIRED JSON RESPONSE SCHEMA:
{
  "translated": [
    {
      "question_hi": "Question in Hindi",
      "options_hi": ["Option A in Hindi", "Option B in Hindi", "Option C in Hindi", "Option D in Hindi"],
      "hint_hi": "Hint in Hindi (or empty string)",
      "explanation_hi": "Detailed rationale in Hindi"
    }
  ]
}`;

  const res = await callGemini(prompt, SYSTEM_INSTRUCTION_QUESTIONS);
  return res.translated || [];
}

// Safe replacement of a nested div container by counting open/close depth
function replaceBalancedContainer(html, startPattern, newContent) {
  let startIndex = -1;
  if (typeof startPattern === 'string') {
    startIndex = html.indexOf(startPattern);
  } else if (startPattern instanceof RegExp) {
    const m = html.match(startPattern);
    if (m) startIndex = m.index;
  }
  if (startIndex === -1) return html;

  const divRegex = /<\/?div\b[^>]*>/gi;
  divRegex.lastIndex = startIndex;

  let depth = 0;
  let match;
  while ((match = divRegex.exec(html)) !== null) {
    if (match[0].startsWith('</')) {
      depth--;
      if (depth === 0) {
        const endIndex = match.index + match[0].length;
        return html.substring(0, startIndex) + newContent + html.substring(endIndex);
      }
    } else {
      depth++;
    }
  }
  return html;
}

// Build complete bilingual HTML with strict container-based replacements
function buildCompleteBilingualHtml(originalHtml, enData, hiData, quizData, pyqData, testData) {
  let html = originalHtml;

  // 1. Language Toggle Button
  if (!html.includes('id="btn-lang-toggle"')) {
    html = html.replace(
      /(<div class="header-actions">)/,
      `$1\n      <button type="button" class="lang-toggle-btn" id="btn-lang-toggle" aria-label="Switch Language / भाषा बदलें">🌐 <span style="font-weight:900;">EN</span> (हिन्दी)</button>`
    );
  }

  // 1b. Inject CSS visibility rules
  if (!html.includes('html[data-lang="en"]')) {
    html = html.replace(
      '</style>',
      'html[data-lang="en"] .lang-hi { display: none !important; }\nhtml[data-lang="hi"] .lang-en { display: none !important; }\nhtml:not([data-lang="hi"]) .lang-hi { display: none !important; }\n</style>'
    );
  }

  // 1c. Inject inline JS logic for language toggle
  if (!html.includes('setLanguage(')) {
    const langScriptSnippet = `
  // Bilingual (English / Hindi) Language Toggle Logic
  const langToggleBtn = document.getElementById('btn-lang-toggle');
  function setLanguage(lang, save) {
    if (lang !== 'hi' && lang !== 'en') lang = 'en';
    document.documentElement.setAttribute('data-lang', lang);
    if (save !== false) {
      localStorage.setItem('sjmaths_preferred_language', lang);
    }
    if (langToggleBtn) {
      langToggleBtn.innerHTML = lang === 'hi' ? '🌐 <span style="font-weight:900;">हिन्दी</span> (EN)' : '🌐 <span style="font-weight:900;">EN</span> (हिन्दी)';
    }
  }
  const savedLang = localStorage.getItem('sjmaths_preferred_language') || 'en';
  setLanguage(savedLang, false);

  if (langToggleBtn) {
    langToggleBtn.addEventListener('click', () => {
      const currentLang = document.documentElement.getAttribute('data-lang') || 'en';
      const nextLang = currentLang === 'en' ? 'hi' : 'en';
      setLanguage(nextLang, true);
    });
  }
`;
    html = html.replace(
      "document.addEventListener('DOMContentLoaded', () => {",
      "document.addEventListener('DOMContentLoaded', () => {" + langScriptSnippet
    );
  }

  // 2. Hero Kicker, Title, Lead
  if (hiData.kicker_hi) {
    html = html.replace(
      /<div class="kicker"[^>]*>[\s\S]*?<\/div>/,
      `<div class="kicker" style="color: #2563eb; font-weight: 800;">
        <span class="lang-en">${enData.kicker}</span>
        <span class="lang-hi">${hiData.kicker_hi}</span>
      </div>`
    );
  }

  if (hiData.title_hi) {
    html = html.replace(
      /<h1>[\s\S]*?<\/h1>/,
      `<h1>
        <span class="lang-en">${enData.title}</span>
        <span class="lang-hi">${hiData.title_hi}</span>
      </h1>`
    );
  }

  if (hiData.lead_hi) {
    html = html.replace(
      /<p class="lead">[\s\S]*?<\/p>/,
      `<p class="lead">
        <span class="lang-en">${enData.lead}</span>
        <span class="lang-hi">${hiData.lead_hi}</span>
      </p>`
    );
  }

  // 3. Tab Buttons labels
  html = html.replace(
    /<span>📖<\/span>\s*(?:<[^>]+>)*\s*<span>Study Notes<\/span>/,
    `<span>📖</span> <span class="lang-en">Study Notes</span><span class="lang-hi">अध्ययन नोट्स</span>`
  );
  html = html.replace(
    /<span>⚡<\/span>\s*(?:<[^>]+>)*\s*<span>Revision Summary<\/span>/,
    `<span>⚡</span> <span class="lang-en">Revision Summary</span><span class="lang-hi">रिवीज़न सारांश</span>`
  );
  html = html.replace(
    /<span>❓<\/span>\s*(?:<[^>]+>)*\s*<span>Practice Quiz<\/span>/,
    `<span>❓</span> <span class="lang-en">Practice Quiz</span><span class="lang-hi">अभ्यास क्विज़</span>`
  );
  html = html.replace(
    /<span>🏛️<\/span>\s*(?:<[^>]+>)*\s*<span>PYQs & Trends<\/span>/,
    `<span>🏛️</span> <span class="lang-en">PYQs & Trends</span><span class="lang-hi">विगत वर्ष प्रश्न</span>`
  );
  html = html.replace(
    /<span>⏱️<\/span>\s*(?:<[^>]+>)*\s*<span>Topic Test<\/span>/,
    `<span>⏱️</span> <span class="lang-en">Topic Test</span><span class="lang-hi">टॉपिक टेस्ट</span>`
  );

  // 4. Tab 1: Sections
  if (Array.isArray(hiData.sections_hi)) {
    enData.sections.forEach((sec, idx) => {
      const hiSec = hiData.sections_hi[idx];
      if (!hiSec) return;

      const enBulletsHtml = sec.bullets.map(b => `<li>${b}</li>`).join('');
      const hiBulletsHtml = (hiSec.bullets_hi || []).map(b => `<li>${b}</li>`).join('');

      const oldSecRegex = new RegExp(
        `<section class="notes-section" id="note-sec-${idx + 1}">[\\s\\S]*?<h2>[\\s\\S]*?<\\/h2>[\\s\\S]*?<div class="prose-content">[\\s\\S]*?<\\/div>\\s*<\\/section>`
      );

      const bilingualSec = `
      <section class="notes-section" id="note-sec-${idx + 1}">
        <h2>
          <span class="lang-en">${sec.heading}</span>
          <span class="lang-hi">${hiSec.heading_hi || sec.heading}</span>
        </h2>
        <div class="prose-content">
          <div class="lang-en">
            <ul class="notes-bullet-list">${enBulletsHtml}</ul>
          </div>
          <div class="lang-hi">
            <ul class="notes-bullet-list">${hiBulletsHtml}</ul>
          </div>
        </div>
      </section>`;

      html = html.replace(oldSecRegex, bilingualSec.trim());
    });
  }

  // 5. Formula Sheet (Clean block replacement)
  if (Array.isArray(enData.formulas) && enData.formulas.length > 0) {
    const cardsHtml = enData.formulas.map((f, idx) => {
      const hiF = (hiData.formula_meta_hi && hiData.formula_meta_hi[idx]) || {};
      const condEn = cleanMathHtml(f.conditions || '');
      const unitEn = cleanMathHtml(f.units || '');
      const condHi = cleanMathHtml(hiF.conditions_hi || condEn);
      const unitHi = cleanMathHtml(hiF.units_hi || unitEn);
      const eqHtml = cleanMathHtml(f.eq || '');

      return `
            <div class="formula-card">
              <div class="formula-name">
                <span class="lang-en">${f.name}</span>
                <span class="lang-hi">${hiF.name_hi || f.name}</span>
              </div>
              <div class="formula-eq">${eqHtml}</div>
              <div class="formula-meta">
                <div class="lang-en">
                  ${condEn ? `<div><strong>Conditions:</strong> ${condEn}</div>` : ''}
                  ${unitEn ? `<div><strong>Units:</strong> ${unitEn}</div>` : ''}
                </div>
                <div class="lang-hi">
                  ${condHi ? `<div><strong>शर्तें:</strong> ${condHi}</div>` : ''}
                  ${unitHi ? `<div><strong>इकाइयाँ:</strong> ${unitHi}</div>` : ''}
                </div>
              </div>
            </div>`;
    }).join('');

    const bilingualFormulaBox = `
        <div class="formula-sheet-box">
          <div class="formula-sheet-title">
            <span class="lang-en">📐 Key Formulas & Equations</span>
            <span class="lang-hi">📐 महत्वपूर्ण सूत्र एवं समीकरण</span>
          </div>
          <div class="formula-grid">
${cardsHtml}
          </div>
        </div>`;

    html = replaceBalancedContainer(html, '<div class="formula-sheet-box">', bilingualFormulaBox.trim());
  }

  // 6. Exceptions (Clean block replacement)
  if (Array.isArray(enData.exceptions) && enData.exceptions.length > 0) {
    const excListHtml = enData.exceptions.map((exc, idx) => {
      const hiExc = (hiData.exceptions_hi && hiData.exceptions_hi[idx]) || {};
      return `
            <div class="exception-card">
              <div class="exception-head">
                <span class="exception-badge"><span class="lang-en">Exception</span><span class="lang-hi">अपवाद</span></span>
                <span class="exception-rule"><span class="lang-en">${exc.rule}</span><span class="lang-hi">${hiExc.rule_hi || exc.rule}</span></span>
              </div>
              <p class="exception-detail">
                <span class="lang-en"><strong>Observation:</strong> ${exc.observation}</span>
                <span class="lang-hi"><strong>प्रेक्षण:</strong> ${hiExc.observation_hi || exc.observation}</span>
              </p>
            </div>`;
    }).join('');

    const bilingualExceptions = `
        <div class="exception-alert-box">
          <div class="exception-alert-title">
            <span class="lang-en">⚠️ Important Exceptions & Anomalies</span>
            <span class="lang-hi">⚠️ महत्वपूर्ण अपवाद एवं विसंगतियाँ</span>
          </div>
          <div class="exception-list">
${excListHtml}
          </div>
        </div>`;

    html = replaceBalancedContainer(html, '<div class="exception-alert-box">', bilingualExceptions.trim());
  }

  // 7. Shortcuts / Tricks (Clean block replacement)
  if (Array.isArray(enData.tricks) && enData.tricks.length > 0) {
    const trickListHtml = enData.tricks.map((trk, idx) => {
      const hiTrk = (hiData.tricks_hi && hiData.tricks_hi[idx]) || {};
      return `
            <div class="trick-card">
              <div class="trick-title"><span class="lang-en">${trk.title}</span><span class="lang-hi">${hiTrk.title_hi || trk.title}</span></div>
              <div class="trick-shortcut">${trk.shortcut}</div>
              <p class="trick-app">
                <span class="lang-en"><strong>Application:</strong> ${trk.application}</span>
                <span class="lang-hi"><strong>अनुप्रयोग:</strong> ${hiTrk.application_hi || trk.application}</span>
              </p>
            </div>`;
    }).join('');

    const bilingualTricks = `
        <div class="trick-box">
          <div class="trick-box-title">
            <span class="lang-en">💡 Shortcuts & Memory Aids</span>
            <span class="lang-hi">💡 शॉर्टकट एवं स्मरणीय सूत्र</span>
          </div>
          <div class="tricks-grid">
${trickListHtml}
          </div>
        </div>`;

    html = replaceBalancedContainer(html, '<div class="trick-box">', bilingualTricks.trim());
  }

  // 8. Comparison Matrix (Clean block replacement)
  if (enData.comparison && hiData.comparison_hi) {
    const comp = enData.comparison;
    const hiComp = hiData.comparison_hi;

    const ths = comp.headers.map((h, i) => {
      const hHi = (hiComp.headers_hi && hiComp.headers_hi[i]) || h;
      return `<th><span class="lang-en">${h}</span><span class="lang-hi">${hHi}</span></th>`;
    }).join('');

    const trs = comp.rows.map((row, rIdx) => {
      const hiRow = (hiComp.rows_hi && hiComp.rows_hi[rIdx]) || [];
      const tds = row.map((cell, cIdx) => {
        const cHi = hiRow[cIdx] || cell;
        return `<td><span class="lang-en">${cell}</span><span class="lang-hi">${cHi}</span></td>`;
      }).join('');
      return `<tr>${tds}</tr>`;
    }).join('');

    const bilingualComparison = `
        <div class="comparison-card">
          <div class="comparison-title">
            <span class="lang-en">⚖️ ${comp.title.replace(/^⚖️\s*/, '')}</span>
            <span class="lang-hi">⚖️ ${(hiComp.title_hi || comp.title).replace(/^⚖️\s*/, '')}</span>
          </div>
          <div class="table-responsive">
            <table class="styled-table">
              <thead><tr>${ths}</tr></thead>
              <tbody>${trs}</tbody>
            </table>
          </div>
        </div>`;

    html = replaceBalancedContainer(html, '<div class="comparison-card">', bilingualComparison.trim());
  }

  // 9. Exam Points Card (Clean block replacement)
  if (Array.isArray(enData.exam_points) && enData.exam_points.length > 0) {
    const enPoints = enData.exam_points.map(p => `<li>${p}</li>`).join('');
    const hiPoints = (hiData.exam_points_hi || enData.exam_points).map(p => `<li>${p}</li>`).join('');

    const bilingualExamPoints = `
        <div class="exam-points-card">
          <div class="exam-points-title">
            <span class="lang-en">🎯 Key Exam Points</span>
            <span class="lang-hi">🎯 महत्वपूर्ण परीक्षा बिंदु (Key Exam Points)</span>
          </div>
          <div class="lang-en">
            <ul class="exam-points-list">${enPoints}</ul>
          </div>
          <div class="lang-hi">
            <ul class="exam-points-list">${hiPoints}</ul>
          </div>
        </div>`;

    html = replaceBalancedContainer(html, '<div class="exam-points-card">', bilingualExamPoints.trim());
  }

  // 10. Common Errors Card (Clean block replacement)
  if (Array.isArray(enData.common_errors) && enData.common_errors.length > 0) {
    const enErrors = enData.common_errors.map(e => `<li>${e}</li>`).join('');
    const hiErrors = (hiData.common_errors_hi || enData.common_errors).map(e => `<li>${e}</li>`).join('');

    const bilingualCommonErrors = `
        <div class="common-errors-card">
          <div class="common-errors-title">
            <span class="lang-en">🚫 Common Errors & Confusions</span>
            <span class="lang-hi">🚫 सामान्य भ्रांतियाँ एवं त्रुटियाँ (Common Errors)</span>
          </div>
          <div class="lang-en">
            <ul class="common-errors-list">${enErrors}</ul>
          </div>
          <div class="lang-hi">
            <ul class="common-errors-list">${hiErrors}</ul>
          </div>
        </div>`;

    html = replaceBalancedContainer(html, '<div class="common-errors-card">', bilingualCommonErrors.trim());
  }

  // 11. Tab 2: Revision Summary
  // Build bilingual summary concepts
  let conceptsHtml = '';
  if (Array.isArray(enData.summary_concepts)) {
    conceptsHtml = enData.summary_concepts.map((c, idx) => {
      const hiC = (hiData.summary_concepts_hi && hiData.summary_concepts_hi[idx]) || {};
      return `
          <div class="summary-concept-card">
            <div class="summary-concept-header">
              <h3 class="summary-concept-title">
                <span class="lang-en">${c.title}</span>
                <span class="lang-hi">${hiC.title_hi || c.title}</span>
              </h3>
            </div>
            <div class="summary-concept-body prose-content">
              <div class="lang-en"><p>${c.body.replace(/<\/?p>/g, '')}</p></div>
              <div class="lang-hi"><p>${hiC.body_hi || c.body}</p></div>
            </div>
          </div>`;
    }).join('\n');
  }

  // Build bilingual glossary
  let glossaryHtml = '';
  if (Array.isArray(enData.glossary)) {
    glossaryHtml = enData.glossary.map((g, idx) => {
      const hiG = (hiData.glossary_hi && hiData.glossary_hi[idx]) || {};
      return `
          <div class="glossary-item">
            <div class="glossary-term-wrap">
              <span class="glossary-term">
                <span class="lang-en">${g.term}</span>
                <span class="lang-hi">${hiG.term_hi || g.term}</span>
              </span>
            </div>
            <div class="glossary-def">
              <span class="lang-en">${g.definition}</span>
              <span class="lang-hi">${hiG.definition_hi || g.definition}</span>
            </div>
          </div>`;
    }).join('\n');
  }

  // Build takeaways
  const enTakeaways = (enData.key_takeaways || []).map(x => `<li>${x}</li>`).join('');
  const hiTakeaways = (hiData.key_takeaways_hi || enData.key_takeaways || []).map(x => `<li>${x}</li>`).join('');

  // Build recall
  const enRecall = (enData.quick_recall || []).map(x => `<li>${x}</li>`).join('');
  const hiRecall = (hiData.quick_recall_hi || enData.quick_recall || []).map(x => `<li>${x}</li>`).join('');

  // Build differences
  let differencesHtml = '';
  if (Array.isArray(enData.key_differences)) {
    differencesHtml = enData.key_differences.map((cf, idx) => {
      const hiCf = (hiData.key_differences_hi && hiData.key_differences_hi[idx]) || {};
      return `
          <div class="confusion-item">
            <div class="confusion-terms">
              <span class="conf-badge-a"><span class="lang-en">${cf.term_a}</span><span class="lang-hi">${hiCf.term_a_hi || cf.term_a}</span></span>
              <span class="conf-vs">VS</span>
              <span class="conf-badge-b"><span class="lang-en">${cf.term_b}</span><span class="lang-hi">${hiCf.term_b_hi || cf.term_b}</span></span>
            </div>
            <p class="confusion-diff">
              <span class="lang-en">${cf.difference}</span>
              <span class="lang-hi">${hiCf.difference_hi || cf.difference}</span>
            </p>
          </div>`;
    }).join('\n');
  }

  const bilingualTab2 = `
      <!-- TAB 2: REVISION SUMMARY & GLOSSARY -->
      <article class="tab-panel hidden" id="tab-summary" role="tabpanel" aria-labelledby="tab-btn-summary">
        <div class="summary-container">
          <div class="summary-hero-box" style="background: linear-gradient(135deg, #1e3a8a 0%, #2563eb 100%);">
            <h2>
              <span class="lang-en">⚡ Quick Revision: ${enData.title}</span>
              <span class="lang-hi">⚡ त्वरित रिवीज़न: ${hiData.title_hi || enData.title}</span>
            </h2>
            <p>
              <span class="lang-en">Core formulas, rapid recall points, and distinguishing criteria at a glance.</span>
              <span class="lang-hi">मुख्य सूत्र, त्वरित स्मरण बिंदु एवं तुलनात्मक मानदंड एक नज़र में।</span>
            </p>
          </div>

${conceptsHtml}

          <h2>
            <span class="lang-en">📚 Terms & Units Glossary</span>
            <span class="lang-hi">📚 पारिभाषिक शब्दावली एवं इकाइयाँ</span>
          </h2>

${glossaryHtml}

          <h2>
            <span class="lang-en">🎯 Key Takeaways</span>
            <span class="lang-hi">🎯 महत्वपूर्ण निष्कर्ष (Key Takeaways)</span>
          </h2>
          <div class="lang-en">
            <ul class="summary-list">${enTakeaways}</ul>
          </div>
          <div class="lang-hi">
            <ul class="summary-list">${hiTakeaways}</ul>
          </div>

          <h2>
            <span class="lang-en">📌 Quick Recall</span>
            <span class="lang-hi">📌 त्वरित स्मरण (Quick Recall)</span>
          </h2>
          <div class="lang-en">
            <ul class="summary-list">${enRecall}</ul>
          </div>
          <div class="lang-hi">
            <ul class="summary-list">${hiRecall}</ul>
          </div>

          <h2>
            <span class="lang-en">⚖️ Key Differences</span>
            <span class="lang-hi">⚖️ महत्वपूर्ण अंतर (Key Differences)</span>
          </h2>
${differencesHtml}
        </div>
      </article>`;

  const sumStart = html.indexOf('<article class="tab-panel hidden" id="tab-summary"');
  const sumEnd = html.indexOf('</article>', sumStart);
  if (sumStart !== -1 && sumEnd !== -1) {
    html = html.substring(0, sumStart) + bilingualTab2.trim() + html.substring(sumEnd + '</article>'.length);
  }

  // 12. Tab 3: Practice Quiz Header & Cards Container
  html = html.replace(
    /<h2>❓ Practice Questions \((\d+) MCQs\)<\/h2>/,
    `<h2><span class="lang-en">❓ Practice Questions ($1 MCQs)</span><span class="lang-hi">❓ अभ्यास प्रश्न ($1 बहुविकल्पीय प्रश्न)</span></h2>`
  );
  html = html.replace(
    /<p>Select an option to test your understanding with instant verification and explanations\.<\/p>/,
    `<p><span class="lang-en">Select an option to test your understanding with instant verification and explanations.</span><span class="lang-hi">अपनी समझ का परीक्षण करने के लिए विकल्प चुनें। तत्काल समाधान एवं व्याख्या उपलब्ध।</span></p>`
  );
  html = html.replace(
    /<div class="score-pill">Score: <span id="quizScore">0<\/span> \/ (\d+)<\/div>/,
    `<div class="score-pill"><span class="lang-en">Score:</span><span class="lang-hi">स्कोर:</span> <span id="quizScore">0</span> / $1</div>`
  );
  html = html.replace(
    /<button type="button" class="btn-reset-quiz" id="btnResetQuiz">Restart Quiz<\/button>/,
    `<button type="button" class="btn-reset-quiz" id="btnResetQuiz"><span class="lang-en">Restart Quiz</span><span class="lang-hi">क्विज़ पुनः आरंभ करें</span></button>`
  );

  const qListStart = html.indexOf('<div class="quiz-questions-list">');
  const qArtEnd = html.indexOf('</article>', qListStart);
  if (qListStart !== -1 && qArtEnd !== -1 && Array.isArray(quizData)) {
    let quizCardsHtml = '\n';
    quizData.forEach((q, idx) => {
      const optsList = Array.isArray(q.options) && q.options.length === 4 ? q.options : ['Option A', 'Option B', 'Option C', 'Option D'];
      const opts = optsList.map((opt, oIdx) => {
        const optHi = (q.options_hi && q.options_hi[oIdx]) || opt;
        return `
      <button type="button" class="quiz-option-btn" data-qindex="${idx}" data-optindex="${oIdx}">
        <span class="option-letter">${letters[oIdx]}</span>
        <span class="option-text">
          <span class="lang-en">${opt}</span>
          <span class="lang-hi">${optHi}</span>
        </span>
      </button>`;
      }).join('');

      const qHi = q.question_hi || q.question;
      const expHi = q.explanation_hi || q.explanation || '';

      quizCardsHtml += `
      <div class="quiz-question-card" id="q-card-${idx}" data-correct="${q.correct_index ?? 0}">
        <div class="q-header">
          <span class="q-number">
            <span class="lang-en">Question ${idx + 1} of ${quizData.length}</span>
            <span class="lang-hi">प्रश्न ${idx + 1} / ${quizData.length}</span>
          </span>
        </div>
        <h3 class="q-text">
          <span class="lang-en">${q.question || 'Practice Question'}</span>
          <span class="lang-hi">${qHi}</span>
        </h3>
        <div class="quiz-options-group">${opts}
    </div>
        <div class="q-feedback hidden" id="feedback-${idx}">
          <div class="feedback-indicator"></div>
          <p class="feedback-explanation">
            <strong><span class="lang-en">Explanation:</span><span class="lang-hi">व्याख्या:</span></strong>
            <span class="lang-en">${q.explanation || 'See solution above.'}</span>
            <span class="lang-hi">${expHi}</span>
          </p>
        </div>
      </div>
    `;
    });
    quizCardsHtml += '\n        </div>\n      ';

    html = html.substring(0, qListStart + '<div class="quiz-questions-list">'.length) +
           quizCardsHtml +
           html.substring(qArtEnd);
  }

  // 13. Tab 4: PYQs & Trends Header & Cards Container
  html = html.replace(
    /<h2>🏛️ Exam Trends & Question Pattern<\/h2>/,
    `<h2><span class="lang-en">🏛️ Exam Trends & Question Pattern</span><span class="lang-hi">🏛️ परीक्षा ट्रेंड एवं प्रश्न पैटर्न</span></h2>`
  );
  html = html.replace(
    /<p>Historical question weightage and patterns for <strong>([\s\S]*?)<\/strong> in UP PGT Chemistry\.<\/p>/,
    `<p><span class="lang-en">Historical question weightage and patterns for <strong>${enData.title}</strong> in UP PGT Chemistry.</span><span class="lang-hi">UP PGT रसायन विज्ञान में <strong>${hiData.title_hi || enData.title}</strong> हेतु विगत वर्षों के प्रश्न भार एवं पैटर्न।</span></p>`
  );
  html = html.replace(
    /<span class="pyq-stat-label">Expected Questions<\/span>/,
    `<span class="pyq-stat-label"><span class="lang-en">Expected Questions</span><span class="lang-hi">अपेक्षित प्रश्न</span></span>`
  );
  html = html.replace(
    /<span class="pyq-stat-label">Topic Weightage<\/span>/,
    `<span class="pyq-stat-label"><span class="lang-en">Topic Weightage</span><span class="lang-hi">टॉपिक भार (Weightage)</span></span>`
  );
  html = html.replace(
    /<span class="pyq-stat-label">Difficulty<\/span>/,
    `<span class="pyq-stat-label"><span class="lang-en">Difficulty</span><span class="lang-hi">कठिनाई स्तर</span></span>`
  );

  const pListStart = html.indexOf('<div class="pyq-questions-list">');
  const pArtEnd = html.indexOf('</article>', pListStart);
  if (pListStart !== -1 && pArtEnd !== -1 && Array.isArray(pyqData)) {
    let pyqCardsHtml = '\n';
    pyqData.forEach((q, idx) => {
      const optsList = Array.isArray(q.options) && q.options.length === 4 ? q.options : ['Option A', 'Option B', 'Option C', 'Option D'];
      const opts = optsList.map((opt, oIdx) => {
        const optHi = (q.options_hi && q.options_hi[oIdx]) || opt;
        return `
      <button type="button" class="quiz-option-btn" data-pyqindex="${idx}" data-optindex="${oIdx}">
        <span class="option-letter">${letters[oIdx]}</span>
        <span class="option-text">
          <span class="lang-en">${opt}</span>
          <span class="lang-hi">${optHi}</span>
        </span>
      </button>`;
      }).join('');

      const correctIdx = (typeof q.correct_index === 'number' && q.correct_index >= 0 && q.correct_index < 4) ? q.correct_index : 0;
      const correctOptTextEn = optsList[correctIdx] || '';
      const correctOptTextHi = (q.options_hi && q.options_hi[correctIdx]) || correctOptTextEn;
      const qHi = q.question_hi || q.question;
      const expHi = q.explanation_hi || q.explanation || '';

      pyqCardsHtml += `
      <div class="pyq-card" id="pyq-card-${idx}" data-correct="${correctIdx}">
        <div class="pyq-header-meta">
          <span class="pyq-badge">${q.year_tag || 'UP PGT'}</span>
        </div>
        <div class="pyq-question-text">
          <span class="lang-en">${q.question || 'PYQ Question'}</span>
          <span class="lang-hi">${qHi}</span>
        </div>
        <div class="quiz-options-group">${opts}
    </div>
        <div class="pyq-expl-box hidden" id="pyq-expl-${idx}">
          <strong>
            <span class="lang-en">Answer: Option ${letters[correctIdx]} (${correctOptTextEn})</span>
            <span class="lang-hi">उत्तर: विकल्प ${letters[correctIdx]} (${correctOptTextHi})</span>
          </strong>
          <span class="lang-en">${q.explanation || ''}</span>
          <span class="lang-hi">${expHi}</span>
        </div>
      </div>
    `;
    });
    pyqCardsHtml += '\n        </div>\n      ';

    html = html.substring(0, pListStart + '<div class="pyq-questions-list">'.length) +
           pyqCardsHtml +
           html.substring(pArtEnd);
  }

  // 14. Tab 5: Timed Topic Test
  html = html.replace(
    /<h2>⏱️ Timed Topic Test<\/h2>/,
    `<h2><span class="lang-en">⏱️ Timed Topic Test</span><span class="lang-hi">⏱️ समयबद्ध टॉपिक टेस्ट</span></h2>`
  );
  html = html.replace(
    /<p>(\d+) questions &bull; (\d+) minutes &bull; Timed practice<\/p>/,
    `<p><span class="lang-en">$1 questions &bull; $2 minutes &bull; Timed practice</span><span class="lang-hi">$1 प्रश्न &bull; $2 मिनट &bull; समयबद्ध अभ्यास</span></p>`
  );
  html = html.replace(
    /<div class="test-instruction-box" id="testStartWrap">[\s\S]*?<h3>Instructions<\/h3>[\s\S]*?<ul>[\s\S]*?<\/ul>[\s\S]*?<button type="button" class="btn-start-test"[^>]*>Start Test<\/button>[\s\S]*?<\/div>/,
    `<div class="test-instruction-box" id="testStartWrap">
      <h3><span class="lang-en">Instructions</span><span class="lang-hi">निर्देश</span></h3>
      <ul>
        <li><strong><span class="lang-en">Questions:</span><span class="lang-hi">प्रश्न:</span></strong> <span class="lang-en">10 MCQs</span><span class="lang-hi">10 बहुविकल्पीय प्रश्न</span></li>
        <li><strong><span class="lang-en">Time Allowed:</span><span class="lang-hi">समय सीमा:</span></strong> <span class="lang-en">10 Minutes</span><span class="lang-hi">10 मिनट</span></li>
        <li><strong><span class="lang-en">Marking:</span><span class="lang-hi">अंकन:</span></strong> <span class="lang-en">+1 mark for correct, 0 for unattempted or wrong</span><span class="lang-hi">सही उत्तर हेतु +1 अंक, गलत या अनुत्तरित हेतु 0</span></li>
      </ul>
      <button type="button" class="btn-start-test" id="btnStartTest" style="background: linear-gradient(135deg, #1e3a8a, #2563eb);">
        <span class="lang-en">Start Test</span>
        <span class="lang-hi">टेस्ट प्रारंभ करें</span>
      </button>
    </div>`
  );

  const tListStart = html.indexOf('<div class="test-questions-list">');
  const tSubmitBar = html.indexOf('<div class="test-submit-bar">', tListStart);
  if (tListStart !== -1 && tSubmitBar !== -1 && Array.isArray(testData)) {
    let testCardsHtml = '\n';
    testData.forEach((t, idx) => {
      const optsList = Array.isArray(t.options) && t.options.length === 4 ? t.options : ['Option A', 'Option B', 'Option C', 'Option D'];
      const opts = optsList.map((opt, oIdx) => {
        const optHi = (t.options_hi && t.options_hi[oIdx]) || opt;
        return `
      <button type="button" class="test-option-btn" data-tindex="${idx}" data-optindex="${oIdx}">
        <span class="option-letter">${letters[oIdx]}</span>
        <span class="option-text">
          <span class="lang-en">${opt}</span>
          <span class="lang-hi">${optHi}</span>
        </span>
      </button>`;
      }).join('');

      const tHi = t.question_hi || t.question;
      const expHi = t.explanation_hi || t.explanation || '';

      testCardsHtml += `
      <div class="test-question-card" id="t-card-${idx}" data-correct="${t.correct_index ?? 0}">
        <div class="test-q-header">
          <span class="t-badge">
            <span class="lang-en">Question ${idx + 1} of ${testData.length}</span>
            <span class="lang-hi">प्रश्न ${idx + 1} / ${testData.length}</span>
          </span>
        </div>
        <div class="test-question-text">
          <span class="lang-en">${t.question || 'Test Question'}</span>
          <span class="lang-hi">${tHi}</span>
        </div>
        <div class="test-options-grid">${opts}
    </div>
        <div class="t-feedback hidden" id="t-feedback-${idx}">
          <p class="feedback-explanation">
            <strong><span class="lang-en">Solution:</span><span class="lang-hi">हल एवं व्याख्या:</span></strong>
            <span class="lang-en">${t.explanation || ''}</span>
            <span class="lang-hi">${expHi}</span>
          </p>
        </div>
      </div>
    `;
    });
    testCardsHtml += '\n          </div>\n          ';

    html = html.substring(0, tListStart + '<div class="test-questions-list">'.length) +
           testCardsHtml +
           html.substring(tSubmitBar);
  }

  // Submit test button
  html = html.replace(
    /<button type="button" class="btn-submit-test" id="btnSubmitTest"[^>]*>[\s\S]*?Submit Test[\s\S]*?<\/button>/,
    `<button type="button" class="btn-submit-test" id="btnSubmitTest" style="background: #2563eb;"><span class="lang-en">Submit Test</span><span class="lang-hi">टेस्ट जमा करें</span></button>`
  );

  // Result modal
  html = html.replace(
    /<h3>Test Result<\/h3>/,
    `<h3><span class="lang-en">Test Result</span><span class="lang-hi">परीक्षा परिणाम</span></h3>`
  );
  html = html.replace(
    /<p id="resFeedbackText">[\s\S]*?Review detailed solutions above for all questions\.[\s\S]*?<\/p>/,
    `<p id="resFeedbackText"><span class="lang-en">Review detailed solutions above for all questions.</span><span class="lang-hi">सभी प्रश्नों के विस्तृत समाधान ऊपर देखें।</span></p>`
  );
  html = html.replace(
    /<button type="button" class="btn-retake-test" id="btnRetakeTest">[\s\S]*?Retake Test[\s\S]*?<\/button>/,
    `<button type="button" class="btn-retake-test" id="btnRetakeTest"><span class="lang-en">Retake Test</span><span class="lang-hi">पुनः टेस्ट दें</span></button>`
  );

  // 15. Sidebar
  html = html.replace(
    /<span class="side-badge">Syllabus Section<\/span>/,
    `<span class="side-badge"><span class="lang-en">Syllabus Section</span><span class="lang-hi">पाठ्यक्रम अनुभाग</span></span>`
  );
  html = html.replace(
    /<h3>Physical Chemistry<\/h3>/,
    `<h3><span class="lang-en">Physical Chemistry</span><span class="lang-hi">भौतिक रसायन</span></h3>`
  );
  html = html.replace(
    /<h3>Inorganic Chemistry<\/h3>/,
    `<h3><span class="lang-en">Inorganic Chemistry</span><span class="lang-hi">अकार्बनिक रसायन</span></h3>`
  );
  html = html.replace(
    /<h3>Organic Chemistry<\/h3>/,
    `<h3><span class="lang-en">Organic Chemistry</span><span class="lang-hi">कार्बनिक रसायन</span></h3>`
  );
  html = html.replace(
    /<p class="side-desc">Branch topics covered under official UP PGT Chemistry curriculum\.<\/p>/,
    `<p class="side-desc"><span class="lang-en">Branch topics covered under official UP PGT Chemistry curriculum.</span><span class="lang-hi">आधिकारिक UP PGT रसायन विज्ञान पाठ्यक्रम के अंतर्गत शामिल विषय।</span></p>`
  );

  // 16. Bottom Navigation buttons
  html = html.replace(
    /<span>Exam Tracker →<\/span>/g,
    `<span class="lang-en">Exam Tracker →</span><span class="lang-hi">परीक्षा ट्रैकर →</span>`
  );
  html = html.replace(
    /<span>Next Topic →<\/span>/g,
    `<span class="lang-en">Next Topic →</span><span class="lang-hi">अगला टॉपिक →</span>`
  );
  html = html.replace(
    /<span>← Previous Topic<\/span>/g,
    `<span class="lang-en">← Previous Topic</span><span class="lang-hi">← पिछला टॉपिक</span>`
  );

  return html;
}

// Process a Single Topic Directory
async function processTopic(topicDir) {
  console.log(`\n========================================`);
  console.log(`Processing Topic: ${topicDir}`);
  console.log(`========================================`);

  const htmlPath = path.join(topicDir, 'index.html');
  const quizPath = path.join(topicDir, 'quiz.json');
  const testPath = path.join(topicDir, 'topic-test.json');
  const pyqPath = path.join(topicDir, 'pyq.json');

  if (!fs.existsSync(htmlPath)) {
    console.warn(`Skipping: ${htmlPath} does not exist.`);
    return false;
  }

  const html = fs.readFileSync(htmlPath, 'utf8');

  // Skip if already completely bilingual unless FORCE is true
  if (html.includes('class="lang-hi"') && html.includes('id="btn-lang-toggle"') && !FORCE) {
    const hasQuizHi = html.indexOf('<span class="lang-hi">') !== -1 && html.indexOf('quiz-questions-list') !== -1;
    if (hasQuizHi) {
      console.log(`Already fully bilingual. Skipping.`);
      return true;
    }
  }

  // 1. Extract and Translate Theory & Revision Summary
  console.log(`[1/3] Translating Theory & Revision Summary via ${MODEL_NAME}...`);
  const enData = extractComprehensiveContent(html);
  const hiData = await translateTheory(enData);

  // 2. Translate Quiz Questions
  let quizData = [];
  if (fs.existsSync(quizPath)) {
    console.log(`[2/3] Translating Practice Quiz (${quizPath})...`);
    quizData = JSON.parse(fs.readFileSync(quizPath, 'utf8'));
    if (!quizData[0]?.question_hi || FORCE) {
      const hiQuiz = await translateQuestions(quizData);
      quizData.forEach((q, idx) => {
        if (hiQuiz[idx]) {
          q.question_hi = hiQuiz[idx].question_hi;
          q.options_hi = hiQuiz[idx].options_hi;
          q.hint_hi = hiQuiz[idx].hint_hi;
          q.explanation_hi = hiQuiz[idx].explanation_hi;
        }
      });
      fs.writeFileSync(quizPath, JSON.stringify(quizData, null, 2), 'utf8');
    }
  }

  // 3. Translate PYQs and Topic Test together in 1 API call
  let pyqData = [];
  let testData = [];
  const needsPyq = fs.existsSync(pyqPath);
  const needsTest = fs.existsSync(testPath);

  if (needsPyq) pyqData = JSON.parse(fs.readFileSync(pyqPath, 'utf8'));
  if (needsTest) testData = JSON.parse(fs.readFileSync(testPath, 'utf8'));

  const pyqToTranslate = (needsPyq && (!pyqData[0]?.question_hi || FORCE)) ? pyqData : [];
  const testToTranslate = (needsTest && (!testData[0]?.question_hi || FORCE)) ? testData : [];

  if (pyqToTranslate.length > 0 || testToTranslate.length > 0) {
    console.log(`[3/3] Translating PYQs & Topic Test combined (${pyqToTranslate.length + testToTranslate.length} questions in 1 API call)...`);
    const combinedQueue = [...pyqToTranslate, ...testToTranslate];
    const translatedCombined = await translateQuestions(combinedQueue);

    if (pyqToTranslate.length > 0) {
      const hiPyqs = translatedCombined.slice(0, pyqToTranslate.length);
      pyqData.forEach((q, idx) => {
        if (hiPyqs[idx]) {
          q.question_hi = hiPyqs[idx].question_hi;
          q.options_hi = hiPyqs[idx].options_hi;
          q.hint_hi = hiPyqs[idx].hint_hi || '';
          q.explanation_hi = hiPyqs[idx].explanation_hi;
        }
      });
      fs.writeFileSync(pyqPath, JSON.stringify(pyqData, null, 2), 'utf8');
    }

    if (testToTranslate.length > 0) {
      const hiTest = translatedCombined.slice(pyqToTranslate.length);
      testData.forEach((q, idx) => {
        if (hiTest[idx]) {
          q.question_hi = hiTest[idx].question_hi;
          q.options_hi = hiTest[idx].options_hi;
          q.hint_hi = hiTest[idx].hint_hi || '';
          q.explanation_hi = hiTest[idx].explanation_hi;
        }
      });
      fs.writeFileSync(testPath, JSON.stringify(testData, null, 2), 'utf8');
    }
  }

  // Compile Comprehensive Bilingual HTML
  const bilingualHtml = buildCompleteBilingualHtml(html, enData, hiData, quizData, pyqData, testData);
  fs.writeFileSync(htmlPath, bilingualHtml, 'utf8');

  console.log(`✓ Successfully updated ${topicDir} to Full Bilingual (EN/HI)!`);
  return true;
}

// Main Driver
async function main() {
  if (TARGET_TOPIC) {
    const ok = await processTopic(TARGET_TOPIC);
    if (ok) {
      let completed = {};
      if (fs.existsSync(STATUS_FILE)) {
        try { completed = JSON.parse(fs.readFileSync(STATUS_FILE, 'utf8')); } catch (e) {}
      }
      completed[TARGET_TOPIC] = { translatedAt: new Date().toISOString() };
      fs.writeFileSync(STATUS_FILE, JSON.stringify(completed, null, 2), 'utf8');
    }
    return;
  }

  // Scan all chemistry directories recursively
  function getTopicDirs(dir) {
    let results = [];
    const list = fs.readdirSync(dir, { withFileTypes: true });
    for (const d of list) {
      const p = path.join(dir, d.name);
      if (d.isDirectory()) {
        if (fs.existsSync(path.join(p, 'index.html')) && fs.existsSync(path.join(p, 'quiz.json'))) {
          results.push(p);
        }
        results = results.concat(getTopicDirs(p));
      }
    }
    return [...new Set(results)];
  }

  const allTopics = getTopicDirs('chemistry');
  console.log(`Found ${allTopics.length} Chemistry topic directories.`);

  // Load status checkpoint
  let completed = {};
  if (fs.existsSync(STATUS_FILE)) {
    try {
      completed = JSON.parse(fs.readFileSync(STATUS_FILE, 'utf8'));
    } catch (e) {}
  }

  const isDone = (t) => completed[t] || completed[t.replace(/\\/g, '/')] || completed[t.replace(/\//g, '\\')];
  const topicsToProcess = allTopics.filter(t => !isDone(t) || FORCE);
  const queue = LIMIT ? topicsToProcess.slice(0, LIMIT) : topicsToProcess;
  console.log(`Topics remaining to process: ${queue.length} / ${allTopics.length}`);

  const CONCURRENCY = parseInt(getArg('--concurrency') || '2', 10);
  console.log(`Running with concurrency = ${CONCURRENCY} workers across ${apiKeys.length} API keys.`);

  let cursor = 0;
  let successCount = 0;

  async function worker(workerId) {
    while (cursor < queue.length) {
      const idx = cursor++;
      const topic = queue[idx];
      console.log(`\n[Worker ${workerId}] [${idx + 1}/${queue.length}] (${Math.round((idx / queue.length) * 100)}%) Starting: ${topic}`);
      try {
        const ok = await processTopic(topic);
        if (ok) {
          completed[topic] = { translatedAt: new Date().toISOString() };
          fs.writeFileSync(STATUS_FILE, JSON.stringify(completed, null, 2), 'utf8');
          successCount++;
        }
      } catch (err) {
        console.error(`[Worker ${workerId}] Error processing ${topic}:`, err.message);
      }
    }
  }

  const workers = Array.from({ length: Math.min(CONCURRENCY, queue.length) }, (_, i) => worker(i + 1));
  await Promise.all(workers);

  console.log(`\n========================================`);
  console.log(`Translation run completed: ${successCount} topics processed successfully.`);
  console.log(`========================================\n`);
}

main().catch(err => {
  console.error('FATAL:', err);
  process.exit(1);
});
