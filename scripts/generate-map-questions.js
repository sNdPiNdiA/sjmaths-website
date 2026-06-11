const fs = require('fs');
const path = require('path');
const { GoogleGenAI, Type } = require('@google/genai');

const baseDir = path.resolve(__dirname, '..');
const gsHistoryDir = path.join(baseDir, 'gs-question-bank', 'history', 'modern-india', 'advent-of-europeans');

// Load API key
let apiKey = process.env.GEMINI_API_KEY;
if (!apiKey) {
    const dotenvPath = path.join(baseDir, '.env');
    if (fs.existsSync(dotenvPath)) {
        const dotenvContent = fs.readFileSync(dotenvPath, 'utf8');
        const match = dotenvContent.match(/GEMINI_API_KEY\s*=\s*([^\s#]+)/);
        if (match) {
            apiKey = match[1].trim().replace(/['"]/g, '');
        }
    }
}

if (!apiKey) {
    console.error('❌ Error: GEMINI_API_KEY not found in environment or .env file.');
    process.exit(1);
}

// Set it explicitly on process.env so SDK picks it up
process.env.GEMINI_API_KEY = apiKey;

const ai = new GoogleGenAI({ apiKey });

// Helper to format topic/folder names into readable text
function formatTopicName(folderName) {
    return folderName.replace(/_/g, ' ');
}

// Find all categories and topics
function getTopicsList() {
    const list = [];
    if (!fs.existsSync(gsHistoryDir)) {
        console.error(`Base directory does not exist: ${gsHistoryDir}`);
        return list;
    }

    const categories = fs.readdirSync(gsHistoryDir).filter(name => {
        const fullPath = path.join(gsHistoryDir, name);
        return fs.statSync(fullPath).isDirectory() && /^\d+_/.test(name);
    });

    categories.forEach(cat => {
        const catPath = path.join(gsHistoryDir, cat);
        const topics = fs.readdirSync(catPath).filter(name => {
            const fullPath = path.join(catPath, name);
            return fs.statSync(fullPath).isDirectory();
        });

        topics.forEach(topic => {
            list.push({
                categoryFolder: cat,
                categoryShort: cat.replace(/^\d+_/, ''),
                categoryName: formatTopicName(cat.replace(/^\d+_/, '')),
                topicFolder: topic,
                topicName: formatTopicName(topic),
                fullPath: path.join(catPath, topic)
            });
        });
    });

    return list;
}

// Generate with retry logic for API limits
async function generateWithRetry(prompt, responseSchema, retries = 5, delay = 5000) {
    for (let i = 0; i < retries; i++) {
        try {
            const response = await ai.models.generateContent({
                model: 'gemini-2.5-flash',
                contents: prompt,
                config: {
                    responseMimeType: "application/json",
                    responseSchema: responseSchema
                }
            });
            return response.text;
        } catch (err) {
            console.error(`⚠️ Attempt ${i + 1} failed: ${err.message}`);
            if (i < retries - 1) {
                const waitTime = delay * Math.pow(2, i); // Exponential backoff
                console.log(`Waiting ${waitTime / 1000}s before next attempt...`);
                await new Promise(resolve => setTimeout(resolve, waitTime));
            } else {
                throw err;
            }
        }
    }
}

async function generateForTopic(topicInfo) {
    const targetFile = path.join(topicInfo.fullPath, 'map_based.json');
    const syllabusRef = `history/modern-india/advent-of-europeans/${topicInfo.categoryFolder}/${topicInfo.topicFolder}`;

    // Skip if already populated with real questions
    if (fs.existsSync(targetFile)) {
        try {
            const content = JSON.parse(fs.readFileSync(targetFile, 'utf8'));
            if (content.length > 0 && content[0].question) {
                const firstQ = content[0].question;
                if (!firstQ.includes('PLACEHOLDER') && firstQ.startsWith('Which of the following is NOT correctly matched?')) {
                    console.log(`⏭️  [SKIPPING] ${topicInfo.categoryName} -> ${topicInfo.topicName} (already has real questions)`);
                    return;
                }
            }
        } catch (e) {
            // Re-generate if empty or invalid JSON
        }
    }

    console.log(`\n[PROCESSING] ${topicInfo.categoryName} -> ${topicInfo.topicName}`);

    const prompt = `
    You are an expert historian and exam designer for elite civil services examinations (like UPSC Civil Services and State PCS).
    Your task is to generate exactly 3 high-quality, historically accurate, syllabus-aligned Map-Based questions under the topic: "${topicInfo.topicName}" (part of "${topicInfo.categoryName}").
    
    Format: "Eliminate the Wrong Map Fact"
    Each question must present 4 options. Each option must pair a Settlement, Port, Factory, Battle Site, Route, or Territorial Expansion related to the topic with its geographical location, coast, region, or ruling European power.
    - Exactly 3 options must be 100% historically and geographically correct.
    - Exactly 1 option must be deliberately wrong (having a plausible but incorrect detail, e.g. wrong coast, wrong European power, wrong city, wrong river bank).
    
    You must generate:
    - 1 Easy difficulty question
    - 1 Medium difficulty question
    - 1 Hard difficulty question

    Example question text:
    "Which of the following is NOT correctly matched regarding Portuguese settlements and their locations?"

    Options example:
    [
      "Goa — West coast of India (captured from Adil Shah of Bijapur)",
      "Pondicherry — Coromandel Coast (French base)",
      "Surat — Eastern coast of India (under English factory charter)",  // Incorrect (Surat is on the West coast/Gulf of Khambhat)
      "Calicut — Malabar Coast (visited by Vasco da Gama)"
    ]
    correct_index: 2
    wrong_fact: "Surat is located on the western coast of India, in Gujarat, not the eastern coast."

    Syllabus Reference: "${syllabusRef}"

    Ensure the correct_index varies across questions (do not always make it 2 or 3).
    Return the response adhering strictly to the JSON schema.
    `;

    const responseSchema = {
        type: Type.OBJECT,
        properties: {
            questions: {
                type: Type.ARRAY,
                description: "Array of exactly 3 questions (easy, medium, hard)",
                items: {
                    type: Type.OBJECT,
                    properties: {
                        id: { type: Type.STRING },
                        question: { type: Type.STRING },
                        options: { type: Type.ARRAY, items: { type: Type.STRING } },
                        correct_index: { type: Type.INTEGER },
                        wrong_fact: { type: Type.STRING },
                        explanation: { type: Type.STRING },
                        difficulty: { type: Type.STRING },
                        geo_tags: { type: Type.ARRAY, items: { type: Type.STRING } },
                        tags: { type: Type.ARRAY, items: { type: Type.STRING } },
                        exam_tags: { type: Type.ARRAY, items: { type: Type.STRING } },
                        syllabus_ref: { type: Type.STRING }
                    },
                    required: ["id", "question", "options", "correct_index", "wrong_fact", "explanation", "difficulty", "geo_tags", "tags", "exam_tags", "syllabus_ref"]
                }
            }
        },
        required: ["questions"]
    };

    try {
        const resultText = await generateWithRetry(prompt, responseSchema);
        const data = JSON.parse(resultText);

        if (data && data.questions) {
            // Adjust IDs and ensure proper format
            const cleanQs = data.questions.map((q, idx) => {
                const diff = q.difficulty || ['easy', 'medium', 'hard'][idx] || 'medium';
                return {
                    ...q,
                    id: `map-${topicInfo.categoryFolder.slice(0,2)}-${topicInfo.topicFolder.toLowerCase()}-${diff}-${idx + 1}`,
                    syllabus_ref: syllabusRef
                };
            });

            fs.writeFileSync(targetFile, JSON.stringify(cleanQs, null, 2), 'utf8');
            console.log(`✅ Success: Generated and saved map_based.json for ${topicInfo.topicFolder}`);
        }
    } catch (err) {
        console.error(`❌ Failed to generate map questions for topic ${topicInfo.topicFolder}:`, err.message);
    }
}

async function main() {
    const topics = getTopicsList();
    console.log(`Found ${topics.length} topics to process.`);

    for (let i = 0; i < topics.length; i++) {
        console.log(`\nTopic ${i + 1}/${topics.length}`);
        await generateForTopic(topics[i]);
        // Rest between requests to avoid hitting rate limits
        await new Promise(resolve => setTimeout(resolve, 2000));
    }

    console.log('\n✨ Finished generating Map-Based questions.');
}

main().catch(console.error);
