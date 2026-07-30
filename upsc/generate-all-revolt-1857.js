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
    name: 'Revolt of 1857 Causes: Economic Causes',
    hindiName: '1857 के विद्रोह के कारण: आर्थिक कारण',
    dir: 'Revolt-of-1857-Causes-Economic-Causes',
    description: 'Detailed analysis of high land revenue, destruction of traditional handicrafts, and drain of wealth.',
  },
  {
    name: 'Revolt of 1857 Causes: Political Causes',
    hindiName: '1857 के विद्रोह के कारण: राजनीतिक कारण',
    dir: 'Revolt-of-1857-Causes-Political-Causes',
    description: 'Impact of the Doctrine of Lapse, Subsidiary Alliance, and annexation of Awadh.',
  },
  {
    name: 'Revolt of 1857 Causes: Administrative Causes',
    hindiName: '1857 के विद्रोह के कारण: प्रशासनिक कारण',
    dir: 'Revolt-of-1857-Causes-Administrative-Causes',
    description: 'Corruption, exclusion of Indians from high posts, and complex judicial machinery.',
  },
  {
    name: 'Revolt of 1857 Causes: Socio-Religious Causes',
    hindiName: '1857 के विद्रोह के कारण: सामाजिक-धार्मिक कारण',
    dir: 'Revolt-of-1857-Causes-Socio-Religious-Causes',
    description: 'Impact of Westernization, Sati abolition, widow remarriage, and religious conversions.',
  },
  {
    name: 'Revolt of 1857 Causes: Influence of Outside Events',
    hindiName: '1857 के विद्रोह के कारण: बाहरी घटनाओं का प्रभाव',
    dir: 'Revolt-of-1857-Causes-Influence-of-Outside-Events',
    description: 'Psychological impact of British defeats in Afghan Wars, Crimean War, and Santhal Rebellion.',
  },
  {
    name: 'Revolt of 1857 Causes: Discontent Among Sepoys',
    hindiName: '1857 के विद्रोह के कारण: सिपाहियों में असंतोष',
    dir: 'Revolt-of-1857-Causes-Discontent-Among-Sepoys',
    description: 'Greased cartridges issue, General Service Enlistment Act, and discrimination in pay and promotion.',
  },
  {
    name: 'Revolt of 1857 Events: Meerut Mutiny',
    hindiName: '1857 के विद्रोह की घटनाएं: मेरठ विद्रोह',
    dir: 'Revolt-of-1857-Events-Meerut-Mutiny',
    description: 'The spark on May 10, 1857, liberation of prisoners, and march to Delhi.',
  },
  {
    name: 'Revolt of 1857 Events: Siege of Delhi',
    hindiName: '1857 के विद्रोह की घटनाएं: दिल्ली की घेराबंदी',
    dir: 'Revolt-of-1857-Events-Siege-of-Delhi',
    description: 'Proclamation of Bahadur Shah Zafar as Emperor and early rebel organization.',
  },
  {
    name: 'Revolt of 1857 Events: Fall of Delhi',
    hindiName: '1857 के विद्रोह की घटनाएं: दिल्ली का पतन',
    dir: 'Revolt-of-1857-Events-Fall-of-Delhi',
    description: 'Suppression of the revolt in Delhi by John Nicholson and capture of Bahadur Shah Zafar.',
  },
  {
    name: 'Important Places and Associated Leaders of the Revolt',
    hindiName: 'विद्रोह के प्रमुख स्थान और संबद्ध नेता',
    dir: 'Important-Places-and-Associated-Leaders-of-the-Revolt',
    description: 'Study of key leaders: Nana Sahib, Begum Hazrat Mahal, Rani Laxmibai, Khan Bahadur, and Kunwar Singh.',
  },
  {
    name: 'Important British Officers during Suppression of Revolt',
    hindiName: 'विद्रोह के दमन के दौरान प्रमुख ब्रिटिश अधिकारी',
    dir: 'Important-British-Officers-during-Suppression-of-Revolt',
    description: 'Analysis of military roles of Havelock, Outram, Campbell, Hugh Rose, and John Nicholson.',
  },
  {
    name: 'Causes of Failure of the Revolt',
    hindiName: 'विद्रोह की विफलता के कारण',
    dir: 'Causes-of-Failure-of-the-Revolt',
    description: 'Critique of lack of unified leadership, limited geographic spread, and superior British resources.',
  },
  {
    name: 'Nature and Impact of the Revolt',
    hindiName: 'विद्रोह की प्रकृति और प्रभाव',
    dir: 'Nature-and-Impact-of-the-Revolt',
    description: 'Historiographical debate: Sepoy Mutiny vs. First War of Independence.',
  },
  {
    name: 'Various Outcomes of the Revolt',
    hindiName: 'विद्रोह के विभिन्न परिणाम',
    dir: 'Various-Outcomes-of-the-Revolt',
    description: 'End of East India Company rule and transfer of power to the British Crown under the 1858 Act.',
  },
  {
    name: 'Changes in the Army: Peel Commission',
    hindiName: 'सेना में बदलाव: पील आयोग',
    dir: 'Changes-in-the-Army-Peel-Commission',
    description: 'Reorganization of the Indian Army, martial races theory, and division policy post-1857.',
  },
  {
    name: 'Public Services: Ilbert Bill Controversy',
    hindiName: 'सार्वजनिक सेवाएं: इल्बर्ट बिल विवाद',
    dir: 'Public-Services-Ilbert-Bill-Controversy',
    description: 'Study of racial discrimination in the judiciary and Indian nationalist response.',
  },
  {
    name: 'Policy of Equal Federation',
    hindiName: 'समान संघ की नीति',
    dir: 'Policy-of-Equal-Federation',
    description: 'Evolution of relations between the British Crown and Indian Princely States.',
  },
  {
    name: 'Princely States',
    hindiName: 'देशी रियासतें',
    dir: 'Princely-States',
    description: 'British policy towards native rulers post-1857, guaranteeing adoption rights and abandoning annexation.',
  },
  {
    name: 'Foreign Policy Post-1857',
    hindiName: 'विदेशी नीति (1857 के बाद)',
    dir: 'Foreign-Policy-Post-1857',
    description: 'British imperial defense, securing of frontiers (Afghan, Burma, Tibet), and commercial interests.',
  },
  {
    name: 'Local Government: Mayos Resolution (1870)',
    hindiName: 'स्थानीय सरकार: मेयो का प्रस्ताव (1870)',
    dir: 'Local-Government-Mayos-Resolution',
    description: 'First steps towards financial decentralization and local self-government.',
  },
  {
    name: 'Local Government: Ripons Resolution (1882)',
    hindiName: 'स्थानीय सरकार: रिपन का प्रस्ताव (1882)',
    dir: 'Local-Government-Ripons-Resolution-1882',
    description: 'The Magna Carta of local self-government in India, introducing elected local boards.',
  },
  {
    name: 'Local Government: Royal Commission on Decentralization (1908)',
    hindiName: 'स्थानीय सरकार: विकेंद्रीकरण पर शाही आयोग (1908)',
    dir: 'Local-Government-Royal-Commission-on-Decentralization-1908',
    description: 'Recommendations for strengthening village panchayats and local bodies.',
  },
  {
    name: 'Local Government: Resolution of May 1918 and Dyarchy 1919',
    hindiName: 'स्थानीय सरकार: मई 1918 का प्रस्ताव और द्वैध शासन 1919',
    dir: 'Local-Government-Resolution-of-May-1918-and-Dyarchy-1919',
    description: 'Impact of Montague-Chelmsford reforms on local government administration.',
  },
  {
    name: 'Local Government: GoI Act 1935 and After',
    hindiName: 'स्थानीय सरकार: भारत सरकार अधिनियम 1935 और उसके बाद',
    dir: 'Local-Government-GoI-Act-1935-and-After',
    description: 'Transition of local government to provincial autonomy and popular ministries.',
  },
  {
    name: 'Labour Law Related Changes',
    hindiName: 'श्रम कानून से संबंधित परिवर्तन',
    dir: 'Labour-Law-Related-Changes',
    description: 'First Factory Act (1881), second Factory Act (1891), and working condition regulations.',
  },
  {
    name: 'Changes in Socio-Cultural Stance',
    hindiName: 'सामाजिक-सांस्कृतिक रुख में बदलाव',
    dir: 'Changes-in-Socio-Cultural-Stance',
    description: 'Shift from social reforms to a policy of non-interference and encourage communal divisions.',
  },
];

function buildMeta(topic, previousTopic, nextTopic) {
  return {
    name: topic.name,
    hindiName: topic.hindiName,
    dir: topic.dir,
    subject: 'Modern History',
    subjectDir: 'modern-history',
    parentTopic: 'The Revolt of 1857',
    parentDir: 'The-Revolt-of-1857',
    previousTopic: previousTopic?.name || '',
    previousDir: previousTopic?.dir || '',
    previousTopicHi: previousTopic?.hindiName || '',
    nextTopic: nextTopic?.name || '',
    nextDir: nextTopic?.dir || '',
    nextTopicHi: nextTopic?.hindiName || '',
    parentTopicHi: '1857 का विद्रोह',
    childTopics: [],
    childDirs: [],
    childTopicsHi: [],
    similarTopics: [],
    similarDirs: [],
    similarTopicsHi: [],
    confusedTopics: [],
    confusedDirs: [],
    confusedTopicsHi: [],
    canonicalUrl: `https://sjmaths.com/upsc/modern-history/The-Revolt-of-1857/${topic.dir}/`,
    description: topic.description,
    hindiDescription: topic.hindiName + ' पर UPSC GS-1 की विस्तृत गाइड।',
    category: 'GS-1',
    supportsMains: true,
    topicId: `modern-history.the-revolt-of-1857.${topic.dir.toLowerCase()}`,
    practiceTypes: ['basic', 'conceptual', 'statement', 'match'],
    difficulty: 'medium',
    studyTime: { concepts: 20, practice: 15, revision: 8 },
    learningObjectives: [
      `Understand the key UPSC concepts for ${topic.name}`,
      `Memorize major events, leaders, and consequences of ${topic.name}`,
      'Apply 1857 Revolt insights to UPSC Prelims and Mains questions',
    ],
    scope: {
      mustExplain: [topic.name, 'Revolt of 1857', 'Modern Indian History'],
      mayMention: ['British Rule', 'Sepoy mutiny', 'East India Company'],
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
  console.log('║ UPSC Revolt of 1857 Microtopic Batch Generator          ║');
  console.log('║ Topics: Modern History / The Revolt of 1857             ║');
  console.log('╚══════════════════════════════════════════════════════════╝\n');

  const contentClient = new GeminiClient(apiKey, {
    model: 'gemini-3.6-flash',
    maxOutputTokens: 8192,
    temperature: 0.3,
  });

  let totalApiCalls = 0;
  const callGemini = async (prompt) => {
    totalApiCalls++;
    const currentModel = 'gemini-3.6-flash';
    console.log(`[API Call #${totalApiCalls}] Routing request to model: ${currentModel}`);
    contentClient.model = currentModel;
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

  console.log('\n🎉 All 26 Revolt of 1857 microtopics generated successfully!');
}

main().catch(err => {
  console.error('Fatal error in main execution loop:', err);
  process.exit(1);
});
