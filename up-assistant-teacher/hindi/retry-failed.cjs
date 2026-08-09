const fs = require('fs');
const path = require('path');

// ============================================================================
// ENV LOADER
// ============================================================================
if (fs.existsSync('.env')) {
    const envContent = fs.readFileSync('.env', 'utf8');
    for (const line of envContent.split('\n')) {
        const match = line.match(/^\s*([\w.-]+)\s*=\s*(.*)?(\s*)$/);
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
    console.error('GEMINI_API_KEY is not set.');
    process.exit(1);
}

// ============================================================================
// CONSTANTS — use higher-capacity model for large responses
// ============================================================================
const REQUEST_DELAY_MS = 25000;
const MAX_RETRIES = 6;
let currentModel = 'gemini-3.5-flash-lite';

// ============================================================================
// THE 11 FAILED TOPICS
// ============================================================================
const FAILED_TOPICS = [
    // Only the 4 topics still needing content (others already succeeded)
    {
        dir: 'jayashankara-parasaada-kaamaayanaee-sakandagaupata',
        name: 'Jaishankar Prasad - Kamayani, Skandagupta (जयशंकर प्रसाद)',
        hindiName: 'जयशंकर प्रसाद - कामायनी, स्कंदगुप्त',
        description: 'Jaishankar Prasad — Chhaayavaad pillar, Kamayani (Shraddha-Manu-Ida), Skandagupta, Chandragupta — themes, characters, and literary significance.',
        keywords: ['Jaishankar Prasad', 'Kamayani', 'Skandagupta', 'Chandragupta', 'Chhaayavaad', 'Hindi Mahakavya', 'Hindi Drama'],
        type: 'literature'
    },
    {
        dir: 'kavai-paraichaya-va-kaavaya-gauna',
        name: 'Kavi Parichay aur Kavya Gun (कवि परिचय)',
        hindiName: 'कवि परिचय व काव्य गुण',
        description: 'Hindi Kavi Parichay (Poet Introduction) and Kavya Gun (Poetic Qualities) — the three Guna: Madhura, Ojasvi, Prasad; how they manifest in poetry; linking poets to their Guna.',
        keywords: ['Kavi Parichay', 'Kavya Gun', 'Madhura Gun', 'Ojasvi Gun', 'Prasad Gun', 'Poet Introduction Hindi', 'Hindi Poetry UP'],
        type: 'poetry'
    },
    {
        dir: 'samakaalaeena-saahaitaya-haraivansha-raaya-bachachana-kamalaeshavara',
        name: 'Samkalin Sahitya - Harivansh Rai Bachchan, Kamleshwar (समकालीन साहित्य)',
        hindiName: 'समकालीन साहित्य - हरिवंश राय बच्चन, कमलेश्वर',
        description: 'Contemporary Hindi Literature — Harivansh Rai Bachchan (Madhushala, Madhubala), Kamleshwar (Kitne Pakistan), Nayi Kavita, Nayi Kahani movement.',
        keywords: ['Harivansh Rai Bachchan', 'Madhushala', 'Kamleshwar', 'Kitne Pakistan', 'Nayi Kavita', 'Nayi Kahani', 'Contemporary Hindi Literature'],
        type: 'literature'
    },
    {
        dir: 'saravanaama-vaibhakatai-evan-kaaraka',
        name: 'Sarvanam - Vibhakti aur Karak (सर्वनाम)',
        hindiName: 'सर्वनाम - विभक्ति एवं कारक',
        description: 'Hindi Sarvanam (Pronoun) — types, vibhakti (case markers), karak (case system), and their grammatical role in sentences.',
        keywords: ['Sarvanam', 'Pronoun Hindi', 'Vibhakti', 'Karak', 'Hindi Grammar UP Assistant Teacher'],
        type: 'grammar'
    }
    // shabada-rachanaa, tarautai, varatanaee, yashapaala — already succeeded
];

// ============================================================================
// PLACEHOLDER — lines kept for structure
// ============================================================================
const _UNUSED = [
    {
        dir: 'shabada-rachanaa-va-shabada-bhandaara',
        name: 'Shabd Rachna aur Shabd Bhandar (शब्द भंडार)',
        hindiName: 'शब्द रचना व शब्द भंडार',
        description: 'Hindi Shabd Rachna (Word Formation) and Shabd Bhandar (Vocabulary) — Tatsam, Tadbhav, Deshaj, Videshi words, synonyms, antonyms, Anekarthi, Paryayvachi.',
        keywords: ['Shabd Rachna', 'Shabd Bhandar', 'Tatsam Tadbhav', 'Paryayvachi Shabd', 'Vilom Shabd', 'Anekarthi Shabd', 'Hindi Vocabulary'],
        type: 'grammar'
    },
    {
        dir: 'tarautai-evan-unakaa-saudhaara',
        name: 'Truti aur Unka Sudhar (त्रुटि सुधार)',
        hindiName: 'त्रुटि एवं उनका सुधार',
        description: 'Hindi Truti Sudhar (Error Correction) — common grammatical errors in Hindi sentences, rules for correction, gender/number/case/tense errors.',
        keywords: ['Truti Sudhar', 'Error Correction Hindi', 'Hindi Grammar Mistakes', 'Vaakya Shuddhi', 'UP Assistant Teacher Hindi'],
        type: 'grammar'
    },
    {
        dir: 'varatanaee-va-vaakaya-shaudadhai',
        name: 'Vartani aur Vakya Shuddhi (वर्तनी व शुद्धि)',
        hindiName: 'वर्तनी व वाक्य शुद्धि',
        description: 'Hindi Vartani (Spelling) and Vakya Shuddhi (Sentence Correction) — rules of correct Hindi spelling, common Vartani errors, and sentence purity.',
        keywords: ['Vartani', 'Vakya Shuddhi', 'Hindi Spelling', 'Hindi Sentence Correction', 'Shuddh Hindi', 'Hindi Grammar UP'],
        type: 'grammar'
    },
    {
        dir: 'yashapaala-jhaoothaa-sacha-daivayaa',
        name: 'Yashpal - Jhootha Sach, Divya (यशपाल)',
        hindiName: 'यशपाल - झूठा सच, दिव्या',
        description: 'Yashpal — progressive writer, Jhootha Sach (partition saga), Divya, Dada Comrade — themes of partition, social inequality, Marxism, and historical fiction.',
        keywords: ['Yashpal', 'Jhootha Sach', 'Divya', 'Dada Comrade', 'Progressive Hindi Fiction', 'Partition Novel Hindi', 'Pragativad'],
        type: 'literature'
    }
];

// ============================================================================
// UTILITY
// ============================================================================
function sleep(ms) { return new Promise(resolve => setTimeout(resolve, ms)); }

// ============================================================================
// GEMINI API CLIENT
// ============================================================================
async function callGemini(prompt, retries = MAX_RETRIES) {
    for (let attempt = 1; attempt <= retries; attempt++) {
        try {
            const url = `https://generativelanguage.googleapis.com/v1beta/models/${currentModel}:generateContent?key=${apiKey}`;
            const res = await fetch(url, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    contents: [{ parts: [{ text: prompt }] }],
                    generationConfig: {
                        temperature: 0.7,
                        maxOutputTokens: 65536,
                        topP: 0.95,
                    },
                }),
            });

            if (res.status === 429 || res.status === 403) {
                const wait = 15000 * Math.pow(2, attempt - 1);
                console.log(`  ⚠️ Rate limited. Waiting ${wait / 1000}s...`);
                await sleep(wait);
                continue;
            }
            if (res.status === 503) {
                console.log(`  ⏳ 503 unavailable. Waiting ${REQUEST_DELAY_MS * 2 / 1000}s...`);
                await sleep(REQUEST_DELAY_MS * 2);
                continue;
            }
            if (!res.ok) {
                const errBody = await res.text();
                throw new Error(`API error ${res.status}: ${errBody.substring(0, 200)}`);
            }

            const data = await res.json();
            const text = data?.candidates?.[0]?.content?.parts?.[0]?.text || '';
            if (!text || text.trim().length === 0) throw new Error('Empty response');
            return text;
        } catch (err) {
            if (attempt === retries) throw err;
            console.log(`  ⚠️ Retry ${attempt}/${retries}: ${err.message}`);
            await sleep(5000);
        }
    }
    throw new Error('Max retries exceeded');
}

// ============================================================================
// ROBUST JSON PARSER — fixes raw newlines in strings, trailing commas, truncation
// ============================================================================

/**
 * Walk through a JSON-like string character by character and escape any raw
 * newline / carriage-return / tab characters that appear *inside* a JSON string
 * value, which the LLM sometimes emits without proper \n escaping.
 */
function fixRawControlCharsInStrings(s) {
    let out = '';
    let inString = false;
    let esc = false;
    for (let i = 0; i < s.length; i++) {
        const ch = s[i];
        if (esc) { out += ch; esc = false; continue; }
        if (ch === '\\') { out += ch; esc = true; continue; }
        if (ch === '"') { inString = !inString; out += ch; continue; }
        if (inString) {
            if (ch === '\n') { out += '\\n'; continue; }
            if (ch === '\r') { out += '\\r'; continue; }
            if (ch === '\t') { out += '\\t'; continue; }
        }
        out += ch;
    }
    return out;
}

function parseResponse(raw) {
    let cleaned = raw.trim();
    if (cleaned.startsWith('```json')) cleaned = cleaned.replace(/^```json\s*/, '').replace(/\s*```$/, '');
    else if (cleaned.startsWith('```')) cleaned = cleaned.replace(/^```\s*/, '').replace(/\s*```$/, '');

    // Normalize smart quotes
    cleaned = cleaned.replace(/[\u2018\u2019]/g, "'").replace(/[\u201c\u201d]/g, '"');

    // Pipeline of fixes to apply before each parse attempt
    const fix = s => {
        s = fixRawControlCharsInStrings(s); // escape raw newlines inside strings
        s = s.replace(/,(\s*[}\]])/g, '$1'); // remove trailing commas
        return s;
    };

    try { return JSON.parse(fix(cleaned)); } catch (e) { }

    // Extract JSON block
    const jsonMatch = cleaned.match(/\{[\s\S]*\}/);
    if (jsonMatch) {
        let block = fix(jsonMatch[0]);
        try { return JSON.parse(block); } catch (e) {
            // Close unclosed structures
            let opens = 0, closes = 0, openArr = 0, closeArr = 0;
            let inString = false, esc = false;
            for (let i = 0; i < block.length; i++) {
                const ch = block[i];
                if (esc) { esc = false; continue; }
                if (ch === '\\') { esc = true; continue; }
                if (ch === '"') { inString = !inString; continue; }
                if (inString) continue;
                if (ch === '{') opens++;
                else if (ch === '}') closes++;
                else if (ch === '[') openArr++;
                else if (ch === ']') closeArr++;
            }
            if (inString) block += '"';
            block = block.replace(/,\s*$/, '');
            while (openArr > closeArr) { block += ']'; closeArr++; }
            while (opens > closes) { block += '}'; closes++; }
            block = block.replace(/,(\s*[}\]])/g, '$1');
            try { return JSON.parse(block); } catch (e2) {
                console.error('❌ Could not repair JSON. First 400 chars:\n', block.substring(0, 400));
                throw new Error('JSON repair failed: ' + e2.message);
            }
        }
    }
    throw new Error('No JSON object found in response');
}

// ============================================================================
// PROMPT — Compact version to stay within token limits
// ============================================================================
function buildCompactPrompt(topic) {
    let focusHint = '';
    if (topic.type === 'literature') {
        focusHint = `Focus: author biography, literary Yug/period, major works (titles, year, genre), key themes, important characters/lines, and exam significance.`;
    } else if (topic.type === 'grammar') {
        focusHint = `Focus: definition, all types/Bhed with Hindi examples, rules, identification steps, comparison of confused types, and common exam errors.`;
    } else if (topic.type === 'prose') {
        focusHint = `Focus: what the skill tests, step-by-step answering approach, question types, marking pattern, common errors, and dos/don'ts.`;
    } else {
        focusHint = `Focus: core concept definition, all types/forms with examples from classic poems, identification signals, and exam question patterns.`;
    }

    return `You are an expert for UP Assistant Teacher (Hindi) exam prep. Generate EXAM-FOCUSED concept notes for: "${topic.name}" (${topic.hindiName}).

${focusHint}

RULES (MANDATORY):
- STRICTLY NO PARAGRAPHS — only table, list, subcards types.
- ENGLISH only for all text. Hindi terms may appear bolded within English.
- Keep each section concise but complete.

Return ONLY valid JSON (no markdown fences) with exactly this structure:
{
  "sections": [
    {
      "title": "Detailed Brief Overview",
      "type": "table",
      "headers": ["Aspect", "Key Details"],
      "rows": [["row1col1","row1col2"],["row2col1","row2col2"]]
    },
    {
      "title": "Concepts and Theories",
      "type": "subcards",
      "items": [
        {"title": "Subcard Title","content": "• Point 1\\n• Point 2\\n• **Mnemonic:** ..."}
      ]
    },
    {
      "title": "Important Facts and Data",
      "type": "table",
      "headers": ["Col1","Col2","Col3"],
      "rows": [["d1","d2","d3"]]
    },
    {
      "title": "Tricks to Remember",
      "type": "list",
      "items": [{"term": "Trick Title","definition": "Explanation"}]
    },
    {
      "title": "Mistakes to Avoid",
      "type": "list",
      "items": [{"term": "Common Error","definition": "Correct rule"}]
    },
    {
      "title": "Point-wise Detailed Summary",
      "type": "list",
      "items": [{"term": "Key Point","definition": "Summary"}]
    }
  ],
  "upscNotes": [
    {"type": "tip","content": "Exam tip"},
    {"type": "trap","content": "Common trap"}
  ],
  "keyTakeaways": ["Takeaway 1","Takeaway 2","Takeaway 3"]
}

Requirements:
- Overview: 6-8 rows
- Subcards: 4-5 subcards, each with 4-6 bullet points + 1 mnemonic
- Facts table: 6-8 rows
- Tricks: 5-6 items
- Mistakes: 5-6 items  
- Summary: 8-10 items
- upscNotes: 3 tips + 2 traps
- keyTakeaways: 4-5 items
Topic keywords: ${topic.keywords.join(', ')}`;
}

// ============================================================================
// FALLBACK
// ============================================================================
function buildFallback(topic) {
    return {
        sections: [{
            title: 'Detailed Brief Overview', type: 'table',
            headers: ['Aspect', 'Key Details'],
            rows: [
                ['Topic', `**${topic.name}**`],
                ['Subject', '**Hindi** for UP Assistant Teacher'],
                ['Status', 'Content under preparation — check back soon']
            ]
        }],
        upscNotes: [{ type: 'tip', content: `Study ${topic.name} for UP Assistant Teacher.` }],
        keyTakeaways: [`Study ${topic.name} thoroughly`, 'Focus on key concepts', 'Practice with past questions']
    };
}

// ============================================================================
// HTML assembler (same template as main generator)
// ============================================================================
function assemblePage(topic, conceptsData) {
    const now = new Date().toISOString();
    const canonicalUrl = `https://sjmaths.com/up-assistant-teacher/hindi/${topic.dir}/`;
    const title = `${topic.hindiName} | हिन्दी | SJMaths`;

    return `<!DOCTYPE html>
<html lang="hi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${title}</title>
    <meta name="description" content="${topic.description}">
    <meta name="robots" content="index, follow, max-image-preview:large">
    <link rel="canonical" href="${canonicalUrl}">
    <meta name="keywords" content="${topic.keywords.join(', ')}, UP Assistant Teacher, हिन्दी, Hindi">
    <meta name="author" content="SJMaths">
    <link rel="icon" type="image/png" href="/favicon.png">
    <meta property="og:title" content="${title}">
    <meta property="og:description" content="${topic.description}">
    <meta property="og:type" content="article">
    <meta property="og:url" content="${canonicalUrl}">
    <meta property="og:image" content="https://sjmaths.com/assets/icons/icon-512x512.png">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Outfit:wght@500;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/assets/css/main.min.css?v=4ba21ce7">
    <link rel="stylesheet" href="/assets/css/layout.min.css?v=e4922b08">
    <link rel="stylesheet" href="/assets/css/component.min.css?v=8c99f11f">
    <link rel="stylesheet" href="/assets/css/improved-ui.min.css?v=86f5556a">
    <link rel="stylesheet" href="/assets/css/pages.min.css?v=9e3bd560">
    <style>
        :root { --glass-bg:rgba(255,255,255,.95);--glass-border:rgba(255,255,255,.2);--shadow-lg:0 10px 30px -5px rgba(212,175,55,.1);--accent-gradient:linear-gradient(135deg,#d4af37,#c0392b); }
        body.dark-mode { --glass-bg:rgba(30,30,46,.95);--glass-border:rgba(255,255,255,.05);--shadow-lg:0 10px 30px -5px rgba(0,0,0,.3); }
        .topic-container{max-width:1100px;margin:2rem auto;padding:2.5rem 1.5rem;animation:fadeIn .5s ease-out}
        .breadcrumbs{margin-bottom:1.5rem;font-size:.88rem;color:#64748b;background:rgba(255,255,255,.6);display:inline-block;padding:.6rem 1.2rem;border-radius:999px;border:1px solid rgba(0,0,0,.04)}
        .breadcrumbs a{color:#d4af37;text-decoration:none;font-weight:500}.breadcrumbs a:hover{text-decoration:underline}
        .breadcrumbs i{margin:0 .5rem;font-size:.7rem;color:#94a3b8}
        .topic-header{background:linear-gradient(135deg,rgba(212,175,55,.03),rgba(192,57,43,.03));border:1px solid rgba(212,175,55,.1);border-radius:1.25rem;padding:2.5rem;margin-bottom:2rem;text-align:center}
        .topic-header h1{font-family:'Outfit',sans-serif;font-size:clamp(1.8rem,5vw,2.5rem);font-weight:800;background:var(--accent-gradient);-webkit-background-clip:text;-webkit-text-fill-color:transparent;margin-bottom:.75rem;line-height:1.2}
        .topic-desc{color:#475569;font-size:1rem;line-height:1.7;max-width:700px;margin:0 auto}
        .topic-meta-bar{display:flex;flex-wrap:wrap;gap:1rem;justify-content:center;align-items:center;margin-top:1.5rem;padding-top:1.25rem;border-top:1px solid rgba(0,0,0,.05)}
        .back-link{display:inline-block;margin-bottom:1.5rem;color:#d4af37;text-decoration:none;font-weight:600;font-size:.9rem}.back-link:hover{text-decoration:underline}
        .study-tabs{display:flex;flex-wrap:wrap;gap:.5rem;padding:.55rem;background:var(--glass-bg);border:1px solid var(--glass-border);border-radius:1rem;margin-bottom:2rem;position:sticky;top:88px;z-index:100;backdrop-filter:blur(16px);justify-content:center}
        .tab-btn{border:none;background:transparent;color:#475569;padding:.65rem 1.1rem;border-radius:999px;cursor:pointer;font-weight:600;font-size:.9rem;font-family:'Outfit',sans-serif;display:inline-flex;align-items:center;gap:.5rem;transition:all .3s ease;white-space:nowrap}
        .tab-btn:hover{background:rgba(212,175,55,.08);color:#d4af37}
        .tab-btn.active{background:var(--accent-gradient);color:#fff;box-shadow:0 8px 20px rgba(212,175,55,.25)}
        .topic-content{min-height:400px}.tab-panel{display:none;animation:slideUp .4s ease-out}.tab-panel.active{display:block}
        @media(max-width:768px){.study-tabs{flex-wrap:nowrap;overflow-x:auto;-webkit-overflow-scrolling:touch;padding:.4rem;scrollbar-width:none;justify-content:flex-start}.study-tabs::-webkit-scrollbar{display:none}.tab-btn{font-size:.85rem;padding:.5rem .9rem}.topic-container{padding:0 1rem 2rem}.topic-header{padding:1.5rem 1rem}}
        @keyframes fadeIn{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:translateY(0)}}
        @keyframes slideUp{from{opacity:0;transform:translateY(15px)}to{opacity:1;transform:translateY(0)}}
    </style>
</head>
<body>
    <div id="header-container"></div>
    <main class="topic-container" id="main-content">
        <a href="/up-assistant-teacher/hindi/" class="back-link"><i class="fas fa-arrow-left"></i> <span class="lang-hi">वापस हिन्दी पर जाएँ</span><span class="lang-en">Back to Hindi</span></a>
        <div class="breadcrumbs">
            <a href="/">Home</a> <i class="fas fa-chevron-right"></i>
            <a href="/up-assistant-teacher/">UP Assistant Teacher</a> <i class="fas fa-chevron-right"></i>
            <a href="/up-assistant-teacher/hindi/">हिन्दी</a> <i class="fas fa-chevron-right"></i>
            <span>${topic.hindiName}</span>
        </div>
        <div class="topic-header">
            <h1><span class="lang-hi">${topic.hindiName}</span><span class="lang-en">${topic.name}</span></h1>
            <p class="topic-desc"><span class="lang-hi">${topic.description}</span><span class="lang-en">${topic.description}</span></p>
            <div class="topic-meta-bar">
                <span style="display:inline-flex;align-items:center;gap:.45rem;padding:.45rem .9rem;border-radius:999px;font-size:.85rem;font-weight:600;background:rgba(245,158,11,.1);color:#b45309;border:1px solid rgba(245,158,11,.2);">
                    <i class="fas fa-signal"></i><span class="lang-hi">मध्यम</span><span class="lang-en">Medium</span>
                </span>
                <span style="display:inline-flex;align-items:center;gap:.45rem;padding:.45rem .9rem;border-radius:999px;font-size:.85rem;font-weight:600;color:#475569;background:rgba(100,116,139,.06);border:1px solid rgba(100,116,139,.12);">
                    <i class="fas fa-clock"></i><span class="lang-hi">कुल 45 मिनट</span><span class="lang-en">45 min total</span>
                </span>
            </div>
        </div>
        <div class="study-tabs" role="tablist" aria-label="Topic resources">
            <button class="tab-btn active" data-tab="tab-concepts" role="tab" aria-selected="true"><i class="fas fa-book-open"></i><span class="lang-hi">1. अवधारणाएँ एवं सिद्धांत</span><span class="lang-en">1. Concepts &amp; Theories</span></button>
            <button class="tab-btn" data-tab="tab-practice" role="tab" aria-selected="false"><i class="fas fa-list-check"></i><span class="lang-hi">2. अभ्यास प्रश्न</span><span class="lang-en">2. Practice Questions</span></button>
            <button class="tab-btn" data-tab="tab-test" role="tab" aria-selected="false"><i class="fas fa-stopwatch"></i><span class="lang-hi">3. मिनी टेस्ट</span><span class="lang-en">3. Mini Test</span></button>
            <button class="tab-btn" data-tab="tab-revision" role="tab" aria-selected="false"><i class="fas fa-redo"></i><span class="lang-hi">4. पुनरावृत्ति</span><span class="lang-en">4. Revision</span></button>
        </div>
        <div class="topic-content" id="topic-content"></div>
        <script id="upsc-page-data" type="application/json">
        ${JSON.stringify({
            topicId: 'up-assistant-teacher.hindi.' + topic.dir,
            topicName: topic.name,
            hindiName: topic.hindiName,
            subject: 'Hindi',
            subjectDir: 'hindi',
            concepts: conceptsData || null,
            practice: null, pyqs: null, test: null,
            version: { generator: 'v1-retry', prompt: '1.1' },
            contentHash: 'sha256-placeholder',
            generatedAt: now
        }, null, 2)}
        </script>
    </main>
    <div id="footer-container"></div>
    <button id="backToTop" class="back-to-top" aria-label="Back to Top"><i class="fas fa-arrow-up"></i></button>
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            document.querySelectorAll('.tab-btn').forEach(function(btn) {
                btn.addEventListener('click', function() {
                    const t = btn.getAttribute('data-tab');
                    document.querySelectorAll('.tab-btn').forEach(b => { b.classList.remove('active'); b.setAttribute('aria-selected','false'); });
                    btn.classList.add('active'); btn.setAttribute('aria-selected','true');
                    document.querySelectorAll('.tab-panel').forEach(p => { p.classList.remove('active'); if (p.id===t) p.classList.add('active'); });
                });
            });
        });
    </script>
    <script src="/assets/js/upsc-renderer.min.js" defer data-cfasync="false"></script>
    <script src="/assets/js/search.min.js?v=68a0a505" defer data-cfasync="false"></script>
    <script src="/assets/js/main.min.js?v=6e28faa6" defer data-cfasync="false"></script>
    <script src="/assets/js/global-header.min.js?v=bd5be716" defer data-cfasync="false"></script>
    <script src="/assets/js/global-footer.min.js?v=c641c625" defer data-cfasync="false"></script>
</body>
</html>`;
}

// ============================================================================
// MAIN
// ============================================================================
async function main() {
    console.log('╔══════════════════════════════════════════════════════════════╗');
    console.log('║ Hindi Retry — 11 Failed Topics                               ║');
    console.log(`║ Model: ${currentModel} (max tokens: 65536)              ║`);
    console.log('╚══════════════════════════════════════════════════════════════╝\n');

    let ok = 0, fail = 0;

    for (let i = 0; i < FAILED_TOPICS.length; i++) {
        const topic = FAILED_TOPICS[i];
        console.log(`\n${'='.repeat(70)}`);
        console.log(`[${i + 1}/${FAILED_TOPICS.length}] ${topic.name} [${topic.type}]`);
        console.log(`${'='.repeat(70)}`);

        const outputDir = path.join(process.cwd(), 'up-assistant-teacher', 'hindi', topic.dir);
        fs.mkdirSync(outputDir, { recursive: true });
        const tabsDir = path.join(outputDir, 'tabs');
        fs.mkdirSync(tabsDir, { recursive: true });

        let conceptsData = null;

        try {
            console.log('  📝 Generating...');
            const raw = await callGemini(buildCompactPrompt(topic));
            const parsed = parseResponse(raw);

            if (!parsed.sections || !Array.isArray(parsed.sections) || parsed.sections.length === 0) {
                throw new Error('Missing sections array');
            }

            // Convert any paragraph sections
            parsed.sections = parsed.sections.map(s =>
                s.type === 'paragraph'
                    ? { title: s.title, type: 'list', items: [{ term: 'Key Point', definition: s.content || '' }] }
                    : s
            );

            conceptsData = parsed;
            fs.writeFileSync(path.join(tabsDir, 'concepts.json'), JSON.stringify(conceptsData, null, 2), 'utf8');
            console.log('  ✅ concepts.json saved');
            ok++;
        } catch (err) {
            console.error(`  ❌ Failed: ${err.message}`);
            conceptsData = buildFallback(topic);
            fail++;
        }

        fs.writeFileSync(path.join(outputDir, 'index.html'), assemblePage(topic, conceptsData), 'utf8');
        fs.writeFileSync(path.join(outputDir, 'data.json'), JSON.stringify({ concepts: conceptsData, practice: null, pyqs: null, test: null }, null, 2), 'utf8');
        console.log('  💾 index.html + data.json saved');

        if (i < FAILED_TOPICS.length - 1) {
            console.log(`  ⏳ Waiting ${REQUEST_DELAY_MS / 1000}s...`);
            await sleep(REQUEST_DELAY_MS);
        }
    }

    console.log(`\n${'='.repeat(70)}`);
    console.log(`📊 RETRY SUMMARY: ${ok} succeeded, ${fail} failed out of ${FAILED_TOPICS.length}`);
    console.log(`${'='.repeat(70)}`);
}

main().catch(err => { console.error('Fatal:', err); process.exit(1); });
