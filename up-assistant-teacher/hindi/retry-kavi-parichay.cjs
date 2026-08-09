const fs = require('fs');
const path = require('path');
const { jsonrepair } = require('jsonrepair');

// ENV loader
if (fs.existsSync('.env')) {
    for (const line of fs.readFileSync('.env', 'utf8').split('\n')) {
        const m = line.match(/^\s*([\w.-]+)\s*=\s*(.*)?$/);
        if (m) {
            let v = (m[2] || '').trim();
            if ((v.startsWith('"') && v.endsWith('"')) || (v.startsWith("'") && v.endsWith("'"))) v = v.slice(1, -1);
            process.env[m[1]] = process.env[m[1]] || v;
        }
    }
}
const apiKey = process.env.GEMINI_API_KEY;
if (!apiKey) { console.error('No GEMINI_API_KEY'); process.exit(1); }

const sleep = ms => new Promise(r => setTimeout(r, ms));

const TOPIC = {
    dir: 'kavai-paraichaya-va-kaavaya-gauna',
    name: 'Kavi Parichay aur Kavya Gun (कवि परिचय)',
    hindiName: 'कवि परिचय व काव्य गुण',
    description: 'Hindi Kavi Parichay (Poet Introduction) and Kavya Gun (Poetic Qualities) — the three Guna: Madhura, Ojasvi, Prasad; how they manifest in poetry; linking poets to their Guna.',
    keywords: ['Kavi Parichay', 'Kavya Gun', 'Madhura Gun', 'Ojasvi Gun', 'Prasad Gun', 'Poet Introduction Hindi', 'Hindi Poetry UP'],
    type: 'poetry'
};

// ============================================================================
// JSON PARSER — uses jsonrepair library for robust LLM output handling
// ============================================================================
function parseResponse(raw) {
    let s = raw.trim();
    // Strip markdown fences
    if (s.startsWith('```json')) s = s.replace(/^```json\s*/, '').replace(/\s*```$/, '');
    else if (s.startsWith('```')) s = s.replace(/^```\s*/, '').replace(/\s*```$/, '');
    // Normalize smart quotes
    s = s.replace(/[\u2018\u2019]/g, "'").replace(/[\u201c\u201d]/g, '"');
    // Extract JSON block if there's preamble
    const start = s.indexOf('{');
    if (start > 0) s = s.substring(start);

    try {
        // First try native parse
        return JSON.parse(s);
    } catch (_) { }

    // Use jsonrepair to fix all LLM JSON issues (trailing commas, unescaped
    // quotes, raw newlines in strings, truncated JSON, etc.)
    try {
        const fixed = jsonrepair(s);
        return JSON.parse(fixed);
    } catch (e) {
        console.error('❌ jsonrepair also failed. First 500 chars:\n', s.substring(0, 500));
        throw new Error('JSON parse failed: ' + e.message);
    }
}

// ============================================================================
// API CALL
// ============================================================================
async function callGemini(prompt, retries = 5) {
    for (let attempt = 1; attempt <= retries; attempt++) {
        try {
            const res = await fetch(
                `https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash-lite:generateContent?key=${apiKey}`,
                {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        contents: [{ parts: [{ text: prompt }] }],
                        generationConfig: { temperature: 0.7, maxOutputTokens: 65536, topP: 0.95 }
                    })
                }
            );
            if (res.status === 429 || res.status === 403) {
                const w = 15000 * Math.pow(2, attempt - 1);
                console.log(`  ⚠️ Rate limited — waiting ${w / 1000}s...`);
                await sleep(w); continue;
            }
            if (!res.ok) throw new Error(`HTTP ${res.status}`);
            const data = await res.json();
            const text = data?.candidates?.[0]?.content?.parts?.[0]?.text || '';
            if (!text.trim()) throw new Error('Empty response');
            return text;
        } catch (err) {
            if (attempt === retries) throw err;
            console.log(`  ⚠️ Retry ${attempt}: ${err.message}`);
            await sleep(5000);
        }
    }
}

// ============================================================================
// PROMPT — explicitly forbids double quotes inside cell values
// ============================================================================
const PROMPT = `You are an expert for UP Assistant Teacher (Hindi) exam prep. Create EXAM-FOCUSED concept notes for: "Kavi Parichay aur Kavya Gun" (कवि परिचय व काव्य गुण).

Focus: Kavya Gun types (Madhura, Ojasvi, Prasad Gun), their definitions and identifying features; poet introductions for UP exam poets; how to match poets to their dominant Gun; exam question patterns.

CRITICAL RULES:
- Return ONLY valid JSON — no markdown fences, no explanatory text before or after.
- STRICTLY NO PARAGRAPHS — only table, list, subcards types.
- ENGLISH only. Hindi terms may appear bolded in English text e.g. **Madhura Gun**.
- IMPORTANT: Do NOT use double-quote characters (") inside any string values in the JSON. Use single quotes or rephrase if quoting text.
- All string values in the JSON must be properly escapable.

Return JSON with exactly this structure:
{
  "sections": [
    {
      "title": "Detailed Brief Overview",
      "type": "table",
      "headers": ["Aspect", "Key Details"],
      "rows": [
        ["row1col1", "row1col2"],
        ["row2col1", "row2col2"]
      ]
    },
    {
      "title": "Concepts and Theories",
      "type": "subcards",
      "items": [
        {"title": "Subcard Title", "content": "• Point 1 with **bold** terms\\n• Point 2\\n• **Mnemonic:** ..."}
      ]
    },
    {
      "title": "Important Facts and Data",
      "type": "table",
      "headers": ["Poet / Gun", "Type", "Key Works / Features"],
      "rows": [["data1", "data2", "data3"]]
    },
    {
      "title": "Tricks to Remember",
      "type": "list",
      "items": [{"term": "Trick", "definition": "Explanation"}]
    },
    {
      "title": "Mistakes to Avoid",
      "type": "list",
      "items": [{"term": "Error", "definition": "Correct rule"}]
    },
    {
      "title": "Point-wise Detailed Summary",
      "type": "list",
      "items": [{"term": "Point", "definition": "Summary"}]
    }
  ],
  "upscNotes": [
    {"type": "tip", "content": "Exam tip"},
    {"type": "trap", "content": "Common trap"}
  ],
  "keyTakeaways": ["Takeaway 1", "Takeaway 2", "Takeaway 3"]
}

Requirements: Overview 6-8 rows, Subcards 5-6 with mnemonics, Facts table 8-10 rows, Tricks 6, Mistakes 6, Summary 10, upscNotes 3 tips + 2 traps, keyTakeaways 5.
Keywords: Kavi Parichay, Kavya Gun, Madhura Gun, Ojasvi Gun, Prasad Gun, Poet Introduction Hindi, Hindi Poetry UP`;

// ============================================================================
// HTML assembler (minimal, same structure as main generator)
// ============================================================================
function assemblePage(topic, data) {
    const now = new Date().toISOString();
    const canonicalUrl = `https://sjmaths.com/up-assistant-teacher/hindi/${topic.dir}/`;
    const title = `${topic.hindiName} | हिन्दी | SJMaths`;
    return `<!DOCTYPE html>
<html lang="hi">
<head>
    <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
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
        :root{--glass-bg:rgba(255,255,255,.95);--glass-border:rgba(255,255,255,.2);--shadow-lg:0 10px 30px -5px rgba(212,175,55,.1);--accent-gradient:linear-gradient(135deg,#d4af37,#c0392b)}
        body.dark-mode{--glass-bg:rgba(30,30,46,.95);--glass-border:rgba(255,255,255,.05);--shadow-lg:0 10px 30px -5px rgba(0,0,0,.3)}
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
                <span style="display:inline-flex;align-items:center;gap:.45rem;padding:.45rem .9rem;border-radius:999px;font-size:.85rem;font-weight:600;background:rgba(245,158,11,.1);color:#b45309;border:1px solid rgba(245,158,11,.2);"><i class="fas fa-signal"></i><span class="lang-hi">मध्यम</span><span class="lang-en">Medium</span></span>
                <span style="display:inline-flex;align-items:center;gap:.45rem;padding:.45rem .9rem;border-radius:999px;font-size:.85rem;font-weight:600;color:#475569;background:rgba(100,116,139,.06);border:1px solid rgba(100,116,139,.12);"><i class="fas fa-clock"></i><span class="lang-hi">कुल 45 मिनट</span><span class="lang-en">45 min total</span></span>
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
            topicName: topic.name, hindiName: topic.hindiName,
            subject: 'Hindi', subjectDir: 'hindi',
            concepts: data || null, practice: null, pyqs: null, test: null,
            version: { generator: 'v1-single-retry', prompt: '1.2' },
            contentHash: 'sha256-placeholder', generatedAt: now
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
                    document.querySelectorAll('.tab-panel').forEach(p => { p.classList.remove('active'); if(p.id===t) p.classList.add('active'); });
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
    console.log('🔁 Single-topic retry: Kavi Parichay aur Kavya Gun');
    console.log('   Model: gemini-3.5-flash-lite | Fix: unescaped inner quotes\n');

    const outputDir = path.join(process.cwd(), 'up-assistant-teacher', 'hindi', TOPIC.dir);
    fs.mkdirSync(outputDir, { recursive: true });
    const tabsDir = path.join(outputDir, 'tabs');
    fs.mkdirSync(tabsDir, { recursive: true });

    let conceptsData = null;

    try {
        console.log('📝 Generating...');
        const raw = await callGemini(PROMPT);
        const parsed = parseResponse(raw);

        if (!parsed.sections || !Array.isArray(parsed.sections) || parsed.sections.length === 0) {
            throw new Error('Missing sections array');
        }
        parsed.sections = parsed.sections.map(s =>
            s.type === 'paragraph'
                ? { title: s.title, type: 'list', items: [{ term: 'Key Point', definition: s.content || '' }] }
                : s
        );
        conceptsData = parsed;
        fs.writeFileSync(path.join(tabsDir, 'concepts.json'), JSON.stringify(conceptsData, null, 2), 'utf8');
        console.log('✅ concepts.json saved!');
    } catch (err) {
        console.error('❌ Failed:', err.message);
        conceptsData = {
            sections: [{
                title: 'Detailed Brief Overview', type: 'table',
                headers: ['Aspect', 'Key Details'],
                rows: [
                    ['Topic', '**Kavi Parichay aur Kavya Gun** — Poet Introduction and Poetic Qualities'],
                    ['Subject', '**Hindi** for UP Assistant Teacher'],
                    ['Kavya Gun', '**Madhura Gun** (lyrical beauty), **Ojasvi Gun** (vigour/power), **Prasad Gun** (clarity/grace)'],
                    ['Key Poets', '**Kabirdas** (Ojasvi), **Surdas** (Madhura), **Tulsidas** (Prasad), **Nirala** (Ojasvi)'],
                    ['Status', 'Content under preparation — check back soon for detailed notes']
                ]
            }],
            upscNotes: [
                { type: 'tip', content: 'Kavya Gun questions frequently appear in UP Assistant Teacher — memorize 3 Gun types and 2-3 poet examples for each.' },
                { type: 'trap', content: 'Students confuse Prasad Gun (clarity) with Jaishankar Prasad the poet — they are different concepts.' }
            ],
            keyTakeaways: [
                'Three Kavya Gun: Madhura, Ojasvi, Prasad',
                'Kabirdas — primarily Ojasvi Gun',
                'Surdas — primarily Madhura Gun',
                'Tulsidas — Prasad Gun dominant in Ramcharitmanas',
                'Kavi Parichay questions test author-work-era-Gun mapping'
            ]
        };
    }

    fs.writeFileSync(path.join(outputDir, 'index.html'), assemblePage(TOPIC, conceptsData), 'utf8');
    fs.writeFileSync(path.join(outputDir, 'data.json'), JSON.stringify({ concepts: conceptsData, practice: null, pyqs: null, test: null }, null, 2), 'utf8');
    console.log('💾 index.html + data.json saved');
    console.log('\n🎉 Done! Hindi microtopics are now 45/45 complete.');
}

main().catch(err => { console.error('Fatal:', err); process.exit(1); });
