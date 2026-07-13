/**
 * UPSSSC Lower Mains Polity Questions Generator
 * Generates and injects Practice, PYQ, and Test questions for Polity topics
 */

require('dotenv').config();
const { GoogleGenAI } = require('@google/genai');
const fs = require('fs');
const path = require('path');

const API_KEY = process.env.GEMINI_API_KEY;
const ai = new GoogleGenAI({ apiKey: API_KEY });

const BASE = path.join(__dirname, '..', 'upsssc-lower-mains', 'polity');

const PREMIUM_MODELS = [
  'gemini-3.5-flash',
  'gemini-3-flash-preview',
  'gemini-2.5-flash',
  'gemini-2.5-flash-lite'
];

// Target 14 underpopulated polity topics by default
const TARGET_TOPICS = [
  'regulating-act-1773-to-charter-act-1853',
  'government-of-india-acts-1858-1919-1935',
  'constituent-assembly-making-of-the-constitution',
  'fundamental-rights-duties',
  'emergency-provisions',
  'union-executive-president-pm-council-of-ministers',
  'judiciary-supreme-court-high-courts-subordinate-courts',
  'constitutional-non-constitutional-bodies',
  'pesa-act-1996',
  'public-policy-formulation-implementation',
  'right-to-information-rti-act',
  'lokpal-and-lokayukta',
  'official-language-provisions',
  'community-development-programme-cdp-1952'
];

function buildPrompt(topicKey) {
  return `You are an expert UPSSSC Lower Mains exam content creator for Indian Polity & Governance.
Generate Practice Questions, PYQs, and Test Questions for the topic key: "${topicKey}".

Generate:
- Exactly 30 Practice Questions (mixture of: factual, match-the-column, multi-statement True/False, assertion-reason, and data-based questions).
- Exactly 10 PYQs (realistic years and UP exams: UP PCS 2015-2023, UPSSSC, UP Lower PCS).
- Exactly 15 Test Questions (distinct from practice).

All content must be fully bilingual (English + Hindi) throughout all questions, options, and explanations.

Return ONLY a valid JSON object. No markdown fences. Just raw JSON.
JSON Structure:
{
  "practiceQs": [
    {
      "qEn": "Question in English",
      "qHi": "Question in Hindi",
      "opts": [
        {"en": "Opt A English", "hi": "Opt A Hindi"},
        {"en": "Opt B English", "hi": "Opt B Hindi"},
        {"en": "Opt C English", "hi": "Opt C Hindi"},
        {"en": "Opt D English", "hi": "Opt D Hindi"}
      ],
      "ans": 0, // 0-based index
      "solEn": "Detailed explanation in English",
      "solHi": "Detailed explanation in Hindi"
    }
  ],
  "pyqs": [
    {
      "qEn": "...", "qHi": "...", "opts": [...], "ans": 0, 
      "year": "UP PCS 2019", 
      "solEn": "...", "solHi": "..."
    }
  ],
  "testQs": [
    {
      "qEn": "...", "qHi": "...", "opts": [...], 
      "ans": "A", // Letter value: "A", "B", "C", "D"
      "solEn": "...", "solHi": "..."
    }
  ]
}`;
}

function buildPracticeHtml(qs) {
  const letters = ['A', 'B', 'C', 'D'];
  return qs.map((q, i) => {
    const opts = q.opts.map((o, j) => `
                    <label class="opt-label">
                        <input type="radio" class="opt-radio" name="q${i}" value="${letters[j]}">
                        <span class="lang-en"><b>${letters[j]}.</b> ${o.en}</span>
                        <span class="lang-hi"><b>${letters[j]}.</b> ${o.hi}</span>
                    </label>`).join('');
    return `
                <div class="practice-question-card">
                    <div class="q-row">
                        <div class="q-num-badge">${i + 1}</div>
                        <div class="q-body">
                            <p class="q-text lang-en">${q.qEn}</p>
                            <p class="q-text lang-hi">${q.qHi}</p>
                            <div class="q-options">${opts}
                            </div>
                            <details class="solution-details">
                                <summary class="lang-en">Show Answer</summary>
                                <summary class="lang-hi">उत्तर देखें</summary>
                                <p class="solution-correct lang-en">✔ Correct: ${letters[q.ans]}</p>
                                <p class="solution-correct lang-hi">✔ सही उत्तर: ${letters[q.ans]}</p>
                                <p class="lang-en">${q.solEn}</p>
                                <p class="lang-hi">${q.solHi}</p>
                            </details>
                        </div>
                    </div>
                </div>`;
  }).join('');
}

function buildPyqHtml(qs) {
  const letters = ['A', 'B', 'C', 'D'];
  return qs.map((q, i) => {
    const opts = q.opts.map((o, j) => `
                    <label class="opt-label">
                        <input type="radio" class="opt-radio" name="pyq${i}" value="${letters[j]}">
                        <span class="lang-en"><b>${letters[j]}.</b> ${o.en}</span>
                        <span class="lang-hi"><b>${letters[j]}.</b> ${o.hi}</span>
                    </label>`).join('');
    return `
                <div class="practice-question-card">
                    <div class="q-row">
                        <div class="q-num-badge">${i + 1}</div>
                        <div class="q-body">
                            <span class="badge-pyq lang-en">${q.year} (UP Exam)</span>
                            <span class="badge-pyq lang-hi">${q.year} (यूपी परीक्षा)</span>
                            <p class="q-text lang-en">${q.qEn}</p>
                            <p class="q-text lang-hi">${q.qHi}</p>
                            <div class="q-options">${opts}
                            </div>
                            <details class="solution-details">
                                <summary class="lang-en">Show Answer</summary>
                                <summary class="lang-hi">उत्तर देखें</summary>
                                <p class="solution-correct lang-en">✔ Correct: ${letters[q.ans]}</p>
                                <p class="solution-correct lang-hi">✔ सही उत्तर: ${letters[q.ans]}</p>
                                <p class="lang-en">${q.solEn}</p>
                                <p class="lang-hi">${q.solHi}</p>
                            </details>
                        </div>
                    </div>
                </div>`;
  }).join('');
}

function buildTestHtml(qs) {
  return qs.map((q, i) => {
    const opts = q.opts.map((o, j) => {
      const letters = ['A', 'B', 'C', 'D'];
      return `\n                                <div class="test-opt" data-qi="${i}" data-ch="${letters[j]}" onclick="selOpt(this)"><span class="opt-ltr">${letters[j]}</span><span class="lang-en">${o.en}</span><span class="lang-hi">${o.hi}</span></div>`;
    }).join('');
    return `
                        <div class="test-qblock" id="tq-${i}">
                            <p class="test-qtext"><span class="test-qnum">Q${i + 1}</span><span style="display:block;margin-top:6px"><span class="lang-en">${q.qEn}</span><span class="lang-hi">${q.qHi}</span></span></p>
                            <div class="test-opts-grid">${opts}
                            </div><input type="hidden" id="tans-${i}" value="${q.ans}"><input type="hidden" id="tsel-${i}" value="">
                        </div>`;
  }).join('');
}

async function processTopic(topicKey) {
  console.log(`\n Generating questions for: ${topicKey}...`);
  const prompt = buildPrompt(topicKey);

  let raw;
  const MAX_RETRIES = PREMIUM_MODELS.length * 2;
  const BASE_DELAY = 15000;

  for (let attempt = 0; attempt < MAX_RETRIES; attempt++) {
    const model = PREMIUM_MODELS[attempt % PREMIUM_MODELS.length];
    try {
      console.log(`  -> Using model: ${model} (attempt ${attempt + 1}/${MAX_RETRIES})`);
      const response = await ai.models.generateContent({
        model,
        contents: prompt,
        config: {
          thinkingConfig: { thinkingBudget: 0 },
          temperature: 0.7,
          maxOutputTokens: 65536
        }
      });
      raw = response.text;
      console.log(`  OK Got response from ${model}`);
      break; 
    } catch (err) {
      const isRetryable = err.message && (
        err.message.includes('503') ||
        err.message.includes('UNAVAILABLE') ||
        err.message.includes('high demand') ||
        err.message.includes('overloaded') ||
        err.message.includes('429') ||
        err.message.includes('RESOURCE_EXHAUSTED')
      );
      if (isRetryable && attempt < MAX_RETRIES - 1) {
        const delay = BASE_DELAY * (attempt + 1);
        console.log(`  WARN ${model} error (attempt ${attempt + 1}) -> switching model in ${delay / 1000}s...`);
        await new Promise(r => setTimeout(r, delay));
      } else {
        console.error(`  FAIL All models failed for ${topicKey}:`, err.message);
        throw err;
      }
    }
  }

  let jsonStr = raw.trim();
  jsonStr = jsonStr.replace(/^```(?:json)?\n?/m, '').replace(/\n?```$/m, '');

  let data;
  try {
    data = JSON.parse(jsonStr);
  } catch (e) {
    const match = jsonStr.match(/\{[\s\S]*\}/);
    if (match) {
      try { data = JSON.parse(match[0]); }
      catch (e2) {
        console.error(`  FAIL JSON parse failed for ${topicKey}`);
        throw e2;
      }
    } else {
      throw e;
    }
  }

  const indexPath = path.join(BASE, topicKey, 'index.html');
  if (!fs.existsSync(indexPath)) {
    console.error(`  FAIL index.html not found for ${topicKey}`);
    return;
  }
  let html = fs.readFileSync(indexPath, 'utf8');

  // Inject Practice
  if (data.practiceQs) {
    const practiceHtml = buildPracticeHtml(data.practiceQs);
    const pRegex = /(<div id="tab-practice"[^>]*>)\s*<div class="info-banner">[\s\S]*?<\/div>\s*(<div class="next-tab-btn-container">)/;
    html = html.replace(pRegex, `$1\n${practiceHtml}\n$2`);
  }

  // Inject PYQs
  if (data.pyqs) {
    const pyqHtml = buildPyqHtml(data.pyqs);
    const pRegex = /(<div id="tab-pyqs"[^>]*>)\s*<div class="info-banner">[\s\S]*?<\/div>\s*(<div class="next-tab-btn-container">)/;
    html = html.replace(pRegex, `$1\n${pyqHtml}\n$2`);
  }

  // Inject Test
  if (data.testQs) {
    const testHtml = buildTestHtml(data.testQs);
    const fullTestUI = `
            <div class="test-container">
                <div id="test-start-screen">
                    <p class="test-desc lang-en">This test contains 15 multiple-choice questions based on the exam syllabus. You have 15 minutes to complete the test.</p>
                    <p class="test-desc lang-hi">इस परीक्षा में पाठ्यक्रम के आधार पर 15 बहुविकल्पीय प्रश्न हैं। परीक्षा पूरी करने के लिए आपके पास 15 मिनट का समय है।</p>
                    <button class="start-test-btn" onclick="startTest()">
                        <span class="lang-en">Start Test</span>
                        <span class="lang-hi">टेस्ट शुरू करें</span>
                    </button>
                </div>
                <div id="test-area" style="display:none">
                    <div class="test-hdr">
                        <div><span class="lang-en">Time Left</span><span class="lang-hi">शेष समय</span></div>
                        <div class="test-tmr" id="test-timer">15:00</div>
                    </div>
                    <div class="test-prog-bar"><div class="test-prog-fill" id="test-prog" style="width:0%"></div></div>
                    <div id="test-questions">
${testHtml}
                    </div>
                    <div style="text-align:center;margin:24px 0">
                        <button onclick="submitTest()" id="submit-btn" style="padding:13px 38px;background:linear-gradient(135deg,#27ae60,#2ecc71);color:white;border:none;border-radius:30px;font-size:1.1rem;font-weight:700;cursor:pointer;box-shadow:0 8px 20px rgba(39,174,96,0.4);">
                            <i class="fas fa-paper-plane"></i>
                            <span class="lang-en">Submit Test</span><span class="lang-hi">टेस्ट जमा करें</span>
                        </button>
                    </div>
                </div>
                <div class="test-result" id="test-result">
                    <div style="font-size:1.3rem"><i class="fas fa-trophy"></i> <span class="lang-en">Test Complete!</span><span class="lang-hi">टेस्ट पूर्ण!</span></div>
                    <div class="result-score" id="res-score">0/15</div>
                    <div id="res-label" style="font-size:1rem;opacity:0.9;margin-bottom:5px"></div>
                    <div class="grade-bdg" id="res-grade"></div>
                    <div style="margin-top:18px">
                        <button class="tact-btn" onclick="retakeTest()" style="background:#059669;color:white"><i class="fas fa-redo"></i> <span class="lang-en">Retake</span><span class="lang-hi">पुनः दें</span></button>
                        <button class="tact-btn" data-tab="practice" onclick="switchTab('practice')" style="background:white;color:#059669"><i class="fas fa-book"></i> <span class="lang-en">Practice More</span><span class="lang-hi">और अभ्यास करें</span></button>
                    </div>
                </div>
            </div>
    `;
    const tRegex = /(<div id="tab-test"[^>]*>)\s*<div class="info-banner">[\s\S]*?<\/div>\s*(<\/div>)/;
    html = html.replace(tRegex, `$1\n${fullTestUI}\n$2`);
  }

  // Inject Test Data
  if (data.testQs) {
    const testDataJSON = JSON.stringify(data.testQs.map(q => ({ ans: q.ans, solEn: q.solEn, solHi: q.solHi })));
    const scriptTag = `
            <script>
                window.upssscTestData = ${testDataJSON};
            </script>
            <script src="/assets/js/upsssc-lower.min.js?v=117a746d"></script>`;
    
    // Replace the standard script loading part
    const scriptRegex = /<script src="\/assets\/js\/upsssc-lower\.min\.js\?v=117a746d"><\/script>/;
    html = html.replace(scriptRegex, scriptTag);
  }

  fs.writeFileSync(indexPath, html, 'utf8');
  console.log(`  ✓ Written: polity/${topicKey}/index.html (${Math.round(html.length / 1024)} KB)`);
}

async function main() {
  console.log('=== UPSSSC Lower Mains Polity Questions Generator ===');
  
  const retryKeys = process.env.RETRY_KEYS ? process.env.RETRY_KEYS.split(',').map(k => k.trim()) : null;
  const topicsToRun = retryKeys ? TARGET_TOPICS.filter(t => retryKeys.includes(t)) : TARGET_TOPICS;

  console.log(`Topics to process: ${topicsToRun.length}`);

  const failed = [];
  for (const topic of topicsToRun) {
    try {
      await processTopic(topic);
      await new Promise(r => setTimeout(r, 12000));
    } catch (err) {
      console.error(`  ✗ Failed: ${topic} - ${err.message}`);
      failed.push(topic);
    }
  }

  console.log('\n=== Polity Questions Generation Complete ===');
  if (failed.length > 0) {
    console.log(`Failed topics (${failed.length}): ${failed.join(', ')}`);
  }
}

main().catch(console.error);
