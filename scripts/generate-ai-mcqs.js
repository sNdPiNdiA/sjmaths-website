const fs = require('fs');
const path = require('path');
const { GoogleGenAI, Type } = require('@google/genai');

// Initialize the Gemini API client
// Ensure you have set your GEMINI_API_KEY environment variable
const ai = new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY });

async function generateQuestions() {
    // Define paths relative to the script location
    const dirPath = path.join(__dirname, '../ahc-ro-aro/history-of-india/pre-historic-period');
    const notesPath = path.join(dirPath, 'index.html');
    const dataPath = path.join(dirPath, 'data.json');

    console.log('Reading source files...');
    
    // Read the study notes (HTML) and strip tags to get raw text context
    const notesHtml = fs.readFileSync(notesPath, 'utf8');
    const notesMatch = notesHtml.match(/<div id="notes-container"[^>]*>([\s\S]*?)<\/div>\s*<\/div>\s*<div class="mt-tab-content"/);
    const notesText = notesMatch ? notesMatch[1].replace(/<[^>]*>?/gm, ' ').replace(/\s+/g, ' ') : '';

    // Read the existing JSON data
    const existingData = JSON.parse(fs.readFileSync(dataPath, 'utf8'));
    const existingQuestions = [...existingData.practice, ...existingData.mock].map(q => q.q);

    const prompt = `
    You are an expert history teacher preparing questions for the Allahabad High Court RO/ARO competitive exam.
    Based on the provided study notes about Pre-Historic India, generate exactly 35 practice MCQs and 12 mock test MCQs.
    
    Guidelines:
    - Focus heavily on UP-specific archaeological sites, timelines, discoverers, and key features of different Stone Age phases.
    - Ensure distractors (wrong options) are plausible.
    - Do NOT duplicate any of these existing questions:
    ${JSON.stringify(existingQuestions, null, 2)}

    Study Notes Context:
    ${notesText}
    `;

    console.log('Calling Gemini API (gemini-2.5-flash) to generate 47 questions. This may take a minute...');

    // Use Structured Outputs to strictly enforce the JSON format
    const response = await ai.models.generateContent({
        model: 'gemini-2.5-flash',
        contents: prompt,
        config: {
            responseMimeType: "application/json",
            responseSchema: {
                type: Type.OBJECT,
                properties: {
                    practice: {
                        type: Type.ARRAY,
                        description: "Exactly 35 practice questions",
                        items: {
                            type: Type.OBJECT,
                            properties: {
                                q: { type: Type.STRING, description: "The question text" },
                                options: { type: Type.ARRAY, items: { type: Type.STRING }, description: "Exactly 4 options" },
                                correct: { type: Type.INTEGER, description: "0-based index of the correct option (0 to 3)" },
                                exp: { type: Type.STRING, description: "Detailed explanation of the answer" }
                            },
                            required: ["q", "options", "correct", "exp"]
                        }
                    },
                    mock: {
                        type: Type.ARRAY,
                        description: "Exactly 12 mock test questions",
                        items: {
                            type: Type.OBJECT,
                            properties: {
                                q: { type: Type.STRING },
                                options: { type: Type.ARRAY, items: { type: Type.STRING } },
                                correct: { type: Type.INTEGER },
                                exp: { type: Type.STRING }
                            },
                            required: ["q", "options", "correct", "exp"]
                        }
                    }
                },
                required: ["practice", "mock"]
            }
        }
    });

    const generatedData = JSON.parse(response.text);

    console.log(`Generated ${generatedData.practice?.length || 0} practice Qs and ${generatedData.mock?.length || 0} mock Qs.`);

    // Merge the new questions with the existing data
    existingData.practice.push(...(generatedData.practice || []));
    existingData.mock.push(...(generatedData.mock || []));

    // Write the updated data back to data.json
    fs.writeFileSync(dataPath, JSON.stringify(existingData, null, 2));
    console.log(`Successfully updated ${dataPath} with new questions!`);
}

generateQuestions().catch(console.error);