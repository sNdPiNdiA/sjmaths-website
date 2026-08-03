import fs from 'fs';
import path from 'path';
import { validateMetadata, GeminiClient, assemblePage, createManifest, TabCache, generateTab } from './upsc-microtopic-template.js';

if (fs.existsSync('.env')) {
  const envContent = fs.readFileSync('.env', 'utf8');
  for (const line of envContent.split('\n')) {
    const match = line.match(/^\s*([\w.-]+)\s*=\s*(.*)?$/);
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
if (!apiKey) { console.error('GEMINI_API_KEY is not set'); process.exit(1); }

function getModelForCall(callNumber) {
    // Always use gemini-2.5-flash for all calls
    return 'gemini-2.5-flash';
}

function kebabToTitle(kebab) {
    return kebab.split('-').map(word => {
        const up = word.toUpperCase();
        // Common science-and-tech acronyms
        const acronyms = ['AI', 'ICT', 'IT', 'IoT', 'DNA', 'RNA', 'IPR', 'BT', 'LASER', 'WIFI', 'BT', 'USB', 'PCR',
            'ISRO', 'NASA', 'GPS', 'IRNSS', 'GSAT', 'INSAT', 'PSLV', 'GSLV', 'LVM', 'DRDO', 'BARC', 'DAE',
            'DST', 'DBT'];
        if (acronyms.includes(up)) return up;
        return word.charAt(0).toUpperCase() + word.slice(1);
    }).join(' ');
}

async function translateMetadata(client, name, description) {
    const prompt = `You are a translator. Translate the following UPSC Science & Technology microtopic name and description into Hindi.
Name: "${name}"
Description: "${description}"

Return ONLY a valid JSON object with keys "hindiName" and "hindiDescription". No markdown formatting, no backticks.
JSON:`;
    try {
        const raw = await client.generate(prompt);
        let cleaned = raw.trim();
        if (cleaned.startsWith('```json')) {
            cleaned = cleaned.replace(/^```json\s*/, '').replace(/\s*```$/, '');
        } else if (cleaned.startsWith('```')) {
            cleaned = cleaned.replace(/^```\s*/, '').replace(/\s*```$/, '');
        }
        const parsed = JSON.parse(cleaned);
        return {
            hindiName: parsed.hindiName || name,
            hindiDescription: parsed.hindiDescription || (parsed.hindiName + ' पर UPSC GS-3 की विस्तृत गाइड।')
        };
    } catch (err) {
        return {
            hindiName: name,
            hindiDescription: name + ' par UPSC GS-3 ki vistrit guide.'
        };
    }
}

function buildMeta(parentDir, parentName, microtopicDir, name, description, hindiName = '', hindiDescription = '', previousTopic = null, nextTopic = null) {
    return {
        name,
        hindiName: hindiName || name,
        dir: microtopicDir,
        subject: 'Science & Technology',
        subjectDir: 'science-and-tech',
        parentTopic: parentName,
        parentDir: parentDir,
        previousTopic: previousTopic?.name || '',
        previousDir: previousTopic?.dir || '',
        previousTopicHi: previousTopic?.hindiName || '',
        nextTopic: nextTopic?.name || '',
        nextDir: nextTopic?.dir || '',
        nextTopicHi: nextTopic?.hindiName || '',
        parentTopicHi: parentName,
        childTopics: [],
        childDirs: [],
        childTopicsHi: [],
        similarTopics: [],
        similarDirs: [],
        similarTopicsHi: [],
        confusedTopics: [],
        confusedDirs: [],
        confusedTopicsHi: [],
        canonicalUrl: `https://sjmaths.com/upsc/science-and-tech/${parentDir}/${microtopicDir}/`,
        description,
        hindiDescription: hindiDescription || (name + ' पर UPSC GS-3 की विस्तृत गाइड।'),
        category: 'GS-3',
        supportsMains: true,
        topicId: `science-and-tech.${parentDir.toLowerCase()}.${microtopicDir.toLowerCase()}`,
        practiceTypes: ['basic', 'conceptual'],
        difficulty: 'medium',
        studyTime: { concepts: 20, practice: 15 },
        learningObjectives: [
            `Understand key UPSC concepts for ${name}`,
            `Memorize key facts and applications for ${name}`,
            `Apply to UPSC Prelims and Mains (GS-3)`
        ],
        scope: {
            mustExplain: [name, 'Science & Technology', 'UPSC GS-3'],
            mayMention: ['Current Affairs', 'Government Initiatives', 'Applications'],
            neverExplain: ['Ancient History', 'Polity', 'Geography'],
            relatedTopics: [name],
            keywords: ['UPSC', 'Science', 'Technology', name]
        },
        related: {
            prerequisite: previousTopic ? [previousTopic.name] : [],
            recommendedNext: nextTopic ? [nextTopic.name] : [],
            advancedTopics: [name]
        }
    };
}

async function main() {
    console.log('╔══════════════════════════════════════════════════════════════╗');
    console.log('║ UPSC Science & Technology Microtopic Batch Generator        ║');
    console.log('╚══════════════════════════════════════════════════════════════╝\n');

    const contentClient = new GeminiClient(apiKey, {
        model: 'gemini-2.5-flash',
        maxOutputTokens: 8192,
        temperature: 0.1,
        requestDelay: 13000
    });

    let totalApiCalls = 0;
    const callGemini = async (prompt) => {
        totalApiCalls++;
        const model = getModelForCall(totalApiCalls);
        console.log(`[API Call #${totalApiCalls}] Routing to ${model}`);
        contentClient.model = model;
        return contentClient.generate(prompt);
    };

    const translate = async (text, targetLang) => text;
    const tabs = ['overview', 'concepts'];

    const subjectDir = path.join(process.cwd(), 'upsc', 'science-and-tech');
    const parentDirs = fs.readdirSync(subjectDir).filter(name => {
        return fs.statSync(path.join(subjectDir, name)).isDirectory();
    });

    // 1. Gather all microtopic folders dynamically
    const allMicrotopics = [];
    for (const parentDir of parentDirs) {
        const parentPath = path.join(subjectDir, parentDir);
        const childDirs = fs.readdirSync(parentPath).filter(name => {
            return fs.statSync(path.join(parentPath, name)).isDirectory();
        });

        const parentName = kebabToTitle(parentDir);
        for (const childDir of childDirs) {
            const childPath = path.join(parentPath, childDir);
            let name = kebabToTitle(childDir);
            let description = `Study guide for ${name} under ${parentName} for UPSC Civil Services Prep (GS-3 Science & Technology).`;

            const contentJsonPath = path.join(childPath, 'content.json');
            if (fs.existsSync(contentJsonPath)) {
                try {
                    const content = JSON.parse(fs.readFileSync(contentJsonPath, 'utf8'));
                    if (content.hero?.title) name = content.hero.title;
                    if (content.hero?.description) description = content.hero.description;
                } catch (e) {
                    // Ignore JSON parsing errors and use defaults
                }
            }

            allMicrotopics.push({
                parentDir,
                parentName,
                dir: childDir,
                name,
                description
            });
        }
    }

    console.log(`Discovered ${allMicrotopics.length} microtopics across ${parentDirs.length} categories.\n`);

    // 2. Generation loop
    for (let i = 0; i < allMicrotopics.length; i++) {
        const topic = allMicrotopics[i];
        const previousTopic = i > 0 ? allMicrotopics[i - 1] : null;
        const nextTopic = i < allMicrotopics.length - 1 ? allMicrotopics[i + 1] : null;
        if (totalApiCalls >= 40) {
            console.log('Reached 40 API calls, stopping generation.');
            break;
        };

        console.log(`\n========================================================================`);
        console.log(`[${i + 1}/${allMicrotopics.length}] Processing: ${topic.parentName} -> ${topic.name}`);
        console.log(`========================================================================`);

        // Check cache first to see if we can skip API calls entirely
        const tempMeta = buildMeta(topic.parentDir, topic.parentName, topic.dir, topic.name, topic.description, '', '', previousTopic, nextTopic);
        const cache = new TabCache(fs, path, process.cwd(), tempMeta);
        const staleTabs = await cache.getStaleTabs(tabs);

        let bilingualData = {};
        let tabResults = {};
        let scores = [];

        if (staleTabs.length === 0) {
            console.log(`[Cache Hit] All tabs up-to-date. Reading from cache...`);
            let allCachedOk = true;
            for (const tabName of tabs) {
                const cached = await cache.get(tabName);
                if (cached) {
                    bilingualData[tabName] = cached.data;
                    tabResults[tabName] = { score: { overall: cached.score }, contentHash: cached.hash };
                    scores.push(cached.score);
                } else {
                    allCachedOk = false;
                }
            }

            if (allCachedOk) {
                const overallScore = scores.length > 0 ? Math.round(scores.reduce((a, b) => a + b, 0) / scores.length) : 0;
                const html = assemblePage(tempMeta, bilingualData, { overall: overallScore });
                const outputDir = path.join(process.cwd(), 'upsc', tempMeta.subjectDir, tempMeta.parentDir, tempMeta.dir);
                fs.mkdirSync(outputDir, { recursive: true });
                fs.writeFileSync(path.join(outputDir, 'index.html'), html, 'utf8');
                console.log(`Re-assembled index.html from cache. Skip generation.`);
                continue;
            }
        }

        // Cache miss -> Translate meta to Hindi using Gemini
        console.log(`[Cache Miss] Translating metadata to Hindi...`);
        const translation = await translateMetadata(contentClient, topic.name, topic.description);
        const meta = buildMeta(
            topic.parentDir,
            topic.parentName,
            topic.dir,
            topic.name,
            topic.description,
            translation.hindiName,
            translation.hindiDescription,
            previousTopic,
            nextTopic
        );

        const metaErrors = validateMetadata(meta);
        if (!metaErrors.passed) {
            console.error(`❌ Metadata validation failed for ${meta.name}: ${metaErrors.errors.join('; ')}`);
            continue;
        }

        // Re-init cache with full metadata
        const fullCache = new TabCache(fs, path, process.cwd(), meta);

        for (const tabName of tabs) {
            try {
                const tabResult = await generateTab(tabName, meta, callGemini, translate, {}, fullCache);
                bilingualData[tabName] = tabResult.data;
                tabResults[tabName] = tabResult;
                if (tabResult.score?.overall) scores.push(tabResult.score.overall);
                console.log(`✅ ${tabName} generated: score=${tabResult.score?.overall || 'N/A'}`);
            } catch (err) {
                console.error(`❌ Failed generating ${tabName}: ${err.message}`);
            }
        }

        const overallScore = scores.length > 0 ? Math.round(scores.reduce((a, b) => a + b, 0) / scores.length) : 0;
        const html = assemblePage(meta, bilingualData, { overall: overallScore });
        const outputDir = path.join(process.cwd(), 'upsc', meta.subjectDir, meta.parentDir, meta.dir);

        fs.mkdirSync(outputDir, { recursive: true });
        fs.writeFileSync(path.join(outputDir, 'index.html'), html, 'utf8');
        fs.writeFileSync(path.join(outputDir, 'page.manifest.json'), JSON.stringify(createManifest(meta, tabResults), null, 2), 'utf8');

        const tabsDir = path.join(outputDir, 'tabs');
        fs.mkdirSync(tabsDir, { recursive: true });
        for (const tabName of tabs) {
            if (bilingualData[tabName]) {
                fs.writeFileSync(path.join(tabsDir, `${tabName}.json`), JSON.stringify(bilingualData[tabName], null, 2), 'utf8');
            }
        }

        console.log(`🎉 Completed: ${meta.name} (Overall Score: ${overallScore}/100)`);
    }

    console.log('\nAll Science & Technology microtopics processed successfully!');
}

main().catch(err => {
    console.error('Fatal error:', err);
    process.exit(1);
});
