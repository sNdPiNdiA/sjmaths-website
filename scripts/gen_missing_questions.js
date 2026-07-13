require('dotenv').config();
const { GoogleGenAI } = require('@google/genai');
const fs = require('fs');
const path = require('path');

const API_KEY = process.env.GEMINI_API_KEY;
const ai = new GoogleGenAI({ apiKey: API_KEY });

const MODELS = [
  'gemini-3.1-flash-lite'
];
const RPM = 5; 
const DELAY_MS = 15000; 

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

const targetFiles = JSON.parse(fs.readFileSync('C:\\\\Users\\\\sande\\\\.gemini\\\\antigravity-ide\\\\brain\\\\21b8a75e-f11a-42b8-a02e-46e7af3ba25e\\\\scratch\\\\target_files.json'));

const PROMPT = `Generate EXACTLY 30 high-level exam practice questions for UPSSSC Lower Subordinate Mains on the topic: "{topic}".
The questions should be very challenging and detailed.

Return the result as a raw JSON array of objects (NO MARKDOWN WRAPPERS) with this structure:
[
  {
    "qEn": "Question text in English",
    "qHi": "Question text in Hindi",
    "options": [
      { "optEn": "Option A in Eng", "optHi": "Option A in Hi", "val": "A" },
      { "optEn": "Option B in Eng", "optHi": "Option B in Hi", "val": "B" },
      { "optEn": "Option C in Eng", "optHi": "Option C in Hi", "val": "C" },
      { "optEn": "Option D in Eng", "optHi": "Option D in Hi", "val": "D" }
    ],
    "correct": "A",
    "solEn": "Detailed solution in English",
    "solHi": "Detailed solution in Hindi"
  }
]
IMPORTANT: Return ONLY a valid JSON array of exactly 30 questions. Do not wrap in \`\`\`json.`;

async function main() {
    let modelIndex = 0;
    for (let i = 0; i < targetFiles.length; i++) {
        const fileObj = targetFiles[i];
        const fullPath = fileObj.file;
        const relative = path.relative(path.join(__dirname, '..', 'upsssc-lower-mains'), fullPath);
        const parts = relative.split(path.sep);
        const subject = parts[0];
        const topicSlug = parts[1];
        
        let topic = topicSlug.replace(/-/g, ' ');
        
        console.log(`\n[${i+1}/${targetFiles.length}] Processing ${subject} - ${topic}`);
        
        let content = fs.readFileSync(fullPath, 'utf8');
        const practiceTabStart = content.indexOf('<div id="tab-practice" class="tab-content"');
        if (practiceTabStart !== -1) {
            const practiceTabEnd = content.indexOf('<div id="tab-pyqs" class="tab-content"');
            if(practiceTabEnd !== -1) {
                const practiceSection = content.substring(practiceTabStart, practiceTabEnd);
                const count = (practiceSection.match(/class="practice-question-card"/g) || []).length;
                if (count === 30) {
                    console.log(`Skipping - already has exactly 30 questions.`);
                    continue;
                }
            }
        }
        
        const currentModel = MODELS[modelIndex];
        console.log(`Using model: ${currentModel}`);
        
        let generatedQuestions = null;
        let retries = 0;
        
        while (retries < 3) {
            try {
                const response = await ai.models.generateContent({
                    model: currentModel,
                    contents: PROMPT.replace('{topic}', `${subject} - ${topic}`),
                    config: {
                        responseMimeType: "application/json",
                    }
                });
                let responseText = response.text || "";
                const match = responseText.match(/\[\s*\{[\s\S]*\}\s*\]/);
                if (match) {
                    responseText = match[0];
                }
                
                generatedQuestions = JSON.parse(responseText);
                
                if (!Array.isArray(generatedQuestions) || generatedQuestions.length === 0) {
                    throw new Error("Invalid JSON structure received");
                }
                
                if (generatedQuestions.length > 30) {
                    generatedQuestions = generatedQuestions.slice(0, 30);
                }
                
                console.log(`Successfully generated ${generatedQuestions.length} questions.`);
                break;
            } catch (err) {
                console.error(`Error generating (Attempt ${retries+1}):`, err.message);
                retries++;
                console.log("Sleeping 10s before retry...");
                await sleep(10000);
            }
        }
        
        if (generatedQuestions) {
            let htmlStr = '';
            generatedQuestions.forEach((q, idx) => {
                htmlStr += `
                <div class="practice-question-card">
                    <div class="q-row">
                        <div class="q-num-badge">${idx + 1}</div>
                        <div class="q-body">
                            <p class="q-text lang-en">${q.qEn}</p>
                            <p class="q-text lang-hi">${q.qHi}</p>
                            <div class="q-options">`;
                
                const optsList = q.options || q.opts || q.choices || [];
                optsList.forEach(opt => {
                    htmlStr += `
                    <label class="opt-label">
                        <input type="radio" class="opt-radio" name="q${idx+1}_${Date.now()}" value="${opt.val || ''}">
                        <span class="lang-en"><b>${opt.val || ''}.</b> ${opt.optEn || opt.en || ''}</span>
                        <span class="lang-hi"><b>${opt.val || ''}.</b> ${opt.optHi || opt.hi || ''}</span>
                    </label>`;
                });
                
                htmlStr += `
                            </div>
                            <details class="solution-details">
                                <summary class="lang-en">Show Answer</summary>
                                <summary class="lang-hi">उत्तर देखें</summary>
                                <p class="solution-correct lang-en">✔ Correct: ${q.correct}</p>
                                <p class="solution-correct lang-hi">✔ सही उत्तर: ${q.correct}</p>
                                <p class="lang-en">${q.solEn}</p>
                                <p class="lang-hi">${q.solHi}</p>
                            </details>
                        </div>
                    </div>
                </div>`;
            });
            
            let content = fs.readFileSync(fullPath, 'utf8');
            const practiceTabStart = content.indexOf('<div id="tab-practice" class="tab-content"');
            if (practiceTabStart !== -1) {
                const practiceTabEnd = content.indexOf('<div id="tab-pyqs" class="tab-content"');
                if(practiceTabEnd !== -1) {
                    const beforeTab = content.substring(0, practiceTabStart);
                    const afterTab = content.substring(practiceTabEnd);
                    const newPracticeTab = `
        <div id="tab-practice" class="tab-content" style="display:none;">
            <div class="card-premium">
                <h2 class="card-title"><i class="fas fa-edit"></i> <span class="lang-en">Practice Questions</span><span class="lang-hi">अभ्यास प्रश्न</span></h2>
                <div class="practice-questions">
                    ${htmlStr}
                </div>
                <div class="next-tab-btn-container">
                    <button class="next-tab-btn" data-tab="pyqs" onclick="switchTab('pyqs')">
                        <span class="lang-en">Next: UP Gov PYQs</span>
                        <span class="lang-hi">अगला: यूपी सरकार PYQs</span>
                        <i class="fas fa-arrow-right"></i>
                    </button>
                </div>
            </div>
        </div>
        `;
                    content = beforeTab + newPracticeTab + afterTab;
                    fs.writeFileSync(fullPath, content);
                    console.log("Updated HTML successfully.");
                } else {
                    console.log("Could not find next tab (pyqs).");
                }
            } else {
                console.log("Could not find practice tab.");
            }
        }
        
        modelIndex = (modelIndex + 1) % MODELS.length;
        console.log(`Waiting ${DELAY_MS/1000}s for rate limits...`);
        await sleep(DELAY_MS);
    }
}
main();
