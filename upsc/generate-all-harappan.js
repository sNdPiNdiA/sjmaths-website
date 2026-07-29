/**
 * UPSC Batch Generator for Harappan / Indus Valley Civilisation microtopics
 * Generates all remaining Harappan microtopics using 1 API call per tab (max quality).
 *
 * Usage:
 *   node upsc/generate-all-harappan.js
 */

import fs from 'fs';
import path from 'path';

if (fs.existsSync('.env')) {
  const envConfig = fs.readFileSync('.env', 'utf8');
  envConfig.split('\n').forEach(line => {
    const [key, value] = line.split('=');
    if (key && value) process.env[key.trim()] = value.trim();
  });
}

import {
  validateMetadata,
  GeminiClient,
  assemblePage,
  createManifest,
  TabCache,
  generateTab,
} from './upsc-microtopic-template.js';

const apiKey = process.env.GEMINI_API_KEY;
if (!apiKey) {
  console.error('❌ GEMINI_API_KEY is not set in environment or .env');
  process.exit(1);
}

const topics = [
  {
    name: 'Decline of Harappan Civilisation',
    hindiName: 'हड़प्पा सभ्यता का पतन',
    dir: 'Decline-of-Harappan-Civilisation',
    description: 'Examination of the causes, chronology, and theories behind the decline and collapse of the Harappan civilization.',
  },
  {
    name: 'Economic Aspects of Indus Valley Civilisation',
    hindiName: 'सिंधु घाटी सभ्यता के आर्थिक पहलू',
    dir: 'Economic-Aspects-of-Indus-Valley-Civilisation',
    description: 'Analysis of the economic foundations, resource management, craft economy, and trade infrastructure of the Harappan world.',
  },
  {
    name: 'Harappan Trade',
    hindiName: 'हड़प्पा व्यापार',
    dir: 'Harappan-Trade',
    description: 'Study of internal and external trade networks, sea trade, Mesopotamian contacts, and Harappan commodities.',
  },
  {
    name: 'Phases of Evolution of Harappan Civilisation',
    hindiName: 'हड़प्पा सभ्यता के विकास के चरण',
    dir: 'Phases-of-Evolution-of-Harappan-Civilisation',
    description: 'Review of the Early, Mature, and Late Harappan phases and their archaeological characteristics.',
  },
  {
    name: 'Religions',
    hindiName: 'धर्म और आस्था',
    dir: 'Religions',
    description: 'Insights into Harappan religious beliefs, mother goddess worship, ritual baths, and sacred symbols.',
  },
  {
    name: 'Script and Language',
    hindiName: 'लिपि और भाषा',
    dir: 'Script-and-Language',
    description: 'Notes on the Harappan script, undeciphered inscriptions, signboard usage, and language theories.',
  },
  {
    name: 'Socio-Cultural Aspects of Indus Valley Civilisation',
    hindiName: 'सिंधु घाटी सभ्यता के सामाजिक-सांस्कृतिक पहलू',
    dir: 'Socio-Cultural-Aspects-of-Indus-Valley-Civilisation',
    description: 'Examination of Harappan society, social structure, family life, gender roles, and cultural practices.',
  },
];

function buildMeta(topic, previousTopic, nextTopic) {
  return {
    name: topic.name,
    hindiName: topic.hindiName,
    dir: topic.dir,
    subject: 'Ancient History',
    subjectDir: 'ancient-history',
    parentTopic: 'Harappan / Indus Valley Civilisation',
    parentDir: 'HarappanIndus-Valley-Civilisation',
    previousTopic: previousTopic?.name || '',
    previousDir: previousTopic?.dir || '',
    previousTopicHi: previousTopic?.hindiName || '',
    nextTopic: nextTopic?.name || '',
    nextDir: nextTopic?.dir || '',
    nextTopicHi: nextTopic?.hindiName || '',
    parentTopicHi: 'हड़प्पा / सिंधु घाटी सभ्यता',
    childTopics: [],
    childDirs: [],
    childTopicsHi: [],
    similarTopics: [],
    similarDirs: [],
    similarTopicsHi: [],
    confusedTopics: [],
    confusedDirs: [],
    confusedTopicsHi: [],
    canonicalUrl: `https://sjmaths.com/upsc/ancient-history/HarappanIndus-Valley-Civilisation/${topic.dir}/`,
    description: topic.description,
    hindiDescription: topic.description,
    category: 'GS-1',
    supportsMains: true,
    topicId: `ancient-history.harappan-indus-valley-civilisation.${topic.dir.toLowerCase()}`,
    practiceTypes: ['basic', 'conceptual', 'statement', 'match'],
    difficulty: 'medium',
    studyTime: { concepts: 20, practice: 15, revision: 8 },
    learningObjectives: [
      `Understand the key UPSC concepts for ${topic.name}`,
      `Memorize major sites, features, and significance of ${topic.name}`,
      'Apply Harappan insights to UPSC Prelims and Mains questions',
    ],
    scope: {
      mustExplain: [topic.name, 'Harappan civilization', 'Indus Valley archaeology'],
      mayMention: ['Mohenjo-daro', 'Harappa', 'Dholavira'],
      neverExplain: ['Mauryan Empire', 'Gupta Empire', 'Vedic period', 'Mughal Empire'],
      relatedTopics: [topic.name],
      keywords: ['Harappan', 'Indus Valley', 'UPSC', topic.name.toLowerCase()],
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
  console.log('║ UPSC Harappan Microtopic Batch Generator                 ║');
  console.log('║ Topics: Harappan / Indus Valley Civilisation             ║');
  console.log('╚══════════════════════════════════════════════════════════╝\n');

  const contentClient = new GeminiClient(apiKey, {
    model: 'gemini-3.5-flash-lite',
    temperature: 0.1,
    maxRetries: 5,
    requestDelay: 12000,
  });

  const tabs = ['overview', 'concepts', 'visual', 'comparisons', 'practice', 'mains', 'revision', 'test'];

  for (let index = 0; index < topics.length; index++) {
    const topic = topics[index];
    const previousTopic = index > 0 ? topics[index - 1] : null;
    const nextTopic = index < topics.length - 1 ? topics[index + 1] : null;
    const meta = buildMeta(topic, previousTopic, nextTopic);

    const validation = validateMetadata(meta);
    if (!validation.passed) {
      console.error(`❌ Metadata validation failed for ${meta.name}:`);
      validation.errors.forEach(e => console.error(`   - ${e}`));
      process.exit(1);
    }

    console.log(`\n${'#'.repeat(72)}`);
    console.log(`[${index + 1}/${topics.length}] Generating: ${meta.name}`);
    console.log(`${'#'.repeat(72)}`);

    const cache = new TabCache(fs, path, process.cwd(), meta);
    const tabResults = {};

    let tabsToGenerate = tabs;
    try {
      const stale = await cache.getStaleTabs(tabs);
      if (stale && stale.length > 0) {
        tabsToGenerate = stale;
        console.log(`🔁 Tabs to generate (stale/missing): ${tabsToGenerate.join(', ')}`);
      } else {
        console.log('⏭️ All tabs are up-to-date in cache.');
        tabsToGenerate = [];
      }
    } catch (e) {
      console.warn('⚠️ Cache check failed; generating all tabs.', e.message);
      tabsToGenerate = tabs;
    }

    for (const tabName of tabsToGenerate) {
      console.log(`\n--- Generating tab: ${tabName} for ${meta.name} ---`);
      try {
        const result = await generateTab(tabName, meta, (prompt) => contentClient.generate(prompt), null, {}, cache);
        tabResults[tabName] = result;
        console.log(`✅ ${tabName} generated: score=${result.score?.overall || 'N/A'} duration=${((result.duration || 0) / 1000).toFixed(1)}s`);
      } catch (err) {
        console.error(`❌ Failed ${tabName}: ${err.message}`);
        tabResults[tabName] = null;
      }
    }

    const bilingualData = {};
    const scores = [];
    for (const tabName of tabs) {
      if (tabResults[tabName]) {
        bilingualData[tabName] = tabResults[tabName].data;
        if (tabResults[tabName].score?.overall) scores.push(tabResults[tabName].score.overall);
      } else {
        try {
          const cached = await cache.get(tabName);
          if (cached) {
            bilingualData[tabName] = cached.data;
            if (cached.score) scores.push(cached.score);
          }
        } catch (e) {}
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

  console.log('\n🎉 All requested Harappan microtopics generated successfully!');
}

main().catch(err => {
  console.error('Fatal error:', err);
  process.exit(1);
});
