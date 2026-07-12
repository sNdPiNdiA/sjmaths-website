/**
 * UPSSSC Lower Mains Hindi Page Generator
 * Uses Gemini API to generate THEORY ONLY content for 51 Hindi topics
 * Run: node scripts/gen_hindi_pages.js
 */

require('dotenv').config();
const { GoogleGenAI } = require('@google/genai');
const fs = require('fs');
const path = require('path');

const API_KEY = process.env.GEMINI_API_KEY;
const ai = new GoogleGenAI({ apiKey: API_KEY });

const BASE = path.join(__dirname, '..', 'upsssc-lower-mains', 'hindi');
const indexHtmlPath = path.join(__dirname, '..', 'upsssc-lower-mains', 'index.html');

// ─── Extract Topics from index.html ───────────────────────────────────────────
function extractTopics() {
    let content = fs.readFileSync(indexHtmlPath, 'utf8');
    const regex = /<a href="\.\/hindi\/([^\/]+)\/"[^>]*><span class="lang-hi">([^<]+)<\/span>/g;
    let match;
    const topics = [];

    while ((match = regex.exec(content)) !== null) {
        const folderName = match[1];
        const rawHindiName = match[2];

        // Edge case: if the folder is still 'topic', we skip or map it, 
        // but we already renamed everything so folderName is the Hindi name.
        
        topics.push({
            key: folderName,
            titleEn: rawHindiName,
            titleHi: rawHindiName,
            breadEn: rawHindiName,
            breadHi: rawHindiName,
            descEn: "UPSSSC लोअर मेन्स के लिए " + rawHindiName + " की व्यापक अध्ययन मार्गदर्शिका।",
            descHi: "UPSSSC लोअर मेन्स के लिए " + rawHindiName + " की व्यापक अध्ययन मार्गदर्शिका।",
            prompt: `Generate UPSSSC Lower Mains exam content for Hindi Grammar topic: "${rawHindiName}". Ensure the explanation covers definitions, detailed grammar rules, plenty of examples, exceptions, and practical usage.`
        });
    }
    return topics;
}

const TOPICS = extractTopics();

// ─── HTML Template ────────────────────────────────────────────────────────────

function pageShell(topic, theoryHtml) {
  return `<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${topic.titleHi} - UPSSSC Lower Mains Hindi</title>
    <meta name="description" content="${topic.descEn}">

    <!-- CSS Dependencies -->
    <link
        href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700;800&family=Inter:wght@400;500;600;700&display=swap"
        rel="stylesheet">
    <link rel="stylesheet" href="/assets/vendor/fontawesome/css/all.min.css?v=7441465c">
    <link rel="stylesheet" href="/assets/css/main.min.css?v=05feb74c">
    <link rel="stylesheet" href="/assets/css/improved-ui.min.css?v=c323837a">
    <link rel="stylesheet" href="/assets/css/topic-details.min.css?v=7bf51abb">
    <link rel="stylesheet" href="/assets/css/upsssc-lower.min.css?v=9d684fc1">
    <script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
    <script>mermaid.initialize({startOnLoad:true});</script>
</head>

<body>
    <div class="container">
        <div class="top-controls">
            <button class="lang-toggle-btn" onclick="toggleLang()">A/अ</button>
        </div>

        <div class="breadcrumbs">
            <div class="breadcrumbs-path">
                <a href="../../index.html">Syllabus</a>
                <i class="fas fa-chevron-right"></i>
                <a href="../../index.html#general-hindi">सामान्य हिन्दी</a>
                <i class="fas fa-chevron-right"></i>
                <span class="lang-en">${topic.breadEn}</span>
                <span class="lang-hi">${topic.breadHi}</span>
            </div>
        </div>

        <div class="topic-header">
            <h1>
                <span class="lang-en">${topic.titleEn}</span>
                <span class="lang-hi">${topic.titleHi}</span>
            </h1>
            <p>
                <span class="lang-en">${topic.descEn}</span>
                <span class="lang-hi">${topic.descHi}</span>
            </p>
        </div>

        <div class="subject-nav">
            <button class="sub-nav-item active" data-tab="theory" onclick="switchTab('theory')">
                <span class="lang-en">Theory &amp; Concepts</span>
                <span class="lang-hi">सिद्धांत और अवधारणाएं</span>
            </button>
            <button class="sub-nav-item" data-tab="practice" onclick="switchTab('practice')">
                <span class="lang-en">Practice (30 Qs)</span>
                <span class="lang-hi">अभ्यास (30 प्रश्न)</span>
            </button>
            <button class="sub-nav-item" data-tab="pyqs" onclick="switchTab('pyqs')">
                <span class="lang-en">UP Gov PYQs</span>
                <span class="lang-hi">यूपी सरकार PYQs</span>
            </button>
            <button class="sub-nav-item" data-tab="test" onclick="switchTab('test')">
                <span class="lang-en">15-Q Test</span>
                <span class="lang-hi">15-प्रश्न टेस्ट</span>
            </button>
        </div>

        <div class="topic-content">

            <div id="tab-theory" class="tab-content" style="display:block">
${theoryHtml}
                <div class="next-tab-btn-container">
                    <button class="next-tab-btn" data-tab="practice" onclick="switchTab('practice')">
                        <span class="lang-en">Next: Practice Questions</span>
                        <span class="lang-hi">अगला: अभ्यास प्रश्न</span>
                        <i class="fas fa-arrow-right"></i>
                    </button>
                </div>
            </div>

            <div id="tab-practice" class="tab-content" style="display:none">
                <div class="info-banner">
                    <span class="lang-en">Practice questions coming soon! Check back later.</span>
                    <span class="lang-hi">अभ्यास प्रश्न जल्द आ रहे हैं! बाद में देखें।</span>
                </div>
                <div class="next-tab-btn-container">
                    <button class="next-tab-btn" data-tab="pyqs" onclick="switchTab('pyqs')">
                        <span class="lang-en">Next: UP Gov PYQs</span>
                        <span class="lang-hi">अगला: यूपी सरकार PYQs</span>
                        <i class="fas fa-arrow-right"></i>
                    </button>
                </div>
            </div>

            <div id="tab-pyqs" class="tab-content" style="display:none">
                <div class="info-banner">
                    <span class="lang-en">Previous Year Questions coming soon!</span>
                    <span class="lang-hi">पिछले वर्ष के प्रश्न जल्द आ रहे हैं!</span>
                </div>
                <div class="next-tab-btn-container">
                    <button class="next-tab-btn" data-tab="test" onclick="switchTab('test')">
                        <span class="lang-en">Next: 15-Q Test</span>
                        <span class="lang-hi">अगला: 15-प्रश्न टेस्ट</span>
                        <i class="fas fa-arrow-right"></i>
                    </button>
                </div>
            </div>

            <div id="tab-test" class="tab-content" style="display:none">
                <div class="info-banner">
                    <span class="lang-en">Timed test coming soon!</span>
                    <span class="lang-hi">समयबद्ध टेस्ट जल्द आ रहे हैं!</span>
                </div>
            </div>

        </div>
    </div>

        <script>
            window.upssscTestData = [];
        </script>
        <script src="/assets/js/upsssc-lower.min.js?v=117a746d"></script>
        <script src="/assets/js/main.min.js?v=86340191"></script>
</body>

</html>`;
}

// ─── Gemini Prompt Builder (Theory Only) ─────────────────────────────────────

function buildTheoryPrompt(topic) {
  return `You are an expert UPSSSC Lower Mains exam content creator for General Hindi Grammar (सामान्य हिन्दी).
Generate ONLY the THEORY/CONCEPTS section for: "${topic.titleHi}"

IMPORTANT: Return ONLY a valid JSON object. No markdown, no explanation. Just the JSON.

Generate this exact JSON structure:
{
  "theory": "<VERY DETAILED HTML string with 10-15 card-premium divs>"
}

THEORY HTML RULES (CRITICAL - MAKE EXTREMELY DETAILED):
- Use these exact CSS classes: card-premium, card-title, theory-heading, theory-para, theory-highlight, theory-overflow-mb, tab-active-bar, theory-section-sep
- Each card structure: <div class="card-premium"><h3 class="card-title">...</h3>...</div>
- CRITICAL LANGUAGE RULE: The subject is Hindi. All content, explanations, and examples MUST be exclusively in Hindi. However, for the HTML markup, you MUST put the EXACT SAME Hindi text in BOTH <span class="lang-en"> and <span class="lang-hi">. DO NOT translate the Hindi to English.
  Example: <span class="lang-en">संधि की परिभाषा</span><span class="lang-hi">संधि की परिभाषा</span>
- Use <h4 class="lang-en theory-heading">heading</h4> and <h4 class="lang-hi theory-heading">heading in Hindi</h4> for subheadings
- Highlight key grammar rules, formulas, with <div class="theory-highlight"><span class="lang-en">...</span><span class="lang-hi">...</span></div>
- Use <p class="theory-para"><span class="lang-en">...</span><span class="lang-hi">...</span></p> for paragraphs

CONTENT STRUCTURE & REQUIREMENTS:
1. MINDMAP (MUST BE THE FIRST CARD):
   - You MUST generate TWO separate Mermaid diagrams summarizing the grammar topic visually. BOTH diagrams MUST be in Hindi.
   - One wrapped in <div class="lang-en"><div class="mermaid">...</div></div>
   - One wrapped in <div class="lang-hi"><div class="mermaid">...</div></div>
   - CRITICAL: Since you are returning JSON, you MUST escape newlines in the Mermaid code as \\n 
     (e.g. <div class="lang-en"><div class="mermaid">mindmap\\n  root((विषय))\\n    उपविषय</div></div>)
2. COMPARISON TABLES / QUICK REVISION:
   - The second card MUST contain comprehensive tables for quick revision (e.g., comparing types of nouns, rules of sandhi, or opposite words). 
   - Use <div class="theory-overflow-mb"><table><thead><tr class="tab-active-bar"><th>...</th></tr></thead><tbody>...</tbody></table></div>
3. DETAILED EXPLANATION:
   - Provide highly detailed grammar rules, definitions, and exceptions.
   - 10-15 cards covering ALL aspects of the topic.
4. TIPS & TRICKS:
   - The final card MUST be dedicated entirely to short tricks, mnemonics, and tips to quickly identify correct answers in the exam.

Topic details: ${topic.prompt}

CRITICAL REMINDERS:
1. Theory MUST start with a mindmap, followed by comparison tables, detailed explanation, and finally tips/tricks.
2. Provide at least 50-60 examples in total for topics like Sandhi, Samas, Paryayvachi, Vilom, etc.
3. Use ONLY Hindi text everywhere. Put the identical Hindi text in both language spans.
4. Do NOT output markdown ticks \`\`\`json. Return pure JSON.`;
}

// ─── Model Pool ───────────────────────────────────────────────────────────────
const MODEL_POOL = [
  'gemini-3.1-flash-lite',
  'gemini-3.5-flash'
];

// ─── Main Generator ───────────────────────────────────────────────────────────

async function generateTopic(topic) {
  console.log(`\n Generating theory for: ${topic.titleHi}...`);

  const prompt = buildTheoryPrompt(topic);

  let raw;
  const MAX_RETRIES = MODEL_POOL.length * 2; // 4 attempts total
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
        console.error(`  FAIL All models failed for ${topic.key}:`, err.message);
        throw err;
      }
    }
  }

  // Extract JSON from response
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
        console.error(`  FAIL JSON parse failed for ${topic.key}`);
        console.error('  Raw (first 500):', jsonStr.substring(0, 500));
        throw e2;
      }
    } else {
      throw e;
    }
  }

  const theoryHtml = data.theory || '<p>Content generation failed. Please retry.</p>';
  const html = pageShell(topic, theoryHtml);

  const outDir = path.join(BASE, topic.key);
  if (!fs.existsSync(outDir)) fs.mkdirSync(outDir, { recursive: true });
  const outFile = path.join(outDir, 'index.html');
  fs.writeFileSync(outFile, html, 'utf8');

  const sizeKB = Math.round(html.length / 1024);
  console.log(`  OK Written: hindi/${topic.key}/index.html (${sizeKB} KB)`);
}

async function main() {
  console.log('=== UPSSSC Lower Mains Hindi Theory Generator ===');
  console.log(`Using Gemini API Key: ${API_KEY ? API_KEY.substring(0, 10) + '...' : 'NOT FOUND'}`);

  if (!API_KEY) {
    console.error('ERROR: GEMINI_API_KEY not found in .env');
    process.exit(1);
  }

  const retryKeys = process.env.RETRY_KEYS
    ? process.env.RETRY_KEYS.split(',').map(k => k.trim())
    : null;
  const topicsToRun = retryKeys
    ? TOPICS.filter(t => retryKeys.includes(t.key))
    : TOPICS;

  if (retryKeys) console.log(`Retrying only: ${retryKeys.join(', ')}`);
  console.log(`Topics to generate: ${topicsToRun.length}`);

  const failed = [];
  for (const topic of topicsToRun) {
    try {
      await generateTopic(topic);
      // Wait 12 seconds between calls to respect rate limits
      await new Promise(r => setTimeout(r, 12000));
    } catch (err) {
      console.error(`  FAIL Failed: ${topic.key} - ${err.message}`);
      failed.push(topic.key);
    }
  }

  console.log('\n=== Generation Complete ===');
  if (failed.length > 0) {
    console.log(`Failed topics (${failed.length}): ${failed.join(', ')}`);
    console.log(`\nRetry with:`);
    console.log(`  RETRY_KEYS="${failed.join(',')}" node scripts/gen_hindi_pages.js`);
  } else {
    console.log('All Hindi theory pages generated successfully!');
  }
}

main().catch(console.error);
