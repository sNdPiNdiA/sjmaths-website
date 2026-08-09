const fs = require('fs');
const path = require('path');
const cheerio = require('cheerio');

// Load env
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
    console.error('GEMINI_API_KEY is not set.');
    process.exit(1);
}

const REQUEST_DELAY_MS = 20000;
const MAX_RETRIES = 5;
let currentModel = 'gemini-3.5-flash-lite';



function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

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
                        responseMimeType: 'application/json',
                        temperature: 0.15,
                        maxOutputTokens: 8192
                    }
                })
            });

            if (res.status === 429 || res.status === 403) {
                const wait = 15000 * Math.pow(2, attempt - 1);
                console.log(`  ⚠️ Rate limited. Waiting ${wait / 1000}s...`);
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
            if (!text || text.trim().length === 0) throw new Error('Empty response from API');
            return text;
        } catch (err) {
            if (attempt === retries) throw err;
            console.log(`  ⚠️ Retry ${attempt}/${retries} after error: ${err.message}`);
            await sleep(5000);
        }
    }
    throw new Error('Max retries exceeded');
}

function parseResponse(raw) {
    if (!raw || typeof raw !== 'string') throw new Error('Invalid response');
    const clean = raw.trim().replace(/^```json\s*/i, '').replace(/```$/, '').trim();
    let repaired = clean.replace(/\\'/g, "'");
    repaired = repaired.replace(/"type"\s*:\s*"subcards"\s*:\s*\[/g, '"type": "subcards", "items": [');
    repaired = repaired.replace(/"subcards"\s*:\s*\[/g, '"items": [');
    return JSON.parse(repaired);
}

function buildConceptsPrompt(topic) {
    return `You are an expert faculty member for UP Assistant Teacher (पर्यावरण एवं सामाजिक अध्ययन) exam preparation. Create ULTRA-COMPREHENSIVE, EXAM-FOCUSED concept notes for the topic: "${topic.name}" (${topic.hindiName}).

TOPIC CONTEXT:
- Subject: Environmental & Social Studies (पर्यावरण एवं सामाजिक अध्ययन)
- Exam: UP Assistant Teacher Recruitment Examination
- Topic Directory: ${topic.dir}
- Keywords to target: ${topic.keywords.join(', ')}

CRITICAL FORMAT RULES — NO PARAGRAPHS ALLOWED:
1. **STRICTLY NO PARAGRAPHS** — Do NOT use the "paragraph" type anywhere. Every section must be a table, list, or subcards.
2. Content must be **point-wise, bulleted, tabular, and structured** for rapid exam revision.
3. Use **bold** for key terms, names, dates, and figures within table cells and list items.
4. Content must be **comprehensive and exam-focused** — cover ALL important facts, concepts, and principles that UP Assistant Teacher asks.
5. **LANGUAGE: Use ENGLISH ONLY** for all content including headers, rows, and items.
6. **CRITICAL JSON SYNTAX RULE:** Do NOT use double quotes (") inside any JSON string values (such as content, descriptions, mnemonics). Use single quotes (') instead. Inner double quotes will break JSON parsing.

REQUIRED SECTION STRUCTURE (in this exact order):

SECTION 1 — "Detailed Brief Overview" (type: "table")
- A comprehensive overview table with 8-10 rows covering: What, When, Who, Why Important, Key Features, Types/Categories, Significance for Exam, and other essential facts.
- Headers: ["Aspect", "Key Details"]

SECTION 2 — "Concepts and Theories" (type: "subcards")
- 5-7 subcards, each covering a major sub-topic or theme.
- Each subcard must have a title and detailed point-wise content (NOT paragraphs).
- Include at least 2-3 powerful mnemonics within these subcards to help memorize sequences, lists, and facts.

SECTION 3 — "Important Facts and Data" (type: "table")
- 3-4 detailed tables with 8-12 rows each covering:
  a) Important Concepts/Principles with their features
  b) Important Terms/Definitions with explanations
  c) Important Facts/Figures with applications
  d) Important Differences/Comparisons

SECTION 4 — "Tricks to Remember" (type: "list")
- 6-8 items with "term" = trick title, "definition" = detailed trick explanation
- Include memory tricks, acronyms, association techniques, and quick recall methods in English

SECTION 5 — "Mistakes to Avoid" (type: "list")
- 6-8 items with "term" = common mistake, "definition" = correct fact and why students get confused
- Cover frequently confused concepts, facts, and figures

SECTION 6 — "Point-wise Detailed Summary" (type: "list")
- 10-15 items with "term" = key point title, "definition" = concise point-wise summary
- This is the final revision summary covering ALL essential facts

ADDITIONAL REQUIREMENTS:
- "upscNotes": Include 4-6 notes with type "tip" (exam strategy) and "trap" (common traps)
- "keyTakeaways": Include 5-8 concise, high-yield takeaways

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
      "title": "Concepts and Theories",
      "type": "subcards",
      "items": [
        {
          "title": "Sub-topic 1 with **mnemonic**",
          "content": "• Point 1 with **bold** terms\\n• Point 2 with **bold** terms\\n• **Mnemonic:** Phrase to remember"
        }
      ]
    },
    {
      "title": "Important Facts and Data",
      "type": "table",
      "headers": ["Column 1", "Column 2", "Column 3"],
      "rows": [
        ["Data 1", "Data 2", "Data 3"]
      ]
    },
    {
      "title": "Tricks to Remember",
      "type": "list",
      "items": [
        {
          "term": "Trick 1: Title",
          "definition": "Detailed explanation of the trick with **bold** key terms"
        }
      ]
    },
    {
      "title": "Mistakes to Avoid",
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
      "content": "Exam strategy tip for UP Assistant Teacher"
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
}

IMPORTANT:
- Use ONLY English text. Do NOT use Hindi or bilingual format.
- Every section must be comprehensive and detailed — this is for serious exam preparation.
- Include ALL important facts, figures, names, dates, and concepts.
- The content must be exam-focused with keywords naturally embedded.
- NO paragraphs anywhere — only tables, lists, and subcards.`;
}

function buildFallbackConcepts(topic) {
    return {
        sections: [
            {
                title: 'Detailed Brief Overview',
                type: 'table',
                headers: ['Aspect', 'Key Details'],
                rows: [
                    ['Topic', `**${topic.name}** (${topic.hindiName})`],
                    ['Subject', '**Environmental & Social Studies** for UP Assistant Teacher'],
                    ['Status', 'Content under preparation — check back soon for comprehensive notes']
                ]
            }
        ],
        upscNotes: [
            { type: 'tip', content: `This topic is important for UP Assistant Teacher exam. Study ${topic.name} thoroughly.` }
        ],
        keyTakeaways: [
            `Study ${topic.name} thoroughly for UP Assistant Teacher`,
            'Focus on important concepts, facts, and principles',
            'Practice with previous year questions'
        ]
    };
}

function assembleMicrotopicPage(topic, conceptsData) {
    const now = new Date().toISOString();
    const canonicalUrl = `https://sjmaths.com/up-assistant-teacher/environmental-social-studies/${topic.dir}/`;
    const title = `${topic.name} | ${topic.hindiName} - पर्यावरण एवं सामाजिक अध्ययन | SJMaths`;
    const description = topic.description;

    return `<!DOCTYPE html>
<html lang="hi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${title}</title>
    <meta name="description" content="${description}">
    <meta name="robots" content="index, follow, max-image-preview:large">
    <link rel="canonical" href="${canonicalUrl}">
    <meta name="keywords" content="${topic.keywords.join(', ')}, UP Assistant Teacher, पर्यावरण एवं सामाजिक अध्ययन">
    <meta name="author" content="SJMaths">
    <link rel="icon" type="image/png" href="/favicon.png">
    <link rel="stylesheet" href="/assets/css/main.min.css?v=4ba21ce7">
    <link rel="stylesheet" href="/assets/css/layout.min.css?v=e4922b08">
    <link rel="stylesheet" href="/assets/css/component.min.css?v=8c99f11f">
    <link rel="stylesheet" href="/assets/css/improved-ui.min.css?v=86f5556a">
    <link rel="stylesheet" href="/assets/css/pages.min.css?v=9e3bd560">
    <link rel="stylesheet" href="/assets/css/topic-module.css">
</head>
<body>
    <div id="header-container"></div>
    <main class="topic-container" id="main-content">
        <a href="/up-assistant-teacher/environmental-social-studies/" class="back-link" style="display:inline-block;margin-bottom:1.5rem;color:#d4af37;text-decoration:none;font-weight:600;"><i class="fas fa-arrow-left"></i> Back to Environmental & Social Studies</a>
        <div class="topic-header">
            <h1><span class="lang-hi">${topic.hindiName}</span><span class="lang-en">${topic.name}</span></h1>
            <p>${topic.description}</p>
        </div>
        <div class="study-tabs" role="tablist">
            <button class="tab-btn active" data-tab="tab-concepts"><i class="fas fa-book-open"></i> <span class="lang-hi">1. अवधारणाएँ एवं सिद्धांत</span><span class="lang-en">1. Concepts & Theories</span></button>
            <button class="tab-btn" data-tab="tab-practice"><i class="fas fa-list-check"></i> <span class="lang-hi">2. अभ्यास प्रश्न</span><span class="lang-en">2. Practice Questions</span></button>
            <button class="tab-btn" data-tab="tab-test"><i class="fas fa-stopwatch"></i> <span class="lang-hi">3. मिनी टेस्ट</span><span class="lang-en">3. Mini Test</span></button>
            <button class="tab-btn" data-tab="tab-revision"><i class="fas fa-redo"></i> <span class="lang-hi">4. पुनरावृत्ति</span><span class="lang-en">4. Revision</span></button>
        </div>
        <div class="topic-content" id="topic-content"></div>
        <script id="upsc-page-data" type="application/json">
        ${JSON.stringify({
        topicId: 'up-assistant-teacher.environmental-social-studies.' + topic.dir,
        topicName: topic.name,
        hindiName: topic.hindiName,
        subject: 'Environmental & Social Studies',
        subjectDir: 'environmental-social-studies',
        concepts: conceptsData || null,
        practice: null,
        pyqs: null,
        test: null,
        version: { generator: 'v1', prompt: '1.0' },
        contentHash: 'sha256-placeholder',
        generatedAt: now
    }, null, 2)}
        </script>
    </main>
    <div id="footer-container"></div>
    <script src="/assets/js/topic-module.js"></script>
    <script src="/assets/js/upsc-renderer.min.js" defer data-cfasync="false"></script>
    <script src="/assets/js/search.min.js?v=68a0a505" defer data-cfasync="false"></script>
    <script src="/assets/js/main.min.js?v=6e28faa6" defer data-cfasync="false"></script>
    <script src="/assets/js/global-header.min.js?v=bd5be716" defer data-cfasync="false"></script>
    <script src="/assets/js/global-footer.min.js?v=c641c625" defer data-cfasync="false"></script>
</body>
</html>`;
}

async function main() {
    console.log('============================================================');
    console.log(' UP Assistant Teacher - Missing Microtopics Generator');
    console.log(` Model: ${currentModel}`);
    console.log('============================================================\n');

    // Load topics dynamically from index.html
    const indexHtmlPath = path.join(process.cwd(), 'up-assistant-teacher', 'environmental-social-studies', 'index.html');
    if (!fs.existsSync(indexHtmlPath)) {
        console.error('Environmental & Social Studies index.html not found!');
        process.exit(1);
    }

    const indexHtml = fs.readFileSync(indexHtmlPath, 'utf8');
    const $ = cheerio.load(indexHtml);
    const topics = [];

    $('.syllabus-list .syllabus-item a').each((i, el) => {
        const href = $(el).attr('href') || '';
        const text = $(el).find('.syllabus-text').text().trim();
        const parts = href.split('/').filter(Boolean);
        const folderName = parts[parts.length - 1];

        let name = text;
        let hindiName = text;
        const match = text.match(/^(.*?)\s*\((.*?)\)$/);
        if (match) {
            name = match[1].trim();
            hindiName = match[2].trim();
        }

        topics.push({
            dir: folderName,
            name: name,
            hindiName: hindiName,
            description: `${name} - syllabus concepts, notes, and trackers for UP Assistant Teacher Exam.`,
            keywords: [name, 'Environmental & Social Studies', 'UP Assistant Teacher', 'Civics', 'History', 'Geography']
        });
    });

    const totalTopics = topics.length;
    let successCount = 0;
    let failCount = 0;

    for (let i = 0; i < totalTopics; i++) {
        const topic = topics[i];
        console.log(`\n${'='.repeat(80)}`);
        console.log(`[${i + 1}/${totalTopics}] Processing: ${topic.name} (${topic.hindiName})`);
        console.log(`${'='.repeat(80)}`);

        const outputDir = path.join(process.cwd(), 'up-assistant-teacher', 'environmental-social-studies', topic.dir);
        
        // Skip if index.html already exists and is NOT a placeholder
        const indexHtmlPath = path.join(outputDir, 'index.html');
        if (fs.existsSync(indexHtmlPath)) {
            const htmlContent = fs.readFileSync(indexHtmlPath, 'utf8');
            if (!htmlContent.includes('Content under preparation') && !htmlContent.includes('under preparation')) {
                console.log(`  ⏭️ Skipping: ${topic.name} (already fully generated)`);
                continue;
            }
        }

        fs.mkdirSync(outputDir, { recursive: true });
        const tabsDir = path.join(outputDir, 'tabs');
        fs.mkdirSync(tabsDir, { recursive: true });

        let conceptsData = null;

        try {
            console.log('  📝 Generating concepts/theories content via Gemini...');
            const prompt = buildConceptsPrompt(topic);
            const raw = await callGemini(prompt);
            console.log(`  ℹ️ Gemini raw response length: ${raw.length}`);
            let parsed;
            try {
                parsed = parseResponse(raw);
            } catch (parseErr) {
                fs.writeFileSync(path.join(outputDir, 'failed_response.txt'), raw, 'utf8');
                throw parseErr;
            }

            if (!parsed.sections || !Array.isArray(parsed.sections) || parsed.sections.length === 0) {
                throw new Error('Generated content missing "sections" array');
            }

            const paragraphSections = parsed.sections.filter(s => s.type === 'paragraph');
            if (paragraphSections.length > 0) {
                console.log('  ⚠️ Found paragraph sections — converting to list format...');
                parsed.sections = parsed.sections.map(section => {
                    if (section.type === 'paragraph') {
                        return { title: section.title, type: 'list', items: [{ term: 'Key Point', definition: section.content || '' }] };
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

        const html = assembleMicrotopicPage(topic, conceptsData);
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
}

main().catch(err => {
    console.error('Fatal error:', err);
    process.exit(1);
});