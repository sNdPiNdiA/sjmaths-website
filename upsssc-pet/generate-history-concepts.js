import fs from 'fs';
import path from 'path';

// ============================================================================
// ENV LOADER
// ============================================================================
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
  console.error('GEMINI_API_KEY is not set. Please add it to .env file.');
  process.exit(1);
}

// ============================================================================
// CONSTANTS
// ============================================================================
const GEMINI_API = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent';
const REQUEST_DELAY_MS = 20000; // 20s between API calls to avoid rate limiting
const MAX_RETRIES = 5;

// ============================================================================
// UPSSSC PET HISTORY TOPICS (18 topics from syllabus)
// ============================================================================
const HISTORY_TOPICS = [
  {
    dir: 'indus-valley-civilization',
    name: 'Indus Valley Civilization',
    hindiName: 'सिन्धु घाटी की सभ्यता',
    description: 'Complete UPSSSC PET guide on Indus Valley Civilization: major sites, town planning, economy, religion, art, seals, script, and decline theories.',
    keywords: ['Indus Valley', 'Harappa', 'Mohenjo-daro', 'Dholavira', 'Lothal', 'town planning', 'seals', 'script']
  },
  {
    dir: 'vedic-culture',
    name: 'Vedic Culture',
    hindiName: 'वैदिक संस्कृति',
    description: 'Complete UPSSSC PET guide on Vedic Culture: Rig Vedic and Later Vedic periods, society, polity, economy, religion, and important texts.',
    keywords: ['Vedic', 'Rig Veda', 'Samaveda', 'Yajurveda', 'Atharvaveda', 'Brahmanas', 'Upanishads', 'Aryans']
  },
  {
    dir: 'buddhism-gautam-buddha',
    name: 'Buddhism & Gautam Buddha',
    hindiName: 'बौद्ध धर्म: गौतम बुद्ध',
    description: 'Complete UPSSSC PET guide on Buddhism: life of Gautam Buddha, Four Noble Truths, Eightfold Path, Buddhist councils, and spread of Buddhism.',
    keywords: ['Buddha', 'Buddhism', 'Four Noble Truths', 'Eightfold Path', 'Sangha', 'Tripitaka', 'Bodh Gaya', 'Sarnath']
  },
  {
    dir: 'jainism-mahavira',
    name: 'Jainism & Mahavira',
    hindiName: 'जैन धर्म: महावीर',
    description: 'Complete UPSSSC PET guide on Jainism: life of Mahavira, Tirthankaras, Jain philosophy, principles, sects, and spread of Jainism.',
    keywords: ['Jainism', 'Mahavira', 'Tirthankara', 'Ahimsa', 'Anekantavada', 'Digambara', 'Svetambara', 'Rishabhanatha']
  },
  {
    dir: 'maurya-dynasty-ashoka',
    name: 'Maurya Dynasty & Ashoka',
    hindiName: 'मौर्य वंश: सम्राट अशोक',
    description: 'Complete UPSSSC PET guide on Maurya Dynasty: Chandragupta, Bindusara, Ashoka, administration, Kautilya Arthashastra, and Ashokan edicts.',
    keywords: ['Maurya', 'Chandragupta', 'Ashoka', 'Kautilya', 'Arthashastra', 'Dhamma', 'Kalinga War', 'edicts']
  },
  {
    dir: 'gupta-dynasty',
    name: 'Gupta Dynasty',
    hindiName: 'गुप्त वंश',
    description: 'Complete UPSSSC PET guide on Gupta Dynasty: Chandragupta I, Samudragupta, Chandragupta II, Golden Age, art, science, and literature.',
    keywords: ['Gupta', 'Samudragupta', 'Chandragupta II', 'Golden Age', 'Aryabhata', 'Kalidas', 'Nalanda', 'Allahabad Pillar']
  },
  {
    dir: 'harshavardhana',
    name: 'Harshavardhana',
    hindiName: 'हर्षवर्द्धन',
    description: 'Complete UPSSSC PET guide on Harshavardhana: rise to power, administration, religion, Hiuen Tsang, Nalanda, and cultural contributions.',
    keywords: ['Harshavardhana', 'Hiuen Tsang', 'Nalanda', 'Kannauj', 'Pushyabhuti', 'Harshacharita', 'Banabhatta', 'Prayag']
  },
  {
    dir: 'rajput-period',
    name: 'Rajput Period',
    hindiName: 'राजपूत काल',
    description: 'Complete UPSSSC PET guide on Rajput Period: major Rajput dynasties, battles, administration, art, architecture, and causes of decline.',
    keywords: ['Rajput', 'Prithviraj Chauhan', 'Rana Pratap', 'Mewar', 'Chauhans', 'Rajputs', 'Tarain', 'Rajputana']
  },
  {
    dir: 'sultanate-period',
    name: 'Sultanate Period',
    hindiName: 'सल्तनत काल',
    description: 'Complete UPSSSC PET guide on Delhi Sultanate: Slave, Khilji, Tughlaq, Sayyid, Lodi dynasties, administration, reforms, and architecture.',
    keywords: ['Delhi Sultanate', 'Slave Dynasty', 'Khilji', 'Tughlaq', 'Sayyid', 'Lodi', 'Qutub Minar', 'Alauddin Khilji']
  },
  {
    dir: 'mughal-empire',
    name: 'Mughal Empire',
    hindiName: 'मुगल साम्राज्य',
    description: 'Complete UPSSSC PET guide on Mughal Empire: Babur to Aurangzeb, Mansabdari system, administration, art, architecture, and decline.',
    keywords: ['Mughal', 'Babur', 'Akbar', 'Aurangzeb', 'Mansabdari', 'Taj Mahal', 'Din-i-Ilahi', 'Battle of Panipat']
  },
  {
    dir: 'maratha',
    name: 'Maratha Empire',
    hindiName: 'मराठा',
    description: 'Complete UPSSSC PET guide on Maratha Empire: Shivaji, Peshwas, administration, military, and Anglo-Maratha wars.',
    keywords: ['Maratha', 'Shivaji', 'Peshwa', 'Bajirao', 'Chhatrapati', 'Anglo-Maratha', 'Swaraj', 'Ashtapradhan']
  },
  {
    dir: 'rise-of-british-rule-first-war-of-independence',
    name: 'Rise of British Rule & First War of Independence',
    hindiName: 'ब्रिटिश राज का अभ्युदय एवं प्रथम स्वतंत्रता संग्राम',
    description: 'Complete UPSSSC PET guide on British expansion and 1857 Revolt: Carnatic wars, Battle of Plassey, Subsidiary Alliance, Doctrine of Lapse, and Revolt of 1857.',
    keywords: ['British Rule', '1857 Revolt', 'Battle of Plassey', 'Subsidiary Alliance', 'Doctrine of Lapse', 'East India Company', 'Mangal Pandey', 'Rani Lakshmibai']
  },
  {
    dir: 'socio-economic-impact-of-british-rule',
    name: 'Socio-Economic Impact of British Rule',
    hindiName: 'ब्रिटिश राज का सामाजिक-आर्थिक प्रभाव',
    description: 'Complete UPSSSC PET guide on British socio-economic impact: land revenue systems, deindustrialization, drain of wealth, social reforms, and education.',
    keywords: ['British Impact', 'Permanent Settlement', 'Ryotwari', 'Mahalwari', 'Drain of Wealth', 'Deindustrialization', 'Social Reforms', 'Education']
  },
  {
    dir: 'early-years-of-freedom-movement',
    name: 'Early Years of Freedom Movement',
    hindiName: 'स्वाधीनता आन्दोलन के प्रारम्भिक वर्ष',
    description: 'Complete UPSSSC PET guide on early freedom movement: INC formation, Moderates, Extremists, Bengal Partition, Swadeshi movement, and Surat Split.',
    keywords: ['Freedom Movement', 'INC', 'Moderates', 'Extremists', 'Bengal Partition', 'Swadeshi', 'Surat Split', 'Bal Gangadhar Tilak']
  },
  {
    dir: 'swadeshi-civil-disobedience-gandhi',
    name: 'Swadeshi & Civil Disobedience Movement (Gandhi)',
    hindiName: 'स्वदेशी तथा सविनय अवज्ञा आंदोलन: महात्मा गांधी',
    description: 'Complete UPSSSC PET guide on Gandhian movements: Non-Cooperation, Civil Disobedience, Salt Satyagraha, Dandi March, and Round Table Conferences.',
    keywords: ['Gandhi', 'Swadeshi', 'Civil Disobedience', 'Salt Satyagraha', 'Dandi March', 'Non-Cooperation', 'Round Table', 'Satyagraha']
  },
  {
    dir: 'revolutionary-movement-aggressive-nationalism',
    name: 'Revolutionary Movement & Aggressive Nationalism',
    hindiName: 'क्रांतिकारी आंदोलन तथा उग्र राष्ट्रवाद',
    description: 'Complete UPSSSC PET guide on revolutionary movements: revolutionary organizations, Bhagat Singh, Chandrashekhar Azad, and aggressive nationalism.',
    keywords: ['Revolutionary', 'Bhagat Singh', 'Chandrashekhar Azad', 'Hindustan Republican', 'Kakori', 'Lala Lajpat Rai', 'Aggressive Nationalism', 'Revolution']
  },
  {
    dir: 'legislative-amendments-british-india-act-1935',
    name: 'Legislative Amendments & British India Act 1935',
    hindiName: 'विधायी संशोधन तथा ब्रिटिश इंडिया एक्ट, 1935',
    description: 'Complete UPSSSC PET guide on constitutional developments: Government of India Acts, Morley-Minto, Montagu-Chelmsford, and Act of 1935.',
    keywords: ['Government of India Act', '1935 Act', 'Morley-Minto', 'Montagu-Chelmsford', 'Dyarchy', 'Provincial Autonomy', 'Legislative', 'Constitutional']
  },
  {
    dir: 'quit-india-ina-netaji-subhash',
    name: 'Quit India Movement, INA & Netaji Subhash',
    hindiName: 'भारत छोड़ो आंदोलन, आजाद हिंद फौज तथा नेताजी सुभाष',
    description: 'Complete UPSSSC PET guide on Quit India Movement, Indian National Army, and Netaji Subhash Chandra Bose.',
    keywords: ['Quit India', 'INA', 'Netaji', 'Subhash Chandra Bose', 'Azad Hind Fauj', 'Cripps Mission', 'August Kranti', 'Singapore']
  }
];

// ============================================================================
// UTILITY FUNCTIONS
// ============================================================================
function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

function kebabToTitle(kebab) {
  return kebab.split('-').map(word => {
    const up = word.toUpperCase();
    const acronyms = ['INA', 'INC', 'PET', 'UPSSSC', 'ACT', 'BRITISH', 'INDIA'];
    if (acronyms.includes(up)) return up;
    return word.charAt(0).toUpperCase() + word.slice(1);
  }).join(' ');
}

function slugify(text) {
  return text.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-+|-+$/g, '');
}

// ============================================================================
// GEMINI API CLIENT
// ============================================================================
async function callGemini(prompt, retries = MAX_RETRIES) {
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
          generationConfig: {
            temperature: 0.1,
            maxOutputTokens: 65536,
            topP: 0.95,
          },
        }),
      });

      if (res.status === 429) {
        const wait = REQUEST_DELAY_MS;
        console.log(`  ⏳ Rate limited (429). Waiting ${wait / 1000}s before retry ${attempt}/${retries}...`);
        await sleep(wait);
        continue;
      }

      if (!res.ok) {
        const errBody = await res.text();
        throw new Error(`Gemini API error ${res.status}: ${errBody.substring(0, 200)}`);
      }

      const data = await res.json();
      const text = data?.candidates?.[0]?.content?.parts?.[0]?.text || '';
      if (!text || text.trim().length === 0) {
        throw new Error('Empty response from API');
      }
      return text;
    } catch (err) {
      if (attempt === retries) throw err;
      console.log(`  ⚠️ Retry ${attempt}/${retries} after error: ${err.message}`);
      await sleep(5000);
    }
  }
  throw new Error('Max retries exceeded');
}

// ============================================================================
// JSON PARSER (handles markdown code fences and common issues)
// ============================================================================
function parseResponse(raw) {
  if (!raw || typeof raw !== 'string') {
    throw new Error('Invalid response: expected string, got ' + typeof raw);
  }

  let cleaned = raw.trim();

  // Remove markdown code fences
  if (cleaned.startsWith('```json')) cleaned = cleaned.replace(/^```json\s*/, '').replace(/\s*```$/, '');
  else if (cleaned.startsWith('```')) cleaned = cleaned.replace(/^```\s*/, '').replace(/\s*```$/, '');

  // Fix smart quotes
  cleaned = cleaned.replace(/[\u2018\u2019]/g, "'").replace(/[\u201c\u201d]/g, '"');

  // Try direct parse
  try { return JSON.parse(cleaned); } catch (err) { }

  // Try extracting JSON from the response
  const jsonMatch = cleaned.match(/[\{\[][\s\S]*[\}\]]/);
  if (jsonMatch) {
    const repaired = jsonMatch[0]
      .replace(/(\{|,|\[|\s)([A-Za-z0-9_\-]+)\s*:/g, '$1"$2":')
      .replace(/'([^'\\]*(?:\\.[^'\\]*)*)'/g, '"$1"')
      .replace(/,\s*([}\]])/g, '$1');
    try { return JSON.parse(repaired); } catch (e) {
      try { return JSON.parse(Function('"use strict"; return (' + repaired + ')')()); } catch (e2) { }
    }
  }

  console.error('❌ Raw response (first 500 chars):', cleaned.substring(0, 500));
  throw new Error('No valid JSON found in response');
}

// ============================================================================
// PROMPT BUILDER — Concepts/Theories Tab (NO PARAGRAPHS)
// ============================================================================
function buildConceptsPrompt(topic) {
  return `You are an expert faculty member for UPSSSC PET (Preliminary Eligibility Test) exam preparation. Create ULTRA-COMPREHENSIVE, SEO-OPTIMIZED concept notes for the History topic: "${topic.name}" (${topic.hindiName}).

TOPIC CONTEXT:
- Subject: History (इतिहास)
- Exam: UPSSSC PET (Uttar Pradesh Subordinate Services Selection Commission - Preliminary Eligibility Test)
- Topic Directory: ${topic.dir}
- Keywords to target: ${topic.keywords.join(', ')}

CRITICAL FORMAT RULES — NO PARAGRAPHS ALLOWED:
1. **STRICTLY NO PARAGRAPHS** — Do NOT use the "paragraph" type anywhere. Every section must be a table, list, or subcards.
2. Content must be **point-wise, bulleted, tabular, and structured** for rapid exam revision.
3. Use **bold** for key terms, names, dates, and figures within table cells and list items.
4. Content must be **comprehensive and exam-focused** — cover ALL important facts, dates, names, events, and figures that UPSSSC PET asks.

REQUIRED SECTION STRUCTURE (in this exact order):

SECTION 1 — "Detailed Brief Overview" (type: "table")
- A comprehensive overview table with 8-10 rows covering: What, When, Where, Who, Why Important, Key Features, Significance for UPSSSC PET, and other essential facts.
- Headers: ["Aspect", "Key Details"]

SECTION 2 — "Detailed Explanation with Mnemonics" (type: "subcards")
- 5-7 subcards, each covering a major sub-topic or theme.
- Each subcard must have a title and detailed point-wise content (NOT paragraphs).
- Include at least 2-3 powerful mnemonics within these subcards to help memorize sequences, lists, and facts.

SECTION 3 — "Comprehensive Data Tables" (type: "table")
- 3-4 detailed tables with 8-12 rows each covering:
  a) Important Rulers/Dynasties/Personalities with their period, achievements, and significance
  b) Important Battles/Wars/Events with year, location, result, and significance
  c) Important Sites/Places/Monuments with location and significance
  d) Important Terms/Concepts with definitions and context

SECTION 4 — "Tricks to Remember" (type: "list")
- 6-8 items with "term" = trick title, "definition" = detailed trick explanation
- Include memory tricks, acronyms, association techniques, and quick recall methods

SECTION 5 — "Mistakes to Avoid" (type: "list")
- 6-8 items with "term" = common mistake, "definition" = correct fact and why students get confused
- Cover frequently confused dates, names, events, and concepts

SECTION 6 — "Point-wise Detailed Summary" (type: "list")
- 10-15 items with "term" = key point title, "definition" = concise point-wise summary
- This is the final revision summary covering ALL essential facts

ADDITIONAL REQUIREMENTS:
- "upscNotes": Include 4-6 notes with type "tip" (exam strategy) and "trap" (common traps in UPSSSC PET)
- "keyTakeaways": Include 5-8 concise, high-yield takeaways

OUTPUT FORMAT — Return ONLY valid JSON with this exact structure:
{
  "sections": [
    {
      "title": "Detailed Brief Overview",
      "type": "table",
      "headers": ["Aspect", "Key Details"],
      "rows": [
        ["Aspect 1", "**Key detail** with bold important terms"],
        ["Aspect 2", "Another **important** detail"]
      ]
    },
    {
      "title": "Detailed Explanation with Mnemonics",
      "type": "subcards",
      "items": [
        {
          "title": "Sub-topic 1 with **mnemonic**",
          "content": "• Point 1 with **bold** terms\n• Point 2 with **bold** terms\n• **Mnemonic:** Phrase to remember"
        }
      ]
    },
    {
      "title": "Comprehensive Data Tables",
      "type": "table",
      "headers": ["Column 1", "Column 2", "Column 3"],
      "rows": [
        ["Data 1", "Data 2", "Data 3"]
      ]
    },
    {
      "title": "Tricks to Remember",
      "type": "list",
      "items": [
        {
          "term": "Trick 1: Title",
          "definition": "Detailed explanation of the trick with **bold** key terms"
        }
      ]
    },
    {
      "title": "Mistakes to Avoid",
      "type": "list",
      "items": [
        {
          "term": "Mistake 1: Common error",
          "definition": "Correct fact and why students get confused"
        }
      ]
    },
    {
      "title": "Point-wise Detailed Summary",
      "type": "list",
      "items": [
        {
          "term": "Key Point 1",
          "definition": "Concise summary point with **bold** key terms"
        }
      ]
    }
  ],
  "upscNotes": [
    {
      "type": "tip",
      "content": "Exam strategy tip for UPSSSC PET"
    },
    {
      "type": "trap",
      "content": "Common trap students fall into"
    }
  ],
  "keyTakeaways": [
    "High-yield takeaway 1",
    "High-yield takeaway 2"
  ]
}

IMPORTANT:
- Use ONLY English text. Do NOT use Hindi or bilingual format.
- Every section must be comprehensive and detailed — this is for serious exam preparation.
- Include ALL important dates, years, names, and figures.
- The content must be SEO-optimized with the topic keywords naturally embedded.
- NO paragraphs anywhere — only tables, lists, and subcards.`;
}

// ============================================================================
// HTML PAGE ASSEMBLER — 4-Tab Structure
// ============================================================================
function assemblePage(topic, conceptsData) {
  const now = new Date().toISOString();
  const canonicalUrl = `https://sjmaths.com/upsssc-pet/history/${topic.dir}/`;
  const title = `${topic.name} | UPSSSC PET History | SJMaths`;
  const description = topic.description;
  const keywords = `UPSSSC PET, ${topic.name}, History, ${topic.hindiName}, ${topic.keywords.join(', ')}`;

  return `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>${title}</title>
  <meta name="description" content="${description}">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <link rel="canonical" href="${canonicalUrl}">
  <meta name="keywords" content="${keywords}">
  <meta name="author" content="SJMaths">
  <link rel="icon" type="image/png" href="/favicon.png">

  <!-- Open Graph -->
  <meta property="og:title" content="${title}">
  <meta property="og:description" content="${description}">
  <meta property="og:type" content="article">
  <meta property="og:url" content="${canonicalUrl}">
  <meta property="og:image" content="https://sjmaths.com/assets/icons/icon-512x512.png">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="${title}">
  <meta name="twitter:description" content="${description}">
  <meta name="twitter:image" content="https://sjmaths.com/assets/icons/icon-512x512.png">

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
        <a href="/upsssc-pet/history/">History</a> <i class="fas fa-chevron-right"></i>
        <span><span class="lang-en">${topic.name}</span><span class="lang-hi">${topic.hindiName}</span></span>
      </div>
    </div>
    <div class="topic-header">
      <h1><span class="lang-en">${topic.name}</span><span class="lang-hi">${topic.hindiName}</span></h1>
      <p class="topic-desc"><span class="lang-en">${topic.description}</span><span class="lang-hi">${topic.hindiName} पर UPSSSC PET की विस्तृत गाइड।</span></p>
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
      <button class="tab-btn" data-tab="tab-pyqs" role="tab" aria-selected="false">
        <i class="fas fa-history"></i> <span class="lang-en">3. PYQs</span><span class="lang-hi">3. पिछले वर्ष के प्रश्न</span>
      </button>
      <button class="tab-btn" data-tab="tab-test" role="tab" aria-selected="false">
        <i class="fas fa-stopwatch"></i> <span class="lang-en">4. Mini Test</span><span class="lang-hi">4. मिनी टेस्ट</span>
      </button>
    </div>
    <div class="topic-content" id="topic-content"></div>
  </div>
  <script id="upsc-page-data" type="application/json">
  ${JSON.stringify({
    topicId: `upsssc-pet.history.${topic.dir}`,
    topicName: topic.name,
    hindiName: topic.hindiName,
    subject: 'History',
    subjectDir: 'history',
    concepts: conceptsData || null,
    practice: null,
    pyqs: null,
    test: null,
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

// ============================================================================
// FALLBACK CONCEPTS DATA (if API fails)
// ============================================================================
function buildFallbackConcepts(topic) {
  return {
    sections: [
      {
        title: 'Detailed Brief Overview',
        type: 'table',
        headers: ['Aspect', 'Key Details'],
        rows: [
          ['Topic', `**${topic.name}** (${topic.hindiName})`],
          ['Subject', '**History** for UPSSSC PET'],
          ['Status', 'Content under preparation — check back soon for comprehensive notes']
        ]
      }
    ],
    upscNotes: [
      {
        type: 'tip',
        content: 'This topic is important for UPSSSC PET History section. Comprehensive notes are being generated.'
      }
    ],
    keyTakeaways: [
      `Study ${topic.name} thoroughly for UPSSSC PET History section`,
      'Focus on important dates, names, and events',
      'Practice with previous year questions'
    ]
  };
}

// ============================================================================
// MAIN GENERATION LOOP
// ============================================================================
async function main() {
  console.log('╔══════════════════════════════════════════════════════════════╗');
  console.log('║ UPSSSC PET History — Concepts & Theories Tab Generator      ║');
  console.log('║ Model: gemini-3.6-flash                                      ║');
  console.log('╚══════════════════════════════════════════════════════════════╝\n');

  const totalTopics = HISTORY_TOPICS.length;
  let successCount = 0;
  let failCount = 0;

  for (let i = 0; i < totalTopics; i++) {
    const topic = HISTORY_TOPICS[i];
    console.log(`\n${'='.repeat(80)}`);
    console.log(`[${i + 1}/${totalTopics}] Processing: ${topic.name} (${topic.hindiName})`);
    console.log(`${'='.repeat(80)}`);

    const outputDir = path.join(process.cwd(), 'upsssc-pet', 'history', topic.dir);
    fs.mkdirSync(outputDir, { recursive: true });

    // Create tabs directory
    const tabsDir = path.join(outputDir, 'tabs');
    fs.mkdirSync(tabsDir, { recursive: true });

    let conceptsData = null;

    try {
      console.log('  📝 Generating concepts/theories content...');
      const prompt = buildConceptsPrompt(topic);
      const raw = await callGemini(prompt);
      const parsed = parseResponse(raw);

      // Validate the parsed data has required structure
      if (!parsed.sections || !Array.isArray(parsed.sections) || parsed.sections.length === 0) {
        throw new Error('Generated content missing "sections" array');
      }

      // Ensure no paragraph type sections (user requirement)
      const paragraphSections = parsed.sections.filter(s => s.type === 'paragraph');
      if (paragraphSections.length > 0) {
        console.log('  ⚠️ Found paragraph sections — converting to list format...');
        parsed.sections = parsed.sections.map(section => {
          if (section.type === 'paragraph') {
            return {
              title: section.title,
              type: 'list',
              items: [
                {
                  term: 'Key Point',
                  definition: section.content || ''
                }
              ]
            };
          }
          return section;
        });
      }

      conceptsData = parsed;
      console.log('  ✅ Concepts content generated successfully!');

      // Save tab data as JSON
      fs.writeFileSync(
        path.join(tabsDir, 'concepts.json'),
        JSON.stringify(conceptsData, null, 2),
        'utf8'
      );
      console.log('  💾 Saved tabs/concepts.json');

      successCount++;
    } catch (err) {
      console.error(`  ❌ Failed to generate concepts: ${err.message}`);
      conceptsData = buildFallbackConcepts(topic);
      failCount++;
    }

    // Assemble and save the HTML page
    const html = assemblePage(topic, conceptsData);
    fs.writeFileSync(path.join(outputDir, 'index.html'), html, 'utf8');
    console.log('  💾 Saved index.html');

    // Save data.json for backward compatibility
    fs.writeFileSync(
      path.join(outputDir, 'data.json'),
      JSON.stringify({ concepts: conceptsData, practice: null, pyqs: null, test: null }, null, 2),
      'utf8'
    );
    console.log('  💾 Saved data.json');

    console.log(`  🎉 Completed: ${topic.name}`);

    // Delay between topics to avoid rate limiting
    if (i < totalTopics - 1) {
      console.log(`  ⏳ Waiting ${REQUEST_DELAY_MS / 1000}s before next topic...`);
      await sleep(REQUEST_DELAY_MS);
    }
  }

  console.log(`\n${'='.repeat(80)}`);
  console.log(`📊 SUMMARY: ${successCount} succeeded, ${failCount} failed out of ${totalTopics} topics`);
  console.log(`${'='.repeat(80)}`);
  console.log('\nAll UPSSSC PET History concepts/theories tabs generated successfully!');
}

main().catch(err => {
  console.error('Fatal error:', err);
  process.exit(1);
});