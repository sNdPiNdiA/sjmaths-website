#!/usr/bin/env node
/**
 * SJ Maths Physics content generator.
 *
 * Each topic is generated with exactly two Gemini calls:
 *   1. Study Notes: concepts, derivations, formulae, diagrams and numericals.
 *   2. Other tabs: revision, practice quiz, PYQ patterns and timed test.
 *
 * Pilot usage:
 *   node scripts/generate_physics.mjs --topic physics/electricity-and-magnetism/alternating-current/ --force
 *
 * Full generation is intentionally opt-in. Use --limit for a controlled batch.
 */

import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import 'dotenv/config';
import { GoogleGenAI } from '@google/genai';
import { jsonrepair } from 'jsonrepair';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const PHYSICS_ROOT = path.join(ROOT, 'physics');
const STATUS_FILE = path.join(ROOT, 'content-generation-status-physics.json');
const MODEL = 'gemini-3.5-flash-lite';

const args = process.argv.slice(2);
const hasFlag = flag => args.includes(flag);
function getArg(flag) {
  const index = args.indexOf(flag);
  return index >= 0 && args[index + 1] ? args[index + 1] : null;
}

const TARGET_TOPIC = getArg('--topic');
const TARGET_SECTION = getArg('--section');
const LIMIT = getArg('--limit') ? Number.parseInt(getArg('--limit'), 10) : null;
const FORCE = hasFlag('--force');
const DRY_RUN = hasFlag('--dry-run');
const RENDER_EXISTING = hasFlag('--render-existing');

const apiKeys = [...new Set([
  process.env.GEMINI_API_KEY,
  process.env.GEMINI_API_KEY_1,
  process.env.GEMINI_API_KEY_2
].filter(Boolean))];

if (!DRY_RUN && apiKeys.length === 0) {
  console.error('CRITICAL ERROR: No GEMINI_API_KEY defined in .env');
  process.exit(1);
}

const clients = apiKeys.map(key => new GoogleGenAI({ apiKey: key }));
let clientIndex = 0;

const SECTION_NAMES = {
  'electricity-and-magnetism': 'Electricity and Magnetism',
  mechanics: 'Mechanics',
  'modern-physics': 'Modern Physics',
  optics: 'Optics',
  'thermal-physics': 'Thermal Physics',
  'waves-and-oscillations': 'Waves and Oscillations'
};

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

function decodeHtml(value) {
  return String(value || '')
    .replace(/&amp;/g, '&').replace(/&quot;/g, '"').replace(/&#39;/g, "'")
    .replace(/&lt;/g, '<').replace(/&gt;/g, '>').trim();
}

function titleFromSlug(slug) {
  return slug.split('-').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' ');
}

function readTopicTitle(filePath) {
  const html = fs.readFileSync(filePath, 'utf8');
  const h1 = html.match(/<h1[^>]*>([\s\S]*?)<\/h1>/i)?.[1];
  return decodeHtml(h1?.replace(/<[^>]+>/g, '') || path.basename(path.dirname(filePath)));
}

function collectFiles(directory) {
  const entries = fs.readdirSync(directory, { withFileTypes: true });
  const files = [];
  for (const entry of entries) {
    if (entry.name.startsWith('.') || entry.name === 'node_modules') continue;
    const fullPath = path.join(directory, entry.name);
    if (entry.isDirectory()) files.push(...collectFiles(fullPath));
    else if (entry.isFile() && entry.name === 'index.html') files.push(fullPath);
  }
  return files;
}

function buildInventory() {
  return collectFiles(PHYSICS_ROOT).map(filePath => {
    const relative = path.relative(ROOT, path.dirname(filePath)).replace(/\\/g, '/');
    const parts = relative.split('/').filter(Boolean);
    const sectionKey = parts[1] || 'general';
    const url = `/${relative}/`;
    return {
      dir: relative,
      url,
      title: readTopicTitle(filePath),
      sectionKey,
      sectionTitle: SECTION_NAMES[sectionKey] || titleFromSlug(sectionKey)
    };
  }).sort((a, b) => a.url.localeCompare(b.url));
}

function eligibleTopics(inventory) {
  return inventory.filter(item => {
    if (TARGET_TOPIC) {
      const target = TARGET_TOPIC.startsWith('/') ? TARGET_TOPIC : `/${TARGET_TOPIC}`;
      return item.url === (target.endsWith('/') ? target : `${target}/`);
    }
    if (TARGET_SECTION && item.sectionKey !== TARGET_SECTION) return false;
    return FORCE || statusMap[item.url]?.status !== 'completed';
  });
}

function contextFor(item, inventory) {
  const index = inventory.findIndex(entry => entry.url === item.url);
  const related = inventory
    .filter(entry => entry.sectionKey === item.sectionKey && entry.url !== item.url)
    .slice(0, 6)
    .map(entry => ({ title: entry.title, url: entry.url }));
  return {
    previous: index > 0 ? inventory[index - 1] : null,
    next: index >= 0 && index < inventory.length - 1 ? inventory[index + 1] : null,
    related
  };
}

function studyPrompt(item, context) {
  return `You are an expert Physics professor preparing accurate, exam-ready study notes for Indian UP TGT Science and UP PGT Physics examinations.

Topic:
- Subject: Physics
- Branch: ${item.sectionTitle}
- Topic: ${item.title}
- Canonical URL: ${item.url}
- Related topics: ${context.related.map(topic => topic.title).join(', ') || 'None supplied'}

Write direct academic content. Do not use promotional filler, generic AI phrases, or claims such as "high-yield" or "students must master". Use SI units, correct signs, dimensions, assumptions and physical interpretation. Use HTML sub/sup tags in narrative text. In equation_html, use LaTeX commands without delimiters (for example \\frac, \\sqrt, \\omega); the renderer will typeset the equation. Do not invent PYQ years; PYQs are handled in the second call.

Return JSON only with this exact shape:
{
  "title": "Clean academic topic title",
  "short_intro": "Two factual sentences defining the topic.",
  "exam_scope": {"tgt_core": "TGT-level scope", "pgt_extension": "PGT-level extension"},
  "prerequisites": ["Prerequisite 1", "Prerequisite 2", "Prerequisite 3"],
  "concept_notes": [
    {"heading": "Authentic topic heading", "bullets": ["Precise fact", "Physical interpretation", "Condition or consequence"]}
  ],
  "derivations": [
    {"title": "Derivation name", "conditions": "Conditions", "steps": ["Step 1", "Step 2", "Step 3"], "result": "Final result"}
  ],
  "formula_sheet": [
    {"name": "Formula or law", "equation_html": "Equation", "variables": "Meaning of symbols", "units": "SI units", "conditions": "Validity conditions"}
  ],
  "graphs_and_experiments": [
    {"title": "Graph or experiment", "what_to_draw": "What the learner should draw", "interpretation": "Meaning", "exam_use": "How it is tested"}
  ],
  "solved_numericals": [
    {"level": "TGT core or PGT extension", "question": "Numerical question", "solution_steps": ["Step 1", "Step 2"], "answer": "Final answer with unit"}
  ],
  "assumptions_and_limitations": ["Assumption and its limitation"],
  "common_misconceptions": [
    {"wrong": "Incorrect belief", "correct": "Correct statement", "why": "Short explanation"}
  ],
  "quick_revision": ["One-line recall point"]
}

Requirements: at least 4 concept groups, 2 derivations where applicable, 8 formulae or key relations where applicable, 3 graph/experiment entries, and 3 solved numericals with at least one TGT and one PGT level. If a derivation or experiment is genuinely not applicable, state that explicitly instead of fabricating one.`;
}

function practicePrompt(item, study) {
  const studyContext = JSON.stringify({
    title: study.title,
    concepts: study.concept_notes,
    formulae: study.formula_sheet,
    misconceptions: study.common_misconceptions,
    scope: study.exam_scope
  });
  return `You are preparing the assessment and revision tabs for the Physics topic "${study.title}" for UP TGT Science and UP PGT Physics.

Use the following already-generated Study Notes as the only content anchor:
${studyContext}

Return JSON only with this exact shape:
{
  "revision": {
    "must_remember": ["Factual recall point"],
    "glossary": [{"term": "Term", "meaning": "Definition or symbol meaning"}],
    "comparisons": [{"title": "Comparison", "headers": ["Parameter", "A", "B"], "rows": [["Parameter", "A", "B"]]}]
  },
  "quiz": [
    {"question": "Conceptual or numerical MCQ", "options": ["A", "B", "C", "D"], "correct_index": 0, "explanation": "Why the answer is correct"}
  ],
  "pyq_patterns": [
    {"question": "Exam-pattern question", "options": ["A", "B", "C", "D"], "correct_index": 0, "explanation": "Answer explanation", "year_tag": "Model Question", "source_note": "Pattern-based practice; not an authenticated PYQ"}
  ],
  "topic_test": [
    {"question": "Timed-test MCQ", "options": ["A", "B", "C", "D"], "correct_index": 0, "explanation": "Answer explanation"}
  ]
}

Rules: create 15 quiz questions, 6 PYQ-pattern questions and 10 timed-test questions. Mix TGT core and PGT extension questions. Wrap every standalone mathematical expression in question, option and explanation text in $...$ delimiters. Do not invent an authentic exam year or pretend a model question is a PYQ. Use "Model Question" unless a year is explicitly supplied in the input. Ensure every correct_index is valid and every explanation is scientifically precise.`;
}

function cleanJson(text) {
  const withoutFence = String(text || '').replace(/^```(?:json)?\s*/i, '').replace(/\s*```$/i, '').trim();
  try {
    return JSON.parse(withoutFence);
  } catch {
    return JSON.parse(jsonrepair(withoutFence));
  }
}

async function callGemini(prompt) {
  const client = clients[clientIndex % clients.length];
  clientIndex += 1;
  const response = await client.models.generateContent({
    model: MODEL,
    contents: prompt,
    config: { responseMimeType: 'application/json', temperature: 0.2, maxOutputTokens: 32768 }
  });
  return cleanJson(response.text);
}

function assertArray(value, name, minimum = 1) {
  if (!Array.isArray(value) || value.length < minimum) {
    throw new Error(`${name} must contain at least ${minimum} items`);
  }
}

function validateStudy(data) {
  if (!data || typeof data.title !== 'string' || !data.title.trim()) throw new Error('Study title missing');
  assertArray(data.concept_notes, 'concept_notes', 4);
  assertArray(data.formula_sheet, 'formula_sheet', 2);
  assertArray(data.graphs_and_experiments, 'graphs_and_experiments', 2);
  assertArray(data.solved_numericals, 'solved_numericals', 3);
  assertArray(data.quick_revision, 'quick_revision', 1);
}

function normalizeStudy(data) {
  if (!Array.isArray(data.quick_revision)) data.quick_revision = [];
  const formulaFallbacks = (data.formula_sheet || [])
    .map(item => item.equation_html ? `${item.name}: ${item.equation_html}` : item.name)
    .filter(Boolean);
  const conceptFallbacks = (data.concept_notes || []).map(item => item.heading).filter(Boolean);
  for (const fallback of [...formulaFallbacks, ...conceptFallbacks]) {
    if (data.quick_revision.length >= 3) break;
    if (!data.quick_revision.includes(fallback)) data.quick_revision.push(fallback);
  }
  if (data.quick_revision.length === 0) data.quick_revision.push('Review the definitions, governing equations, conditions and common errors for this topic.');
  return data;
}

function validateQuestionSet(items, name, minimum) {
  assertArray(items, name, minimum);
  for (const [index, item] of items.entries()) {
    if (!item.question || !Array.isArray(item.options) || item.options.length !== 4) {
      throw new Error(`${name}[${index}] must have a question and four options`);
    }
    if (!Number.isInteger(item.correct_index) || item.correct_index < 0 || item.correct_index > 3) {
      throw new Error(`${name}[${index}] has an invalid correct_index`);
    }
  }
}

function validatePractice(data) {
  if (!data?.revision) throw new Error('revision object missing');
  assertArray(data.revision.must_remember, 'revision.must_remember', 1);
  assertArray(data.revision.glossary, 'revision.glossary', 1);
  validateQuestionSet(data.quiz, 'quiz', 15);
  validateQuestionSet(data.pyq_patterns, 'pyq_patterns', 6);
  validateQuestionSet(data.topic_test, 'topic_test', 10);
}

function normalizePractice(data, study) {
  if (!data.revision || typeof data.revision !== 'object') data.revision = {};
  if (!Array.isArray(data.revision.must_remember)) data.revision.must_remember = [];
  if (!Array.isArray(data.revision.glossary)) data.revision.glossary = [];
  if (!Array.isArray(data.revision.comparisons)) data.revision.comparisons = [];
  const formulas = (study.formula_sheet || []).filter(item => item.name);
  for (const formula of formulas) {
    if (data.revision.glossary.length >= 4) break;
    if (!data.revision.glossary.some(item => item.term === formula.name)) {
      data.revision.glossary.push({
        term: formula.name,
        meaning: `${formula.equation_html || ''}${formula.conditions ? ` (${formula.conditions})` : ''}`.trim()
      });
    }
  }
  for (const point of study.quick_revision || []) {
    if (data.revision.must_remember.length >= 4) break;
    if (!data.revision.must_remember.includes(point)) data.revision.must_remember.push(point);
  }
  if (data.revision.must_remember.length === 0) data.revision.must_remember.push('Review the topic formulae, conditions and standard problem method.');
  if (data.revision.glossary.length === 0) data.revision.glossary.push({ term: study.title, meaning: study.short_intro });
  return data;
}

function safe(value) {
  return String(value ?? '')
    .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;').replace(/'/g, '&#39;');
}

function rich(value) {
  return String(value ?? '')
    .replace(/<script[\s\S]*?<\/script>/gi, '')
    .replace(/\son[a-z]+\s*=\s*(['"]).*?\1/gi, '')
    .replace(/javascript:/gi, '');
}

function math(value) {
  return rich(value)
    .replace(/<sub>(.*?)<\/sub>/gi, '_{$1}')
    .replace(/<sup>(.*?)<\/sup>/gi, '^{$1}')
    .replace(/&pi;/gi, '\\pi')
    .replace(/&omega;/gi, '\\omega')
    .replace(/&phi;/gi, '\\phi')
    .replace(/&Omega;/gi, '\\Omega')
    .replace(/&times;/gi, '\\times ')
    .replace(/&approx;/gi, '\\approx ')
    .replace(/&radic;\[([^\]]+)\]/gi, '\\sqrt{$1}')
    .replace(/&radic;([^\s<]+)/gi, '\\sqrt{$1}')
    .replace(/&deg;/gi, '^\\circ');
}

function inlineMath(value) {
  const text = String(value ?? '');
  if (!/[=/_^*]|\b(?:omega|alpha|beta|gamma|theta|phi|pi|sqrt)\b/i.test(text)) return scientific(text);
  if (!/[=]/.test(text) && /\b[a-z]{3,}\s+[a-z]{3,}\b/i.test(text)) return scientific(text);
  const expression = text
    .replace(/\bomega\b/gi, '\\omega')
    .replace(/\balpha\b/gi, '\\alpha')
    .replace(/\bbeta\b/gi, '\\beta')
    .replace(/\bgamma\b/gi, '\\gamma')
    .replace(/\btheta\b/gi, '\\theta')
    .replace(/\bphi\b/gi, '\\phi')
    .replace(/\bpi\b/gi, '\\pi')
    .replace(/\bsqrt\b/gi, '\\sqrt')
    .replace(/([A-Za-z])_([A-Za-z0-9]+)/g, '$1_{$2}')
    .replace(/\^([A-Za-z0-9]+)/g, '^{$1}')
    .replace(/\s*\*\s*/g, ' \\cdot ');
  return `$${safe(expression)}$`;
}

function scientific(value) {
  return safe(value)
    .replace(/\b(omega|alpha|beta|gamma|theta|phi|pi)(?:_([A-Za-z0-9]+))?\b/gi, (match, name, subscript) => {
      const symbol = { omega: '\\omega', alpha: '\\alpha', beta: '\\beta', gamma: '\\gamma', theta: '\\theta', phi: '\\phi', pi: '\\pi' }[name.toLowerCase()] || name;
      return `$${symbol}${subscript ? `_{${subscript}}` : ''}$`;
    })
    .replace(/\b([IVRXZQPLC])_([A-Za-z0-9]+)(?:\^([A-Za-z0-9]+))?\b/g, (match, base, subscript, exponent) => `$${base}_{${subscript}}${exponent ? `^{${exponent}}` : ''}$`);
}

function list(items, renderer = safe) {
  return `<ul>${(items || []).map(item => `<li>${renderer(item)}</li>`).join('')}</ul>`;
}

function renderQuestionSet(items, prefix) {
  return (items || []).map((item, index) => `
    <article class="question" data-correct="${item.correct_index}">
      <h3>${index + 1}. ${scientific(item.question)}</h3>
      <div class="options">${item.options.map((option, optionIndex) => `<button type="button" class="option" data-index="${optionIndex}">${inlineMath(option)}</button>`).join('')}</div>
      <p class="answer" id="${prefix}-answer-${index}"><strong>Explanation:</strong> ${scientific(item.explanation)}</p>
    </article>`).join('');
}

function renderStudy(study) {
  const conceptHtml = study.concept_notes.map(group => `<section class="card"><h2>${safe(group.heading)}</h2>${list(group.bullets, rich)}</section>`).join('');
  const derivationHtml = study.derivations.map(entry => `<article class="subcard"><h3>${safe(entry.title)}</h3><p><strong>Conditions:</strong> ${safe(entry.conditions)}</p>${list(entry.steps, rich)}<p class="result"><strong>Result:</strong> ${rich(entry.result)}</p></article>`).join('');
  const formulaHtml = `<div class="table-wrap"><table><thead><tr><th>Formula / law</th><th>Equation</th><th>Variables and units</th><th>Conditions</th></tr></thead><tbody>${study.formula_sheet.map(entry => `<tr><td>${safe(entry.name)}</td><td class="equation">$$${math(entry.equation_html)}$$</td><td>${rich(entry.variables)}<br>${rich(entry.units)}</td><td>${safe(entry.conditions)}</td></tr>`).join('')}</tbody></table></div>`;
  const graphHtml = study.graphs_and_experiments.map(entry => `<article class="subcard"><h3>${safe(entry.title)}</h3><p><strong>Draw:</strong> ${safe(entry.what_to_draw)}</p><p><strong>Interpret:</strong> ${safe(entry.interpretation)}</p><p><strong>Exam use:</strong> ${safe(entry.exam_use)}</p></article>`).join('');
  const numericalHtml = study.solved_numericals.map(entry => `<article class="subcard"><span class="level">${safe(entry.level)}</span><h3>${safe(entry.question)}</h3>${list(entry.solution_steps, rich)}<p class="result"><strong>Answer:</strong> ${rich(entry.answer)}</p></article>`).join('');
  const misconceptionHtml = study.common_misconceptions.map(entry => `<article class="comparison"><p><strong>Common error:</strong> ${safe(entry.wrong)}</p><p><strong>Correct:</strong> ${safe(entry.correct)}</p><p>${safe(entry.why)}</p></article>`).join('');
  return `<div class="study-grid">
    <section class="card"><h2>Scope and prerequisites</h2><div class="scope-grid"><div><h3>TGT core</h3><p>${safe(study.exam_scope?.tgt_core)}</p></div><div><h3>PGT extension</h3><p>${safe(study.exam_scope?.pgt_extension)}</p></div></div><h3>Prerequisites</h3>${list(study.prerequisites, safe)}</section>
    ${conceptHtml}
    <section class="card"><h2>Derivations</h2>${derivationHtml}</section>
    <section class="card"><h2>Formula sheet</h2>${formulaHtml}</section>
    <section class="card"><h2>Graphs and experiments</h2>${graphHtml}</section>
    <section class="card"><h2>Solved numericals</h2>${numericalHtml}</section>
    <section class="card"><h2>Assumptions and limitations</h2>${list(study.assumptions_and_limitations, rich)}</section>
    <section class="card"><h2>Common misconceptions</h2>${misconceptionHtml}</section>
    <section class="card"><h2>Quick revision</h2>${list(study.quick_revision, rich)}</section>
  </div>`;
}

function renderOtherTabs(practice) {
  const revision = `<section class="card"><h2>Must remember</h2>${list(practice.revision.must_remember, rich)}<h2>Glossary</h2><div class="glossary">${practice.revision.glossary.map(item => `<div><strong>${safe(item.term)}</strong><span>${safe(item.meaning)}</span></div>`).join('')}</div>${(practice.revision.comparisons || []).map(item => `<h2>${safe(item.title)}</h2><div class="table-wrap"><table><thead><tr>${item.headers.map(header => `<th>${safe(header)}</th>`).join('')}</tr></thead><tbody>${item.rows.map(row => `<tr>${row.map(cell => `<td>${rich(cell)}</td>`).join('')}</tr>`).join('')}</tbody></table></div>`).join('')}</section>`;
  return { revision, quiz: renderQuestionSet(practice.quiz, 'quiz'), pyq: renderQuestionSet(practice.pyq_patterns, 'pyq'), test: renderQuestionSet(practice.topic_test, 'test') };
}

function renderHtml(item, context, study, practice) {
  const title = study.title || item.title;
  const description = `${title}: Physics study notes, derivations, formulae, solved numericals and TGT/PGT practice.`;
  const canonical = `https://sjmaths.com${item.url}`;
  const other = renderOtherTabs(practice);
  const related = context.related.map(entry => `<a href="${safe(entry.url)}">${safe(entry.title)}</a>`).join('');
  return `<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>${safe(title)} — Physics Notes | SJ Maths</title>
<meta name="description" content="${safe(description)}"><meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large,max-video-preview:-1">
<link rel="canonical" href="${canonical}"><link rel="icon" type="image/png" href="/favicon.png">
<meta property="og:type" content="article"><meta property="og:site_name" content="SJ Maths"><meta property="og:title" content="${safe(title)} — Physics Notes"><meta property="og:description" content="${safe(description)}"><meta property="og:url" content="${canonical}">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css"><script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script><script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" onload="renderMathInElement(document.body,{delimiters:[{left:'$$',right:'$$',display:true},{left:'$',right:'$',display:false}],throwOnError:false})"></script>
<script type="application/ld+json">${JSON.stringify({'@context':'https://schema.org','@type':'LearningResource',name:title,headline:`${title} — Physics Notes`,description,url:canonical,isPartOf:{'@type':'WebSite',name:'SJ Maths',url:'https://sjmaths.com/'}})}</script>
<style>
:root{--bg:#f6f8fb;--paper:#fff;--ink:#182238;--muted:#667085;--line:#dfe6ef;--brand:#16324f;--accent:#0e7490;--soft:#eef8fa;--bad:#fff1f0;--good:#e8f7ef}*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.55 Inter,system-ui,-apple-system,"Segoe UI",sans-serif}a{color:inherit}.wrap{width:min(1180px,calc(100% - 32px));margin:auto}.site-header{position:sticky;top:0;z-index:5;background:#fff;border-bottom:1px solid var(--line)}.header-inner{min-height:66px;display:flex;align-items:center;justify-content:space-between;gap:16px}.brand{display:flex;gap:10px;align-items:center;text-decoration:none}.brand-mark{width:38px;height:38px;border-radius:10px;background:var(--brand);display:grid;place-items:center;color:#fff;font-weight:900}.brand-name{font-weight:850;display:block}.brand-sub{font-size:.7rem;color:var(--muted);display:block}.back{padding:8px 12px;border:1px solid var(--line);border-radius:999px;text-decoration:none;font-size:.8rem;font-weight:700}.hero{padding:36px 0 22px}.crumbs{font-size:.8rem;color:var(--muted);margin-bottom:14px}.kicker{color:var(--accent);font-weight:800;text-transform:uppercase;letter-spacing:.1em;font-size:.75rem}.hero h1{font-size:clamp(2rem,4vw,3.2rem);line-height:1.1;margin:10px 0}.lead{max-width:900px;color:#4b5565}.badges{display:flex;gap:8px;flex-wrap:wrap}.badge{padding:5px 10px;border:1px solid #cfe1e6;border-radius:999px;background:#fff;color:var(--accent);font-size:.75rem;font-weight:800}.tabs{display:flex;gap:8px;flex-wrap:wrap;margin:16px 0}.tab{border:1px solid var(--line);background:#fff;color:var(--brand);border-radius:10px;padding:10px 13px;font-weight:800;cursor:pointer}.tab.active,.tab:hover{background:var(--accent);color:#fff;border-color:var(--accent)}.panel{display:none}.panel.active{display:block}.study-grid{display:grid;gap:18px}.card,.subcard,.question,.comparison{background:#fff;border:1px solid var(--line);border-radius:16px;padding:20px;box-shadow:0 2px 10px #1c273c08}.card h2{font-size:1.3rem;margin:0 0 14px}.card h3,.subcard h3{margin:0 0 8px}.card p,.subcard p{color:#4b5565}.card ul,.subcard ul{padding-left:21px}.card li{margin:7px 0}.scope-grid{display:grid;grid-template-columns:1fr 1fr;gap:14px}.scope-grid>div{background:var(--soft);padding:15px;border-radius:12px}.scope-grid p{margin:0}.subcard{margin:12px 0;background:#fbfcfe}.result{border-left:4px solid var(--accent);padding-left:12px}.level{display:inline-block;color:var(--accent);font-size:.72rem;font-weight:900;text-transform:uppercase;letter-spacing:.08em;margin-bottom:6px}.table-wrap{overflow:auto}table{width:100%;border-collapse:collapse;min-width:680px}th,td{text-align:left;vertical-align:top;padding:10px;border:1px solid var(--line)}th{background:#f0f5f8}.equation{font-size:1.05rem}.glossary{display:grid;gap:8px}.glossary div{display:grid;grid-template-columns:180px 1fr;gap:12px;border-bottom:1px solid var(--line);padding:8px 0}.question{margin:14px 0}.question h3{margin:0 0 12px;font-size:1rem}.options{display:grid;gap:8px}.option{padding:10px 12px;text-align:left;background:#fff;border:1px solid var(--line);border-radius:9px;cursor:pointer}.option:hover{border-color:var(--accent)}.option.correct{background:var(--good);border-color:#39a66b}.option.incorrect{background:var(--bad);border-color:#dc6b64}.answer{display:none;color:#4b5565;margin:12px 0 0}.question.answered .answer{display:block}.related{display:flex;gap:8px;flex-wrap:wrap;margin:16px 0 50px}.related a{padding:7px 10px;background:#fff;border:1px solid var(--line);border-radius:8px;text-decoration:none;font-size:.8rem}.footer{padding:28px 0;background:#fff;border-top:1px solid var(--line);color:var(--muted);font-size:.8rem}@media(max-width:680px){.scope-grid{grid-template-columns:1fr}.glossary div{grid-template-columns:1fr}.header-inner{align-items:flex-start;padding:12px 0;flex-direction:column}}
</style></head><body>
<header class="site-header"><div class="wrap header-inner"><a class="brand" href="/"><span class="brand-mark">&int;</span><span><span class="brand-name">SJ Maths</span><span class="brand-sub">Physics TGT / PGT Preparation</span></span></a><a class="back" href="/up-pgt-physics/">← Physics Tracker</a></div></header>
<main class="wrap"><section class="hero"><div class="crumbs"><a href="/">Home</a> › <a href="/up-pgt-physics/">Physics</a> › ${safe(item.sectionTitle)} › ${safe(title)}</div><div class="kicker">${safe(item.sectionTitle)}</div><h1>${safe(title)}</h1><p class="lead">${safe(study.short_intro)}</p><div class="badges"><span class="badge">UP TGT Science</span><span class="badge">UP PGT Physics</span><span class="badge">Study Notes + Practice</span></div></section>
<nav class="tabs" aria-label="Study sections"><button class="tab active" data-panel="study">📖 Study Notes</button><button class="tab" data-panel="revision">⚡ Revision</button><button class="tab" data-panel="quiz">❓ Practice Quiz</button><button class="tab" data-panel="pyq">🏛️ PYQ Patterns</button><button class="tab" data-panel="test">⏱️ Timed Test</button></nav>
<section id="study" class="panel active">${renderStudy(study)}</section><section id="revision" class="panel">${other.revision}</section><section id="quiz" class="panel"><div class="card"><h2>Practice Quiz</h2><p>Choose an option to reveal the explanation.</p>${other.quiz}</div></section><section id="pyq" class="panel"><div class="card"><h2>PYQ Patterns</h2><p>These are pattern-based practice questions. Authentic year labels are only used when verified from a source.</p>${other.pyq}</div></section><section id="test" class="panel"><div class="card"><h2>Timed Topic Test</h2><p>Attempt these questions under a ten-minute limit using a separate timer.</p>${other.test}</div></section>
<div class="related"><strong>Related topics:</strong>${related}</div></main><footer class="footer"><div class="wrap">SJ Maths • Physics preparation for UP TGT Science and UP PGT Physics</div></footer>
<script>
document.querySelectorAll('.tab').forEach(function(tab){tab.addEventListener('click',function(){document.querySelectorAll('.tab').forEach(function(item){item.classList.remove('active')});document.querySelectorAll('.panel').forEach(function(item){item.classList.remove('active')});tab.classList.add('active');document.getElementById(tab.dataset.panel).classList.add('active')})});
document.querySelectorAll('.question').forEach(function(card){var correct=Number(card.dataset.correct);card.querySelectorAll('.option').forEach(function(button){button.addEventListener('click',function(){if(card.classList.contains('answered'))return;card.classList.add('answered');card.querySelectorAll('.option').forEach(function(option,index){option.disabled=true;if(index===correct)option.classList.add('correct');else if(option===button)option.classList.add('incorrect')})})})});
</script></body></html>`;
}

async function processTopic(item, inventory) {
  const context = contextFor(item, inventory);
  console.log(`\n[Physics] ${item.url} — ${item.title}`);
  if (DRY_RUN) {
    console.log(`[DRY RUN] Would make 2 ${MODEL} calls and write ${item.dir}/index.html plus JSON tabs.`);
    return true;
  }

  if (RENDER_EXISTING) {
    const targetDir = path.join(ROOT, item.dir);
    const study = JSON.parse(fs.readFileSync(path.join(targetDir, 'study-notes.json'), 'utf8'));
    const practice = {
      revision: JSON.parse(fs.readFileSync(path.join(targetDir, 'revision.json'), 'utf8')),
      quiz: JSON.parse(fs.readFileSync(path.join(targetDir, 'quiz.json'), 'utf8')),
      pyq_patterns: JSON.parse(fs.readFileSync(path.join(targetDir, 'pyq.json'), 'utf8')),
      topic_test: JSON.parse(fs.readFileSync(path.join(targetDir, 'topic-test.json'), 'utf8'))
    };
    validateStudy(study);
    validatePractice(practice);
    fs.writeFileSync(path.join(targetDir, 'index.html'), renderHtml(item, context, study, practice), 'utf8');
    console.log(`  Re-rendered existing JSON without an API call: ${item.dir}/index.html`);
    return true;
  }

  statusMap[item.url] = { status: 'generating', startedAt: new Date().toISOString(), model: MODEL, calls: 0 };
  saveStatus();

  console.log('  Call 1/2: generating Study Notes...');
  const study = normalizeStudy(await callGemini(studyPrompt(item, context)));
  validateStudy(study);
  statusMap[item.url].calls = 1;

  console.log('  Call 2/2: generating revision and assessment tabs...');
  const practice = normalizePractice(await callGemini(practicePrompt(item, study)), study);
  validatePractice(practice);
  statusMap[item.url].calls = 2;

  const targetDir = path.join(ROOT, item.dir);
  fs.mkdirSync(targetDir, { recursive: true });
  fs.writeFileSync(path.join(targetDir, 'study-notes.json'), JSON.stringify(study, null, 2), 'utf8');
  fs.writeFileSync(path.join(targetDir, 'revision.json'), JSON.stringify(practice.revision, null, 2), 'utf8');
  fs.writeFileSync(path.join(targetDir, 'quiz.json'), JSON.stringify(practice.quiz, null, 2), 'utf8');
  fs.writeFileSync(path.join(targetDir, 'pyq.json'), JSON.stringify(practice.pyq_patterns, null, 2), 'utf8');
  fs.writeFileSync(path.join(targetDir, 'topic-test.json'), JSON.stringify(practice.topic_test, null, 2), 'utf8');
  fs.writeFileSync(path.join(targetDir, 'index.html'), renderHtml(item, context, study, practice), 'utf8');

  statusMap[item.url] = {
    status: 'completed', model: MODEL, calls: 2, title: study.title,
    quizCount: practice.quiz.length, pyqCount: practice.pyq_patterns.length,
    testCount: practice.topic_test.length, completedAt: new Date().toISOString(), reviewed: false
  };
  saveStatus();
  console.log(`  Saved generated Physics tabs to ${item.dir}`);
  return true;
}

async function main() {
  const inventory = buildInventory();
  if (!inventory.length) throw new Error('No physics/index.html topics found.');
  const topics = eligibleTopics(inventory);
  const selected = LIMIT ? topics.slice(0, LIMIT) : topics;
  console.log(`Physics inventory: ${inventory.length} topics; selected: ${selected.length}; model: ${MODEL}`);
  if (!DRY_RUN) console.log(`API keys available: ${apiKeys.length}; calls per topic: 2`);

  let completed = 0;
  for (const item of selected) {
    try {
      if (await processTopic(item, inventory)) completed += 1;
    } catch (error) {
      console.error(`  Failed ${item.url}: ${error.message}`);
      statusMap[item.url] = { status: 'failed', model: MODEL, error: error.message, failedAt: new Date().toISOString() };
      saveStatus();
    }
  }
  console.log(`Finished: ${completed}/${selected.length}`);
}

main().catch(error => {
  console.error('Fatal Physics generator error:', error);
  process.exit(1);
});
