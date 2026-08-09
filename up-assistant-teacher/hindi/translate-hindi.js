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
const REQUEST_DELAY_MS = 10000;
const MAX_RETRIES = 5;
let currentModel = 'gemini-3.1-flash-lite';

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
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    contents: [{ parts: [{ text: prompt }] }],
                    generationConfig: { temperature: 0.1, maxOutputTokens: 65536, topP: 0.95, responseMimeType: 'application/json' },
                }),
            });

            if (res.status === 429 || res.status === 403) {
                const wait = 15000 * Math.pow(2, attempt - 1);
                console.log(`  ⏳ Rate limited (429). Waiting ${wait / 1000}s before retry ${attempt}/${retries}...`);
                await sleep(wait);
                continue;
            }

            if (res.status === 503) {
                const wait = 20000;
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

function extractValidJson(raw) {
    let startIdx = raw.indexOf('{');
    if (startIdx === -1) startIdx = raw.indexOf('[');
    if (startIdx === -1) return raw;

    let openBraces = 0, inString = false, escape = false, hasStarted = false;
    for (let i = startIdx; i < raw.length; i++) {
        const char = raw[i];
        if (escape) { escape = false; continue; }
        if (char === '\\') { escape = true; continue; }
        if (char === '"') { inString = !inString; continue; }
        if (!inString) {
            if (char === '{' || char === '[') { openBraces++; hasStarted = true; }
            else if (char === '}' || char === ']') { openBraces--; }
            if (hasStarted && openBraces === 0) return raw.substring(startIdx, i + 1);
        }
    }
    return raw;
}

function parseResponse(raw) {
    let cleaned = raw.trim();
    if (cleaned.startsWith('```json')) cleaned = cleaned.replace(/^```json\s*/, '').replace(/\s*```$/, '');
    else if (cleaned.startsWith('```')) cleaned = cleaned.replace(/^```\s*/, '').replace(/\s*```$/, '');
    cleaned = cleaned.replace(/[\u2018\u2019]/g, "'").replace(/[\u201c\u201d]/g, '"');

    const extracted = extractValidJson(cleaned);
    try { return JSON.parse(extracted); } catch (err) {
        console.error('Failed to parse directly. Error:', err.message);
        const posMatch = err.message.match(/position (\d+)/);
        if (posMatch) {
            const pos = parseInt(posMatch[1], 10);
            console.error('Context around position:', extracted.substring(Math.max(0, pos - 100), Math.min(extracted.length, pos + 100)));
        }
    }

    const jsonMatch = extracted.match(/[\{\[][\s\S]*[\}\]]/);
    if (jsonMatch) {
        try { return JSON.parse(jsonMatch[0]); } catch (e) {
            console.error('Failed to parse regex match. Error:', e.message);
            const posMatch = e.message.match(/position (\d+)/);
            if (posMatch) {
                const pos = parseInt(posMatch[1], 10);
                console.error('Context around regex position:', jsonMatch[0].substring(Math.max(0, pos - 100), Math.min(jsonMatch[0].length, pos + 100)));
            }
        }
    }

    console.error('Raw response length:', cleaned.length);
    throw new Error('Could not parse valid JSON from Gemini response');
}

// ============================================================================
// TRANSLATION ENGINE (Hindi only)
// ============================================================================
async function translateConcepts(conceptsJson) {
    console.log(`    🧩 Translating concepts JSON in chunks to avoid token limits...`);
    const hindiConcepts = { sections: [], upscNotes: [], keyTakeaways: [] };

    for (let s = 0; s < conceptsJson.sections.length; s++) {
        const section = conceptsJson.sections[s];
        console.log(`      🔸 Translating section ${s + 1}/${conceptsJson.sections.length}...`);
        const sectionPrompt = `You are a professional English-to-Hindi translator specializing in Hindi subject notes for the UP Assistant Teacher exam. Translate the following single section of exam prep notes entirely into Hindi.
Replace every English text string in the JSON with its natural, accurate Hindi translation. Keep structural keys and layout values (like "type": "table", "type": "list", "type": "subcards") as simple strings unchanged. Preserve all markdown formatting (**, *, etc.).
Return ONLY valid JSON matching the exact same structure — all text values must be in Hindi only (no English).

Here is the Section JSON:
${JSON.stringify(section, null, 2)}`;

        const rawSec = await callGemini(sectionPrompt);
        const translatedSec = parseResponse(rawSec);
        hindiConcepts.sections.push(translatedSec);
        await sleep(1500);
    }

    if (conceptsJson.upscNotes && conceptsJson.upscNotes.length > 0) {
        console.log(`      🔸 Translating upscNotes...`);
        const notesPrompt = `You are a professional English-to-Hindi translator for Hindi subject notes. Translate the following list of notes into Hindi.
Replace every English text string with its natural, accurate Hindi translation. Keep the "type" key as a simple string. Preserve markdown.
Return ONLY valid JSON matching the array structure — all text values must be in Hindi only.

Notes JSON:
${JSON.stringify(conceptsJson.upscNotes, null, 2)}`;

        const rawNotes = await callGemini(notesPrompt);
        hindiConcepts.upscNotes = parseResponse(rawNotes);
        await sleep(1500);
    }

    if (conceptsJson.keyTakeaways && conceptsJson.keyTakeaways.length > 0) {
        console.log(`      🔸 Translating keyTakeaways...`);
        const takeawaysPrompt = `You are a professional English-to-Hindi translator for Hindi subject notes. Translate the following list of key takeaways into Hindi.
Replace each English string with its natural, accurate Hindi translation. Preserve markdown.
Return ONLY valid JSON matching the array structure — all text values must be in Hindi only.

Takeaways JSON:
${JSON.stringify(conceptsJson.keyTakeaways, null, 2)}`;

        const rawTakeaways = await callGemini(takeawaysPrompt);
        hindiConcepts.keyTakeaways = parseResponse(rawTakeaways);
    }

    return hindiConcepts;
}

// ============================================================================
// UPDATE index.html (no regex - string split to avoid escaping issues)
// ============================================================================
function updateIndexHtml(indexPath, hindiConcepts) {
    if (!fs.existsSync(indexPath)) return;
    let html = fs.readFileSync(indexPath, 'utf8');
    const TAG_OPEN = '<script id="upsc-page-data" type="application/json">';
    const TAG_CLOSE = '</script>';
    const startIdx = html.indexOf(TAG_OPEN);
    if (startIdx === -1) {
        console.warn('  ⚠️ Could not find <script id="upsc-page-data"> in index.html');
        return;
    }
    const contentStart = startIdx + TAG_OPEN.length;
    const endIdx = html.indexOf(TAG_CLOSE, contentStart);
    if (endIdx === -1) {
        console.warn('  ⚠️ Closing </script> not found in index.html');
        return;
    }
    try {
        const pageData = JSON.parse(html.slice(contentStart, endIdx).trim());
        pageData.concepts = hindiConcepts;
        const updatedJson = JSON.stringify(pageData, null, 2);
        html = html.slice(0, contentStart) + '\n' + updatedJson + '\n' + html.slice(endIdx);
        fs.writeFileSync(indexPath, html, 'utf8');
        console.log('  💾 Updated index.html inline data');
    } catch (e) {
        console.error('  ❌ Error updating index.html JSON block:', e.message);
    }
}

// ============================================================================
// MAIN PIPELINE
// ============================================================================
async function main() {
    const targetDir = path.join(process.cwd(), 'up-assistant-teacher', 'hindi');
    const topics = fs.readdirSync(targetDir).filter(f => {
        const fullPath = path.join(targetDir, f);
        return fs.statSync(fullPath).isDirectory() && fs.existsSync(path.join(fullPath, 'tabs', 'concepts.json'));
    });

    console.log(`Found ${topics.length} Hindi topics to translate.`);

    const filterTopic = process.argv[2];
    const topicsToProcess = filterTopic ? topics.filter(t => t === filterTopic) : topics;

    if (filterTopic && topicsToProcess.length === 0) {
        console.error(`Topic "${filterTopic}" not found or missing concepts.json.`);
        process.exit(1);
    }

    for (let i = 0; i < topicsToProcess.length; i++) {
        const topic = topicsToProcess[i];
        const topicPath = path.join(targetDir, topic);
        const conceptsPath = path.join(topicPath, 'tabs', 'concepts.json');
        const dataPath = path.join(topicPath, 'data.json');
        const indexPath = path.join(topicPath, 'index.html');

        console.log(`\n[${i + 1}/${topicsToProcess.length}] Translating Hindi topic: ${topic}`);

        try {
            const concepts = JSON.parse(fs.readFileSync(conceptsPath, 'utf8'));

            // Skip if already translated — Hindi titles contain Devanagari characters
            const firstTitle = concepts.sections?.[0]?.title;
            const isDevanagari = typeof firstTitle === 'string' && /[\u0900-\u097F]/.test(firstTitle);
            if (!firstTitle || isDevanagari) {
                console.log('  ⏭️ Already translated. Skipping...');
                continue;
            }

            console.log('  🌐 Sending to Gemini for Hindi translation...');
            const hindiConcepts = await translateConcepts(concepts);

            fs.writeFileSync(conceptsPath, JSON.stringify(hindiConcepts, null, 2), 'utf8');
            console.log('  💾 Updated tabs/concepts.json');

            if (fs.existsSync(dataPath)) {
                const data = JSON.parse(fs.readFileSync(dataPath, 'utf8'));
                data.concepts = hindiConcepts;
                fs.writeFileSync(dataPath, JSON.stringify(data, null, 2), 'utf8');
                console.log('  💾 Updated data.json');
            }

            updateIndexHtml(indexPath, hindiConcepts);

            console.log(`  ✅ Successfully translated: ${topic}`);

            if (i < topicsToProcess.length - 1) {
                console.log(`  ⏳ Waiting ${REQUEST_DELAY_MS / 1000}s to prevent rate limits...`);
                await sleep(REQUEST_DELAY_MS);
            }
        } catch (e) {
            console.error(`  ❌ Failed to process ${topic}:`, e.message);
        }
    }

    console.log('\n🎉 Hindi translation process complete!');
}

main().catch(err => {
    console.error('Fatal error:', err);
    process.exit(1);
});
