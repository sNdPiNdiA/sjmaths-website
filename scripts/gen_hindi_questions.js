/**
 * UPSSSC Lower Mains Hindi Questions Generator
 * Uses Gemini API to generate Practice, PYQ, and Test questions for all 51 topics
 * Run: node scripts/gen_hindi_questions.js
 */

require('dotenv').config();
const { GoogleGenAI } = require('@google/genai');
const fs = require('fs');
const path = require('path');

const API_KEY = process.env.GEMINI_API_KEY;
const ai = new GoogleGenAI({ apiKey: API_KEY });

const BASE = path.join(__dirname, '..', 'upsssc-lower-mains', 'hindi');

// Get all topics (directories in hindi/)
function getTopics() {
  const dirs = fs.readdirSync(BASE, { withFileTypes: true })
    .filter(dirent => dirent.isDirectory())
    .map(dirent => dirent.name);
  return dirs;
}

const MODEL_POOL = ['gemini-3.1-flash-lite', 'gemini-3.5-flash'];

function buildPrompt(topicName) {
  return `You are an expert UPSSSC Lower Mains exam content creator for General Hindi Grammar (सामान्य हिन्दी).
Generate exactly 30 Practice Questions, 10 Previous Year Questions (PYQs), and 15 Timed Test Questions for the topic: "${topicName}".

IMPORTANT: The subject is Hindi. All questions, options, and explanations MUST be exclusively in Hindi.
Return ONLY a valid JSON object. No markdown ticks, no explanation.

Generate this exact JSON structure:
{
  "practiceHtml": "<string containing 30 .practice-card divs>",
  "pyqsHtml": "<string containing 10 .practice-card divs>",
  "testHtml": "<string containing 15 .test-q-block divs>",
  "testData": [ { "ans": "A/B/C/D", "solEn": "explanation in Hindi", "solHi": "explanation in Hindi" } ] // exactly 15 objects
}

HTML STRUCTURE RULES (CRITICAL):

1. PRACTICE & PYQs HTML (practiceHtml and pyqsHtml):
For each question, output this exact structure:
<div class="practice-card">
  <div class="q-header"><div>Q[Number]. [Question Text]</div></div>
  <ul class="options-list">
    <li class="opt-item">A) [Option]</li>
    <li class="opt-item">B) [Option]</li>
    <li class="opt-item">C) [Option]</li>
    <li class="opt-item">D) [Option]</li>
  </ul>
  <button class="sol-btn" onclick="this.nextElementSibling.style.display='block'">उत्तर देखें</button>
  <div class="explanation-box" style="display:none">
    <strong>सही उत्तर: [A/B/C/D]</strong><br>
    [Detailed Explanation]
  </div>
</div>

2. TEST HTML (testHtml):
For each question (from index 0 to 14), output this exact structure (NOTE: id and data-qi MUST match the index):
<div class="test-q-block" id="tq-[index]">
  <div class="test-q-text">Q[index + 1]. [Question Text]</div>
  <div class="test-options">
    <div class="test-opt" data-qi="[index]" data-ch="A" onclick="selOpt(this)">A) [Option A]</div>
    <div class="test-opt" data-qi="[index]" data-ch="B" onclick="selOpt(this)">B) [Option B]</div>
    <div class="test-opt" data-qi="[index]" data-ch="C" onclick="selOpt(this)">C) [Option C]</div>
    <div class="test-opt" data-qi="[index]" data-ch="D" onclick="selOpt(this)">D) [Option D]</div>
  </div>
  <input type="hidden" id="tsel-[index]" value="">
</div>

3. TEST DATA (testData):
A JSON array of exactly 15 objects. Each object must have:
- "ans": The correct option letter ("A", "B", "C", or "D").
- "solEn": The explanation in Hindi.
- "solHi": The EXACT same explanation in Hindi.
Example: { "ans": "B", "solEn": "यह दीर्घ संधि का उदाहरण है।", "solHi": "यह दीर्घ संधि का उदाहरण है।" }

Do NOT use any dual language (lang-en/lang-hi) spans for the questions. Output plain HTML tags with Hindi text.`;
}

async function generateQuestions(topicName) {
  console.log(`\n Generating questions for: ${topicName}...`);

  const prompt = buildPrompt(topicName);
  let raw;
  const MAX_RETRIES = MODEL_POOL.length * 2;
  const BASE_DELAY = 15000;

  for (let attempt = 0; attempt < MAX_RETRIES; attempt++) {
    const model = MODEL_POOL[attempt % MODEL_POOL.length];
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
        console.error(`  FAIL All models failed for ${topicName}:`, err.message);
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
        console.error(`  FAIL JSON parse failed for ${topicName}`);
        throw e2;
      }
    } else {
      throw e;
    }
  }

  // Read existing index.html
  const indexPath = path.join(BASE, topicName, 'index.html');
  if (!fs.existsSync(indexPath)) {
    console.error(`  FAIL index.html not found for ${topicName}`);
    return;
  }
  let html = fs.readFileSync(indexPath, 'utf8');

  // Inject Practice
  if (data.practiceHtml) {
    const pRegex = /(<div id="tab-practice"[^>]*>)([\s\S]*?)(<div class="next-tab-btn-container">)/;
    html = html.replace(pRegex, `$1\n${data.practiceHtml}\n$3`);
  }

  // Inject PYQs
  if (data.pyqsHtml) {
    const pRegex = /(<div id="tab-pyqs"[^>]*>)([\s\S]*?)(<div class="next-tab-btn-container">)/;
    html = html.replace(pRegex, `$1\n${data.pyqsHtml}\n$3`);
  }

  // Inject Test
  if (data.testHtml) {
    // The test tab doesn't have a next-tab-btn-container usually, it just ends with </div></div>
    // Let's replace the content between <div id="tab-test"...> and the closing </div> of the tab.
    // Actually, in the template it is:
    // <div id="tab-test" class="tab-content" style="display:none">
    //     <div class="info-banner">...</div>
    // </div>
    // So we can replace the info-banner directly.
    const tRegex = /(<div id="tab-test"[^>]*>)\s*<div class="info-banner">[\s\S]*?<\/div>\s*(<\/div>)/;
    // Wait, the test needs the timer/start UI too!
    const fullTestUI = `
      <div id="test-start-scr" style="text-align:center; padding: 40px 20px;">
          <h3>Ready for the Test?</h3>
          <p>15 Questions • 15 Minutes</p>
          <button class="check-btn" onclick="startTest()">Start Test</button>
      </div>
      <div id="test-area" style="display:none;">
          <div style="display:flex; justify-content:space-between; margin-bottom: 20px; align-items:center;">
              <div style="font-weight:bold;">Progress: <span id="prog-fill" style="display:inline-block;height:10px;background:var(--primary);width:0%;"></span></div>
              <div id="tmr-display" style="font-size:1.5rem; font-weight:bold; color:var(--error);">15:00</div>
          </div>
          ${data.testHtml}
          <div style="text-align:center; margin-top:20px;">
              <button id="submit-btn" class="check-btn" onclick="submitTest()">Submit Test</button>
          </div>
          <div id="test-result" style="display:none; text-align:center; margin-top: 30px; padding: 20px; border-radius:10px; background:var(--box-bg);">
              <h3>Test Complete!</h3>
              <div id="res-score" style="font-size:2rem; font-weight:bold; margin: 10px 0;"></div>
              <div id="res-grade"></div>
              <div id="res-label" style="margin-top: 10px;"></div>
              <button class="check-btn" style="margin-top:20px;" onclick="retakeTest()">Retake Test</button>
          </div>
      </div>
    `;
    html = html.replace(tRegex, `$1\n${fullTestUI}\n$2`);
  }

  // Inject Test Data
  if (data.testData) {
    const scriptRegex = /window\.upssscTestData\s*=\s*\[\];/;
    html = html.replace(scriptRegex, `window.upssscTestData = ${JSON.stringify(data.testData)};`);
  }

  fs.writeFileSync(indexPath, html, 'utf8');
  console.log(`  OK Injected questions for ${topicName}`);
}

async function main() {
  console.log('=== UPSSSC Lower Mains Hindi Questions Generator ===');
  const topics = getTopics();
  console.log(`Found ${topics.length} topics.`);

  const retryKeys = process.env.RETRY_KEYS ? process.env.RETRY_KEYS.split(',').map(k => k.trim()) : null;
  const topicsToRun = retryKeys ? topics.filter(t => retryKeys.includes(t)) : topics;

  const failed = [];
  for (const topic of topicsToRun) {
    try {
      await generateQuestions(topic);
      await new Promise(r => setTimeout(r, 12000));
    } catch (err) {
      console.error(`  FAIL Failed: ${topic} - ${err.message}`);
      failed.push(topic);
    }
  }

  console.log('\n=== Generation Complete ===');
  if (failed.length > 0) {
    console.log(`Failed topics (${failed.length}): ${failed.join(', ')}`);
  }
}

main().catch(console.error);
