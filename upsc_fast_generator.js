import fs from 'fs';
import path from 'path';
import { assemblePage, createManifest } from './upsc/upsc-microtopic-template.js';

let apiKey = process.env.GEMINI_API_KEY;
if (!apiKey && fs.existsSync('.env')) {
  const envContent = fs.readFileSync('.env', 'utf8');
  for (const line of envContent.split('\n')) {
    if (line.startsWith('GEMINI_API_KEY=')) apiKey = line.split('=')[1].trim();
  }
}

if (!apiKey) {
  console.error('❌ GEMINI_API_KEY is not set.');
  process.exit(1);
}

const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

function kebabToTitle(kebab) {
  return kebab.split('-').map(w => w.charAt(0).toUpperCase() + w.slice(1)).join(' ');
}

function parseSafeJson(raw) {
  let cleaned = raw.trim();
  if (cleaned.startsWith('```json')) cleaned = cleaned.replace(/^```json/, '');
  if (cleaned.startsWith('```')) cleaned = cleaned.replace(/^```/, '');
  if (cleaned.endsWith('```')) cleaned = cleaned.replace(/```$/, '');
  cleaned = cleaned.trim();
  return JSON.parse(cleaned);
}

async function generateSingleCall(topicName, parentName, subject) {
  const prompt = `You are India's foremost UPSC Civil Services faculty and subject matter expert. 
Generate a comprehensive, exhaustive, and 360-degree concepts & theory study note for the UPSC microtopic: "${topicName}".
Subject: ${subject} | Parent Module: ${parentName}

CRITICAL UPSC EXAM-COVERAGE REQUIREMENT:
Ensure COMPLETE coverage of "${topicName}" so that ANY question asked in UPSC Prelims or Mains can be directly solved.

STRICT CONTENT RULES:
1. ONLY English language strings.
2. NO fluffy descriptive prose. Sharp, high-density bullet points, comparative tables, definitions, and subcards.
3. Include relevant dates, acts, articles, committees, classifications, and scientific mechanisms.
4. Include high-yield MNEMONICS & memory tricks for Prelims.
5. Highlight EXAMINER TRAPS (common confusion points in Prelims MCQs).
6. Return ONLY valid JSON matching this schema:

{
  "overview": {
    "title": "${topicName}",
    "definition": "Precise, academic 1-2 sentence core definition and scope.",
    "importanceInUpsc": "Why this microtopic is tested in UPSC CSE.",
    "learningOutcomes": [
      "Master foundational concepts and mechanisms of ${topicName}.",
      "Evaluate spatial distribution, institutional frameworks, and policy dimensions.",
      "Apply high-yield mnemonics to solve tricky Prelims and Mains questions."
    ],
    "prerequisites": ["Core foundational concepts"],
    "estimatedReadingTime": 15
  },
  "concepts": {
    "sections": [
      {
        "title": "Core Foundations & Conceptual Framework",
        "type": "paragraph",
        "content": "• **Foundational Principle 1**: Direct factual/conceptual point with key terminology in **bold**.\\n• **Foundational Principle 2**: Direct factual/conceptual point with key terminology in **bold**.\\n• **Foundational Principle 3**: Direct factual/conceptual point with key terminology in **bold**.\\n• **Key Metric / Factor**: Specific quantitative or analytical dimension."
      },
      {
        "title": "Comprehensive Classification & Comparative Matrix",
        "type": "table",
        "headers": ["Classification / Type / Component", "Key Characteristics & Locations", "Governing Factors / Mechanism", "UPSC Exam Significance"],
        "rows": [
          ["Category A", "Full specific details and features", "Underlying causes / drivers", "Specific Prelims / Mains angle"],
          ["Category B", "Full specific details and features", "Underlying causes / drivers", "Specific Prelims / Mains angle"]
        ]
      },
      {
        "title": "Key Terminology, Institutions & Mechanisms",
        "type": "list",
        "items": [
          {
            "term": "Key Concept / Technical Term 1",
            "definition": "Exhaustive explanation with its practical and exam context."
          },
          {
            "term": "Key Concept / Technical Term 2",
            "definition": "Exhaustive explanation with its practical and exam context."
          }
        ]
      },
      {
        "title": "Multi-Dimensional Sub-concepts & Applications",
        "type": "subcards",
        "items": [
          {
            "title": "Major Applications / Initiatives",
            "content": "• **Key Application 1**: Core technical mechanism.\\n• **Key Application 2**: Real-world deployment or mission."
          },
          {
            "title": "Challenges & Way Forward",
            "content": "• **Key Challenges**: Technical or policy bottlenecks.\\n• **Solutions**: Next-generation solutions."
          }
        ]
      },
      {
        "title": "High-Yield Memory Hacks & Mnemonics",
        "type": "subcards",
        "items": [
          {
            "title": "Mnemonic for Retention",
            "content": "• **Memory Acronym / Phrase**: Punchy mnemonic formula.\\n• **Decoded Meaning**: Step-by-step breakdown."
          }
        ]
      }
    ],
    "upscNotes": [
      {
        "type": "trap",
        "content": "Examiner Trap: Specific misleading statement frequently tested in UPSC."
      },
      {
        "type": "tip",
        "content": "Mains Value Addition: High-impact analytical keywords or quotes."
      }
    ],
    "keyTakeaways": [
      "Crucial summary takeaway 1.",
      "Crucial summary takeaway 2.",
      "Crucial summary takeaway 3."
    ]
  }
}`;

  const url = `https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-lite:generateContent?key=${apiKey}`;
  const payload = {
    contents: [{ parts: [{ text: prompt }] }],
    generationConfig: { responseMimeType: 'application/json', temperature: 0.1 }
  };

  const controller = new AbortController();
  const timeoutId = setTimeout(() => controller.abort(), 25000);

  try {
    const res = await fetch(url, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload),
      signal: controller.signal
    });

    clearTimeout(timeoutId);

    if (!res.ok) {
      const errText = await res.text();
      throw new Error(`HTTP ${res.status}: ${errText}`);
    }

    const data = await res.json();
    const rawText = data.candidates[0].content.parts[0].text.trim();
    return parseSafeJson(rawText);
  } finally {
    clearTimeout(timeoutId);
  }
}

const baseDir = path.join(process.cwd(), 'upsc');
const subjects = [
  'science-and-tech',
  'modern-history',
  'medieval-history',
  'ancient-history',
  'environment',
  'csat'
];

async function run() {
  const limitArg = process.argv.find(a => a.startsWith('--limit='));
  const limit = limitArg ? parseInt(limitArg.split('=')[1]) : 500;
  const targetSubjArg = process.argv.find(a => a.startsWith('--subject='));
  const targetSubj = targetSubjArg ? targetSubjArg.split('=')[1] : null;

  console.log('🚀 Starting Single-Call Fast Concept Generator (gemini-3.1-flash-lite)...');
  console.log(`⏱️ Rate Limit: 6.0s delay between calls. Hard Stop Limit: ${limit} calls\n`);

  let processed = 0;

  for (const s of subjects) {
    if (targetSubj && s !== targetSubj) continue;
    const sPath = path.join(baseDir, s);
    if (!fs.existsSync(sPath)) continue;

    const parents = fs.readdirSync(sPath).filter(d => fs.statSync(path.join(sPath, d)).isDirectory());

    for (const p of parents) {
      const pPath = path.join(sPath, p);
      const microtopics = fs.readdirSync(pPath).filter(d => fs.statSync(path.join(pPath, d)).isDirectory());

      for (let i = 0; i < microtopics.length; i++) {
        if (processed >= limit) {
          console.log(`\n🛑 Reached hard stop limit of ${limit} calls. Exiting.`);
          return;
        }

        const m = microtopics[i];
        const mPath = path.join(pPath, m);
        const idxPath = path.join(mPath, 'index.html');

        if (!fs.existsSync(idxPath)) continue;

        const html = fs.readFileSync(idxPath, 'utf8');
        const isStub = html.includes('competitive-exam-guide.min.js') && !html.includes('id="embedded-study-guide-data"');

        const conceptsJsonPath = path.join(mPath, 'tabs', 'concepts.json');
        let hasDuplicateHi = false;
        if (fs.existsSync(conceptsJsonPath)) {
          const rawC = fs.readFileSync(conceptsJsonPath, 'utf8');
          if (rawC.includes('"hi": "') && !/[\u0900-\u097F]/.test(rawC)) {
            hasDuplicateHi = true;
          }
        }

        if (!isStub && !hasDuplicateHi) continue;

        const topicName = kebabToTitle(m);
        const parentName = kebabToTitle(p);
        const prevDir = i > 0 ? microtopics[i - 1] : null;
        const nextDir = i < microtopics.length - 1 ? microtopics[i + 1] : null;

        console.log(`[#${processed + 1}] Processing: [${s}] ${parentName} -> ${topicName}`);

        try {
          const pureEnglishData = await generateSingleCall(topicName, parentName, kebabToTitle(s));

          const meta = {
            name: topicName,
            hindiName: topicName,
            description: `Study guide for ${topicName} under ${parentName} for UPSC Civil Services Preparation.`,
            hindiDescription: `Study guide for ${topicName} under ${parentName} for UPSC Civil Services Preparation.`,
            canonicalUrl: `https://sjmaths.com/upsc/${s}/${p}/${m}/`,
            subject: kebabToTitle(s),
            subjectDir: s,
            parentTopic: parentName,
            parentDir: p,
            dir: m,
            topicId: `${s}.${p}.${m}`,
            category: 'GS-1',
            difficulty: 'medium',
            studyTime: { concepts: 20, practice: 15, revision: 10 },
            learningObjectives: pureEnglishData.overview?.learningOutcomes || [`Master ${topicName}`],
            previousTopic: prevDir ? kebabToTitle(prevDir) : '',
            previousDir: prevDir || '',
            nextTopic: nextDir ? kebabToTitle(nextDir) : '',
            nextDir: nextDir || '',
            supportsMains: true
          };

          const fullHtml = assemblePage(meta, pureEnglishData, { overall: 95 });
          fs.writeFileSync(idxPath, fullHtml, 'utf8');

          const tabsDir = path.join(mPath, 'tabs');
          fs.mkdirSync(tabsDir, { recursive: true });
          fs.writeFileSync(path.join(tabsDir, 'overview.json'), JSON.stringify(pureEnglishData.overview, null, 2), 'utf8');
          fs.writeFileSync(path.join(tabsDir, 'concepts.json'), JSON.stringify(pureEnglishData.concepts, null, 2), 'utf8');

          fs.writeFileSync(path.join(mPath, 'page.manifest.json'), JSON.stringify(createManifest(meta, {
            overview: { score: { overall: 95 } },
            concepts: { score: { overall: 95 } }
          }), null, 2), 'utf8');

          processed++;
          console.log(`✅ [#${processed}/${limit}] Completed: ${topicName}`);

          await sleep(6000);
        } catch (err) {
          console.error(`❌ Error on ${topicName}:`, err.message);
          if (err.message.includes('429')) {
            console.log('⚠️ Rate limit hit. Backing off for 15s...');
            await sleep(15000);
          } else {
            await sleep(6000);
          }
        }
      }
    }
  }

  console.log(`\n🎉 Finished generating ${processed} topics.`);
}

run().catch(console.error);
