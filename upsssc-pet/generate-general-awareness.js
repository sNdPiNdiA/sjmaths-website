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
if (!apiKey) { console.error('GEMINI_API_KEY is not set'); process.exit(1); }

const GEMINI_API = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash-lite:generateContent';

async function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function callGemini(prompt, retries = 3) {
  for (let attempt = 1; attempt <= retries; attempt++) {
    try {
      const res = await fetch(GEMINI_API, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-goog-api-key': apiKey,
        },
        body: JSON.stringify({
          contents: [{ parts: [{ text: prompt }] }],
          generationConfig: { temperature: 0.1, maxOutputTokens: 8192 },
        }),
      });
      if (res.status === 429) {
        const wait = 13000; // 13s delay as requested
        console.log(`  Rate limited. Waiting ${wait / 1000}s before retry ${attempt}/${retries}...`);
        await sleep(wait);
        continue;
      }
      if (!res.ok) throw new Error(`Gemini API error: ${res.status}`);
      const data = await res.json();
      const text = data?.candidates?.[0]?.content?.parts?.[0]?.text || '';
      if (!text || text.trim().length === 0) {
        throw new Error('Empty response from API');
      }
      return text;
    } catch (err) {
      if (attempt === retries) throw err;
      console.log(`  Retry ${attempt}/${retries} after error: ${err.message}`);
      await sleep(5000);
    }
  }
}

function kebabToTitle(kebab) {
  return kebab.split('-').map(word => {
    if (word.toLowerCase() === 'uts' || word.toLowerCase() === 'ut') return 'UTs';
    if (word.toLowerCase() === 'dpsp') return 'DPSP';
    if (word.toLowerCase() === 'pesa') return 'PESA';
    if (word.toLowerCase() === 'scs' || word.toLowerCase() === 'st') return word.toUpperCase();
    return word.charAt(0).toUpperCase() + word.slice(1);
  }).join(' ');
}

function slugify(text) {
  return text.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-+|-+$/g, '');
}

const TOPICS = [
  { dir: 'awards-winners', name: 'Awards & Winners', description: 'Important national and international awards, honours, and their recipients for UPSSSC PET General Awareness.' },
  { dir: 'climate-change-environment', name: 'Climate Change & Environment', description: 'Key environmental issues, climate change concepts, and conservation efforts for competitive exams.' },
  { dir: 'countries-capitals-currencies', name: 'Countries, Capitals & Currencies', description: 'World geography facts covering countries, their capitals, and official currencies for exam preparation.' },
  { dir: 'famous-books-authors', name: 'Famous Books & Authors', description: 'Notable literary works and their authors from India and around the world for general awareness.' },
  { dir: 'india-world-sports', name: 'India & World Sports', description: 'Major sporting events, tournaments, and famous sportspersons for UPSSSC PET preparation.' },
  { dir: 'indian-art-culture', name: 'Indian Art & Culture', description: 'Rich cultural heritage of India including classical arts, festivals, and traditions for competitive exams.' },
  { dir: 'indian-parliament-rajya-sabha-lok-sabha', name: 'Indian Parliament (Rajya Sabha & Lok Sabha)', description: 'Structure, functions, and procedures of Indian Parliament for UPSSSC PET General Awareness.' },
  { dir: 'indian-research-organizations', name: 'Indian Research Organizations', description: 'Key research institutions and their headquarters in India for general knowledge preparation.' },
  { dir: 'indian-states-union-territories', name: 'Indian States & Union Territories', description: 'States and UTs of India with capitals, areas, and important facts for competitive examinations.' },
  { dir: 'indian-tourist-places', name: 'Indian Tourist Places', description: 'Famous tourist destinations, heritage sites, and monuments across India for general awareness.' },
  { dir: 'national-international-days', name: 'National & International Days', description: 'Important dates, days, and their significance observed nationally and internationally.' },
  { dir: 'neighboring-countries-of-india', name: 'Neighboring Countries of India', description: 'India\'s neighboring countries with their capitals, leaders, and key facts for exam preparation.' },
  { dir: 'world-organizations-headquarters', name: 'World Organizations & Headquarters', description: 'Major international organizations and their headquarters locations for general awareness.' },
];

const GLOSSARY = {
  'Constitution': 'संविधान',
  'Parliament': 'संसद',
  'President': 'राष्ट्रपति',
  'Prime Minister': 'प्रधान मंत्री',
  'Supreme Court': 'सर्वोच्च न्यायालय',
  'Election Commission': 'चुनाव आयोग',
  'Reserve Bank': 'रिजर्व बैंक',
  'United Nations': 'संयुक्त राष्ट्र',
  'World Bank': 'विश्व बैंक',
  'IMF': 'IMF',
  'UNESCO': 'UNESCO',
  'WHO': 'WHO',
  'NATO': 'NATO',
  'SAARC': 'SAARC',
  'ASEAN': 'ASEAN',
  'G20': 'G20',
  'BRICS': 'BRICS',
  'UNSC': 'UNSC',
  'Olympics': 'ओलंपिक',
  'Cricket': 'क्रिकेट',
  'Tennis': 'टेनिस',
  'Football': 'फुटबॉल',
  'Hockey': 'हॉकी',
  'Badminton': 'बैडमिंटन',
  'Arjuna Award': 'अर्जुन पुरस्कार',
  'Padma Vibhushan': 'पद्म विभूषण',
  'Padma Bhushan': 'पद्म भूषण',
  'Padma Shri': 'पद्म श्री',
  'Bharat Ratna': 'भारत रत्न',
  'Nobel Prize': 'नोबेल पुरस्कार',
  'Booker Prize': 'बुकर पुरस्कार',
  'Pulitzer Prize': 'पुलित्जर पुरस्कार',
};

async function translateMetadata(name, description) {
  return {
    hindiName: name,
    hindiDescription: name + ' पर UPSSSC PET की विस्तृत गाइड।'
  };
}

function promptConcepts(meta) {
  return `You are an expert faculty for UPSSSC PET exam. Write COMPREHENSIVE, EXAM-FOCUSED concept notes for the topic: "${meta.name}".

CRITICAL REQUIREMENTS FOR UPSSSC PET EXAM SUCCESS:
1. Write 12-15 sections minimum - this must be ULTRA COMPREHENSIVE to clear the exam
2. Cover ALL important facts, dates, names, figures, events, awards, organizations, and their details
3. Include multiple tables with 8-10 rows each - not just 1-2 rows
4. Include detailed classifications with 5-6 categories minimum
5. Add powerful mnemonics and memory tricks
6. Include important statistics, years, and numerical data
7. Add comparison tables for related items
8. Include famous personalities, their contributions, and associated facts
9. Add pro tips specifically for UPSSSC PET exam pattern
10. Use ONLY English text. Do NOT use Hindi or bilingual format.

Generate JSON with this COMPREHENSIVE structure:
{
  "sections": [
    {
      "title": "Complete Overview & Important Facts",
      "type": "table",
      "headers": ["Category", "Important Details"],
      "rows": [
        ["Category 1", "Detailed fact with all important information"],
        ["Category 2", "Another important fact"]
      ]
    },
    {
      "title": "Detailed Classification System",
      "type": "classification",
      "categories": [
        {
          "name": "Category A with details",
          "items": ["Item 1", "Item 2", "Item 3"]
        },
        {
          "name": "Category B with details",
          "items": ["Item 1", "Item 2"]
        }
      ]
    },
    {
      "title": "Important Dates, Years & Timeline",
      "type": "datatable",
      "headers": ["Year/Date", "Event/Fact", "Significance"],
      "rows": [
        ["2024", "Event name with full details", "Why it matters for exam"]
      ]
    },
    {
      "title": "Powerful Mnemonic for Complete Memorization",
      "type": "mnemonic",
      "phrase": "Mnemonic phrase to remember everything",
      "expansion": "What each part stands for",
      "usage": "How to use this mnemonic effectively"
    },
    {
      "title": "Exam-Critical Tricks & Shortcuts",
      "type": "tricks",
      "tricks": [
        {
          "title": "Trick 1: How to remember",
          "description": "Detailed explanation of the trick"
        },
        {
          "title": "Trick 2: Quick recall method",
          "description": "How to use this trick"
        }
      ]
    },
    {
      "title": "Complete Comparison Matrix",
      "type": "comparison",
      "headers": ["Aspect", "Option A", "Option B", "Option C"],
      "rows": [
        ["Aspect 1", "Detail A", "Detail B", "Detail C"]
      ]
    },
    {
      "title": "Famous Personalities & Their Contributions",
      "type": "table",
      "headers": ["Name", "Contribution/Achievement", "Year/Period", "Significance"],
      "rows": [
        ["Person 1", "Major contribution", "Year", "Why important"]
      ]
    },
    {
      "title": "Important Statistics & Key Figures",
      "type": "datatable",
      "headers": ["Item/Parameter", "Value/Figure", "Year/Source", "Relevance"],
      "rows": [
        ["Parameter 1", "Important value", "2024", "Why it matters"]
      ]
    },
    {
      "title": "Awards, Honors & Recognitions",
      "type": "table",
      "headers": ["Award/Honor", "Recipient", "Year", "Field/Category"],
      "rows": [
        ["Award 1", "Winner name", "2024", "Category"]
      ]
    },
    {
      "title": "Headquarters & Locations",
      "type": "table",
      "headers": ["Organization/Entity", "Headquarters/Location", "Country/City"],
      "rows": [
        ["Org 1", "HQ location", "Country"]
      ]
    },
    {
      "title": "Key Terms & Definitions",
      "type": "table",
      "headers": ["Term", "Definition", "Context"],
      "rows": [
        ["Term 1", "Clear definition", "Where used"]
      ]
    },
    {
      "title": "Pro Tips for UPSSSC PET Exam",
      "type": "tips",
      "tips": [
        {
          "point": "Exam pattern insight 1",
          "explanation": "Why this is frequently asked and how to prepare"
        },
        {
          "point": "Exam pattern insight 2",
          "explanation": "Common mistakes to avoid"
        },
        {
          "point": "Memory technique",
          "explanation": "How to memorize quickly and retain"
        }
      ]
    }
  ],
  "keyTakeaways": [
    "Most important takeaway 1",
    "Most important takeaway 2",
    "Most important takeaway 3",
    "Most important takeaway 4"
  ]
}`;
}

function promptPractice(meta) {
  return `You are an expert faculty for UPSSSC PET exam. Create practice questions for topic: "${meta.name}".

Generate exactly these types with exactly these counts:
- 7 Basic MCQs
- 7 Statement-based questions
- 7 Matching type questions
- 7 Assertion-Reason questions

After that, create a mini test of 10 questions mixing all types.

IMPORTANT RULES:
1. Each option in MCQ/Statement/Matching/Assertion-Reason must have detailed explanation.
2. Explanations must explain why each option is correct or incorrect.
3. All questions must be directly relevant to the topic: ${meta.name}.
4. Use realistic, factual content - no dummy text.
5. Use ONLY English text. Do NOT use Hindi or bilingual format.

Generate JSON with this exact structure:
{
  "basicMcqs": [
    {
      "id": 1,
      "question": "Question text?",
      "options": [
        {"letter": "A", "text": "Option A", "correct": false},
        {"letter": "B", "text": "Option B", "correct": true},
        {"letter": "C", "text": "Option C", "correct": false},
        {"letter": "D", "text": "Option D", "correct": false}
      ],
      "explanation": "Correct answer explanation. Why A is wrong, B is correct, C and D are wrong."
    }
  ],
  "statementBased": [
    {
      "id": 8,
      "question": "Consider the following statements:",
      "statements": [
        {"number": 1, "text": "Statement 1", "correct": true},
        {"number": 2, "text": "Statement 2", "correct": false}
      ],
      "options": [
        {"letter": "A", "text": "1 only", "correct": true},
        {"letter": "B", "text": "2 only", "correct": false},
        {"letter": "C", "text": "Both 1 and 2", "correct": false},
        {"letter": "D", "text": "Neither 1 nor 2", "correct": false}
      ],
      "explanation": "Explanation covering why statement 1 is correct, why statement 2 is incorrect, and why the answer is correct."
    }
  ],
  "matchingType": [
    {
      "id": 15,
      "question": "Match the items in List I with List II:",
      "pairs": [
        {"left": "1. Item A", "right": "A. Match A"},
        {"left": "2. Item B", "right": "B. Match B"},
        {"left": "3. Item C", "right": "C. Match C"},
        {"left": "4. Item D", "right": "D. Match D"}
      ],
      "options": [
        {"letter": "A", "text": "1-C, 2-D, 3-B, 4-A", "correct": true},
        {"letter": "B", "text": "1-A, 2-B, 3-C, 4-D", "correct": false},
        {"letter": "C", "text": "1-D, 2-A, 3-B, 4-C", "correct": false},
        {"letter": "D", "text": "1-B, 2-C, 3-D, 4-A", "correct": false}
      ],
      "explanation": "Explanation for correct matching and why other options are wrong."
    }
  ],
  "assertionReason": [
    {
      "id": 22,
      "question": "Assertion (A): ... Reason (R): ...",
      "options": [
        {"letter": "A", "text": "Both A and R are true and R explains A", "correct": true},
        {"letter": "B", "text": "Both A and R are true but R does not explain A", "correct": false},
        {"letter": "C", "text": "A is true but R is false", "correct": false},
        {"letter": "D", "text": "A is false but R is true", "correct": false}
      ],
      "explanation": "Explanation for assertion and reason relationship."
    }
  ],
  "miniTest": [
    {
      "id": 29,
      "question": "Mixed type question 1?",
      "options": [
        {"letter": "A", "text": "Option A"},
        {"letter": "B", "text": "Option B"},
        {"letter": "C", "text": "Option C"},
        {"letter": "D", "text": "Option D"}
      ],
      "correctAnswer": "A",
      "explanation": "Explanation"
    }
  ]
}`;
}

function promptRevision(meta) {
  return `You are an expert faculty for UPSSSC PET exam. Create ultra-condensed revision notes for topic: "${meta.name}".

Make it extremely visual and easy to memorize using:
- Bullet points only (no paragraphs)
- Flow diagrams in text
- Comparison tables
- Mnemonics
- Color-coded importance levels

Use ONLY English text. Do NOT use Hindi or bilingual format.

Generate JSON:
{
  "onePageNotes": {
    "columns": [
      {
        "title": "Key Facts",
        "points": [
          "Fact in English"
        ]
      }
    ]
  },
  "mnemonics": [
    {
      "phrase": "Mnemonic",
      "meaning": "What it means",
      "explanation": "How to remember"
    }
  ],
  "flashcards": [
    {
      "question": "Question?",
      "answer": "Answer"
    }
  ],
  "frequentlyConfusedFacts": [
    {
      "misconception": "Wrong belief",
      "correction": "Correct fact"
    }
  ],
  "examDaySheet": {
    "fiveFacts": [
      "Must know fact 1"
    ],
    "threeTraps": [
      "Common trap 1"
    ],
    "oneMnemonic": {
      "phrase": "Quick recall mnemonic",
      "meaning": "Meaning"
    }
  }
}`;
}

const PROMPT_GENERATORS = {
  concepts: promptConcepts,
  practice: promptPractice,
  revision: promptRevision,
};

function generatePrompt(tabName, meta) {
  const generator = PROMPT_GENERATORS[tabName];
  if (!generator) throw new Error(`Unknown tab: ${tabName}`);
  return generator(meta);
}

function parseResponse(raw) {
  if (!raw || typeof raw !== 'string') {
    throw new Error('Invalid response: expected string, got ' + typeof raw);
  }
  let cleaned = raw.trim();
  if (cleaned.startsWith('```json')) cleaned = cleaned.replace(/^```json\s*/, '').replace(/\s*```$/, '');
  else if (cleaned.startsWith('```')) cleaned = cleaned.replace(/^```\s*/, '').replace(/\s*```$/, '');
  cleaned = cleaned.replace(/[\u2018\u2019]/g, "'").replace(/[\u201c\u201d]/g, '"');
  try { return JSON.parse(cleaned); } catch (err) { }
  const jsonMatch = cleaned.match(/[\{\[][\s\S]*[\}\]]/);
  if (jsonMatch) {
    const repaired = jsonMatch[0].replace(/(\{|,|\[|\s)([A-Za-z0-9_\-]+)\s*:/g, '$1"$2":').replace(/'([^'\\]*(?:\\.[^'\\]*)*)'/g, '"$1"').replace(/,\s*([}\]])/g, '$1');
    try { return JSON.parse(repaired); } catch (e) { return JSON.parse(Function('"use strict"; return (' + repaired + ')')()); }
  }
  console.error('Raw response (first 500 chars):', cleaned.substring(0, 500));
  throw new Error('No JSON found in response');
}

function buildMeta(topic) {
  return {
    name: topic.name,
    hindiName: topic.name,
    dir: topic.dir,
    subject: 'General Awareness',
    subjectDir: 'general-awareness',
    parentTopic: 'General Awareness',
    parentDir: 'general-awareness',
    previousTopic: '',
    previousDir: '',
    previousTopicHi: '',
    nextTopic: '',
    nextDir: '',
    nextTopicHi: '',
    parentTopicHi: 'सामान्य जागरूकता',
    childTopics: [],
    childDirs: [],
    childTopicsHi: [],
    similarTopics: [],
    similarDirs: [],
    similarTopicsHi: [],
    confusedTopics: [],
    confusedDirs: [],
    confusedTopicsHi: [],
    canonicalUrl: `https://sjmaths.com/upsssc-pet/general-awareness/${topic.dir}/`,
    description: topic.description,
    hindiDescription: topic.description + ' UPSSSC PET के लिए महत्वपूर्ण जानकारी।',
    category: 'PET',
    supportsMains: false,
    topicId: `upsssc-pet.general-awareness.${topic.dir}`,
    practiceTypes: ['basic', 'conceptual', 'statement', 'assertion', 'match', 'advanced'],
    difficulty: 'medium',
    studyTime: { concepts: 25, practice: 30, revision: 10 },
    learningObjectives: [
      `Understand key concepts of ${topic.name}`,
      `Memorize important facts and figures`,
      `Apply knowledge to UPSSSC PET questions`
    ],
    scope: {
      mustExplain: [topic.name, 'Important facts', 'Key figures', 'Relevant dates'],
      mayMention: ['Related topics', 'Current context'],
      neverExplain: ['Ancient history', 'Unrelated subjects'],
      relatedTopics: [topic.name],
      keywords: ['UPSSSC PET', 'General Awareness', topic.name]
    },
    related: {
      prerequisite: [],
      recommendedNext: [],
      advancedTopics: [topic.name]
    }
  };
}

function cleanUndefined(obj) {
  if (typeof obj === 'undefined') return null;
  if (Array.isArray(obj)) return obj.map(item => cleanUndefined(item));
  if (obj && typeof obj === 'object') {
    const cleaned = {};
    for (const [key, value] of Object.entries(obj)) {
      if (typeof value !== 'undefined') cleaned[key] = cleanUndefined(value);
    }
    return cleaned;
  }
  return obj;
}

function assemblePage(meta, data) {
  const now = new Date().toISOString();
  return `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>${meta.name} | UPSSSC PET General Awareness | SJMaths</title>
  <meta name="description" content="${meta.description}">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="${meta.canonicalUrl}">
  <meta name="keywords" content="UPSSSC PET, ${meta.name}, General Awareness, ${meta.subject}">
  <link rel="icon" type="image/png" href="/favicon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Outfit:wght@500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/assets/css/main.min.css?v=4ba21ce7">
  <link rel="stylesheet" href="/assets/css/layout.min.css?v=e4922b08">
  <link rel="stylesheet" href="/assets/css/component.min.css?v=8c99f11f">
  <link rel="stylesheet" href="/assets/css/improved-ui.min.css?v=86f5556a">
  <link rel="stylesheet" href="/assets/css/pages.min.css?v=9e3bd560">
  <link rel="stylesheet" href="/assets/css/competitive-exam-guide.min.css?v=bcdc8e39">
  <style>
    :root {
      --up-primary: #0f172a;
      --up-accent: #3b82f6;
      --up-accent-purple: #8b5cf6;
      --up-surface: rgba(255, 255, 255, 0.85);
      --up-radius-xl: 24px;
      --up-radius-lg: 16px;
    }
    html.lang-en .lang-hi, body.lang-en .lang-hi, html:not(.lang-hi) .lang-hi, body:not(.lang-hi):not(.lang-en) .lang-hi { display: none !important; }
    html.lang-hi .lang-en, body.lang-hi .lang-en { display: none !important; }
    .topic-container { max-width: 1150px; margin: 2rem auto; padding: 0 1.5rem 3rem; animation: upFadeIn 0.6s ease-out; }
    .breadcrumbs { margin-bottom: 1.5rem; font-size: 0.88rem; color: #64748b; background: rgba(255, 255, 255, 0.6); display: inline-block; padding: 0.6rem 1.2rem; border-radius: 999px; border: 1px solid rgba(0, 0, 0, 0.04); }
    .breadcrumbs a { color: var(--up-accent); text-decoration: none; font-weight: 500; }
    .breadcrumbs a:hover { color: var(--up-accent-purple); text-decoration: underline; }
    .breadcrumbs i { margin: 0 0.5rem; font-size: 0.7rem; color: #94a3b8; }
    .topic-header { background: linear-gradient(135deg, rgba(59, 130, 246, 0.03), rgba(139, 92, 246, 0.03), rgba(212, 175, 55, 0.03)); border: 1px solid rgba(59, 130, 246, 0.08); border-radius: var(--up-radius-xl); padding: 2.5rem; margin-bottom: 1.75rem; text-align: center; position: relative; overflow: hidden; backdrop-filter: blur(10px); }
    .topic-header h1 { font-family: 'Outfit', 'Inter', system-ui, sans-serif; font-size: clamp(2rem, 5vw, 2.75rem); font-weight: 800; background: linear-gradient(135deg, var(--up-primary) 0%, var(--up-accent) 50%, var(--up-accent-purple) 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; margin-bottom: 0.75rem; line-height: 1.2; letter-spacing: -0.02em; }
    .topic-desc { color: #475569; font-size: clamp(0.95rem, 2vw, 1.05rem); line-height: 1.7; max-width: 780px; margin: 0 auto; }
    .topic-meta-bar { display: flex; flex-wrap: wrap; gap: 1rem; justify-content: center; align-items: center; margin-top: 1.5rem; padding-top: 1.25rem; border-top: 1px solid rgba(0, 0, 0, 0.05); }
    .topic-difficulty { display: inline-flex; align-items: center; gap: 0.45rem; padding: 0.45rem 0.9rem; border-radius: 999px; font-size: 0.85rem; font-weight: 600; background: rgba(245, 158, 11, 0.1); color: #b45309; border: 1px solid rgba(245, 158, 11, 0.2); }
    .topic-study-time { display: inline-flex; align-items: center; gap: 0.45rem; padding: 0.45rem 0.9rem; border-radius: 999px; font-size: 0.85rem; font-weight: 600; color: #475569; background: rgba(100, 116, 139, 0.06); border: 1px solid rgba(100, 116, 139, 0.12); }
    .lang-toggle { display: inline-flex; background: rgba(59, 130, 246, 0.06); border: 1px solid rgba(59, 130, 246, 0.12); border-radius: 999px; padding: 0.2rem; gap: 0.2rem; }
    .lang-toggle button { border: none; background: transparent; color: #64748b; font-weight: 600; padding: 0.35rem 0.85rem; border-radius: 999px; cursor: pointer; font-size: 0.8rem; transition: all 0.2s ease; }
    .lang-toggle button.active { background: #ffffff; color: var(--up-accent); box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08); }
    .study-tabs { display: flex; flex-wrap: wrap; gap: 0.5rem; padding: 0.55rem; background: var(--up-surface); border: 1px solid rgba(0, 0, 0, 0.05); border-radius: var(--up-radius-lg); margin-bottom: 2rem; position: sticky; top: 88px; z-index: 100; backdrop-filter: blur(16px); justify-content: center; }
    .tab-btn { border: none; background: transparent; color: #475569; padding: 0.65rem 1.1rem; border-radius: 999px; cursor: pointer; font-weight: 600; font-size: 0.9rem; font-family: 'Outfit', 'Inter', system-ui, sans-serif; display: inline-flex; align-items: center; gap: 0.5rem; transition: all 0.3s ease; white-space: nowrap; }
    .tab-btn:hover { background: rgba(59, 130, 246, 0.08); color: var(--up-accent); }
    .tab-btn.active { background: linear-gradient(135deg, var(--up-accent), var(--up-accent-purple)); color: #ffffff; box-shadow: 0 8px 20px rgba(59, 130, 246, 0.25); }
    .topic-content { min-height: 400px; }
    .tab-panel { display: none; }
    .tab-panel.active { display: block; }
    .concept-section { margin-bottom: 2rem; padding: 1.5rem; background: #f8fafc; border-radius: 16px; border: 1px solid #e2e8f0; }
    .concept-section h3 { margin-bottom: 1rem; color: var(--up-primary); font-family: 'Outfit', 'Inter', system-ui, sans-serif; }
    table { width: 100%; border-collapse: collapse; margin: 1rem 0; font-size: 0.95rem; }
    th, td { padding: 0.75rem 1rem; text-align: left; border-bottom: 1px solid #e2e8f0; }
    th { background: #f1f5f9; font-weight: 600; color: var(--up-primary); }
    tr:hover { background: #f8fafc; }
    .practice-question { padding: 1.25rem; margin-bottom: 1rem; background: #ffffff; border-radius: 12px; border: 1px solid #e2e8f0; }
    .practice-question h4 { margin-bottom: 0.75rem; color: var(--up-primary); }
    .options-grid { display: grid; gap: 0.5rem; }
    .option-item { padding: 0.75rem 1rem; background: #f8fafc; border-radius: 8px; border: 1px solid #e2e8f0; }
    .option-item.correct { background: #dcfce7; border-color: #86efac; }
    .option-item.incorrect { background: #fee2e2; border-color: #fca5a5; }
    .solution-box { margin-top: 1rem; padding: 1rem; background: #eff6ff; border-radius: 8px; border-left: 4px solid var(--up-accent); }
    .revision-card { padding: 1.25rem; background: #ffffff; border-radius: 12px; border: 1px solid #e2e8f0; margin-bottom: 1rem; }
    .revision-card h4 { color: var(--up-primary); margin-bottom: 0.75rem; }
    @media (max-width: 768px) {
      .study-tabs { flex-wrap: nowrap; overflow-x: auto; -webkit-overflow-scrolling: touch; padding: 0.4rem; scrollbar-width: none; justify-content: flex-start; }
      .study-tabs::-webkit-scrollbar { display: none; }
      .tab-btn { font-size: 0.85rem; padding: 0.5rem 0.9rem; }
      .topic-container { padding: 0 1rem 2rem; }
      .topic-header { padding: 1.5rem 1rem; }
    }
  </style>
</head>
<body>
  <div class="topic-container">
    <div class="breadcrumbs">
      <div class="breadcrumbs-path">
        <a href="/">Home</a> <i class="fas fa-chevron-right"></i>
        <a href="/upsssc-pet/">UPSSSC PET</a> <i class="fas fa-chevron-right"></i>
        <a href="/upsssc-pet/general-awareness/">General Awareness</a> <i class="fas fa-chevron-right"></i>
        <span><span class="lang-en">${meta.name}</span><span class="lang-hi">${meta.hindiName}</span></span>
      </div>
    </div>
    <div class="topic-header">
      <h1><span class="lang-en">${meta.name}</span><span class="lang-hi">${meta.hindiName}</span></h1>
      <p class="topic-desc"><span class="lang-en">${meta.description}</span><span class="lang-hi">${meta.hindiDescription}</span></p>
      <div class="topic-meta-bar">
        <span class="topic-difficulty"><i class="fas fa-signal"></i> <span class="lang-en">Medium</span><span class="lang-hi">मध्यम</span></span>
        <span class="topic-study-time"><i class="fas fa-clock"></i> <span class="lang-en">65 min total</span><span class="lang-hi">कुल 65 मिनट</span></span>
        <div class="lang-toggle">
          <button id="langEn" class="active" aria-pressed="true">EN</button>
          <button id="langHi" aria-pressed="false">हिन्दी</button>
        </div>
      </div>
    </div>
    <div class="study-tabs" role="tablist" aria-label="Topic resources">
      <button class="tab-btn active" data-tab="tab-concepts" role="tab" aria-selected="true">
        <i class="fas fa-book-open"></i> <span class="lang-en">1. Concepts & Theories</span><span class="lang-hi">1. अवधारणाएँ एवं सिद्धांत</span>
      </button>
      <button class="tab-btn" data-tab="tab-practice" role="tab" aria-selected="false">
        <i class="fas fa-list-check"></i> <span class="lang-en">2. Practice Questions</span><span class="lang-hi">2. अभ्यास प्रश्न</span>
      </button>
      <button class="tab-btn" data-tab="tab-revision" role="tab" aria-selected="false">
        <i class="fas fa-rotate"></i> <span class="lang-en">3. Revision</span><span class="lang-hi">3. पुनरावृत्ति</span>
      </button>
    </div>
    <div class="topic-content" id="topic-content"></div>
  </div>
  <script id="upsc-page-data" type="application/json">
  ${JSON.stringify({
    topicId: meta.topicId,
    topicName: meta.name,
    hindiName: meta.hindiName,
    subject: meta.subject,
    subjectDir: meta.subjectDir,
    concepts: data.concepts || null,
    practice: data.practice || null,
    revision: data.revision || null,
    version: { generator: 'v1', prompt: '1.0', translator: '1.0', normalizer: '1.0' },
    contentHash: 'sha256-placeholder',
    generatedAt: now
  }, null, 2)}
  </script>
  <script src="/assets/js/upsc-renderer.min.js" defer></script>
  <script src="/assets/js/main.min.js?v=10f0770d" defer data-cfasync="false"></script>
  <script>
    (function () {
      const btnEn = document.getElementById('langEn');
      const btnHi = document.getElementById('langHi');
      const apply = (lang) => {
        document.documentElement.classList.toggle('lang-hi', lang === 'hi');
        document.documentElement.classList.toggle('lang-en', lang !== 'hi');
        document.body.classList.toggle('lang-hi', lang === 'hi');
        document.body.classList.toggle('lang-en', lang !== 'hi');
        if (btnEn) btnEn.classList.toggle('active', lang !== 'hi');
        if (btnHi) btnHi.classList.toggle('active', lang === 'hi');
        if (btnEn) btnEn.setAttribute('aria-pressed', String(lang !== 'hi'));
        if (btnHi) btnHi.setAttribute('aria-pressed', String(lang === 'hi'));
        try { localStorage.setItem('sj_pref_lang', lang); } catch (e) { }
      };
      document.addEventListener('DOMContentLoaded', () => {
        const pref = (localStorage.getItem('sj_pref_lang') || 'en');
        apply(pref);
        if (btnEn) btnEn.addEventListener('click', () => apply('en'));
        if (btnHi) btnHi.addEventListener('click', () => apply('hi'));
      });
    })();
  </script>
</body>
</html>`;
}

async function main() {
  console.log('╔══════════════════════════════════════════════════════════╗');
  console.log('║ UPSSSC PET General Awareness Microtopic Generator        ║');
  console.log('╚══════════════════════════════════════════════════════════╝\n');

  const tabs = ['concepts'];

  for (let i = 0; i < TOPICS.length; i++) {
    const topic = TOPICS[i];
    console.log(`\n========================================================================`);
    console.log(`[${i + 1}/${TOPICS.length}] Processing: ${topic.name}`);
    console.log(`========================================================================`);

    const meta = buildMeta(topic);
    const translation = await translateMetadata(topic.name, topic.description);
    meta.hindiName = translation.hindiName;
    meta.hindiDescription = translation.hindiDescription;

    const outputDir = path.join(process.cwd(), 'upsssc-pet', 'general-awareness', topic.dir);
    fs.mkdirSync(outputDir, { recursive: true });

    const tabData = {};
    for (const tabName of tabs) {
      try {
        console.log(`  [${tabName}] Generating content...`);
        const prompt = generatePrompt(tabName, meta);
        const raw = await callGemini(prompt);
        const parsed = parseResponse(raw);
        tabData[tabName] = cleanUndefined(parsed);
        console.log(`  [${tabName}] Done`);
      } catch (err) {
        console.error(`  [${tabName}] Failed: ${err.message}`);
        tabData[tabName] = null;
      }
      await sleep(13000); // 13-second delay between tab generations as requested
    }

    tabData.practice = null;
    tabData.revision = null;

    // Fallback: if concepts failed, provide minimal structure to prevent renderer crash
    if (!tabData.concepts || !tabData.concepts.sections) {
      tabData.concepts = {
        sections: [
          {
            title: "Content Under Preparation",
            type: "table",
            headers: ["Topic", "Status"],
            rows: [
              [meta.name, "Check back soon for comprehensive notes"]
            ]
          }
        ],
        keyTakeaways: ["Content being generated"]
      };
    }

    const html = assemblePage(meta, tabData);
    fs.writeFileSync(path.join(outputDir, 'index.html'), html, 'utf8');
    fs.writeFileSync(path.join(outputDir, 'data.json'), JSON.stringify(tabData, null, 2), 'utf8');

    console.log(`\n🎉 Completed: ${meta.name}`);

    // Delay between topics to avoid rate limiting
    if (i < TOPICS.length - 1) {
      await sleep(13000); // 13-second delay between topics as requested
    }
  }

  console.log('\nAll General Awareness microtopics generated successfully!');
}

main().catch(err => {
  console.error('Fatal error:', err);
  process.exit(1);
});