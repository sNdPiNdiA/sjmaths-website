const fs = require('fs');
const path = require('path');
const dotenv = require('dotenv');
const { GoogleGenAI } = require('@google/genai');

dotenv.config();

const API_KEY = process.env.GEMINI_API_KEY;
if (!API_KEY) {
    console.error("❌ Error: GEMINI_API_KEY not found in .env file.");
    process.exit(1);
}

const ai = new GoogleGenAI({ apiKey: API_KEY });

const ROOT_DIR = path.join(__dirname, '..');
const CLASS11_DIR = path.join(ROOT_DIR, 'class-11-applied-mathematics');

const FORCE_OVERWRITE = true;

const topics = [
    {
        dir: "1-1-binary-numbers",
        name: "Binary Numbers",
        section: "1.1"
    },
    {
        dir: "1-2-indices-logarithm-and-antilogarithm",
        name: "Indices, Logarithm and Antilogarithm",
        section: "1.2"
    },
    {
        dir: "1-3-introduction-to-bhartiya-system-of-numeration",
        name: "Introduction to Bhartiya System of Numeration",
        section: "1.3"
    },
    {
        dir: "1-4-clocks",
        name: "Clocks",
        section: "1.4"
    },
    {
        dir: "1-5-calendar",
        name: "Calendar",
        section: "1.5"
    },
    {
        dir: "1-6-time-and-work",
        name: "Time and Work",
        section: "1.6"
    },
    {
        dir: "1-7-speed-distance-and-time",
        name: "Speed, Distance and Time",
        section: "1.7"
    },
    {
        dir: "1-8-seating-arrangement",
        name: "Seating Arrangement",
        section: "1.8"
    }
];

// Helper to make API calls using gemini-3.1-flash-lite
async function callGemini(prompt, systemInstruction = "") {
    let retries = 5;
    while (retries > 0) {
        try {
            const response = await ai.models.generateContent({
                model: 'gemini-3.1-flash-lite',
                contents: prompt,
                config: {
                    responseMimeType: "application/json",
                    systemInstruction: systemInstruction || undefined
                }
            });
            // Delay 6 seconds to respect the 15 RPM rate limit
            await new Promise(r => setTimeout(r, 6000));
            return response.text;
        } catch (e) {
            console.warn(`⚠️ Gemini API call failed... retries left: ${retries - 1}. Error: ${e.message}`);
            retries--;
            await new Promise(r => setTimeout(r, 8000));
        }
    }
    throw new Error("❌ API call failed after 5 retries");
}

function extractJsonString(rawText) {
    let cleanedText = rawText.trim();
    
    // Remove markdown code fences if present
    if (cleanedText.startsWith('```')) {
        cleanedText = cleanedText.replace(/^```[a-z]*\n/, '').replace(/\n```$/, '').trim();
    }
    
    const firstBrace = cleanedText.indexOf('{');
    const lastBrace = cleanedText.lastIndexOf('}');
    const firstBracket = cleanedText.indexOf('[');
    const lastBracket = cleanedText.lastIndexOf(']');
    
    if (firstBrace !== -1 && (firstBracket === -1 || firstBrace < firstBracket)) {
        if (lastBrace !== -1) {
            return cleanedText.substring(firstBrace, lastBrace + 1);
        }
    } else if (firstBracket !== -1) {
        if (lastBracket !== -1) {
            return cleanedText.substring(firstBracket, lastBracket + 1);
        }
    }
    return cleanedText;
}

async function callAndParseGemini(prompt, systemInstruction = "") {
    let retries = 5;
    while (retries > 0) {
        try {
            const text = await callGemini(prompt, systemInstruction);
            const cleanedText = extractJsonString(text);
            return JSON.parse(cleanedText);
        } catch (e) {
            console.warn(`⚠️ JSON Parse or fetch failed. Retrying... (${retries - 1} left). Error: ${e.message}`);
            retries--;
            await new Promise(r => setTimeout(r, 5000));
        }
    }
    throw new Error("Failed to get valid JSON from Gemini after 5 retries");
}

function formatTheoryHtml(concepts) {
    return concepts.map(c => `
        <div class="card-premium">
            <h3 class="card-title">${c.heading}</h3>
            <p class="theory-para">${c.text}</p>
            ${c.formula ? `<div class="theory-highlight">${c.formula}</div>` : ''}
            ${c.solvedExamples ? c.solvedExamples.map((ex, idx) => `
                <div class="theory-example" style="margin-top: 15px; border-left: 3px solid var(--primary); padding-left: 15px;">
                    <strong>Example ${idx + 1}:</strong> ${ex.q}
                    <details class="solution-details" style="margin-top: 5px;">
                        <summary>Show Step-by-Step Solution</summary>
                        <p class="solution-explanation">
                            ${ex.steps.map(step => `• ${step}`).join('<br>')}
                            <br><br><strong>Answer:</strong> ${ex.ans}
                        </p>
                    </details>
                </div>
            `).join('') : ''}
        </div>
    `).join('\n');
}

function formatExerciseHtml(data) {
    let html = '';
    
    // MCQs
    if (data.mcqs && data.mcqs.length > 0) {
        html += '<h3 class="exercise-section-title">Section A: Multiple Choice Questions (MCQs)</h3>';
        data.mcqs.forEach((q, idx) => {
            const name = `mcq-${Math.random().toString(36).substr(2, 9)}`;
            html += `
            <div class="practice-question-card">
                <div class="q-row">
                    <div class="q-num-badge">${idx + 1}</div>
                    <div class="q-body">
                        <p class="q-text">${q.q}</p>
                        <div class="q-options">
                            ${q.opts.map((opt, oIdx) => {
                                const ltr = ['A', 'B', 'C', 'D'][oIdx];
                                return `
                                <label class="opt-label">
                                    <input type="radio" class="opt-radio" name="${name}" value="${ltr}">
                                    <span><b>${ltr}.</b> ${opt}</span>
                                </label>`;
                            }).join('')}
                        </div>
                        <details class="solution-details">
                            <summary>Show Answer</summary>
                            <p class="solution-correct">✔ Correct: ${q.ans}</p>
                            <p class="solution-explanation">${q.sol}</p>
                        </details>
                    </div>
                </div>
            </div>`;
        });
    }

    // Assertion-Reason
    if (data.assertionReason && data.assertionReason.length > 0) {
        html += '<h3 class="exercise-section-title" style="margin-top: 2rem;">Section B: Assertion-Reason Questions</h3>';
        data.assertionReason.forEach((q, idx) => {
            const name = `ar-${Math.random().toString(36).substr(2, 9)}`;
            html += `
            <div class="practice-question-card">
                <div class="q-row">
                    <div class="q-num-badge">${idx + 1}</div>
                    <div class="q-body">
                        <p class="q-text">
                            <strong>Assertion (A):</strong> ${q.assertion}<br>
                            <strong>Reason (R):</strong> ${q.reason}<br><br>
                            <em>Directions: Choose the correct option:</em><br>
                            (A) Both A and R are true and R is the correct explanation of A.<br>
                            (B) Both A and R are true but R is not the correct explanation of A.<br>
                            (C) A is true but R is false.<br>
                            (D) A is false but R is true.
                        </p>
                        <div class="q-options">
                            ${['A', 'B', 'C', 'D'].map(ltr => `
                            <label class="opt-label">
                                <input type="radio" class="opt-radio" name="${name}" value="${ltr}">
                                <span><b>${ltr}.</b> Option ${ltr}</span>
                            </label>`).join('')}
                        </div>
                        <details class="solution-details">
                            <summary>Show Answer</summary>
                            <p class="solution-correct">✔ Correct: ${q.ans}</p>
                            <p class="solution-explanation">${q.sol}</p>
                        </details>
                    </div>
                </div>
            </div>`;
        });
    }

    // Short Answer
    if (data.shortAnswer && data.shortAnswer.length > 0) {
        html += '<h3 class="exercise-section-title" style="margin-top: 2rem;">Section C: Short Answer Questions</h3>';
        data.shortAnswer.forEach((q, idx) => {
            html += `
            <div class="practice-question-card">
                <div class="q-row">
                    <div class="q-num-badge">${idx + 1}</div>
                    <div class="q-body">
                        <p class="q-text">${q.q}</p>
                        <details class="solution-details">
                            <summary>Show Answer & Solution</summary>
                            <p class="solution-explanation">${q.sol}</p>
                        </details>
                    </div>
                </div>
            </div>`;
        });
    }

    // Long Answer
    if (data.longAnswer && data.longAnswer.length > 0) {
        html += '<h3 class="exercise-section-title" style="margin-top: 2rem;">Section D: Long Answer Questions</h3>';
        data.longAnswer.forEach((q, idx) => {
            html += `
            <div class="practice-question-card">
                <div class="q-row">
                    <div class="q-num-badge">${idx + 1}</div>
                    <div class="q-body">
                        <p class="q-text">${q.q}</p>
                        <details class="solution-details">
                            <summary>Show Answer & Solution</summary>
                            <p class="solution-explanation">${q.sol}</p>
                        </details>
                    </div>
                </div>
            </div>`;
        });
    }

    // Case-Based
    if (data.caseBased) {
        html += '<h3 class="exercise-section-title" style="margin-top: 2rem;">Section E: Case-Based Questions</h3>';
        html += `
        <div class="practice-question-card">
            <div class="q-row">
                <div class="q-num-badge">1</div>
                <div class="q-body">
                    <p class="q-text"><strong>Case Study:</strong> ${data.caseBased.passage}</p>
                    <div style="margin-left: 15px; margin-top: 10px;">
                        ${data.caseBased.subQs.map((sub, sIdx) => `
                            <p style="margin-top: 15px;"><strong>Sub-question ${sIdx + 1}:</strong> ${sub.q}</p>
                            <details class="solution-details">
                                <summary>Show Solution</summary>
                                <p class="solution-explanation">${sub.sol}</p>
                            </details>
                        `).join('')}
                    </div>
                </div>
            </div>
        </div>`;
    }

    return html;
}

async function generateTopic(topic) {
    const topicPath = path.join(CLASS11_DIR, topic.dir);
    const indexPath = path.join(topicPath, 'index.html');

    if (fs.existsSync(indexPath) && !FORCE_OVERWRITE) {
        console.log(`⏩ Skipping ${topic.name} (already exists)`);
        return;
    }

    console.log(`\n⏳ Generating content for: ${topic.name}...`);

    // Call 1: Theory
    const theoryPrompt = `You are a CBSE Class 11 Applied Mathematics professor.
Generate detailed concepts and theory with stepwise solved examples for the topic: "${topic.name}" under Unit 1.
The content must be written strictly only in English. Do not include any Hindi translation.
Return ONLY a JSON object with fields:
{
  "descriptionEn": "Brief English description/summary of this topic for SEO",
  "concepts": [
    {
      "heading": "Heading of Key Concept",
      "text": "Detailed pedagogical explanation of this concept",
      "formula": "Key formulas or properties format like markdown/LaTeX if applicable, otherwise plain text",
      "solvedExamples": [
         {
           "q": "Example Question statement",
           "steps": [
             "Step 1...",
             "Step 2..."
           ],
           "ans": "Final answer statement"
         }
      ]
    }
  ]
}`;

    const theoryData = await callAndParseGemini(theoryPrompt, "You output ONLY valid JSON.");
    const theoryHtml = formatTheoryHtml(theoryData.concepts);

    // Call 2: Practice
    const practicePrompt = `For the CBSE Class 11 Applied Mathematics topic "${topic.name}", generate a structured Practice Exercise.
Must contain sections:
- Section A: Multiple Choice Questions (MCQs) - 3 questions
- Section B: Assertion-Reason Questions - 2 questions (with statements for Assertion and Reason, and correct option choice A, B, C, D)
- Section C: Short Answer Questions - 2 questions
- Section D: Long Answer Questions - 2 questions (detailed multi-step calculations/proofs)
- Section E: Case-Based Questions - 1 Case Study passage with 2 sub-questions.
The content must be strictly only in English. Do not wrap fields in HTML inside the JSON, keep them as clean text.
Return ONLY a JSON object with fields:
{
  "mcqs": [
    { "q": "Question text", "opts": ["Opt A", "Opt B", "Opt C", "Opt D"], "ans": "A", "sol": "Explanation" }
  ],
  "assertionReason": [
    { "assertion": "Assertion text", "reason": "Reason text", "ans": "A", "sol": "Explanation" }
  ],
  "shortAnswer": [
    { "q": "Question text", "sol": "Step-by-step solution" }
  ],
  "longAnswer": [
    { "q": "Question text", "sol": "Detailed step-by-step solution" }
  ],
  "caseBased": {
    "passage": "Case Study Context/Passage",
    "subQs": [
      { "q": "Sub-question text", "sol": "Solution explanation" }
    ]
  }
}`;

    const practiceData = await callAndParseGemini(practicePrompt, "You output ONLY valid JSON.");
    const practiceHtml = formatExerciseHtml(practiceData);

    // Call 3: Worksheet
    const worksheetPrompt = `For the CBSE Class 11 Applied Mathematics topic "${topic.name}", generate a structured Worksheet.
Must contain sections:
- Section A: Multiple Choice Questions (MCQs) - 3 questions
- Section B: Assertion-Reason Questions - 2 questions (with statements for Assertion and Reason, and correct option choice A, B, C, D)
- Section C: Short Answer Questions - 2 questions
- Section D: Long Answer Questions - 2 questions
- Section E: Case-Based Questions - 1 Case Study passage with 2 sub-questions.
The content must be strictly only in English. Do not wrap fields in HTML inside the JSON, keep them as clean text.
Return ONLY a JSON object of the same structure as the previous exercise.`;

    const worksheetData = await callAndParseGemini(worksheetPrompt, "You output ONLY valid JSON.");
    const worksheetHtml = formatExerciseHtml(worksheetData);

    // Call 4: Quiz Questions (10 questions of mixed types)
    const quizPrompt = `Generate a set of 10 multiple choice questions for the topic: "${topic.name}" to serve as a mini test.
The questions must be structured as follows:
- Q1 to Q4: Standard Multiple Choice Questions (MCQs)
- Q5 & Q6: Assertion-Reason MCQs (Question text must contain Assertion (A) and Reason (R), and standard options: A, B, C, D)
- Q7 & Q8: Short/Numeric MCQs
- Q9 & Q10: Case-Based MCQs (both sharing the same Case Study passage. Question text should start with '**Case Study:** [Passage]' followed by the sub-question)
The content must be strictly only in English.
Each question should have:
- qEn: question text in English
- optsEn: array of 4 choices in English
- ans: correct choice letter (A, B, C, or D)
- solEn: step-by-step solution in English
Return ONLY a JSON array of 10 objects. Do not wrap in markdown code blocks.`;

    const quizData = await callAndParseGemini(quizPrompt, "You output ONLY a valid JSON array.");

    // Normalize for the engine (fill in empty fields to prevent errors)
    const normalizedQuizData = quizData.map(q => ({
        qEn: q.qEn,
        qHi: q.qEn,
        optsEn: q.optsEn,
        optsHi: ["", "", "", ""],
        ans: q.ans,
        solEn: q.solEn,
        solHi: ""
    }));

    // Construct final HTML content
    const htmlTemplate = `<!DOCTYPE html>
<html lang="en">
<head>
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-7924751316191829" crossorigin="anonymous"></script>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${topic.name} - Class 11 Applied Mathematics | SJMaths</title>
    <meta name="description" content="${theoryData.descriptionEn}">
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700;800&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/assets/vendor/fontawesome/css/all.min.css">
    <link rel="stylesheet" href="/assets/css/main.min.css">
    <link rel="stylesheet" href="/assets/css/layout.min.css">
    <link rel="stylesheet" href="/assets/css/component.min.css">
    <link rel="stylesheet" href="/assets/css/improved-ui.min.css">
    <link rel="stylesheet" href="/assets/css/topic-details.min.css">
    <link rel="stylesheet" href="/assets/css/upsssc-lower.min.css">
    
    <!-- MathJax for rendering equations -->
    <script>
    window.MathJax = {
      tex: {
        inlineMath: [['$', '$'], ['\\\\(', '\\\\)']],
        displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']],
        processEscapes: true,
        processEnvironments: true
      },
      options: {
        skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre']
      }
    };
    </script>
    <script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js" id="MathJax-script" async></script>
</head>
<body>
    <!-- Dynamic Header Container -->
    <div id="header-container"></div>
    
    <div class="container">
        <div class="breadcrumbs">
            <div class="breadcrumbs-path">
                <a href="../index.html">Syllabus</a>
                <i class="fas fa-chevron-right"></i>
                <a href="../index.html#unit-1">Numbers & Quantification</a>
                <i class="fas fa-chevron-right"></i>
                <span>${topic.name}</span>
            </div>
        </div>

        <div class="topic-header">
            <h1>${topic.name}</h1>
            <p>${theoryData.descriptionEn}</p>
        </div>

        <div class="subject-nav">
            <button class="sub-nav-item active" data-tab="theory">
                <span>Theory & Concepts</span>
            </button>
            <button class="sub-nav-item" data-tab="practice">
                <span>Practice Questions</span>
            </button>
            <button class="sub-nav-item" data-tab="worksheet">
                <span>Worksheets</span>
            </button>
            <button class="sub-nav-item" data-tab="test">
                <span>10-Q Mini Test</span>
            </button>
        </div>

        <div class="topic-content">
            <!-- Theory Tab -->
            <div id="tab-theory" class="tab-content" style="display:block">
                ${theoryHtml}
                <div class="next-tab-btn-container">
                    <button class="next-tab-btn" data-tab="practice" onclick="switchTab('practice')">
                        <span>Next: Practice Questions</span>
                        <i class="fas fa-arrow-right"></i>
                    </button>
                </div>
            </div>

            <!-- Practice Tab -->
            <div id="tab-practice" class="tab-content" style="display:none">
                ${practiceHtml}
                <div class="next-tab-btn-container">
                    <button class="next-tab-btn" data-tab="worksheet" onclick="switchTab('worksheet')">
                        <span>Next: Worksheets</span>
                        <i class="fas fa-arrow-right"></i>
                    </button>
                </div>
            </div>

            <!-- Worksheet Tab -->
            <div id="tab-worksheet" class="tab-content" style="display:none">
                ${worksheetHtml}
                <div class="next-tab-btn-container">
                    <button class="next-tab-btn" data-tab="test" onclick="switchTab('test')">
                        <span>Next: 10-Q Mini Test</span>
                        <i class="fas fa-arrow-right"></i>
                    </button>
                </div>
            </div>

            <!-- Test Tab -->
            <div id="tab-test" class="tab-content" style="display:none">
                <div class="test-container">
                    <div class="card-premium" style="margin-bottom: 2rem;">
                        <h4 class="card-title">Dynamic Test Generator (Gemini Powered)</h4>
                        <p style="font-size: 0.9rem; margin-bottom: 1rem;">
                            Enter your Gemini API Key to generate a dynamic test in real-time with MCQs, Assertion-Reason, and Case-Based questions. If you do not have a key, click "Use Static Test" below to load pre-generated questions instead.
                        </p>
                        <div style="display: flex; gap: 10px; flex-wrap: wrap; margin-bottom: 1rem;">
                            <input type="password" id="gemini-api-key-input" placeholder="Enter Gemini API Key (AIzaSy...)" style="padding: 10px; border: 1px solid var(--border); border-radius: 8px; flex-grow: 1; font-family: inherit; background: var(--card-bg); color: var(--text);">
                            <button onclick="saveApiKey()" style="padding: 10px 20px; background: var(--primary); color: white; border: none; border-radius: 8px; cursor: pointer; font-weight: bold;">
                                Save Key
                            </button>
                        </div>
                        <div style="display: flex; gap: 10px;">
                            <button id="gen-dynamic-btn" onclick="generateDynamicTest()" style="padding: 10px 20px; background: #3498db; color: white; border: none; border-radius: 8px; cursor: pointer; font-weight: bold; display: none;">
                                Generate Dynamic Test
                            </button>
                            <button onclick="loadStaticTest()" style="padding: 10px 20px; background: #7f8c8d; color: white; border: none; border-radius: 8px; cursor: pointer; font-weight: bold;">
                                Use Static Test
                            </button>
                        </div>
                    </div>

                    <div id="test-start-scr">
                        <p class="test-desc">This test contains 10 multiple-choice questions (including MCQs, Assertion-Reason, and Case-Based questions). You have 10 minutes to complete the test.</p>
                        <button class="start-test-btn" onclick="startTest()">
                            Start Test
                        </button>
                    </div>

                    <div id="test-area" style="display:none">
                        <div class="test-hdr">
                            <div>Time Left</div>
                            <div class="test-tmr" id="tmr-display">10:00</div>
                        </div>
                        <div class="test-prog-bar"><div class="test-prog-fill" id="prog-fill" style="width:0%"></div></div>
                        <div id="test-questions"></div>
                        <div style="text-align:center;margin:24px 0">
                            <button onclick="submitTest()" id="submit-btn" style="padding:13px 38px;background:linear-gradient(135deg,#27ae60,#2ecc71);color:white;border:none;border-radius:30px;font-size:1.1rem;font-weight:700;cursor:pointer;box-shadow:0 8px 20px rgba(39,174,96,0.4);">
                                <i class="fas fa-paper-plane"></i> Submit Test
                            </button>
                        </div>
                    </div>

                    <div class="test-result" id="test-result" style="display:none">
                        <div style="font-size:1.3rem"><i class="fas fa-trophy"></i> Test Complete!</div>
                        <div class="result-score" id="res-score">0/10</div>
                        <div id="res-label" style="font-size:1rem;opacity:0.9;margin-bottom:5px"></div>
                        <div class="grade-bdg" id="res-grade"></div>
                        <div style="margin-top:18px">
                            <button class="tact-btn" onclick="retakeTest()" style="background:#059669;color:white"><i class="fas fa-redo"></i> Retake</button>
                            <button class="tact-btn" data-tab="practice" onclick="switchTab('practice')" style="background:white;color:#059669"><i class="fas fa-book"></i> Practice More</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Dynamic Footer Container -->
    <div id="footer-container"></div>
    
    <script>
        // Static test data generated by the build script
        window.staticTestData = ${JSON.stringify(normalizedQuizData)};
        window.upssscTestData = []; // Active test data
    </script>
    
    <script src="/assets/js/search.min.js" defer></script>
    <script src="/assets/js/main.min.js" defer></script>
    <script src="/assets/js/global-header.min.js" defer></script>
    <script src="/assets/js/global-footer.min.js" defer></script>
    <script src="/assets/js/upsssc-lower.min.js" defer></script>
    
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const keyInput = document.getElementById('gemini-api-key-input');
            const dynamicBtn = document.getElementById('gen-dynamic-btn');
            
            const savedKey = localStorage.getItem('gemini-api-key');
            if (savedKey) {
                keyInput.value = savedKey;
                dynamicBtn.style.display = 'inline-block';
            }
            
            // Set static as default
            window.upssscTestData = JSON.parse(JSON.stringify(window.staticTestData));
            renderTestQuestions(window.upssscTestData);
        });

        function saveApiKey() {
            const key = document.getElementById('gemini-api-key-input').value.trim();
            if (key) {
                localStorage.setItem('gemini-api-key', key);
                document.getElementById('gen-dynamic-btn').style.display = 'inline-block';
                alert('API Key saved successfully!');
            } else {
                localStorage.removeItem('gemini-api-key');
                document.getElementById('gen-dynamic-btn').style.display = 'none';
                alert('API Key cleared.');
            }
        }

        function loadStaticTest() {
            window.upssscTestData = JSON.parse(JSON.stringify(window.staticTestData));
            renderTestQuestions(window.upssscTestData);
            alert('Loaded static pre-generated test questions.');
        }

        function renderTestQuestions(data) {
            const container = document.getElementById('test-questions');
            container.innerHTML = '';
            
            data.forEach((q, idx) => {
                const qBlock = document.createElement('div');
                qBlock.className = 'test-qblock';
                qBlock.id = \`tq-\${idx}\`;
                
                // Parse markdown-like syntax for pretty display
                let formattedText = q.qEn
                    .replace(/\\*\\*Assertion \\(A\\):\\*\\*/g, '<strong>Assertion (A):</strong>')
                    .replace(/\\*\\*Reason \\(R\\):\\*\\*/g, '<strong>Reason (R):</strong>')
                    .replace(/\\*\\*Case Study:\\*\\*/g, '<strong>Case Study:</strong>')
                    .replace(/\\n/g, '<br>');

                qBlock.innerHTML = \`
                    <p class="test-qtext">
                        <span class="test-qnum">Q\${idx + 1}</span>
                        <span style="display:block;margin-top:6px">
                            <span>\${formattedText}</span>
                        </span>
                    </p>
                    <div class="test-opts-grid">
                        <div class="test-opt" data-qi="\${idx}" data-ch="A" onclick="selOpt(this)">
                            <span class="opt-ltr">A</span>
                            <span>\${q.optsEn[0]}</span>
                        </div>
                        <div class="test-opt" data-qi="\${idx}" data-ch="B" onclick="selOpt(this)">
                            <span class="opt-ltr">B</span>
                            <span>\${q.optsEn[1]}</span>
                        </div>
                        <div class="test-opt" data-qi="\${idx}" data-ch="C" onclick="selOpt(this)">
                            <span class="opt-ltr">C</span>
                            <span>\${q.optsEn[2]}</span>
                        </div>
                        <div class="test-opt" data-qi="\${idx}" data-ch="D" onclick="selOpt(this)">
                            <span class="opt-ltr">D</span>
                            <span>\${q.optsEn[3]}</span>
                        </div>
                    </div>
                    <input type="hidden" id="tans-\${idx}" value="\${q.ans}">
                    <input type="hidden" id="tsel-\${idx}" value="">
                \`;
                container.appendChild(qBlock);
            });
        }

        async function generateDynamicTest() {
            const apiKey = localStorage.getItem('gemini-api-key');
            if (!apiKey) {
                alert('Please enter and save your Gemini API Key first.');
                return;
            }
            
            const btn = document.getElementById('gen-dynamic-btn');
            btn.disabled = true;
            btn.textContent = 'Generating...';
            
            const prompt = \`Generate a 10-question multiple choice test for CBSE Class 11 Applied Mathematics on the topic: "${topic.name}". Structure it exactly: Q1-Q4 MCQs, Q5-Q6 Assertion-Reason, Q7-Q8 Numeric MCQs, Q9-Q10 Case-Based MCQs. Respond ONLY with a valid JSON array of objects, with no markdown code block formatting. Each object MUST have the exact structure: {"qEn": "Question in English", "optsEn": ["A", "B", "C", "D"], "ans": "A", "solEn": "English solution"}\`;

            try {
                const response = await fetch(\`https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-lite:generateContent?key=\${apiKey}\`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        contents: [{ parts: [{ text: prompt }] }],
                        generationConfig: { responseMimeType: "application/json" }
                    })
                });
                
                const result = await response.json();
                const text = result.candidates[0].content.parts[0].text;
                const quizData = JSON.parse(text);
                
                if (Array.isArray(quizData) && quizData.length > 0) {
                    window.upssscTestData = quizData.map(q => ({
                        qEn: q.qEn,
                        qHi: q.qEn,
                        optsEn: q.optsEn,
                        optsHi: ["", "", "", ""],
                        ans: q.ans,
                        solEn: q.solEn,
                        solHi: ""
                    }));
                    renderTestQuestions(window.upssscTestData);
                    alert('Successfully generated and loaded a fresh 10-Question Dynamic Test!');
                } else {
                    throw new Error('Invalid JSON format received');
                }
            } catch (err) {
                console.error(err);
                alert('Failed to generate dynamic test: ' + err.message + '. Falling back to static test.');
                loadStaticTest();
            } finally {
                btn.disabled = false;
                btn.textContent = 'Generate Dynamic Test';
            }
        }
    </script>
</body>
</html>`;

    // Create directories
    fs.mkdirSync(topicPath, { recursive: true });
    fs.writeFileSync(indexPath, htmlTemplate, 'utf8');
    console.log(`✅ Saved: ${indexPath}`);
}

async function main() {
    console.log("🚀 Starting structured textbook-style English-only Unit 1 content generation with gemini-3.1-flash-lite...");
    for (const topic of topics) {
        try {
            await generateTopic(topic);
        } catch (e) {
            console.error(`❌ Error generating ${topic.name}:`, e.message);
            console.log("Waiting 5 seconds before retrying...");
            await new Promise(r => setTimeout(r, 5000));
        }
        // Small delay between topics to respect rate limits
        await new Promise(r => setTimeout(r, 2000));
    }
    console.log("🎉 All Unit 1 content generated successfully!");
}

main();
