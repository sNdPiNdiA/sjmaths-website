import dotenv from 'dotenv';
import fs from 'node:fs/promises';
import path from 'node:path';

dotenv.config();

const apiKey = process.env.GEMINI_API_KEY;
if (!apiKey) {
  throw new Error('GEMINI_API_KEY is not set in the environment or .env file.');
}

const model = 'gemini-2.5-flash';
const delayMs = 12000;
const baseDir = path.resolve('ssc-cgl/general-awareness/history-and-culture');

const topics = [
  {
    slug: 'pre-historic-period-paleolithic-neolithic-ages',
    title: 'Pre-historic Period & Paleolithic/Neolithic Ages',
    focus: 'Palaeolithic, Mesolithic, Neolithic, Chalcolithic, tools, sites, chronology, rock art, earliest agriculture, SSC factual traps'
  },
  {
    slug: 'indus-valley-civilization-major-sites-findings-trade',
    title: 'Indus Valley Civilization: Major Sites, Findings & Trade',
    focus: 'Harappan discovery, sites, rivers, excavators, town planning, seals, crafts, trade, decline, SSC repeated site-finding pairs'
  },
  {
    slug: 'vedic-age-rig-vedic-and-later-vedic-society-literature',
    title: 'Vedic Age: Rig Vedic and Later Vedic Society & Literature',
    focus: 'Rig Vedic polity, economy, society, gods, later Vedic changes, Vedas, Brahmanas, Aranyakas, Upanishads, Vedangas'
  },
  {
    slug: 'rise-of-mahajanapadas-magadha-empire',
    title: 'Rise of Mahajanapadas & Magadha Empire',
    focus: 'Sixteen Mahajanapadas, capitals, republics, Magadha rise, Haryanka, Shishunaga, Nanda, sources, Alexander context'
  },
  {
    slug: 'buddhism-life-of-buddha-teachings-councils',
    title: 'Buddhism: Life of Buddha, Teachings & Councils',
    focus: 'Buddha life events, four noble truths, eightfold path, symbols, councils, sects, texts, patrons, SSC PYQ facts'
  },
  {
    slug: 'jainism-mahavira-philosophy-sects',
    title: 'Jainism: Mahavira, Philosophy & Sects',
    focus: 'Tirthankaras, Mahavira life, Triratna, five vows, Syadvada, Anekantavada, sects, councils, literature, symbols'
  },
  {
    slug: 'mauryan-empire',
    title: "Mauryan Empire: Chandragupta, Ashoka's Dhamma & Administration",
    focus: 'Chandragupta, Bindusara, Ashoka, Kautilya, Megasthenes, administration, edicts, dhamma, art, decline'
  },
  {
    slug: 'gupta-empire',
    title: 'Gupta Empire: Samudragupta, Chandragupta II & Golden Age',
    focus: 'Gupta rulers, inscriptions, administration, coins, literature, science, art, religion, foreign travellers, decline'
  },
  {
    slug: 'post-gupta-period',
    title: 'Post-Gupta Period: Harshavardhana & Southern Dynasties',
    focus: 'Harsha, Pushyabhutis, Banabhatta, Xuanzang, Chalukyas, Pallavas, Rashtrakutas, Sangam linkages, temples, regional powers'
  }
];

const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));
const esc = (value = '') => String(value)
  .replace(/&/g, '&amp;')
  .replace(/</g, '&lt;')
  .replace(/>/g, '&gt;')
  .replace(/"/g, '&quot;');

function cleanJson(text) {
  return text.replace(/^```json\s*/i, '').replace(/^```\s*/i, '').replace(/```$/i, '').trim();
}

function promptFor(topic) {
  return `Create SSC CGL General Awareness study content for "${topic.title}".
Level: SSC CGL Tier 1 and Tier 2 General Awareness. Include all high-frequency and previous-year-type facts commonly asked in SSC CGL, CHSL, CPO, MTS, Stenographer and related SSC exams. Do not invent exact years/shifts unless certain; label such questions as "SSC PYQ pattern" or "Repeated SSC theme" in explanations.
Focus coverage: ${topic.focus}

Return ONLY valid JSON with this exact schema:
{
  "description": "one SEO description under 155 chars",
  "theory": [
    {"heading":"...", "bodyHtml":"HTML using p, ul, li, table only"}
  ],
  "quickRevision": ["25 concise facts"],
  "practice": [
    {"q":"...", "options":["A","B","C","D"], "answer":0, "explanation":"..."}
  ],
  "pyqs": [
    {"q":"...", "options":["A","B","C","D"], "answer":0, "tag":"SSC PYQ pattern", "explanation":"..."}
  ],
  "test": [
    {"q":"...", "options":["A","B","C","D"], "answer":0, "explanation":"..."}
  ]
}
Counts required: theory 6 sections, practice 30 questions, pyqs 30 questions, test 15 questions.
Use Indian English. Questions must be factually accurate and exam-focused.`;
}

async function generate(topic) {
  const url = `https://generativelanguage.googleapis.com/v1beta/models/${model}:generateContent?key=${apiKey}`;
  const res = await fetch(url, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      contents: [{ parts: [{ text: promptFor(topic) }] }],
      generationConfig: { responseMimeType: 'application/json', temperature: 0.35 }
    })
  });
  if (!res.ok) throw new Error(`${res.status} ${res.statusText}: ${await res.text()}`);
  const json = await res.json();
  const text = json.candidates?.[0]?.content?.parts?.map((p) => p.text || '').join('') || '';
  return JSON.parse(cleanJson(text));
}

function questionCard(item, index, extra = '') {
  const letters = ['A', 'B', 'C', 'D'];
  return `<div class="practice-question-card ${extra}">
    <h4>Q${index + 1}. ${esc(item.q)}</h4>
    <div class="options-grid">${item.options.map((opt, i) => `<div class="option"><strong>${letters[i]}.</strong> ${esc(opt)}</div>`).join('')}</div>
    <div class="answer-box"><strong>Answer:</strong> ${letters[item.answer]} &nbsp; <span>${esc(item.options[item.answer])}</span><p>${esc(item.explanation)}</p>${item.tag ? `<small>${esc(item.tag)}</small>` : ''}</div>
  </div>`;
}

function render(topic, data) {
  const canonical = `https://sjmaths.com/ssc-cgl/general-awareness/history-and-culture/${topic.slug}/`;
  const title = `${topic.title} | SSC CGL | SJMaths`;
  const testData = data.test.map((q) => ({ ans: ['A', 'B', 'C', 'D'][q.answer], solEn: q.explanation, solHi: q.explanation }));
  return `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>${esc(title)}</title>
  <meta name="description" content="${esc(data.description)}">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <link rel="canonical" href="${canonical}">
  <meta property="og:title" content="${esc(title)}">
  <meta property="og:description" content="${esc(data.description)}">
  <meta property="og:url" content="${canonical}">
  <meta property="og:type" content="article">
  <meta property="og:site_name" content="SJMaths">
  <link rel="icon" type="image/png" href="/favicon.png">
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700;800&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/assets/vendor/fontawesome/css/all.min.css?v=7441465c">
  <link rel="stylesheet" href="/assets/css/main.min.css?v=4ba21ce7">
  <link rel="stylesheet" href="/assets/css/layout.min.css?v=e4922b08">
  <link rel="stylesheet" href="/assets/css/component.min.css?v=8c99f11f">
  <link rel="stylesheet" href="/assets/css/improved-ui.min.css?v=574ed909">
  <link rel="stylesheet" href="/assets/css/topic-details.min.css?v=c54bbbc3">
  <link rel="stylesheet" href="/assets/css/upsssc-lower.min.css?v=94ee8a40">
</head>
<body>
  <div id="header-container"></div>
  <div class="container">
    <div class="breadcrumbs"><div class="breadcrumbs-path"><a href="../../../syllabus/">Syllabus</a><i class="fas fa-chevron-right"></i><a href="../">History & Culture</a><i class="fas fa-chevron-right"></i><span>${esc(topic.title)}</span></div></div>
    <div class="topic-header"><h1>${esc(topic.title)}</h1><p>${esc(data.description)} Built for SSC CGL General Awareness with high-yield facts, PYQ patterns, and timed practice.</p></div>
    <div class="subject-nav">
      <button class="sub-nav-item active" data-tab="theory" onclick="switchTab('theory')">Theory & Concepts</button>
      <button class="sub-nav-item" data-tab="practice" onclick="switchTab('practice')">Practice (30 Qs)</button>
      <button class="sub-nav-item" data-tab="pyqs" onclick="switchTab('pyqs')">SSC PYQs</button>
      <button class="sub-nav-item" data-tab="test" onclick="switchTab('test')">15-Q Test</button>
    </div>
    <div class="topic-content">
      <div id="tab-theory" class="tab-content" style="display:block">
        ${data.theory.map((s, i) => `<div class="card-premium"><h3 class="card-title">${i + 1}. ${esc(s.heading)}</h3><div class="theory-para">${s.bodyHtml}</div></div>`).join('\n')}
        <div class="card-premium"><h3 class="card-title">Quick Revision Facts</h3><ul class="theory-para">${data.quickRevision.map((fact) => `<li>${esc(fact)}</li>`).join('')}</ul></div>
      </div>
      <div id="tab-practice" class="tab-content" style="display:none"><h2 class="section-title">SSC CGL Practice Questions</h2>${data.practice.map((q, i) => questionCard(q, i)).join('\n')}</div>
      <div id="tab-pyqs" class="tab-content" style="display:none"><h2 class="section-title">SSC Previous-Year Themes & PYQ Patterns</h2><div class="info-banner"><p class="sol-text"><strong><i class="fas fa-info-circle"></i> Note:</strong> These questions cover repeated SSC facts and PYQ-style patterns. Exact shift labels are avoided unless certain.</p></div>${data.pyqs.map((q, i) => questionCard(q, i, 'pyq-card')).join('\n')}</div>
      <div id="tab-test" class="tab-content" style="display:none"><div id="test-start-scr" class="test-start-scr"><h3><i class="fas fa-stopwatch"></i> 15-Question Timed Test</h3><p style="color:#666;margin-bottom:20px">Attempt this mixed SSC-level test after revision.</p><button class="btn btn-primary" onclick="startTest()">Start Test</button></div><div id="test-area" style="display:none">${data.test.map((q, i) => questionCard(q, i, 'test-question')).join('\n')}</div></div>
    </div>
  </div>
  <script>window.upssscTestData = ${JSON.stringify(testData)};</script>
  <script src="/assets/js/search.min.js?v=68a0a505" defer data-cfasync="false"></script>
  <script src="/assets/js/main.min.js?v=10f0770d" defer data-cfasync="false"></script>
  <script src="/assets/js/global-header.min.js?v=d6ad26b3" defer data-cfasync="false"></script>
  <script src="/assets/js/global-footer.min.js?v=c641c625" defer data-cfasync="false"></script>
  <script src="/assets/js/upsssc-lower.min.js?v=04b168f8" defer data-cfasync="false"></script>
</body>
</html>`;
}

for (const [index, topic] of topics.entries()) {
  console.log(`[${index + 1}/${topics.length}] Generating ${topic.slug}`);
  const data = await generate(topic);
  const dir = path.join(baseDir, topic.slug);
  await fs.mkdir(dir, { recursive: true });
  await fs.writeFile(path.join(dir, 'index.html'), render(topic, data), 'utf8');
  console.log(`Wrote ${path.join(dir, 'index.html')}`);
  if (index < topics.length - 1) {
    await sleep(delayMs);
  }
}
