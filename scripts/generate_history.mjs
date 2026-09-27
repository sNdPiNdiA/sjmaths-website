#!/usr/bin/env node
/**
 * SJ Maths History Topic Content Generator
 * Generates point-wise, high-yield study notes, key concepts, quick revision,
 * self-assessment checklist, and exam PYQ facts for history pages using Gemini 3.5 Flash Lite.
 *
 * Usage:
 *   node scripts/generate_history.mjs --dry-run
 *   node scripts/generate_history.mjs --topic ancient-india/religious-movements/bhagvatism
 *   node scripts/generate_history.mjs --limit 5
 *   node scripts/generate_history.mjs --all
 */

import fs from 'node:fs';
import path from 'node:path';
import 'dotenv/config';
import { GoogleGenAI } from '@google/genai';
import { jsonrepair } from 'jsonrepair';
import * as cheerio from 'cheerio';

const ROOT = process.cwd();
const HISTORY_ROOT = path.join(ROOT, 'history');
const STATUS_PATH = path.join(ROOT, 'content-generation-status-history.json');
const MODEL = process.env.GEMINI_MODEL || 'gemini-3.5-flash-lite';

// API Key rotation / fallback support
const API_KEYS = [
  process.env.GEMINI_API_KEY_1,
  process.env.GEMINI_API_KEY_2,
  process.env.GEMINI_API_KEY
].filter(Boolean);

if (API_KEYS.length === 0) {
  console.error('ERROR: No GEMINI_API_KEY configured in environment or .env');
  process.exit(1);
}

let keyIndex = 0;
function getAIClient() {
  const key = API_KEYS[keyIndex % API_KEYS.length];
  return new GoogleGenAI({ apiKey: key });
}

function rotateKey() {
  keyIndex = (keyIndex + 1) % API_KEYS.length;
  console.log(`Switching to API key index ${keyIndex}`);
}

const args = process.argv.slice(2);
const hasFlag = (f) => args.includes(f);
function getArg(flag) {
  const i = args.indexOf(flag);
  return i >= 0 ? args[i + 1] : null;
}

const requestedTopic = getArg('--topic');
const requestedLimit = getArg('--limit') ? parseInt(getArg('--limit'), 10) : 0;
const dryRun = hasFlag('--dry-run');
const force = hasFlag('--force');
const allFlag = hasFlag('--all');
const gapMs = Math.max(0, parseInt(getArg('--gap') || '1', 10)) * 1000;

function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

function readStatus() {
  if (!fs.existsSync(STATUS_PATH)) return {};
  try {
    return JSON.parse(fs.readFileSync(STATUS_PATH, 'utf8'));
  } catch {
    return {};
  }
}

function writeStatus(status) {
  try {
    fs.writeFileSync(STATUS_PATH, JSON.stringify(status, null, 2) + '\n', 'utf8');
  } catch (err) {
    console.warn('Warning: Could not update status log:', err.message);
  }
}

function escapeHtml(str) {
  return String(str || '')
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}

function discoverHistoryPages(dir) {
  let results = [];
  const entries = fs.readdirSync(dir, { withFileTypes: true });
  for (const entry of entries) {
    const fullPath = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      results = results.concat(discoverHistoryPages(fullPath));
    } else if (entry.name === 'index.html') {
      const relPath = path.relative(HISTORY_ROOT, fullPath).replace(/\\/g, '/');
      results.push({
        fullPath,
        relPath, // e.g. "ancient-india/religious-movements/bhagvatism/index.html"
        topicDir: path.dirname(relPath)
      });
    }
  }
  return results;
}

function isPlaceholderContent(html) {
  return (
    html.includes('Understanding standard terminology, scope, and basic assumptions') ||
    html.includes('Mathematical expressions, properties, and governing relationships') ||
    html.includes('Typical numerical applications and conceptual scenarios') ||
    !html.includes('study-notes-list')
  );
}

function buildPrompt(metadata) {
  return `You are a distinguished Professor of History and Subject Expert for Indian competitive exams (UP TGT Social Science, UP PGT History, UPSC, State PCS, UGC NET).

Create comprehensive, accurate, high-yield STUDY NOTES for the following topic:
- Topic Title: "${metadata.title}"
- Breadcrumb / Section: "${metadata.breadcrumb}"
- Hierarchy Context: "${metadata.kicker}"
- Target Exam Audience: UP TGT Social Science / UP PGT History / Competitive Exams

IMPORTANT FORMATTING RULES:
1. All study notes MUST be POINT-WISE (bullet points). NEVER produce long walls of text or paragraphs.
2. Every point should begin with a bold keyword or sub-concept (e.g., "• <strong>Origins & Sources:</strong> ...").
3. Include specific names, dates, archaeological sites, literary sources, inscriptions, rulers, and architectural or socio-economic facts.
4. Keep the content academically rigorous and verified.
5. Provide the output in RAW JSON format only (no markdown fencing, no preamble).

JSON SCHEMA REQUIRED:
{
  "syllabus_focus_points": [
    "High-yield syllabus focus point 1",
    "High-yield syllabus focus point 2",
    "High-yield syllabus focus point 3",
    "High-yield syllabus focus point 4"
  ],
  "study_sections": [
    {
      "heading": "Section Heading (e.g., Historical Background & Sources)",
      "points": [
        "Point 1 with <strong>Bold Keyword</strong>: Clear, factual note",
        "Point 2 with <strong>Bold Keyword</strong>: Clear, factual note",
        "Point 3 with <strong>Bold Keyword</strong>: Clear, factual note",
        "Point 4 with <strong>Bold Keyword</strong>: Clear, factual note"
      ]
    },
    {
      "heading": "Section Heading (e.g., Core Principles, Beliefs & Developments)",
      "points": [
        "Point 1 with <strong>Bold Keyword</strong>: Detailed factual point",
        "Point 2 with <strong>Bold Keyword</strong>: Detailed factual point",
        "Point 3 with <strong>Bold Keyword</strong>: Detailed factual point",
        "Point 4 with <strong>Bold Keyword</strong>: Detailed factual point"
      ]
    },
    {
      "heading": "Section Heading (e.g., Significant Figures, Sites & Chronology)",
      "points": [
        "Point 1 with <strong>Bold Keyword</strong>: Specific names, sites, or dates",
        "Point 2 with <strong>Bold Keyword</strong>: Specific names, sites, or dates",
        "Point 3 with <strong>Bold Keyword</strong>: Specific names, sites, or dates",
        "Point 4 with <strong>Bold Keyword</strong>: Specific names, sites, or dates"
      ]
    },
    {
      "heading": "Section Heading (e.g., Impact, Legacy & Historiography)",
      "points": [
        "Point 1 with <strong>Bold Keyword</strong>: Analysis, legacy, or historical significance",
        "Point 2 with <strong>Bold Keyword</strong>: Analysis, legacy, or historical significance",
        "Point 3 with <strong>Bold Keyword</strong>: Analysis, legacy, or historical significance",
        "Point 4 with <strong>Bold Keyword</strong>: Analysis, legacy, or historical significance"
      ]
    }
  ],
  "key_facts_revision": [
    "Essential fact 1 frequently asked in exam papers",
    "Essential fact 2 frequently asked in exam papers",
    "Essential fact 3 frequently asked in exam papers",
    "Essential fact 4 frequently asked in exam papers",
    "Essential fact 5 frequently asked in exam papers",
    "Essential fact 6 frequently asked in exam papers"
  ],
  "exam_traps_and_distinctions": [
    "Common misconception or exam trap to avoid 1",
    "Common misconception or exam trap to avoid 2",
    "Common misconception or exam trap to avoid 3"
  ],
  "interactive_checklist": [
    "Checklist item 1 specific to this topic",
    "Checklist item 2 specific to this topic",
    "Checklist item 3 specific to this topic",
    "Checklist item 4 specific to this topic",
    "Checklist item 5 specific to this topic"
  ]
}`;
}

async function generateContentWithRetry(prompt, maxAttempts = 3) {
  let attempt = 0;
  while (attempt < maxAttempts) {
    attempt++;
    try {
      const client = getAIClient();
      const response = await client.models.generateContent({
        model: MODEL,
        contents: prompt
      });

      let text = response.text || '';
      text = text.trim().replace(/^```(?:json)?\s*/i, '').replace(/\s*```$/i, '').trim();

      try {
        return JSON.parse(text);
      } catch (err) {
        return JSON.parse(jsonrepair(text));
      }
    } catch (err) {
      console.warn(`Attempt ${attempt} failed: ${err.message}`);
      if (err.message?.includes('429') || err.message?.includes('quota') || err.message?.includes('ResourceExhausted')) {
        rotateKey();
        await sleep(3000 * attempt);
      } else {
        await sleep(1500 * attempt);
      }
      if (attempt >= maxAttempts) throw err;
    }
  }
}

function renderHtml(originalHtml, data, metadata) {
  const $ = cheerio.load(originalHtml);

  // Update lead text if suitable
  if (metadata.title) {
    $('.hero h1').text(metadata.title);
  }

  // Build the new point-wise cards inside .content-col
  const contentCol = $('.main-grid .content-col');
  contentCol.empty();

  // Card 1: Syllabus Overview & Exam Focus (Point-wise)
  let card1Html = `<article class="card">
    <h2>1. Syllabus Overview & Exam Focus</h2>
    <p>In competitive examinations (UP TGT Social Science / UP PGT History / UGC NET), <strong>${escapeHtml(metadata.title)}</strong> is a key tested topic. Focus your preparation on the following high-priority points:</p>
    <ul class="point-notes">`;
  for (const pt of (data.syllabus_focus_points || [])) {
    card1Html += `<li>${pt}</li>`;
  }
  card1Html += `</ul>
  </article>`;
  contentCol.append(card1Html);

  // Card 2+: Study Notes Sections (Point-wise notes)
  let sectionIndex = 2;
  for (const section of (data.study_sections || [])) {
    let secHtml = `<article class="card">
      <h2>${sectionIndex}. ${escapeHtml(section.heading)}</h2>
      <ul class="point-notes">`;
    for (const pt of (section.points || [])) {
      secHtml += `<li>${pt}</li>`;
    }
    secHtml += `</ul>
    </article>`;
    contentCol.append(secHtml);
    sectionIndex++;
  }

  // Card: High-Yield Key Facts & Chronology
  if (Array.isArray(data.key_facts_revision) && data.key_facts_revision.length > 0) {
    let factsHtml = `<article class="card">
      <h2>${sectionIndex}. High-Yield Key Facts & Exam Memory Points</h2>
      <div class="quick-facts-box">
        <ul class="point-notes">`;
    for (const fact of data.key_facts_revision) {
      factsHtml += `<li><strong>Key Fact:</strong> ${fact}</li>`;
    }
    factsHtml += `</ul>
      </div>
    </article>`;
    contentCol.append(factsHtml);
    sectionIndex++;
  }

  // Card: Common Misconceptions & Exam Traps
  if (Array.isArray(data.exam_traps_and_distinctions) && data.exam_traps_and_distinctions.length > 0) {
    let trapsHtml = `<article class="card">
      <h2>${sectionIndex}. Common Exam Pitfalls & Confusions to Avoid</h2>
      <ul class="point-notes warning-points">`;
    for (const trap of data.exam_traps_and_distinctions) {
      trapsHtml += `<li>${trap}</li>`;
    }
    trapsHtml += `</ul>
    </article>`;
    contentCol.append(trapsHtml);
    sectionIndex++;
  }

  // Card: Topic Self-Assessment Checklist
  const checklistItems = Array.isArray(data.interactive_checklist) && data.interactive_checklist.length > 0
    ? data.interactive_checklist
    : [
        `Master fundamental chronology and sources for ${metadata.title}`,
        `Understand key terms, inscriptions, and archaeological findings`,
        `Review major rulers, thinkers, or socio-economic dynamics`,
        `Solve minimum 20 previous years' questions (PYQ)`,
        `Mark complete on the main syllabus tracker`
      ];

  let checkHtml = `<article class="card">
    <h2>${sectionIndex}. Self-Assessment & Topic Checklist</h2>
    <p>Check off each item as you master the factual and analytical aspects of <strong>${escapeHtml(metadata.title)}</strong>:</p>
    <div class="checklist">`;
  for (const item of checklistItems) {
    checkHtml += `<label class="check-item"><input type="checkbox"> <span>${item}</span></label>`;
  }
  checkHtml += `</div>
  </article>`;
  contentCol.append(checkHtml);

  // Ensure styling for point-notes is present in <style>
  if (!$('style').text().includes('.point-notes')) {
    const additionalCss = `
.point-notes{margin:8px 0 16px 20px;padding:0;display:grid;gap:10px}
.point-notes li{color:var(--ink2);line-height:1.65;font-size:.92rem}
.point-notes li strong{color:var(--ink)}
.quick-facts-box{background:#f8fafc;border:1px solid #e2e8f0;border-radius:12px;padding:14px 16px}
.warning-points li{color:#92400e}
.warning-points li strong{color:#78350f}
`;
    $('style').append(additionalCss);
  }

  return $.html();
}

async function main() {
  console.log(`Starting History Topic Generator [Model: ${MODEL}]`);
  const allPages = discoverHistoryPages(HISTORY_ROOT);
  console.log(`Found ${allPages.length} total history topic pages.`);

  const status = readStatus();

  // Filter pages
  let targets = allPages;
  if (requestedTopic) {
    const cleanReq = requestedTopic.replace(/\\/g, '/').replace(/\/index\.html$/, '');
    targets = allPages.filter((p) => p.topicDir.includes(cleanReq) || p.relPath.includes(cleanReq));
    if (targets.length === 0) {
      console.error(`Error: No topic matched '${requestedTopic}'`);
      process.exit(1);
    }
  } else if (!force && !allFlag) {
    // By default target placeholder pages
    targets = allPages.filter((p) => {
      const html = fs.readFileSync(p.fullPath, 'utf8');
      return isPlaceholderContent(html);
    });
  }

  if (requestedLimit > 0) {
    targets = targets.slice(0, requestedLimit);
  }

  console.log(`Targeting ${targets.length} pages for generation.`);

  if (dryRun) {
    console.log('DRY RUN: Targeted pages:');
    targets.forEach((t, idx) => console.log(`  [${idx + 1}] ${t.relPath}`));
    return;
  }

  let completed = 0;
  for (const page of targets) {
    console.log(`\n[${completed + 1}/${targets.length}] Processing: ${page.relPath}`);

    try {
      const originalHtml = fs.readFileSync(page.fullPath, 'utf8');
      const $ = cheerio.load(originalHtml);

      const title = $('h1').text().trim() || path.basename(page.topicDir);
      const kicker = $('.kicker').text().trim();
      const breadcrumb = $('.breadcrumb').text().replace(/\s+/g, ' ').trim();

      const metadata = {
        title,
        kicker,
        breadcrumb,
        relPath: page.relPath
      };

      console.log(`  Generating point-wise content for "${title}"...`);
      const prompt = buildPrompt(metadata);
      const data = await generateContentWithRetry(prompt);

      console.log(`  Received ${data.study_sections?.length || 0} study sections. Rendering HTML...`);
      const updatedHtml = renderHtml(originalHtml, data, metadata);

      fs.writeFileSync(page.fullPath, updatedHtml, 'utf8');
      console.log(`  ✓ Successfully updated: ${page.relPath}`);

      status[page.relPath] = {
        updatedAt: new Date().toISOString(),
        model: MODEL,
        status: 'completed'
      };
      writeStatus(status);

      completed++;

      if (gapMs > 0 && completed < targets.length) {
        await sleep(gapMs);
      }
    } catch (err) {
      console.error(`  ✗ Failed to process ${page.relPath}: ${err.message}`);
      status[page.relPath] = {
        updatedAt: new Date().toISOString(),
        model: MODEL,
        status: 'error',
        error: err.message
      };
      writeStatus(status);
    }
  }

  console.log(`\nFinished! Successfully generated and updated ${completed}/${targets.length} pages.`);
}

main().catch((err) => {
  console.error('Fatal error:', err);
  process.exit(1);
});
