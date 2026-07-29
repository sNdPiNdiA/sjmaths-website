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
    name: 'Settlements at Various Places',
    hindiName: 'विभिन्न स्थानों पर EIC की बस्तियां',
    dir: 'Settlements-at-Various-Places',
    description: 'Establishment of early British factories and settlements in Surat, Madras, Bombay, and Calcutta.',
  },
  {
    name: 'British Conquest of Bengal',
    hindiName: 'बंगाल पर ब्रिटिश विजय',
    dir: 'British-Conquest-of-Bengal',
    description: 'Detailed analysis of political, economic, and strategic factors leading to British dominance in Bengal.',
  },
  {
    name: 'Bengal: Battle of Plassey (1757)',
    hindiName: 'बंगाल: प्लासी का युद्ध (1757)',
    dir: 'Bengal-Battle-of-Plassey',
    description: 'Causes, course, key personalities (Siraj-ud-daulah, Robert Clive), treachery, and historical significance of the Battle of Plassey.',
  },
  {
    name: 'Bengal: Battle of Buxar (1764)',
    hindiName: 'बंगाल: बक्सर का युद्ध (1764)',
    dir: 'Bengal-Battle-of-Buxar',
    description: 'Analysis of the conflict between the joint forces (Mir Qasim, Shuja-ud-daulah, Shah Alam II) and the British, and its decisive consequences.',
  },
  {
    name: 'Bengal: Treaty of Allahabad (1765)',
    hindiName: 'बंगाल: इलाहाबाद की संधि (1765)',
    dir: 'Bengal-Treaty-of-Allahabad',
    description: 'Terms of the treaty signed with Shuja-ud-daulah and Shah Alam II, securing Diwani rights for the East India Company.',
  },
  {
    name: 'Bengal: Dual Polity in Bengal (1765–1772)',
    hindiName: 'बंगाल: बंगाल में द्वैध शासन (1765-1772)',
    dir: 'Bengal-Dual-Polity-in-Bengal-Diwani-and-Nizamat',
    description: 'Evaluation of the division of power between Diwani (revenue collection) and Nizamat (administrative responsibility) under Robert Clive.',
  },
  {
    name: '4 Anglo-Mysore Wars',
    hindiName: '4 आंग्ल-मैसूर युद्ध',
    dir: '4-Anglo-Mysore-Wars',
    description: 'Detailed study of conflicts with Hyder Ali and Tipu Sultan, strategic treaties, and the annexation of Mysore.',
  },
  {
    name: '3 Anglo-Maratha Wars',
    hindiName: '3 आंग्ल-मराठा युद्ध',
    dir: '3-Anglo-Maratha-Wars',
    description: 'Study of British interventions in Maratha politics, major battles, internal dissensions, and final British victory.',
  },
  {
    name: 'Prominent Maratha Families Ruling from Different Places',
    hindiName: 'विभिन्न स्थानों से शासन करने वाले प्रमुख मराठा परिवार',
    dir: 'Prominent-Maratha-Families-Ruling-from-Different-Places',
    description: 'Overview of the Maratha Confederacy: Peshwa (Pune), Gaekwad (Baroda), Scindia (Gwalior), Holkar (Indore), and Bhonsle (Nagpur).',
  },
  {
    name: 'EIC Treaties: Surat, Purandar, Salbai, Bassein, Poona, Gwalior, and Mandsor',
    hindiName: 'EIC संधियां: सूरत, पुरंदर, साल्बाई, बेसिन, पूना, ग्वालियर और मंदसौर',
    dir: 'EIC-Treaties-Surat-Purandar-Salbai-Bassein-Poona-Gwalior-and-Mandsor',
    description: 'Critical analysis of treaties signed by the East India Company to consolidate power over Indian states.',
  },
  {
    name: 'Marathas Defeat and its Reasons',
    hindiName: 'मराठा पराजय और उसके कारण',
    dir: 'Marathas-Defeat-and-its-reasons',
    description: 'Evaluation of structural, military, administrative, and economic factors leading to the fall of the Maratha Empire.',
  },
  {
    name: 'The Subsidiary Alliance System and its Impact',
    hindiName: 'सहायक संधि प्रणाली और उसका प्रभाव',
    dir: 'The-Subsidiary-Alliance-System-and-its-Impact',
    description: 'Detailed analysis of Lord Wellesley\'s system, terms of the alliance, and its impact on the sovereignty of Indian princely states.',
  },
];

function buildMeta(topic, previousTopic, nextTopic) {
  return {
    name: topic.name,
    hindiName: topic.hindiName,
    dir: topic.dir,
    subject: 'Modern History',
    subjectDir: 'modern-history',
    parentTopic: 'Expansion of East India Company',
    parentDir: 'Expansion-of-East-India-Company',
    previousTopic: previousTopic?.name || '',
    previousDir: previousTopic?.dir || '',
    previousTopicHi: previousTopic?.hindiName || '',
    nextTopic: nextTopic?.name || '',
    nextDir: nextTopic?.dir || '',
    nextTopicHi: nextTopic?.hindiName || '',
    parentTopicHi: 'ईस्ट इंडिया कंपनी का विस्तार',
    childTopics: [],
    childDirs: [],
    childTopicsHi: [],
    similarTopics: [],
    similarDirs: [],
    similarTopicsHi: [],
    confusedTopics: [],
    confusedDirs: [],
    confusedTopicsHi: [],
    canonicalUrl: `https://sjmaths.com/upsc/modern-history/Expansion-of-East-India-Company/${topic.dir}/`,
    description: topic.description,
    hindiDescription: topic.hindiName + ' पर UPSC GS-1 की विस्तृत गाइड।',
    category: 'GS-1',
    supportsMains: true,
    topicId: `modern-history.expansion-of-east-india-company.${topic.dir.toLowerCase()}`,
    practiceTypes: ['basic', 'conceptual', 'statement', 'match'],
    difficulty: 'medium',
    studyTime: { concepts: 20, practice: 15, revision: 8 },
    learningObjectives: [
      `Understand the key UPSC concepts for ${topic.name}`,
      `Memorize major events, battles, treaties, and significance of ${topic.name}`,
      'Apply Modern History insights to UPSC Prelims and Mains questions',
    ],
    scope: {
      mustExplain: [topic.name, 'East India Company expansion', 'Modern Indian History'],
      mayMention: ['Bengal conquest', 'British Empire', 'Princely states'],
      neverExplain: ['Gupta Empire', 'Harappan trade details', 'Vedic rituals'],
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
  console.log('║ UPSC EIC Expansion Microtopic Batch Generator            ║');
  console.log('║ Topics: Modern History / Expansion of East India Company ║');
  console.log('╚══════════════════════════════════════════════════════════╝\n');

  const contentClient = new GeminiClient(apiKey, {
    model: 'gemini-2.5-flash',
    maxOutputTokens: 8192,
    temperature: 0.3,
  });

  const callGemini = async (prompt) => {
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

  console.log('\n🎉 All 12 Expansion of East India Company microtopics generated successfully!');
}

main().catch(err => {
  console.error('Fatal error in main execution loop:', err);
  process.exit(1);
});
