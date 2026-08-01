import {
    validateMetadata,
    GeminiClient,
    assemblePage,
    createManifest,
    TabCache,
    generateTab,
} from './upsc-microtopic-template.js';
import fs from 'fs';
import path from 'path';

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
    console.error('❌ GEMINI_API_KEY is not set in environment or .env');
    process.exit(1);
}

const topics = [
    {
        name: 'Doctrine of Ring Fence',
        hindiName: 'रिंग फेंस का सिद्धांत',
        dir: 'Doctrine-of-Ring-Fence',
        description: 'Detailed analysis of Warren Hastings\' Ring Fence policy, its objectives, implementation, and impact on British expansion in India.',
    },
    {
        name: 'Policy of Proud Reserve',
        hindiName: 'गर्वित तटस्थता की नीति',
        dir: 'Policy-of-Proud-Reserve',
        description: 'Study of Lord Wellesley\'s Policy of Proud Reserve, its departure from Ring Fence, and its role in British imperial consolidation.',
    },
    {
        name: 'Doctrine of Masterly Inactivity',
        hindiName: 'कुशल निष्क्रियता का सिद्धांत',
        dir: 'Doctrine-of-Masterly-Inactivity',
        description: 'Analysis of Lord Lawrence\'s policy of non-intervention, its application in Afghanistan and North-West Frontier, and its strategic rationale.',
    },
    {
        name: 'Doctrine of Lapse and its Victim States',
        hindiName: 'व्यपगत का सिद्धांत और इसके शिकार राज्य',
        dir: 'Doctrine-of-Lapse-and-its-Victim-States',
        description: 'Comprehensive study of Lord Dalhousie\'s Doctrine of Lapse, annexation of Satara, Jhansi, Nagpur, and other princely states.',
    },
    {
        name: 'EIC\'s Relations with Neighboring Countries',
        hindiName: 'पड़ोसी देशों के साथ ईस्ट इंडिया कंपनी के संबंध',
        dir: 'EICs-Relations-with-Neighboring-Countries',
        description: 'British East India Company\'s diplomatic and military relations with Afghanistan, Burma, Nepal, Tibet, and Central Asia.',
    },
    {
        name: '2-Anglo-Sikh-Wars',
        hindiName: 'द्वितीय आंग्ल-सिख युद्ध',
        dir: '2-Anglo-Sikh-Wars',
        description: 'Causes, events, and consequences of the Second Anglo-Sikh War (1848-1849), including the Battle of Chillianwala and annexation of Punjab.',
    },
    {
        name: 'Annexation of Oudh',
        hindiName: 'अवध का विलय',
        dir: 'Annexation-of-Oudh',
        description: 'Detailed study of the annexation of Awadh (1856) under Lord Dalhousie, charges of misgovernment, and its impact on the Revolt of 1857.',
    },
];

function buildMeta(topic, previousTopic, nextTopic) {
    return {
        name: topic.name,
        hindiName: topic.hindiName,
        dir: topic.dir,
        subject: 'Modern History',
        subjectDir: 'modern-history',
        parentTopic: 'Second Phase of British Expansion In India',
        parentDir: 'Second-Phase-of-British-Expansion-In-India',
        previousTopic: previousTopic?.name || '',
        previousDir: previousTopic?.dir || '',
        previousTopicHi: previousTopic?.hindiName || '',
        nextTopic: nextTopic?.name || '',
        nextDir: nextTopic?.dir || '',
        nextTopicHi: nextTopic?.hindiName || '',
        parentTopicHi: 'भारत में ब्रिटिश विस्तार का दूसरा चरण',
        childTopics: [],
        childDirs: [],
        childTopicsHi: [],
        similarTopics: [],
        similarDirs: [],
        similarTopicsHi: [],
        confusedTopics: [],
        confusedDirs: [],
        confusedTopicsHi: [],
        canonicalUrl: `https://sjmaths.com/upsc/modern-history/Second-Phase-of-British-Expansion-In-India/${topic.dir}/`,
        description: topic.description,
        hindiDescription: topic.hindiName + ' पर UPSC GS-1 की विस्तृत गाइड।',
        category: 'GS-1',
        supportsMains: true,
        topicId: `modern-history.second-phase-of-british-expansion.${topic.dir.toLowerCase()}`,
        practiceTypes: ['basic', 'conceptual', 'statement', 'match'],
        difficulty: 'medium',
        studyTime: { concepts: 20, practice: 15, revision: 8 },
        learningObjectives: [
            `Understand the key UPSC concepts for ${topic.name}`,
            `Memorize major events, policies, and consequences of ${topic.name}`,
            'Apply insights to UPSC Prelims and Mains questions',
        ],
        scope: {
            mustExplain: [topic.name, 'British Expansion in India', 'Modern Indian History'],
            mayMention: ['British Rule', 'East India Company', 'Governor-Generals'],
            neverExplain: ['Gupta Empire', 'Harappan Civilisation details', 'Vedic period rituals'],
            relatedTopics: [topic.name],
            keywords: ['UPSC', 'Modern History', topic.name],
        },
        related: {
            prerequisite: previousTopic ? [previousTopic.name] : [],
            recommendedNext: nextTopic ? [nextTopic.name] : [],
            advancedTopics: [topic.name],
        },
    };
}

async function main() {
    console.log('╔══════════════════════════════════════════════════════════╗');
    console.log('║ UPSC Second Phase British Expansion Microtopic Generator║');
    console.log('║ Topics: Modern History / Second Phase of British Exp.   ║');
    console.log('╚══════════════════════════════════════════════════════════╝\n');

    const contentClient = new GeminiClient(apiKey, {
        model: 'gemini-3.5-flash-lite',
        maxOutputTokens: 8192,
        temperature: 0.1,
        requestDelay: 13000,
    });

    let totalApiCalls = 0;
    const callGemini = async (prompt) => {
        totalApiCalls++;
        console.log(`[API Call #${totalApiCalls}] Routing request to model: gemini-3.5-flash-lite`);
        contentClient.model = 'gemini-3.5-flash-lite';
        return contentClient.generate(prompt);
    };

    const translate = async (text, targetLang) => {
        return text;
    };

    const tabs = ['overview', 'concepts', 'visual', 'comparisons', 'practice', 'mains', 'revision', 'test'];

    for (let i = 0; i < topics.length; i++) {
        const topic = topics[i];
        const previousTopic = i > 0 ? topics[i - 1] : null;
        const nextTopic = i < topics.length - 1 ? topics[i + 1] : null;
        const meta = buildMeta(topic, previousTopic, nextTopic);

        const metaErrors = validateMetadata(meta);
        if (!metaErrors.passed) {
            console.error(`❌ Metadata validation failed for ${meta.name}:`, metaErrors.errors);
            continue;
        }

        console.log(`\n========================================================================`);
        console.log(`[${i + 1}/${topics.length}] Processing Microtopic: ${meta.name}`);
        console.log(`========================================================================`);

        const cache = new TabCache(fs, path, process.cwd(), meta);
        const bilingualData = {};
        const tabResults = {};
        const scores = [];

        for (const tabName of tabs) {
            try {
                console.log(`\n--- Generating tab: ${tabName} for ${meta.name} ---`);
                const tabResult = await generateTab(tabName, meta, callGemini, translate, {}, cache);
                bilingualData[tabName] = tabResult.data;
                tabResults[tabName] = tabResult;
                if (tabResult.score?.overall) {
                    scores.push(tabResult.score.overall);
                }
                console.log(`✅ ${tabName} generated: score=${tabResult.score?.overall || 'N/A'}`);
            } catch (err) {
                console.error(`❌ Failed ${tabName}: ${err.message}`);
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

        console.log(`\n✅ Completed: ${meta.name}`);
        console.log(`   Output: ${outputDir}`);
        console.log(`   Overall score: ${overallScore}/100`);
    }

    console.log('\n🎉 All 7 Second Phase British Expansion microtopics generated successfully!');
}

main().catch(err => {
    console.error('Fatal error in main execution loop:', err);
    process.exit(1);
});