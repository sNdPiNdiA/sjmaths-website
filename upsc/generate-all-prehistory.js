/**
 * UPSC Batch Generator for Remaining Prehistory Topics
 */

import fs from 'fs';
import path from 'path';

// Load .env
if (fs.existsSync('.env')) {
    const envConfig = fs.readFileSync('.env', 'utf8');
    envConfig.split('\n').forEach(line => {
        const [key, value] = line.split('=');
        if (key && value) {
            process.env[key.trim()] = value.trim();
        }
    });
}

import {
    validateMetadata,
    generatePrompt,
    parseResponse,
    normalizeContent,
    translateToBilingual,
    generateSha256Hash,
    PageScorer,
    QualityControl,
    GeminiClient,
    assemblePage,
    createManifest,
    createLogEntry,
    DEFAULT_GLOSSARY,
    VERSION,
} from './upsc-microtopic-template.js';

const apiKey = process.env.GEMINI_API_KEY;
if (!apiKey) {
    console.error('❌ GEMINI_API_KEY is not set in environment or .env');
    process.exit(1);
}

const topics = [
    {
        name: 'Sources of Information of Pre-History',
        hindiName: 'प्राऐरिशियन इतिहास के स्रोत',
        dir: 'Sources-of-Information-of-Pre-History',
        previousTopic: 'Introduction',
        previousDir: '',
        previousTopicHi: 'परिचय',
        nextTopic: 'Prehistoric Time Periods',
        nextDir: 'Prehistoric-Time-Periods',
        nextTopicHi: 'प्राऐरिशियन समय अवधारणाएँ',
        description: 'Study of archaeological sources, fossils, artifacts, stratigraphy, and radio-carbon dating methods used to reconstruct Indian prehistory.'
    },
    {
        name: 'History of Paleolithic or Old Stone Age',
        hindiName: 'पुरापाषाण या पुराना पत्थर काल का इतिहास',
        dir: 'History-of-Paleolithic-or-Old-Stone-Age',
        previousTopic: 'Prehistoric Time Periods',
        previousDir: 'Prehistoric-Time-Periods',
        previousTopicHi: 'प्राऐरिशियन समय अवधारणाएँ',
        nextTopic: 'History of Mesolithic or Middle Stone Age',
        nextDir: 'History-of-Mesolithic-or-Middle-Stone-Age',
        nextTopicHi: 'मध्यपाषाण या मध्य पाषाण काल का इतिहास',
        description: 'Comprehensive analysis of the Paleolithic Age (Lower, Middle, Upper), tool traditions (Acheulian, Soanian), hominin evolution, and major sites.'
    },
    {
        name: 'History of Mesolithic or Middle Stone Age',
        hindiName: 'मध्यपाषाण या मध्य पाषाण काल का इतिहास',
        dir: 'History-of-Mesolithic-or-Middle-Stone-Age',
        previousTopic: 'History of Paleolithic or Old Stone Age',
        previousDir: 'History-of-Paleolithic-or-Old-Stone-Age',
        previousTopicHi: 'पुरापाषाण या पुराना पत्थर काल का इतिहास',
        nextTopic: 'History of Neolithic Age or New Stone Age',
        nextDir: 'History-of-Neolithic-Age-or-New-Stone-Age',
        nextTopicHi: 'नवपाषाण या नया पत्थर काल का इतिहास',
        description: 'Exploration of the Mesolithic transitional phase, microlith technology, animal domestication, rock art, and key sites like Bagor and Adamgarh.'
    },
    {
        name: 'History of Neolithic Age or New Stone Age',
        hindiName: 'नवपाषाण या नया पत्थर काल का इतिहास',
        dir: 'History-of-Neolithic-Age-or-New-Stone-Age',
        previousTopic: 'History of Mesolithic or Middle Stone Age',
        previousDir: 'History-of-Mesolithic-or-Middle-Stone-Age',
        previousTopicHi: 'मध्यपाषाण या मध्य पाषाण काल का इतिहास',
        nextTopic: 'History of Chalcolithic Age',
        nextDir: 'History-of-Chalcolithic-Age',
        nextTopicHi: 'ताम्रपाषाण काल का इतिहास',
        description: 'Study of the Neolithic Revolution, settled agriculture, pottery, polished stone axes, pit dwellings at Burzahom, and Mehrgarh.'
    },
    {
        name: 'History of Chalcolithic Age',
        hindiName: 'ताम्रपाषाण काल का इतिहास',
        dir: 'History-of-Chalcolithic-Age',
        previousTopic: 'History of Neolithic Age or New Stone Age',
        previousDir: 'History-of-Neolithic-Age-or-New-Stone-Age',
        previousTopicHi: 'नवपाषाण या नया पत्थर काल का इतिहास',
        nextTopic: 'History of Early Iron Age',
        nextDir: 'History-of-Early-Iron-Age',
        nextTopicHi: 'प्रारंभिक लौह युग का इतिहास',
        description: 'Detailed review of the copper-stone age, painted pottery cultures (Ahar, Kayatha, Jorwe), village farming economies, and limitations.'
    },
    {
        name: 'History of Early Iron Age',
        hindiName: 'प्रारंभिक लौह युग का इतिहास',
        dir: 'History-of-Early-Iron-Age',
        previousTopic: 'History of Chalcolithic Age',
        previousDir: 'History-of-Chalcolithic-Age',
        previousTopicHi: 'ताम्रपाषाण काल का इतिहास',
        nextTopic: 'Geographical Distribution and Characteristics of Pre-History',
        nextDir: 'Geographical-Distribution-and-Characteristics-of-Pre-History',
        nextTopicHi: 'प्रागैतिहास का भौगोलिक वितरण और विशेषताएँ',
        description: 'Analysis of the transition to iron technology, Megalithic culture in South India, Painted Grey Ware (PGW), and socio-economic transformation.'
    },
    {
        name: 'Geographical Distribution and Characteristics of Pre-History',
        hindiName: 'प्रागैतिहास का भौगोलिक वितरण और विशेषताएँ',
        dir: 'Geographical-Distribution-and-Characteristics-of-Pre-History',
        previousTopic: 'History of Early Iron Age',
        previousDir: 'History-of-Early-Iron-Age',
        previousTopicHi: 'प्रारंभिक लौह युग का इतिहास',
        nextTopic: 'Indus Valley Civilization',
        nextDir: '../Indus-Valley-Civilization/',
        nextTopicHi: 'सिंधु घाटी सभ्यता',
        description: 'Geographical mapping of prehistoric sites across river valleys, topography, and overarching socio-economic characteristics in the Indian subcontinent.'
    }
];

function collectStrings(obj, strings = new Set()) {
    if (typeof obj === 'string') {
        strings.add(obj);
    } else if (Array.isArray(obj)) {
        obj.forEach(item => collectStrings(item, strings));
    } else if (typeof obj === 'object' && obj !== null) {
        Object.values(obj).forEach(v => collectStrings(v, strings));
    }
    return strings;
}

function applyGlossary(text, glossary) {
    let result = text;
    for (const [en, hi] of Object.entries(glossary)) {
        const escaped = en.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
        const regex = new RegExp(`\\b${escaped}\\b`, 'gi');
        result = result.replace(regex, hi);
    }
    return result;
}

async function batchTranslate(stringsSet, client) {
    const strings = Array.from(stringsSet);
    const translations = new Map();
    const batchSize = 30;
    const totalBatches = Math.ceil(strings.length / batchSize);

    for (let i = 0; i < strings.length; i += batchSize) {
        const batch = strings.slice(i, i + batchSize);
        const batchNum = Math.floor(i / batchSize) + 1;

        const prompt = `Translate the following ${batch.length} English strings into Hindi for UPSC exam study notes. Keep technical terms, archaeological site names, and tool names recognizable in Devanagari or English script as appropriate. Return ONLY a valid JSON array of strings in the exact same order.\n\nJSON Array:\n` + JSON.stringify(batch);

        try {
            const result = await client.generate(prompt);
            const parsed = parseResponse(result);
            if (Array.isArray(parsed)) {
                for (let j = 0; j < batch.length && j < parsed.length; j++) {
                    translations.set(batch[j], String(parsed[j]).trim());
                }
            } else {
                throw new Error('Not an array');
            }
        } catch (err) {
            console.warn(`  Batch ${batchNum} failed: ${err.message}. Using fallback.`);
            for (let j = 0; j < batch.length; j++) {
                translations.set(batch[j], batch[j]);
            }
        }
    }
    return translations;
}

async function generateTab(tabName, meta, contentClient, translationClient) {
    const prompt = generatePrompt(tabName, meta);
    const raw = await contentClient.generate(prompt);
    const englishJson = parseResponse(raw);
    const normalized = normalizeContent(englishJson);

    const scorer = new PageScorer(meta);
    const score = scorer.score(tabName, normalized);

    const allStrings = collectStrings(normalized);
    const mergedGlossary = { ...DEFAULT_GLOSSARY };
    const glossaryAppliedStrings = new Set();
    for (const str of allStrings) {
        glossaryAppliedStrings.add(applyGlossary(str, mergedGlossary));
    }

    const translations = await batchTranslate(glossaryAppliedStrings, translationClient);
    const translateFn = (text, targetLang) => {
        if (targetLang !== 'hi') return text;
        return translations.get(text) || text;
    };

    const bilingualData = await translateToBilingual(normalized, translateFn, mergedGlossary);
    const contentHash = generateSha256Hash(bilingualData);

    return {
        data: bilingualData,
        score,
        contentHash,
        duration: 1000
    };
}

async function main() {
    const contentClient = new GeminiClient(apiKey, {
        model: 'gemini-3.5-flash-lite',
        temperature: 0.1,
        maxRetries: 5,
        requestDelay: 12000,
    });

    const translationClient = new GeminiClient(apiKey, {
        model: 'gemini-3.5-flash-lite',
        temperature: 0.1,
        maxRetries: 5,
        requestDelay: 12000,
    });

    const tabs = ['overview', 'concepts', 'visual', 'comparisons', 'practice', 'mains', 'revision', 'test'];

    for (let i = 0; i < topics.length; i++) {
        const t = topics[i];
        console.log(`\n${'#'.repeat(70)}`);
        console.log(`[Topic ${i + 1}/${topics.length}] Generating: ${t.name}`);
        console.log(`${'#'.repeat(70)}`);

        const meta = {
            name: t.name,
            hindiName: t.hindiName,
            dir: t.dir,
            subject: 'Ancient History',
            subjectDir: 'ancient-history',
            parentTopic: 'Prehistory',
            parentDir: 'Prehistory',
            previousTopic: t.previousTopic,
            previousDir: t.previousDir,
            previousTopicHi: t.previousTopicHi,
            nextTopic: t.nextTopic,
            nextDir: t.nextDir,
            nextTopicHi: t.nextTopicHi,
            parentTopicHi: 'प्राऐरिशियन',
            childTopics: [],
            childDirs: [],
            childTopicsHi: [],
            similarTopics: [],
            similarDirs: [],
            similarTopicsHi: [],
            confusedTopics: [],
            confusedDirs: [],
            confusedTopicsHi: [],
            canonicalUrl: `https://sjmaths.com/upsc/ancient-history/Prehistory/${t.dir}/`,
            description: t.description,
            category: 'GS-1',
            supportsMains: true,
            topicId: `ancient-history.prehistory.${t.dir.toLowerCase()}`,
            practiceTypes: ['basic', 'conceptual', 'statement', 'match'],
            difficulty: 'medium',
            studyTime: { concepts: 20, practice: 15, revision: 8 },
            learningObjectives: [
                `Understand key aspects and historical significance of ${t.name}`,
                'Analyze archaeological evidence, site distribution, and socio-economic patterns',
                'Examine UPSC Prelims and Mains dimensions related to this prehistoric phase'
            ],
            scope: {
                mustExplain: [t.name, 'Archaeological evidence', 'Chronology and significance'],
                mayMention: ['Sites', 'Dating techniques'],
                neverExplain: ['Later historical periods'],
                relatedTopics: [t.name],
                keywords: ['prehistory', 'ancient history', 'upsc', t.name.toLowerCase()]
            },
            related: {
                prerequisite: [t.previousTopic],
                recommendedNext: [t.nextTopic],
                advancedTopics: [t.name]
            },
            hindiDescription: t.description,
        };

        const tabResults = {};
        for (const tabName of tabs) {
            console.log(`\n--- Generating tab: ${tabName} for ${t.name} ---`);
            try {
                const res = await generateTab(tabName, meta, contentClient, translationClient);
                tabResults[tabName] = res;
                console.log(`✅ Success: ${tabName} (Score: ${res.score.overall}/100)`);
            } catch (err) {
                console.error(`❌ Failed tab ${tabName}: ${err.message}`);
                tabResults[tabName] = null;
            }
        }

        const bilingualData = {};
        for (const tabName of tabs) {
            if (tabResults[tabName]) bilingualData[tabName] = tabResults[tabName].data;
        }

        const overallScore = Math.round(
            Object.values(tabResults)
                .filter(r => r)
                .reduce((sum, r) => sum + (r.score?.overall || 0), 0) /
            Object.values(tabResults).filter(r => r).length
        );

        const html = assemblePage(meta, bilingualData, { overall: overallScore });
        const outputDir = path.join(process.cwd(), 'upsc', meta.subjectDir, meta.parentDir, meta.dir);
        fs.mkdirSync(outputDir, { recursive: true });

        fs.writeFileSync(path.join(outputDir, 'index.html'), html, 'utf8');
        fs.writeFileSync(path.join(outputDir, 'page.manifest.json'), JSON.stringify(createManifest(meta, tabResults), null, 2), 'utf8');

        const tabsDir = path.join(outputDir, 'tabs');
        fs.mkdirSync(tabsDir, { recursive: true });
        for (const tabName of tabs) {
            if (tabResults[tabName]) {
                fs.writeFileSync(path.join(tabsDir, `${tabName}.json`), JSON.stringify(tabResults[tabName].data, null, 2), 'utf8');
            }
        }

        console.log(`🎉 Topic generated & written to: ${outputDir}`);
    }
    console.log('\n🏁 All remaining prehistory topics generated successfully!');
}

main().catch(err => {
    console.error('Fatal error:', err);
    process.exit(1);
});
