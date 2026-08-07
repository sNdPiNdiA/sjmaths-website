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
const REQUEST_DELAY_MS = 6000; // Delay between calls to prevent rate limits
const MAX_RETRIES = 5;
let currentModel = 'gemini-2.5-flash';

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
                        responseMimeType: "application/json"
                    },
                }),
            });

            if (res.status === 429 || res.status === 403) {
                if (currentModel === 'gemini-2.5-flash') {
                    console.log(`  ⚠️ Model ${currentModel} rate limited. Switching to fallback model gemini-3.1-flash-lite...`);
                    currentModel = 'gemini-3.1-flash-lite';
                    continue;
                }
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

function extractValidJson(raw) {
    let startIdx = raw.indexOf('{');
    if (startIdx === -1) startIdx = raw.indexOf('[');
    if (startIdx === -1) return raw;

    let openBraces = 0;
    let inString = false;
    let escape = false;
    let hasStarted = false;

    for (let i = startIdx; i < raw.length; i++) {
        const char = raw[i];
        if (escape) {
            escape = false;
            continue;
        }
        if (char === '\\') {
            escape = true;
            continue;
        }
        if (char === '"') {
            inString = !inString;
            continue;
        }
        if (!inString) {
            if (char === '{' || char === '[') {
                openBraces++;
                hasStarted = true;
            } else if (char === '}' || char === ']') {
                openBraces--;
            }
            if (hasStarted && openBraces === 0) {
                return raw.substring(startIdx, i + 1);
            }
        }
    }
    return raw;
}

function parseResponse(raw) {
    let cleaned = raw.trim();
    if (cleaned.startsWith('```json')) cleaned = cleaned.replace(/^```json\s*/, '').replace(/\s*```$/, '');
    else if (cleaned.startsWith('```')) cleaned = cleaned.replace(/^```\s*/, '').replace(/\s*```$/, '');

    cleaned = cleaned.replace(/[\u2018\u2019]/g, "'").replace(/[\u201c\u201d]/g, '"');

    // Try extracting valid JSON block using balanced brackets
    const extracted = extractValidJson(cleaned);

    try { return JSON.parse(extracted); } catch (err) {
        console.error("Failed to parse directly. Error:", err.message);
        const posMatch = err.message.match(/position (\d+)/);
        if (posMatch) {
            const pos = parseInt(posMatch[1], 10);
            console.error("Context around position:", extracted.substring(Math.max(0, pos - 100), Math.min(extracted.length, pos + 100)));
        }
    }

    const jsonMatch = extracted.match(/[\{\[][\s\S]*[\}\]]/);
    if (jsonMatch) {
        try { return JSON.parse(jsonMatch[0]); } catch (e) {
            console.error("Failed to parse regex match. Error:", e.message);
            const posMatch = e.message.match(/position (\d+)/);
            if (posMatch) {
                const pos = parseInt(posMatch[1], 10);
                console.error("Context around regex position:", jsonMatch[0].substring(Math.max(0, pos - 100), Math.min(jsonMatch[0].length, pos + 100)));
            }
        }
    }
    
    console.error("Raw response length:", cleaned.length);
    throw new Error('Could not parse valid JSON from Gemini response');
}

// ============================================================================
// TRANSLATION ENGINE
// ============================================================================
async function translateConcepts(conceptsJson) {
    console.log(`    🧩 Translating concepts JSON in chunks to avoid token limits...`);
    const bilingualConcepts = {
        sections: [],
        upscNotes: [],
        keyTakeaways: []
    };

    // 1. Translate sections one by one
    for (let s = 0; s < conceptsJson.sections.length; s++) {
        const section = conceptsJson.sections[s];
        console.log(`      🔸 Translating section ${s + 1}/${conceptsJson.sections.length}...`);
        const sectionPrompt = `You are a professional English-to-Hindi translator specializing in Geography exam prep notes. Translate the following single section of exam prep notes into a BILINGUAL format.
For every text string in the JSON (including title, headers, table cells, lists, definitions, terms, subcard content, etc.), convert it into a bilingual object:
{
  "en": "Original English string",
  "hi": "Accurate, clean, and natural Hindi translation"
}
Keep structural keys and layout values (like "type": "table", "type": "list", "type": "subcards") as simple strings. Maintain all markdown formatting like **, *, •, \n.
Return ONLY valid JSON matching this exact section structure.

Here is the Section JSON:
${JSON.stringify(section, null, 2)}`;

        const rawSec = await callGemini(sectionPrompt);
        const translatedSec = parseResponse(rawSec);
        bilingualConcepts.sections.push(translatedSec);
        await sleep(1500); // Small sleep between chunk calls to be safe
    }

    // 2. Translate upscNotes
    if (conceptsJson.upscNotes && conceptsJson.upscNotes.length > 0) {
        console.log(`      🔸 Translating upscNotes...`);
        const notesPrompt = `You are a professional English-to-Hindi translator specializing in Geography notes. Translate the following list of notes/tips into a BILINGUAL format.
For the "content" of each note, convert the string into a bilingual object:
{
  "en": "Original English content",
  "hi": "Accurate and natural Hindi translation"
}
Keep the "type" key (e.g. "tip", "trap") as a simple string. Maintain all markdown formatting.
Return ONLY valid JSON matching the array structure.

Here is the notes JSON:
${JSON.stringify(conceptsJson.upscNotes, null, 2)}`;

        const rawNotes = await callGemini(notesPrompt);
        bilingualConcepts.upscNotes = parseResponse(rawNotes);
        await sleep(1500);
    }

    // 3. Translate keyTakeaways
    if (conceptsJson.keyTakeaways && conceptsJson.keyTakeaways.length > 0) {
        console.log(`      🔸 Translating keyTakeaways...`);
        const takeawaysPrompt = `You are a professional English-to-Hindi translator specializing in Geography notes. Translate the following list of key takeaways into a BILINGUAL format.
Convert each string in the array into a bilingual object:
{
  "en": "Original English takeaway",
  "hi": "Accurate and natural Hindi translation"
}
Maintain all markdown formatting.
Return ONLY valid JSON matching the array structure.

Here is the takeaways JSON:
${JSON.stringify(conceptsJson.keyTakeaways, null, 2)}`;

        const rawTakeaways = await callGemini(takeawaysPrompt);
        bilingualConcepts.keyTakeaways = parseResponse(rawTakeaways);
    }

    return bilingualConcepts;
}

// ============================================================================
// MAIN PIPELINE
// ============================================================================
async function main() {
    const targetDir = path.join(process.cwd(), 'upsssc-pet', 'geography');
    const topics = fs.readdirSync(targetDir).filter(f => {
        const fullPath = path.join(targetDir, f);
        return fs.statSync(fullPath).isDirectory() && fs.existsSync(path.join(fullPath, 'tabs', 'concepts.json'));
    });

    console.log(`Found ${topics.length} Geography topics to translate.`);

    const filterTopic = process.argv[2];
    const topicsToProcess = filterTopic ? topics.filter(t => t === filterTopic) : topics;

    if (filterTopic && topicsToProcess.length === 0) {
        console.error(`Topic "${filterTopic}" not found or doesn't have concepts.json.`);
        process.exit(1);
    }

    for (let i = 0; i < topicsToProcess.length; i++) {
        const topic = topicsToProcess[i];
        const topicPath = path.join(targetDir, topic);
        const conceptsPath = path.join(topicPath, 'tabs', 'concepts.json');
        const dataPath = path.join(topicPath, 'data.json');
        const indexPath = path.join(topicPath, 'index.html');

        console.log(`\n[${i + 1}/${topicsToProcess.length}] Translating Geography topic: ${topic}`);

        try {
            // 1. Read and check if already translated
            const concepts = JSON.parse(fs.readFileSync(conceptsPath, 'utf8'));
            
            // Check first section title to see if it's already translated
            if (concepts.sections && concepts.sections[0] && typeof concepts.sections[0].title === 'object') {
                console.log(`  ⏭️ Already translated. Skipping...`);
                continue;
            }

            console.log(`  🌐 Sending to Gemini for bilingual translation...`);
            const bilingualConcepts = await translateConcepts(concepts);

            // 2. Save tabs/concepts.json
            fs.writeFileSync(conceptsPath, JSON.stringify(bilingualConcepts, null, 2), 'utf8');
            console.log(`  💾 Updated tabs/concepts.json`);

            // 3. Save data.json
            if (fs.existsSync(dataPath)) {
                const data = JSON.parse(fs.readFileSync(dataPath, 'utf8'));
                data.concepts = bilingualConcepts;
                fs.writeFileSync(dataPath, JSON.stringify(data, null, 2), 'utf8');
                console.log(`  💾 Updated data.json`);
            }

            // 4. Update index.html
            if (fs.existsSync(indexPath)) {
                let html = fs.readFileSync(indexPath, 'utf8');
                const scriptRegex = /(<script id="upsc-page-data" type="application\/json">)([\s\S]*?)(<\/script>)/;
                const match = html.match(scriptRegex);
                if (match) {
                    try {
                        const pageData = JSON.parse(match[2].trim());
                        pageData.concepts = bilingualConcepts;
                        const updatedJson = JSON.stringify(pageData, null, 2);
                        html = html.replace(scriptRegex, `$1\n${updatedJson}\n$3`);
                        fs.writeFileSync(indexPath, html, 'utf8');
                        console.log(`  💾 Updated index.html inline data`);
                    } catch (e) {
                        console.error(`  ❌ Error updating index.html JSON block:`, e.message);
                    }
                } else {
                    console.warn(`  ⚠️ Could not find <script id="upsc-page-data"> in index.html`);
                }
            }

            console.log(`  ✅ Successfully translated: ${topic}`);

            if (i < topicsToProcess.length - 1) {
                console.log(`  ⏳ Waiting ${REQUEST_DELAY_MS / 1000}s to prevent rate limits...`);
                await sleep(REQUEST_DELAY_MS);
            }
        } catch (e) {
            console.error(`  ❌ Failed to process ${topic}:`, e.message);
        }
    }

    console.log('\n🎉 Geography translation process complete!');
}

main().catch(err => {
    console.error('Fatal error:', err);
    process.exit(1);
});
