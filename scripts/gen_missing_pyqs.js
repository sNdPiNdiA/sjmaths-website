require('dotenv').config();
const { GoogleGenAI } = require('@google/genai');
const fs = require('fs');
const path = require('path');

const API_KEY = process.env.GEMINI_API_KEY;
const ai = new GoogleGenAI({ apiKey: API_KEY });

const MODELS = [
  'gemini-3.1-flash-lite'
];

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

const targetFiles = JSON.parse(fs.readFileSync('C:\\\\Users\\\\sande\\\\.gemini\\\\antigravity-ide\\\\brain\\\\21b8a75e-f11a-42b8-a02e-46e7af3ba25e\\\\scratch\\\\target_pyqs_files.json'));

const PROMPT = `Generate EXACTLY 10 highly realistic Previous Year Questions (PYQs) for UPSSSC Lower Subordinate Mains or similar UP state exams on the topic: "{topic}".
The questions should be very challenging and detailed.

Return the result as a raw JSON array of objects (NO MARKDOWN WRAPPERS) with this structure:
[
  {
    "examEn": "UPSSSC Lower Subordinate 2019",
    "examHi": "UPSSSC अवर अधीनस्थ 2019",
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
IMPORTANT: Return ONLY a valid JSON array of exactly 10 questions.`;

async function main() {
    let modelIndex = 0;
    for (let i = 0; i < targetFiles.length; i++) {
        const fileObj = targetFiles[i];
        const fullPath = fileObj.file;
        const relative = path.relative(path.join(__dirname, '..', 'upsssc-lower-mains'), fullPath);
        const parts = relative.split(path.sep);
        const subject = parts[0];
        const topicSlug = parts[1];
        
        if (!topicSlug) {
            console.log(`Skipping invalid path: ${fullPath}`);
            continue;
        }
        
        let topic = topicSlug.replace(/-/g, ' ');
        
        console.log(`\n[${i+1}/${targetFiles.length}] Processing PYQs for ${subject} - ${topic}`);
        
        const currentModel = MODELS[modelIndex];
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
                
                // Remove markdown code blocks if any
                responseText = responseText.replace(/^```json\n?/, '').replace(/```$/, '').trim();
                
                // Extract everything from the first '[' to the last ']' that follows the last '}'
                const firstBracket = responseText.indexOf('[');
                if (firstBracket !== -1) {
                    responseText = responseText.substring(firstBracket);
                }
                
                const lastBrace = responseText.lastIndexOf('}');
                if (lastBrace !== -1) {
                    const endBracket = responseText.indexOf(']', lastBrace);
                    if (endBracket !== -1) {
                        responseText = responseText.substring(0, endBracket + 1);
                    }
                }
                
                generatedQuestions = JSON.parse(responseText);
                
                if (!Array.isArray(generatedQuestions) || generatedQuestions.length === 0) {
                    throw new Error("Invalid JSON structure received");
                }
                
                if (generatedQuestions.length > 10) {
                    generatedQuestions = generatedQuestions.slice(0, 10);
                }
                
                console.log(`Successfully generated ${generatedQuestions.length} PYQs.`);
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
                <div class="practice-question-card pyq-card">
                    <div class="q-row">
                        <div class="q-num-badge">${idx + 1}</div>
                        <div class="q-body">
                            <span class="badge-pyq lang-en">${q.examEn || 'UP Exam PYQ'}</span>
                            <span class="badge-pyq lang-hi">${q.examHi || 'यूपी परीक्षा PYQ'}</span>
                            <p class="q-text lang-en">${q.qEn}</p>
                            <p class="q-text lang-hi">${q.qHi}</p>
                            <div class="q-options">`;
                
                const optsList = q.options || q.opts || q.choices || [];
                optsList.forEach(opt => {
                    htmlStr += `
                    <label class="opt-label">
                        <input type="radio" class="opt-radio" name="pyq${idx+1}_${Date.now()}" value="${opt.val || ''}">
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
            const pyqsTabStart = content.indexOf('<div id="tab-pyqs"');
            
            if (pyqsTabStart !== -1) {
                let nextSectionStart = content.indexOf('<div id="tab-', pyqsTabStart + 20);
                if (nextSectionStart === -1) {
                    nextSectionStart = content.indexOf('    <script>', pyqsTabStart);
                    if (nextSectionStart !== -1) {
                        nextSectionStart = content.lastIndexOf('</div>', nextSectionStart - 1);
                        nextSectionStart = content.lastIndexOf('</div>', nextSectionStart - 1);
                    } else {
                        nextSectionStart = content.length;
                    }
                }
                
                const beforeTab = content.substring(0, pyqsTabStart);
                const afterTab = content.substring(nextSectionStart);
                
                const newPyqsTab = `
        <div id="tab-pyqs" class="tab-content" style="display:none;">
            <div class="card-premium">
                <h2 class="card-title"><i class="fas fa-history"></i> <span class="lang-en">Previous Year Questions</span><span class="lang-hi">पिछले वर्ष के प्रश्न</span></h2>
                <div class="pyq-questions">
                    ${htmlStr}
                </div>
            </div>
        </div>
        `;
                content = beforeTab + newPyqsTab + afterTab;
                fs.writeFileSync(fullPath, content);
                console.log("Updated HTML successfully.");
            } else {
                console.log("Could not find pyqs tab.");
            }
        }
        
        console.log("Waiting 15s for rate limits...");
        await sleep(15000);
    }
}

main();
