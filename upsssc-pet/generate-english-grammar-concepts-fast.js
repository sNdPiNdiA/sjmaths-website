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
const REQUEST_DELAY_MS = 6000; // 6s between topics
const MAX_RETRIES = 5;
let currentModel = 'gemini-3.6-flash';

// ============================================================================
// UPSSSC PET ENGLISH GRAMMAR TOPICS (8 topics)
// ============================================================================
const ENGLISH_GRAMMAR_TOPICS = [
    {
        dir: 'parts-of-speech',
        name: 'Parts of Speech',
        hindiName: 'शब्द भेद (Parts of Speech)',
        description: 'Comprehensive guide on Parts of Speech: Nouns, Pronouns, Verbs, Adjectives, Adverbs, Prepositions, Conjunctions, and Interjections for UPSSSC PET.',
        keywords: ['Parts of Speech', 'Nouns', 'Pronouns', 'Verbs', 'Adjectives', 'Adverbs', 'Prepositions', 'Conjunctions', 'English Grammar']
    },
    {
        dir: 'tenses',
        name: 'Tenses and Time Aspect',
        hindiName: 'काल (Tenses)',
        description: 'Complete rules on Tenses (Present, Past, Future), time indicators, structural formulas, and common usage rules for UPSSSC PET.',
        keywords: ['Tenses', 'Present Tense', 'Past Tense', 'Future Tense', 'Verb Forms', 'Time and Tense', 'English Grammar']
    },
    {
        dir: 'articles-determiners',
        name: 'Articles and Determiners',
        hindiName: 'आर्टिकल्स एवं डिटरमाइनर्स (Articles & Determiners)',
        description: 'Detailed usage of Articles (A, An, The), Omission of Articles, and Quantifiers/Determiners with rules and examples for UPSSSC PET.',
        keywords: ['Articles', 'Determiners', 'Use of A An The', 'Omission of Articles', 'Quantifiers', 'English Grammar']
    },
    {
        dir: 'subject-verb-agreement',
        name: 'Subject-Verb Agreement',
        hindiName: 'कर्त्ता-क्रिया संगति (Subject-Verb Agreement)',
        description: 'Golden rules of Subject-Verb Agreement / Syntax, singular-plural rules, collective nouns, compound subjects, and exceptions for UPSSSC PET.',
        keywords: ['Subject Verb Agreement', 'Syntax', 'Singular Plural Rules', 'Grammar Rules', 'Error Spotting', 'English Grammar']
    },
    {
        dir: 'voice-active-passive',
        name: 'Active and Passive Voice',
        hindiName: 'कर्तृवाच्य एवं कर्मवाच्य (Active & Passive Voice)',
        description: 'Transformation rules from Active to Passive Voice across all tenses, modal verbs, imperatives, and interrogatives for UPSSSC PET.',
        keywords: ['Active Voice', 'Passive Voice', 'Voice Change', 'Sentence Transformation', 'English Grammar', 'UPSSSC PET']
    },
    {
        dir: 'direct-indirect-speech',
        name: 'Direct and Indirect Speech',
        hindiName: 'प्रत्यक्ष एवं अप्रत्यक्ष कथन (Direct & Indirect Speech)',
        description: 'Narration change rules for Direct and Indirect Speech: reporting verbs, tense changes, pronoun shifts, and interrogative/imperative transformations for UPSSSC PET.',
        keywords: ['Direct Speech', 'Indirect Speech', 'Narration', 'Reporting Verb', 'Sentence Conversion', 'English Grammar']
    },
    {
        dir: 'vocabulary-synonyms-antonyms',
        name: 'Vocabulary: Synonyms & Antonyms',
        hindiName: 'शब्दावली: पर्यायवाची एवं विलोम (Synonyms & Antonyms)',
        description: 'High-yield vocabulary list for UPSSSC PET: Synonyms, Antonyms, Commonly Confused Words, and Word Roots with tips & memory tricks.',
        keywords: ['Synonyms', 'Antonyms', 'Vocabulary', 'Word Power', 'English Vocabulary', 'UPSSSC PET English']
    },
    {
        dir: 'one-word-substitution-idioms',
        name: 'Idioms, Phrases & One Word Substitution',
        hindiName: 'मुहावरे एवं एक शब्द प्रतिस्थापन (Idioms & One Word Substitution)',
        description: 'Important Idioms, Phrases, and One Word Substitutions frequently tested in UPSSSC PET and UP state exams with meanings and usage.',
        keywords: ['Idioms', 'Phrases', 'One Word Substitution', 'Vocabulary Tricks', 'English Grammar', 'UPSSSC PET']
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
                const wait = 8000 * Math.pow(2, attempt - 1);
                console.log(`  ⏳ Waiting ${wait / 1000}s...`);
                await sleep(wait);
                continue;
            }

            if (res.status === 503) {
                const wait = 12000;
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
            await sleep(3000);
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

    if (cleaned.startsWith('```json')) cleaned = cleaned.replace(/^```json\s*/, '').replace(/\s*```$/, '');
    else if (cleaned.startsWith('```')) cleaned = cleaned.replace(/^```\s*/, '').replace(/\s*```$/, '');

    cleaned = cleaned.replace(/[\u2018\u2019]/g, "'").replace(/[\u201c\u201d]/g, '"');

    try { return JSON.parse(cleaned); } catch (err) { }

    const jsonMatch = cleaned.match(/[\{\[][\s\S]*[\}\]]/);
    if (jsonMatch) {
        try { return JSON.parse(jsonMatch[0]); } catch (e) { }
    }

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
        try { return JSON.parse(partial); } catch (e) { }
    }

    throw new Error('No valid JSON found in response');
}

// ============================================================================
// PROMPT BUILDER — Concepts/Theories, Tips & Tricks (Exhaustive & Detailed)
// ============================================================================
function buildConceptsPrompt(topic) {
    return `You are an expert Senior English Grammar Faculty member for UPSSSC PET (Preliminary Eligibility Test) exam preparation.
Create ULTRA-COMPREHENSIVE, SEO-OPTIMIZED, DETAILED concept notes with tips and tricks for the English Grammar topic: "${topic.name}" (${topic.hindiName}).

TOPIC CONTEXT:
- Subject: General English (सामान्य अंग्रेजी)
- Exam: UPSSSC PET
- Topic Directory: ${topic.dir}
- Keywords to target: ${topic.keywords.join(', ')}

CRITICAL FORMAT RULES — NO PARAGRAPHS ALLOWED:
1. **STRICTLY NO PARAGRAPHS** — Do NOT use the "paragraph" type anywhere. Every section must be a table, subcards, or list.
2. Content must be **point-wise, bulleted, tabular, and structured** for rapid exam revision.
3. Use **bold** for key rules, definitions, terms, and examples within table cells and list items.
4. Content must be **comprehensive and exam-focused** — cover ALL important rules, golden formulas, classic examples, exceptions, and error-spotting patterns asked in UPSSSC PET.
5. Provide clear English explanations with Hindi meanings/terms in brackets where helpful for Hindi-medium candidates.

REQUIRED SECTION STRUCTURE (in this exact order):

SECTION 1 — "Detailed Brief Overview" (type: "table")
- A comprehensive overview table with 8-10 rows covering: What, Scope in UPSSSC PET, Core Functional Categories, Fundamental Rule Formulas, Exam Weightage, and Key Types.
- Headers: ["Aspect", "Key Details"]

SECTION 2 — "Core Rules & Detailed Explanations" (type: "subcards")
- 5-7 subcards, each covering a major sub-topic or golden grammar rule.
- Each subcard must have a clear title and detailed point-wise content with 5+ concrete example sentences (showing Incorrect vs Correct where applicable).
- Include 2-3 memory tricks/mnemonics (Shortcuts & Formulas) within these subcards.

SECTION 3 — "Comprehensive Rule & Classification Tables" (type: "table")
- 3-4 detailed tables with 8-12 rows each covering:
  a) Important Rules with Conditions and Correct Usage Examples
  b) Exceptions & Confusing Edge Cases
  c) Formula / Transformation Patterns
  d) Categorized Word Lists / Usage Sets

SECTION 4 — "Tricks & Shortcuts to Remember" (type: "list")
- 6-8 items with "term" = trick title, "definition" = detailed trick explanation with bold example sentences

SECTION 5 — "Common Mistakes to Avoid" (type: "list")
- 6-8 items with "term" = common grammatical mistake/trap, "definition" = correct rule and explanation of why candidates get confused

SECTION 6 — "Point-wise Detailed Summary" (type: "list")
- 10-15 items with "term" = key rule title, "definition" = concise point-wise revision summary

ADDITIONAL REQUIREMENTS:
- "upscNotes": Include 4-6 notes with type "tip" (exam strategy) and "trap" (common traps set in MCQs)
- "keyTakeaways": Include 5-8 concise, high-yield key takeaways

OUTPUT FORMAT — Return ONLY valid JSON with this exact structure:
{
  "sections": [
    {
      "title": "Detailed Brief Overview",
      "type": "table",
      "headers": ["Aspect", "Key Details"],
      "rows": [
        ["Aspect 1", "**Key detail** with bold important terms"],
        ["Aspect 2", "Another **important** detail"]
      ]
    },
    {
      "title": "Core Rules & Detailed Explanations",
      "type": "subcards",
      "items": [
        {
          "title": "Rule 1 with **Mnemonic / Trick**",
          "content": "• Point 1 with **bold** terms\\n• Point 2 with **bold** terms\\n• **Example 1:** Incorrect: ... | **Correct:** ...\\n• **Tip/Trick:** Formula to remember"
        }
      ]
    },
    {
      "title": "Comprehensive Rule & Classification Tables",
      "type": "table",
      "headers": ["Category / Rule", "Grammatical Condition", "Examples & Usage"],
      "rows": [
        ["Data 1", "Data 2", "Data 3"]
      ]
    },
    {
      "title": "Tricks & Shortcuts to Remember",
      "type": "list",
      "items": [
        {
          "term": "Trick 1: Title",
          "definition": "Detailed explanation of the trick with **bold** key terms"
        }
      ]
    },
    {
      "title": "Common Mistakes to Avoid",
      "type": "list",
      "items": [
        {
          "term": "Mistake 1: Common error",
          "definition": "Correct fact and why students get confused"
        }
      ]
    },
    {
      "title": "Point-wise Detailed Summary",
      "type": "list",
      "items": [
        {
          "term": "Key Point 1",
          "definition": "Concise summary point with **bold** key terms"
        }
      ]
    }
  ],
  "upscNotes": [
    {
      "type": "tip",
      "content": "Exam strategy tip for UPSSSC PET"
    },
    {
      "type": "trap",
      "content": "Common trap students fall into"
    }
  ],
  "keyTakeaways": [
    "High-yield takeaway 1",
    "High-yield takeaway 2"
  ]
}`;
}

// ============================================================================
// HTML PAGE ASSEMBLER — 4-Tab Structure
// ============================================================================
function assemblePage(topic, conceptsData) {
    const now = new Date().toISOString();
    const canonicalUrl = `https://sjmaths.com/upsssc-pet/english/english-grammar/${topic.dir}/`;
    const title = `${topic.name} | UPSSSC PET English Grammar | SJMaths`;
    const description = topic.description;
    const keywords = `UPSSSC PET, ${topic.name}, English Grammar, ${topic.hindiName}, ${topic.keywords.join(', ')}`;

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
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <style>
    :root { --up-primary: #0f172a; --up-accent: #3b82f6; --up-accent-purple: #8b5cf6; --up-surface: rgba(255, 255, 255, 0.9); --up-radius-xl: 24px; --up-radius-lg: 16px; }
    html.lang-en .lang-hi, body.lang-en .lang-hi, html:not(.lang-hi) .lang-hi, body:not(.lang-hi):not(.lang-en) .lang-hi { display: none !important; }
    html.lang-hi .lang-en, body.lang-hi .lang-en { display: none !important; }
    .topic-container { max-width: 1150px; margin: 2rem auto; padding: 0 1.5rem 3rem; animation: upFadeIn 0.6s ease-out; }
    .breadcrumbs { margin-bottom: 1.5rem; font-size: 0.88rem; color: #64748b; background: rgba(255, 255, 255, 0.6); display: inline-block; padding: 0.6rem 1.2rem; border-radius: 999px; border: 1px solid rgba(0, 0, 0, 0.04); }
    .breadcrumbs a { color: var(--up-accent); text-decoration: none; font-weight: 500; }
    .breadcrumbs a:hover { color: var(--up-accent-purple); text-decoration: underline; }
    .breadcrumbs i { margin: 0 0.5rem; font-size: 0.7rem; color: #94a3b8; }
    .topic-header { background: linear-gradient(135deg, rgba(59, 130, 246, 0.04), rgba(139, 92, 246, 0.04), rgba(15, 23, 42, 0.02)); border: 1px solid rgba(59, 130, 246, 0.12); border-radius: var(--up-radius-xl); padding: 2.5rem; margin-bottom: 1.75rem; text-align: center; position: relative; overflow: hidden; backdrop-filter: blur(10px); }
    .topic-header h1 { font-family: 'Outfit', 'Inter', system-ui, sans-serif; font-size: clamp(2rem, 5vw, 2.75rem); font-weight: 800; background: linear-gradient(135deg, var(--up-primary) 0%, var(--up-accent) 50%, var(--up-accent-purple) 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; margin-bottom: 0.75rem; line-height: 1.2; letter-spacing: -0.02em; }
    .topic-desc { color: #475569; font-size: clamp(0.95rem, 2vw, 1.05rem); line-height: 1.7; max-width: 780px; margin: 0 auto; }
    .topic-meta-bar { display: flex; flex-wrap: wrap; gap: 1rem; justify-content: center; align-items: center; margin-top: 1.5rem; padding-top: 1.25rem; border-top: 1px solid rgba(0, 0, 0, 0.05); }
    .topic-difficulty { display: inline-flex; align-items: center; gap: 0.45rem; padding: 0.45rem 0.9rem; border-radius: 999px; font-size: 0.85rem; font-weight: 600; background: rgba(59, 130, 246, 0.1); color: #1d4ed8; border: 1px solid rgba(59, 130, 246, 0.2); }
    .topic-study-time { display: inline-flex; align-items: center; gap: 0.45rem; padding: 0.45rem 0.9rem; border-radius: 999px; font-size: 0.85rem; font-weight: 600; color: #475569; background: rgba(100, 116, 139, 0.06); border: 1px solid rgba(100, 116, 139, 0.12); }
    .lang-toggle { display: inline-flex; background: rgba(59, 130, 246, 0.06); border: 1px solid rgba(59, 130, 246, 0.12); border-radius: 999px; padding: 0.2rem; gap: 0.2rem; }
    .lang-toggle button { border: none; background: transparent; color: #64748b; font-weight: 600; padding: 0.35rem 0.85rem; border-radius: 999px; cursor: pointer; font-size: 0.8rem; transition: all 0.2s ease; }
    .lang-toggle button.active { background: #ffffff; color: var(--up-accent); box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08); }
    .study-tabs { display: flex; flex-wrap: wrap; gap: 0.5rem; padding: 0.55rem; background: var(--up-surface); border: 1px solid rgba(0, 0, 0, 0.05); border-radius: var(--up-radius-lg); margin-bottom: 2rem; position: sticky; top: 88px; z-index: 100; backdrop-filter: blur(16px); justify-content: center; }
    .tab-btn { border: none; background: transparent; color: #475569; padding: 0.65rem 1.1rem; border-radius: 999px; cursor: pointer; font-weight: 600; font-size: 0.9rem; font-family: 'Outfit', 'Inter', system-ui, sans-serif; display: inline-flex; align-items: center; gap: 0.5rem; transition: all 0.3s ease; white-space: nowrap; }
    .tab-btn:hover { background: rgba(59, 130, 246, 0.08); color: var(--up-accent); }
    .tab-btn.active { background: linear-gradient(135deg, var(--up-accent), var(--up-accent-purple)); color: #ffffff; box-shadow: 0 8px 20px rgba(59, 130, 246, 0.25); }
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
        <a href="/upsssc-pet/english/">English</a> <i class="fas fa-chevron-right"></i>
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
        topicId: `upsssc-pet.english.english-grammar.${topic.dir}`,
        topicName: topic.name,
        hindiName: topic.hindiName,
        subject: 'General English',
        subjectDir: 'english',
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
// FALLBACK GENERATOR
// ============================================================================
function buildFallbackConcepts(topic) {
    return {
        sections: [
            {
                title: 'Detailed Brief Overview',
                type: 'table',
                headers: ['Aspect', 'Key Details'],
                rows: [
                    ['Topic', `**${topic.name}** (${topic.hindiName})`],
                    ['Subject', '**General English** for UPSSSC PET'],
                    ['Status', 'Comprehensive concepts & theory guide under active generation']
                ]
            }
        ],
        upscNotes: [
            { type: 'tip', content: `Study ${topic.name} thoroughly for UPSSSC PET English Grammar section.` }
        ],
        keyTakeaways: [
            `Master all core rules of ${topic.name} for UPSSSC PET.`
        ]
    };
}

// ============================================================================
// MAIN GENERATION LOOP
// ============================================================================
async function main() {
    console.log('╔══════════════════════════════════════════════════════════════╗');
    console.log('║ UPSSSC PET English Grammar — Concepts & Theories Generator  ║');
    console.log('║ Model: gemini-3.6-flash                                      ║');
    console.log('╚══════════════════════════════════════════════════════════════╝\n');

    const totalTopics = ENGLISH_GRAMMAR_TOPICS.length;
    let successCount = 0;
    let failCount = 0;

    for (let i = 0; i < totalTopics; i++) {
        const topic = ENGLISH_GRAMMAR_TOPICS[i];
        console.log(`\n${'='.repeat(80)}`);
        console.log(`[${i + 1}/${totalTopics}] Generating Concepts/Theories for: ${topic.name} (${topic.hindiName})`);
        console.log(`${'='.repeat(80)}`);

        const outputDir = path.join(process.cwd(), 'upsssc-pet', 'english', 'english-grammar', topic.dir);
        fs.mkdirSync(outputDir, { recursive: true });

        const tabsDir = path.join(outputDir, 'tabs');
        fs.mkdirSync(tabsDir, { recursive: true });

        let conceptsData = null;

        try {
            console.log('  📝 Generating detailed concepts/theories content...');
            const prompt = buildConceptsPrompt(topic);
            const raw = await callGemini(prompt);
            conceptsData = parseResponse(raw);

            if (!conceptsData.sections || !Array.isArray(conceptsData.sections) || conceptsData.sections.length === 0) {
                throw new Error('Generated content missing "sections" array');
            }

            console.log('  ✅ Concepts content generated successfully!');

            fs.writeFileSync(path.join(tabsDir, 'concepts.json'), JSON.stringify(conceptsData, null, 2), 'utf8');
            console.log('  💾 Saved tabs/concepts.json');

            // Read existing data.json or create new one
            const dataPath = path.join(outputDir, 'data.json');
            let data = { concepts: conceptsData, practice: null, pyqs: null, test: null };
            if (fs.existsSync(dataPath)) {
                try {
                    const existing = JSON.parse(fs.readFileSync(dataPath, 'utf8'));
                    data = { ...existing, concepts: conceptsData };
                } catch (e) { }
            }
            fs.writeFileSync(dataPath, JSON.stringify(data, null, 2), 'utf8');
            console.log('  💾 Saved data.json');

            // Save index.html
            const html = assemblePage(topic, conceptsData);
            fs.writeFileSync(path.join(outputDir, 'index.html'), html, 'utf8');
            console.log('  💾 Saved index.html');

            successCount++;
        } catch (err) {
            console.error(`  ❌ Failed to generate concepts: ${err.message}`);
            conceptsData = buildFallbackConcepts(topic);
            fs.writeFileSync(path.join(tabsDir, 'concepts.json'), JSON.stringify(conceptsData, null, 2), 'utf8');
            const dataPath = path.join(outputDir, 'data.json');
            fs.writeFileSync(dataPath, JSON.stringify({ concepts: conceptsData, practice: null, pyqs: null, test: null }, null, 2), 'utf8');
            const html = assemblePage(topic, conceptsData);
            fs.writeFileSync(path.join(outputDir, 'index.html'), html, 'utf8');
            failCount++;
        }

        console.log(`  🎉 Completed: ${topic.name}`);

        if (i < totalTopics - 1) {
            console.log(`  ⏳ Waiting ${REQUEST_DELAY_MS / 1000}s before next topic...`);
            await sleep(REQUEST_DELAY_MS);
        }
    }

    console.log(`\n${'='.repeat(80)}`);
    console.log(`📊 SUMMARY: ${successCount} succeeded, ${failCount} failed out of ${totalTopics} topics`);
    console.log(`${'='.repeat(80)}`);
    console.log('\nAll UPSSSC PET English Grammar concepts/theories generated successfully!');
}

main().catch(err => {
    console.error('Fatal error:', err);
    process.exit(1);
});
