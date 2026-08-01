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

const parentTopic = 'First Phase of National Movement (1905-1917)';
const parentDir = 'First-Phase-of-National-Movement-1905-1917';
const parentTopicHi = 'राष्ट्रीय आंदोलन का प्रथम चरण (1905-1917)';

const topics = [
    { name: 'Annulment of Partition of Bengal', hindiName: 'बंगाल विभाजन का निरस्तीकरण', dir: 'Annulment-of-Partition-of-Bengal', desc: 'The annulment of the Partition of Bengal in 1911 and its impact on the national movement.' },
    { name: 'Campaign for General Administrative Reforms', hindiName: 'सामान्य प्रशासनिक सुधारों के लिए अभियान', dir: 'Campaign-for-General-Administrative-Reforms', desc: 'The moderate campaign for administrative reforms in British India during the late 19th century.' },
    { name: 'Chittagong Revolt Group', hindiName: 'चटगांव विद्रोह समूह', dir: 'Chittagong-Revolt-Group', desc: 'Study of the Chittagong Armoury Raid led by Surya Sen and the revolutionary group.' },
    { name: 'Comparative Account of Moderates and Extremists', hindiName: 'नरमपंथियों और गरमपंथियों का तुलनात्मक विवरण', dir: 'Comparative-Account-of-Moderates-and-Extremists', desc: 'Comparative analysis of Moderate and Extremist ideologies in the Indian National Congress.' },
    { name: 'Constitutional Reforms and Propaganda in Legislature', hindiName: 'संवैधानिक सुधार और विधानमंडल में प्रचार', dir: 'Constitutional-Reforms-and-Propaganda-in-Legislature', desc: 'The role of legislative councils in propagating constitutional reforms during the national movement.' },
    { name: 'Debate over INC being a Safety Valve', hindiName: 'INC के सेफ्टी वाल्व होने पर बहस', dir: 'Debate-over-INC-being-a-Safety-Valve', desc: 'Historiographical debate on whether the INC was a safety valve for British interests.' },
    { name: 'Developments that led to Home Rule League', hindiName: 'होम रूल लीग की ओर ले जाने वाले विकास', dir: 'Developments-that-led-to-Home-Rule-League', desc: 'The political developments and factors that led to the formation of the Home Rule League.' },
    { name: 'Differences between the Moderates and the Extremists', hindiName: 'नरमपंथियों और गरमपंथियों के बीच मतभेद', dir: 'Differences-between-the-Moderates-and-the-Extremists', desc: 'Key ideological, methodological, and strategic differences between Moderates and Extremists.' },
    { name: 'Early Phase Indian National Congress', hindiName: 'भारतीय राष्ट्रीय कांग्रेस का प्रारंभिक चरण', dir: 'Early-Phase-Indian-National-Congress', desc: 'The early phase of the Indian National Congress from 1885 focusing on moderate demands.' },
    { name: 'Economic Critique of Imperialism', hindiName: 'साम्राज्यवाद की आर्थिक आलोचना', dir: 'Economic-Critique-of-Imperialism', desc: 'Nationalist economic critique of British imperialism led by Dadabhai Naoroji and others.' },
    { name: 'Government Repression', hindiName: 'सरकारी दमन', dir: 'Government-Repression', desc: 'British government repression of nationalist activities including sedition laws and prosecutions.' },
    { name: 'Government\'s Response towards INC', hindiName: 'INC के प्रति सरकार की प्रतिक्रिया', dir: 'Governments-Response-towards-INC', desc: 'British government\'s evolving response to the Indian National Congress and its demands.' },
    { name: 'Hindustan Republican Association', hindiName: 'हिंदुस्तान रिपब्लिकन एसोसिएशन', dir: 'Hindustan-Republican-Association', desc: 'Study of the Hindustan Republican Association and its revolutionary activities.' },
    { name: 'Home Rule League Movement 1916', hindiName: 'होम रूल लीग आंदोलन 1916', dir: 'Home-Rule-League-Movement-1916', desc: 'The Home Rule League Movement of 1916 led by Tilak and Annie Besant.' },
    { name: 'Important INC Sessions Extremist Phase', hindiName: 'INC के महत्वपूर्ण अधिवेशन - गरमपंथी चरण', dir: 'Important-INC-Sessions-Extremist-Phase', desc: 'Key sessions of the Indian National Congress during the Extremist phase (1905-1918).' },
    { name: 'Key Sessions of the Indian National Congress', hindiName: 'भारतीय राष्ट्रीय कांग्रेस के प्रमुख अधिवेशन', dir: 'Key-Sessions-of-the-Indian-National-Congress-INC', desc: 'Comprehensive study of important INC sessions including their presidents and resolutions.' },
    { name: 'Limitations with Home Rule Leagues', hindiName: 'होम रूल लीग की सीमाएं', dir: 'Limitations-with-Home-Rule-Leagues', desc: 'Analysis of the limitations and weaknesses of the Home Rule League movement.' },
    { name: 'Lucknow Session of INC 1916 Lucknow Pact', hindiName: 'INC का लखनऊ अधिवेशन 1916 - लखनऊ समझौता', dir: 'Lucknow-Session-of-INC-1916-Lucknow-Pact', desc: 'The Lucknow Session of 1916 and the historic Lucknow Pact between Congress and Muslim League.' },
    { name: 'Mass Participation Extremist Phase', hindiName: 'गरमपंथी चरण में जन भागीदारी', dir: 'Mass-Participation-Extremist-Phase', desc: 'The growth of mass participation in the national movement during the Extremist phase.' },
    { name: 'Militant Nationalism 1905 to 1918', hindiName: 'उग्र राष्ट्रवाद 1905 से 1918', dir: 'Militant-Nationalism-1905-to-1918', desc: 'The rise of militant nationalism in India from the Swadeshi Movement to the end of WWI.' },
    { name: 'Moderate Campaign for Administrative Reforms', hindiName: 'प्रशासनिक सुधारों के लिए नरमपंथी अभियान', dir: 'Moderate-Campaign-for-Administrative-Reforms', desc: 'The moderate campaign for administrative reforms including Indianization of civil services.' },
    { name: 'Moderate Campaign for Constitutional Reforms', hindiName: 'संवैधानिक सुधारों के लिए नरमपंथी अभियान', dir: 'Moderate-Campaign-for-Constitutional-Reforms', desc: 'The moderate phase of constitutional reform demands through petitions and resolutions.' },
    { name: 'Moderate Opinion Against Economic Exploitation', hindiName: 'आर्थिक शोषण के खिलाफ नरमपंथी राय', dir: 'Moderate-Opinion-Against-Economic-Exploitation', desc: 'Moderate nationalist critique of British economic exploitation of India.' },
    { name: 'Montague Statement of August 1917', hindiName: 'अगस्त 1917 का मोंटेग्यू वक्तव्य', dir: 'Montague-Statement-of-August-1917', desc: 'The Montague Declaration of August 1917 promising responsible government in India.' },
    { name: 'Morley Minto Reforms 1909', hindiName: 'मॉर्ले-मिंटो सुधार 1909', dir: 'Morley-Minto-Reforms-1909', desc: 'The Morley-Minto Reforms of 1909 and the introduction of separate electorates.' },
    { name: 'Movement Under Extremist Leadership', hindiName: 'गरमपंथी नेतृत्व में आंदोलन', dir: 'Movement-Under-Extremist-Leadership', desc: 'The national movement under the leadership of Extremists like Tilak, Bipin Chandra Pal, and Lala Lajpat Rai.' },
    { name: 'Movements of All India Muslim League 1906', hindiName: '1906 में अखिल भारतीय मुस्लिम लीग के आंदोलन', dir: 'Movements-of-All-India-Muslim-League-1906', desc: 'The formation and early movements of the All India Muslim League from 1906.' },
    { name: 'National Movement in Light of First World War', hindiName: 'प्रथम विश्व युद्ध के प्रकाश में राष्ट्रीय आंदोलन', dir: 'National-Movement-in-Light-of-First-World-War', desc: 'Impact of the First World War on the Indian national movement and political developments.' },
    { name: 'Pre-INC Campaigns and their Objectives', hindiName: 'INC-पूर्व अभियान और उनके उद्देश्य', dir: 'Pre-INC-Campaigns-and-their-Objectives', desc: 'Political campaigns and movements before the formation of the Indian National Congress.' },
    { name: 'Pre-INC Organisations', hindiName: 'INC-पूर्व संगठन', dir: 'Pre-INC-Organisations', desc: 'Study of pre-INC political organizations like the British Indian Association and Poona Sarvajanik Sabha.' },
    { name: 'Reasons of Muslim League pact with Congress', hindiName: 'कांग्रेस के साथ मुस्लिम लीग समझौते के कारण', dir: 'Reasons-of-Muslim-League-pact-with-Congress', desc: 'Factors leading to the Lucknow Pact of 1916 between the Muslim League and Congress.' },
    { name: 'Reasons of Readmission of Extremists', hindiName: 'गरमपंथियों के पुनः प्रवेश के कारण', dir: 'Reasons-of-Readmission-of-Extremists', desc: 'The circumstances and reasons for the readmission of Extremists into the INC in 1916.' },
    { name: 'Revolutionary Activities', hindiName: 'क्रांतिकारी गतिविधियां', dir: 'Revolutionary-Activities', desc: 'Revolutionary activities in India including the Alipore Bomb Case and Delhi Conspiracy Case.' },
    { name: 'Revolutionary Activities Abroad', hindiName: 'विदेशों में क्रांतिकारी गतिविधियां', dir: 'Revolutionary-Activities-Abroad', desc: 'Indian revolutionary activities abroad including the Ghadar Party, Berlin Committee, and Komagata Maru.' },
    { name: 'Success and Limitations with Moderate Approach', hindiName: 'नरमपंथी दृष्टिकोण की सफलताएं और सीमाएं', dir: 'Success-and-Limitations-with-Moderate-Approach', desc: 'Evaluation of the successes and limitations of the Moderate approach in the national movement.' },
    { name: 'Swadeshi Movement and Associated Leaders', hindiName: 'स्वदेशी आंदोलन और संबद्ध नेता', dir: 'Swadeshi-Movement-and-Associated-Leaders', desc: 'The Swadeshi Movement of 1905 and its key leaders including Bal Gangadhar Tilak and Lala Lajpat Rai.' },
    { name: 'The Moderate Congress 1885-1905', hindiName: 'नरमपंथी कांग्रेस 1885-1905', dir: 'The-Moderate-Congress-1885-1905', desc: 'The Moderate phase of the Indian National Congress from 1885 to 1905 and its constitutional methods.' },
];

function buildMeta(topic, previousTopic, nextTopic) {
    return {
        name: topic.name,
        hindiName: topic.hindiName,
        dir: topic.dir,
        subject: 'Modern History',
        subjectDir: 'modern-history',
        parentTopic: parentTopic,
        parentDir: parentDir,
        previousTopic: previousTopic?.name || '',
        previousDir: previousTopic?.dir || '',
        previousTopicHi: previousTopic?.hindiName || '',
        nextTopic: nextTopic?.name || '',
        nextDir: nextTopic?.dir || '',
        nextTopicHi: nextTopic?.hindiName || '',
        parentTopicHi: parentTopicHi,
        childTopics: [],
        childDirs: [],
        childTopicsHi: [],
        similarTopics: [],
        similarDirs: [],
        similarTopicsHi: [],
        confusedTopics: [],
        confusedDirs: [],
        confusedTopicsHi: [],
        canonicalUrl: `https://sjmaths.com/upsc/modern-history/${parentDir}/${topic.dir}/`,
        description: topic.desc,
        hindiDescription: topic.hindiName + ' पर UPSC GS-1 की विस्तृत गाइड।',
        category: 'GS-1',
        supportsMains: true,
        topicId: `modern-history.first-phase-national-movement.${topic.dir.toLowerCase()}`,
        practiceTypes: ['basic', 'conceptual', 'statement', 'match'],
        difficulty: 'medium',
        studyTime: { concepts: 20, practice: 15, revision: 8 },
        learningObjectives: [
            `Understand the key UPSC concepts for ${topic.name}`,
            `Memorize major events, leaders, and consequences of ${topic.name}`,
            'Apply insights to UPSC Prelims and Mains questions',
        ],
        scope: {
            mustExplain: [topic.name, 'First Phase of National Movement', 'Modern Indian History'],
            mayMention: ['British Rule', 'Indian National Congress', 'Swadeshi Movement'],
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
    console.log('╔══════════════════════════════════════════════════════════════╗');
    console.log('║ UPSC First Phase National Movement (1905-1917) Generator    ║');
    console.log('║ Topics: Modern History / First Phase of National Movement   ║');
    console.log(`║ Total: ${topics.length} microtopics                            ║`);
    console.log('╚══════════════════════════════════════════════════════════════╝\n');

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

    console.log('\n🎉 All 37 First Phase National Movement microtopics generated successfully!');
}

main().catch(err => {
    console.error('Fatal error in main execution loop:', err);
    process.exit(1);
});