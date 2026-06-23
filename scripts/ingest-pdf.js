const fs = require('fs');
const path = require('path');
const pdf = require('pdf-parse');
require('dotenv').config();
const { GoogleGenAI } = require('@google/genai');

const apiKey = process.env.GEMINI_API_KEY;
if (!apiKey) {
    console.error("Error: GEMINI_API_KEY is not set in .env file.");
    process.exit(1);
}

const ai = new GoogleGenAI({ apiKey });

async function main() {
    const args = process.argv.slice(2);
    if (args.length < 2) {
        console.log("Usage: node scripts/ingest-pdf.js <path-to-pdf> <date-YYYY-MM-DD>");
        process.exit(1);
    }

    const pdfPath = path.resolve(args[0]);
    const targetDate = args[1];

    if (!/^\d{4}-\d{2}-\d{2}$/.test(targetDate)) {
        console.error("Error: Date must be in YYYY-MM-DD format.");
        process.exit(1);
    }

    if (!fs.existsSync(pdfPath)) {
        console.error(`Error: File not found at ${pdfPath}`);
        process.exit(1);
    }

    console.log(`📖 Reading PDF file: ${pdfPath}...`);
    const dataBuffer = fs.readFileSync(pdfPath);
    
    try {
        const pdfData = await pdf(dataBuffer);
        const text = pdfData.text;
        console.log(`✅ Extracted ${text.length} characters of text from PDF.`);
        
        console.log(`🤖 Invoking Gemini API to process and format current affairs...`);
        const prompt = `
You are an expert educational content writer preparing Current Affairs for UPSC and SSC competitive exams in India.
Below is the raw extracted text from a daily current affairs PDF (from Physics Wallah / Adda247).
Please read this text, filter out any advertisements or non-relevant items, and extract the high-yield news events for the date ${targetDate}.

Please return the extracted information strictly in JSON format matching the schema below.

JSON Schema:
{
  "news": [
    {
      "title_en": "Headline in English",
      "title_hi": "Headline in Hindi",
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

Raw PDF Text:
${text}
        `;

        const response = await ai.models.generateContent({
            model: 'gemini-1.5-flash',
            contents: prompt,
            config: {
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

        console.log(`🎉 Ingestion successful!`);
        console.log(`💾 Daily updates saved to: ${dailyPath}`);
        console.log(`💾 Quizzes saved to: ${mcqPath}`);

    } catch (err) {
        console.error("❌ Ingestion failed:", err.message);
        process.exit(1);
    }
}

main();
