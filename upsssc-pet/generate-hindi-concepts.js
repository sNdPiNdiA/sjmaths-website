import fs from 'fs';
import path from 'path';

// ============================================================================
// ENV LOADER
// ============================================================================
if (fs.existsSync('.env')) {
    const envContent = fs.readFileSync('.env', 'utf8');
    for (const line of envContent.split('\n')) {
        const match = line.match(/^\s*([\w.-]+)\s*=\s*(.*)?\s*$/);
        if (match) {
            const key = match[1];
            let value = match[2] || '';
            if (value.startsWith('"') && value.endsWith('"')) value = value.slice(1, -1);
            if (value.startsWith("'") && value.endsWith("'")) value = value.slice(1, -1);
            process.env[key] = process.env[key] || value.trim();
        }
    }
}

const apiKey = process.env.GEMINI_API_KEY;
if (!apiKey) {
    console.error('GEMINI_API_KEY is not set. Please add it to .env file.');
    process.exit(1);
}

// ============================================================================
// CONSTANTS
// ============================================================================
const REQUEST_DELAY_MS = 20000; // 20s between API calls to avoid rate limiting
const MAX_RETRIES = 5;
let currentModel = 'gemini-3.6-flash';

// ============================================================================
// UPSSSC PET HINDI TOPICS (9 topics from syllabus)
// ============================================================================
const HINDI_TOPICS = [
    {
        dir: 'संधि',
        name: 'Sandhi (Joinings)',
        hindiName: 'संधि',
        description: 'Detailed concepts of Hindi Sandhi (Svara, Vyanjana, and Visarga Sandhi) rules, exceptions, and practice examples for UPSSSC PET.',
        keywords: ['Sandhi', 'Svara Sandhi', 'Vyanjana Sandhi', 'Visarga Sandhi', 'Hindi Grammar', 'Syllabus']
    },
    {
        dir: 'विलोम-शब्द',
        name: 'Antonyms (Vilom Shabd)',
        hindiName: 'विलोम शब्द',
        description: 'Comprehensive list of important Hindi Antonyms (विलोम शब्द) with explanation and practice questions for UPSSSC PET.',
        keywords: ['Vilom Shabd', 'Antonyms', 'Hindi Vocabulary', 'Opposite Words']
    },
    {
        dir: 'पर्यायवाची-शब्द',
        name: 'Synonyms (Paryayvachi Shabd)',
        hindiName: 'पर्यायवाची शब्द',
        description: 'Exhaustive list of high-yield Hindi Synonyms (पर्यायवाची शब्द) categorized and simplified for UPSSSC PET exam.',
        keywords: ['Paryayvachi Shabd', 'Synonyms', 'Hindi Vocabulary', 'Similar Words']
    },
    {
        dir: 'वाक्यांशों-के-लिए-एक-शब्द',
        name: 'One Word Substitution',
        hindiName: 'वाक्यांशों के लिए एक शब्द',
        description: 'Complete compilation of One Word Substitutions (वाक्यांशों के लिए एक शब्द) in Hindi for rapid revision in UPSSSC PET.',
        keywords: ['One Word Substitution', 'Vakyanshon ke liye ek shabd', 'Hindi Grammar', 'Vocabulary']
    },
    {
        dir: 'लिंग',
        name: 'Gender (Ling)',
        hindiName: 'लिंग',
        description: 'Hindi gender rules (लिंग - पुल्लिंग एवं स्त्रीलिंग), identification shortcuts, common patterns, and exceptions for UPSSSC PET.',
        keywords: ['Ling', 'Masculine', 'Feminine', 'Pulink', 'Strilink', 'Hindi Grammar']
    },
    {
        dir: 'समरूप-भिन्नार्थक-शब्द',
        name: 'Homophones (Samroop Bhinnarthak)',
        hindiName: 'समरूप भिन्नार्थक शब्द',
        description: 'Words having similar pronunciation but different meanings (समरूप भिन्नार्थक शब्द) explained clearly with examples for UPSSSC PET.',
        keywords: ['Samroop Bhinnarthak', 'Homophones', 'Hindi Vocabulary', 'Confusing Words']
    },
    {
        dir: 'मुहावरे-लोकोक्तियाँ',
        name: 'Idioms & Proverbs',
        hindiName: 'मुहावरे-लोकोक्तियाँ',
        description: 'Important Hindi Idioms (मुहावरे) and Proverbs (लोकोक्तियाँ) with their contextual meanings and sentence usage for UPSSSC PET.',
        keywords: ['Muhavare', 'Lokoktiyan', 'Idioms', 'Proverbs', 'Hindi Grammar']
    },
    {
        dir: 'सामान्य-अशुद्धियाँ',
        name: 'Common Grammar & Spelling Errors',
        hindiName: 'सामान्य अशुद्धियाँ',
        description: 'Common grammatical, structural, and spelling errors (सामान्य अशुद्धियाँ) in Hindi sentence correction rules for UPSSSC PET.',
        keywords: ['Samanya Ashuddhiyan', 'Spelling Errors', 'Grammar Correction', 'Hindi Correction']
    },
    {
        dir: 'लेखक-और-रचनायें',
        name: 'Authors and Works (Gady & Pady)',
        hindiName: 'लेखक और रचनायें (गद्य एवं पद्य)',
        description: 'Detailed study guide of famous Hindi authors, poets, and their classic literary works (लेखक और रचनायें - गद्य एवं पद्य) for UPSSSC PET.',
        keywords: ['Lekhak aur Rachnayein', 'Hindi Authors', 'Hindi Literature', 'Poetry', 'Prose']
    }
];

// ============================================================================
// UTILITY FUNCTIONS
// ============================================================================
function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

// ============================================================================
// GEMINI API CLIENT
// ============================================================================
async function callGemini(prompt, retries = MAX_RETRIES) {
    for (let attempt = 1; attempt <= retries; attempt++) {
        try {
            const url = `https://generativelanguage.googleapis.com/v1beta/models/${currentModel}:generateContent?key=${apiKey}`;
            const res = await fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    contents: [{ parts: [{ text: prompt }] }],
                    generationConfig: {
                        temperature: 0.1,
                        maxOutputTokens: 65536,
                        topP: 0.95,
                    },
                }),
            });

            if (res.status === 429 || res.status === 403) {
                console.log(`  ⚠️ Rate limited. Waiting before retry ${attempt}/${retries}...`);
                const wait = 15000 * Math.pow(2, attempt - 1);
                console.log(`  ⏳ Waiting ${wait / 1000}s...`);
                await sleep(wait);
                continue;
            }

            if (res.status === 503) {
                const wait = REQUEST_DELAY_MS * 2;
                console.log(`  ⏳ Service unavailable (503). Waiting ${wait / 1000}s before retry ${attempt}/${retries}...`);
                await sleep(wait);
                continue;
            }

            if (!res.ok) {
                const errBody = await res.text();
                throw new Error(`Gemini API error ${res.status}: ${errBody.substring(0, 200)}`);
            }

            const data = await res.json();
            const text = data?.candidates?.[0]?.content?.parts?.[0]?.text || '';
            if (!text || text.trim().length === 0) {
                throw new Error('Empty response from API');
            }
            return text;
        } catch (err) {
            if (attempt === retries) throw err;
            console.log(`  ⚠️ Retry ${attempt}/${retries} after error: ${err.message}`);
            await sleep(5000);
        }
    }
    throw new Error('Max retries exceeded');
}

// ============================================================================
// JSON PARSER
// ============================================================================
function parseResponse(raw) {
    if (!raw || typeof raw !== 'string') {
        throw new Error('Invalid response: expected string, got ' + typeof raw);
    }

    let cleaned = raw.trim();

    // Remove markdown code fences
    if (cleaned.startsWith('```json')) cleaned = cleaned.replace(/^```json\s*/, '').replace(/\s*```$/, '');
    else if (cleaned.startsWith('```')) cleaned = cleaned.replace(/^```\s*/, '').replace(/\s*```$/, '');

    // Fix smart quotes
    cleaned = cleaned.replace(/[\u2018\u2019]/g, "'").replace(/[\u201c\u201d]/g, '"');

    // Try direct parse
    try { return JSON.parse(cleaned); } catch (err) { }

    // Try extracting JSON from the response
    const jsonMatch = cleaned.match(/[\{\[][\s\S]*[\}\]]/);
    if (jsonMatch) {
        const repaired = jsonMatch[0]
            .replace(/(\{|,|\[|\s)([A-Za-z0-9_\-]+)\s*:/g, '$1"$2":')
            .replace(/'([^'\\]*(?:\\.[^'\\]*)*)'/g, '"$1"')
            .replace(/,\s*([}\]])/g, '$1');
        try { return JSON.parse(repaired); } catch (e) {
            try { return JSON.parse(Function('"use strict"; return (' + repaired + ')')()); } catch (e2) { }
        }
    }

    // Try to repair truncated JSON
    const jsonStart = cleaned.indexOf('{');
    if (jsonStart >= 0) {
        let partial = cleaned.substring(jsonStart);
        partial = partial.replace(/,\s*$/, '');
        let opens = 0, closes = 0, openArr = 0, closeArr = 0;
        let inString = false, escape = false;
        for (let i = 0; i < partial.length; i++) {
            const ch = partial[i];
            if (escape) { escape = false; continue; }
            if (ch === '\\') { escape = true; continue; }
            if (ch === '"') { inString = !inString; continue; }
            if (inString) continue;
            if (ch === '{') opens++;
            else if (ch === '}') closes++;
            else if (ch === '[') openArr++;
            else if (ch === ']') closeArr++;
        }
        if (inString) partial += '"';
        while (openArr > closeArr) { partial += ']'; closeArr++; }
        while (opens > closes) { partial += '}'; closes++; }
        partial = partial.replace(/,\s*([}\]])/g, '$1');
        try { return JSON.parse(partial); } catch (e) {
            try { return JSON.parse(Function('"use strict"; return (' + partial + ')')()); } catch (e2) { }
        }
    }

    console.error('❌ Raw response (first 500 chars):', cleaned.substring(0, 500));
    throw new Error('No valid JSON found in response');
}

// ============================================================================
// PROMPT BUILDER — Hindi Subject Concepts (Bilingual/Hindi allowed & encouraged)
// ============================================================================
function buildConceptsPrompt(topic) {
    return `You are an expert faculty member for UPSSSC PET (Preliminary Eligibility Test) exam preparation, specializing in General Hindi (सामान्य हिन्दी).
Create ULTRA-COMPREHENSIVE, SEO-OPTIMIZED concept notes in HINDI (with English terms/transliteration in brackets where helpful for clarity) for the topic: "${topic.name}" (${topic.hindiName}).

TOPIC CONTEXT:
- Subject: General Hindi (सामान्य हिन्दी)
- Exam: UPSSSC PET
- Topic Directory: ${topic.dir}
- Keywords to target: ${topic.keywords.join(', ')}

CRITICAL FORMAT RULES — NO PARAGRAPHS ALLOWED:
1. **STRICTLY NO PARAGRAPHS** — Do NOT use the "paragraph" type anywhere. Every section must be a table, list, or subcards.
2. Content must be **point-wise, bulleted, tabular, and structured** for rapid exam revision.
3. Use **bold** for key terms, rules, definitions, and examples within table cells and list items.
4. Content must be **comprehensive and exam-focused** — cover ALL important rules, definitions, classic examples, exceptions, and patterns asked in UPSSSC PET.
5. All definitions, examples, and rules MUST be in Hindi (Devanagari script) with high grammatical accuracy.

REQUIRED SECTION STRUCTURE (in this exact order):

SECTION 1 — "Detailed Brief Overview" (type: "table")
- A comprehensive overview table with 8-10 rows covering aspects like: परिभाषा (Definition), प्रकार (Types), पहचान (Key Identification), महत्व (Importance in PET), प्रमुख नियम (Key Rules), etc.
- Headers: ["विषय/पहल (Aspect)", "मुख्य विवरण (Key Details)"]

SECTION 2 — "Detailed Explanation with Mnemonics" (type: "subcards")
- 5-7 subcards covering major concepts/subtopics (rules, classifications, steps, and structures).
- Include clear explanation of rules and 10+ high-quality classic examples for each rule/category.
- Include 2-3 memory tricks/mnemonics (याद रखने की शार्ट-ट्रिक) to help students recall complex classifications or rules.

SECTION 3 — "Comprehensive Data Tables" (type: "table")
- 3-4 detailed tables with 10-15 rows each covering:
  a) महत्वपूर्ण उदाहरण और विच्छेद / नियम (Important Examples with explanations/splits)
  b) अपवाद तथा महत्वपूर्ण नियम (Exceptions and crucial edge cases)
  c) परीक्षाओं में बार-बार पूछे गए शब्द / वाक्य (Frequently asked terms/questions in competitive exams)
  d) श्रेणीवार वर्गीकरण (Categorized listings)

SECTION 4 — "Tricks to Remember" (type: "list")
- 6-8 items with "term" = ट्रिक का नाम (Trick Title), "definition" = ट्रिक का विस्तृत विवरण (Detailed explanation of the trick with bold examples)

SECTION 5 — "Mistakes to Avoid" (type: "list")
- 6-8 items with "term" = अक्सर होने वाली गलती (Common Mistake), "definition" = सही नियम और स्पष्टीकरण (Correct rule, spelling or usage, and why students get confused)

SECTION 6 — "Point-wise Detailed Summary" (type: "list")
- 10-15 items with "term" = मुख्य बिंदु (Key Point Title), "definition" = संक्षेप में त्वरित रिवीजन बिंदु (Concise revision summary point)

ADDITIONAL REQUIREMENTS:
- "upscNotes": Include 4-6 strategy notes with type "tip" (परीक्षा रणनीति) and "trap" (परीक्षक के जाल - common traps set in MCQs)
- "keyTakeaways": Include 5-8 high-yield key takeaways (महत्वपूर्ण सूत्र / निष्कर्ष)

OUTPUT FORMAT — Return ONLY valid JSON with this exact structure:
{
  "sections": [
    {
      "title": "Detailed Brief Overview",
      "type": "table",
      "headers": ["विषय/पहल (Aspect)", "मुख्य विवरण (Key Details)"],
      "rows": [
        ["पहलू 1", "**मुख्य विवरण** नियम और उदाहरणों के साथ"],
        ["पहलू 2", "अन्य **महत्वपूर्ण** विवरण"]
      ]
    },
    {
      "title": "Detailed Explanation with Mnemonics",
      "type": "subcards",
      "items": [
        {
          "title": "उप-विषय 1 (**ट्रिक/सूत्र** के साथ)",
          "content": "• बिंदु 1 **बोल्ड** अक्षरों के साथ\\n• बिंदु 2\\n• **ट्रिक:** याद रखने की शार्ट-ट्रिक"
        }
      ]
    },
    {
      "title": "Comprehensive Data Tables",
      "type": "table",
      "headers": ["कॉलम 1", "कॉलम 2", "कॉलम 3"],
      "rows": [
        ["डेटा 1", "डेटा 2", "डेटा 3"]
      ]
    },
    {
      "title": "Tricks to Remember",
      "type": "list",
      "items": [
        {
          "term": "ट्रिक 1: शीर्षक",
          "definition": "ट्रिक का विस्तृत विवरण **बोल्ड** उदाहरणों के साथ"
        }
      ]
    },
    {
      "title": "Mistakes to Avoid",
      "type": "list",
      "items": [
        {
          "term": "गलती 1: सामान्य भ्रम",
          "definition": "सही नियम और स्पष्टीकरण ताकि परीक्षा में अंक न कटें"
        }
      ]
    },
    {
      "title": "Point-wise Detailed Summary",
      "type": "list",
      "items": [
        {
          "term": "मुख्य बिंदु 1",
          "definition": "त्वरित रिवीजन हेतु संक्षेप बिंदु **बोल्ड** शब्दों के साथ"
        }
      ]
    }
  ],
  "upscNotes": [
    {
      "type": "tip",
      "content": "परीक्षा हेतु महत्वपूर्ण रणनीति या शार्टकट"
    },
    {
      "type": "trap",
      "content": "परीक्षक द्वारा अक्सर विकल्पों में फंसाने का तरीका"
    }
  ],
  "keyTakeaways": [
    "उच्च-प्राथमिकता वाला निष्कर्ष 1",
    "उच्च-प्राथमिकता वाला निष्कर्ष 2"
  ]
}

IMPORTANT:
- The JSON structures and keys ("sections", "title", "type", "headers", "rows", "items", "term", "definition", "upscNotes", "keyTakeaways") MUST remain in English.
- The values (descriptions, tables, points, examples, titles) MUST be in Hindi to serve Hindi language students properly.
- NO paragraphs anywhere — only tables, lists, and subcards.`;
}

// ============================================================================
// HTML PAGE ASSEMBLER — 4-Tab Structure
// ============================================================================
function assemblePage(topic, conceptsData) {
    const now = new Date().toISOString();
    const canonicalUrl = `https://sjmaths.com/upsssc-pet/hindi/${encodeURIComponent(topic.dir)}/`;
    const title = `${topic.name} | UPSSSC PET Hindi | SJMaths`;
    const description = topic.description;
    const keywords = `UPSSSC PET, ${topic.name}, Hindi Grammar, ${topic.hindiName}, ${topic.keywords.join(', ')}`;

    return `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>${title}</title>
  <meta name="description" content="${description}">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <link rel="canonical" href="${canonicalUrl}">
  <meta name="keywords" content="${keywords}">
  <meta name="author" content="SJMaths">
  <link rel="icon" type="image/png" href="/favicon.png">
  <meta property="og:title" content="${title}">
  <meta property="og:description" content="${description}">
  <meta property="og:type" content="article">
  <meta property="og:url" content="${canonicalUrl}">
  <meta property="og:image" content="https://sjmaths.com/assets/icons/icon-512x512.png">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="${title}">
  <meta name="twitter:description" content="${description}">
  <meta name="twitter:image" content="https://sjmaths.com/assets/icons/icon-512x512.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Outfit:wght@500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/assets/css/main.min.css?v=4ba21ce7">
  <link rel="stylesheet" href="/assets/css/layout.min.css?v=e4922b08">
  <link rel="stylesheet" href="/assets/css/component.min.css?v=8c99f11f">
  <link rel="stylesheet" href="/assets/css/improved-ui.min.css?v=86f5556a">
  <link rel="stylesheet" href="/assets/css/pages.min.css?v=9e3bd560">
  <link rel="stylesheet" href="/assets/css/competitive-exam-guide.min.css?v=bcdc8e39">
  <style>
    :root { --up-primary: #0f172a; --up-accent: #d4af37; --up-accent-purple: #2980b9; --up-surface: rgba(255, 255, 255, 0.9); --up-radius-xl: 24px; --up-radius-lg: 16px; }
    html.lang-en .lang-hi, body.lang-en .lang-hi, html:not(.lang-hi) .lang-hi, body:not(.lang-hi):not(.lang-en) .lang-hi { display: none !important; }
    html.lang-hi .lang-en, body.lang-hi .lang-en { display: none !important; }
    .topic-container { max-width: 1150px; margin: 2rem auto; padding: 0 1.5rem 3rem; animation: upFadeIn 0.6s ease-out; }
    .breadcrumbs { margin-bottom: 1.5rem; font-size: 0.88rem; color: #64748b; background: rgba(255, 255, 255, 0.6); display: inline-block; padding: 0.6rem 1.2rem; border-radius: 999px; border: 1px solid rgba(0, 0, 0, 0.04); }
    .breadcrumbs a { color: var(--up-accent-purple); text-decoration: none; font-weight: 500; }
    .breadcrumbs a:hover { color: var(--up-accent); text-decoration: underline; }
    .breadcrumbs i { margin: 0 0.5rem; font-size: 0.7rem; color: #94a3b8; }
    .topic-header { background: linear-gradient(135deg, rgba(212, 175, 55, 0.03), rgba(41, 128, 185, 0.03), rgba(139, 92, 246, 0.03)); border: 1px solid rgba(212, 175, 55, 0.1); border-radius: var(--up-radius-xl); padding: 2.5rem; margin-bottom: 1.75rem; text-align: center; position: relative; overflow: hidden; backdrop-filter: blur(10px); }
    .topic-header h1 { font-family: 'Outfit', 'Inter', system-ui, sans-serif; font-size: clamp(2rem, 5vw, 2.75rem); font-weight: 800; background: linear-gradient(135deg, var(--up-primary) 0%, var(--up-accent) 50%, var(--up-accent-purple) 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; margin-bottom: 0.75rem; line-height: 1.2; letter-spacing: -0.02em; }
    .topic-desc { color: #475569; font-size: clamp(0.95rem, 2vw, 1.05rem); line-height: 1.7; max-width: 780px; margin: 0 auto; }
    .topic-meta-bar { display: flex; flex-wrap: wrap; gap: 1rem; justify-content: center; align-items: center; margin-top: 1.5rem; padding-top: 1.25rem; border-top: 1px solid rgba(0, 0, 0, 0.05); }
    .topic-difficulty { display: inline-flex; align-items: center; gap: 0.45rem; padding: 0.45rem 0.9rem; border-radius: 999px; font-size: 0.85rem; font-weight: 600; background: rgba(245, 158, 11, 0.1); color: #b45309; border: 1px solid rgba(245, 158, 11, 0.2); }
    .topic-study-time { display: inline-flex; align-items: center; gap: 0.45rem; padding: 0.45rem 0.9rem; border-radius: 999px; font-size: 0.85rem; font-weight: 600; color: #475569; background: rgba(100, 116, 139, 0.06); border: 1px solid rgba(100, 116, 139, 0.12); }
    .lang-toggle { display: inline-flex; background: rgba(212, 175, 55, 0.06); border: 1px solid rgba(212, 175, 55, 0.12); border-radius: 999px; padding: 0.2rem; gap: 0.2rem; }
    .lang-toggle button { border: none; background: transparent; color: #64748b; font-weight: 600; padding: 0.35rem 0.85rem; border-radius: 999px; cursor: pointer; font-size: 0.8rem; transition: all 0.2s ease; }
    .lang-toggle button.active { background: #ffffff; color: var(--up-accent-purple); box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08); }
    .study-tabs { display: flex; flex-wrap: wrap; gap: 0.5rem; padding: 0.55rem; background: var(--up-surface); border: 1px solid rgba(0, 0, 0, 0.05); border-radius: var(--up-radius-lg); margin-bottom: 2rem; position: sticky; top: 88px; z-index: 100; backdrop-filter: blur(16px); justify-content: center; }
    .tab-btn { border: none; background: transparent; color: #475569; padding: 0.65rem 1.1rem; border-radius: 999px; cursor: pointer; font-weight: 600; font-size: 0.9rem; font-family: 'Outfit', 'Inter', system-ui, sans-serif; display: inline-flex; align-items: center; gap: 0.5rem; transition: all 0.3s ease; white-space: nowrap; }
    .tab-btn:hover { background: rgba(212, 175, 55, 0.08); color: var(--up-accent-purple); }
    .tab-btn.active { background: linear-gradient(135deg, var(--up-accent), var(--up-accent-purple)); color: #ffffff; box-shadow: 0 8px 20px rgba(41, 128, 185, 0.25); }
    .topic-content { min-height: 400px; }
    .tab-panel { display: none; }
    .tab-panel.active { display: block; }
    table { width: 100%; border-collapse: collapse; margin: 1rem 0; font-size: 0.95rem; }
    th, td { padding: 0.75rem 1rem; text-align: left; border-bottom: 1px solid #e2e8f0; }
    th { background: #f1f5f9; font-weight: 600; color: var(--up-primary); }
    tr:hover { background: #f8fafc; }
    @media (max-width: 768px) {
      .study-tabs { flex-wrap: nowrap; overflow-x: auto; -webkit-overflow-scrolling: touch; padding: 0.4rem; scrollbar-width: none; justify-content: flex-start; }
      .study-tabs::-webkit-scrollbar { display: none; }
      .tab-btn { font-size: 0.85rem; padding: 0.5rem 0.9rem; }
      .topic-container { padding: 0 1rem 2rem; }
      .topic-header { padding: 1.5rem 1rem; }
    }
  </style>
</head>
<body>
  <div class="topic-container">
    <div class="breadcrumbs">
      <div class="breadcrumbs-path">
        <a href="/">Home</a> <i class="fas fa-chevron-right"></i>
        <a href="/upsssc-pet/">UPSSSC PET</a> <i class="fas fa-chevron-right"></i>
        <a href="/upsssc-pet/hindi/">General Hindi</a> <i class="fas fa-chevron-right"></i>
        <span><span class="lang-en">${topic.name}</span><span class="lang-hi">${topic.hindiName}</span></span>
      </div>
    </div>
    <div class="topic-header">
      <h1><span class="lang-en">${topic.name}</span><span class="lang-hi">${topic.hindiName}</span></h1>
      <p class="topic-desc"><span class="lang-en">${topic.description}</span><span class="lang-hi">${topic.hindiName} पर UPSSSC PET की विस्तृत गाइड।</span></p>
      <div class="topic-meta-bar">
        <span class="topic-difficulty"><i class="fas fa-signal"></i> <span class="lang-en">Medium</span><span class="lang-hi">मध्यम</span></span>
        <span class="topic-study-time"><i class="fas fa-clock"></i> <span class="lang-en">45 min total</span><span class="lang-hi">कुल 45 मिनट</span></span>
        <div class="lang-toggle">
          <button id="langEn" class="active" aria-pressed="true">EN</button>
          <button id="langHi" aria-pressed="false">हिन्दी</button>
        </div>
      </div>
    </div>
    <div class="study-tabs" role="tablist" aria-label="Topic resources">
      <button class="tab-btn active" data-tab="tab-concepts" role="tab" aria-selected="true">
        <i class="fas fa-book-open"></i> <span class="lang-en">1. Concepts & Theories</span><span class="lang-hi">1. अवधारणाएँ एवं सिद्धांत</span>
      </button>
      <button class="tab-btn" data-tab="tab-practice" role="tab" aria-selected="false">
        <i class="fas fa-list-check"></i> <span class="lang-en">2. Practice Questions</span><span class="lang-hi">2. अभ्यास प्रश्न</span>
      </button>
      <button class="tab-btn" data-tab="tab-pyqs" role="tab" aria-selected="false">
        <i class="fas fa-history"></i> <span class="lang-en">3. PYQs</span><span class="lang-hi">3. पिछले वर्ष के प्रश्न</span>
      </button>
      <button class="tab-btn" data-tab="tab-test" role="tab" aria-selected="false">
        <i class="fas fa-stopwatch"></i> <span class="lang-en">4. Mini Test</span><span class="lang-hi">4. मिनी टेस्ट</span>
      </button>
    </div>
    <div class="topic-content" id="topic-content"></div>
  </div>
  <script id="upsc-page-data" type="application/json">
  ${JSON.stringify({
        topicId: `upsssc-pet.hindi.${topic.dir}`,
        topicName: topic.name,
        hindiName: topic.hindiName,
        subject: 'General Hindi',
        subjectDir: 'hindi',
        concepts: conceptsData || null,
        practice: null,
        pyqs: null,
        test: null,
        version: { generator: 'v1', prompt: '1.0', translator: '1.0', normalizer: '1.0' },
        contentHash: 'sha256-placeholder',
        generatedAt: now
    }, null, 2)}
  </script>
  <script src="/assets/js/upsc-renderer.min.js" defer></script>
  <script src="/assets/js/main.min.js?v=10f0770d" defer data-cfasync="false"></script>
  <script>
    (function () {
      const btnEn = document.getElementById('langEn');
      const btnHi = document.getElementById('langHi');
      const apply = (lang) => {
        document.documentElement.classList.toggle('lang-hi', lang === 'hi');
        document.documentElement.classList.toggle('lang-en', lang !== 'hi');
        document.body.classList.toggle('lang-hi', lang === 'hi');
        document.body.classList.toggle('lang-en', lang !== 'hi');
        if (btnEn) btnEn.classList.toggle('active', lang !== 'hi');
        if (btnHi) btnHi.classList.toggle('active', lang === 'hi');
        if (btnEn) btnEn.setAttribute('aria-pressed', String(lang !== 'hi'));
        if (btnHi) btnHi.setAttribute('aria-pressed', String(lang === 'hi'));
        try { localStorage.setItem('sj_pref_lang', lang); } catch (e) { }
      };
      document.addEventListener('DOMContentLoaded', () => {
        const pref = (localStorage.getItem('sj_pref_lang') || 'en');
        apply(pref);
        if (btnEn) btnEn.addEventListener('click', () => apply('en'));
        if (btnHi) btnHi.addEventListener('click', () => apply('hi'));
      });
    })();
  </script>
</body>
</html>`;
}

// ============================================================================
// FALLBACK CONCEPTS DATA
// ============================================================================
function buildFallbackConcepts(topic) {
    return {
        sections: [
            {
                title: 'Detailed Brief Overview',
                type: 'table',
                headers: ['विषय/पहल (Aspect)', 'मुख्य विवरण (Key Details)'],
                rows: [
                    ['Topic', `**${topic.name}** (${topic.hindiName})`],
                    ['Subject', '**General Hindi (सामान्य हिन्दी)** for UPSSSC PET'],
                    ['Status', 'सामग्री तैयार की जा रही है — कृपया जल्द ही पुनः देखें।']
                ]
            }
        ],
        upscNotes: [
            { type: 'tip', content: `यह विषय UPSSSC PET सामान्य हिन्दी अनुभाग के लिए बहुत महत्वपूर्ण है। ${topic.hindiName} को ध्यान से पढ़ें।` }
        ],
        keyTakeaways: [
            `UPSSSC PET के लिए ${topic.hindiName} का गहन अध्ययन करें।`,
            'नियमों, परिभाषाओं और महत्वपूर्ण उदाहरणों पर ध्यान दें।',
            'पिछले वर्ष के प्रश्नों के साथ अभ्यास करें।'
        ]
    };
}

// ============================================================================
// MAIN GENERATION LOOP
// ============================================================================
async function main() {
    console.log('╔══════════════════════════════════════════════════════════════╗');
    console.log('║ UPSSSC PET Hindi — Concepts & Theories Tab Generator        ║');
    console.log('║ Model: gemini-3.6-flash                                      ║');
    console.log('╚══════════════════════════════════════════════════════════════╝\n');

    const totalTopics = HINDI_TOPICS.length;
    let successCount = 0;
    let failCount = 0;

    for (let i = 0; i < totalTopics; i++) {
        const topic = HINDI_TOPICS[i];
        console.log(`\n${'='.repeat(80)}`);
        console.log(`[${i + 1}/${totalTopics}] Processing: ${topic.name} (${topic.hindiName})`);
        console.log(`${'='.repeat(80)}`);

        const outputDir = path.join(process.cwd(), 'upsssc-pet', 'hindi', topic.dir);
        fs.mkdirSync(outputDir, { recursive: true });

        const tabsDir = path.join(outputDir, 'tabs');
        fs.mkdirSync(tabsDir, { recursive: true });

        let conceptsData = null;

        try {
            console.log('  📝 Generating concepts/theories content...');
            const prompt = buildConceptsPrompt(topic);
            const raw = await callGemini(prompt);
            const parsed = parseResponse(raw);

            if (!parsed.sections || !Array.isArray(parsed.sections) || parsed.sections.length === 0) {
                throw new Error('Generated content missing "sections" array');
            }

            // Ensure no paragraph type sections
            const paragraphSections = parsed.sections.filter(s => s.type === 'paragraph');
            if (paragraphSections.length > 0) {
                console.log('  ⚠️ Found paragraph sections — converting to list format...');
                parsed.sections = parsed.sections.map(section => {
                    if (section.type === 'paragraph') {
                        return {
                            title: section.title,
                            type: 'list',
                            items: [{ term: 'Key Point', definition: section.content || '' }]
                        };
                    }
                    return section;
                });
            }

            conceptsData = parsed;
            console.log('  ✅ Concepts content generated successfully!');

            fs.writeFileSync(path.join(tabsDir, 'concepts.json'), JSON.stringify(conceptsData, null, 2), 'utf8');
            console.log('  💾 Saved tabs/concepts.json');

            successCount++;
        } catch (err) {
            console.error(`  ❌ Failed to generate concepts: ${err.message}`);
            conceptsData = buildFallbackConcepts(topic);
            failCount++;
        }

        const html = assemblePage(topic, conceptsData);
        fs.writeFileSync(path.join(outputDir, 'index.html'), html, 'utf8');
        console.log('  💾 Saved index.html');

        fs.writeFileSync(path.join(outputDir, 'data.json'), JSON.stringify({ concepts: conceptsData, practice: null, pyqs: null, test: null }, null, 2), 'utf8');
        console.log('  💾 Saved data.json');

        console.log(`  🎉 Completed: ${topic.name}`);

        if (i < totalTopics - 1) {
            console.log(`  ⏳ Waiting ${REQUEST_DELAY_MS / 1000}s before next topic...`);
            await sleep(REQUEST_DELAY_MS);
        }
    }

    console.log(`\n${'='.repeat(80)}`);
    console.log(`📊 SUMMARY: ${successCount} succeeded, ${failCount} failed out of ${totalTopics} topics`);
    console.log(`${'='.repeat(80)}`);
    console.log('\nAll UPSSSC PET Hindi concepts/theories tabs generated successfully!');
}

main().catch(err => {
    console.error('Fatal error:', err);
    process.exit(1);
});
