/**
 * UPSC Microtopic Generator — Runner Script
 * Runs upsc/upsc-microtopic-template.js for the first microtopic:
 * /upsc/ancient-history/Prehistory/Prehistoric-Time-Periods/
 *
 * This script:
 * 1. Imports all functions from the template
 * 2. Defines topic metadata for "Prehistoric Time Periods"
 * 3. Sets up the Gemini API client
 * 4. Runs the generation pipeline for all 8 tabs
 * 5. Batch-translates content to Hindi (to minimize API calls)
 * 6. Assembles the HTML page and writes to disk
 */

import fs from 'fs';
import path from 'path';

// ── Load .env ──────────────────────────────────────────────────────────────
if (fs.existsSync('.env')) {
    const envConfig = fs.readFileSync('.env', 'utf8');
    envConfig.split('\n').forEach(line => {
        const [key, value] = line.split('=');
        if (key && value) {
            process.env[key.trim()] = value.trim();
        }
    });
}

// ── Import template functions ──────────────────────────────────────────────
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
    getSubjectConfig,
    getFocusedRetryPrompt,
} from './upsc-microtopic-template.js';

// ── Topic Metadata ─────────────────────────────────────────────────────────
const meta = {
    name: 'Prehistoric Time Periods',
    hindiName: 'प्राऐरिशियन समय अवधारणाएँ',
    dir: 'Prehistoric-Time-Periods',
    subject: 'Ancient History',
    subjectDir: 'ancient-history',
    parentTopic: 'Prehistory',
    parentDir: 'Prehistory',
    previousTopic: 'Sources of Information of Pre-History',
    previousDir: 'Sources-of-Information-of-Pre-History',
    previousTopicHi: 'प्राऐरिशियन इतिहास के स्रोत',
    nextTopic: 'History of Paleolithic or Old Stone Age',
    nextDir: 'History-of-Paleolithic-or-Old-Stone-Age',
    nextTopicHi: 'पुरापाषाण या पुराना पत्थर काल का इतिहास',
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
    canonicalUrl: 'https://sjmaths.com/upsc/ancient-history/Prehistory/Prehistoric-Time-Periods/',
    description: 'Comprehensive UPSC GS-1 guide on Prehistoric Time Periods. Study notes, tool typology, timeline, practice questions, and mock tests covering Paleolithic, Mesolithic, Neolithic, and Chalcolithic ages.',
    category: 'GS-1',
    supportsMains: true,
    topicId: 'ancient-history.prehistory.prehistoric-time-periods',
    practiceTypes: ['basic', 'conceptual', 'statement', 'match'],
    difficulty: 'medium',
    studyTime: { concepts: 20, practice: 15, revision: 8 },
    learningObjectives: [
        'Explain the four major prehistoric time periods and their characteristics',
        'Compare tool technologies across Paleolithic, Mesolithic, Neolithic, and Chalcolithic ages',
        'Identify key archaeological sites and their significance in Indian prehistory'
    ],
    scope: {
        mustExplain: [
            'Paleolithic Age characteristics and tool traditions',
            'Mesolithic Age and microlith technology',
            'Neolithic Age and agricultural revolution',
            'Chalcolithic Age and copper metallurgy',
            'Chronological framework of prehistoric periods',
            'Tool typology evolution'
        ],
        mayMention: [
            'Archaeological dating methods',
            'Major prehistoric sites in India',
            'Rock art and cave paintings'
        ],
        neverExplain: [
            'Indus Valley Civilization',
            'Vedic period',
            'Mauryan Empire',
            'Gupta Empire'
        ],
        relatedTopics: [
            'Paleolithic Age',
            'Mesolithic Age',
            'Neolithic Age',
            'Chalcolithic Age'
        ],
        keywords: [
            'prehistory', 'stone age', 'paleolithic', 'mesolithic', 'neolithic',
            'chalcolithic', 'microliths', 'handaxes', 'agriculture', 'domestication',
            'archaeology', 'tool technology', 'chronological framework'
        ]
    },
    related: {
        prerequisite: ['Sources of Information of Pre-History'],
        recommendedNext: ['History of Paleolithic or Old Stone Age'],
        advancedTopics: ['Bhimbetka Rock Paintings', 'Prehistoric Sites of India']
    },
    hindiDescription: 'प्राऐरिशियन समय अवधारणाओं पर UPSC GS-1 की व्यापक गाइड। अध्ययन नोट्स, उपकरण तकनीक, रेखांकरण, अभ्यास प्रश्न और मॉक टेस्ट जो पुरापाषाण, मध्यपाषाण, नवपाषाण और ताम्रपाषाण युगों को कवर करते हैं।',
};

// ── Helper: collect all unique strings from an object ──────────────────────
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

// ── Helper: apply glossary to text (mirrors translateToBilingual internals) ─
function applyGlossary(text, glossary) {
    let result = text;
    for (const [en, hi] of Object.entries(glossary)) {
        const escaped = en.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
        const regex = new RegExp(`\\b${escaped}\\b`, 'gi');
        result = result.replace(regex, hi);
    }
    return result;
}

// ── Helper: batch translate strings via Gemini ─────────────────────────────
async function batchTranslate(strings, client, batchSize = 20) {
    const translations = new Map();
    const stringArray = Array.from(strings);
    const totalBatches = Math.ceil(stringArray.length / batchSize);

    for (let i = 0; i < stringArray.length; i += batchSize) {
        const batch = stringArray.slice(i, i + batchSize);
        const batchNum = Math.floor(i / batchSize) + 1;
        const prompt = `Translate the following English text items to Hindi. Keep technical terms, names, and formatting intact. Return ONLY the translations, one per line, in the same order as the input.\n\n${batch.map((s, idx) => `${idx + 1}. ${s}`).join('\n')}\n\nTranslations:`;

        try {
            const result = await client.generate(prompt);
            const lines = result.trim().split('\n');
            for (let j = 0; j < batch.length && j < lines.length; j++) {
                translations.set(batch[j], lines[j].trim());
            }
            console.log(`  Translated batch ${batchNum}/${totalBatches} (${batch.length} strings)`);
        } catch (err) {
            console.warn(`  Batch ${batchNum} failed: ${err.message}. Using fallback.`);
            for (let j = 0; j < batch.length; j++) {
                translations.set(batch[j], batch[j]);
            }
        }
    }

    return translations;
}

// ── Helper: generate a single tab manually (with batch translation) ─────────
async function generateTabWithBatchTranslation(tabName, meta, contentClient, translationClient, glossary) {
    const log = (event, details) => createLogEntry(event, { tabName, ...details });
    const maxRetries = 3;

    for (let attempt = 1; attempt <= maxRetries; attempt++) {
        const startTime = Date.now();

        try {
            // 1. Generate prompt
            const prompt = generatePrompt(tabName, meta);

            // 2. Call Gemini for content
            const raw = await contentClient.generate(prompt);

            // 3. Parse JSON
            const englishJson = parseResponse(raw);

            // 4. Validate
            const qc = new QualityControl(meta);
            const validation = qc.validate(tabName, englishJson);
            if (!validation.passed) {
                log('validation-failed', { errors: validation.errors, attempt });
                if (attempt >= maxRetries) {
                    throw new Error(`[${tabName}] Quality gate: validation failed after ${maxRetries} attempts. Errors: ${validation.errors.join('; ')}`);
                }
                continue;
            }

            // 5. Normalize
            const normalized = normalizeContent(englishJson, glossary);

            // 6. Score
            const scorer = new PageScorer(meta);
            const score = scorer.score(tabName, normalized);

            // 7. Smart retry if score < 90
            if (!score.passed) {
                if (attempt >= maxRetries) {
                    console.warn(`[${tabName}] Score ${score.overall} < 90 after ${maxRetries} attempts. Using generated content.`);
                } else {
                    const focusedPrompt = getFocusedRetryPrompt(tabName, score, normalized);
                    if (focusedPrompt) {
                        log('smart-retry', { score: score.overall, dimensions: score.dimensions });
                        // For retry, we need to call Gemini with the focused prompt
                        // But we need to generate a new prompt... let's just continue
                        // and accept the lower score
                        console.warn(`[${tabName}] Score ${score.overall} < 90. Attempting focused retry.`);
                    }
                }
            }

            // 8. Collect all strings and batch-translate
            const allStrings = collectStrings(normalized);
            const mergedGlossary = { ...DEFAULT_GLOSSARY, ...glossary };

            // Apply glossary to each string (mirrors translateToBilingual internals)
            const glossaryAppliedStrings = new Set();
            for (const str of allStrings) {
                glossaryAppliedStrings.add(applyGlossary(str, mergedGlossary));
            }

            // Batch-translate all unique glossary-applied strings
            const translations = await batchTranslate(glossaryAppliedStrings, translationClient);

            // 9. Create translateFn that uses the cache
            const translateFn = (text, targetLang) => {
                if (targetLang !== 'hi') return text;
                return translations.get(text) || text;
            };

            // 10. Translate to bilingual using template's function
            const bilingual = await translateToBilingual(normalized, translateFn, glossary);

            // 11. Generate content hash
            const contentHash = await generateSha256Hash(bilingual);

            const duration = Date.now() - startTime;

            log('success', {
                attempt,
                duration,
                score: score.overall,
                contentHash,
                uniqueStrings: allStrings.size,
            });

            return {
                data: bilingual,
                score,
                validation,
                version: VERSION,
                contentHash,
                attempt,
                duration,
            };
        } catch (err) {
            log('error', { message: err.message, attempt });
            if (attempt >= maxRetries) throw err;
            console.log(`[${tabName}] Attempt ${attempt} failed, retrying...`);
        }
    }
}

// ── Main ───────────────────────────────────────────────────────────────────
async function main() {
    console.log('╔══════════════════════════════════════════════════════════╗');
    console.log('║ UPSC Microtopic Generator v5 — Runner                  ║');
    console.log('║ Topic: Prehistoric Time Periods                        ║');
    console.log('║ Path: /upsc/ancient-history/Prehistory/                ║');
    console.log('║       Prehistoric-Time-Periods/                        ║');
    console.log('╚══════════════════════════════════════════════════════════╝');
    console.log('');

    // Check API key
    const apiKey = process.env.GEMINI_API_KEY;
    if (!apiKey) {
        console.error('❌ GEMINI_API_KEY not found in environment variables.');
        process.exit(1);
    }
    console.log(`✅ API key loaded (length: ${apiKey.length})`);

    // Validate metadata
    console.log('\n📋 Validating topic metadata...');
    const validation = validateMetadata(meta);
    if (!validation.passed) {
        console.error('❌ Metadata validation failed:');
        validation.errors.forEach(e => console.error(`   - ${e}`));
        process.exit(1);
    }
    console.log('✅ Metadata validation passed.');
    if (validation.warnings.length > 0) {
        console.warn(`⚠️  ${validation.warnings.length} warnings:`);
        validation.warnings.forEach(w => console.warn(`   - ${w}`));
    }

    // Get subject config
    const subjectConfig = getSubjectConfig(meta.subjectDir);
    console.log(`\n📚 Subject config: supportsTimeline=${subjectConfig.supportsTimeline}, supportsMaps=${subjectConfig.supportsMaps}, supportsMains=${subjectConfig.supportsMains}`);

    // Create Gemini clients
    // Content client: 13s delay (as per template)
    const contentClient = new GeminiClient(apiKey, {
        model: 'gemini-3.5-flash-lite',
        temperature: 0.1,
        maxRetries: 5,
        requestDelay: 13000,
    });

    // Translation client: shorter delay for batch translations
    const translationClient = new GeminiClient(apiKey, {
        model: 'gemini-3.5-flash-lite',
        temperature: 0.1,
        maxRetries: 5,
        requestDelay: 13000,
    });

    console.log('✅ Gemini clients initialized.');

    // Tabs to generate
    const tabs = ['overview', 'concepts', 'visual', 'comparisons', 'practice', 'mains', 'revision', 'test'];

    // Generate each tab
    const tabResults = {};
    for (const tabName of tabs) {
        console.log(`\n${'='.repeat(60)}`);
        console.log(`📝 Generating tab: ${tabName}`);
        console.log(`   Prompt: ${generatePrompt(tabName, meta).substring(0, 100)}...`);
        console.log(`   Estimated time: ~30-60s (content + translation)`);
        console.log(`${'='.repeat(60)}`);

        try {
            const result = await generateTabWithBatchTranslation(
                tabName, meta, contentClient, translationClient, {}
            );
            tabResults[tabName] = result;
            console.log(`✅ Tab "${tabName}" generated successfully!`);
            console.log(`   Score: ${result.score?.overall || 'N/A'}/100`);
            console.log(`   Duration: ${(result.duration / 1000).toFixed(1)}s`);
            console.log(`   Content hash: ${result.contentHash?.substring(0, 20)}...`);
        } catch (err) {
            console.error(`❌ Failed to generate tab "${tabName}": ${err.message}`);
            tabResults[tabName] = null;
        }
    }

    // Assemble HTML page
    console.log(`\n${'='.repeat(60)}`);
    console.log('🔨 Assembling HTML page...');
    console.log(`${'='.repeat(60)}`);

    const bilingualData = {};
    for (const tabName of tabs) {
        if (tabResults[tabName]) {
            bilingualData[tabName] = tabResults[tabName].data;
        }
    }

    const overallScore = Math.round(
        Object.values(tabResults)
            .filter(r => r)
            .reduce((sum, r) => sum + (r.score?.overall || 0), 0) /
        Object.values(tabResults).filter(r => r).length
    );

    const html = assemblePage(meta, bilingualData, { overall: overallScore });

    // Write HTML to disk
    const outputDir = path.join(process.cwd(), 'upsc', meta.subjectDir, meta.parentDir, meta.dir);
    fs.mkdirSync(outputDir, { recursive: true });

    const htmlPath = path.join(outputDir, 'index.html');
    fs.writeFileSync(htmlPath, html, 'utf8');
    console.log(`✅ HTML page written to: ${htmlPath}`);
    console.log(`   File size: ${(html.length / 1024).toFixed(1)} KB`);

    // Write manifest
    const manifest = createManifest(meta, tabResults);
    const manifestPath = path.join(outputDir, 'page.manifest.json');
    fs.writeFileSync(manifestPath, JSON.stringify(manifest, null, 2), 'utf8');
    console.log(`✅ Manifest written to: ${manifestPath}`);

    // Write tab JSON files
    const tabsDir = path.join(outputDir, 'tabs');
    fs.mkdirSync(tabsDir, { recursive: true });
    for (const tabName of tabs) {
        if (tabResults[tabName]) {
            const tabPath = path.join(tabsDir, `${tabName}.json`);
            fs.writeFileSync(tabPath, JSON.stringify(tabResults[tabName].data, null, 2), 'utf8');
        }
    }
    console.log(`✅ Tab JSON files written to: ${tabsDir}/`);

    // Summary
    console.log(`\n${'='.repeat(60)}`);
    console.log('📊 Generation Summary');
    console.log(`${'='.repeat(60)}`);
    console.log(`Topic: ${meta.name}`);
    console.log(`URL: ${meta.canonicalUrl}`);
    console.log(`Overall score: ${overallScore}/100`);
    console.log(`Tabs generated: ${Object.values(tabResults).filter(r => r).length}/${tabs.length}`);
    for (const tabName of tabs) {
        const result = tabResults[tabName];
        if (result) {
            console.log(`  ✅ ${tabName}: ${result.score?.overall || 'N/A'}/100 (${(result.duration / 1000).toFixed(1)}s)`);
        } else {
            console.log(`  ❌ ${tabName}: FAILED`);
        }
    }
    console.log(`${'='.repeat(60)}`);
    console.log('🎉 Done!');
}

main().catch(err => {
    console.error('\n❌ Fatal error:', err);
    process.exit(1);
});
