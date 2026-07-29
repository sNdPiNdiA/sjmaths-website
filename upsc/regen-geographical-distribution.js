/**
 * Regenerate Geographical Distribution and Characteristics of Pre-History
 */
import fs from 'fs';
import path from 'path';

// Load .env
if (fs.existsSync('.env')) {
    const envConfig = fs.readFileSync('.env', 'utf8');
    envConfig.split('\n').forEach(line => {
        const [key, value] = line.split('=');
        if (key && value) process.env[key.trim()] = value.trim();
    });
}

import {
    generatePrompt,
    parseResponse,
    normalizeContent,
    translateToBilingual,
    generateSha256Hash,
    PageScorer,
    GeminiClient,
    assemblePage,
    createManifest,
    DEFAULT_GLOSSARY,
} from './upsc-microtopic-template.js';

const apiKey = process.env.GEMINI_API_KEY;

const topic = {
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
};

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

    for (let i = 0; i < strings.length; i += batchSize) {
        const batch = strings.slice(i, i + batchSize);
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
            console.warn(`  Batch failed: ${err.message}. Using fallback.`);
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

    console.log(`\n${'#'.repeat(70)}`);
    console.log(`[Regenerating] ${topic.name}`);
    console.log(`${'#'.repeat(70)}`);

    const meta = {
        name: topic.name,
        hindiName: topic.hindiName,
        dir: topic.dir,
        subject: 'Ancient History',
        subjectDir: 'ancient-history',
        parentTopic: 'Prehistory',
        parentDir: 'Prehistory',
        previousTopic: topic.previousTopic,
        previousDir: topic.previousDir,
        previousTopicHi: topic.previousTopicHi,
        nextTopic: topic.nextTopic,
        nextDir: topic.nextDir,
        nextTopicHi: topic.nextTopicHi,
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
        canonicalUrl: `https://sjmaths.com/upsc/ancient-history/Prehistory/${topic.dir}/`,
        description: topic.description,
        category: 'GS-1',
        supportsMains: true,
        topicId: `ancient-history.prehistory.${topic.dir.toLowerCase()}`,
        practiceTypes: ['basic', 'conceptual', 'statement', 'match'],
        difficulty: 'medium',
        studyTime: { concepts: 20, practice: 15, revision: 8 },
        learningObjectives: [
            `Understand key aspects and historical significance of ${topic.name}`,
            'Analyze archaeological evidence, site distribution, and socio-economic patterns',
            'Examine UPSC Prelims and Mains dimensions related to this prehistoric phase'
        ],
        scope: {
            mustExplain: [topic.name, 'Archaeological evidence', 'Chronology and significance'],
            mayMention: ['Sites', 'Dating techniques'],
            neverExplain: ['Later historical periods'],
            relatedTopics: [topic.name],
            keywords: ['prehistory', 'ancient history', 'upsc', topic.name.toLowerCase()]
        },
        related: {
            prerequisite: [topic.previousTopic],
            recommendedNext: [topic.nextTopic],
            advancedTopics: [topic.name]
        },
        hindiDescription: topic.description,
    };

    const tabResults = {};
    for (const tabName of tabs) {
        console.log(`\n--- Generating tab: ${tabName} ---`);
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
    let filesWritten = 0;
    for (const tabName of tabs) {
        if (tabResults[tabName]) {
            const filePath = path.join(tabsDir, `${tabName}.json`);
            fs.writeFileSync(filePath, JSON.stringify(tabResults[tabName].data, null, 2), 'utf8');
            console.log(`  📝 Written: ${filePath}`);
            filesWritten++;
        }
    }

    console.log(`\n🎉 Topic regenerated successfully!`);
    console.log(`   Location: ${outputDir}`);
    console.log(`   Tabs generated: ${Object.keys(bilingualData).length}/8 (${filesWritten} files written)`);
}

main().catch(err => {
    console.error('Fatal error:', err);
    process.exit(1);
});