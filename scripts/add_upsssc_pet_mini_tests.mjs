#!/usr/bin/env node
/**
 * Add 30 High Quality Bilingual Questions in Tab 4 (3-Level Mini Test) for UPSSSC PET Topics.
 *
 * Uses Gemini API (gemini-3.5-flash-lite) to generate exam-standard, curriculum-aligned
 * timed mini-test questions split into Easy (10), Medium (10), and Hard (10) levels.
 *
 * Usage:
 *   node scripts/add_upsssc_pet_mini_tests.mjs
 *   node scripts/add_upsssc_pet_mini_tests.mjs <dir1> <dir2> ...
 *   node scripts/add_upsssc_pet_mini_tests.mjs --topic awards-winners --limit 1
 *   node scripts/add_upsssc_pet_mini_tests.mjs --dir geography --limit 2
 *   node scripts/add_upsssc_pet_mini_tests.mjs --dry-run
 *   node scripts/add_upsssc_pet_mini_tests.mjs --force
 */

import fs from 'node:fs';
import path from 'node:path';
import 'dotenv/config';
import { GoogleGenAI } from '@google/genai';
import { jsonrepair } from 'jsonrepair';

const ROOT_DIR = process.cwd();
const STATUS_FILE = path.join(ROOT_DIR, 'upsssc-pet-test-status.json');

const DEFAULT_DIRS = [
  'upsssc-pet/general-awareness',
  'upsssc-pet/geography',
  'upsssc-pet/hindi',
  'upsssc-pet/history',
  'upsssc-pet/polity',
  'upsssc-pet/science'
];

// CLI Arguments parsing
function parseCliArgs(args) {
  const flags = {};
  const positionals = [];
  for (let i = 0; i < args.length; i++) {
    const arg = args[i];
    if (arg.startsWith('--')) {
      if (arg.includes('=')) {
        const [k, ...v] = arg.slice(2).split('=');
        flags[k] = v.join('=');
      } else {
        const next = args[i + 1];
        if (next !== undefined && !next.startsWith('--')) {
          flags[arg.slice(2)] = next;
          i++;
        } else {
          flags[arg.slice(2)] = true;
        }
      }
    } else {
      positionals.push(arg);
    }
  }
  return { flags, positionals };
}

const { flags, positionals: positionalArgs } = parseCliArgs(process.argv.slice(2));

const TARGET_MODEL = flags.model || process.env.GEMINI_MODEL || 'gemini-3.5-flash-lite';
const LIMIT = flags.limit ? parseInt(flags.limit, 10) : 0;
const TOPIC_FILTER = flags.topic || null;
const DIR_FILTER = flags.dir || null;
const FORCE = Boolean(flags.force);
const DRY_RUN = Boolean(flags['dry-run']);
const GAP_MS = (parseInt(flags.gap || '1', 10)) * 1000;
const MAX_ATTEMPTS = parseInt(flags.attempts || '3', 10);

// API Keys setup with rotation
const apiKeys = [
  process.env.GEMINI_API_KEY,
  process.env.GEMINI_API_KEY_1,
  process.env.GEMINI_API_KEY_2,
  process.env.GOOGLE_API_KEY
].filter(Boolean);

if (apiKeys.length === 0) {
  console.error('❌ Error: No Gemini API Key found in .env (GEMINI_API_KEY, GEMINI_API_KEY_1, or GOOGLE_API_KEY)');
  process.exit(1);
}

let currentKeyIndex = 0;
function getGenAIClient() {
  const apiKey = apiKeys[currentKeyIndex % apiKeys.length];
  return new GoogleGenAI({ apiKey });
}

function rotateApiKey() {
  if (apiKeys.length > 1) {
    currentKeyIndex = (currentKeyIndex + 1) % apiKeys.length;
    console.log(`🔄 Rotated to Gemini API key #${currentKeyIndex + 1}`);
  }
}

// Read status log
function readStatus() {
  if (fs.existsSync(STATUS_FILE)) {
    try {
      return JSON.parse(fs.readFileSync(STATUS_FILE, 'utf8'));
    } catch {
      return {};
    }
  }
  return {};
}

function writeStatus(status) {
  try {
    fs.writeFileSync(STATUS_FILE, JSON.stringify(status, null, 2), 'utf8');
  } catch (err) {
    console.warn('Warning: Could not save status file:', err.message);
  }
}

// Recursively find all topic index.html files
function findTopicPages(dirs) {
  const pages = [];
  dirs.forEach(target => {
    const resolvedPath = path.isAbsolute(target) ? target : path.join(ROOT_DIR, target);
    if (!fs.existsSync(resolvedPath)) {
      console.warn(`⚠️ Path does not exist: ${resolvedPath}`);
      return;
    }

    const stat = fs.statSync(resolvedPath);
    if (stat.isFile() && resolvedPath.endsWith('index.html')) {
      pages.push(resolvedPath);
      return;
    }

    if (stat.isDirectory()) {
      const walk = (dir) => {
        const files = fs.readdirSync(dir);
        for (const file of files) {
          const fullPath = path.join(dir, file);
          const fStat = fs.statSync(fullPath);
          if (fStat.isDirectory()) {
            walk(fullPath);
          } else if (file === 'index.html') {
            try {
              const headSnippet = fs.readFileSync(fullPath, 'utf8');
              if (headSnippet.includes('id="upsc-page-data"')) {
                pages.push(fullPath);
              }
            } catch {
              // ignore
            }
          }
        }
      };
      walk(resolvedPath);
    }
  });

  return pages;
}

// Clean and extract context from existing concepts
function extractTopicContext(pageData) {
  const parts = [];
  if (pageData.concepts?.sections) {
    for (const sec of pageData.concepts.sections) {
      if (sec.title?.en) parts.push(`Section: ${sec.title.en}`);
      if (sec.type === 'table' && sec.rows) {
        sec.rows.slice(0, 10).forEach(r => {
          const enCells = r.map(c => c.en || '').filter(Boolean).join(' - ');
          if (enCells) parts.push(enCells);
        });
      }
      if (sec.type === 'list' && sec.items) {
        sec.items.slice(0, 10).forEach(item => {
          if (item.term?.en) parts.push(`${item.term.en}: ${item.definition?.en || ''}`);
        });
      }
    }
  }
  if (pageData.concepts?.keyTakeaways) {
    if (Array.isArray(pageData.concepts.keyTakeaways)) {
      parts.push('Key points: ' + pageData.concepts.keyTakeaways.map(k => k.en || k).slice(0, 8).join('; '));
    } else if (pageData.concepts.keyTakeaways.en) {
      parts.push('Key points: ' + pageData.concepts.keyTakeaways.en);
    }
  }
  return parts.slice(0, 25).join('\n');
}

// Construct generation prompt for 30 high-quality Mini Test questions
function buildPrompt(topicInfo) {
  return `You are a premier senior examination question setter and test designer for the Uttar Pradesh Subordinate Services Selection Commission (UPSSSC) Preliminary Eligibility Test (PET).

Topic Information:
- Subject: ${topicInfo.subject}
- Topic Name: ${topicInfo.topicName}
- Hindi Name: ${topicInfo.hindiName || topicInfo.topicName}
${topicInfo.context ? `\nCore Syllabus Reference Facts:\n${topicInfo.context}` : ''}

TASK:
Generate exactly 30 authentic, exam-standard Multiple Choice Questions (MCQs) for this topic to be used as a 3-Level Timed Mini Test for UPSSSC PET.

REQUIREMENTS:
1. Divide questions into 3 difficulty tiers with exactly 10 questions each:
   - "easy": 10 questions (IDs 1 to 10) - Rapid recall, direct factual questions, basic definitions, key dates, names, locations, and essential baseline questions suitable for Level 1 test.
   - "medium": 10 questions (IDs 11 to 20) - Moderate complexity questions, cause and effect, chronological sequences, multi-statement evaluation, standard UPSSSC PET exam-grade test questions.
   - "hard": 10 questions (IDs 21 to 30) - Challenging analytical questions, trap options, subtle exceptions, assertions, and questions with UP state-level relevance where applicable.

2. BILINGUAL STRICT REQUIREMENT:
   Every single question, all 4 options, and the explanation MUST be in both English ("en") and authentic Hindi ("hi") using standardized Hindi terminology (official UP exam Hindi).

3. MCQ FORMAT:
   - Exactly 4 options labeled "A", "B", "C", and "D".
   - Plausible, high-quality distractors typical of UPSSSC competitive exams.
   - "correctAnswer" MUST be exactly one of "A", "B", "C", or "D".
   - "explanation" must be concise and educational, highlighting key revision facts and why the option is correct.

OUTPUT FORMAT:
Return strictly a valid JSON object matching this schema without any preamble, markdown code blocks, or extra text:

{
  "easy": [
    {
      "id": 1,
      "question": {
        "en": "...",
        "hi": "..."
      },
      "options": [
        { "letter": "A", "text": { "en": "...", "hi": "..." } },
        { "letter": "B", "text": { "en": "...", "hi": "..." } },
        { "letter": "C", "text": { "en": "...", "hi": "..." } },
        { "letter": "D", "text": { "en": "...", "hi": "..." } }
      ],
      "correctAnswer": "A",
      "explanation": {
        "en": "...",
        "hi": "..."
      }
    }
  ],
  "medium": [
    ... 10 questions with IDs 11 to 20 ...
  ],
  "hard": [
    ... 10 questions with IDs 21 to 30 ...
  ]
}`;
}

// Generate with Gemini API
async function generateTestWithGemini(topicInfo) {
  const prompt = buildPrompt(topicInfo);
  let lastError = null;

  for (let attempt = 1; attempt <= MAX_ATTEMPTS; attempt++) {
    try {
      const ai = getGenAIClient();
      const response = await ai.models.generateContent({
        model: TARGET_MODEL,
        contents: prompt,
        config: {
          temperature: 0.25,
          responseMimeType: 'application/json'
        }
      });

      const text = response?.text;
      if (!text) throw new Error('Empty response received from Gemini API');

      let parsed;
      try {
        parsed = JSON.parse(text);
      } catch (jsonErr) {
        parsed = JSON.parse(jsonrepair(text));
      }

      // Validate structure
      const easy = Array.isArray(parsed.easy) ? parsed.easy : [];
      const medium = Array.isArray(parsed.medium) ? parsed.medium : [];
      const hard = Array.isArray(parsed.hard) ? parsed.hard : [];

      if (easy.length === 0 && medium.length === 0 && hard.length === 0) {
        throw new Error('Received JSON does not contain easy/medium/hard question arrays');
      }

      // Re-index questions cleanly from 1 to 30
      let curId = 1;
      const normalizeGroup = (group) => group.map(q => {
        const item = {
          id: curId++,
          question: {
            en: q.question?.en || String(q.question || ''),
            hi: q.question?.hi || q.question?.en || String(q.question || '')
          },
          options: (q.options || []).map((opt, i) => ({
            letter: opt.letter || ['A', 'B', 'C', 'D'][i] || 'A',
            text: {
              en: opt.text?.en || String(opt.text || ''),
              hi: opt.text?.hi || opt.text?.en || String(opt.text || '')
            }
          })),
          correctAnswer: (q.correctAnswer || 'A').toUpperCase().trim().charAt(0),
          explanation: {
            en: q.explanation?.en || String(q.explanation || ''),
            hi: q.explanation?.hi || q.explanation?.en || String(q.explanation || '')
          }
        };
        return item;
      });

      return {
        levels: {
          easy: normalizeGroup(easy),
          medium: normalizeGroup(medium),
          hard: normalizeGroup(hard)
        }
      };
    } catch (err) {
      lastError = err;
      console.warn(`  ⚠️ Attempt ${attempt}/${MAX_ATTEMPTS} failed for ${topicInfo.topicName}: ${err.message}`);
      rotateApiKey();
      if (attempt < MAX_ATTEMPTS) {
        const backoff = attempt * 3000;
        await new Promise(r => setTimeout(r, backoff));
      }
    }
  }

  throw lastError;
}

// Process a single topic HTML file
async function processTopicPage(filePath, statusLog) {
  const relPath = path.relative(ROOT_DIR, filePath).replace(/\\/g, '/');
  const fileContent = fs.readFileSync(filePath, 'utf8');

  // Match the page data script
  const scriptRegex = /<script\s+id="upsc-page-data"\s+type="application\/json">([\s\S]*?)<\/script>/;
  const match = fileContent.match(scriptRegex);

  if (!match) {
    console.log(`⏭️  Skipping ${relPath} (no #upsc-page-data script found)`);
    return false;
  }

  let pageData;
  try {
    pageData = JSON.parse(match[1]);
  } catch (err) {
    try {
      pageData = JSON.parse(jsonrepair(match[1]));
    } catch (repairErr) {
      console.error(`❌ Could not parse JSON in ${relPath}: ${err.message}`);
      return false;
    }
  }

  // Check if test is already populated with levels
  const existingTest = pageData.test;
  const hasExistingLevels = existingTest && existingTest.levels &&
    Object.values(existingTest.levels).some(arr => Array.isArray(arr) && arr.length > 0);

  if (hasExistingLevels && !FORCE) {
    const totalQ = Object.values(existingTest.levels).reduce((sum, a) => sum + (Array.isArray(a) ? a.length : 0), 0);
    console.log(`✅ [Already Populated] ${pageData.topicName || relPath} (${totalQ} test questions)`);
    return false;
  }

  console.log(`\n📝 Generating 3-Level Mini Test for: ${pageData.topicName} (${pageData.hindiName || ''}) [${relPath}]`);

  const topicInfo = {
    topicName: pageData.topicName || path.basename(path.dirname(filePath)),
    hindiName: pageData.hindiName || '',
    subject: pageData.subject || 'UPSSSC PET',
    context: extractTopicContext(pageData)
  };

  if (DRY_RUN) {
    console.log(`   [DRY-RUN] Would generate Mini Test for "${topicInfo.topicName}"`);
    return true;
  }

  const testData = await generateTestWithGemini(topicInfo);
  const totalCount = Object.values(testData.levels).reduce((s, a) => s + a.length, 0);

  // Update pageData
  pageData.test = testData;
  if (Array.isArray(pageData.tabs) && !pageData.tabs.includes('test')) {
    pageData.tabs.push('test');
  }

  // Update index.html safely without dollar sign interpolation
  const updatedScriptTag = `<script id="upsc-page-data" type="application/json">${JSON.stringify(pageData, null, 2)}</script>`;
  const updatedHtml = fileContent.replace(scriptRegex, () => updatedScriptTag);
  fs.writeFileSync(filePath, updatedHtml, 'utf8');

  // Also write tabs/test.json
  try {
    const tabsDir = path.join(path.dirname(filePath), 'tabs');
    if (!fs.existsSync(tabsDir)) fs.mkdirSync(tabsDir, { recursive: true });
    fs.writeFileSync(path.join(tabsDir, 'test.json'), JSON.stringify(testData, null, 2), 'utf8');
  } catch (tabErr) {
    console.warn(`   Could not write tabs/test.json: ${tabErr.message}`);
  }

  console.log(`   🎉 Successfully added ${totalCount} Mini Test Questions (10 Easy, 10 Medium, 10 Hard) to ${relPath}`);

  // Update status log
  statusLog[relPath] = {
    topicName: topicInfo.topicName,
    questionCount: totalCount,
    updatedAt: new Date().toISOString(),
    model: TARGET_MODEL
  };
  writeStatus(statusLog);

  return true;
}

// Main execution flow
async function main() {
  console.log('='.repeat(70));
  console.log('🎯 UPSSSC PET 3-Level Mini Test Generator (Tab 4)');
  console.log(`🤖 Model: ${TARGET_MODEL}`);
  console.log(`🔑 Available API Keys: ${apiKeys.length}`);
  if (DRY_RUN) console.log('🔍 Mode: DRY-RUN (no files will be written)');
  if (FORCE) console.log('⚡ Force: Overwriting existing questions');
  console.log('='.repeat(70));

  const targetDirs = positionalArgs.length > 0 ? positionalArgs : DEFAULT_DIRS;
  console.log(`\nScanning directories:\n${targetDirs.map(d => ` - ${d}`).join('\n')}\n`);

  let topicPages = findTopicPages(targetDirs);

  // Apply filters
  if (DIR_FILTER) {
    topicPages = topicPages.filter(p => p.toLowerCase().includes(DIR_FILTER.toLowerCase()));
  }
  if (TOPIC_FILTER) {
    topicPages = topicPages.filter(p => p.toLowerCase().includes(TOPIC_FILTER.toLowerCase()));
  }

  console.log(`Found ${topicPages.length} eligible topic pages.`);

  if (LIMIT > 0) {
    topicPages = topicPages.slice(0, LIMIT);
    console.log(`Limiting to first ${LIMIT} topic(s).`);
  }

  const statusLog = readStatus();
  let generatedCount = 0;
  let skippedCount = 0;
  let errorCount = 0;

  for (let i = 0; i < topicPages.length; i++) {
    const pagePath = topicPages[i];
    console.log(`\n[${i + 1}/${topicPages.length}] Processing...`);
    try {
      const generated = await processTopicPage(pagePath, statusLog);
      if (generated) {
        generatedCount++;
        if (GAP_MS > 0 && i < topicPages.length - 1) {
          console.log(`⏳ Waiting ${GAP_MS / 1000}s before next topic...`);
          await new Promise(r => setTimeout(r, GAP_MS));
        }
      } else {
        skippedCount++;
      }
    } catch (err) {
      errorCount++;
      console.error(`❌ Failed to process ${pagePath}: ${err.message}`);
    }
  }

  console.log('\n' + '='.repeat(70));
  console.log('🏁 Batch Mini Test Generation Complete');
  console.log(`✅ Newly Generated: ${generatedCount}`);
  console.log(`⏭️  Already Populated / Skipped: ${skippedCount}`);
  console.log(`❌ Errors: ${errorCount}`);
  console.log('='.repeat(70));
}

main().catch(err => {
  console.error('Fatal execution error:', err);
  process.exit(1);
});
