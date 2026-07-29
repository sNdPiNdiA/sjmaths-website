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
    name: 'Responsible Factors for Arrival of Europeans',
    hindiName: 'यूरोपियों के भारत आगमन के उत्तरदायी कारक',
    dir: 'Responsible-Factors-for-Arrival-of-Europeans',
    description: 'Analysis of geopolitical, economic, and technological factors driving European maritime expansion to India.',
  },
  {
    name: 'The Columbian Exchange',
    hindiName: 'कोलंबियाई विनिमय (कोलंबियन एक्सचेंज)',
    dir: 'The-Columbian-Exchange',
    description: 'Study of global trade, agricultural crops, pathogens, and economic transformations brought by European arrival.',
  },
  {
    name: 'The Portuguese in India',
    hindiName: 'भारत में पुर्तगाली',
    dir: 'The-Portuguese-in-India',
    description: 'Overview of Portuguese arrival, trade empire (Estado da India), and strategic settlements in India.',
  },
  {
    name: 'Vasco Da Gama',
    hindiName: 'वास्को डी गामा',
    dir: 'Portuguese-Vasco-Da-Gama',
    description: 'Examination of Vasco da Gama\'s 1498 voyage to Calicut, trade treaties, and historical impact.',
  },
  {
    name: 'Pedro Alvarez Cabral',
    hindiName: 'पेड्रो अल्वारेज़ कैब्राल',
    dir: 'Portuguese-Pedro-Alvarez-Cabral',
    description: 'Key developments during Pedro Alvarez Cabral\'s 1500 expedition and factory establishment in Calicut.',
  },
  {
    name: 'Francisco De Almeida',
    hindiName: 'फ्रांसिस्को डी अल्मेडा',
    dir: 'Portuguese-De-Almeida',
    description: 'Analysis of Francisco de Almeida\'s governorship and the Blue Water Policy in the Indian Ocean.',
  },
  {
    name: 'Afonso de Albuquerque',
    hindiName: 'अफोनसो डी अल्बुकर्क',
    dir: 'Portuguese-Albuquerque',
    description: 'Study of Afonso de Albuquerque\'s conquest of Goa (1510), naval choke points, and administrative policies.',
  },
  {
    name: 'Nino Da Cunha',
    hindiName: 'निनो दा कुन्हा',
    dir: 'Portuguese-Nino-Da-Cunha',
    description: 'Review of Nino da Cunha\'s governorship, shift of capital to Goa (1530), and treaty with Bahadur Shah.',
  },
  {
    name: 'Causes of Failure of Portuguese Empire in India',
    hindiName: 'भारत में पुर्तगाली साम्राज्य के पतन के कारण',
    dir: 'Causes-of-Failure-of-Portuguese-empire-in-India',
    description: 'Critical analysis of religious intolerance, corruption, Brazil focus, and European rivalries leading to Portuguese decline.',
  },
  {
    name: 'The Dutch in India',
    hindiName: 'भारत में डच (नेदरलैंड्स)',
    dir: 'The-Dutch-in-India',
    description: 'Overview of United East India Company (VOC), factory networks, and spice trade dominance.',
  },
  {
    name: 'The Dutch Settlements, Personalities, and Decline',
    hindiName: 'डच बस्तियां, व्यक्तित्व और पतन',
    dir: 'The-Dutch-in-India-settlements-personalities-decline',
    description: 'Detailed study of Pulicat, Chinsurah, Nagapatnam settlements, Battle of Bedara (1759), and Dutch exit.',
  },
  {
    name: 'Farrukhsiyar\'s Farman (1717)',
    hindiName: 'फर्रुखसियर का फरमान (1717)',
    dir: 'The-English-Farrukhsiyar-s-Farman',
    description: 'Analysis of the Magna Carta of East India Company, duty-free trade rights, and currency minting privileges.',
  },
  {
    name: 'Causes of English Success in India',
    hindiName: 'भारत में अंग्रेजों की सफलता के कारण',
    dir: 'The-English-Causes-of-English-Success',
    description: 'Evaluation of financial stability, naval superiority, industrial backing, and diplomatic strategies of the British.',
  },
  {
    name: 'The Danes in India',
    hindiName: 'भारत में डेन (डेनमार्क)',
    dir: 'The-Danes-in-India',
    description: 'Overview of Danish East India Company, Serampore mission, and trade operations.',
  },
  {
    name: 'Danish Settlements, Personalities, and Decline',
    hindiName: 'डेनिश बस्तियां, व्यक्तित्व और पतन',
    dir: 'The-Danes-in-India-settlements-personalities-decline',
    description: 'Detailed analysis of Tranquebar (Tharangambadi), Serampore press, and sale of factories to the British (1845).',
  },
  {
    name: 'The French in India',
    hindiName: 'भारत में फ्रांसीसी',
    dir: 'The-French',
    description: 'Establishment of Compagnie des Indes Orientales by Colbert and founding of Pondicherry.',
  },
  {
    name: 'French Settlements, Personalities, and Decline',
    hindiName: 'फ्रांसीसी बस्तियां, व्यक्तित्व और पतन',
    dir: 'The-French-settlements-personalities-decline',
    description: 'Study of Francois Martin, Joseph Francois Dupleix, Battle of Wandiwash (1760), and French defeat.',
  },
  {
    name: 'First Carnatic War (1746–1748)',
    hindiName: 'प्रथम कर्नाटक युद्ध (1746–1748)',
    dir: 'First-Carnatic-War',
    description: 'Causes, course of Battle of St. Thome, and Treaty of Aix-la-Chapelle in Anglo-French rivalry.',
  },
  {
    name: 'The Second Carnatic War (1749–1754)',
    hindiName: 'द्वितीय कर्नाटक युद्ध (1749–1754)',
    dir: 'The-Second-Carnatic-War',
    description: 'Analysis of succession disputes in Hyderabad and Arcot, Siege of Arcot by Clive, and Treaty of Pondicherry.',
  },
  {
    name: 'The Third Carnatic War (1758–1763)',
    hindiName: 'तृतीय कर्नाटक युद्ध (1758–1763)',
    dir: 'The-Third-Carnatic-War',
    description: 'Seven Years War impact, Battle of Wandiwash (1760), Comte de Lally, and Treaty of Paris (1763).',
  },
  {
    name: 'Anglo-French Rivalry',
    hindiName: 'आंग्ल-फ्रांसीसी प्रतिद्वंद्विता',
    dir: 'Anglo-French-Rivalry',
    description: 'Comprehensive analysis of factors leading to British victory over French in Carnatic Wars.',
  },
  {
    name: 'Rise of the Hyderabad State',
    hindiName: 'हैदराबाद राज्य का उदय',
    dir: 'Rise-of-the-Hyderabad-State',
    description: 'Establishment of Asaf Jahi dynasty by Nizam-ul-Mulk Asaf Jah I and role in South Indian politics.',
  },
];

function buildMeta(topic, previousTopic, nextTopic) {
  return {
    name: topic.name,
    hindiName: topic.hindiName,
    dir: topic.dir,
    subject: 'Modern History',
    subjectDir: 'modern-history',
    parentTopic: 'Arrival of Europeans in India',
    parentDir: 'Arrival-of-Europeans-in-India',
    previousTopic: previousTopic?.name || '',
    previousDir: previousTopic?.dir || '',
    previousTopicHi: previousTopic?.hindiName || '',
    nextTopic: nextTopic?.name || '',
    nextDir: nextTopic?.dir || '',
    nextTopicHi: nextTopic?.hindiName || '',
    parentTopicHi: 'भारत में यूरोपियों का आगमन',
    childTopics: [],
    childDirs: [],
    childTopicsHi: [],
    similarTopics: [],
    similarDirs: [],
    similarTopicsHi: [],
    confusedTopics: [],
    confusedDirs: [],
    confusedTopicsHi: [],
    canonicalUrl: `https://sjmaths.com/upsc/modern-history/Arrival-of-Europeans-in-India/${topic.dir}/`,
    description: topic.description,
    hindiDescription: topic.hindiName + ' पर UPSC GS-1 की विस्तृत गाइड।',
    category: 'GS-1',
    supportsMains: true,
    topicId: `modern-history.arrival-of-europeans-in-india.${topic.dir.toLowerCase()}`,
    practiceTypes: ['basic', 'conceptual', 'statement', 'match'],
    difficulty: 'medium',
    studyTime: { concepts: 20, practice: 15, revision: 8 },
    learningObjectives: [
      `Understand the key UPSC concepts for ${topic.name}`,
      `Memorize major events, personalities, treaties, and significance of ${topic.name}`,
      'Apply Modern History insights to UPSC Prelims and Mains questions',
    ],
    scope: {
      mustExplain: [topic.name, 'European arrival', 'Modern Indian History'],
      mayMention: ['East India Company', 'Portuguese', 'Dutch', 'French'],
      neverExplain: ['Gupta Empire', 'Vedic period', 'Mughal Empire internal details'],
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
  console.log('║ UPSC Arrival of Europeans Microtopic Batch Generator    ║');
  console.log('║ Topics: Modern History / Arrival of Europeans in India   ║');
  console.log('╚══════════════════════════════════════════════════════════╝\n');

  const contentClient = new GeminiClient(apiKey, {
    model: 'gemini-3.5-flash-lite',
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

  console.log('\n🎉 All requested Arrival of Europeans microtopics generated successfully!');
}

main().catch(err => {
  console.error('Fatal error in main execution loop:', err);
  process.exit(1);
});
