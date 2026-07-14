require('dotenv').config();
const fs = require('fs');
const path = require('path');
const cheerio = require('cheerio');
const { GoogleGenAI } = require('@google/genai');

const ai = new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY });

const indexHtmlPath = path.join(__dirname, '../upsc/index.html');

async function translateBatch(texts) {
    const prompt = `You are an expert translator. Translate the following English UPSC syllabus topics into Hindi. 
Return ONLY a valid JSON array of strings, where each string is the exact Hindi translation of the corresponding English string in the same order. Do not include markdown formatting or any other text.

English Texts:
${JSON.stringify(texts, null, 2)}`;

    try {
        const response = await ai.models.generateContent({
            model: 'gemini-2.5-flash',
            contents: prompt,
            config: {
                temperature: 0.2
            }
        });
        
        let out = response.text;
        // Clean up markdown code blocks if any
        out = out.replace(/```json/g, '').replace(/```/g, '').trim();
        return JSON.parse(out);
    } catch (e) {
        console.error("Error translating batch:", e.message);
        return null;
    }
}

function chunkArray(arr, size) {
    const chunks = [];
    for(let i = 0; i < arr.length; i += size) {
        chunks.push(arr.slice(i, i + size));
    }
    return chunks;
}

async function run() {
    console.log("Loading upsc/index.html...");
    let html = fs.readFileSync(indexHtmlPath, 'utf8');
    const $ = cheerio.load(html, { decodeEntities: false });
    
    // We need to collect elements and their texts
    const elementsToTranslate = [];
    
    // 1. Subject Titles
    $('.subject-title a').each((i, el) => {
        // Text node after the <i> tag
        const clone = $(el).clone();
        clone.find('i').remove();
        const text = clone.text().trim();
        if (text) {
            elementsToTranslate.push({ type: 'subject', el: $(el), text: text });
        }
    });
    
    // 2. Subsection Titles
    $('.subsection-title').each((i, el) => {
        const text = $(el).text().trim();
        if (text) {
            elementsToTranslate.push({ type: 'subsection', el: $(el), text: text });
        }
    });
    
    // 3. Topic Items
    $('.topic-item').each((i, el) => {
        const clone = $(el).clone();
        clone.find('i').remove();
        const text = clone.text().trim();
        if (text) {
            elementsToTranslate.push({ type: 'topic', el: $(el), text: text });
        }
    });
    
    console.log(`Found ${elementsToTranslate.length} unique elements to translate.`);
    
    const uniqueTexts = [...new Set(elementsToTranslate.map(e => e.text))];
    console.log(`Unique strings to translate: ${uniqueTexts.length}`);
    
    const textToHindi = {};
    
    // Check if we already have a cached translation (in case it fails midway)
    const cacheFile = path.join(__dirname, 'translation_cache.json');
    if (fs.existsSync(cacheFile)) {
        const cache = JSON.parse(fs.readFileSync(cacheFile, 'utf8'));
        Object.assign(textToHindi, cache);
        console.log(`Loaded ${Object.keys(textToHindi).length} translations from cache.`);
    }
    
    const toTranslate = uniqueTexts.filter(t => !textToHindi[t]);
    
    if (toTranslate.length > 0) {
        console.log(`Need to translate ${toTranslate.length} strings via API.`);
        const chunks = chunkArray(toTranslate, 100);
        
        for (let i = 0; i < chunks.length; i++) {
            console.log(`Translating chunk ${i+1}/${chunks.length}...`);
            const chunk = chunks[i];
            const translatedChunk = await translateBatch(chunk);
            
            if (translatedChunk && translatedChunk.length === chunk.length) {
                for (let j = 0; j < chunk.length; j++) {
                    textToHindi[chunk[j]] = translatedChunk[j];
                }
                fs.writeFileSync(cacheFile, JSON.stringify(textToHindi, null, 2));
            } else {
                console.error("Mismatch in translation chunk or error occurred. Aborting.");
                process.exit(1);
            }
            
            // Wait 2 seconds to avoid rate limits
            await new Promise(r => setTimeout(r, 2000));
        }
    }
    
    console.log("Applying translations to HTML...");
    
    elementsToTranslate.forEach(item => {
        const hiText = textToHindi[item.text];
        if (!hiText) return;
        
        if (item.type === 'subject' || item.type === 'topic') {
            const icon = item.el.find('i').prop('outerHTML') || '';
            item.el.html(`${icon} <span class="lang-en">${item.text}</span><span class="lang-hi" style="display:none;">${hiText}</span>`);
        } else if (item.type === 'subsection') {
            item.el.html(`<span class="lang-en">${item.text}</span><span class="lang-hi" style="display:none;">${hiText}</span>`);
        }
    });
    
    fs.writeFileSync(indexHtmlPath, $.html());
    console.log("Successfully updated upsc/index.html with dual languages!");
}

run();
