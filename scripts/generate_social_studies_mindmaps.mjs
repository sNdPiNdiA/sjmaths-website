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

const MODELS = ['gemini-2.5-flash', 'gemini-3.5-flash-lite', 'gemini-3.8-flash'];
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
const catalogPath = path.join(process.cwd(), 'scripts', 'social_studies_topics_catalog.json');
if (!fs.existsSync(catalogPath)) {
  console.error('Missing catalog file scripts/social_studies_topics_catalog.json');
  process.exit(1);
}
const topics = JSON.parse(fs.readFileSync(catalogPath, 'utf8'));

// 3. Status Tracker
const STATUS_FILE = path.join(process.cwd(), 'content-generation-status-upper-primary-social-studies-mindmaps.json');
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

// 5. Prompt Builder tailored for Social Studies (History, Geography, Civics, UP Special)
function buildMindmapPrompt(topic) {
  const headings = topic.cardHeadings.map(h => `${h.en} (${h.hi})`).join('; ');
  const samplePoints = topic.samplePointsEn.slice(0, 5).join('; ');

  return `You are a premier National-level Senior Social Studies Faculty, textbook author (NCERT & SCERT UP), and competitive examination coach for UP Upper Primary Teacher (Class 6-8, Super TET Junior Part 2B - Social Studies / सामाजिक अध्ययन).

Create an EXHAUSTIVE, COMPREHENSIVE, TOPPER-GRADE CONCEPT MINDMAP in STRICT JSON for:
Topic Slug: ${topic.slug}
Topic Title: ${topic.enTitle} | ${topic.hiTitle}
Lead Description: ${topic.leadEn || ''} / ${topic.leadHi || ''}
Key Core Sections in Study Notes: ${headings || 'Comprehensive Curriculum'}
Sample Reference Points: ${samplePoints || 'Standard UP SCERT Curriculum'}

CRITICAL REQUIREMENT:
The mindmap must cover EVERY SINGLE CONCEPT, HISTORICAL TIMELINE/EVENT, GEOGRAPHICAL MECHANISM/LANDFORM/RESOURCE, CONSTITUTIONAL ARTICLE/POLITY STRUCTURE, UP SPECIAL FACT, AND EXAM TRAP related to this topic from NCERT Classes 6-8 and UP SCERT 'Hamari Virasat' (History), 'Prithvi aur Humara Jeevan' (Geography), and 'Hamara Samvidhan evam Loktantra' (Civics/Polity) curricula. DO NOT MISS ANY CONCEPT.

Structure the mindmap into 5 or 6 logical, content-dense branches tailored to the nature of the topic:
- For History: Chronology/Timeline, Administrative Systems, Socio-Economic/Culture, Key Figures/Treaties/Sources, Causes & Consequences, Exam Traps/Mnemonics.
- For Geography: Core Physical Concepts/Definitions, Classifications/Spatial Zones, Scientific/Geomorphic Processes, Economic & Resource Distribution, Environmental Impact/Conservation, Map Pointers/Exam Traps.
- For Civics/Polity: Constitutional Articles/Provisions, Institutional Setup & Powers, Democratic Processes/Elections, Rights/Duties/Social Justice, Key Amendments/Judicial Rulings, High-Yield Traps.
- For UP Special: Location/Administrative Divisions, Physical/River/Soil Systems, Agriculture/Irrigation/Minerals, Forests/Wildlife/Sanctuaries, Demography/Schemes, UP GK Exam Traps.

Each branch MUST contain 4 to 6 detailed, specific, content-rich subnodes.
Each subnode must provide specific depth: exact years, battle dates, constitutional article numbers, soil types, river tributaries, percentages, dynasties, authors of texts, commission names, or mnemonic shortcuts.
Both English ('en') and Hindi ('hi') translations must be fluent, authoritative, and examination-grade.

OUTPUT SCHEMA:
Return ONLY valid JSON matching this exact structure:
{
  "root_en": "${topic.enTitle}",
  "root_hi": "${topic.hiTitle}",
  "icon": "fa-landmark", // pick relevant FontAwesome 6 icon like fa-landmark, fa-scroll, fa-crown, fa-globe-asia, fa-compass, fa-mountain, fa-water, fa-seedling, fa-balance-scale, fa-vote-yea, fa-shield-halved, fa-map-location-dot, fa-tree, fa-handshake
  "branches": [
    {
      "icon": "fa-scroll",
      "title_en": "Branch Title in English",
      "title_hi": "शाखा का शीर्षक हिंदी में",
      "subnodes": [
        {
          "en": "Detailed historical/geographical/civic fact with dates/articles/terms",
          "hi": "विस्तृत ऐतिहासिक/भौगोलिक/नागरिक तथ्य तिथियों/अनुच्छेदों/पारिभाषिक शब्दों सहित"
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
        await new Promise(r => setTimeout(r, 1000));
      }
    }

    rotateKey();
    await new Promise(r => setTimeout(r, 1200));
  }

  throw new Error(`Exhausted retries for ${topic.slug}: ${lastErr ? lastErr.message : 'Unknown'}`);
}

// 7. Mindmap HTML Component Builder
function renderMindmapHtml(topic, data) {
  let branchesHtml = '';
  
  data.branches.forEach((b) => {
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

  const rootIcon = data.icon ? (data.icon.startsWith('fa-') ? data.icon : `fa-${data.icon}`) : 'fa-landmark';

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
                        <i class="fas ${rootIcon}"></i>
                        <span class="lang-en">${esc(data.root_en || topic.enTitle)}</span>
                        <span class="lang-hi">${esc(data.root_hi || topic.hiTitle)}</span>
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
  const filePath = path.join(process.cwd(), 'up-upper-primary-teacher', 'social-studies', topic.slug, 'index.html');
  if (!fs.existsSync(filePath)) {
    throw new Error(`File not found: ${filePath}`);
  }

  let html = fs.readFileSync(filePath, 'utf8');

  // Check if mindmap is already present
  if (html.includes('<!-- Mindmap Component')) {
    // Replace existing mindmap
    html = html.replace(/<!-- Mindmap Component[\s\S]*?<\/div>\s*<\/div>\s*<\/div>\s*<\/div>/, mindmapHtml.trim());
  } else {
    // 1. Try finding first prep-card inside tab-concepts
    let targetIdx = -1;
    const tabConceptsIdx = html.indexOf('id="tab-concepts"');
    if (tabConceptsIdx !== -1) {
      targetIdx = html.indexOf('<div class="prep-card">', tabConceptsIdx);
    }
    
    // 2. If not found or no tab-concepts, look after study-tabs-strip
    if (targetIdx === -1) {
      const tabsStripIdx = html.indexOf('class="study-tabs-strip"');
      if (tabsStripIdx !== -1) {
        targetIdx = html.indexOf('<div class="prep-card">', tabsStripIdx);
      }
    }

    // 3. Fallback: look after completion-card
    if (targetIdx === -1) {
      const compCardIdx = html.indexOf('class="completion-card"');
      if (compCardIdx !== -1) {
        targetIdx = html.indexOf('<div class="prep-card">', compCardIdx);
      }
    }

    // 4. Ultimate fallback: first prep-card in document
    if (targetIdx === -1) {
      targetIdx = html.indexOf('<div class="prep-card">');
    }

    if (targetIdx === -1) {
      throw new Error(`Cannot find insertion point (<div class="prep-card">) in ${topic.slug}`);
    }

    html = html.slice(0, targetIdx) + mindmapHtml + '\n        ' + html.slice(targetIdx);
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

// 9. Worker Processor
async function processTopic(topic, workerId, idx, total) {
  const cacheKey = topic.slug;
  if (statusTracker[cacheKey] && statusTracker[cacheKey].status === 'SUCCESS' && !process.argv.includes('--force')) {
    return;
  }

  console.log(`[Worker ${workerId}][${idx + 1}/${total}] Generating Mindmap for: ${topic.slug} (${topic.enTitle})`);
  
  try {
    const data = await generateMindmapData(topic);
    const mindmapHtml = renderMindmapHtml(topic, data);
    insertMindmapIntoTopic(topic, mindmapHtml);

    statusTracker[cacheKey] = {
      status: 'SUCCESS',
      timestamp: new Date().toISOString(),
      branchesCount: data.branches.length,
      subnodesCount: data.branches.reduce((acc, b) => acc + (b.subnodes || []).length, 0)
    };
    saveStatusTracker();
    console.log(`  [Worker ${workerId}] SUCCESS: ${topic.slug} (${data.branches.length} branches, ${statusTracker[cacheKey].subnodesCount} subnodes)`);
  } catch (err) {
    console.error(`  [Worker ${workerId}] ERROR on ${topic.slug}: ${err.message}`);
    statusTracker[cacheKey] = {
      status: 'FAILED',
      timestamp: new Date().toISOString(),
      error: err.message
    };
    saveStatusTracker();
  }
}

// 10. Main Concurrent Runner
async function main() {
  console.log('================================================================');
  console.log(`UP Upper Primary Social Studies: Mindmap Generator (${topics.length} Topics)`);
  console.log(`Active API Keys: ${API_KEYS.length} keys loaded`);
  console.log('================================================================\n');

  const pending = topics.map((t, idx) => ({ topic: t, idx }))
    .filter(({ topic }) => {
      if (process.argv.includes('--force')) return true;
      return !(statusTracker[topic.slug] && statusTracker[topic.slug].status === 'SUCCESS');
    });

  console.log(`Total Topics: ${topics.length} | Pending: ${pending.length}`);

  if (pending.length === 0) {
    console.log('All topics already successfully generated! Use --force to regenerate.');
    return;
  }

  const CONCURRENCY = 4;
  let cursor = 0;

  async function worker(workerId) {
    while (cursor < pending.length) {
      const current = pending[cursor++];
      if (!current) break;
      await processTopic(current.topic, workerId, current.idx, topics.length);
    }
  }

  const workers = [];
  for (let i = 1; i <= CONCURRENCY; i++) {
    workers.push(worker(i));
  }

  await Promise.all(workers);

  const succeeded = Object.values(statusTracker).filter(s => s.status === 'SUCCESS').length;
  const failed = Object.values(statusTracker).filter(s => s.status === 'FAILED').length;

  console.log('\n================================================================');
  console.log(`Batch Generation Finished!`);
  console.log(`Total Topics: ${topics.length}`);
  console.log(`Succeeded: ${succeeded}`);
  console.log(`Failed: ${failed}`);
  console.log('================================================================');
}

main().catch(err => {
  console.error('Fatal execution error:', err);
  process.exit(1);
});
