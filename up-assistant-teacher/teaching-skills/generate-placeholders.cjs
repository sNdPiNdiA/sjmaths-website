/**
 * Generates content ONLY for the 2 placeholder topics:
 *  - inclusive-education
 *  - new-initiatives-in-elementary-education
 *
 * Reuses the same prompt / HTML assembler pattern as generate-microtopics.cjs.
 * Run from the repo root:  node up-assistant-teacher/teaching-skills/generate-placeholders.cjs
 */

const fs   = require('fs');
const path = require('path');

// ── ENV ───────────────────────────────────────────────────────────────────────
if (fs.existsSync('.env')) {
    for (const line of fs.readFileSync('.env', 'utf8').split('\n')) {
        const m = line.match(/^\s*([\w.-]+)\s*=\s*(.*)?$/);
        if (m) {
            let v = (m[2] || '').trim();
            if ((v.startsWith('"') && v.endsWith('"')) || (v.startsWith("'") && v.endsWith("'"))) v = v.slice(1,-1);
            process.env[m[1]] = process.env[m[1]] || v;
        }
    }
}
const apiKey = process.env.GEMINI_API_KEY;
if (!apiKey) { console.error('GEMINI_API_KEY missing.'); process.exit(1); }

// ── CONSTANTS ─────────────────────────────────────────────────────────────────
const MODEL          = 'gemini-3.5-flash-lite';
const DELAY_MS       = 20000;
const MAX_RETRIES    = 5;
const TEACHING_ROOT  = path.join(process.cwd(), 'up-assistant-teacher', 'teaching-skills');

// ── 2 PLACEHOLDER TOPICS ─────────────────────────────────────────────────────
const TOPICS = [
    {
        dir: 'inclusive-education',
        name: 'Inclusive Education',
        hindiName: 'समावेशी शिक्षा',
        description: 'Inclusive education - teaching diverse learners, children with special needs (CWSN), learning disabilities, integration strategies.',
        keywords: ['Inclusive Education', 'CWSN', 'Special Needs', 'Learning Disabilities', 'Differentiated Instruction', 'Integration']
    },
    {
        dir: 'new-initiatives-in-elementary-education',
        name: 'New Initiatives in Elementary Education',
        hindiName: 'प्रारम्भिक शिक्षा के नवीन प्रयास',
        description: 'New initiatives in elementary education - government schemes, Sarva Shiksha Abhiyan, RTE Act 2009, NEP 2020, education policies.',
        keywords: ['New Initiatives', 'Elementary Schemes', 'SSA', 'RTE Act 2009', 'NEP 2020', 'Education Schemes', 'Samagra Shiksha']
    }
];

// ── UTILITIES ─────────────────────────────────────────────────────────────────
const sleep = ms => new Promise(r => setTimeout(r, ms));

async function callGemini(prompt, retries = MAX_RETRIES) {
    for (let attempt = 1; attempt <= retries; attempt++) {
        try {
            const url = `https://generativelanguage.googleapis.com/v1beta/models/${MODEL}:generateContent?key=${apiKey}`;
            const res = await fetch(url, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    contents: [{ parts: [{ text: prompt }] }],
                    generationConfig: { temperature: 0.7, maxOutputTokens: 65536, topP: 0.95 }
                })
            });
            if (res.status === 429 || res.status === 403) {
                const wait = 15000 * Math.pow(2, attempt - 1);
                console.log(`  ⚠️  Rate limited – waiting ${wait/1000}s (attempt ${attempt}/${retries})`);
                await sleep(wait); continue;
            }
            if (res.status === 503) { await sleep(DELAY_MS * 2); continue; }
            if (!res.ok) throw new Error(`API ${res.status}: ${(await res.text()).slice(0,200)}`);
            const data = await res.json();
            const text = data?.candidates?.[0]?.content?.parts?.[0]?.text || '';
            if (!text.trim()) throw new Error('Empty response');
            return text;
        } catch (err) {
            if (attempt === retries) throw err;
            console.log(`  ⚠️  Retry ${attempt}/${retries}: ${err.message}`);
            await sleep(5000);
        }
    }
}

function parseResponse(raw) {
    let s = raw.trim()
        .replace(/^```json\s*/, '').replace(/\s*```$/, '')
        .replace(/^```\s*/, '').replace(/\s*```$/, '')
        .replace(/[\u2018\u2019]/g,"'").replace(/[\u201c\u201d]/g,'"');
    try { return JSON.parse(s); } catch(_) {}
    const m = s.match(/[\{\[][\s\S]*[\}\]]/);
    if (m) { try { return JSON.parse(m[0]); } catch(_) {} }
    throw new Error('No valid JSON in response');
}

// ── PROMPT ────────────────────────────────────────────────────────────────────
function buildPrompt(topic) {
    return `You are an expert faculty member for UP Assistant Teacher (शिक्षण कौशल) exam preparation. Create ULTRA-COMPREHENSIVE, EXAM-FOCUSED concept notes for the topic: "${topic.name}" (${topic.hindiName}).

TOPIC CONTEXT:
- Subject: Teaching Skills (शिक्षण कौशल)
- Exam: UP Assistant Teacher Recruitment Examination
- Keywords to target: ${topic.keywords.join(', ')}

CRITICAL FORMAT RULES — NO PARAGRAPHS ALLOWED:
1. STRICTLY NO PARAGRAPHS — Do NOT use the "paragraph" type anywhere.
2. Content must be point-wise, bulleted, tabular, and structured for rapid exam revision.
3. Use **bold** for key terms, names, dates, and figures within table cells and list items.
4. Content must be comprehensive and exam-focused.
5. LANGUAGE: Use ENGLISH ONLY for all content.

REQUIRED SECTION STRUCTURE (in this exact order):

SECTION 1 — "Detailed Brief Overview" (type: "table")
- 8-10 rows: What, When, Who, Why Important, Key Features, Types/Categories, Significance for Exam, Core Objectives, etc.
- Headers: ["Aspect", "Key Details"]

SECTION 2 — "Concepts and Theories" (type: "subcards")
- 5-7 subcards, each a major sub-topic with point-wise content and 2-3 mnemonics.

SECTION 3 — "Important Facts and Data" (type: "table")
- 3 columns, 8-12 rows covering key facts, figures, comparisons.
- Headers: ["Category", "Key Term / Concept", "Key Facts & Figures"]

SECTION 4 — "Tricks to Remember" (type: "list")
- 6-8 items: { "term": "Trick N: Title", "definition": "Detailed trick with **bold** terms" }

SECTION 5 — "Mistakes to Avoid" (type: "list")
- 6-8 items: { "term": "Mistake N: Error", "definition": "Correct fact and why confused" }

SECTION 6 — "Point-wise Detailed Summary" (type: "list")
- 10-15 items: { "term": "Key Point Title", "definition": "Concise summary with **bold** terms" }

OUTPUT FORMAT — Return ONLY valid JSON:
{
  "sections": [
    { "title": "Detailed Brief Overview", "type": "table", "headers": ["Aspect","Key Details"], "rows": [["Aspect","**Detail**"]] },
    { "title": "Concepts and Theories", "type": "subcards", "items": [{ "title": "Sub-topic (Mnemonic: XYZ)", "content": "• Point 1\\n• Point 2\\n• **Mnemonic:** ..." }] },
    { "title": "Important Facts and Data", "type": "table", "headers": ["Category","Key Term / Concept","Key Facts & Figures"], "rows": [["Cat","Term","**Fact**"]] },
    { "title": "Tricks to Remember", "type": "list", "items": [{ "term": "Trick 1: Title", "definition": "Explanation" }] },
    { "title": "Mistakes to Avoid", "type": "list", "items": [{ "term": "Mistake 1: Error", "definition": "Correction" }] },
    { "title": "Point-wise Detailed Summary", "type": "list", "items": [{ "term": "Point Title", "definition": "Summary" }] }
  ],
  "upscNotes": [
    { "type": "tip", "content": "Exam strategy tip" },
    { "type": "trap", "content": "Common trap" }
  ],
  "keyTakeaways": ["Takeaway 1", "Takeaway 2"]
}

Generate comprehensive, exam-ready content now.`;
}

// ── READ EXISTING index.html AND INJECT CONTENT ───────────────────────────────
function injectConceptsIntoHtml(topic, conceptsData) {
    const htmlPath = path.join(TEACHING_ROOT, topic.dir, 'index.html');
    if (!fs.existsSync(htmlPath)) {
        console.log(`  ⚠️  index.html not found for ${topic.dir} – skipping HTML update`);
        return;
    }
    let html = fs.readFileSync(htmlPath, 'utf8');

    // Update the embedded JSON data block
    html = html.replace(
        /(<script id="upsc-page-data"[^>]*>)([\s\S]*?)(<\/script>)/,
        (_, open, content, close) => {
            try {
                const data = JSON.parse(content.trim());
                data.concepts = conceptsData;
                return `${open}\n${JSON.stringify(data, null, 2)}\n${close}`;
            } catch(_) {
                return _;
            }
        }
    );

    fs.writeFileSync(htmlPath, html, 'utf8');
    console.log(`  💾 Updated index.html JSON data block`);
}

// ── MAIN ──────────────────────────────────────────────────────────────────────
async function main() {
    console.log('╔══════════════════════════════════════════════════════╗');
    console.log('║  Generating 2 placeholder Teaching Skills topics     ║');
    console.log('╚══════════════════════════════════════════════════════╝\n');

    for (let i = 0; i < TOPICS.length; i++) {
        const topic = TOPICS[i];
        console.log(`\n${'='.repeat(60)}`);
        console.log(`[${i+1}/${TOPICS.length}] ${topic.name}`);
        console.log('='.repeat(60));

        const outDir  = path.join(TEACHING_ROOT, topic.dir);
        const tabsDir = path.join(outDir, 'tabs');
        fs.mkdirSync(tabsDir, { recursive: true });

        let conceptsData;
        try {
            console.log('  📝 Calling Gemini API...');
            const raw    = await callGemini(buildPrompt(topic));
            conceptsData = parseResponse(raw);

            // Strip any paragraph-type sections
            conceptsData.sections = (conceptsData.sections || []).map(s =>
                s.type === 'paragraph'
                    ? { title: s.title, type: 'list', items: [{ term: 'Key Point', definition: s.content || '' }] }
                    : s
            );

            console.log(`  ✅ Generated ${conceptsData.sections.length} sections`);
        } catch (err) {
            console.error(`  ❌ Generation failed: ${err.message}`);
            process.exit(1);
        }

        // Save tabs/concepts.json
        fs.writeFileSync(path.join(tabsDir, 'concepts.json'), JSON.stringify(conceptsData, null, 2), 'utf8');
        console.log('  💾 Saved tabs/concepts.json');

        // Inject into existing index.html data block
        injectConceptsIntoHtml(topic, conceptsData);

        if (i < TOPICS.length - 1) {
            console.log(`  ⏳ Waiting ${DELAY_MS/1000}s before next topic...`);
            await sleep(DELAY_MS);
        }
    }

    console.log('\n✅ Done! Now run:');
    console.log('   node scripts/prerender-seo-content.cjs --scope=up-assistant-teacher/teaching-skills');
}

main().catch(err => { console.error('Fatal:', err); process.exit(1); });
