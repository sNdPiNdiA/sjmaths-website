import fs from 'fs';
import path from 'path';
import dotenv from 'dotenv';
import { GoogleGenAI } from '@google/genai';
import { jsonrepair } from 'jsonrepair';

dotenv.config();

// 1. API Keys & Models
const API_KEYS = [
  process.env.GEMINI_API_KEY_1,
  process.env.GEMINI_API_KEY_2,
  process.env.GEMINI_API_KEY
].filter(Boolean);

if (API_KEYS.length === 0) {
  console.error('No GEMINI_API_KEY found in environment or .env');
  process.exit(1);
}

const MODELS = ['gemini-3.5-flash-lite', 'gemini-3.8-flash', 'gemini-2.5-flash'];
let currentKeyIdx = 0;

function getActiveConfig() {
  return {
    key: API_KEYS[currentKeyIdx % API_KEYS.length],
    models: MODELS,
    name: `KEY_${(currentKeyIdx % API_KEYS.length) + 1}`
  };
}

function rotateKey() {
  currentKeyIdx++;
  const active = getActiveConfig();
  console.log(`\n>>> [Key Rotation] Switched to ${active.name} <<<\n`);
  return active;
}

// 2. Load Topics Catalog
const catalogPath = path.join(process.cwd(), 'scripts', 'science_topics_catalog.json');
if (!fs.existsSync(catalogPath)) {
  console.error('Missing catalog file scripts/science_topics_catalog.json');
  process.exit(1);
}
const topics = JSON.parse(fs.readFileSync(catalogPath, 'utf8'));

// 3. Status Cache Tracker
const STATUS_FILE = path.join(process.cwd(), 'content-generation-status-upper-primary-science-mindmaps.json');
let statusTracker = {};
if (fs.existsSync(STATUS_FILE)) {
  try {
    statusTracker = JSON.parse(fs.readFileSync(STATUS_FILE, 'utf8'));
  } catch (e) {
    statusTracker = {};
  }
}

function saveStatusTracker() {
  fs.writeFileSync(STATUS_FILE, JSON.stringify(statusTracker, null, 2), 'utf8');
}

// 4. HTML Escaper
function esc(str) {
  if (!str) return '';
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
}

// 5. Prompt Builder
function buildMindmapPrompt(topic) {
  return `You are a premier National-level Senior Science Faculty, textbook author (NCERT & SCERT UP), and competitive examination coach for UP Upper Primary Teacher (Class 6-8, Super TET Junior Part 2C - Science).

Create an EXHAUSTIVE, COMPREHENSIVE, TOPPER-GRADE CONCEPT MINDMAP in STRICT JSON for:
Topic #${topic.num}: ${topic.titleEn} | ${topic.titleHi}
Directory Slug: ${topic.slug}
Syllabus Focus: ${topic.focusEn} / ${topic.focusHi}
Key Core Sections: ${topic.cardHeadings.join('; ')}

CRITICAL REQUIREMENT:
The mindmap must cover EVERY SINGLE CONCEPT, LAW, FORMULA, EXPERIMENT, CLASSIFICATION, AND EXAM TRAP related to this topic from NCERT Classes 6-8 and UP SCERT 'Hamara Vigyan' curricula. DO NOT MISS ANY CONCEPT.

Structure the mindmap into 5 or 6 logical branches:
1. Fundamental Principles, Laws & Core Definitions (मूल सिद्धांत, नियम एवं मौलिक परिभाषाएं)
2. Classifications, Taxonomies & Structural Mechanisms (वर्गीकरण, श्रेणियाँ एवं संरचनात्मक तंत्र)
3. Formulas, Units, Equations & Scientific Calculations (सूत्र, मात्रक, रासायनिक समीकरण व गणनाएं)
4. Laboratory Techniques, Experiments & Diagnostic Tests (प्रयोगशाला विधियां, प्रयोग एवं परीक्षण)
5. Practical Applications, Daily Life Utilities & Technology (दैनिक जीवन में उपयोगिता एवं आधुनिक तकनीक)
6. Scientific Exceptions, Distractor Traps & High-Yield Facts (वैज्ञानिक अपवाद, परीक्षा के जाल एवं त्वरित तथ्य)

Each branch MUST contain 5 to 8 detailed, content-rich subnodes.
Each subnode must provide specific scientific depth (formulas, SI units, scientific names, chemical equations, numerical shortcuts, key examples).
Both English ('en') and Hindi ('hi') translations must be fluent, authoritative, and scientifically accurate.

OUTPUT SCHEMA:
Return ONLY valid JSON matching this exact structure:
{
  "root_en": "Concise Core Topic Title in English",
  "root_hi": "सटीक मुख्य विषय शीर्षक हिंदी में",
  "branches": [
    {
      "icon": "fa-flask", // pick appropriate FontAwesome 6 icon (e.g. fa-atom, fa-flask, fa-bolt, fa-dna, fa-microscope, fa-leaf, fa-fire, fa-calculator, fa-lightbulb, fa-triangle-exclamation)
      "title_en": "Branch 1 Title in English",
      "title_hi": "शाखा 1 का शीर्षक हिंदी में",
      "subnodes": [
        {
          "en": "Detailed scientific statement with laws/formulas/examples",
          "hi": "विस्तृत वैज्ञानिक तथ्य/नियम/सूत्र/उदाहरण सहित विवरण"
        }
      ]
    }
  ]
}`;
}

// 6. Gemini Invocation with Fallback & Rotation
async function generateMindmapData(topic) {
  const prompt = buildMindmapPrompt(topic);
  let lastErr = null;

  for (let attempt = 0; attempt < 8; attempt++) {
    const config = getActiveConfig();
    const ai = new GoogleGenAI({ apiKey: config.key });

    for (const model of config.models) {
      try {
        console.log(`    [Attempt ${attempt + 1}] Requesting Mindmap [${config.name} | ${model}] for: ${topic.slug}`);
        const response = await ai.models.generateContent({
          model,
          contents: prompt,
          config: {
            responseMimeType: 'application/json',
            temperature: 0.25
          }
        });

        const rawText = response.text;
        if (!rawText) throw new Error('Empty response received from model');

        let parsed;
        try {
          parsed = JSON.parse(rawText);
        } catch (e) {
          const repaired = jsonrepair(rawText);
          parsed = JSON.parse(repaired);
        }

        if (!parsed.branches || parsed.branches.length < 4) {
          throw new Error(`Incomplete branches count: ${parsed.branches ? parsed.branches.length : 0}`);
        }

        return parsed;
      } catch (err) {
        lastErr = err;
        console.warn(`    [Warning] ${config.name}/${model} failed on ${topic.slug}: ${err.message}`);
        await new Promise(r => setTimeout(r, 1200));
      }
    }

    rotateKey();
    await new Promise(r => setTimeout(r, 1500));
  }

  throw new Error(`Exhausted retries for ${topic.slug}: ${lastErr ? lastErr.message : 'Unknown'}`);
}

// 7. Mindmap HTML Component Builder
function renderMindmapHtml(topic, data) {
  let branchesHtml = '';
  
  data.branches.forEach((b, bIdx) => {
    let subnodesHtml = '';
    (b.subnodes || []).forEach(sub => {
      subnodesHtml += `
                            <li class="mindmap-subnode-item">
                                <i class="fas fa-angle-right" style="color: var(--brand-emerald); margin-right: 0.35rem;"></i>
                                <span class="lang-en">${esc(sub.en)}</span>
                                <span class="lang-hi">${esc(sub.hi)}</span>
                            </li>`;
    });

    const iconClass = b.icon ? (b.icon.startsWith('fa-') ? b.icon : `fa-${b.icon}`) : 'fa-layer-group';

    branchesHtml += `
                    <div class="mindmap-branch-card">
                        <div class="mindmap-branch-title">
                            <i class="fas ${iconClass}" style="color: var(--brand-emerald);"></i>
                            <span class="lang-en">${esc(b.title_en)}</span>
                            <span class="lang-hi">${esc(b.title_hi)}</span>
                        </div>
                        <ul class="mindmap-subnodes">
                            ${subnodesHtml}
                        </ul>
                    </div>`;
  });

  return `
        <!-- Mindmap Component (Comprehensive Concept Flow) -->
        <div class="prep-card">
            <h2>
                <i class="fas fa-sitemap" style="color: var(--brand-emerald);"></i>
                <span class="lang-en">Comprehensive Concept Mindmap</span>
                <span class="lang-hi">माइंडमैप (समग्र संकल्पना प्रवाह)</span>
            </h2>
            <div class="mindmap-wrapper">
                <div class="mindmap-root-node">
                    <span class="mindmap-root-badge">
                        <i class="fas fa-atom"></i>
                        <span class="lang-en">${esc(data.root_en || topic.titleEn)}</span>
                        <span class="lang-hi">${esc(data.root_hi || topic.titleHi)}</span>
                    </span>
                </div>
                <div class="mindmap-branches">
                    ${branchesHtml}
                </div>
            </div>
        </div>
`;
}

// 8. Insertion Handler
function insertMindmapIntoTopic(topic, mindmapHtml) {
  const filePath = path.join(process.cwd(), 'up-upper-primary-teacher', 'science', topic.slug, 'index.html');
  if (!fs.existsSync(filePath)) {
    throw new Error(`File not found: ${filePath}`);
  }

  let html = fs.readFileSync(filePath, 'utf8');

  // Check if mindmap is already present
  if (html.includes('<!-- Mindmap Component')) {
    // Replace existing mindmap
    html = html.replace(/<!-- Mindmap Component[\s\S]*?<\/div>\s*<\/div>\s*<\/div>\s*<\/div>/, mindmapHtml.trim());
  } else {
    // Insert before the first prep-card inside tab-concepts
    const tabConceptsIdx = html.indexOf('id="tab-concepts"');
    if (tabConceptsIdx === -1) {
      throw new Error(`Cannot find id="tab-concepts" in ${topic.slug}`);
    }

    const firstPrepCardIdx = html.indexOf('<div class="prep-card">', tabConceptsIdx);
    if (firstPrepCardIdx === -1) {
      throw new Error(`Cannot find <div class="prep-card"> after tab-concepts in ${topic.slug}`);
    }

    html = html.slice(0, firstPrepCardIdx) + mindmapHtml + '\n        ' + html.slice(firstPrepCardIdx);
  }

  // Ensure CSS reference has cache-buster
  if (!html.includes('up-upper-primary-topic.min.css?v=20261002_02')) {
    html = html.replace(
      /\/assets\/css\/up-upper-primary-topic\.min\.css(\?v=[a-zA-Z0-9_\-]+)?/g,
      '/assets/css/up-upper-primary-topic.min.css?v=20261002_02'
    );
  }

  fs.writeFileSync(filePath, html, 'utf8');
}

// 9. Batch Worker Runner
async function processTopic(topic, workerId, total) {
  const cacheKey = topic.slug;
  if (statusTracker[cacheKey] && statusTracker[cacheKey].status === 'SUCCESS' && !process.argv.includes('--force')) {
    console.log(`[Worker ${workerId}][${topic.num}/${total}] Skipping already generated: ${topic.slug}`);
    return;
  }

  console.log(`[Worker ${workerId}][${topic.num}/${total}] Generating Mindmap for: ${topic.slug} (${topic.titleEn})`);
  
  try {
    const data = await generateMindmapData(topic);
    const mindmapHtml = renderMindmapHtml(topic, data);
    insertMindmapIntoTopic(topic, mindmapHtml);

    statusTracker[cacheKey] = {
      status: 'SUCCESS',
      timestamp: new Date().toISOString(),
      branchesCount: data.branches.length,
      totalSubnodes: data.branches.reduce((acc, b) => acc + (b.subnodes || []).length, 0)
    };
    saveStatusTracker();

    console.log(`[Worker ${workerId}]  ✓ SUCCESS: Inserted Mindmap into ${topic.slug} (${statusTracker[cacheKey].branchesCount} branches, ${statusTracker[cacheKey].totalSubnodes} subnodes)`);
  } catch (err) {
    console.error(`[Worker ${workerId}]  ✗ FAILED on ${topic.slug}: ${err.message}`);
    statusTracker[cacheKey] = {
      status: 'ERROR',
      error: err.message,
      timestamp: new Date().toISOString()
    };
    saveStatusTracker();
  }
}

// 10. Main Concurrent Runner
async function main() {
  console.log(`================================================================`);
  console.log(`UP Upper Primary Science: Comprehensive Concept Mindmap Generator`);
  console.log(`Target: 34 Official Science Topic Pages`);
  console.log(`Available Keys: ${API_KEYS.length}`);
  console.log(`================================================================\n`);

  const concurrencyArgIdx = process.argv.indexOf('--concurrency');
  const concurrency = concurrencyArgIdx !== -1 ? parseInt(process.argv[concurrencyArgIdx + 1], 10) : 3;

  const queue = [...topics];
  const workers = [];

  for (let i = 0; i < concurrency; i++) {
    workers.push((async (wId) => {
      while (queue.length > 0) {
        const item = queue.shift();
        if (!item) break;
        await processTopic(item, wId + 1, topics.length);
      }
    })(i));
  }

  await Promise.all(workers);

  const successCount = Object.values(statusTracker).filter(s => s.status === 'SUCCESS').length;
  console.log(`\n================================================================`);
  console.log(`Finished processing mindmaps.`);
  console.log(`Success: ${successCount} / ${topics.length}`);
  console.log(`================================================================`);
}

main().catch(console.error);
