const fs = require('fs');
const path = require('path');
require('dotenv').config();
const { GoogleGenAI } = require('@google/genai');

const apiKey = process.env.GEMINI_API_KEY;
if (!apiKey) {
    console.error("Error: GEMINI_API_KEY is not set in .env file.");
    process.exit(1);
}

const ai = new GoogleGenAI({ apiKey });

// Helper to get today's date in YYYY-MM-DD IST format
function getTodayIST() {
    const date = new Date();
    const tzOffset = 5.5 * 60 * 60 * 1000;
    const istTime = date.getTime() + date.getTimezoneOffset() * 60000 + tzOffset;
    const istDate = new Date(istTime);
    const yyyy = istDate.getFullYear();
    const mm = String(istDate.getMonth() + 1).padStart(2, '0');
    const dd = String(istDate.getDate()).padStart(2, '0');
    return `${yyyy}-${mm}-${dd}`;
}

async function main() {
    const args = process.argv.slice(2);
    const targetDate = args[0] || getTodayIST();

    if (!/^\d{4}-\d{2}-\d{2}$/.test(targetDate)) {
        console.error("Error: Date must be in YYYY-MM-DD format.");
        process.exit(1);
    }

    console.log(`🔍 Querying Gemini with Search Grounding for current affairs on: ${targetDate}...`);
    
    const prompt = `
Search the web for the most detailed, high-yield Indian and International Current Affairs for the date ${targetDate}.
Focus on educational portals used for competitive exams (such as Adda247, Physics Wallah (PW), Drishti IAS, GKToday, and PIB).
Extract the key news events for this date and structure the data strictly in the JSON format matching the schema below.

JSON Schema:
{
  "news": [
    {
      "title_en": "Headline in English",
      "title_hi": "Headline in Hindi (translated accurately)",
      "desc_en": "Detailed analysis/description in English",
      "desc_hi": "Detailed analysis/description in Hindi",
      "category_en": "Category in English (e.g. Economy, Polity, Environment, Science & Tech, International Relations, National, Defence)",
      "category_hi": "Category in Hindi",
      "source": "Source name (e.g. PW, Adda247, PIB, etc.)",
      "exams": ["UPSC", "SSC CGL", "Railway", "RO/ARO"]
    }
  ],
  "oneliners": {
    "en": [
      "One-liner summary 1 in English",
      "One-liner summary 2 in English"
    ],
    "hi": [
      "One-liner summary 1 in Hindi",
      "One-liner summary 2 in Hindi"
    ]
  },
  "mnemonics": [
    {
      "topic_en": "Topic of mnemonic in English",
      "topic_hi": "Topic of mnemonic in Hindi",
      "hook_en": "Mnemonic phrase/acronym in English",
      "hook_hi": "Mnemonic phrase/acronym in Hindi",
      "explain_en": "Detailed explanation of mnemonic letters/parts in English",
      "explain_hi": "Detailed explanation of mnemonic letters/parts in Hindi"
    }
  ],
  "mindmapText": "A valid Mermaid.js mindmap diagram starting with 'mindmap' syntax describing the day's connections.",
  "mcqs": [
    {
      "question": "Question text in English (or bilingual if appropriate)",
      "options": ["Option A", "Option B", "Option C", "Option D"],
      "correctAnswer": 0, // index of correct option (0-3)
      "explanation": "Detailed explanation of the answer in English/Bilingual",
      "category": "category name",
      "difficulty": "medium/hard/easy"
    }
  ]
}

Ensure the output is valid JSON, and nothing else (do not wrap in markdown \`\`\`json tags, return raw JSON string).
    `;

    try {
        const response = await ai.models.generateContent({
            model: 'gemini-1.5-flash',
            contents: prompt,
            config: {
                tools: [{ googleSearch: {} }], // Enable search grounding!
                responseMimeType: 'application/json'
            }
        });

        const jsonText = response.text;
        const result = JSON.parse(jsonText);

        // Split into daily and mcqs files
        const dailyData = {
            news: result.news,
            oneliners: result.oneliners,
            mnemonics: result.mnemonics,
            mindmapText: result.mindmapText
        };

        const mcqData = result.mcqs;

        const dataDir = path.resolve(__dirname, '../current-affairs/data');
        const mcqDir = path.join(dataDir, 'mcqs');

        if (!fs.existsSync(dataDir)) fs.mkdirSync(dataDir, { recursive: true });
        if (!fs.existsSync(mcqDir)) fs.mkdirSync(mcqDir, { recursive: true });

        const dailyPath = path.join(dataDir, `daily-${targetDate}.json`);
        const mcqPath = path.join(mcqDir, `${targetDate}.json`);

        fs.writeFileSync(dailyPath, JSON.stringify(dailyData, null, 2), 'utf8');
        fs.writeFileSync(mcqPath, JSON.stringify(mcqData, null, 2), 'utf8');

        console.log(`🎉 Ingestion and generation successful!`);
        console.log(`💾 Daily updates saved to: ${dailyPath}`);
        console.log(`💾 Quizzes saved to: ${mcqPath}`);

    } catch (err) {
        console.error("❌ Generation failed:", err.message);
        process.exit(1);
    }
}

main();
